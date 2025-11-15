import dataframe_image as dfi

def create_image(dataframe, name:str):
    dfi.export(dataframe, name, table_conversion='matplotlib')
