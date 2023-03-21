package hotel

import (
	"database/sql"
	"encoding/json"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

// Création de la base de donnée
type Hotel struct {
	IdHotel   int    `json:"idHotel"`
	Nom       string `json:"nom"`
	Adresse   string `json:"adresse"`
	Telephone string `json:"telephone"`
}

func dbConn() (db *sql.DB) {
	dbDriver := "mysql" //nom du pilote de base de donnée à utiliser
	dbUser := "root"    //nom utilisateur pour se connecter à la base de donnée
	dbPass := ""        //mot de passe de l'utilisateur
	dbName := "mydb"    //nom de la base de donnée
	/*
		Cette ligne de code utilise la méthode Open de la bibliothèque database/sql pour établir une connexion à la base de données MySQL.
		Si la variable err est différent de nulle donc une erreur sera renvoyer
	*/
	db, err := sql.Open(dbDriver, dbUser+":"+dbPass+"@/"+dbName)
	if err != nil {
		panic(err.Error())
	}
	return db
}

func RecupererHotel(w http.ResponseWriter, r *http.Request) {
	db := dbConn()
	rows, err := db.Query("SELECT idHotel, nom, adresse, telephone FROM hotel")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer rows.Close()

	var hotels []Hotel
	for rows.Next() {
		var h Hotel
		if err := rows.Scan(&h.IdHotel, &h.Nom, &h.Adresse, &h.Telephone); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		hotels = append(hotels, h)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(hotels)
}

// Création d'un nouveau hotel
func CreerHotel(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")

	var hotel Hotel
	err := json.NewDecoder(r.Body).Decode(&hotel) // Lecture des données JSON du corps de la requête et stockage dans la variable hotel
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	// Préparation de la requête SQL d'insertion
	stmt, err := db.Prepare("INSERT INTO hotel(nom, adresse, telephone) VALUES(?, ?, ?)")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Exécution de la requête SQL d'insertion avec les valeurs de l'hôtel à créer
	result, err := stmt.Exec(hotel.Nom, hotel.Adresse, hotel.Telephone)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Récupération de l'ID de l'hôtel créé
	id, err := result.LastInsertId()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Attribution de l'ID de l'hôtel créé à la variable hotel
	hotel.IdHotel = int(id)

	// Encodage des données JSON de l'hôtel créé et envoi dans le corps de la réponse
	json.NewEncoder(w).Encode(hotel)
}

// Mettre à jour un hotel existant
func MettreAJourHotel(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	var hotel Hotel
	err = json.NewDecoder(r.Body).Decode(&hotel)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("UPDATE hotel SET nom=?, adresse=?, telephone=? WHERE idHotel=?")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	result, err := stmt.Exec(hotel.Nom, hotel.Adresse, hotel.Telephone, id)
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

	hotel.IdHotel = id
	json.NewEncoder(w).Encode(hotel)
}

// Supprimer hotel
func SupprimerHotel(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db := dbConn()
	defer db.Close()

	stmt, err := db.Prepare("DELETE FROM hotel WHERE idHotel=?")
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
		http.Error(w, "Hotel non trouve", http.StatusNotFound)
		return
	}

	json.NewEncoder(w).Encode(map[string]string{"message": "suppression reussie"})
}
