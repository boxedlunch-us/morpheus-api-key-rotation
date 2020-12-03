import sys
from morph_api_tomcart import refresh_access_token, create_cypher, days_until_expire

# TODO: push API check
# TODO: check key expiration duration
# TODO: motd countdown

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

expiry = days_until_expire(appliance_name, "access_token", access_token)
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

