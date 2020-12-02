import sys
from morph_api_tomcart import refresh_access_token, create_cypher
# TODO: push API check
# TODO: check key expiration duration
# TODO: motd countdown
#


# command line arguments - required
appliance_name = sys.argv[1]
client_id = sys.argv[2]  # morph-api, morph-automation, morph-cli, morph-customer
refresh_token = sys.argv[3]

# get current bearer token using on username/password
response = refresh_access_token(appliance_name, client_id, refresh_token)
print(response)
new_bearer = response['access_token']
new_refresh = response['refresh_token']

# create/update cypher entry for access/bearer token
create_cypher(new_bearer, "access_token", appliance_name, new_bearer)
create_cypher(new_refresh, "refresh_token", appliance_name, new_bearer)
