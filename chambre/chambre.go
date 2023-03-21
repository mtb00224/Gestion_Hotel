package chambre

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Chambre struct {
	Numero                string `json:"numero"`
	Etat                  string `json:"etat"`
	Etage_numero          int    `json:"etage_numero"`
	Categorie_idCategorie int    `json:"categorie_idCategorie"`
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

func RecupererChambre(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT numero, etat, etage_numero, categorie_idCategorie FROM chambre")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var chambres []Chambre
	for rows.Next() {
		var h Chambre
		if err := rows.Scan(&h.Numero, &h.Etat, &h.Etage_numero, &h.Categorie_idCategorie); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		chambres = append(chambres, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(chambres)
}

func CreerChambre(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var chambre Chambre
	err := json.NewDecoder(r.Body).Decode(&chambre)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO chambre(etat, etage_numero, categorie_idCategorie) VALUES(?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(chambre.Etat, chambre.Etage_numero, chambre.Categorie_idCategorie)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	chambre.Numero = strconv.FormatInt(id, 10)

	json.NewEncoder(w).Encode(chambre)
}

func MettreAJourChambre(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var chambre Chambre
	err = json.NewDecoder(r.Body).Decode(&chambre)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE chambre SET etat=?, etage_numero=?, categorie_idCategorie=? WHERE numero=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(chambre.Etat, chambre.Etage_numero, chambre.Categorie_idCategorie, id)
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
		http.Error(w, "Chambre non trouvee", http.StatusNotFound)
		return
	}

	chambre.Numero = strconv.Itoa(id)
	json.NewEncoder(w).Encode(chambre)
}

func SupprimerChambre(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM chambre WHERE numero=?")
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
		http.Error(w, "Chambre non trouvee", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "suppression reussie"})
}
