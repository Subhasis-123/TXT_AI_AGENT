from agents.template_reader import TemplateReaderAgent
from agents.file_reader import FileReaderAgent
from agents.gemma_agent import GemmaAgent
from agents.excel_writer import ExcelWriterAgent
from prompts.prompt_builder import PromptBuilder


class Orchestrator:

    def __init__(self, template_file, txt_files):

        self.template_file = template_file
        self.txt_files = txt_files

    def run(self):

        generated_files = []

        # Read Template
        template_agent = TemplateReaderAgent(self.template_file)
        template_info = template_agent.read_template()

        # Read TXT Files
        file_reader = FileReaderAgent(self.txt_files)
        documents = file_reader.read_files()

        # Initialize Agents
        gemma = GemmaAgent()
        excel_writer = ExcelWriterAgent()

        # Process each TXT file
        for doc in documents:

            # Build Prompt
            prompt_builder = PromptBuilder(
                headers=template_info["headers"],
                txt_content=doc["content"]
            )

            prompt = prompt_builder.build_prompt()

            # Generate AI Response
            response = gemma.generate(prompt)

            # Generate Excel Workbook
            output_file = excel_writer.create_workbook(
                self.template_file,
                doc["file_name"],
                response
            )

            generated_files.append(output_file)

        return generated_files