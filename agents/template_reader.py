import pandas as pd


class TemplateReaderAgent:

    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def read_template(self):
        """
        Reads the uploaded Excel template.
        Returns sheet name, headers and dataframe.
        """

        # Read first sheet
        excel = pd.ExcelFile(self.uploaded_file)

        sheet_name = excel.sheet_names[0]

        df = pd.read_excel(
            self.uploaded_file,
            sheet_name=sheet_name
        )

        headers = list(df.columns)

        return {
            "sheet_name": sheet_name,
            "headers": headers,
            "dataframe": df
        }