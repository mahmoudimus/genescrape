# -*- coding: utf-8 -*-
import gspread
from elasticsearch import Elasticsearch
from oauth2client.service_account import ServiceAccountCredentials
from scrapy.conf import settings
from scrapy.exporters import BaseItemExporter


class ESItemExporter(BaseItemExporter):
    index = "genescrape"
    doc_type = "Post"

    def __init__(self, **kwargs):
        super(ESItemExporter, self).__init__(**kwargs)

        self.elastic_hosts = settings.get("ELASTIC_HOSTS")

        if self.elastic_hosts is not None:
            self.client = Elasticsearch(hosts=self.elastic_hosts)

    def start_exporting(self):
        pass

    def finish_exporting(self):
        pass

    def export_item(self, item):
        if self.client is None:
            return item

        item_id = item["url"]
        self.client.index(
            index=self.index, doc_type=self.doc_type, body=dict(item), id=item_id
        )
        return item


class GoogleSheetItemExporter(BaseItemExporter):
    def __init__(self, spreadsheet="diseases", worksheet="data"):
        scope = [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
        ]
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            "google_client_secret.json", scope
        )
        self.gc = gspread.authorize(credentials)
        self.spreadsheet = self.gc.open("OnlineJobs")
        self.worksheet = self.spreadsheet.sheet1

    def export_item(self, item):
        if self.credentials.access_token_expired:
            self.client.login()
        self.worksheet.append_row(**item)
