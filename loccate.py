from datetime import datetime, timedelta
import re
dt_now = datetime.now()
print((dt_now-timedelta(days=1)).strftime('%Y.%m.%d') )
print(dt_now.strftime('%Y.%m.%d'))
print((dt_now-timedelta(days=30)).strftime('%Y.%m.%d') )
ss_bbufer='01/01/25 12:10:03.234567'
#ss_bbufer= input()


ert=( re.split('[:,.,/, ]',ss_bbufer))
god='20'+ert[2]

#print(ert)
erty=(datetime(int(god),int(ert[0] ),int(ert[1] ),int(ert[3] ),int(ert[4] ) ,int(ert[5] ) ,int(ert[6] )   ) )
print(erty)
