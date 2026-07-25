import json
import re

import google.generativeai as genai

from config import GOOGLE_API_KEY, MODEL_NAME


if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

genai.configure(api_key=GOOGLE_API_KEY)


class GemmaAgent:

    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt):

        response = self.model.generate_content(prompt)

        content = response.text.strip()

        # Remove markdown code blocks if present
        content = re.sub(r"```json", "", content, flags=re.IGNORECASE)
        content = re.sub(r"```", "", content).strip()

        match = re.search(r"\[.*\]", content, re.DOTALL)

        if not match:
            raise Exception(
                f"Gemini did not return valid JSON.\n\nResponse:\n{content}"
            )

        return json.loads(match.group(0))