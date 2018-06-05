
import pyodbc

server = 'vitelemetry.database.windows.net'
database = 'topics'
username = 'royir'
password = 'Id034545111'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


#cursor.execute("select * from EntityTypes")
#row = cursor.fetchone()
#while row:
#    print(str(row[0]) + " " + str(row[1]))
#    row = cursor.fetchone()


file = open("C:\\Users\\royir\\Documents\\Media AI\\Topics\\Yago\\...", 'r')
j = 0
while j <= 1582520:
    try:
        line = file.readline()
        if line.find("rdf:type\t") != -1 and line.find("wikicat_") == -1:
            j = j + 1
    except:
        continue
print("j is " + str(j))


i = 1
sqlQuery = ""
while line:
    try:
        line = file.readline()
        if line.find("rdf:type\t") == -1 or line.find("wikicat_") != -1:  # if not rdf:type, continue to next line
            continue
        line = line.replace("<", "").replace(">", "").replace("'", "''")
        entity = line.split("\t")[1]
        entityType = line.split("\t")[3]
        print(line)
        print(entity)
        print(entityType)
        sqlQuery = sqlQuery + ("if not exists (select * from EntityTypes where entity='"+entity+"' and entityType='"+entityType+"')"
                               " begin insert EntityTypes values('"+entity+"','"+entityType+"') end;")
        print(i)
        i = i+1
        if 0 == i % 5000:
            cursor.execute(sqlQuery)
            cnxn.commit()
            sqlQuery = ""
            i = 1
    except:
        print("derror")
        continue

file.close()








#os.system("C:\\Users\\royir\\Documents\\Media AI\\BingCelebs\\Debug\\RecognitionModelExe.exe "
#          "..\\CelebsTestImages\\sam-lee.jpg")

