import json
import re
import time
import ollama


class GemmaAgent:

    def __init__(self, model="gemma3:4b"):
        self.model = model

    def generate(self, prompt):

        start = time.time()

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0
            }
        )

        print(f"Response Time : {time.time()-start:.2f} sec")

        content = response["message"]["content"].strip()

        if not content:
            raise Exception("Gemma returned an empty response.")

        content = re.sub(r"```json", "", content, flags=re.IGNORECASE)
        content = re.sub(r"```", "", content).strip()

        start_idx = content.find("[")
        end_idx = content.rfind("]")

        if start_idx == -1 or end_idx == -1:
            raise Exception("No JSON array found in Gemma response.")

        json_text = content[start_idx:end_idx + 1]

        return json.loads(json_text)