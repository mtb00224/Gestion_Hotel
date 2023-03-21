package client

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"
	"time"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Client struct {
	IdClient      string    `json:"idClient"`
	Nom           string    `json:"nom"`
	Prenom        int       `json:"prenom"`
	Telephone     int       `json:"telephone"`
	DateReserv    time.Time `json:"dateReserv"`
	DateEnter     time.Time `json:"dateEntrer"`
	DateSortie    time.Time `json:"dateSortie"`
	Nuite         int       `json:"nuite"`
	Hotel_idHotel int       `json:"Hotel_idHotel"`
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

func RecupererClient(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT idClient, nom, prenom, telephone, dateReserv, dateEnter, dateSortie, nuite, Hotel_idHotel FROM client")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var clients []Client
	for rows.Next() {
		var c Client
		if err := rows.Scan(&c.IdClient, &c.Nom, &c.Prenom, &c.Telephone, &c.DateReserv, &c.DateEnter, &c.DateSortie, &c.Nuite, &c.Hotel_idHotel); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		clients = append(clients, c)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(clients)
}

func CreerClient(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var client Client
	err := json.NewDecoder(r.Body).Decode(&client)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO client(nom, prenom, telephone, dateReserv, dateEnter, dateSortie, nuite, Hotel_idHotel) VALUES(?, ?, ?, ?, ?, ?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(client.Nom, client.Prenom, client.Telephone, client.DateReserv, client.DateEnter, client.DateSortie, client.Nuite, client.Hotel_idHotel)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	client.IdClient = strconv.FormatInt(id, 10)

	json.NewEncoder(w).Encode(client)
}

func MettreAJourClient(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var client Client
	err = json.NewDecoder(r.Body).Decode(&client)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE client SET nom=?, prenom=?, telephone=?, dateReserv=?, dateEnter=?, dateSortie=?, nuite=?, Hotel_idHotel=? WHERE idClient=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(client.Nom, client.Prenom, client.Telephone, client.DateReserv, client.DateEnter, client.DateSortie, client.Nuite, client.Hotel_idHotel, id)
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
		http.Error(w, "Client non trouvé", http.StatusNotFound)
		return
	}

	client.IdClient = strconv.Itoa(id)
	json.NewEncoder(w).Encode(client)
}

func SupprimerClient(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM client WHERE idClient=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(id)
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
		http.Error(w, "Client non trouvé", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "suppression réussie"})
}
