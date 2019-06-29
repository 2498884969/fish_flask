from mapp.view_models.book import BookModelView


class MyGifts:
    """非接口方法尽量之对于变量进行读取"""

    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        my_gifts = []
        for gift in self.__gifts_of_mine:
            my_gifts.append(self.__matching(gift))
        return my_gifts

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        return {'wishes_count': count,
                'book': BookModelView(gift.book),
                'id': gift.id}
