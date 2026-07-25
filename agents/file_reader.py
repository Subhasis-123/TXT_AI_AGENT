class FileReaderAgent:

    def __init__(self, uploaded_files):
        self.uploaded_files = uploaded_files

    def read_files(self):
        """
        Read all uploaded TXT files.
        Returns a list of dictionaries.
        """

        txt_documents = []

        for file in self.uploaded_files:

            content = file.read().decode("utf-8", errors="ignore")

            txt_documents.append(
                {
                    "file_name": file.name,
                    "content": content
                }
            )

        return txt_documents