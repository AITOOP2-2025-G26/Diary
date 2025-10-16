from diaries.AbstractDiary import AbstractDiary

class NakagawaDiary(AbstractDiary):

    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2の3回目の授業だった。
慣れない作業で大変だった。

"""
    def get_author(self):
        return "Nakagawa"