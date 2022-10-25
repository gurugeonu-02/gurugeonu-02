import request
from bs4 import BeautifulSoup as bs
import pandas as pd

filename = "datas.csv"

for i in range(1000, 25904):
    page = requests.get("https://www.acmicpc.net/problem/"+str(i))
    if page.status_code != 200:
        continue
    soup = bs(page.text, "html.parser")
    val = soup.find_all('td')
    print(val)
    #012345 => X X 제출 정답 맞힌사람 정답비율
