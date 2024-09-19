from archiv.models import Event, Wab

# Title of WAB for which the keywords are to be linked
titles = [
    "1. Symphonie",
    "2. Symphonie",
    "3. Symph",
    "4. Symph",
    "5. Symph",
    "6. Symphonie",
    "7. Symphon",
    "8. Symphonie",
    "9. Symphon",
]

for title in titles:
    WAB = Wab.objects.filter(title__contains=title)[0]
    events = Event.objects.filter(key_word__contains=title)
    for x in events:
        x.wab.add(WAB)
