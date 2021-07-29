def over_lapping():
    import requests
    import pandas as pd
    import re
    from bs4 import BeautifulSoup
    import time
    import datetime

    r= requests.get('https://trends24.in/pakistan/')
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html5lib')
    time1 = soup.find_all('h5', class_ = "trend-card__time")[1]
    time2 = soup.find_all('h5', class_ = "trend-card__time")[2]

    onlyTime1=time1.get_text().split(' ').pop()
    onlyTime2=time2.get_text().split(' ').pop()

    def get_sec(time_str):
        """Get Seconds from time."""
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(s)


    secondResult = int(get_sec(onlyTime1)) - int(get_sec(onlyTime2))
    result = []
    result.append(secondResult)
    df = pd.DataFrame(result)
    df.to_csv('~/store_files_airflow/No3.csv', index= False)