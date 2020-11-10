import requests

requests.packages.urllib3.disable_warnings()


def execute_rest(method, url, bearertoken, payload):
    if bearertoken:
        headers = {
            'Authorization': 'BEARER ' + bearertoken + '',
            'Content-Type': 'application/json'
        }
    else:
        headers = {
            'Content-Type': 'application/json'
        }
    response = requests.request(
        method, url, headers=headers, data=payload, verify=False)
    json = response.json()  # type: object

    return json


def refresh_access_token(appliance_name, client_id, refresh_token):
    method = 'POST'
    url = "https://" + appliance_name + "/oauth/token?grant_type=refresh_token&client_id=" + client_id + "&scope=write"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'refresh_token=' + refresh_token + ''

    response = requests.request(
        method, url, headers=headers, data=payload, verify=False)
    json = response.json()  # type: object

    return json


def get_current_token(appliance_name, client_id, username, password):
    method = 'POST'
    url = "https://" + appliance_name + "/oauth/token?grant_type=password&client_id=" + client_id + "&scope=write"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'username=' + username + '&password=' + password + ''

    response = requests.request(
        method, url, headers=headers, data=payload, verify=False)
    json = response.json()  # type: object

    return json


def create_cypher(secret_value, secret_name, appliance_name, token):
    url = "https://" + appliance_name + "/api/cypher/secret/" + secret_name + "?value=" + secret_value + "&type=string"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token + ''
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text.encode('utf8'))
