from diaries.DiarySample import DiarySample

from diaries.NakagawaDiary import NakagawaDiary
from diaries.Miyazawadiary import Miyazawadiary
from diaries.SasakiDiary import SasakiDiary
from diaries.RyoDiary import RyoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           Miyazawadiary(),
           SasakiDiary(),
           RyoDiary(),
           NakagawaDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()