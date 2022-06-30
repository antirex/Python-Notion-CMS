from ast import Not
import json
import requests
from ...config import NotionSettings

class ThoughtExperiments:
  def __init__(self) -> None:
    self.database_id = NotionSettings.DATABASE_ID
    self.token = NotionSettings.TOKEN

  def map_notion_result_to_article(result):

    article_id = result['id']
    properties = result['properties']
    author = properties['Author']['rich_text'][0]['text']['content']
    name = properties['Name']['title'][0]['text']['content']
    tags = properties['Tags']['multi_select']

    return {
      'author': author,
      'name': name,
      'article_id': article_id,
      'tags': tags
    }


  def get_articles(self):
    url = f'https://api.notion.com/v1/databases/{self.database_id}/query'

    r = requests.post(url, headers={
      "Authorization": f"Bearer {self.token}",
      "Notion-Version": "2021-08-16"
    })

    result_dict = r.json()
    articles_list_result = result_dict['results']


    articles = []

    for article in articles_list_result:

          article_dict = self.map_notion_result_to_article(article)
          articles.append(article_dict)

    return articles

