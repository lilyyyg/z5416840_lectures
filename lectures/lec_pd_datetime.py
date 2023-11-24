""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt

import pandas as pd

import toolkit_config as cfg

CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')


# ----------------------------------------------------------------------------
# The datetime class:
#   Implements several methods to generate instances of `datetime`
#   representing a certain date
# ----------------------------------------------------------------------------

# One of the methods implemented by `dt.datetime` is called `now`, which
# returns an instance of `dt.datetime` representing the current date/time.

# Instance of `dt.datetime` with the current date/time
dt_now  = dt.datetime.now()

# This will produce a string representing the date/time in `dt_now`
print(dt_now)

# This will confirm that `dt_now` is an instance of the `datetime` class
print(type(dt_now))


# From the `print` statement above, we can see that instances of `datetime`
# store the date (year, month, day) and time (hour, minute, second,
# microsecond). You can access these attributes directly from the instance:

#s = 'Date in day/month/year format is: {}/{}/{} '.format(dt_now.day, dt_now.month, dt_now.year)
#print(s)
#


# ----------------------------------------------------------------------------
#   Comparing `repr` and `print` (datetime instances)
# ----------------------------------------------------------------------------
# String representing the data included in the object
#print(dt_now)

# This will give you a string representing how the instance could be
# constructed
#print(repr(dt_now))


# Create another datetime instance with value 2021-08-21 13:24:27.283311

#a_little_ago = dt.datetime(
#    year=2021,
#    month=8,
#    day=21,
#    hour=13,
#    minute=27,
#    second=1, microsecond=283311)
#print(a_little_ago)
## Output:
# 2021-08-21 13:24:27.283311


# Note that we don't have to pass all arguments

#dt_other = dt.datetime(
#    year=2021,
#    month=8,
#    day=21,
#    )
#print(dt_other)
#


# ----------------------------------------------------------------------------
#   `datetime.timedelta` objects
# ----------------------------------------------------------------------------

# Lets create two other datetime instances

dt0 = dt.datetime(year=2019, month=12, day=31)
dt1 = dt.datetime(year=2020, month=1, day=1)
#

# Operations between datetime objects will return timedelta objects
delta  = dt1 - dt0
print(repr(delta))
print(delta)


# These two dates are 12 hours apart
new_delta  = t1 - t2
print(new_delta)


# Add 12 hours to some date
#   - `start` will be the starting date
#   - `delta` will be a period of 12 hours
#   - `end` will be the ending date

#start = dt.datetime(year=2020, month=12, day=31, hour=0)
#delta = dt.timedelta(hours=12)
## This is the new date
#end = start + delta
#
#print(start)
#print(end)
#


# ----------------------------------------------------------------------------
#   The `strftime` method
# ----------------------------------------------------------------------------

# | Directive | Meaning                                                       | Example                  |
# |-----------|---------------------------------------------------------------|--------------------------|
# | %a        | Weekday as locale's abbreviated name.                         | Sun, Mon,...             |
# | %A        | Weekday as locale's full name.                                | Sunday, Monday,...       |
# | %w        | Weekday as a decimal number (Sunday=0,Saturday=6)             | 0, 1,..., 6              |
# | %d        | Day of the month as a zero-padded decimal number.             | 01, 02, …, 31            |
# | %b        | Month as locale's abbreviated name.                           | Jan, Feb,..., Dec        |
# | %B        | Month as locale's full name.                                  | January, February,...    |
# | %m        | Month as a zero-padded decimal number.                        | 01, 02, …, 12            |
# | %y        | Year without century as a zero-padded decimal number.         | 00, 01,..., 99           |
# | %Y        | Year with century as a decimal number.                        | 0001, 1999, 2013, 2014   |
# | %H        | Hour (24-hour clock) as a zero-padded decimal number.         | 00, 01, …, 23            |
# | %I        | Hour (12-hour clock) as a zero-padded decimal number.         | 01, 02, …, 12            |
# | %p        | Locale's equivalent of either AM or PM.                       | AM, PM                   |
# | %M        | Minute as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %S        | Second as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %j        | Day of the year as a zero-padded decimal number.              | 001, 002, …, 366         |
# | %U        | Week number of the year (Sunday as the first day of the week) | 00, 01, …, 53            |
# | %W        | Week number of the year (Monday as the first day of the week) | 00, 01, …, 53            |
# | %c        | Locale's appropriate date and time representation.            | Tue Aug 16 21:30:00 1988 |

# Create a datatime object
date  = dt.datetime(year = 2020, month = 12, day = 31, hour =0)

# Create a string with the representation we want:
s  = date.strftime('%Y-%m-%d')
#print(s)
# Output:
#  '2020-12-31'


# ----------------------------------------------------------------------------
#   Time series with Pandas
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#   Load the data into a dataframe
# ----------------------------------------------------------------------------

#prc = pd.read_csv(CSVLOC)
#print(prc)
#prc.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2645 entries, 0 to 2644
# Data columns (total 7 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Date       2645 non-null   object
#  1   Open       2645 non-null   float64
#  2   High       2645 non-null   float64
#  3   Low        2645 non-null   float64
#  4   Close      2645 non-null   float64
#  5   Adj Close  2645 non-null   float64
#  6   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1), object(1)
# memory usage: 144.8+ KB
#
## 'Date' is a column of strings with dates.
#print(prc.loc[:, 'Date'])
#
## The index is just a counter
#print(prc.index)
# Output:
# RangeIndex(start=0, stop=2645, step=1)


# ----------------------------------------------------------------------------
#   The `to_datetime` method
# ----------------------------------------------------------------------------
# Compare these two cases:

# prc['Date'] is a series
dser  = pd.to_datetime(prc['Date'], format=''%Y-%m-%d')
#print(dser)
# Output:
# 0      2010-06-29
# 1      2010-06-30
# 2      2010-07-01
# 3      2010-07-02
# 4      2010-07-06
#           ...
# 2640   2020-12-22
# 2641   2020-12-23
# 2642   2020-12-24
# 2643   2020-12-28
# 2644   2020-12-29
# Name: Date, Length: 2645, dtype: datetime64[ns]

# prc['Date'].array is a pandas array
didx  = pd.to_datetime(prc['Date'].array, format='%Y-%m-%d')
#print(didx)
# Output:
# DatetimeIndex(['2010-06-29', '2010-06-30', '2010-07-01', '2010-07-02',
#                '2010-07-06', '2010-07-07', '2010-07-08', '2010-07-09',
#                '2010-07-12', '2010-07-13',
#                ...
#                '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18',
#                '2020-12-21', '2020-12-22', '2020-12-23', '2020-12-24',
#                '2020-12-28', '2020-12-29'],
#               dtype='datetime64[ns]', length=2645, freq=None)

# Convert the string elements in the Date column to datetime objects
#prc.loc[:, 'Date'] = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
#prc.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2645 entries, 0 to 2644
# Data columns (total 7 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Date       2645 non-null   datetime64[ns]
#  1   Open       2645 non-null   float64
#  2   High       2645 non-null   float64
#  3   Low        2645 non-null   float64
#  4   Close      2645 non-null   float64
#  5   Adj Close  2645 non-null   float64
#  6   Volume     2645 non-null   int64
# dtypes: datetime64[ns](1), float64(5), int64(1)

# ----------------------------------------------------------------------------
#   Setting the index
# ----------------------------------------------------------------------------
another_df  = prc.set_index('Date')
#another_df.info()

# Override the variable with another dataframe
# prc = prc.set_index('Date')
# Or use the `inplace` argument (when available):
# (recommended)
#prc.set_index('Date', inplace=True)
#prc.info()

# Check the new index
#print(prc.index)

# ----------------------------------------------------------------------------
#   Setting datetime indexes during read_csv
# ----------------------------------------------------------------------------
# previously:
# prc = pd.read_csv(CSVLOC)

# New version

#prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
#prc.info()
## <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 2645 entries, 2010-06-29 to 2020-12-29
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       2645 non-null   float64
#  1   High       2645 non-null   float64
#  2   Low        2645 non-null   float64
#  3   Close      2645 non-null   float64
#  4   Adj Close  2645 non-null   float64
#  5   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1)
# memory usage: 144.6 KB
#


# ----------------------------------------------------------------------------
#   Illustrating the advantages of a datetime indexes
# ----------------------------------------------------------------------------

## Select all data for a given year in one go
#print(prc.loc['2020'])
#
## Select all data for a given month
#print(prc.loc['2020-01'])
#
## Selecting date ranges using strings
#print(prc.loc['2020-01-01':'2020-01-05'])
#
#


# ----------------------------------------------------------------------------
#   Computing returns
# ----------------------------------------------------------------------------
# Make sure the dataframe is sorted
#prc.sort_index(inplace=True)

# compute returns - this method computes the percentage change of two
# consecutive observations.
# When applied to 'close', the result is the stock daily return

#rets = prc.loc[:, 'Close'].pct_change()
#print(rets)

# Output:
# Date
# 2010-06-29         NaN