import datetime
import os
import pandas as pd

class Categories: # thu tu tao obj 1
    """
    This class contain CategoryID, CategoryName
    and Description from Categories table
    """
    __index = 0
    def __init__(self, name, des):
        self.__catID = Categories.get_index('Categories')
        self.__validate_type(name, des)
        self.cat_name = name 
        self.cat_des = des
    
    @classmethod
    def get_index(cls,table_name):
        file_path = '/content/' + table_name + '.csv'
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            cls.__index  = len(pd.read_csv(file_path)) + 1
        else:
            cls.__index += 1

        return cls.__index

    @staticmethod
    def __validate_type(name, description) -> None:
        assert type(name) == str
        assert type(description) == str


    def get_id(self):
        return self.__catID


    def __str__(self):
        return f'Categorical : {self.get_id()},{self.cat_name}, {self.cat_des}'