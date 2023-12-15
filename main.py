import psycopg2


class PostgresDB:
    def __init__(self, dbname, username, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = username
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_all(self):
        return self.cursor.fetchall()

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()


class StatisticsProvider:
    def __init__(self):
        self.database = PostgresDB(dbname='db_lab3_petrov', username='postgres', password='1000dollars')

    def execute_query(self, query):
        self.database.connect()
        self.database.execute_query(query)
        result = self.database.fetch_all()
        self.database.close_connection()

        return result

    def get_conversation_messages_count(self):
        query = """
            select name, count(message_id) as message_count
            from conversation c
                left join message m on c.conversation_id = m.conversation_id
            group by name;
        """

        return self.execute_query(query)

    def get_user_messages_count(self):
        query = """
            select username, count(message_id)
            from users u
                left join message m on u.user_id = m.sender_id
            group by username;
        """

        return self.execute_query(query)

    def get_daily_messages_count(self):
        query = """
            select DATE(timestamp) as date, COUNT(*) as message_count
            from message
            where DATE(timestamp) between '2023-12-12' and '2023-12-15'
            group by DATE(timestamp)
            order by DATE(timestamp);
        """

        return self.execute_query(query)


statistics_provider = StatisticsProvider()
print(statistics_provider.get_conversation_messages_count())
print(statistics_provider.get_user_messages_count())
print(statistics_provider.get_daily_messages_count())
