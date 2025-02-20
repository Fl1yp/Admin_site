from django.core.management import BaseCommand

from card.models import WhyLook, WhyEat, WhyStop, MyHistory, ZoneRelax, Proiz, Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        WhyLook.objects.all().delete()
        WhyStop.objects.all().delete()
        WhyEat.objects.all().delete()
        MyHistory.objects.all().delete()
        ZoneRelax.objects.all().delete()
        Proiz.objects.all().delete()
        Question.objects.all().delete()

        WhyLook.objects.create(
            img='why/look/izumr.webp',
            name='Изумрудный дворец',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://drrk36.ru/"
        )
        WhyLook.objects.create(
            img='why/look/korova.webp',
            name='Музей Коров',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://zal-korov.ru/"
        )
        WhyLook.objects.create(
            img='/why/look/molod.webp',
            name='Молодежный центр',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://molcentr36.ru/"
        )
        WhyLook.objects.create(
            img='why/look/myzey.webp',
            name='Музей ВОВ',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://kdovdohnovenie.ru/item/1215447"
        )

        WhyStop.objects.create(
            img='why/stop/img.webp',
            name='Гостиница Хуторок',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://zoon.ru/voronezh/hotels/kafe_hutorok_v_rossoshi/"
        )
        WhyStop.objects.create(
            img='why/stop/img_1.webp',
            name='Гостиница Якиманка',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://tdyakimanka.ru/hotel.html"
        )
        WhyStop.objects.create(
            img='why/stop/img_2.webp',
            name='Гостиница Русь',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://travel.yandex.ru/hotels/rossosh/rus/"
        )
        WhyStop.objects.create(
            img='why/stop/img_3.png',
            name='Гостиница Славия',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://slavija.clients.site/"
        )

        WhyEat.objects.create(
            img='why/eat/img_1.webp',
            name='Кофе Pro sushi',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://rossosh.wed-expert.com/profiles/forest_1"
        )
        WhyEat.objects.create(
            img='why/eat/img.webp',
            name='Кофе Testo',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://pizzatesto.ru/"
        )
        WhyEat.objects.create(
            img='why/eat/img_3.png',
            name='Кофе Лагуна',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://zoon.ru/voronezh/restaurants/kafe_laguna_na_ulitse_rossosh/"
        )
        WhyEat.objects.create(
            img='why/eat/img_2.webp',
            name='Кофе Веранда',
            description="Сайт разработан для медицинской компании. С учетом всех требований и пожеланий",
            address="https://veranda-grillbar.ru/"
        )

        MyHistory.objects.create(
            img='bg/igor.webp',
            img_2='bg/igor.png',
            name='  Россошанский район место битвы князя Игоря',
            description="«…И сражались, обходя вокруг озеро.так в день святого воскресенья низвел на нас Господь гнев свой,"
                        " вместо радости обрек нас на плач и вместо веселья – на горе на реке Каялы…»"
        )
        MyHistory.objects.create(
            img='bg/tolstoy.webp',
            img_2='bg/tolstoy.png',
            name='  Толстовские места х.Ржевск',
            description="«Хутор под Россошью превратился на несколько лет в крупный издательский центр "
                        "России. Владимир Чертков перенёс в хутор редакцию «Посредника» - первого издательства в "
                        "России, ставившего своей целью просвещение русского народа.»"
        )
        MyHistory.objects.create(
            img='bg/myzey.webp',
            img_2='bg/myzey.png',
            name='Краеведческий музей',
            description="И да, это последний блок репрезентативного контента-заполнителя. Опять же, на самом деле "
                        " не предназначен для чтения, просто здесь, чтобы дать вам лучшее представление о том, как"
                        " это будет выглядеть с некоторым реальным содержанием. Ваш контент."
        )
        MyHistory.objects.create(
            img='bg/bitva.webp',
            img_2='bg/bitva.png',
            name='Россошанский район – часть сталинградской битвы…',
            description="Территория Среднедонской наступательной операции «Малый Сатурн»."
                        "Военные историки оценивают операцию как составную часть Сталинградской битвы."
        )
        MyHistory.objects.create(
            img='bg/tsercov.webp',
            img_2='bg/tsercov.png',
            name='Россошанский район – центр духовного просвещения…',
            description="Россошанская Епархия восстановлена как  самостоятельная и выделена из состава "
                        "Воронежской в пределах 13-ти муниципальных районов области."
        )
        ZoneRelax.objects.create(
            img='zone_relax_slider/xim-main.webp',
            img_2="zone_relax_slider/xim_2.png",
            img_3="zone_relax_slider/xim_2.png",
            name='Дом у леса',
            description="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque id, rerum? Accusantium aliquid amet aut beatae dicta dolor esse excepturi expedita illo neque nulla, perferendis perspiciatis placeat porro quae quaerat quasi quia quidem quisquam saepe sapiente tempore velit voluptates voluptatibus.."
        )
        ZoneRelax.objects.create(
            img='zone_relax_slider/kk-main.webp',
            img_2='zone_relax_slider/kk_2.png',
            img_3='zone_relax_slider/kk_3.png',
            name='Лагерь "Артек"',
            description="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque id, rerum? Accusantium aliquid amet aut beatae dicta dolor esse excepturi expedita illo neque nulla, perferendis perspiciatis placeat porro quae quaerat quasi quia quidem quisquam saepe sapiente tempore velit voluptates voluptatibus."
        )

        Proiz.objects.create(
            img='proiz/img.webp',
            name='ЭкоНива',
            description="На сегодняшний день компания занимает лидирующие позиции в сфере поставок и сервисного обслуживания сельхозтехники в России, а также имеет устоявшуюся на рынке репутацию экспертов."
        )
        Proiz.objects.create(
            img='proiz/img_2.webp',
            name='ТракторЦентр',
            description="У нас в наличии более 20 моделей мини-тракторов различных габаритов и мощностей, а так же навесное оборудование под различные задачи. Поможем вам выбрать мини-трактор или навесное оборудование идеально подходящее именно вам!"
        )
        Proiz.objects.create(
            img='proiz/img_1.webp',
            name='Гварта-Агро',
            description="Деятельность компании ООО «Агротех-Гарант» - это удачный пример союза науки и практики, умелого ведения бизнеса и социальной ответственности. Открывшись в 1998 году, компания прочно завоевала позиции на современном рынке АПК, став символом надежного партнерства."
        )
        Proiz.objects.create(
            img='proiz/img_3.webp',
            name='Ольховатский сахарный комбинат',
            description="Во второй половине XX века производство на обоих заводах увеличилось, были установлены автоматические центрифуги, запущена система замкнутого водоснабжения, цеха подключили к государственной электросети. В 1969 году два предприятия объединились в Ольховатский сахарный комбинат — третий по величине в России.")
        Proiz.objects.create(
            img='proiz/img.webp',
            name='ЭкоНива',
            description="На сегодняшний день компания занимает лидирующие позиции в сфере поставок и сервисного обслуживания сельхозтехники в России, а также имеет устоявшуюся на рынке репутацию экспертов."
        )
        Proiz.objects.create(
            img='proiz/img_2.webp',
            name='ТракторЦентр',
            description="У нас в наличии более 20 моделей мини-тракторов различных габаритов и мощностей, а так же навесное оборудование под различные задачи. Поможем вам выбрать мини-трактор или навесное оборудование идеально подходящее именно вам!"
        )
        Proiz.objects.create(
            img='proiz/img_1.webp',
            name='Гварта-Агро',
            description="Деятельность компании ООО «Агротех-Гарант» - это удачный пример союза науки и практики, умелого ведения бизнеса и социальной ответственности. Открывшись в 1998 году, компания прочно завоевала позиции на современном рынке АПК, став символом надежного партнерства."
        )
        Proiz.objects.create(
            img='proiz/img_3.webp',
            name='Ольховатский сахарный комбинат',
            description="Во второй половине XX века производство на обоих заводах увеличилось, были установлены автоматические центрифуги, запущена система замкнутого водоснабжения, цеха подключили к государственной электросети. В 1969 году два предприятия объединились в Ольховатский сахарный комбинат — третий по величине в России."
        )
        Proiz.objects.create(
            img='proiz/img_3.webp',
            name='АгроСнаб',
            description="Во второй половине XX века производство на обоих заводах увеличилось, были установлены автоматические центрифуги, запущена система замкнутого водоснабжения, цеха подключили к государственной электросети. В 1969 году два предприятия объединились в Ольховатский сахарный комбинат — третий по величине в России."
        )
        Question.objects.create(
            question='Что мы можем показать?',
            answer="Мы проведем вам экскурсию по всему пайону заехав на меловые горы и на ферму коров")
        Question.objects.create(
            question='Как с нами миожно свзяться?',
            answer="Связаться с нами можно по номеру 8-800-888-88-88 или написав на почту tueismrossosh@mail.ru")
        Question.objects.create(
            question='Со скольки мы работаем ',
            answer="Мы работаем с 9:00 до 18:00 пн-пт, Экскурсии у нас проходят в четные дни недели ")
