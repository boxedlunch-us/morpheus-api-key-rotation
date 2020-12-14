import sys
from morph_api_tomcart import refresh_access_token, create_cypher, days_until_expire, execute_rest

# asdf
# TODO: push API check
# TODO: check key expiration duration
# TODO: motd countdown
# 20201214
# TODO: Failure conditions: lack of cypher entry, incorrect access token, incorrect refresh token

# 20201203
# TODO: Setup Alert Rule - no response/bad response (job fail/connectivity)
# TODO: Single notification on threshold meet
# TODO: - deferred: additional/paralell check with differnt severitiy levelvvvlvlvlvl

# command line arguments - required
appliance_name = sys.argv[1]
client_id = sys.argv[2]  # morph-api, morph-automation, morph-cli, morph-customer
access_token = sys.argv[3]
refresh_token = sys.argv[4]
# get current bearer token using on username/password
whoami_url = "https://" + appliance_name + "/api/whoami"
try:
    api_check = execute_rest("GET", whoami_url, access_token, "")
    if "error" in api_check.keys():
        raise KeyError
except:
    err = sys.exc_info()
    print(err)
    sys.exit("Unable to verify access to the API.")
try:
    expiry = days_until_expire(appliance_name, "access_token", access_token)
except:
    err = sys.exc_info()
    print("Error: %s" % err[0])
    print("Error: %s" % err[1])
    sys.exit("Unable to acquire the cypher entry")

if expiry <= 1:
    print("Rotating access token and updating API key")
    response = refresh_access_token(appliance_name, client_id, refresh_token)
    new_bearer = response['access_token']
    new_refresh = response['refresh_token']

    # create/update cypher entry for access/bearer token
    create_cypher(new_bearer, "access_token", appliance_name, new_bearer, "3d")
    create_cypher(new_refresh, "refresh_token", appliance_name, new_bearer, "3d")
else:
    print("API key has not yet expired. " + str(expiry) + " days remaining on lease.")
