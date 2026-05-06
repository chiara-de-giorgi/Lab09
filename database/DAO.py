from database.DB_connect import DBConnect
from model.airports import Airports


#from model.arco import Arco


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAeroporti():
        conn=DBConnect.get_connection()
        cursor=conn.cursor(dictionary=True)

        result=[]   #Lista di aeroporti

        query="""select * from airports"""

        cursor.execute(query)

        for row in cursor:
            result.append(Airports(**row)) #

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllEdgesPesati(idMap, x):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select ORIGIN_AIRPORT_ID as o1, DESTINATION_AIRPORT_ID as o2, AVG(DISTANCE) as peso
                    from flights f 
                    group by ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID
                     HAVING AVG(DISTANCE) >= %s"""


        cursor.execute(query, (x, ))

        for row in cursor:
            aeroporto1=idMap[row["o1"]]
            aeroporto2 = idMap[row["o2"]]
            peso = row["peso"]
            result.append((aeroporto1, aeroporto2, peso))

        cursor.close()
        conn.close()


        return result