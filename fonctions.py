import time
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

"""
    cette fonction permet de vérifier si une date est valide :
    une date est valide si elle est composée de chiffre et qu'elle est de la forme : jj-mm-aaaa
"""
def dateIsValide(date):
    #date = str(date)
    date = date.split("-")
    if date[0].isdigit() and date[1].isdigit() and date[2].isdigit():
        if len(date) != 3:
            return False
        else:
            return True
    else:
        return False


"""
    cette fonction se charge de verifier qu'une date de reservation est correcte :
    une date de reservtion est correcte lorsqu'elle est bien defin c a d elle n'est pas inferieur à la date en cours
"""
def dateIsCorrect(date):
    today = time.localtime()
    if dateIsValide(date):
        date = date.split("-")
        if int(date[2]) == today[0]:
            if int(date[1]) >= today[1] and int(date[0]) >= today[2]:
                return True
            elif int(date[0]) < today[2] and int(date[1]) >= today[1]:
                return True
            else:
                return False
        else:
            return False

def chaineIsValide(chaine):
    return chaine.isalpha()

def colorBackground(self, color):
    rgba = Gdk.RGBA.from_color(Gdk.color_parse(color))
    self.override_background_color(Gtk.StateFlags.NORMAL, rgba)


def boutonRetour(self, classe):
    self.hide()
    instance = classe()
    instance.show_all()


class BoiteDialogue(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, parent=parent)
        self.set_title("Hotel   :   LA GAZELLE")
        self.set_default_size(400, 300)
        colorBackground(self, "black")
        self.add_button("_OK", Gtk.ResponseType.OK)
        self.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        self.connect("response", self.reponse)

        label = Gtk.Label()
        label.set_markup("<span size='25000' foreground='red'>\t\t\t\tALERTE \n\nVEUILLEZ VERIFIER CE QUE VOUS AVEZ SAISI</span>".format(label.get_text()))
        self.vbox.add(label)

        self.show_all()

    def reponse(self, dialog, reponse):

        dialog.destroy()

class BoiteDialogueSucces(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, parent=parent)
        self.set_title("Hotel   :   LA GAZELLE")
        self.set_default_size(300, 200)
        colorBackground(self, "black")
        self.add_button("_OK", Gtk.ResponseType.OK)
        self.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        self.connect("response", self.reponse)

        label = Gtk.Label()
        label.set_markup("<span size='25000' foreground='green'>\n\nBIEN ENVOYE </span>".format(label.get_text()))
        self.vbox.add(label)

        self.show_all()

    def reponse(self, dialog, reponse):
        dialog.destroy()

class BoiteDialogueAlerte(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, parent=parent)
        self.set_title("Hotel   :   LA GAZELLE")
        self.set_default_size(300, 200)
        colorBackground(self, "black")
        self.add_button("_OUI", Gtk.ResponseType.OK)
        self.add_button("_NON", Gtk.ResponseType.CANCEL)
        self.connect("response", self.reponse)

        label = Gtk.Label()
        label.set_markup("<span size='25000' foreground='orange'>\n\nETES-VOUS SûR ?</span>".format(label.get_text()))
        self.vbox.add(label)

        self.show_all()

    def reponse(self, dialog, reponse):
        dialog.destroy()


class BoiteDialogueDescription(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, parent=parent)
        self.set_title("Description Hotel")
        colorBackground(self, "white")
        self.set_default_size(700, 350)
        self.add_button("_OK", Gtk.ResponseType.OK)
        self.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        self.connect("response", self.reponse)

        label = Gtk.Label()
        label.set_markup(
            "<span size='20000' foreground='dodgerblue'>\tVOICI LES INFORMATIONS DE L'HOTEL\n\n"
            "Nom\t\t\t\t\t:   LA GAZELLE\n\nNombre d' etage\t\t:   12\n\nNombre de chambre\t:   10\n\nAdresse\t\t\t\t:   Rue x angle y quartier z"
            "</span>".format(label.get_text()))
        self.vbox.add(label)

        self.show_all()

    def reponse(self, dialog, response):

        dialog.destroy()
