class BoterKaasEieren:

    def __init__(self, speler1, speler2):
        self.spelzet = 0
        self.spel_stand = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
        self.speler1 = speler1
        self.speler2 = speler2

        self.score_speler1 = 0
        self.score_speler2 = 0

    #geeft de score terug van speler 1
    def get_score_speler1(self):
        return self.score_speler1

    #geeft de score terug van speler 2
    def get_score_speler2(self):
        return self.score_speler2

    #zet het bord terug naar default
    def set_spel_stand(self):
        self.spel_stand = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

    #zet de spelzetten terug naar default
    def set_spelzet(self):
        self.spelzet = 0

    #het speltype wordt opgeslagen
    def set_speltype(self, speltype):
        self.speltype = speltype

    def spel_weergeven(self):
        '''
            De functie print de huidige status van het spel.
            De ingevulde/nog in te vullen opties worden opgehaald uit self.spel_stand en weergeven.
        '''

        print("\n\nKies een nummer tussen 1-9, die nog niet is gebruikt.\n")
        print("\t " + self.spel_stand.get(1) + "  |  " + self.spel_stand.get(2) + "  |  " + self.spel_stand.get(3))
        print("\t- - - - - - - -")
        print("\t " + self.spel_stand.get(4) + "  |  " + self.spel_stand.get(5) + "  |  " + self.spel_stand.get(6))
        print("\t- - - - - - - -")
        print("\t " + self.spel_stand.get(7) + "  |  " + self.spel_stand.get(8) + "  |  " + self.spel_stand.get(9))

    def zet_maken(self):
        '''
            In deze functie worden de zetten van de spelers bijgehouden.

            Als de zet (self.spelzet) oneven is, dan is speler 1 aan de beurt.
            Bij een even getal is speler 2 aan de beurt.

            Als het gekozen getal niet voorkomt in self.spel_stand of als het gekozen getal
            eerder is gebruikt, zal de speler nog een keer moeten kiezen.
            Als het gekozen getal nog kan worden gebruikt, krijgt de key(gekozen getal) een nieuwe value (X/O).
        '''

        if self.spelzet % 2 != 0:
            try:
                gekozen_getal = int(input(self.speler1 + " (X) is aan de beurt, voer een getal in: "))
                if self.spel_stand[gekozen_getal] == "X" or self.spel_stand[gekozen_getal] == "O":
                    print("Dit nummer is al gekozen! Kies een ander nummer.")
                    self.zet_maken()
                else:
                    self.spel_stand[gekozen_getal] = "X"
                    self.check_winner()
            except Exception:
                print("De invoer is niet geldig. Kies een nummer tussen 1 - 9!")
                self.zet_maken()

        else:
            try:
                gekozen_getal = int(input(self.speler2 + " (O) is aan de beurt, voer een getal in: "))
                if self.spel_stand[gekozen_getal] == "X" or self.spel_stand[gekozen_getal] == "O":
                    print("Dit nummer is al gekozen! Kies een ander nummer.")
                    self.zet_maken()
                else:
                    self.spel_stand[gekozen_getal] = "O"
                    self.check_winner()
            except Exception:
                print("De invoer is niet geldig. Kies een nummer tussen 1 - 9!")
                self.zet_maken()

    def check_winner(self):
        '''
            Er wordt gecheckt of een speler 3 op een rij heeft.
            Als dit het geval is wordt de functie self.check_speler() aangeroepen,
            om te bepalen wie er heeft gewonnen.

            Als er nog niemand heeft gewonnen wordt nagekeken of het een gelijkspel is,
            anders wordt er doorgespeeld.
        '''

        #horizontaal boven
        if self.spel_stand.get(1) == self.spel_stand.get(2) == self.spel_stand.get(3):
            self.check_speler()
        #horizontaal midden
        elif self.spel_stand.get(4) == self.spel_stand.get(5) == self.spel_stand.get(6):
            self.check_speler()
        #horizontaal beneden
        elif self.spel_stand.get(7) == self.spel_stand.get(8) == self.spel_stand.get(9):
            self.check_speler()
        #verticaal links
        elif self.spel_stand.get(1) == self.spel_stand.get(4) == self.spel_stand.get(7):
            self.check_speler()
        #verticaal midden
        elif self.spel_stand.get(2) == self.spel_stand.get(5) == self.spel_stand.get(8):
            self.check_speler()
        #verticaal rechts
        elif self.spel_stand.get(3) == self.spel_stand.get(6) == self.spel_stand.get(9):
            self.check_speler()
        #schuin
        elif self.spel_stand.get(1) == self.spel_stand.get(5) == self.spel_stand.get(9):
            self.check_speler()
        #schuin
        elif self.spel_stand.get(7) == self.spel_stand.get(5) == self.spel_stand.get(3):
            self.check_speler()
        else:
            self.check_gelijkspel()
            self.spel_weergeven()
            self.spelzet += 1
            self.zet_maken()


    def check_gelijkspel(self):
        '''
            Er wordt in deze functie gecheckt of het een gelijkspel is.

            Als het bord vol is (self.spelzet == 9) en als er 1 ronde wordt gespeeld,
            dan wordt het spel afgesloten.

            Als het bord vol is (self.spelzet = 9) en er worden meerdere rondes gespeeld,
            dan wordt de stand en de ronde naar default gezet en kan er verder worden gespeeld.
        '''

        if self.spelzet == 9 and self.speltype == "1":
            self.spel_weergeven()
            print("\nHet is een gelijkspel.")
            exit()
        elif self.spelzet == 9 and self.speltype == "2":
            self.spel_weergeven()
            print("\nHet is een gelijkspel.")
            self.set_spelzet()
            self.set_spel_stand()


    def check_speler(self):
        '''
            Deze functie checkt welke speler er heeft gewonnen.
            Als de ronde oneven is, heeft speler 1 gewonnen en wordt er een punt bij self.score_speler1 gerekend.
            Als de ronde even is, heeft speler 2 gewonnen en wordt er een punt bij self.score_speler2 gerekend.
        '''

        if self.spelzet % 2 != 0:
            self.spel_weergeven()
            print("\n" + self.speler1 + " heeft de ronde gewonnen!")
            self.score_speler1 += 1
        else:
            self.spel_weergeven()
            print("\n" + self.speler2 + " heeft de ronde gewonnen!")
            self.score_speler2 += 1


def main():
    '''
        De namen van de spelers worden gevraagd en doorgegeven naar de class BoterKaasEieren

        Er wordt gecheckt of de invoer van speltype klopt, anders wordt main() opnieuw gestart.

        Als er 1 ronde wordt gespeeld, wordt het speltype opgeslagen en het spel gestart.

        Als er meedere rondes worden gespeeld, wordt het speltype opgeslagen.
        Zolang geen van de spelers 3 punten heeft, wordt er doorgespeeld.
        Elke ronde worden self.spel_stand en self.spelzet terug naar default gezet.

        Na iedere ronde wordt de score weergeven.
        Als er een speler 3 punten heeft, wordt er weergeven wie er heeft gewonnen.
    '''

    speler1 = input("Speler 1, wat is je naam?")
    speler2 = input("Speler 2, wat is je naam?")
    spelen = BoterKaasEieren(speler1, speler2)
    speltype = input("Er zijn twee verschillende speltypes:\n1. 1 ronde"
                     "\n2. Tot een speler 3 punten heeft.\nVul in welk speltype je wilt spelen:")

    if speltype == "1":
        spelen.set_speltype(speltype)
        spelen.check_winner()
    elif speltype == "2":
        spelen.set_speltype(speltype)
        while spelen.get_score_speler1() < 3 and spelen.get_score_speler2() < 3:
            spelen.check_winner()
            spelen.set_spel_stand()
            spelen.set_spelzet()
            print("\nDe score is: " + speler1 + " (" + str(spelen.get_score_speler1()) + ") - " +
                  speler2 + " (" + str(spelen.get_score_speler2()) + ")\n")
        else:
            if spelen.get_score_speler1() == 3:
                print(speler1 + " heeft het spel gewonnen!")
            else:
                print(speler2 + " heeft het spel gewonnen!")
    else:
        print("De invoer is niet geldig. Begin opnieuw.")
        main()

main()