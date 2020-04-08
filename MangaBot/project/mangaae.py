from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DB.Manga import Manga
from DB.Chapter import Chapter
from DB.Page import Page
from DB.Author import Author
from DB.Tag import Tag
from DB.MangaTag import MangaTag
class MangaSpider(CrawlSpider):
    name = 'mangaspider'
    start_urls = ['https://www.manga.ae/manga', 'https://www.manga.ae']
    allowed_domains = ['manga.ae']

    rules = (
        Rule(LinkExtractor(allow=[r'^https:\/\/www\.[^/]+\/[^/\n]+\/?$'], deny=[r'support/?$']), callback='parse_manga',
             follow=True),
        Rule(LinkExtractor(allow=[r'^https:\/\/www\.[^/]+\/[^/\n]+\/?[\d.]+\/\d\/?$']), callback='parse_chapter',
             follow=True),
    )

    custom_settings = {
        'LOG_ENABLED': False,
        'ROBOTSTXT_OBEY': False
    }

    def parse_manga(self, response):

        mangaDetail = response.css('.manga-details').get()
        if mangaDetail is None:
            print("I. " + "Link " + response.url + "is ignored")
            return
        title_en = response.css('.EnglishName::text').get()
        h4s = response.css('.manga-details-extended > h4')
        try:
            year = h4s[0].xpath("text()").get()
        except NameError:
            year = 0

        try:
            etat = h4s[1].xpath("text()").get().strip()
            if etat == 'مستمرة':
                etat = 0
            elif etat == 'مكتملة':
                etat = 2
            else:
                etat = 1
        except NameError:
            etat = 0

        try:
            about = h4s[2].xpath("text()").get()
        except NameError:
            about = ""
        image = response.css('.manga-cover').xpath("@src").get()
        links = response.css('.manga-details-author h4 > a')
        author_image = response.css('.manga-author').xpath('@src').get()
        fullname = links[len(links) - 1].xpath('text()').get()
        author_link = links[len(links) - 1].xpath('@href').get()
        tags = response.css('.manga-details-extended > ul > li > a')
        title = response.css('.main::text').get()

        title_en = title_en.replace('(', '').replace(')', '')
        try:
            manga = Manga.select(Manga.id, Manga.updatable).where(Manga.title_en == title_en).get()
            mangaExist = True
        except:
            mangaExist = False

        try:
            author = Author.select(Author.id).where(Author.fullname == fullname).get()
            print("I. Author " + fullname + " is already exist")
        except:
            author = Author()
            author.fullname = fullname
            author.image = author_image
            author.link = author_link
            author.save()
            print("I. Author " + fullname + " has been added")

        if mangaExist:
            if manga.updatable == 1:
                Manga.update(updatable=0, title=title, year=year, stopped=etat, cover=image, about=about,
                             author_id=author.id).execute()
                self.addTags(tags, manga)
                print("I. " + title_en + " has been updated!")
            else:
                print("I. " + title_en + " is already exist and up to date.")
            return

        manga = Manga()
        manga.title_en = title_en
        manga.title = title
        manga.year = year
        manga.stopped = etat
        manga.link = response.url
        manga.cover = image
        manga.about = about
        manga.author_id = author.id
        manga.save()
        self.addTags(tags, manga)
        print("I. " + title_en + " has been added")

    def parse_chapter(self, response):
        showChapter = response.css('#showchaptercontainer').get()
        if showChapter is None:
            print("II. Link " + response.url + " has been ignored because it is not a page of chapter")
            return

        title_en = response.css('.manga::text').get()
        edition_number = response.css('.chapter::text').get()
        if title_en is None:
            print("II. Link " + response.url + " has been ignored because don't contains a title")
            return

        page_number = float(response.css('#showchaptercontainer > span').xpath('text()').get())
        image = response.css('#showchaptercontainer > a > img').xpath('@src').get()
        # Is manga exist exist ?

        try:
            manga = Manga.select(Manga.id).where(Manga.title_en == title_en).get()
        except:
            manga = Manga()
            manga.title_en = title_en
            manga.link = response.css('.manga').xpath('@href').get()
            manga.updatable = 1
            manga.save()
            print("II. Manga " + title_en + " has been added, but need update !")

        try:
            chapter = Chapter.select(Chapter.id).where(
                (Chapter.manga_id == manga.id) & (Chapter.edition_number == edition_number)).get()
            print("II. Chapter " + edition_number + " of " + title_en + " already exist")
        except:
            chapter = Chapter()
            chapter.edition_number = edition_number
            chapter.manga_id = manga.id
            chapter.views = 0
            chapter.save()
            print("II. Chapter " + edition_number + " of " + title_en + " has been added")

        try:
            Page.select(Page.id).where((Page.chapter_id == chapter.id) & (Page.page_number == page_number)).get()
            print("II. Page number " + str(
                page_number) + " of chapter " + edition_number + " of " + title_en + " already exist")
        except:
            page = Page()
            page.page_number = page_number
            page.chapter_id = chapter.id
            page.image = image
            page.save()
            print("II. Page number " + str(
                page_number) + " of chapter " + edition_number + " of " + title_en + " has been added")

    def addTags(self, tags, manga):
        for t in tags:
            tagname = t.xpath('text()').get()
            try:
                tag = Tag.select(Tag.id).where(Tag.name == tagname).get()
            except:
                # Add tag
                tag = Tag()
                tag.name = tagname
                tag.save()

            # Link tag
            try:
                m_tag = MangaTag.select(MangaTag.id).where(
                    (MangaTag.manga_id == manga.id) & (MangaTag.tag_id == tag.id)).get()
            except:
                m_tag = MangaTag()
                m_tag.manga_id = manga.id
                m_tag.tag_id = tag.id
                m_tag.save()

    def parse_manga1(self, response):
        image = response.css("#imgcat").xpath("@src").get()
        if image is None:
            return
        texts = response.css('#lefti').get()
        texts = texts.split("\n")
        mangaRes = Manga.select(Manga.id).where(Manga.title_en == texts[3].split("</strong> ")[1])
        if (mangaRes):
            print(texts[3].split("</strong> ")[1] + " is already exist")
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
        print(texts[3].split("</strong> ")[1] + " has been added")

    def parse_chapter1(self, response):
        ##Infos ::

        tab2 = response.css("#tab-2")
        texts = tab2.css('#leftis').get()
        texts = texts.split("\n")
        chapterRes = Chapter.select().where((Chapter.title_en == texts[3].split("</strong> ")[1]) & (
                    Chapter.edition_number == int(texts[6].split("</strong> ")[1])))
        if chapterRes:
            print("Chapter " + str(texts[6].split("</strong> ")[1]) + " of " + texts[3].split("</strong> ")[
                1] + " is already exist!")
            return
        else:
            mangaRes = Manga.get(Manga.title_en == texts[3].split("</strong> ")[1])
            if (mangaRes):
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
                print("Chapter " + str(texts[6].split("</strong> ")[1]) + " of " + texts[3].split("</strong> ")[
                    1] + " has been added")
            else:
                print(texts[3].split("</strong> ")[1] + " Manga Dosen't exist")


from scrapy.crawler import CrawlerProcess

process=CrawlerProcess()

process.crawl(MangaSpider)
process.start()