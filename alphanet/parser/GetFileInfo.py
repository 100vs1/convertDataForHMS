import xlrd


class GetFileInfo:
    filePath = "D:\\alphaParser\\"

    xls_format = "xls"
    xlsx_format = "xlsx"

    def __init__(self):
        print("Complete object create.")

    @staticmethod
    def get_file_list(self):
        print (self.filePath)