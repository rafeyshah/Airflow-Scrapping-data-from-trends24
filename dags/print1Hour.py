def print_1_Hour():
    import requests
    import pandas as pd
    import re
    from bs4 import BeautifulSoup
    
    r= requests.get('https://trends24.in/pakistan/')
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html5lib')

    quotes=[]

    time = soup.find_all('h5', class_ = "trend-card__time")[1]
    table = soup.find_all('ol', class_ = "trend-card__list")[1]

    for element in table:
        quotes.append(element.get_text())
    
    quotes.insert(0, time.get_text())

    df = pd.DataFrame(quotes)
    df.to_csv('~/store_files_airflow/No1.csv', index= False)
    