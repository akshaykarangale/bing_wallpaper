
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
# waiting for my laptop to get connected to internet when my PC starts
while code != 200:
	time.sleep(15)
	fn = datetime.date.isoformat(datetime.datetime.now()).replace("-","") # building filename
	try:
		response = requests.get("http://bingwallpaper.com/"+fn+".html") # getting html page from url
# In[3]:

		soup = bs4.BeautifulSoup(response.text, 'lxml') # parsing the html


# In[8]:

		a = soup.select('.imgContainer > img') # getting the link of today's wallpaper


# In[18]:

		url = "http://"+a[0]['src'][2:] # building the url for downloading wallpaper


# In[37]:
# In[38]:

		urllib.request.urlretrieve(url,filename="/home/akshay/bing_wallpaper/"+fn+".jpg") # downloading the wallpaper
		print("Downloading complete !")

# In[39]:
		# setting the wallpaper
		os.system("gsettings set org.gnome.desktop.background picture-uri file:///home/akshay/bing_wallpaper/"+fn+".jpg")
		print("Wallpaper set")
		code = 200
	except requests.exceptions.ConnectionError:
		# catching the exception when internet is not connected
		print("Internet not connected")
# In[ ]:



