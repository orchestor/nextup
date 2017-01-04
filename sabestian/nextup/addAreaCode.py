import xlrd
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='bhavya', db='nextup', autocommit=True)
cur = conn.cursor()
wb = xlrd.open_workbook("area-code-Divison.xlsx")
for sheet in wb.sheets():
	numberOfRows = sheet.nrows
	counter = 1
	while (counter < numberOfRows):
		cur.execute("INSERT INTO locality_areacodemapping VALUES ('%d', '%d', '%d', '%s', '%s');" % (counter + 1, sheet.cell(counter, 0).value, sheet.cell(counter, 1).value, sheet.cell(counter, 2).value, (sheet.cell(counter, 3).value).replace(" ", "")))
		counter += 1 