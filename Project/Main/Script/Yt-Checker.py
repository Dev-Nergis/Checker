import json
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

id = input('ID: ')
if "watch?v=" in id:
    vid = id.split("watch?v=")[1]
else:
    vid = id

r = requests.get(f"https://returnyoutubedislikeapi.com/votes?videoId={vid}")

if (r.status_code == requests.codes.ok):
    vd = r.json()
    print("결과: \n비디오 ID: %s \n올라온 날자: %s \n좋아요: %s \n싫어요: %s \n조회수: %s " % (vd["id"], vd["dateCreated"], vd["likes"], vd["dislikes"], vd["viewCount"]))

input("Please press the Enter key to exit")
