"""
Module for generating articles
"""
import os
import openai

openai.api_key = os.environ.get("OPENAI_KEY")


class GPT3:
    def __init__(self):
        self.model: str = "gpt-3.5-turbo"
        self.temperature: float = 0.6
        self.top_p: float = 1.0
        self.frequency_penalty: float = 0.8
        self.presence_penalty: float = 0.0

    def gen_article(self, topic):
        """
        Generate text for the article using OpenAI API
        :param topic: topic for desired article
        :return: text of the article
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": f"You are qualified IT expert.",
                },
                {
                    "role": "user",
                    "content": f"Generate scientific article in Markdown format on this topic: {topic}"
                },
            ],
            temperature=self.temperature,
            max_tokens=1000,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return response.get("choices")[0].get("message").get("content")

    def extract_keywords(self, text):
        """
        Extract keywords from the text
        :return: comma-separated keywords in str
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": f"Extract one-word keywords as tags from this text to list separated with comma:\n\n{text}",
                },
            ],
            temperature=self.temperature,
            max_tokens=50,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return response.get("choices")[0].get("message").get("content")
