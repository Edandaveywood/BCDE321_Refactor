import aiomysql
from beautifultable import BeautifulTable

import pymysql
from converter import Converter

# from distutils.sysconfig import get_python_lib
# print(get_python_lib())

class MySQL:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, connection):
        self.__connection = connection

    async def create_connection(self, db_config):
        self.__connection = await aiomysql.connect(**db_config)
        print("Connection established...")

    def close_connection(self):
        self.__connection.close()

    async def create_cursor(self):
        self.__cursor = await self.__connection.cursor()

    async def close_cursor(self):
        await self.__cursor.close()

    async def process_query(self, query):
        await self.__cursor.execute(query)
        return f'Query "{query}" processed!'

    async def insert_records(self, query, data):
        return await self.__cursor.executemany(query, data)

    async def fetch_all_records(self, query):
        await self.process_query(query)
        return await self.__cursor.fetchall()

    async def fetch_one(self, query):
        await self.process_query(query)
        return await self.__cursor.fetchone()


async def testing_connection():
    db_config = {
        'host': 'ara-mysql.mysql.database.azure.com',
        'port': 3306,
        'db': 'uml_resource',
        'user': 'ara_user@ara-mysql',
        'password': 'Test1234'
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)
        print("Connection build successfully")

    except pymysql.Error as err:

        sqlstate = err.args[1]
        print(sqlstate)

    else:

        await mysql.create_cursor()
        db_ver_query = "SELECT VERSION()"
        await mysql.process_query(db_ver_query)
        r = await mysql.fetch_one(db_ver_query)
        print(f'Database version: {r[0]}')

        db_list_query = "SHOW DATABASES"
        await mysql.process_query(db_list_query)
        r = await mysql.fetch_all_records(db_list_query)

        db_list = []
        for i in range(len(r)):
            db_list.append(r[i][0])
        print(f'Database list: {db_list}')

        print("Connection closing...")
        # await mysql.close_cursor()
        # mysql.close_connection()


    # conn = await aiomysql.connect(host='ara-mysql.mysql.database.azure.com', port=3306,
    #                               user='ara_user@ara-mysql', password='Test1234', db='uml_resource'
    #                               )
    # async with conn.cursor() as cur:
    #     await cur.execute("SELECT VERSION()")
    #     r = await cur.fetchone()
    #     print(f'Database version: {r[0]}')
    #
    #     await cur.execute("SHOW DATABASES")
    #     r = await cur.fetchall()
    #
    #     db_list = []
    #     for i in range(len(r)):
    #         db_list.append(r[i][0])
    #     print(f'Database list: {db_list}')

        # r = await cur.fetchall()
        # print(r)
        # for row in await cur.fetchall():
        #     # yield row
        #     print(row)



        # table.columns.header = [i[0] for i in r.description]
        # for i in r:
        #     table.rows[i] = list[i]


        # header1 = [i[0] for i in r.description]
        # rows1 = [list(i) for i in r]
        # rows1.insert(0, header1)
        # print(rows1)

    # await conn.close()



async def testing_select_all():
    db_config = {
        'host': 'ara-mysql.mysql.database.azure.com',
        'port': 3306,
        'db': 'uml_resource',
        'user': 'ara_user@ara-mysql',
        'password': 'Test1234'
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)
        print("Connection build successfully")

    except pymysql.Error as err:

        sqlstate = err.args[1]
        print(sqlstate)

    else:

        await mysql.create_cursor()
        table_all_query = "SELECT * FROM uml_resource.class_info"
        await mysql.process_query(table_all_query)
        r = await mysql.fetch_all_records(table_all_query)

        print("Select all data from class_info table...")

        table = BeautifulTable()
        table.columns.header = ['id', 'name', 'attr_num', 'method_num']


        my_row_list = []
        for i in range(len(r)):
            my_row_list.append(str(i))
            # print(str(i))
            table.rows.append(list(r[i]))
        table.rows.header = my_row_list
        print(table)

        print("Connection closing...")

        # db_list = []
        # for i in range(len(r)):
        #     db_list.append(r[i])
        #     # yield row
        # print(db_list)


        # db_list = []
        # for i in range(len(r)):
        #     db_list.append(r[i][0])
        # print(f'Database list: {db_list}')

        # await mysql.close_cursor()
        # mysql.close_connection()


async def testing_btf_table():

    con = pymysql.connect('ara-mysql.mysql.database.azure.com', 'ara_user@ara-mysql',
                          'Test1234', 'uml_resource')
    print("Connection established...")

    try:

        with con.cursor() as cur:
            print("Connection build successfully")

            cur.execute('DESCRIBE uml_resource.class_info')
            # print(cur.description)
            print("Beatiful table below")
            r = cur.fetchall()

            table = BeautifulTable()

            my_col_list = []
            for i in range(len(cur.description)):
                # print(str(i))
                my_col_list.append(cur.description[i][0])
            table.columns.header = my_col_list

            my_row_list = []
            for i in range(len(r)):
                my_row_list.append(str(i))
                # print(str(i))
                table.rows.append(list(r[i]))
            table.rows.header = my_row_list

            print(table)

            print("Connection closing...")

    except pymysql.Error as err:
        sqlstate = err.args[1]
        print(sqlstate)


async def main1():
    await testing_connection()

async def main2():
    await testing_select_all()

async def main3():
    await testing_btf_table()



async def testing_method_all():
    db_config = {
        'host': 'ara-mysql.mysql.database.azure.com',
        'port': 3306,
        'db': 'uml_resource',
        'user': 'ara_user@ara-mysql',
        'password': 'Test1234'
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)
        print("Connection build successfully")

    except pymysql.Error as err:

        sqlstate = err.args[1]
        print(sqlstate)

    else:

        await mysql.create_cursor()
        table_all_query = "SELECT * FROM uml_resource.class_method"
        await mysql.process_query(table_all_query)
        r = await mysql.fetch_all_records(table_all_query)

        print("Select all data from class_method table...")

        table = BeautifulTable()
        table.columns.header = ['id', 'method']


        my_row_list = []
        for i in range(len(r)):
            my_row_list.append(str(i))
            # print(str(i))
            table.rows.append(list(r[i]))
        table.rows.header = my_row_list
        print(table)

        print("Connection closing...")


async def main4():
    await testing_method_all()




async def testing_attr_all():
    db_config = {
        'host': 'ara-mysql.mysql.database.azure.com',
        'port': 3306,
        'db': 'uml_resource',
        'user': 'ara_user@ara-mysql',
        'password': 'Test1234'
    }

    mysql = MySQL()

    try:

        await mysql.create_connection(db_config)
        print("Connection build successfully")

    except pymysql.Error as err:

        sqlstate = err.args[1]
        print(sqlstate)

    else:

        await mysql.create_cursor()
        table_all_query = "SELECT * FROM uml_resource.class_attr"
        await mysql.process_query(table_all_query)
        r = await mysql.fetch_all_records(table_all_query)

        print("Select all data from class_attr table...")

        table = BeautifulTable()
        table.columns.header = ['id', 'attributes']


        my_row_list = []
        for i in range(len(r)):
            my_row_list.append(str(i))
            # print(str(i))
            table.rows.append(list(r[i]))
        table.rows.header = my_row_list
        print(table)

        print("Connection closing...")


async def main5():
    await testing_attr_all()