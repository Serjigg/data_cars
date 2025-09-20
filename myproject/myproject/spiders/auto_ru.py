import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'auto'
    allowed_domains = ['auto.ru']
    start_urls = [
        'https://auto.ru/logbook/review/cars/jaguar/xf/7771114/ochen-nedootsenennaia-marka_72200147-86e4-4c3a-9d81-f2bc26db8a6e/']

    def parse(self, response):
        # Correct title extraction
        #mark = response.xpath('.BreadCrumbs__item ::text').get() # TODO

        mark_mod_gen = response.css('.BreadCrumbs__item ::text').getall()
        mark = mark_mod_gen[3]
        model = mark_mod_gen[4]
        generation = mark_mod_gen[5]
        #model_right = response.css('.ContentLinks__title-TdcWA ::text').get()
        review_text = response.css('.LogbookCardContentItem__text-a85z7 ::text').getall()
        comments_about_auto = response.css('.CommentsList__commentWrapper ::text').getall()
        name_author = response.css('.LogbookVerified-DBngj ::text').get()
        rating = response.css('.StarRate2__rating-e5yYY ::text').get()
        positive_qualities = response.xpath('(//*[contains(@class, "LogbookCardRatingSummary__prosAndConsContent")])[1]//text()').get()
        negative_qualities = response.xpath('(//*[contains(@class, "LogbookCardRatingSummary__prosAndConsContent")])[2]//text()').get()

        print(name_author)  # имя автора
        print(rating)  # рейтинг
        print(positive_qualities)
        print(negative_qualities)
        print(mark)
        print(model)
        print(generation)
        print(review_text)
        print(comments_about_auto)


        #print(text)
        # Alternative XPath approach (corrected syntax)
        name = response.xpath("//div[contains(@class, 'LogbookCardAuthor__profile-ZAoW0')]/text()")


        yield {
            'mark': model,
            'author_css': name_author,
            'author_xpath': name

        }