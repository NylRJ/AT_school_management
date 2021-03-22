###
# Classroom RPC Services
from nameko.rpc import rpc, RpcProxy
import sqlite3


class DBConnection:
    def __init__(self, dbname):
        self.con = sqlite3.connect(dbname)
        self.cursor = self.con.cursor()

    def __del__(self):
        self.con.close()


class ClassRoomService:
    name = "classroom_service"
    db = DBConnection("classroom.db")

    @rpc
    def get_date(self, *args):
        query = "SELECT DISTINCT date FROM classroom;"
        self.db.cursor.execute(query)
        results = self.db.cursor.fetchall()
        return results
