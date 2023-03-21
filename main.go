package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"

	"gestion_hotel/categorie"
	"gestion_hotel/chambre"
	"gestion_hotel/client"
	"gestion_hotel/etage"
	"gestion_hotel/hotel"
	"gestion_hotel/serviceannexe"
	"gestion_hotel/reservation"
)

func main() {
	router := mux.NewRouter()

	// Enregistrement des routes HTTP
	router.HandleFunc("/hotels", hotel.RecupererHotel).Methods("GET")
	router.HandleFunc("/hotels", hotel.CreerHotel).Methods("POST")
	router.HandleFunc("/hotels/{id}", hotel.MettreAJourHotel).Methods("PUT")
	router.HandleFunc("/hotels/{id}", hotel.SupprimerHotel).Methods("DELETE")

	router.HandleFunc("/categorie", categorie.RecupererCategorie).Methods("GET")
	router.HandleFunc("/categorie", categorie.CreerCategorie).Methods("POST")
	router.HandleFunc("/categorie{id}", categorie.MettreAJourCategorie).Methods("POST")
	router.HandleFunc("/categorie{id}", categorie.SupprimerCategorie).Methods("POST")

	router.HandleFunc("/chambre", chambre.RecupererChambre).Methods("GET")
	router.HandleFunc("/chambre", chambre.CreerChambre).Methods("POST")
	router.HandleFunc("/chambre", chambre.MettreAJourChambre).Methods("POST")
	router.HandleFunc("/chambre", chambre.SupprimerChambre).Methods("POST")

	router.HandleFunc("/client", client.RecupererClient).Methods("GET")
	router.HandleFunc("/client", client.CreerClient).Methods("POST")
	router.HandleFunc("/client", client.MettreAJourClient).Methods("POST")
	router.HandleFunc("/client", client.SupprimerClient).Methods("POST")

	router.HandleFunc("/etage", etage.RecupererEtage).Methods("GET")
	router.HandleFunc("/etage", etage.CreerEtage).Methods("POST")
	router.HandleFunc("/etage", etage.MettreAJourEtage).Methods("POST")
	router.HandleFunc("/etage", etage.SupprimerEtage).Methods("POST")

	router.HandleFunc("/serviceannexe", serviceannexe.RecupererServiceAnnexe).Methods("GET")
	router.HandleFunc("/serviceannexe", serviceannexe.CreerServiceAnnexe).Methods("POST")
	router.HandleFunc("/serviceannexe", serviceannexe.MettreAJourServiceAnnexe).Methods("POST")
	router.HandleFunc("/serviceannexe", serviceannexe.SupprimerServiceAnnexe).Methods("POST")

	router.HandleFunc("/reservation", reservation.RecupererReservation).Methods("GET")
	router.HandleFunc("/reservation", reservation.CreerReservation).Methods("POST")
	router.HandleFunc("/reservation", reservation.MettreAJourReservation).Methods("POST")
	router.HandleFunc("/reservation", serviceannexe.SupprimerReservation).Methods("POST")

	// Démarrage du serveur
	fmt.Println("Serveur démarré sur le port :8000")
	log.Fatal(http.ListenAndServe(":8000", router))
}
