from diaries.DiarySample import DiarySample
<<<<<<< HEAD
from diaries.Miyazawadiary import Miyazawadiary
from diaries.SasakiDiary import SasakiDiary
from diaries.RyoDiary import RyoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           Miyazawadiary(),
           SasakiDiary(),
           RyoDiary()
=======
from diaries.RyoDiary import RyoDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           RyoDiary(),
>>>>>>> 4ed7c8da5906587a1657ae62f1d380da3c840ed4
        ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()