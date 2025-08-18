# Data Analyst Learning Notes

---

Pandas

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
from my_pandas import PdSeries()
p1 = PdSeries()
print(p1.series())
print(p1.series()[1])
print(p1.labels())
print(p1.labels()["y"])
print(p1.dic())
print(p1.dic2())
print(p1.multi())

### 5 data frame
res = DataFrame()
print(res.load_data())
print(res.loc_row(res.a,0))  # loc[] --> locate row
print(res.loc_row(res.a,[0,1]))
print(res.name_index())
print(res.read_file())

### 6 read csv
res = ReadCSV()
print(res.to_str())
print(res.system_max())
print(res.max_rows())

### 7 read json
res = ReadJson()
print(res.to_str())
print(res.entire_str())
print(res.json_data(res.data))

### 8 analyzing data
res = Analyst()
print(res.return_head(5))
print(res.return_tail())
print(res.return_info())

### 9 cleaning empty data
res = CleanData()
print(res.read_data())
print(res.remove_row())
print(res.remove_inplace())
print(res.replace_empty(130))
print(res.replace_empty({"Calories":130}))
print(res.replace_mean("Calories"))
print(res.replace_median("Calories"))
print(res.replace_mode("Calories",0))

### 10 cleaning wrong format
res = WrongFormat()
print(res.to_date('Date'))
print(res.remove_null('Date'))

### 11 cleaning wrong data
res = FixData()
print(res.read_csv())
print(res.replace_value(7,'Duration',45))
print(res.replace_loop('Duration',120))
print(res.remove_row('Duration',120))

### 12 removing duplicates
res = Duplicates()
print(res.dup_bool())
print(res.dup_remove())

### 13 Correlations
res = Correlations()
print(res.read_csv())
print(res.corr_csv())