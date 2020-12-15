import sys
from morph_api_tomcart import refresh_access_token, create_cypher, days_until_expire, execute_rest

# TODO: Failure conditions: lack of cypher entry, incorrect access token, incorrect refresh token
#      1. Lack of API Access - DONE
#      2. Cypher entry missing (access and/or refresh) - DONE
#      3. Incorrect refresh token
# TODO: push API check

# TODO: Setup Alert Rule - no response/bad response (job fail/connectivity)
# TODO: Single notification on threshold meet
# TODO: - deferred: additional/paralell check with differnt severitiy levelvvvlvlvlvl


# command line arguments - required
appliance_name = sys.argv[1]
client_id = sys.argv[2]  # morph-api, morph-automation, morph-cli, morph-customer
access_token = sys.argv[3]
refresh_token = sys.argv[4]


def push_api():
    execute_rest("POST", push_api_url, access_token, "")


# CRITICAL: Check to see if there is access to Morpheus API
whoami_url = "https://" + appliance_name + "/api/whoami"
try:
    api_check = execute_rest("GET", whoami_url, access_token, "")
    if "error" in api_check.keys():
        error_desc = api_check['error_description']
        raise KeyError

except KeyError:

    sys.exit("Unable to verify access to the API." + error_desc)

# CRITICAL: Check for missing cypher entries - mainly refresh as we wouldn't make it this far without access token
secret_name = 'secret/refresh_token'
cypher_url = "https://" + appliance_name + "/api/cypher/secret/" + secret_name
try:
    entry_check = execute_rest("GET", cypher_url, access_token, "")
    if not entry_check['success']:
        raise ValueError


except ValueError:

    sys.exit("Unable to retrieve Cypher entry for " + secret_name)

expiry = days_until_expire(appliance_name, "access_token", access_token)

if expiry <= 1:
    print("Rotating access token and updating API key")

    # New tokens to be passed on
    response = refresh_access_token(appliance_name, client_id, refresh_token)
    new_bearer = response['access_token']
    new_refresh = response['refresh_token']

    # create/update cypher entry for access/bearer token
    create_cypher(new_bearer, "access_token", appliance_name, new_bearer, "3d")
    create_cypher(new_refresh, "refresh_token", appliance_name, new_bearer, "3d")
else:
    print("API key has not yet expired. " + str(expiry) + " days remaining on lease.")
