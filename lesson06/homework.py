

class FileWorking:
    def __enter__(self):
        open('example.txt', 'r')
        print(text)

    def __exit__(self, exc_type, exc_val, exc_tb, f):
        open('example.txt', 'r').close()


with FileWorking as fw:
    print('OK')