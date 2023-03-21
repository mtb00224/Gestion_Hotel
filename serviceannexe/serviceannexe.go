package serviceannexe

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type ServiceAnnexe struct {
	IdServiceAnnexe int     `json:"idServiceAnnexe"`
	Nom             string  `json:"nom"`
	Tarif           float32 `json:"tarif"`
	Client_idClient int     `json:"Client_idClient"`
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

func RecupererServiceAnnexe(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT idServiceAnnexe, nom, tarif, Client_idClient FROM serviceannexe")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var services []ServiceAnnexe
	for rows.Next() {
		var h ServiceAnnexe
		if err := rows.Scan(&h.IdServiceAnnexe, &h.Nom, &h.Tarif, &h.Client_idClient); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		services = append(services, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(services)
}

func CreerServiceAnnexe(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var serviceAnnexe ServiceAnnexe
	err := json.NewDecoder(r.Body).Decode(&serviceAnnexe)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO serviceannexe(nom, tarif, Client_idClient) VALUES(?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(serviceAnnexe.Nom, serviceAnnexe.Tarif, serviceAnnexe.Client_idClient)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	serviceAnnexe.IdServiceAnnexe = int(id)

	json.NewEncoder(w).Encode(serviceAnnexe)
}

func MettreAJourServiceAnnexe(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var serviceAnnexe ServiceAnnexe
	err = json.NewDecoder(r.Body).Decode(&serviceAnnexe)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE serviceannexe SET nom=?, tarif=?, Client_idClient=? WHERE idServiceAnnexe=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(serviceAnnexe.Nom, serviceAnnexe.Tarif, serviceAnnexe.Client_idClient, id)
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
		http.Error(w, "Service annexe non trouvé", http.StatusNotFound)
		return
	}

	serviceAnnexe.IdServiceAnnexe = id
	json.NewEncoder(w).Encode(serviceAnnexe)
}

func SupprimerServiceAnnexe(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM serviceannexe WHERE idServiceAnnexe=?")
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
		http.Error(w, "Service annexe non trouvé", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "suppression réussie"})
}
