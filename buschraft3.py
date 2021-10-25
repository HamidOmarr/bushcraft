leeftijd = int(input('Hoe oud ben je?'))
flexibel = int(input('hoeveel uren per week ben je vrij?'))
doorzettend = int(input('van een schaal van 1 tot 10 hoe doorzettend ben je?'))
Positief = int(input('van een schaal van 1 tot 10 hoe positief ben je?'))

if leeftijd >= 16 and flexibel  >= 10 and doorzettend >= 6 and Positief >= 6:
    print ('Nu zullen we kijken bij welke dier het best bij jouw past.')
else:
    print ('Helaas, je voldoet niet aan onze criteria.')
    exit()

beervraag1 = int(input('hoeveel kun je tillen?'))
beervraag2 = int(input('van een schaal van 1 tot 10 hoe sterk ben je?'))
Vosvraag1 = input('Hoe goed ben je in het oplossen van praktische problemen? [g/hg/s]')
Vosvraag2 = int(input('van een schaal van 1 tot 10 hoe Slim ben je?'))
bevervraag1 = int(input('Hoeveel hulpmiddelen kun construeren?'))
bevervraag2 = int(input('van een schaal van 1 tot 10 hoe Handig ben je?'))
uilvraag1 = int(input('Hoe vaak heb je dit al gedaan?'))
uilvraag2 = int(input('van een schaal van 1 tot 10 hoeveel natuurlijke kennis heb je?'))
uilvraag3 = int(input('op hoeveel verschillende manieren kun je voor eten zorgen?'))
uilvraag4 = int(input('van een schaal van 1 tot 10 hoeveel kennis heb je van water zuiveren?'))

if beervraag1 >= 60 and beervraag2 >= 6:
    print ('Beer, Dus je bent sterk en doet graag zwaarwerk.')
if Vosvraag1 == 'g' or 'hg' and Vosvraag2 >= 6:
    print ('Vos, Dus erg slim in het oplossen van praktische problemen en in het vangen van dieren.')
if bevervraag1 >= 15 and bevervraag2 >= 6:
    print ('Bever, Dus erg handig in het bewerken van materialen en het construeren en bouwen van hutten en andere hulpmiddelen.')
if uilvraag1 >= 6 and uilvraag2 >= 6 and uilvraag3 >= 10 and uilvraag4 >= 8:
    print ('Uil, Dus heeft veel kennis van de bruikbaarheid van natuurlijke materialen voor eten, drinken, genezen, verwarmen en beschermen..')

else:
    print ('Helaas, je voldoet niet aan onze criteria.')
    exit()