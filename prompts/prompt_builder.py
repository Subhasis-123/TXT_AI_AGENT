import json


class PromptBuilder:

    def __init__(self, headers, txt_content):
        self.headers = headers
        self.txt_content = txt_content

    def build_prompt(self):

        row_schema = {}

        for header in self.headers:
            row_schema[header] = ""

        final_schema = [
            {
                "table_name": "TABLE_NAME",
                "rows": [
                    row_schema
                ]
            }
        ]

        schema = json.dumps(
            final_schema,
            indent=4
        )

        prompt = f"""
You are an expert in reading database schema documents.

The uploaded TXT file may contain one or more database tables.

Your task is:

1. Detect every table.
2. Extract all fields of each table.
3. Group fields by table.
4. Return ONLY JSON.
5. No explanation.
6. No markdown.
7. No ```json```.
8. Do not invent values.

Return JSON exactly like this:

{schema}

TXT Document

----------------------------

{self.txt_content}

Return ONLY JSON.
"""

        return prompt