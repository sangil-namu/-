import time,datetime

days_ago = datetime.datetime.now() - datetime.timedelta(days=2)

ym = days_ago.strftime('%Y-%m')
ymd = days_ago.strftime('%Y%m%d')


def dayago(tday):
  daytoago = datetime.datetime.now() - datetime.timedelta(days=tday)
  day2day = daytoago.strftime('%Y%m%d')
  time2time = daytoago.strftime('%Y%m%d %H%M%S')
  print('day  : ' , day2day)
  print('time : ', time2time)
  
  
  
#check
 dayago(2)  <-enter
