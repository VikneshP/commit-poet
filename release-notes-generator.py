import os
import vertexai
import subprocess

from vertexai.generative_models import (
    GenerativeModel,
)


class ReleaseNotes:
    def __init__(self):
        vertexai.init(project="genai-hackathon-432810", location="us-central1")

    def generate_content(self, prompt_query: str):
        model = GenerativeModel("gemini-1.5-flash-001")
        response = model.generate_content(prompt_query)
        return response

    def get_diff(self, branch1: str, branch2: str):
        response = subprocess.check_output(f"git diff {branch1} {branch2}", shell=True)
        return response.decode().strip()

    def generate_release_notes(self, branch1: str, branch2: str):
        """Generates release notes using Google Gemini"""
        diff = self.get_diff(branch1, branch2)
        prompt_query = (f"You are a software release notes generator. Given the following git diff between branches, "
                        f" generate detailed release notes : ---- {diff}")
        print(prompt_query)
        return self.generate_content(prompt_query)


if __name__ == "__main__":
    release_notes_gen_ai = ReleaseNotes();
    release_notes = release_notes_gen_ai.generate_release_notes("main", "calculator-features");
    print(release_notes)
