import json

import scrapy

from kingfisher_scrapy.base_spider import BaseSpider
from kingfisher_scrapy.util import handle_error


class AfghanistanReleases(BaseSpider):
    name = 'afghanistan_releases'
    download_delay = 1.5

    def start_requests(self):
        yield scrapy.Request(
            'https://ocds.ageops.net/api/ocds/releases/dates',
            meta={'kf_filename': 'list.json'},
            callback=self.parse_list
        )

    @handle_error
    def parse_list(self, response):
        files_urls = json.loads(response.text)
        if self.sample:
            files_urls = [files_urls[0]]

        for file_url in files_urls:
            yield scrapy.Request(
                file_url,
                meta={'kf_filename': file_url.split('/')[-1] + '.json'},
                callback=self.parse_release_list
            )

    @handle_error
    def parse_release_list(self, response):
        files_urls = json.loads(response.text)
        if self.sample:
            files_urls = [files_urls[0]]

        for file_url in files_urls:
            yield scrapy.Request(file_url, meta={'kf_filename': file_url.split('/')[-1] + '.json'})

    @handle_error
    def parse(self, response):
        yield self.build_file_from_response(response, data_type='release')
