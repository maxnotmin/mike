import os, sys
import csv
import functools
import pathlib



class UCDSheetRead:
    """
    This class will be about to create a JSON file from a EXCEL or CSV file and will be able to determine
    which type of Sheet Type it is and then perform the specific methods based upon the type

    """

    def __init__(self, file_path='', file_name='', sheet_type='', file_found=False):
        self.file_path = file_path
        self.file_name = file_name
        self.sheet_type = sheet_type
        self.file_found = file_found



    def verify_file_type(self):

        print("IN VERIFY FILE TYPE: ", self.file_name)
        if self.file_name.endswith('.csv'):
            print("FILE TYPE CSV VERIFIED | READ CVS")
        elif self.file_name.endswith('.xls'):
            print("FILE XLS VERIFIELD | READ EXCEL")
        else:
            print("THIS SPREAD SHEET FILE CAN NOT BE USED")

    def verify_full_path(self):
        cur_dir = os.getcwd()
        full_path = cur_dir + "/" + self.file_path + "/" + self.file_name
        print("FULL PATH: ", full_path)
        check_full_path = pathlib.Path(full_path).is_file()
        print("FULL PATH IS VERIFIED: ", check_full_path)

        if check_full_path:
            return full_path

    def read_csv(self):
        the_full_path = self.verify_full_path()

        with open(the_full_path) as csvfile:
            the_reader = csv.reader(csvfile, delimiter=',')
            for row in the_reader:
                print(row)

    def read_excel(self):
        pass

    def determind_sheet_meth(self):
        pass


    def convert_csv_to_dict(the_file):
        """
        We want to read a CSV FILE, that should be 2 columns and turn it into a dictionary
        EXAMPLE OUTPUT:
        the_dict = {'date':'Saturday, April 14, 2018',
                    'title': 'Art Bell | Syria and Trump |Ancient Giants',
                     'youtube': 'https://www.youtube.com/watch?v=_BV8TT6-9fE'}
        :arg the_file : CSV

        :return dict()
        """
        the_dict = dict()
        for i, k in the_file:
            the_dict = the_dict[i][k]



    def convert_dict_to_text(the_dict):
        pass


def run():
    """

    :return: Call Other function to run
    """
    pass


if __name__ == "__main__":
    #TODO READ CSV FILE
    """
    We'll probably use the 'with open' sytax to make sure the file is closed with the script is done
    link: https://docs.python.org/2/library/csv.html

    """
    x = UCDSheetRead(file_path='csv', file_name=r'OBDM 604_04-26-18.csv')

    print("OBEJCT ATTS: ", x.file_name, x.file_path, x.verify_file_type())
    x.read_csv()

