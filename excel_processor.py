import pandas as pd

class ExcelProcessor:
    def __init__(self, file1_path, file2_path):
        self.df1 = pd.read_excel(file1_path)
        self.df2 = pd.read_excel(file2_path)

    def process(self, gateway_id):
        filtered_data = self.df1[self.df1["Gateway Id"] == gateway_id]
        if filtered_data.empty:
            raise ValueError(f"Gateway Id '{gateway_id}' not found in the data.")
        combined_data = pd.concat([filtered_data, self.df2])
        return combined_data

    def save_to_excel(self, output_path, gateway_id):
        try:
            result = self.process(gateway_id)
            result.to_excel(output_path, index=False)
            print(f"File saved successfully at {output_path}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
