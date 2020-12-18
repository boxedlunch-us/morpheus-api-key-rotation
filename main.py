import sys
import yaml
from morph_api_tomcart import refresh_access_token, create_cypher, days_until_expire, execute_rest, \
    execute_rest_no_bearer

from morpheuscypher import Cypher
# TODO: Single notification on threshold meet
# TODO: - deferred: Restructure morph_api package - too many functions; classes to separate logical constructs
#       a. critical error message standardization - custom error classes
# TODO: If any command arguments are null - error
# TODO: rollback if cypher writes fail
# TODO: Config file - arguments are too numerous

# command line args
access_token = sys.argv[1]
refresh_token = sys.argv[2]

# load parameters from config file
with open("config.yaml", "r") as yaml_config:
    cfg = yaml.load(yaml_config, Loader=yaml.FullLoader)

appliance_name = cfg['appliance']['name']
client_id = cfg['api']['client_id']
critical_check_apikey = cfg['monitoring']['critical_check_apikey']
warning_check_apikey = cfg['monitoring']['warning_check_apikey']
lease_duration = cfg['api']['lease']

critical_payload = '{"success":false, "message": "Critical error message"}'
warning_payload = '{"success":false, "message": "Warning error message"}'
success_payload = '{"success":true, "message": "Healthy message"}'


def push_api(payload, api_key):
    push_api_url = "https://" + appliance_name + "/api/monitoring/push?apiKey=" + api_key
    execute_rest_no_bearer("POST", push_api_url, payload)


# CRITICAL: Check to see if there is access to Morpheus API
whoami_url = "https://" + appliance_name + "/api/whoami"
try:
    api_check = execute_rest("GET", whoami_url, access_token, "")
    if "error" in api_check.keys():
        error_desc = api_check['error_description']
        raise KeyError

except KeyError:
    # TODO: Account for PushAPI failures
    push_api(critical_payload, critical_check_apikey)
    sys.exit("Unable to verify access to the API. " + error_desc)

# CRITICAL: Check for missing cypher entries - mainly refresh as we wouldn't make it this far without access token
secret_name = 'refresh_token'
cypher_url = "https://" + appliance_name + "/api/cypher/secret/" + secret_name
try:
    entry_check = execute_rest("GET", cypher_url, access_token, "")
    if not entry_check['success']:
        raise ValueError


except ValueError:
    push_api(critical_payload, critical_check_apikey)
    sys.exit("Unable to retrieve Cypher entry for " + secret_name)

# Check for remaining days on Cypher lease
# 7 days pushes warning to api
# 1 or fewer rotates and pushes success to api upon completion
expiry = days_until_expire(appliance_name, "access_token", access_token)

if expiry <= 1:
    print("Rotating access token and updating API key")

    # New tokens to be passed on
    try:
        response = refresh_access_token(appliance_name, client_id, refresh_token)
        if "error" in response.keys():
            raise ValueError
    except ValueError:
        push_api(critical_payload, critical_check_apikey)
        sys.exit("Unable to rotate key due to: " + response['error'])

    new_bearer = response['access_token']
    new_refresh = response['refresh_token']

    # create/update cypher entry for access/bearer token
    # TODO: Lease duration as argument
    create_cypher(new_bearer, "access_token", appliance_name, new_bearer, lease_duration)
    create_cypher(new_refresh, "refresh_token", appliance_name, new_bearer, lease_duration)
    push_api(success_payload, warning_check_apikey)
    push_api(success_payload, critical_check_apikey)
elif expiry <= 7:
    print("Key expires in 7 days or less.")
    # TODO: Removal of extraneous pushAPI
    push_api(warning_payload, warning_check_apikey)
    push_api(success_payload, critical_check_apikey)
else:
    print("API key has not yet expired. " + str(expiry) + " days remaining on lease.")
    push_api(success_payload, warning_check_apikey)
    push_api(success_payload, critical_check_apikey)
