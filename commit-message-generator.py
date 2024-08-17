import os
import vertexai
import subprocess

from vertexai.generative_models import (
    GenerativeModel,
)


class CommitMessage:
    def __init__(self):
        vertexai.init(project="genai-hackathon-432810", location="us-central1")

    def generate_content(self, prompt_query: str):
        model = GenerativeModel("gemini-1.5-flash-001")
        response = model.generate_content(prompt_query)
        return response

    def get_diff(self):
        response = subprocess.check_output("git diff", shell=True)
        return response.decode().strip()

    def generate_commit_message(self):
        """Generates a commit message using Google Gemini"""
        diff = self.get_diff()
        prompt_query = (f"You are a commit message generator. Given the following git diff "
                        f"suggest a concise and descriptive commit message : ---- {diff}")
        print(prompt_query)
        return self.generate_content(prompt_query)


if __name__ == "__main__":
    commit_message_gen_ai = CommitMessage();
    commit_message = commit_message_gen_ai.generate_commit_message();
    print(commit_message)
