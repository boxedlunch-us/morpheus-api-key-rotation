import sys
from morph_api_tomcart import refresh_access_token, create_cypher, get_current_token

# command line arguments - required
appliance_name = sys.argv[1]
client_id = sys.argv[2]  # morph-api, morph-automation, morph-cli, morph-customer
username = sys.argv[3]
password = sys.argv[4]

# get current bearer token using on username/password
current = get_current_token(appliance_name, client_id, username, password)
response = refresh_access_token(appliance_name, client_id, current['refresh_token'])

new_bearer = response['access_token']
new_refresh = response['refresh_token']

# create/update cypher entry for access/bearer token
create_cypher(new_bearer, "access_token", appliance_name, new_bearer)
