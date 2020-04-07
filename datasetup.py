import os

class DataSetup:
    def __init__(self):
        try:
            os.makedirs('data')
        except FileExistsError:
            print('directory exist')
