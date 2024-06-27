import base64

PORT_NUMBER="<port>"
USERNAME_PASSWORD="riot:<password>"

BASE_URL=f"https://127.0.0.1:{PORT_NUMBER}"
ENCODED=base64.b64encode(USERNAME_PASSWORD.encode("ascii")).decode("ascii")
AUTHENTICATION=f"Basic {ENCODED}"
