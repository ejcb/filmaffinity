import scrapy

class FilmaffinitySpider(scrapy.Spider):
    name = "filmaffinity"

    def start_requests(self):
        urls = [
            'https://www.filmaffinity.com/es/cat_new_sa_es.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        catalogoDVD = response.xpath('//*[@id="wrapper-cat"]/div[*]/div[*]/a')
        for peli in catalogoDVD: 
            titulo = peli.xpath('@title').get()
            enlace = peli.xpath('@href').get()
            yield { 'titulo': titulo, 
                    'enlace': enlace
                  }
        
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''

