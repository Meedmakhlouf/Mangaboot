import scrapy
import peewee
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from models.Manga import Manga
from models.Chapter import Chapter
from models.Page import Page
import csv
def addManga(title_ar,title_en,description,image,year,etat,link):
    with open('mangas.csv', 'a',encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter='|',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([title_en,image,link,year,etat,title_ar,description])
class MangaSpider(CrawlSpider):
    name = 'mangaspider'
    start_urls = ['https://www.shqqaa.com/manga/']
    allowed_domains = ['shqqaa.com']
    
    rules = (
        Rule(LinkExtractor(allow=[r'manga/[A-Za-z0-9\-]+/?$']),callback='parse_manga',follow=True),#trete descrip
        Rule(LinkExtractor(allow=[r'manga/[A-Za-z0-9\-]+/\d+/?$']),callback='parse_chapter',follow=True),#tr episode
    )

    custom_settings = {
        'LOG_ENABLED': True,
        'ROBOTSTXT_OBEY':True
    }

    def parse_manga(self, response):
        image = response.css("#imgcat").xpath("@src").get()
        if image is None:
            return
        texts = response.css('#lefti').get()
        texts = texts.split("\n")
        mangaRes = Manga.select(Manga.id).where(Manga.title_en == texts[3].split("</strong> ")[1])
        if(mangaRes):
            print(texts[3].split("</strong> ")[1]+" is already exist")
            return
        manga = Manga()
        manga.title_en = texts[3].split("</strong> ")[1]
        manga.title = texts[1].split("</strong> ")[1]
        etat = response.css('.mostmr::text').get()
        manga.shqqaa_link = response.url
        manga.cover = image
        manga.about = response.css("p#leftd::text").get()
        stopped = 0
        if etat is None:
            stopped = 1
        manga.stopped = stopped
        manga.save()
        print(texts[3].split("</strong> ")[1]+" has been added")
    def parse_chapter(self, response):
        ##Infos ::

        tab2 = response.css("#tab-2")
        texts = tab2.css('#leftis').get()
        texts = texts.split("\n")
        chapterRes = Chapter.select().where((Chapter.title_en == texts[3].split("</strong> ")[1]) & (Chapter.edition_number == int(texts[6].split("</strong> ")[1])))
        if chapterRes:
            print("Chapter "+str(texts[6].split("</strong> ")[1])+" of "+texts[3].split("</strong> ")[1]+" is already exist!")
            return
        else:
            mangaRes = Manga.get(Manga.title_en == texts[3].split("</strong> ")[1])
            if(mangaRes):
                chapter = Chapter()
                edition = texts[6].split("</strong> ")[1]
                chapter.edition_number = edition
                chapter.views = texts[8].split("</strong> ")[1]
                chapter.title_en = mangaRes.title_en
                chapter.title = mangaRes.title
                chapter.cover = mangaRes.cover
                chapter.about = mangaRes.about
                chapter.manga_id = mangaRes.id
                chapter.save()
                ##Add Pages
                images = response.css('#sqmang > img')
                for image in images:
                    imageSRC = image.xpath("@src").get()
                    if Page.select().where((Page.image == imageSRC) & (Page.chapter_id == chapter.id)):
                        continue
                    page = Page()
                    page.chapter_id = chapter.id
                    page.image = imageSRC
                    page.save()
                print("Chapter "+str(texts[6].split("</strong> ")[1])+" of "+texts[3].split("</strong> ")[1]+" has been added")
            else:
                print(texts[3].split("</strong> ")[1]+" Manga Dosen't exist")



    """
    def parse(self, response):
        links = set()
        for row in response.css('.module'):
            p = row.css('p')
            links.add(p.css('a'))

        for link in links:
            response.follow(link, self.parse)
        self.homePage(response)
        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

    def homePage(self,response):
        for row in response.css('.module'):
            p = row.css('p')
            link = p.css('a').xpath('@href').get()
            image = p.css('a > img').xpath('@src').get()
            title_ar = p.css('span > b::text').get()
            title_en = p.css('a > span.tt::text').get()
            description = row.css('p.leftd > span::text').get()
            etat = row.css('div.am > div::text').get()
            stopped = 1
            if etat == 'مستمر' :
                stopped = 0
            addManga(title_ar,title_en,description,image,2030,stopped,link)
    """