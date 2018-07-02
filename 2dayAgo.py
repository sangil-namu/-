import time,datetime

days_ago = datetime.datetime.now() - datetime.timedelta(days=2)

ym = days_ago.strftime('%Y-%m')
ymd = days_ago.strftime('%Y%m%d')
