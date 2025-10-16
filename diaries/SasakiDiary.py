from diaries.AbstractDiary import AbstractDiary
class SasakiDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"
    def get_summary(self):
        return """GitHubの勉強"""

    def get_author(self):
        return "Sasaki"