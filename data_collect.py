import request
from bs4 import BeautifulSoup as bs
import pandas as pd

filename = "datas.csv"

li = []

for i in range(1000, 25904):
    page = requests.get("https://www.acmicpc.net/problem/"+str(i))
    if page.status_code != 200: continue;
    soup = bs(page.text, "html.parser")
    val = soup.find_all('td')
    ret = [val[1], val[2], val[3], val[4]]
    if val[1] < 300: continue;
    ret.insert(0, i)
    solvedac_tier_tar = soup.find_all('td')
    solved_ac_tier = solvedac_tier_tar[2]
    solved_ac_tier = solved_ac_tier[43:-4]
    ret.insert(1, solved_ac_tier)
    li.append(val)
    # 번호, 티어, 제출 수, 정답 수, 정답자 수, 정답 비율


