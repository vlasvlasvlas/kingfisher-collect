from kingfisher_scrapy.spiders.honduras_portal_base import HondurasPortalBase


class HondurasPortalReleases(HondurasPortalBase):
    """
    API documentation
      http://www.contratacionesabiertas.gob.hn/manual_api/
    Swagger API documentation
      http://www.contratacionesabiertas.gob.hn/servicio/
    Spider arguments
      publisher
        Filter the data by a specific publisher.
        ``oncae`` for "Oficina Normativa de Contratación y Adquisiciones del Estado" publisher.
        ``sefin`` for "Secretaria de Finanzas de Honduras" publisher.
      sample
        Download only the first release package in the dataset.
        If ``publisher`` is also provided, a single package is downloaded from that publisher.
    """
    name = 'honduras_portal_releases'
    data_type = 'release_package'
    data_pointer = '/releasePackage'
    url = 'http://www.contratacionesabiertas.gob.hn/api/v1/release/?format=json'
