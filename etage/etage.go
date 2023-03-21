package etage

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Etage struct {
	Numero        string `json:"numero"`
	NombreChambre string `json:"nombreChambre"`
	Hotel_idHotel int    `json:"Hotel_idHotel"`
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

func RecupererEtage(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT numero, nombreChambre, Hotel_idHotel FROM etage")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var etages []Etage
	for rows.Next() {
		var h Etage
		if err := rows.Scan(&h.Numero, &h.NombreChambre, &h.Hotel_idHotel); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		etages = append(etages, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(etages)
}

func CreerEtage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var etage Etage
	err := json.NewDecoder(r.Body).Decode(&etage)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO etage(numero, nombreChambre, Hotel_idHotel) VALUES(?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(etage.Numero, etage.NombreChambre, etage.Hotel_idHotel)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	etage.Numero = strconv.FormatInt(id, 10)

	json.NewEncoder(w).Encode(etage)
}

func MettreAJourEtage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var etage Etage
	err = json.NewDecoder(r.Body).Decode(&etage)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE etage SET numero=?, nombreChambre=?, Hotel_idHotel=? WHERE numero=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(etage.Numero, etage.NombreChambre, etage.Hotel_idHotel, id)
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
		http.Error(w, "Etage non trouve", http.StatusNotFound)
		return
	}

	etage.Numero = strconv.Itoa(id)
	json.NewEncoder(w).Encode(etage)
}

func SupprimerEtage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id := params["id"]

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM etage WHERE numero=?")
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
		http.Error(w, "Étage non trouvé", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "Suppression réussie"})
}
