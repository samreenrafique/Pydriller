# # Database Connection 20-10-2022
# import datetime
# import mysql.connector
#
# name = input("Please Enter Your Name : ")
# attendence = int(input("How many days you're present? "))
# perday = 1200
#
# totalsalary = attendence * perday
# cureent = datetime.datetime.now()
# print(f"{name} your Salary is Rs. {totalsalary}")
#
# # Data Saved in File
# f = open("EmployeeRecord.txt", "a")
# f.write(f"{name} Salary is Rs . {totalsalary}\nRecord Saved at {cureent}\n")
# f.close()
#
# # Database Connection
# DbCon = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password= "",
#     database = "employeedb"
# )
#
# cursor = DbCon.cursor()
#
# insert_query = "INSERT INTO `employeerecord`( `Name`, `Attendance`, `perday`, `TotalSalary`, `Currenttime`) VALUES (%s,%s,%s,%s,%s)"
# meri_value = [name, attendence, perday, totalsalary, cureent]
#
# cursor.execute(insert_query,meri_value)
# DbCon.commit()
# DbCon.close()

# 22 - October - 2022
# import pandas
# from openpyxl.workbook import Workbook
# import lxml
#
# stu = {
#     "name" : ["Ahad","Muzammil","Zaryab","Amin","Mahad"],
#     "gender" : ["Male","Male","MAle","Male","Male"],
#     "Age":[12,44,23,56,12]
# }
#
# print(stu)
# convert_table = pandas.DataFrame(stu)
# print(convert_table)
#
#
# # Save Data in Excel
# convert_table.to_excel("MEriFile.xlsx",index=False)
# # Save Data in CSV
# convert_table.to_csv("Merifile.csv")
# # Save Data in XML
# convert_table.to_xml("merifile.xml")
# # Save Data in JSON
# convert_table.to_json("merifile.js")


# 25-Oct-2022
# Fetch commits from Github
# Pydriller


from pydriller import Repository
import pandas
import lxml
# Make dishes
Commitwalekanaam, Commitkidate, Commitmsg = [] , [] , []
# Fetch Data

for i in Repository(path_to_repo="https://github.com/nomadkode/nomad-shopping-cart.git").traverse_commits():
    Commitwalekanaam.append(i.committer.name)
    Commitkidate.append(i.committer_date)
    Commitmsg.append(i.msg)

#
# Save Data in Dictionary
GitHub_Dict = {
    "CommitterName" : Commitwalekanaam,
    "CommitDate" : Commitkidate,
    "Message" : Commitmsg

}
# Save data into CSV
Convert_to_Table = pandas.DataFrame(GitHub_Dict)
Convert_to_Table.to_csv("RepositoryKaData.csv",index= False)
Convert_to_Table.to_xml("RepositoryKaData.xml")

print("Data Saved Successfully")















