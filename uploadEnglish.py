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


file = open("C:\\Users\\royir\\Documents\\Media AI\\Topics\\Yago\\yagoAndWordnetTypes.tsv", 'r')

j = 0;
while j<=16685365:
    file.readline()
    j = j + 1


i = 1
line = "dummy"
sqlQuery = ""
while line:
    try:
        line = file.readline()
        line = line.replace("<", "").replace(">", "").replace("'", "''")
        entity = line.split("\t")[0]
        entityType = line.split("\t")[1]
        print(line)
        print(entity)
        print(entityType)
        # sqlQuery = sqlQuery + ("if not exists (select * from YagoWordnetTypes where wikiid='"+entity+"' and class='"+entityType+"')"
        #                       " begin insert YagoWordnetTypes values('"+entity+"','"+entityType+"') end;")
        sqlQuery = sqlQuery + ("insert YagoWordnetTypesEn values('"+entity+"','"+entityType+"');")
        print(i)
        i = i+1
        if 0 == i % 500:
            cursor.execute(sqlQuery)
            cnxn.commit()
            sqlQuery = ""
            i = 1
    except:
        print("error")
        continue

file.close()
