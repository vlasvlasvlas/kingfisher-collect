import json

import scrapy

from kingfisher_scrapy.base_spider import SimpleSpider
from kingfisher_scrapy.util import handle_error, parameters, replace_parameter


class CanadaMontreal(SimpleSpider):
    """
    API documentation
      http://donnees.ville.montreal.qc.ca/dataset/contrats-et-subventions-api
    Spider arguments
      sample
        Download only the first page.
    """
    name = 'canada_montreal'
    data_type = 'release_package'
    step = 10000

    def start_requests(self):
        url = 'https://ville.montreal.qc.ca/vuesurlescontrats/api/releases.json?limit={step}'.format(step=self.step)
        yield scrapy.Request(url, meta={'kf_filename': 'offset-0.json'}, callback=self.parse_list)

    @handle_error
    def parse_list(self, response):
        yield from self.parse(response)

        if not self.sample:
            data = json.loads(response.text)
            offset = data['meta']['pagination']['limit']
            total = data['meta']['count']
            for offset in range(offset, total, self.step):
                url = replace_parameter(response.request.url, 'offset', offset)
                yield self.build_request(url, formatter=parameters('offset'))
