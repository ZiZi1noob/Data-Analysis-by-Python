import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas.core import series

#******************************************************************************************
#******************************************************************************************
#******************************Introduction to pandas data structures**********************
#******************************************************************************************
#******************************************************************************************


#################################################################################################################################
#                                                 Series                                                                        #
#             A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type)              #
#             and an associated array of data labels, called its index.                                                         #
#################################################################################################################################
'''
                                                 CAUTION
The column returned when indexing a DataFrame is a view on the underlying data, not a copy.Thus, any in-place modifications to 
the Series will be reflected in the DataFrame. The column can be explicitly copied using the Series’s copy method.'''





seriesObj = Series([1,2,3,4,5]) #<class 'pandas.core.series.Series'>
print(seriesObj.values) #[1 2 3 4 5]
print(seriesObj.index) #RangeIndex(start=0, stop=5, step=1)

'''we can also identify each data index'''
seriesObj2 = Series([7,8,9,5,3], index=['A','B','C','D','E'])
print(seriesObj2)
# A    7
# B    8
# C    9
# D    5
# E    3
# dtype: int64
seriesObj2.values[1] = 10 #change 'B' index's value to 10
print(seriesObj2)
'''we can create a Series from a Python dict'''
pyDic = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
Series_with_Missing = Series(pyDic, index=['Perking', 'Ohio', 'Texas', 'Oregon'])
# Perking     NaN
# Ohio      35000
# Texas     71000
# Oregon    16000
# dtype: int64
'''in pandas, a missing data will be denoted by NaN; and we use isnull and notnull function to detect mising numbers'''
print(pd.isnull(Series_with_Missing))
# Perking     True
# Ohio       False
# Texas      False
# Oregon     False
# dtype: bool
print(pd.notnull(Series_with_Missing))
# Perking    False
# Ohio        True
# Texas       True
# Oregon      True
# dtype: bool
'''A critical Series feature for many applications is that it automatically aligns differently-indexed data in arithmetic operations'''
Series_with_dic = Series(pyDic)
print(Series_with_dic + Series_with_Missing)
# Ohio        70000.0
# Oregon      32000.0
# Perking         NaN
# Texas      142000.0
# Utah            NaN
# dtype: float64
Series_with_dic.name = 'FreeStyle'
Series_with_dic.index.name = 'IndexName'
print(Series_with_dic)
# IndexName
# Ohio      35000
# Texas     71000
# Oregon    16000
# Utah       5000
# Name: FreeStyle, dtype: int64

Series_with_dic.index = ['Change','Index', 'Name', 'by this']
print(Series_with_dic)
# Change     35000
# Index      71000
# Name       16000
# by this     5000
# Name: FreeStyle, dtype: int64

#################################################################################################################################
#                                                 DataFrame                                                                     #
#             A Series is a one-dimensional array-like object containing an array of data (of any NumPy data type)              #
#             and an associated array of data labels, called its index.                                                         #
#################################################################################################################################
dfDic = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame1 = DataFrame(dfDic)
print(frame1)
#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9
'''we can also change column's order by this way:'''
frame2 = DataFrame(dfDic, columns= ['year', 'state', 'pop'])
print(frame2)
#    year   state  pop
# 0  2000    Ohio  1.5
# 1  2001    Ohio  1.7
# 2  2002    Ohio  3.6
# 3  2001  Nevada  2.4
# 4  2002  Nevada  2.9

'''As with Series, if you pass a column that isn’t contained in data, it will appear with NA values in the result:'''
frame3 = DataFrame(dfDic, columns=['year', 'state', 'pop', 'debt'],
                     index=['one', 'two', 'three', 'four', 'five'])
print(frame3['year'])
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64
print(frame3.year)
# one      2000
# two      2001
# three    2002
# four     2001
# five     2002
# Name: year, dtype: int64
'''find row'''
'''delete row'''
del frame2['year']
frame3['debt'] = 1
print(frame3)
#        year   state  pop  debt
# one    2000    Ohio  1.5     1
# two    2001    Ohio  1.7     1
# three  2002    Ohio  3.6     1
# four   2001  Nevada  2.4     1
# five   2002  Nevada  2.9     1
frame3['debt'] = np.arange(5)
print(frame3)
#        year   state  pop  debt
# one    2000    Ohio  1.5     0
# two    2001    Ohio  1.7     1
# three  2002    Ohio  3.6     2
# four   2001  Nevada  2.4     3
# five   2002  Nevada  2.9     4

pop = DataFrame({'Nevada': {2001: 2.4, 2002: 2.9},
           'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}})
pop.T # transpose
DataFrame(pop, index=[2001, 2002, 2003]) # sort row index
DataFrame({'Ohio': pop['Ohio'][:-1],
             'Nevada': pop['Nevada'][:2]}) # select targeted elements


#################################################################################################################################
#                                                 Index Objects                                                                 #
#             pandas's index objects are responsible for holding the axis labels and other metadata                             #
#             Index objects are immutable and thus can’t be modified by the user                                                #
#################################################################################################################################

obj = Series(range(3), index=['a','b','c'])
index = obj.index
# Index(['a', 'b', 'c'], dtype='object')
obj2 = obj.append(Series('dd'))
print(obj2)
'''
Index methods and properties

Method	       Description
append	       Concatenate with additional Index objects, producing a new Index
diff	       Compute set difference as an Index
intersection	Compute set intersection
union	       Compute set union
isin	       Compute boolean array indicating whether each value is contained in the passed collection
delete 	Compute new Index with element at index i deleted
drop	       Compute new index by deleting passed values
insert	       Compute new Index by inserting element at index i
is_monotonic	Returns True if each element is greater than or equal to the previous element
is_unique	Returns True if the Index has no duplicate values
unique	       Compute the array of unique values in the Index
'''
##############################################################################################################################################
#                                                 Reindexing                                                                                 #
#             A critical method on pandas objects is reindex, which means to create a new object                                             #
#             with the data conformed to a new index.                                                                                        #
#             Reindex can alter either the row(index), columns, or both. When passing just a sequence, the rows are reindexed in the result  #
##############################################################################################################################################

obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj_fill = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj_fill)
# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    0.0
# dtype: float64
obj3 = Series(['blue', 'purple', 'yellow'], index=['a', 'd', 'f'])
print(obj3.reindex(['a','b','c','d','e','f'], method='ffill'))
# a      blue
# b      blue
# c      blue
# d    purple
# e    purple
# f    yellow
# dtype: object
frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                   columns=['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)
#     Ohio  Texas  California
# a   0.0    1.0         2.0
# b   NaN    NaN         NaN
# c   3.0    4.0         5.0
# d   6.0    7.0         8.0
frame3 = frame.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=['Ohio', 'Texas', 'California'])
print(frame3)
#   Ohio  Texas  California
# a     0      1           2
# b     0      1           2
# c     3      4           5
# d     6      7           8
'''
reindex method (interpolation) options

Argument	       Description
ffill or pad	       Fill (or carry) values forward
bfill or backfill	Fill (or carry) values backward
'''
################################################################################################################################################
#                                                Dropping entries from an axis                                                                 #
#             the drop method will return a new object with the indicated value or values deleted from an axis                                 #
# ##############################################################################################################################################
data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data.drop(['Ohio'], axis=0)) #default: axis = 0 
print(data.drop(['one'], axis=1))

################################################################################################################################################
#                                                Indexing, selection, and filtering                                                            #
#         works analogously to NumPy array indexing, except you can use the Series’s index values instead of only integers.                    #
# ##############################################################################################################################################
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
# a    0.0
# b    1.0
# c    2.0
# d    3.0
# dtype: float64
print(obj['b'] == obj[1]) #1.0
# True
print(obj[2:4]  == obj[['c', 'd']])
print(obj['c':'d'])
# c    True
# d    Truex

data = DataFrame(np.arange(16).reshape((4, 4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['one', 'two', 'three', 'four'])
print(data.loc[['Ohio','Colorado'],['one','two']])
#          one  two
#Ohio        0    1
#Colorado    4    5
'''
pd.iloc() vs. pd.loc() https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different
loc gets rows (and/or columns) with particular labels.

iloc gets rows (and/or columns) at integer locations.
'''
s = pd.Series(list("abcdef"), index=[49, 48, 47, 0, 1, 2])
print(s)
# 49    a
# 48    b
# 47    c
# 0     d
# 1     e
# 2     f
# dtype: object
s.loc[0] # 'd'
s.iloc[0] # 'a'
s.loc[0:1]    # 0    d  
              # 1    e
s.iloc[0:1]   #49    a
df = DataFrame(np.arange(20).reshape((4, 5)), columns=list('bcdfg'),
                    index=['Ohio', 'Texas', 'Colorado','Columbia'])
print(df.loc[:'Columbia', 'c':'f'])
#           c   d   f
# Ohio       1   2   3
# Texas      6   7   8
# Colorado  11  12  13
# Columbia  16  17  18
print(df.iloc[:2, :3])
#       b  c  d
# Ohio   0  1  2
# Texas  5  6  7
################################################################################################################################################
#                                                Arithmetic and data alignment                                                                 #
#         if any index pairs are not the same, the index in the result will be index pairs                                                     #
# ##############################################################################################################################################
df1 = DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'),
                    index=['Ohio', 'Texas', 'Colorado'])
df2 = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1+df2)
#            b   c     d   e
# Colorado  NaN NaN   NaN NaN
# Ohio      3.0 NaN   6.0 NaN
# Oregon    NaN NaN   NaN NaN
# Texas     9.0 NaN  12.0 NaN
# Utah      NaN NaN   NaN NaN
df1_puls_df2 = df2.add(df1, fill_value= 0)
print(df1_puls_df2)
#            b    c     d     e
# Colorado  6.0  7.0   8.0   NaN
# Ohio      3.0  1.0   6.0   5.0
# Oregon    9.0  NaN  10.0  11.0
# Texas     9.0  4.0  12.0   8.0
# Utah      0.0  NaN   1.0   2.0
'''
Flexible arithmetic methods

Method	Description
add	Method for addition (+)
sub	Method for subtraction (-)
div	Method for division (/)
mul	Method for multiplication (*)
'''
frame = DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
seres = frame.iloc[0]
print(seres)
print(frame.sub(seres,axis=1))
#          b    d    e
# Utah    0.0  0.0  0.0
# Ohio    3.0  3.0  3.0
# Texas   6.0  6.0  6.0
# Oregon  9.0  9.0  9.0

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                   index=['Utah', 'Ohio', 'Texas', 'Oregon'])
f = lambda x: x.max() - x.min()
print(frame.apply(f))
# b    3.107291
# d    0.901345
# e    3.778292
# dtype: float64
format = lambda x: '%.2f' % x
print(frame.applymap(format))
#            b      d      e
# Utah    -0.65  -1.49   0.36
# Ohio    -1.80   0.63  -0.17
# Texas   -2.16  -0.00  -0.45
# Oregon   1.44  -0.54  -1.68
print(frame['e'].map(format))
# Utah       0.72
# Ohio       0.96
# Texas     -0.38
# Oregon    -0.82

################################################################################################################################################
#                                                Sorting and ranking                                                                           #
#          To sort lexicographically by row or column index, use the sort_index method, which returns a new, sorted object                     #
#          assigning ranks from one through the number of valid data points in an array                                                        #
# ##############################################################################################################################################
obj = Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
# a    1
# b    2
# c    3
# d    0
# dtype: int64
frame = DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                   columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
#        d  a  b  c
# one    4  5  6  7
# three  0  1  2  3
print(frame.sort_values('b'))
#        d  a  b  c
# three  0  1  2  3
# one    4  5  6  7
obj = Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
# 0    6.5
# 1    1.0
# 2    6.5
# 3    4.5
# 4    3.0
# 5    2.0
# 6    4.5
# dtype: float64
################################################################################################################################################
#                                                Summarizing and Computing Descriptive Statistics                                              #
#          To sort lexicographically by row or column index, use the sort_index method, which returns a new, sorted object                     #
#          assigning ranks from one through the number of valid data points in an array                                                        #
# ##############################################################################################################################################
'''
                            Descriptive and summary statistics

Method	              Description
count	              Number of non-NA values
describe	       Compute set of summary statistics for Series or each DataFrame column
min, max	       Compute minimum and maximum values
argmin, argmax	Compute index locations (integers) at which minimum or maximum value obtained, respectively
idxmin, idxmax	Compute index values at which minimum or maximum value obtained, respectively
quantile	       Compute sample quantile ranging from 0 to 1
sum	              Sum of values
mean	              Mean of values
median	              Arithmetic median (50% quantile) of values
mad	              Mean absolute deviation from mean value
var	              Sample variance of values
std	              Sample standard deviation of values
skew	              Sample skewness (3rd moment) of values
kurt	              Sample kurtosis (4th moment) of values
cumsum	              Cumulative sum of values
cummin, cummax	Cumulative minimum or maximum of values, respectively
cumprod	       Cumulative product of values
diff	              Compute 1st arithmetic difference (useful for time series)
pct_change	       Compute percent changes
'''
df = DataFrame([[1.4, np.nan], [7.1, -4.5],
    				[np.nan, np.nan], [0.75, -1.3]],
    			   index=['a', 'b', 'c', 'd'],
    			   columns=['one', 'two'])
print(df.sum()) # default axis = 0
# one    9.25
# two   -5.80
# dtype: float64
print(df.sum(axis=1))
# a    1.40
# b    2.60
# c    0.00
# d   -0.55
# dtype: float64
print(df.mean(axis=1, skipna=False))
# a      NaN
# b    1.300
# c      NaN
# d   -0.275
# dtype: float64
print(df.describe())
#            one       two
# count  3.000000  2.000000
# mean   3.083333 -2.900000
# std    3.493685  2.262742
# min    0.750000 -4.500000
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000

################################################################################################################################################
#                                                Unique Values, Value Counts, and Membership                                                   #
# ##############################################################################################################################################
#Method	       Description
#isin	              Compute boolean array indicating whether each Series value is contained in the passed sequence of values.
#unique	       Compute array of unique values in a Series, returned in the order observed.
#value_counts	       Return a Series containing unique values as its index and frequencies as its values, ordered count in descending order.

################################################################################################################################################
#                                                Handling Missing Data                                                                         #
#  pandas uses the floating point value NaN (Not a Number) to represent missing data in both floating as well as in non-floating point arrays  #
# ##############################################################################################################################################
'''
NA                   handling methods
Argument	       Description
dropna	              Filter axis labels based on whether values for each label have missing data, with varying thresholds for how much missing data to tolerate.
fillna	              Fill in missing data with some value or using an interpolation method such as 'ffill' or 'bfill'.
isnull	              Return like-type object containing boolean values indicating which values are missing / NA.
notnull	       Negation of isnull.
'''
data = Series([1, np.nan, 3.5, np.nan, 7])
print(data)
# 0    1.0
# 1    NaN
# 2    3.5
# 3    NaN
# 4    7.0
# dtype: float64
data.dropna()
print(data[data.notnull()])
# 0    1.0
# 2    3.5
# 4    7.0
# dtype: float64

data = DataFrame([[1., 6.5, 3.], [np.nan, np.nan, np.nan],
 				  [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.],[np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data.dropna(axis=1, how = 'all'))
'''
Suppose you want to keep only rows containing a certain number of observations. You can indicate this with the thresh argument
'''
df = DataFrame(np.random.randn(7, 3))
df.iloc[:4,1] = np.nan; df.iloc[:2,2] = np.nan
print(df)
#          0         1         2
# 0  0.102012       NaN       NaN
# 1  1.114245       NaN       NaN
# 2  0.120191       NaN  1.606363
# 3  0.634609       NaN -0.569714
# 4 -1.339399  0.016629  1.176083
# 5 -0.121108  0.055944 -0.660088
# 6  0.865581 -0.063874 -0.676273
df2 = df.dropna(thresh=3)
print(df2)
#          0         1         2
# 4  0.144553 -0.823962 -0.702406
# 5 -0.541658 -1.329512 -0.428666
# 6  0.487786  1.018696  0.002505
################################################################################################################################################
#                                                Filling in Missing Data                                                                       #
#                                                                                                                                              #
# ##############################################################################################################################################
df3 = df.fillna('yo')
print(df3)
#           0         1         2
# 0 -0.784747        yo        yo
# 1  0.542099        yo        yo
# 2  0.843661        yo  0.322336
# 3  0.366144        yo -0.131099
# 4 -1.194357 -2.131621  2.410864
# 5  0.885477 -0.532255 -2.428564
# 6  1.771790  0.370458   2.22824
df4 = df.fillna({1: 0.5, 2: -1})
print(df4)
#           0         1         2
# 0  0.794533  0.500000 -1.000000
# 1 -0.685401  0.500000 -1.000000
# 2 -2.139314  0.500000  0.018518
# 3 -0.571489  0.500000 -1.238190
# 4 -1.639770 -0.366178 -1.677333
# 5  0.964440  0.147398 -1.663045
# 6  0.667218  0.672672 -0.599545
'''
fillna function arguments

Argument	Description
value	       Scalar value or dict-like object to use to fill missing values
method	       Interpolation, by default 'ffill' if function called with no other arguments
axis	       Axis to fill on, default axis=0
inplace	Modify the calling object without producing a copy
limit	       For forward and backward filling, maximum number of consecutive periods to fill
'''

################################################################################################################################################
#                                                Hierarchical indexing                                                                         #
#                                                                                                                                              #
# ##############################################################################################################################################