# Baza Wiedzy Stacji Kosmicznej Omega
# Zawiera min. 50 wpisów dotyczących procedur, opisów modułów i zasad bezpieczeństwa.

knowledge_base = [
    # Sekcja 1: Zasady Ogólne i Dostęp
    "1. Dostęp do Głównego Centrum Sterowania mają wyłącznie oficerowie o randze Komandora.",
    "2. Wszyscy członkowie załogi muszą nosić identyfikatory biometryczne w strefach publicznych przez cały czas.",
    "3. Śluza powietrzna nr 4 jest wyłączona z użytku do czasu zakończenia naprawy w 2055 roku.",
    "4. W przypadku wykrycia spadku ciśnienia, maski tlenowe opuszczą się automatycznie w każdej sekcji.",
    "5. Konsumpcja racji żywnościowych poza mesą jest surowo zabroniona w celu uniknięcia zanieczyszczenia systemów wentylacji.",
    "6. Każdy spacer kosmiczny (EVA) musi być zatwierdzony przez oficera ds. bezpieczeństwa na 24 godziny przed wyjściem.",
    "7. Broń energetyczna jest przechowywana w Zbrojowni Gamma i wymaga autoryzacji dwóch oficerów do otwarcia.",
    "8. Cisza nocna obowiązuje w sektorach mieszkalnych od godziny 22:00 do 06:00 czasu pokładowego.",
    "9. Kontakt z obcymi formami życia wymaga natychmiastowego uruchomienia Procedury Kwarantanny Poziomu 5.",
    "10. System sztucznej inteligencji stacji (HAL) nie może samodzielnie otwierać drzwi śluzy bez fizycznego potwierdzenia przez człowieka.",
    "11. Wszelkie odpady biologiczne muszą być utylizowane w recyklatorze materii w sektorze technicznym.",
    "12. Personel techniczny ma pierwszeństwo dostępu do wind towarowych w godzinach 08:00 - 16:00.",
    "13. Używanie osobistych urządzeń komunikacyjnych w pobliżu Rdzenia Reaktora jest zabronione ze względu na interferencje.",
    "14. Goście z Ziemi muszą przejść 48-godzinną aklimatyzację w strefie buforowej przed wejściem do głównej części stacji.",
    "15. Palenie tytoniu i używanie e-papierosów jest dozwolone tylko w wyznaczonej kabinie w Sektorze Rozrywki.",
    
    # Sekcja 2: Moduły i Technologia
    "16. Stacja Omega zasilana jest przez Reaktor Fuzyjny typu Mark-IV, znajdujący się w Sektorze Inżynieryjnym.",
    "17. Moduł Hydroponiczny produkuje 85% żywności roślinnej spożywanej na stacji.",
    "18. Systemy podtrzymywania życia (ECLSS) są dublowane w każdym module mieszkalnym.",
    "19. Grawitacja na poziomie mieszkalnym jest utrzymywana na poziomie 0.9G poprzez rotację pierścienia zewnętrznego.",
    "20. Hangary dla promów kosmicznych znajdują się na osi obrotu stacji, aby ułatwić dokowanie w stanie nieważkości.",
    "21. Skanery dalekiego zasięgu mogą wykrywać obiekty o wielkości 10cm z odległości 1000 km.",
    "22. Osłony przeciwradiacyjne stacji są wykonane ze stopu ołowiu i polimerów węglowych.",
    "23. Węzeł komunikacyjny 'Alpha' zapewnia stałe połączenie z Bazą Księżycową i Ziemią z opóźnieniem 1.3 sekundy.",
    "24. Roboty konserwacyjne klasy 'Spider' patrolują poszycie stacji co 6 godzin w poszukiwaniu mikrometeorytów.",
    "25. MedBay wyposażony jest w 5 kapsuł regeneracyjnych i 2 stoły operacyjne z asystą robotyczną.",
    
    # Sekcja 3: Procedury Awaryjne
    "26. Alarm Czerwony oznacza bezpośrednie zagrożenie integralności kadłuba lub atak zewnętrzny.",
    "27. Alarm Żółty oznacza awarię systemów krytycznych lub wykrycie nieznanego obiektu na kursie kolizyjnym.",
    "28. Alarm Niebieski oznacza awarię medyczną lub wypadek przy pracy wymagający zespołu ratunkowego.",
    "29. W przypadku pożaru, systemy Halonowe w danej sekcji aktywują się po 10 sekundach od wykrycia dymu.",
    "30. Procedura 'Last Hope' zakłada ewakuację całej załogi do kapsuł ratunkowych w ciągu 15 minut.",
    "31. Kod 99 oznacza bunt na pokładzie i upoważnia dowództwo do użycia środków przymusu bezpośredniego.",
    "32. W razie awarii zasilania głównego, baterie awaryjne podtrzymają systemy życiowe przez 72 godziny.",
    "33. Dekompresja w sektorze mieszkalnym powoduje automatyczne zaryglowanie grodzi w promieniu 50 metrów.",
    "34. Skażenie chemiczne wymaga natychmiastowego założenia masek pełnotwarzowych i udania się do punktów odkażania.",
    
    # Sekcja 4: Personel i Obowiązki
    "35. Główny Inżynier odpowiada za stan techniczny reaktora i silników manewrowych.",
    "36. Oficer Medyczny ma prawo odsunąć każdego członka załogi od obowiązków w przypadku stwierdzenia niezdolności psychofizycznej.",
    "37. Szef Ochrony podlega bezpośrednio Komandorowi Stacji.",
    "38. Kucharz pokładowy zarządza zapasami żywności i ustala menu w porozumieniu z dietetykiem.",
    "39. Technicy hydroponiki są odpowiedzialni za jakość upraw i cykl nawadniania.",
    "40. Operatorzy systemów komunikacji muszą znać biegle co najmniej 3 języki ziemskie i kod binarny.",
    
    # Sekcja 5: Wyposażenie Sklepu/Magazynu (zgodnie z sugestią o produktach)
    "41. Kombinezon EVA Mark-VII - odporny na promieniowanie, zapas tlenu na 8h, wbudowany HUD.",
    "42. Raca Żywnościowa Typ C - smak kurczaka, zawiera komplet witamin na 24h, termin przydatności 5 lat.",
    "43. Latarka Plazmowa - zasięg 500m w próżni, tryb stroboskopowy do sygnalizacji SOS.",
    "44. Buty Magnetyczne - umożliwiają chodzenie po metalowych powierzchniach w stanie nieważkości.",
    "45. Apteczka Osobista - zawiera środki przeciwbólowe, bandaże, koagul antykrwotoczny i stymulanty adrenaliny.",
    "46. Tablet Diagnostyczny - uniwersalne złącze do systemów stacji, ekran holograficzny, wzmocniona obudowa.",
    "47. Multitool Inżynierski - zawiera laser tnący, klucz uniwersalny, spawarę punktową i śrubokręt soniczny.",
    "48. Kawa Syntetyczna 'StarBrew' - dostępna w mesie, wysoka zawartość kofeiny, smak orzechowy.",
    "49. Filtr Wody Osobisty - oczyszcza 99.9% zanieczyszczeń, niezbędny w zestawach przetrwania.",
    "50. Moduł Pamięci Zewnętrznej - 100 Petabajtów, szyfrowanie kwantowe, wodoodporny.",
    "51. Gaśnica Próżniowa - specjalna mieszanka pianowa twardniejąca w kontakcie z próżnią, do łatania dziur.",
    "52. Skaner Biometryczny Ręczny - do szybkiej identyfikacji personelu i sprawdzania uprawnień.",
]
