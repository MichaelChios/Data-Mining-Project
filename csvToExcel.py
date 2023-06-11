import pandas as pd

def toExcel(data, name):
    # Create a new Excel file
    excel_file = pd.ExcelWriter(f'{name}.xlsx', engine='xlsxwriter')

    # Write the data to a sheet in the Excel file
    data.to_excel(excel_file, index=False, sheet_name='Sheet1')

    # Save the Excel file
    excel_file.save()

    print("Data has been successfully inserted into the Excel file.")