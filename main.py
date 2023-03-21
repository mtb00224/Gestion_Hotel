import gi , time
from key import API_KEY
from api import connectionAPI, dataDictionnaire, envoieData
from fonctions import dateIsValide, dateIsCorrect, BoiteDialogue, chaineIsValide, BoiteDialogueDescription, boutonRetour, BoiteDialogueSucces, BoiteDialogueAlerte


gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk

url = "https://newsapi.org/v2/top-headlines?country=fr&apiKey="+str(API_KEY)
articles = connectionAPI(url)

class PagePrincipal(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)

        fixe = Gtk.Fixed()
        #grid.set_column_spacing(10)
        #grid.set_row_spacing(10)
        self.add(fixe)

        #Action des sous menus des differents bouttons
                #Gestion Hotel
        menu_hotel = Gtk.Menu()
        menuitem_hotel0 = Gtk.MenuItem(label="Description Hotel")
        menu_hotel.append(menuitem_hotel0)
        menuitem_hotel0.show()

        menuitem_hotel1 = Gtk.MenuItem(label="Modifier Nom")
        menu_hotel.append(menuitem_hotel1)
        menuitem_hotel1.show()

        menuitem_hotel2 = Gtk.MenuItem(label="Modifier Tarif Chambre")
        menuitem_hotel2.show()
        menu_hotel.append(menuitem_hotel2)

        menuitem_hotel3 = Gtk.MenuItem(label="Renitialiser")
        menuitem_hotel3.show()
        menu_hotel.append(menuitem_hotel3)

        menuitem_hotel0.connect("activate", self.description)
        menuitem_hotel1.connect("activate", self.modifierNom)
        menuitem_hotel2.connect("activate", self.modifierTarif)
        menuitem_hotel3.connect("activate", self.renitialiser)

                #Reservation
        menu_reservation = Gtk.Menu()
        menuitem_reservation1 = Gtk.MenuItem(label="Ajouter")
        menu_reservation.append(menuitem_reservation1)
        menuitem_reservation1.show()

        menuitem_reservation2 = Gtk.MenuItem(label="Reporter")
        menuitem_reservation2.show()
        menu_reservation.append(menuitem_reservation2)

        menuitem_reservation3 = Gtk.MenuItem(label="Annuler")
        menuitem_reservation3.show()
        menu_reservation.append(menuitem_reservation3)

        menuitem_reservation4 = Gtk.MenuItem(label="Historique")
        menuitem_reservation4.show()
        menu_reservation.append(menuitem_reservation4)

        menuitem_reservation1.connect("activate", self.reserver)
        menuitem_reservation2.connect("activate", self.reporter)
        menuitem_reservation3.connect("activate", self.annuler)
        menuitem_reservation4.connect("activate", self.historique)

                #Gestion Client
        menu_client = Gtk.Menu()
        menuitem_client1 = Gtk.MenuItem(label="Liste client en chambre")
        menu_client.append(menuitem_client1)
        menuitem_client1.show()

        menuitem_client2 = Gtk.MenuItem(label="Liste client qui reserve")
        menuitem_client2.show()
        menu_client.append(menuitem_client2)

        menuitem_client3 = Gtk.MenuItem(label="Liste client qui sort aujourd'hui")
        menuitem_client3.show()
        menu_client.append(menuitem_client3)

        menuitem_client1.connect("activate", self.listeClientEnChambre)
        menuitem_client2.connect("activate", self.listeClientEnReserve)
        menuitem_client3.connect("activate", self.listeClientQuiSort)

                #Gestion Chambre
        menu_chambre = Gtk.Menu()
        menuitem_chambre1 = Gtk.MenuItem(label="Liste chambre occupee")
        menu_chambre.append(menuitem_chambre1)
        menuitem_chambre1.show()

        menuitem_chambre2 = Gtk.MenuItem(label="Liste chambre en reserve")
        menuitem_chambre2.show()
        menu_chambre.append(menuitem_chambre2)

        menuitem_chambre3 = Gtk.MenuItem(label="Liste chambre qui seront libre aujourd'hui")
        menuitem_chambre3.show()
        menu_chambre.append(menuitem_chambre3)

        menuitem_chambre1.connect("activate", self.listeChambreOccupee)
        menuitem_chambre2.connect("activate", self.listeChambreEnReserve)
        menuitem_chambre3.connect("activate", self.listeChambreLibre)

        btn_hotel = Gtk.Button(label="      Gestion Hotel       ")
        fixe.put(btn_hotel, 0, 150)

        btn_reservation = Gtk.Button(label="        Reservation         ")
        fixe.put(btn_reservation, 0, 290)

        btn_client = Gtk.Button(label="     Gestion Client      ")
        fixe.put(btn_client, 0, 440)

        btn_chambre = Gtk.Button(label="  Gestion Chambre  ")
        fixe.put(btn_chambre, 0, 590)

        btn_statistique = Gtk.Button(label="        Statistique         ")
        fixe.put(btn_statistique, 0, 740)

        btn_quitter = Gtk.Button(label="            Quitter             ")
        fixe.put(btn_quitter, 0, 850)

        # Action des boutons de la fenetre principale
        btn_hotel.connect_object('button-press-event', self.voir_sous_menu, menu_hotel)
        btn_reservation.connect_object('button-press-event', self.voir_sous_menu, menu_reservation)
        btn_client.connect_object('button-press-event', self.voir_sous_menu, menu_client)
        btn_chambre.connect_object('button-press-event', self.voir_sous_menu, menu_chambre)
        btn_statistique.connect("clicked", self.statisque)
        btn_quitter.connect("clicked", self.quitter)

        date = time.ctime()
        date = date.split()
        label_date = Gtk.Label()
        label_date.set_markup("<span size='17000' foreground='dodgerblue'>Nous sommes :  {0} le {1} {2} {3} et il est : {4}  </span>".format(date[0], date[2], date[1], date[4], date[3]))
        fixe.put(label_date, 850, 10)


        #Message de bienvenue
        banner = Gtk.Label()
        banner.set_markup("<span size='25000'>BIENVENUE A VOUS DANS L'HOTEL : LA GAZELLE</span>")
        banner.set_width_chars(100)
        fixe.put(banner, 550, 100)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/hotel_1.jpg")
        fixe.put(image, 350, 150)

        #Affichage des sous menu
    def voir_sous_menu(self, widget, event):
        widget.popup(None, None, None, None, event.button, event.time)

    #Definition des methodes
    def description(self, widget):
        desc = BoiteDialogueDescription(self)
        desc.run()

    def statisque(self, widget):
        self.hide()
        nom_hotel = Statistique()
        nom_hotel.show_all()

    def quitter(self, widget):
        Gtk.main_quit()

    def reserver(self, widget):
        self.hide()
        reservation = AjoutReservation()
        reservation.show_all()

    def reporter(self, widget):
        self.hide()
        reservation = ReporterReservation()
        reservation.show_all()

    def annuler(self, widget):
        self.hide()
        reservation = AnnulerReservation()
        reservation.show_all()

    def historique(self, widget):
        self.hide()
        reservation = HistoriqueReservation()
        reservation.show_all()


    def modifierNom(self, widget):
        self.hide()
        nom_hotel = ModifierNom()
        nom_hotel.show_all()

    def modifierTarif(self, widget):
        self.hide()
        nom_hotel = ModifierTarif()
        nom_hotel.show_all()

    def renitialiser(self, widget):
        self.hide()
        renitialiser = BoiteDialogueAlerte(self)
        renitialiser.run()

        if Gtk.ResponseType.OK:
            boutonRetour(self, PagePrincipal)

    def listeClientEnChambre(self, widget):
        self.hide()
        nom_hotel = ListeClientEnChambre()
        nom_hotel.show_all()

    def listeClientEnReserve(self, widget):
        self.hide()
        nom_hotel = ListeClientEnReserve()
        nom_hotel.show_all()

    def listeClientQuiSort(self, widget):
        self.hide()
        nom_hotel = ListeClientQuiSort()
        nom_hotel.show_all()

    def listeChambreOccupee(self, widget):
        self.hide()
        nom_hotel = ListeChambreOccupee()
        nom_hotel.show_all()

    def listeChambreEnReserve(self, widget):
        self.hide()
        nom_hotel = ListeChambreEnReserve()
        nom_hotel.show_all()

    def listeChambreLibre(self, widget):
        self.hide()
        nom_hotel = ListeChambreLibre()
        nom_hotel.show_all()

class AjoutReservation(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        label_nom = Gtk.Label()
        label_nom.set_markup("<span size='25000'>Nom</span>".format(label_nom.get_text()))
        fixe.put(label_nom, 50, 50)

        self.champ_nom = Gtk.Entry()
        fixe.put(self.champ_nom, 350, 50)

        label_prenom = Gtk.Label()
        label_prenom.set_markup("<span size='25000'>Prenom</span>".format(label_nom.get_text()))
        fixe.put(label_prenom, 50, 150)

        self.champ_prenom = Gtk.Entry()
        fixe.put(self.champ_prenom, 350, 150)

        label_tel = Gtk.Label()
        label_tel.set_markup("<span size='25000'>Telephone</span>".format(label_nom.get_text()))
        fixe.put(label_tel, 50, 250)

        self.champ_tel = Gtk.Entry()
        fixe.put(self.champ_tel, 350, 250)

        label_dr = Gtk.Label()
        label_dr.set_markup("<span size='25000'>Date de reservation</span>".format(label_nom.get_text()))
        fixe.put(label_dr, 50, 350)

        self.champ_dr = Gtk.Entry()
        fixe.put(self.champ_dr, 350, 350)

        label_de = Gtk.Label()
        label_de.set_markup("<span size='25000'>Date entrée</span>".format(label_nom.get_text()))
        fixe.put(label_de, 50, 450)

        self.champ_de = Gtk.Entry()
        fixe.put(self.champ_de, 350, 450)

        label_nuite= Gtk.Label()
        label_nuite.set_markup("<span size='25000'>Nombre de jour</span>".format(label_nom.get_text()))
        fixe.put(label_nuite, 50, 550)

        self.champ_nuite = Gtk.Entry()
        fixe.put(self.champ_nuite, 350, 550)

        label_classe_chambre = Gtk.Label()
        label_classe_chambre.set_markup("<span size='25000'>Classe chambre</span>".format(label_nom.get_text()))
        fixe.put(label_classe_chambre, 50, 650)

        eco = Gtk.RadioButton.new_with_label_from_widget(None, "Economique")
        eco.connect("toggled", self.on_button_toggled, "1")
        fixe.put(eco, 300, 670)

        standard = Gtk.RadioButton.new_with_label_from_widget(None, "Standard")
        standard.connect("toggled", self.on_button_toggled, "2")
        fixe.put(standard, 430, 670)

        affaire = Gtk.RadioButton.new_with_label_from_widget(None, "Affaire")
        affaire.connect("toggled", self.on_button_toggled, "3")
        fixe.put(affaire, 550, 670)

        label_service = Gtk.Label()
        label_service.set_markup("<span size='25000'>Service Annexe</span>".format(label_nom.get_text()))
        fixe.put(label_service, 50, 750)

        petit_deuje = Gtk.RadioButton.new_with_label_from_widget(None, "Petit dejeûner")
        petit_deuje.connect("toggled", self.on_button_toggled, "1")
        fixe.put(petit_deuje, 290, 770)

        service_tel = Gtk.RadioButton.new_with_label_from_widget(None, "Service telephonique")
        service_tel.connect("toggled", self.on_button_toggled, "2")
        fixe.put(service_tel, 410, 770)

        bar = Gtk.RadioButton.new_with_label_from_widget(None, "Bar")
        bar.connect("toggled", self.on_button_toggled, "3")
        fixe.put(bar, 580, 770)

        label_choix_etage = Gtk.Label()
        label_choix_etage.set_markup("<span size='25000'>Choix de l'etage</span>".format(label_nom.get_text()))
        fixe.put(label_choix_etage, 50, 830)

        self.champ_choix_etage = Gtk.Entry()
        fixe.put(self.champ_choix_etage, 350, 830)

        enregistrer = Gtk.Button.new_with_label("ENREGISTRER")
        fixe.put(enregistrer, 450, 0)
        enregistrer.connect("clicked", self.enregistrer)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/client.png")
        fixe.put(image, 650, 25)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def enregistrer(self, widget):
        if chaineIsValide(self.champ_nom.get_text()) and chaineIsValide(self.champ_prenom.get_text()) and dateIsCorrect(self.champ_dr.get_text()) and \
                dateIsCorrect(self.champ_de.get_text()) and self.champ_tel.get_text().isdigit() and self.champ_nuite.get_text().isdigit() and self.champ_choix_etage.get_text().isalnum():
            succce = BoiteDialogueSucces(self)
            succce.run()

            if Gtk.ResponseType.OK:
                data = dataDictionnaire(self.champ_nom.get_text(), self.champ_prenom.get_text(), self.champ_tel.get_text(), self.champ_dr.get_text(),
                                      self.champ_de.get_text(), self.champ_nuite.get_text(), self.champ_choix_etage.get_text())
                a = envoieData(url, data)
                print(a)

                time.sleep(2)
                boutonRetour(self, PagePrincipal)
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ReporterReservation(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        label_tel = Gtk.Label()
        label_tel.set_markup("<span size='25000'>Telephone</span>".format(label_tel.get_text()))
        fixe.put(label_tel, 50, 100)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("dodgerblue"))
        label_tel.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        self.champ_tel = Gtk.Entry()
        fixe.put(self.champ_tel, 350, 100)

        label_dr = Gtk.Label()
        label_dr.set_markup("<span size='25000'>Date de reservation</span>".format(label_dr.get_text()))
        fixe.put(label_dr, 50, 200)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("dodgerblue"))
        label_dr.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        self.champ_dr = Gtk.Entry()
        fixe.put(self.champ_dr, 350, 200)

        label_de = Gtk.Label()
        label_de.set_markup("<span size='25000'>Date entrée</span>".format(label_de.get_text()))
        fixe.put(label_de, 50, 300)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("dodgerblue"))
        label_de.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        self.champ_de = Gtk.Entry()
        fixe.put(self.champ_de, 350, 300)

        label_nuite = Gtk.Label()
        label_nuite.set_markup("<span size='25000'>Nombre de jour</span>".format(label_nuite.get_text()))
        fixe.put(label_nuite, 50, 400)
        rgba = Gdk.RGBA.from_color(Gdk.color_parse("dodgerblue"))
        label_nuite.override_background_color(Gtk.StateFlags.NORMAL, rgba)

        self.champ_nuite = Gtk.Entry()
        fixe.put(self.champ_nuite, 350, 400)

        enregistrer = Gtk.Button.new_with_label("ENREGISTRER")
        fixe.put(enregistrer, 250, 800)
        enregistrer.connect("clicked", self.enregistrer)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/client.png")
        fixe.put(image, 650, 25)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def enregistrer(self, widget):
        if dateIsCorrect(self.champ_dr.get_text()) and dateIsCorrect(self.champ_de.get_text()) and self.champ_tel.get_text().isdigit()\
                and self.champ_nuite.get_text().isdigit():
            succces = BoiteDialogueSucces(self)
            succces.run()

            time.sleep(2)

            boutonRetour(self, PagePrincipal)
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class AnnulerReservation(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        alerte = Gtk.Label()
        alerte.set_markup("<span size='25000' foreground='red'>\t\t\tAttention !!!\n vous allez annuler une réservation</span>".format(alerte.get_text()))
        fixe.put(alerte, 400, 150)

        label_tel = Gtk.Label()
        label_tel.set_markup("<span size='25000' foreground='white'>Telephone</span>".format(label_tel.get_text()))
        fixe.put(label_tel, 500, 300)

        self.champ_tel = Gtk.Entry()
        fixe.put(self.champ_tel, 750, 300)

        enregistrer = Gtk.Button.new_with_label("ENREGISTRER")
        fixe.put(enregistrer, 650, 400)
        enregistrer.connect("clicked", self.enregistrer)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def enregistrer(self, widget):
        if self.champ_tel.get_text().isdigit():
            alerte = BoiteDialogueAlerte(self)
            alerte.run()

            time.sleep(2)
            if Gtk.ResponseType.OK:
                succes = BoiteDialogueSucces(self)
                succes.run()
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()


    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class HistoriqueReservation(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        label_hitorique_info = Gtk.Label()
        label_hitorique_info.set_markup(
            "<span size='25000' foreground='dodgerblue'>HISTORIQUE DES RESERVATIONS</span>".format(
                label_hitorique_info.get_text()))
        fixe.put(label_hitorique_info, 450, 10)

        entete = Gtk.Label()
        entete.set_markup(
            "<span size='25000' foreground='dodgerblue'>Titre\t\t\t\t\t\t\t\t\t\t\tAuteur\t\t\t\t\t\tSource</span>".format(
                entete.get_text()))
        fixe.put(entete, 50, 60)

        y = 100
        i = 0
        for article in articles:
            x = 50
            valeur = article['title'].split("-")
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[0])
            fixe.put(label_historique_titre, x, y)

            x = 790
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 1200
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            y = y + 30
            i = i + 1

        total = Gtk.Label()
        total.set_markup(
            f"<span size='25000' foreground='green'>TOTAL   :\t{i}</span>".format(
                total.get_text(), i))
        fixe.put(total, 700, 850)

        print(articles)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ModifierNom(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HOTEL  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        label_texte = Gtk.Label()
        label_texte.set_markup("<span size='25000' foreground='orange'>Vous êtes sur le point de modifier \n\t\tle nom de l'hôtel</span>".format(label_texte.get_text()))
        fixe.put(label_texte, 900,30)

        label_new_nom = Gtk.Label()
        label_new_nom.set_markup(
            "<span size='25000' foreground='white'>Donnez le nouveau nom de l'hotel</span>".format(
                label_new_nom.get_text()))
        fixe.put(label_new_nom, 900, 230)

        self.champ_new_nom = Gtk.Entry()
        fixe.put(self.champ_new_nom, 1070, 300)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/interieur_hotel.png")
        fixe.put(image, 0, 0)

        enregistrer = Gtk.Button.new_with_label("ENREGISTRER")
        enregistrer.connect("clicked", self.enregistrer)
        fixe.put(enregistrer, 1100, 500)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 1120, 700)

    def enregistrer(self, widget):
        if chaineIsValide(self.champ_new_nom.get_text()):
            succes = BoiteDialogueSucces(self)
            succes.run()

            if Gtk.ResponseType.OK:
                boutonRetour(self, PagePrincipal)
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ModifierTarif(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        tarif_eco = Gtk.Label()
        tarif_eco.set_markup("<span size='25000'>Tarif chambre eco</span>".format(tarif_eco.get_text()))
        fixe.put(tarif_eco, 20, 100)

        self.champ_tarif_eco = Gtk.Entry()
        fixe.put(self.champ_tarif_eco, 400, 100)

        tarif_standard = Gtk.Label()
        tarif_standard.set_markup("<span size='25000'>Tarif chambre stand</span>".format(tarif_standard.get_text()))
        fixe.put(tarif_standard, 20, 200)

        self.champ_tarif_standard = Gtk.Entry()
        fixe.put(self.champ_tarif_standard, 400, 200)

        tarif_aff = Gtk.Label()
        tarif_aff.set_markup("<span size='25000'>Tarif chambre aff</span>".format(tarif_aff.get_text()))
        fixe.put(tarif_aff, 20, 300)

        self.champ_tarif_aff = Gtk.Entry()
        fixe.put(self.champ_tarif_aff, 400, 300)

        tarif_petit_deuje = Gtk.Label()
        tarif_petit_deuje.set_markup("<span size='25000'>Tarif petit deujener</span>".format(tarif_petit_deuje.get_text()))
        fixe.put(tarif_petit_deuje, 20, 400)

        self.champ_tarif_petit_deuje = Gtk.Entry()
        fixe.put(self.champ_tarif_petit_deuje, 400, 400)

        tarif_phone = Gtk.Label()
        tarif_phone.set_markup("<span size='25000'>Tarif telephone</span>".format(tarif_phone.get_text()))
        fixe.put(tarif_phone, 20, 500)

        self.champ_tarif_phone = Gtk.Entry()
        fixe.put(self.champ_tarif_phone, 400, 500)

        tarif_bar = Gtk.Label()
        tarif_bar.set_markup("<span size='25000'>Tarif bar</span>".format(tarif_bar.get_text()))
        fixe.put(tarif_bar, 20, 600)

        self.champ_tarif_bar = Gtk.Entry()
        fixe.put(self.champ_tarif_bar, 400, 600)

        tarif_normal = Gtk.Label()
        tarif_normal.set_markup("<span size='25000'>Tarif Normal</span>".format(tarif_normal.get_text()))
        fixe.put(tarif_normal, 20, 700)

        self.champ_tarif_normal = Gtk.Entry()
        fixe.put(self.champ_tarif_normal, 400, 700)

        tarif_special = Gtk.Label()
        tarif_special.set_markup("<span size='25000'>Tarif special</span>".format(tarif_special.get_text()))
        fixe.put(tarif_special, 20, 800)

        self.champ_tarif_special = Gtk.Entry()
        fixe.put(self.champ_tarif_special, 400, 800)

        enregistrer = Gtk.Button.new_with_label("ENREGISTRER")
        fixe.put(enregistrer, 250, 870)
        enregistrer.connect("clicked", self.enregistrer)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/hotel3.png")
        fixe.put(image, 650, 25)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def enregistrer(self, widget):
        if self.champ_tarif_eco.get_text().isdigit() and self.champ_tarif_petit_deuje.get_text().isdigit() and self.champ_tarif_phone.get_text().isdigit() \
            and self.champ_tarif_bar.get_text().isdigit() and self.champ_tarif_normal.get_text().isdigit() and self.champ_tarif_special.get_text().isdigit() \
                and self.champ_tarif_standard.get_text().isdigit() and self.champ_tarif_aff.get_text().isdigit():
            succes = BoiteDialogueSucces(self)
            succes.run()

            if Gtk.ResponseType.OK:
                boutonRetour(self, PagePrincipal)
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeClientEnChambre(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup("<span size='25000' foreground='dodgerblue'>Liste des clients qui occupent des chambres</span>".format(annoce.get_text()))
        fixe.put(annoce, 500, 0)

        entete_nom = Gtk.Label()
        entete_nom.set_markup("<span size='25000'>NOM</span>".format(entete_nom.get_text()))
        fixe.put(entete_nom, 100, 50)

        entete_prenom = Gtk.Label()
        entete_prenom.set_markup("<span size='25000'>PRENOM</span>".format(entete_prenom.get_text()))
        fixe.put(entete_prenom, 500, 50)

        entete_tel = Gtk.Label()
        entete_tel.set_markup("<span size='25000'>TELEPHONE</span>".format(entete_tel.get_text()))
        fixe.put(entete_tel, 800, 50)

        entete_chambre = Gtk.Label()
        entete_chambre.set_markup("<span size='25000'>NUM CHAMBRE</span>".format(entete_chambre.get_text()))
        fixe.put(entete_chambre, 1100, 50)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeClientEnReserve(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup(
            "<span size='25000' foreground='dodgerblue'>Liste des clients qui reservent des chambres</span>".format(
                annoce.get_text()))
        fixe.put(annoce, 500, 0)

        entete_nom = Gtk.Label()
        entete_nom.set_markup("<span size='25000'>NOM</span>".format(entete_nom.get_text()))
        fixe.put(entete_nom, 200, 50)

        entete_prenom = Gtk.Label()
        entete_prenom.set_markup("<span size='25000'>PRENOM</span>".format(entete_prenom.get_text()))
        fixe.put(entete_prenom, 500, 50)

        entete_tel = Gtk.Label()
        entete_tel.set_markup("<span size='25000'>TELEPHONE</span>".format(entete_tel.get_text()))
        fixe.put(entete_tel, 800, 50)

        entete_chambre = Gtk.Label()
        entete_chambre.set_markup("<span size='25000'>NUM CHAMBRE</span>".format(entete_chambre.get_text()))
        fixe.put(entete_chambre, 1100, 50)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeClientQuiSort(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup(
            "<span size='25000' foreground='dodgerblue'>Liste des clients qui sortent aujourd'hui</span>".format(
                annoce.get_text()))
        fixe.put(annoce, 500, 0)

        entete_nom = Gtk.Label()
        entete_nom.set_markup("<span size='25000'>NOM</span>".format(entete_nom.get_text()))
        fixe.put(entete_nom, 100, 50)

        entete_prenom = Gtk.Label()
        entete_prenom.set_markup("<span size='25000'>PRENOM</span>".format(entete_prenom.get_text()))
        fixe.put(entete_prenom, 500, 50)

        entete_tel = Gtk.Label()
        entete_tel.set_markup("<span size='25000'>TELEPHONE</span>".format(entete_tel.get_text()))
        fixe.put(entete_tel, 800, 50)

        entete_chambre = Gtk.Label()
        entete_chambre.set_markup("<span size='25000'>NUM CHAMBRE</span>".format(entete_chambre.get_text()))
        fixe.put(entete_chambre, 1100, 50)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeChambreOccupee(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup(
            "<span size='25000' foreground='dodgerblue'>Liste des clients des chambres occupées</span>".format(
                annoce.get_text()))
        fixe.put(annoce, 500, 0)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeChambreEnReserve(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup(
            "<span size='25000' foreground='dodgerblue'>Liste des clients des chambres en reserve</span>".format(
                annoce.get_text()))
        fixe.put(annoce, 500, 0)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class ListeChambreLibre(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        annoce = Gtk.Label()
        annoce.set_markup(
            "<span size='25000' foreground='dodgerblue'>Liste des clients des chambres libres</span>".format(
                annoce.get_text()))
        fixe.put(annoce, 500, 0)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class HistoriqueSta(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        fixe = Gtk.Fixed()
        self.add(fixe)

        entete_nom = Gtk.Label()
        entete_nom.set_markup("<span size='25000'>NOM</span>".format(entete_nom.get_text()))
        fixe.put(entete_nom, 200, 30)

        entete_prenom = Gtk.Label()
        entete_prenom.set_markup("<span size='25000'>PRENOM</span>".format(entete_prenom.get_text()))
        fixe.put(entete_prenom, 500, 30)

        entete_tel = Gtk.Label()
        entete_tel.set_markup("<span size='25000'>TELEPHONE</span>".format(entete_tel.get_text()))
        fixe.put(entete_tel, 800, 30)

        entete_chambre = Gtk.Label()
        entete_chambre.set_markup("<span size='25000'>NUM CHAMBRE</span>".format(entete_chambre.get_text()))
        fixe.put(entete_chambre, 1100, 30)

        y = 100
        i = 0
        for article in articles:
            i = i + 1
            x = 50
            valeur = article['title']
            label_historique_titre = Gtk.Label()
            label_historique_titre.set_text(valeur[:20])
            fixe.put(label_historique_titre, x, y)

            x = 530
            label_historique_author = Gtk.Label()
            label_historique_author.set_text(article['author'])
            fixe.put(label_historique_author, x, y)

            x = 840
            label_historique_source = Gtk.Label()
            label_historique_source.set_text(article['source']['name'])
            fixe.put(label_historique_source, x, y)

            x = 1200
            label_historique_desc = Gtk.Label()
            label_historique_desc.set_text(str(i))
            fixe.put(label_historique_desc, x, y)

            y = y + 30

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        fixe.put(retour, 0, 0)

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

class Statistique(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hotel  :   LA GAZELLE")
        self.set_border_width(10)
        self.set_default_size(1500, 900)
        self.connect("destroy", Gtk.main_quit)

        self.fixe = Gtk.Fixed()
        self.add(self.fixe)

        label_texte = Gtk.Label()
        label_texte.set_markup(
            "<span size='20000' foreground='white'>VEUILLEZ DONNER UN INTERVAL DE TEMPS \n\
POUR AVOIR L'ENSEMBLE DES RESERVATIONS\nEFFECTUEES PENDANT CETTE PERIODE\n\nNB : Utiliser le format : j-m-a</span>".
            format(label_texte.get_text()))
        self.fixe.put(label_texte, 900, 50)

        label_date_deb = Gtk.Label()
        label_date_deb.set_markup("<span size='25000' foreground='white'>DU</span>".format(label_date_deb.get_text()))
        self.fixe.put(label_date_deb, 1150, 230)

        self.champ_date_deb= Gtk.Entry()
        self.fixe.put(self.champ_date_deb, 1100, 350)

        label_date_fin = Gtk.Label()
        label_date_fin.set_markup("<span size='25000' foreground='white'>AU</span>".format(label_date_fin.get_text()))
        self.fixe.put(label_date_fin, 1150, 450)


        self.champ_date_fin = Gtk.Entry()
        self.fixe.put(self.champ_date_fin, 1100, 550)

        # Ajout de l'image
        image = Gtk.Image()
        image = Gtk.Image.new_from_file("Image/interieur_hotel.png")
        self.fixe.put(image, 0, 0)

        envoyer = Gtk.Button.new_with_label("ENVOYER")
        envoyer.connect("clicked", self.envoyer)
        self.fixe.put(envoyer, 1140, 700)

        retour = Gtk.Button.new_with_label("Retour")
        retour.connect("clicked", self.retour)
        self.fixe.put(retour, 1400, 0)

    def envoyer(self, champ_date_deb):
        date_deb = self.champ_date_deb.get_text()
        date_fin = self.champ_date_fin.get_text()

        if dateIsValide(date_deb) and dateIsValide(date_fin):
            self.hide()
            histo = HistoriqueSta()
            histo.show_all()
        else:
            dialogue = BoiteDialogue(self)
            dialogue.run()

    def retour(self, widget):
        boutonRetour(self, PagePrincipal)

if __name__ == "__main__":
    win = PagePrincipal()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()