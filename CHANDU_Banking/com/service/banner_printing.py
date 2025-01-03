
from CHANDU_Banking.com.service.constants import *

def bannerPrinting():
    with open(BANNERPATH,encoding='utf-8') as f:
        data = f.read()
        print(data)
        return None

def exit_banner_printing():
    with open(EXITBANNERPATH,mode='r',encoding='utf-8') as f:
        data = f.read()
        print(data)
        return None