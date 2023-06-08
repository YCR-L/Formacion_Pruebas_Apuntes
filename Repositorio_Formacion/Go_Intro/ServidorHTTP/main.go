package main

//IMPORTS
import (
	"fmt"
	"log"
	"net/http"
)

//Handler formulario
func formularioHandler(w http.ResponseWriter, r *http.Request) {

	if err := r.ParseForm(); err != nil {

		fmt.Fprintf(w, "ParseForm() err: %v", err)
		return
		
	}

	fmt.Fprintf(w, "POST request successful")
	nombre := r.FormValue("name")
	email := r.FormValue("email")
	fmt.Fprintf(w, "Nombre = %s\n", nombre)
	fmt.Fprintf(w, "Email = %s\n", email)

}

//Handler saludo
func saludoHandler (w http.ResponseWriter, r *http.Request) {

	if r.URL.Path != "/hola" {
		
		http.Error(w, "404 not found", http.StatusNotFound)
		return

	}

	if r.Method != "GET" {

		http.Error(w, "method is not supported", http.StatusNotFound)
		return

	}

	fmt.Fprintf(w, "¡Hola!")

}

//FuncionPrincipal
func main() {

	server := http.FileServer(http.Dir("./static"))
	http.Handle("/", server)
	http.HandleFunc("/form", formularioHandler)
	http.HandleFunc("/hola", saludoHandler )

	fmt.Printf("Arrancando el server en el puerto 8080 (revisa si lo tienes ocupado para evitar errores)\n")
	if err := http.ListenAndServe(":8080", nil); err != nil {

		log.Fatal(err)
		
	}
}