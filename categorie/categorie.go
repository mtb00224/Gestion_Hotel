package categorie

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

type Categorie struct {
	IdCategorie  int     `json:"idCategorie"`
	Classe       string  `json:"classe"`
	TarifNormal  float32 `json:"tarifNormal"`
	TarifSpecial float32 `json:"tarifSpecial"`
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

func RecupererCategorie(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT idCategorie, classe, tarifNormal, tarifSpecial FROM categorie")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var categories []Categorie
	for rows.Next() {
		var h Categorie
		if err := rows.Scan(&h.IdCategorie, &h.Classe, &h.TarifNormal, &h.TarifSpecial); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		categories = append(categories, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(categories)
}

func CreerCategorie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var categorie Categorie
	err := json.NewDecoder(r.Body).Decode(&categorie)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("INSERT INTO hotel(classe, tarifNormal, tarifSpecial) VALUES(?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(categorie.Classe, categorie.TarifNormal, categorie.TarifSpecial)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	categorie.IdCategorie = int(id)

	json.NewEncoder(w).Encode(categorie)
}

func MettreAJourCategorie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var categorie Categorie
	err = json.NewDecoder(r.Body).Decode(&categorie)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE categorie SET classe=?, tarifNormal=?, tarifSpecial=? WHERE idCategorie=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(categorie.Classe, categorie.TarifNormal, categorie.TarifSpecial, id)
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
		http.Error(w, "Hotel non trouve", http.StatusNotFound)
		return
	}

	categorie.IdCategorie = id
	json.NewEncoder(w).Encode(categorie)
}

func SupprimerCategorie(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM categorie WHERE idCategorie=?")
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
		http.Error(w, "Categorie non trouvee", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "suppression reussie"})
}

// func main() {
// 	r := mux.NewRouter()
// 	r.HandleFunc("/categorie", recupererCategorie).Methods("GET")
// 	r.HandleFunc("/categorie", creerCategorie).Methods("POST")
// 	r.HandleFunc("/categorie", mettreAJourCategorie).Methods("POST")
// 	r.HandleFunc("/categorie", supprimerCategorie).Methods("POST")
// 	log.Fatal(http.ListenAndServe(":8000", r))
// }
