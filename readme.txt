# Data Analyst Learning Notes

---

pandas -> numpy -> matplotlib

---

## my_pandas list

1. `1_intro.py`
2. `2_dataframe.py`
3. `3_version.py`
4. `4_series.py`
5. `5_dataframe.py`
6. `6_readcsv.py`
7. `7_readjson.py`
8. `8_analyst.py`
9. `9_cleandata.py`
10. `10_wrongformat.py`
11. `11_fixdata.py`
12. `12_duplicate.py`
13. `13_correlation.py`
14. `14_plotting.py`

## pandas main
### 4 series
```python
p1 = PdSeries()
print(p1.series())
print(p1.series()[1])
print(p1.labels())
print(p1.labels()["y"])
print(p1.dic())
print(p1.dic2())
print(p1.multi())
```
### 5 data frame
```python
res = DataFrame()
print(res.load_data())
print(res.loc_row(res.a,0))  # loc[] --> locate row
print(res.loc_row(res.a,[0,1]))
print(res.name_index())
print(res.read_file())
```
### 6 read csv
```python
res = ReadCSV()
print(res.to_str())
print(res.system_max())
print(res.max_rows())
```
### 7 read json
```python
res = ReadJson()
print(res.to_str())
print(res.entire_str())
print(res.json_data(res.data))
```
### 8 analyzing data
```python
res = Analyst()
print(res.return_head(5))
print(res.return_tail())
print(res.return_info())
```
### 9 cleaning empty data
```python
res = CleanData()
print(res.read_data())
print(res.remove_row())
print(res.remove_inplace())
print(res.replace_empty(130))
print(res.replace_empty({"Calories":130}))
print(res.replace_mean("Calories"))
print(res.replace_median("Calories"))
print(res.replace_mode("Calories",0))
```
### 10 cleaning wrong format
```python
res = WrongFormat()
print(res.to_date('Date'))
print(res.remove_null('Date'))
```
### 11 cleaning wrong data
```python
res = FixData()
print(res.read_csv())
print(res.replace_value(7,'Duration',45))
print(res.replace_loop('Duration',120))
print(res.remove_row('Duration',120))
```
### 12 removing duplicates
```python
res = Duplicates()
print(res.dup_bool())
print(res.dup_remove())
```
### 13 Correlations
```python
res = Correlations()
print(res.read_csv())
print(res.corr_csv())
```
### 14 Plotting
```python
res = Plotting()
res.return_plot()
res.scatter_plot('Duration','Calories')
res.scatter_plot('Duration','Maxpulse')
res.plot_attr('Duration','hist')
```
## my_numpy list

0. `0_basenumpy.py`
1. `1_ndarrays.py`
2. `2_datatype.py`
3. `3_copyview.py`
4. `4_arrayshape.py`
5. `5_arrayiterate.py`
6. `6_arrayjoin.py`
7. `7_arraysplit.py`

## numpy main

### 1 NdArrays
```python
res = NdArrays()
a = 42
b1 = [1, 2, 3, 4]
b2 = [1, 2, 3, 4, 5, 6, 7]
c = [[1,2,3,4,5], [6,7,8,9,10]]
d = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

arr, dim = res.array_info(a)

arr, dim = res.array_info(b1)
res.return_index(arr[0])
res.return_index(arr[1])
res.return_index(arr[2]+arr[3])

arr, dim = res.array_info(b2)
res.return_slice(arr[1:5])
res.return_slice(arr[1:5:2])
res.return_slice(arr[4:]) # 567
res.return_slice(arr[:4]) # 1234
res.return_slice(arr[::2])
#negative slice element example
res.return_slice(arr[-3:-1]) # 56

arr, dim = res.array_info(c)
res.return_index(arr[0,1])
res.return_index(arr[1,4])
#negative index sample
res.return_index(arr[1,-1])
# Slice 2-D arrays
res.return_slice(arr[1,1:4])
res.return_slice(arr[0:2, 2])
res.return_slice(arr[0:2,1:4])

arr, dim = res.array_info(d)
res.return_index(arr[0,1,2])
```
### 2 DataType
```python
res = DataType()
a = [1,2,3,4]
b = ['apple', 'banana', 'cherry']
e = [1.1, 2.1, 3.1]
bo = [1,0,3]
#int32
res.ini_np(a)
res.dtype_readable(a)
#unicode string
res.ini_np(b)
res.dtype_readable(b)
#byte string
c = res.ini_np(a,dtype='S')
res.dtype_readable(c)
#float64
d = res.ini_np(a,dtype='f8')
res.dtype_readable(d)
#after creation, make a new copy, useful when convert existing data to a different dtype
# e float64 -> f int32
f = res.ini_np(e,return_print=False).astype(int) # int = 'i'
res.ini_np(f)
res.dtype_readable(f)
# integer -> boolean
g = res.ini_np(bo,return_print=False).astype(bool)
res.ini_np(g)
res.dtype_readable(g)
```
### 3 CopyView
```python
a = [1,2,3,4,5]
res = CopyView(a)
res.return_copy()
res.return_view(an=0,cn=31,change_view=True)
res.return_view(an=0,cn=42,change_arr=True)
res.return_compare()
```
### 4 ArrayShape
```python
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
res = ArrayShape(a)
res.return_shape()
b = [1,2,3,4]
res2 = ArrayShape(b,ndmin=5)
res2.return_shape()
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res3 = ArrayShape(c)
res3.return_reshape(4,3)
res3.return_reshape(2,3,2)
d = [1, 2, 3, 4, 5, 6, 7, 8]
res4 = ArrayShape(d)
# #cannot reshape array of size 8 into shape (3,3)
# res4.return_reshape(3,3)
res4.return_reshape(2,2,-1)
e = [[1, 2, 3], [4, 5, 6]]
res5 = ArrayShape(e)
res5.return_reshape(-1) # -> [1,2,3,4,5,6]
```
### 5 ArrayIterate
```python
arr1 = [1,2,3]
res1 = ArrayIterate(arr1)
res1.return_1d()
arr2 = [[1, 2, 3], [4, 5, 6]]
res2 = ArrayIterate(arr2)
res2.return_2d()
arr3 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
res3 = ArrayIterate(arr3)
res3.return_3d()
arr4 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
res4 = ArrayIterate(arr4)
res4.return_nditer()
res4.return_nditer(flags=['buffered'],op_dtypes=['S'])
arr5 = [[1, 2, 3, 4], [5, 6, 7, 8]]
res5 = ArrayIterate(arr5)
# (slice(None),slice(None,None,2)) == [:, ::2]
res5.return_nditer(slice_obj=(slice(None),slice(None,None,2)))
res6 = ArrayIterate(arr1)
res6.return_nd()
res7 = ArrayIterate(arr5)
res7.return_nd()
```
### 6 ArrayJoin
```python
arr1 = [1,2,3]
arr2 = [4,5,6]
res1 = ArrayJoin(arr1,arr2)
print('concatenate()')
res1.return_con()
arr3 = [[1, 2], [3, 4]]
arr4 = [[5, 6], [7, 8]]
res2 = ArrayJoin(arr3,arr4)
res2.return_con()
res2.return_con(axis=1)
print('stack()')
res1.return_stack()
res1.return_stack(axis=1)
print('hstack()')
res1.return_hstack()
print('vstack()')
res1.return_vstack()
print('dstack()')
res1.return_dstack()
```
### 7 ArraySplit
```python

```
## my_matplotlib list

## matplotlib main