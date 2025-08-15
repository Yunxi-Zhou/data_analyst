from my_pandas import PdSeries
from my_pandas import DataFrame
from my_pandas import ReadCSV
from my_pandas import ReadJson
from my_pandas import Analyst
from my_pandas import CleanData
from my_pandas import WrongFormat
from my_pandas import FixData

if __name__ == '__main__':
    # 4 series
    # p1 = PdSeries()
    # print(p1.series())
    # print(p1.series()[1])
    # print(p1.labels())
    # print(p1.labels()["y"])
    # print(p1.dic())
    # print(p1.dic2())
    # print(p1.multi())

    # 5 data frame
    # res = DataFrame()
    # print(res.load_data())
    # print(res.loc_row(res.a,0))  # loc[] --> locate row
    # print(res.loc_row(res.a,[0,1]))
    # print(res.name_index())
    # print(res.read_file())

    # 6 read csv
    # res = ReadCSV()
    # print(res.to_str())
    # print(res.system_max())
    # print(res.max_rows())

    # 7 read json
    # res = ReadJson()
    # print(res.to_str())
    # print(res.entire_str())
    # print(res.json_data(res.data))

    # 8 analyzing data
    # res = Analyst()
    # print(res.return_head(5))
    # print(res.return_tail())
    # print(res.return_info())

    # 9 cleaning empty data
    # res = CleanData()
    # print(res.read_data())
    # print(res.remove_row())
    # print(res.remove_inplace())
    # print(res.replace_empty(130))
    # print(res.replace_empty({"Calories":130}))
    # print(res.replace_mean("Calories"))
    # print(res.replace_median("Calories"))
    # print(res.replace_mode("Calories",0))

    # 10 cleaning wrong format
    # res = WrongFormat()
    # print(res.to_date('Date'))
    # print(res.remove_null('Date'))

    # 11 cleaning wrong data