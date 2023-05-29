import pandas as pd
from web_scr import Scrapper

lst = []
with Scrapper(teardown=True) as bot:
   for i in range(1,171):
      link = "https://www.babynamespedia.com/names/boy/arabic-language"
      if i > 1 :
         link=link+"/"+str(i)
      bot.land_page(link)
      lst.extend(bot.find())

   for i in range(1,180):
      link = "https://www.babynamespedia.com/names/girl/arabic-language"
      if i > 1 :
         link=link+"/"+str(i)
      bot.land_page(link)
      lst.extend(bot.find())

df = pd.DataFrame()
df['names']= lst


