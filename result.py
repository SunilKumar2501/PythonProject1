from excel_processor import ExcelProcessor

# Define file paths
file1 = r"C:\Users\sunil\Downloads\telerik-excel-export (5).xlsx"
file2 = r"C:\Users\sunil\Downloads\practice.xlsx"
output_file = r"C:\Users\sunil\Downloads\practice.xlsx"

# Initialize the processor
processor = ExcelProcessor(file1, file2)

# User input for Gateway Id
gateway_id = input("Enter the Gateway Id: ")

# Process and save data
processor.save_to_excel(output_file, gateway_id)
