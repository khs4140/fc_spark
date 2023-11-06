# 패키지 가져오기
from pyspark import SparkConf, SparkContext
import pandas as pd

# Spark 설정
conf = SparkConf().setMaster('local[8]').setAppName('uber-date-trips') # [4] 4개 Thread 사용하여 연산
sc = SparkContext(conf=conf)

# 사용 데이터
# folder_name = '/Users/hangdori/_PML/fc_spark/data'
folder_name = '/Users/lifelog/_PML/fc_spark/data'
file_name = 'fhvhv_tripdata_2020-03.csv'

# 데이터 파싱
lines = sc.textFile(f"file:///{folder_name}/{file_name}") # RDD(Resilient Distributed Dataset)
header = lines.first()
filtered_lines = lines.filter(lambda x: x != header)

# 필요한 부분만 선택&세기
dates = filtered_lines.map(lambda x: x.split(",")[4].split(" ")[0])
result = dates.countByValue()

pd.Series(result, name='trips').to_csv('trips_date.csv')
