/*Apuntes 
Introductorios
Kotlin */

//Bucles y Condicionales
fun main(args:Array<String>){

    val apellido1 = "Escudero"
    val apellido2 = "Romero"

    var apellidoLargo = ""

    getApellidoLargo(apellido1, apellido2)

    val password="pEP;t@ 301."
    comprobarPass(password)
    
    
    val nums = intArrayOf(1990,1991,1992,1993,1994,1995,1996,1997)
    //FOR
    for (num: Int in nums) println("-" + num + "-")

    var n = 1
    //WHILE
    while(n >0 && n <= 50){
        println(n)
        n++
    }
    //DO-WHILE
    do{
        println(n)
        n--
    } while (n > 0)
}

fun getApellidoLargo(apellido1: String, apellido2: String){

    //IF-ELSE
    var apellidoLargo = ""
    if(apellido1.length>apellido2.length){
        apellidoLargo = apellido1
    } else{
        apellidoLargo = apellido2
    }
    println("El apellido con mas letras es $apellidoLargo con " + apellidoLargo.length +" letras" )
}

fun comprobarPass(password: String){
    
    //WHEN(SWITCH)
    when(password.length){
        0 ->println("Contraseña vacia")
        in 1..5->println("Contraseña muy corta, contraseña de mínimo 6 carácteres")
        in 6..8->println("Contraseña débil")
        else->println("Contraseña adecuada")
    }
}