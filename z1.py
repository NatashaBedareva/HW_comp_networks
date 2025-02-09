import pandas as pd

from subprocess import check_output

hostnames = ["unity.com", "www.python.org","ru.wikipedia.org","askubuntu.com","www.youtube.com",
             "habr.com","mail.google.com", "www.cyberforum.ru","sky.pro","genshin.hoyoverse.com"]
data = []

for hostname in hostnames:
    out = int(check_output("ping -n 1 " + hostname).split()[-2])
    data.append([hostname,out])

df = pd.DataFrame(data)
df.columns=['host_name','average_speed']
df.to_csv('out.csv', index=False)
