import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('mysql+pymysql://root:sagarmendi1988#@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

file_counter_table = sqlalchemy.Table('file_counter', metadata, autoload_with=engine)


# find max number of total files and later link it to find which day that happened
max=sqlalchemy.select((sqlalchemy.func.max(file_counter_table.columns.total)))



result_proxy=connection.execute(max)
countresult = result_proxy.fetchone()
my_value = countresult[0]

#pprint(my_value)



# select the files where total=max
query = sqlalchemy.select((file_counter_table.columns.day)).where(file_counter_table.columns.total == my_value)
result_proxy=connection.execute(query)
countresult = result_proxy.fetchone()
my_value = countresult[0]

print(f"the date where max number of files where moved was '{my_value}'")