import pandas as pd
from datetime import datetime

month_map = {'January':1,'February':2,'March':3,'April':4,'May':5,
'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

def remove_comma(str_no):
    number_arr = str_no.split(",")
    number_str = ""
    for n in number_arr:
        number_str += n
    return number_str
    
def change_date(date):
    if 'May' in date:
        date_split = date.split(".")
        date_split[2] = "20" + date_split[2]
    else:
        date_split = date.split(" ")
    year = date_split[2]
    month = month_map[date_split[1]]
    day = date_split[0]
    date = "{0}/{1}/{2}".format(year,month,day)
    return date


def date_dif(str_d1,str_d2="2023/1/8"):
    d1 = datetime.strptime(str_d1, "%Y/%m/%d")
    d2 = datetime.strptime(str_d2, "%Y/%m/%d")
    # difference between dates in timedelta
    delta = d2 - d1
    return delta.days

if __name__ == "__main__":
    song_df = pd.read_csv('./top_songs.csv')

    highest_acceleration = 0
    cheetah_arr = []
    for i,data in song_df.iterrows():
        next_date = change_date(data['Release Date'])
        diff = date_dif(next_date)
        streams = int(remove_comma(data['Streams (Billions)']))
        cur_acc = streams/diff
        cheetah_arr.append((data['Song'],data['Artist'],cur_acc))
    cheetah_arr.sort(key = lambda x : x[2], reverse=True)
    for song,artist,_ in cheetah_arr[0:10]:
        print(song)
        print(artist)
        print("\n")
        