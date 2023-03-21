package reservation

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Reservation struct {
	Client_idClient int     `json:"Client_idClient"`
	Chambre_numero  string  `json:"Chambre_numero"`
	Facture         float32 `json:"facture"`
}

func dbConn() (db *sql.DB) {
	dbDriver := "mysql"
	dbUser := "root"
	dbPass := ""
	dbName := "mydb"

	db, err := sql.Open(dbDriver, dbUser+":"+dbPass+"@/"+dbName)
	if err != nil {
		panic(err.Error())
	}
	return db
}

func RecupererReservation(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT Client_idClient , Chambre_numero, facture FROM reservation")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var reservations []Reservation
	for rows.Next() {
		var h Reservation
		if err := rows.Scan(&h.Client_idClient, &h.Chambre_numero, &h.Facture); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		reservations = append(reservations, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(reservations)
}

func CreerReservation(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var reservation Reservation
	err := json.NewDecoder(r.Body).Decode(&reservation)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO reservation(Client_idClient, Chambre_numero, facture) VALUES(?, ?, ?) ON DUPLICATE KEY UPDATE facture=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(reservation.Client_idClient, reservation.Chambre_numero, reservation.Facture, reservation.Facture)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if rowsAffected == 0 {
		http.Error(w, "Failed to create or update reservation", http.StatusInternalServerError)
		return
	}

	reservationID := strconv.Itoa(reservation.Client_idClient) + "-" + reservation.Chambre_numero
	reservation.ID = reservationID

	json.NewEncoder(w).Encode(reservation)
}

func MettreAJourReservation(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    params := mux.Vars(r)
    clientID, err := strconv.Atoi(params["Client_idClient"])
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    chambreNumero := params["Chambre_numero"]

    var reservation Reservation
    err = json.NewDecoder(r.Body).Decode(&reservation)
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    db := dbConn()
    defer db.Close()

    stmt, err := db.Prepare("UPDATE reservation SET facture=? WHERE Client_idClient=? AND Chambre_numero=?")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    result, err := stmt.Exec(reservation.Facture, clientID, chambreNumero)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    rowsAffected, err := result.RowsAffected()
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    if rowsAffected == 0 {
        http.Error(w, "Réservation non trouvée", http.StatusNotFound)
        return
    }

    reservation.Client_idClient = clientID
    reservation.Chambre_numero = chambreNumero
    json.NewEncoder(w).Encode(reservation)
}

func SupprimerReservation(w http.ResponseWriter, r *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    params := mux.Vars(r)
    clientID, err := strconv.Atoi(params["Client_idClient"])
    if err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }
    chambreNumero := params["Chambre_numero"]

    db := dbConn()
    defer db.Close()

    stmt, err := db.Prepare("DELETE FROM reservation WHERE Client_idClient=? AND Chambre_numero=?")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    result, err := stmt.Exec(clientID, chambreNumero)
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    rowsAffected, err := result.RowsAffected()
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }

    if rowsAffected == 0 {
        http.Error(w, "Réservation non trouvée", http.StatusNotFound)
        return
    }

    json.NewEncoder(w).Encode(map[string]string{"message": "suppression réussie"})
}
