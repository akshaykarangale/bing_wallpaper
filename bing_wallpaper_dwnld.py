
# coding: utf-8

# In[32]:

import requests
import bs4
import urllib.request
import os
import datetime
import time

# In[40]:
code = 400
print("Downloading wallpaper....")
while code != 200:
	time.sleep(15)
	fn = datetime.date.isoformat(datetime.datetime.now()).replace("-","")
	try:
		response = requests.get("http://bingwallpaper.com/"+fn+".html")
# In[3]:

		soup = bs4.BeautifulSoup(response.text, 'lxml')


# In[8]:

		a = soup.select('.imgContainer > img')


# In[18]:

		url = "http://"+a[0]['src'][2:]


# In[37]:
# In[38]:

		urllib.request.urlretrieve(url,filename="/home/akshay/bing_wallpaper/"+fn+".jpg")
		print("Downloading complete !")

# In[39]:

		os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/akshay/bing_wallpaper/"+fn+".jpg")
		print("Wallpaper set")
		code = 200
	except requests.exceptions.ConnectionError:
		print("Internet not connected")
# In[ ]:



