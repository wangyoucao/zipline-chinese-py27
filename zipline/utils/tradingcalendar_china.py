
#author zhanghan
'''
This is the trading calendar of Stock in China, in this version
We only consider the day level data
'''
import pandas as pd
import pytz

from datetime import datetime
from dateutil import rrule
from functools import partial

start = pd.Timestamp('1990-01-01', tz='UTC')
end_base = pd.Timestamp('today', tz='UTC')
# Give an aggressive buffer for logic that needs to use the next trading
# day or minute.
end = end_base + pd.Timedelta(days=365)

def canonicalize_datetime(dt):
    # Strip out any HHMMSS or timezone info in the user's datetime, so that
    # all the datetimes we return will be 00:00:00 UTC.
    return datetime(dt.year, dt.month, dt.day, tzinfo=pytz.utc)

def get_non_trading_days(start, end):
    non_trading_rules = []
    start = canonicalize_datetime(start)
    end = canonicalize_datetime(end)

    #this is the rule of saturday and sunday
    weekends = rrule.rrule(
        rrule.YEARLY,
        byweekday=(rrule.SA, rrule.SU),
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(weekends)

    #first day of the year
    new_years = rrule.rrule(
        rrule.MONTHLY,
        byyearday=1,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(new_years)

    # 5.1
    may_1st = rrule.rrule(
        rrule.MONTHLY,
        bymonth=5,
        bymonthday=1,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(may_1st)

    #10.1,2,3
    oct_1st=rrule.rrule(
        rrule.MONTHLY,
        bymonth=10,
        bymonthday=1,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(oct_1st)

    oct_2nd=rrule.rrule(
        rrule.MONTHLY,
        bymonth=10,
        bymonthday=2,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(oct_2nd)

    oct_3rd=rrule.rrule(
        rrule.MONTHLY,
        bymonth=10,
        bymonthday=3,
        cache=True,
        dtstart=start,
        until=end
    )
    non_trading_rules.append(oct_3rd)

    non_trading_ruleset = rrule.rruleset()

    for rule in non_trading_rules:
        non_trading_ruleset.rrule(rule)

    non_trading_days = non_trading_ruleset.between(start, end, inc=True)

    non_trading_days.append(datetime(1991, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1991, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1991, 2, 18, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1991, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1991, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1991, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 2, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1992, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1993, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1993, 1, 25, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1993, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1993, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 2,  8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 2, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1994, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 2, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1995, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 21, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 28, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 2, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 3, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 9, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1996, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 13, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 2, 14, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 6, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 7, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1997, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 28, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 2, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1998, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 16, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 17, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 18, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 24, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 25, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 2, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 12, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(1999, 12, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 5, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2000, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 24, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 25, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 2, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 5, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2001, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 13, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 14, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 18, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 21, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 2, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 5, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 5, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 9, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2002, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 2, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 5, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2003, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 21, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 1, 28, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 5, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 5, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 5, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2004, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 14, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 5, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 5, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2005, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 2, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 5, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2006, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 2, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 2, 21, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 2, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 2, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 5, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 5, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2007, 12, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 2, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 6, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 9, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 9, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 9, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2008, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 28, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 4, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 5, 28, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 5, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2009, 10, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 2, 16, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 2, 17, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 2, 18, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 4, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 5, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 6, 14, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 6, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 6, 16, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 9, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 9, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 9, 24, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2010, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 2, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 2, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 4, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 6, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 9, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2011, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 24, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 25, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 26, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 4, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 4, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 4, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 6, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2012, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 1, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 2, 13, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 2, 14, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 2, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 4, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 4, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 4, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 6, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 6, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 6, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 9, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 9, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2013, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 2, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 2, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 2, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 2, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 4, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 6, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 9, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2014, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 2, 18, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 2, 19, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 2, 20, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 2, 23, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 2, 24, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 4, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 6, 22, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 9, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 9, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 10, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2015, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 1, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 2, 8, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 2, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 2, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 2, 11, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 2, 12, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 5, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 6, 9, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 6, 10, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 9, 15, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 9, 16, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 10, 6, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2016, 10, 7, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 1, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 1, 27, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 1, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 1, 31, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 2, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 2, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 4, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 4, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 5, 1, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 5, 29, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 5, 30, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 10, 2, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 10, 3, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 10, 4, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 10, 5, tzinfo=pytz.utc))
    non_trading_days.append(datetime(2017, 10, 6, tzinfo=pytz.utc))          
    
    non_trading_days.sort()

    return pd.DatetimeIndex(non_trading_days)

non_trading_days = get_non_trading_days(start, end)
trading_day = pd.tseries.offsets.CDay(holidays=non_trading_days)


def get_trading_days(start, end, trading_day=trading_day):
    return pd.date_range(start=start.date(),
                         end=end.date(),
                         freq=trading_day).tz_localize('UTC')

trading_days = get_trading_days(start, end)


def get_early_closes(start, end):
    # 1:00 PM close rules based on
    # http://quant.stackexchange.com/questions/4083/nyse-early-close-rules-july-4th-and-dec-25th # noqa
    # and verified against http://www.nyse.com/pdfs/closings.pdf

    # These rules are valid starting in 1993

    start = canonicalize_datetime(start)
    end = canonicalize_datetime(end)

    start = max(start, datetime(1993, 1, 1, tzinfo=pytz.utc))
    end = max(end, datetime(1993, 1, 1, tzinfo=pytz.utc))

    # Not included here are early closes prior to 1993
    # or unplanned early closes

    early_close_rules = []

    day_after_thanksgiving = rrule.rrule(
        rrule.MONTHLY,
        bymonth=11,
        # 4th Friday isn't correct if month starts on Friday, so restrict to
        # day range:
        byweekday=(rrule.FR),
        bymonthday=range(23, 30),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(day_after_thanksgiving)

    christmas_eve = rrule.rrule(
        rrule.MONTHLY,
        bymonth=12,
        bymonthday=24,
        byweekday=(rrule.MO, rrule.TU, rrule.WE, rrule.TH),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(christmas_eve)

    friday_after_christmas = rrule.rrule(
        rrule.MONTHLY,
        bymonth=12,
        bymonthday=26,
        byweekday=rrule.FR,
        cache=True,
        dtstart=start,
        # valid 1993-2007
        until=min(end, datetime(2007, 12, 31, tzinfo=pytz.utc))
    )
    early_close_rules.append(friday_after_christmas)

    day_before_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=3,
        byweekday=(rrule.MO, rrule.TU, rrule.TH),
        cache=True,
        dtstart=start,
        until=end
    )
    early_close_rules.append(day_before_independence_day)

    day_after_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=5,
        byweekday=rrule.FR,
        cache=True,
        dtstart=start,
        # starting in 2013: wednesday before independence day
        until=min(end, datetime(2012, 12, 31, tzinfo=pytz.utc))
    )
    early_close_rules.append(day_after_independence_day)

    wednesday_before_independence_day = rrule.rrule(
        rrule.MONTHLY,
        bymonth=7,
        bymonthday=3,
        byweekday=rrule.WE,
        cache=True,
        # starting in 2013
        dtstart=max(start, datetime(2013, 1, 1, tzinfo=pytz.utc)),
        until=max(end, datetime(2013, 1, 1, tzinfo=pytz.utc))
    )
    early_close_rules.append(wednesday_before_independence_day)

    early_close_ruleset = rrule.rruleset()

    for rule in early_close_rules:
        early_close_ruleset.rrule(rule)
    early_closes = early_close_ruleset.between(start, end, inc=True)

    # Misc early closings from NYSE listing.
    # http://www.nyse.com/pdfs/closings.pdf
    #
    # New Year's Eve
    nye_1999 = datetime(1999, 12, 31, tzinfo=pytz.utc)
    if start <= nye_1999 and nye_1999 <= end:
        early_closes.append(nye_1999)

    early_closes.sort()
    return pd.DatetimeIndex(early_closes)

early_closes = get_early_closes(start, end)


def get_open_and_close(day, early_closes):
    market_open = pd.Timestamp(
        datetime(
            year=day.year,
            month=day.month,
            day=day.day,
            hour=9,
            minute=31),
        tz='US/Eastern').tz_convert('UTC')
    # 1 PM if early close, 4 PM otherwise
    close_hour = 13 if day in early_closes else 16
    market_close = pd.Timestamp(
        datetime(
            year=day.year,
            month=day.month,
            day=day.day,
            hour=close_hour),
        tz='Asia/Shanghai').tz_convert('UTC')

    return market_open, market_close


def get_open_and_closes(trading_days, early_closes, get_open_and_close):
    open_and_closes = pd.DataFrame(index=trading_days,
                                   columns=('market_open', 'market_close'))

    get_o_and_c = partial(get_open_and_close, early_closes=early_closes)

    open_and_closes['market_open'], open_and_closes['market_close'] = \
        zip(*open_and_closes.index.map(get_o_and_c))

    return open_and_closes

open_and_closes = get_open_and_closes(trading_days, early_closes,
                                      get_open_and_close)
