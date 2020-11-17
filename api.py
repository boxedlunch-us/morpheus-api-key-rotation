import requests

requests.packages.urllib3.disable_warnings()

def get_current_token(appliance_name, client_id, access_token):
    method = 'POST'
    url = "https://" + appliance_name + "/oauth/token?grant_type=password&client_id=" + client_id + "&scope=write"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = 'refresh_token=' +  + ''

    response = requests.request(
        method, url, headers=headers, data=payload, verify=False)
    json = response.json()  # type: object

    return json