
import requests
from datetime import datetime

FIREWALL_IP = "10.10.10.10"
API_KEY = "replace-api-key"

url = f"https://{FIREWALL_IP}/api/v2/monitor/system/config/backup"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

try:
    response = requests.get(
        url,
        headers=headers,
        verify=False,
        timeout=20
    )

    if response.status_code == 200:

        file_name = f"firewall_backup_{datetime.now().strftime('%Y%m%d')}.conf"

        with open(file_name, "wb") as f:
            f.write(response.content)

        print("Backup completed successfully")
        print(f"Saved backup from {FIREWALL_IP}")
        print(file_name)

    else:
        print("Backup request failed")
        print(response.status_code)

except Exception as err:
    print("Unexpected error")
    print(err)
