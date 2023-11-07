# ----------------------------------------------------------------------------
#   Indexing using lists
# ----------------------------------------------------------------------------

# The `start` variable will hold the first index in the slice and the `end`
# variable will hold the last index in the slice. Remember that the `index`
# list method will return the position of the element in the list, starting at
# 0. In this case, `start` will be set to 2 and `end` will be set to 6.

# Remember to uncomment the statements below and complete the part with '?'
start  = '?'
end  = '?'
#print(start, end)

# Now, slice the `prices` list.
# Remember that slices do not include endpoints
prcs_w1  = '?'

# Finally, calculate the average of the prices in the slice
avgprc  = '?'
#print(avgprc)


# ----------------------------------------------------------------------------
#   Indexing using dictionaries
# ----------------------------------------------------------------------------
prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  '2020-01-13': 7.0200,
  '2020-01-14': 7.1100,
  '2020-01-15': 7.0400,
  }

# Get the price on '2020-01-13', in this case, 7.02
x  = '?'
#print(f'The price on 2020-01-13 is {x}')


# Try the following... it will not work because we cannot slice dictionaries
#prc_dic['2020-01-02':'2020-01-13']          # Raises Exception