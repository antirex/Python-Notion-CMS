import requests_async as requests
from config import NotionSettings


class ExperienceDesignHandler:
    def __init__(self) -> None:
        self.database_id = NotionSettings().EXPERIENCE_DESIGN_DATABASE_ID
        self.token = NotionSettings().TOKEN

    @staticmethod
    def map_notion_result_to_article(result):

        article_id = result["id"]
        properties = result["properties"]
        author = properties["Author"]["rich_text"][0]["text"]["content"]
        name = properties["Name"]["title"][0]["text"]["content"]
        tags = properties["Tags"]["multi_select"]

        return {"author": author, "name": name, "article_id": article_id, "tags": tags}

    async def get_articles(self):
        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        try:
            r = await requests.post(
                url,
                headers={
                    "Authorization": f"Bearer {self.token}",
                    "Notion-Version": "2021-08-16",
                },
            )

            result_dict = r.json()
            articles_list_result = result_dict["results"]

        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)

        articles = []

        for article in articles_list_result:

            article_dict = self.map_notion_result_to_article(article)
            articles.append(article_dict)

        return articles
