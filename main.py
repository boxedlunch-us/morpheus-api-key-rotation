import sys
# from morph_api_tomcart import execute_rest, await_job_exec_status
from api import execute_rest, refresh_access_token, create_cypher, get_current_token

appliance_name = "192.168.1.162"
client_id = "morph-customer"
url = "https://" + appliance_name + "/oauth/token?grant_type=refresh_token&client_id=" + client_id + "&scope=write"
username = sys.argv[1]
password = sys.argv[2]
current = get_current_token(appliance_name, client_id, username, password)

response = refresh_access_token(appliance_name, client_id, current['refresh_token'])

new_bearer = response['access_token']
new_refresh = response['refresh_token']

# create/update cypher entry for access/bearer token
create_cypher(new_bearer, "accesstoken", appliance_name, new_bearer)

# # create/update cypher entry for refresh token
# create_cypher(new_refresh, "refreshtoken", appliance_name, new_bearer)
