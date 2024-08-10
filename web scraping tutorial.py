from selenium import webdriver as wd

firefox = wd.Chrome()
browser = firefox.get('https://www.google.com/search?gs_ssp=eJzj4tTP1TcwSivKKzRg9BIoScxOLc7IVC9WSE4sLslJBQCHSgmi&q=takeshi%27s+castle&rlz=1C1CHBD_enNG923NG923&oq=takeshi&gs_lcrp=EgZjaHJvbWUqDAgBEC4YQxiABBiKBTIGCAAQRRg5MgwIARAuGEMYgAQYigUyDAgCEC4YQxiABBiKBTIHCAMQLhiABDIHCAQQLhiABDIHCAUQLhiABDIHCAYQLhiABDIHCAcQLhiABDIHCAgQLhiABNIBCDQyMThqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8')