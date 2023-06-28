#clean the desktop
# get my tools
from pathlib import Path
import pprint
import sqlalchemy
import time 

def sum(png,jpg,py,jpeg,pdf,doc,html,xls):
    sum=png+jpg+py+jpeg+pdf+doc+html+xls
    return sum

count_png=0
count_jpg=0
count_py=0
count_jpeg=0
count_pdf=0
count_doc=0
count_html=0
count_xls=0

dictionary={}

#locate the desktop
desktop = Path().home().joinpath("OneDrive\Escritorio")
print(desktop)


#identify type of files
for f in desktop.iterdir():
    if f.suffix==".png":
        count_png+=1
        
    elif f.suffix==".jpg":
        count_jpg+=1

    elif f.suffix==".py":
        count_py+=1

    elif f.suffix==".jpeg":
        count_jpeg+=1

    elif f.suffix==".pdf":
        count_pdf+=1

    elif f.suffix==".doc":
        count_doc+=1

    elif f.suffix==".html":
        count_html+=1

    elif f.suffix==".xls":
        count_xls+=1

    else:
        pass


# collect each type in a dictionary
dictionary={".png files":count_png , ".jpg files":count_jpg, ".py files":count_py, ".jpeg files":count_jpeg, ".pdf files":count_pdf,
            ".doc files":count_doc, ".html files":count_html, ".xls files":count_xls, "date":time.strftime('%Y-%m-%d %H:%M:%S')}

# print the dictionary
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(dictionary)


# route to the database for file_counter in MySQL
engine = sqlalchemy.create_engine('mysql+pymysql://root:sagarmendi1988#@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()

# path to the folder
file_counter_table = sqlalchemy.Table('file_counter', metadata, autoload_with=engine)

date=time.strftime('%Y-%m-%d %H:%M:%S')
total_sum=sum(count_png,count_jpg,count_py,count_jpeg,count_pdf,count_doc,count_html,count_xls)

# insert the new count of files, new row
query = sqlalchemy.insert(file_counter_table).values(png_files=count_png, jpg_files=count_jpg, py_files=count_py, jpeg_files=count_jpeg,
                                                     pdf_files=count_pdf, doc_files=count_doc, html_files=count_html, xls_files=count_xls,
                                                     total=total_sum, day=date)
result_proxy = connection.execute(query)
result_proxy1=connection.commit() 

#-----------------------------------------------------------------------------------------------------------------------------------------------
# Get the total number of files since the begining

query = sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.total)))
q_png=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.png_files)))
q_jpg=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.jpg_files)))
q_py=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.py_files)))
q_jpeg=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.jpeg_files)))
q_pdf=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.pdf_files)))
q_doc=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.doc_files)))
q_html=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.html_files)))
q_xls=sqlalchemy.select((sqlalchemy.func.sum(file_counter_table.columns.xls_files)))

result_proxy=connection.execute(query)
result_png=connection.execute(q_png)
result_jpg=connection.execute(q_jpg)
result_py=connection.execute(q_py)
result_jpeg=connection.execute(q_jpeg)
result_pdf=connection.execute(q_pdf)
result_doc=connection.execute(q_doc)
result_html=connection.execute(q_html)
result_xls=connection.execute(q_xls)

result_proxy1=connection.commit() 


countresult = result_proxy.fetchone()
my_value_total = countresult[0]

c_png=result_png.fetchone()
my_value_png=c_png[0]

c_jpg=result_jpg.fetchone()
my_value_jpg=c_jpg[0]

c_py=result_py.fetchone()
my_value_py=c_py[0]

c_jpeg=result_jpeg.fetchone()
my_value_jpeg=c_jpeg[0]

c_pdf=result_pdf.fetchone()
my_value_pdf=c_pdf[0]

c_doc=result_doc.fetchone()
my_value_doc=c_doc[0]

c_html=result_html.fetchone()
my_value_html=c_html[0]

c_xls=result_xls.fetchone()
my_value_xls=c_xls[0]


pp.pprint(f" the total amount of files is {my_value_total}")
pp.pprint(f" the total amount of 'png' files is {my_value_png}")
pp.pprint(f" the total amount of 'jpg' files is {my_value_jpg}")
pp.pprint(f" the total amount of 'py' files is {my_value_py}")
pp.pprint(f" the total amount of 'jpeg' files is {my_value_jpeg}")
pp.pprint(f" the total amount of 'pdf' files is {my_value_pdf}")
pp.pprint(f" the total amount of 'pdf' files is {my_value_doc}")
pp.pprint(f" the total amount of 'html' files is {my_value_html}")
pp.pprint(f" the total amount of 'xls' files is {my_value_xls}")
          
          
#------------------------------------------------------------------------------------------------------
# Try to find which day was the max number of total files
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


#----------------------------------------------------------------------------------------------

lista=[my_value_png,my_value_jpg,my_value_py,my_value_jpeg,my_value_pdf,my_value_doc,my_value_html,my_value_xls]

count=0
for i in lista:
    if i>count:
        count=i
    else:
        pass

if count==my_value_png:
    pp.pprint(f"The most common file is 'png' with a total amount of {count}")

elif count==my_value_jpg:
    pp.pprint(f"The most common file is 'jpg' with a total amount of {count}")

elif count==my_value_py:
    pp.pprint(f"The most common file is 'py' with a total amount of {count}")

elif count==my_value_jpeg:
    pp.pprint(f"The most common file is 'jpeg' with a total amount of {count}")

elif count==my_value_pdf:
    pp.pprint(f"The most common file is 'pdf' with a total amount of {count}")

elif count==my_value_doc:
    pp.pprint(f"The most common file is 'doc' with a total amount of {count}")

elif count==my_value_html:
    pp.pprint(f"The most common file is 'html' with a total amount of {count}")

else:
    pp.pprint(f"The most common file is 'xls' with a total amount of {count}")




