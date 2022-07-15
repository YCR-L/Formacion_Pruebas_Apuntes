/*Apuntes 
Introductorios
Kotlin */

//Variables y constantes

fun main(args:Array<String>){

    var nombre = "Yago"
    var apellidos: String

    apellidos = "Candal Romero"

    //Variable read-only
    var saludoNombreCompleto = "Hello " + mensaje

    print(saludoNombreCompleto)

    //Concatenación de Variables
    println("Nombre: " + nombre)
    println("Apellidos: " + apellidos)
    println("Nombre completo: " + nombre + apellidos)

    //Constantes
    const val x = 2
    const val y = 0
    const val res = x + y
    
    print(x)
    print(y)
    print(res)
}