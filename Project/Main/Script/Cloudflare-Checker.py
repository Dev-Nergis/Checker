import requests
import json

r = requests.get("https://cloudflare.com/cdn-cgi/trace")

if (r.status_code == requests.codes.ok):
  print(r.text)
  data = {r.text.split("\n")[0].split("=")[0]: r.text.split("\n")[0].split("=")[1], r.text.split("\n")[1].split("=")[0]: r.text.split("\n")[1].split("=")[1], r.text.split("\n")[2].split("=")[0]: r.text.split("\n")[2].split("=")[1], r.text.split("\n")[3].split("=")[0]: r.text.split("\n")[3].split("=")[1], r.text.split("\n")[4].split("=")[0]: r.text.split("\n")[4].split("=")[1], r.text.split("\n")[5].split("=")[0]: r.text.split("\n")[5].split("=")[1], r.text.split("\n")[6].split("=")[0]: r.text.split("\n")[6].split("=")[1], r.text.split("\n")[7].split("=")[0]: r.text.split("\n")[7].split("=")[1], r.text.split("\n")[8].split("=")[0]: r.text.split("\n")[8].split("=")[1], r.text.split("\n")[9].split("=")[0]: r.text.split("\n")[9].split("=")[1], r.text.split("\n")[10].split("=")[0]: r.text.split("\n")[10].split("=")[1], r.text.split("\n")[11].split("=")[0]: r.text.split("\n")[11].split("=")[1], r.text.split("\n")[12].split("=")[0]: r.text.split("\n")[12].split("=")[1]}
  with open("rlconfig.json", "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  print("\n INFORMATION SAVE SUCCESS!. \n")

input("Please press the Enter key to exit")
