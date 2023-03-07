"""
Module for publishing article to Medium
"""
import os
import requests

from typing import List

MEDIUM_TOKEN = os.environ.get("OPENAI_KEY")


class Article:
    def __init__(
            self,
            medium_token: str = MEDIUM_TOKEN,
    ):
        self.publisher = "medium"
        self.token = medium_token

    def get_author_id(self):
        """
        Uses the /me medium api to get the user's author id
        :return: if response is OK, return the authorId
        """
        response = requests.get(
            url="https://api.medium.com/v1/me",
            headers={
                "Authorization": f"Bearer {self.token}"
            }
        )
        if response.status_code == 200:
            return response.json()["data"]["id"]
        return None

    def publish(
            self,
            article_name: str,
            article_tags: List[str],
            article_content: str,
    ) -> str:
        """
        Publish article to Medium through /posts endpoint
        :param article_name: name of the article
        :param article_tags: keyword-tags for the article
        :param article_content: text of the article in the MD5 format
        :return: if response is OK, returns link to the article, otherwise response error
        """
        author_id = self.get_author_id()

        response = requests.request(
            method="POST",
            url=f"https://api.medium.com/v1/users/{author_id}/posts",
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Accept-Charset": "utf-8",
                "Authorization": f"Bearer {self.token}"
            },
            json={
                "title": article_name,
                "contentFormat": "markdown",
                "tags": article_tags,
                "content": article_content,
            }
        )

        if response.status_code in [200, 201]:
            return f"Successfully published to: {response.json()['data']['url']}"
        return f"Failed: {response}"
