import requests
import json
import base64

r = requests.get("https://chromium.googlesource.com/chromium/src/+/refs/heads/main/chrome/VERSION?format=TEXT")

if r.status_code == 200:
    version_string = base64.b64decode(r.text).decode('utf-8')
    version_data = {version_string.split("\n")[0].split("=")[0]: version_string.split("\n")[0].split("=")[1], version_string.split("\n")[1].split("=")[0]: version_string.split("\n")[1].split("=")[1], version_string.split("\n")[2].split("=")[0]: version_string.split("\n")[2].split("=")[1], version_string.split("\n")[3].split("=")[0]: version_string.split("\n")[3].split("=")[1]}
    v_json = json.dumps(version_data, ensure_ascii=False, indent=4)
    v_json_data = json.loads(v_json)
    chrome_version = str(v_json_data['MAJOR']) + "." + str(v_json_data['MINOR']) + "." + str(v_json_data['BUILD']) + "." + str(v_json_data['PATCH'])
    print(f"크로미움 최신버전: {chrome_version}")
