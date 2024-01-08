class DBConnection:

    def __enter__(self):
        print('connecting to DB...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('disconnected from DB...')

with DBConnection() as conn:
    print('selecting from DB....')