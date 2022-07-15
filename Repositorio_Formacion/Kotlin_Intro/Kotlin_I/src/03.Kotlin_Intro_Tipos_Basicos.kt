/*Apuntes 
Introductorios
Kotlin */

/*Nota, esto es para aprender/apuntar,
obviamente lo correcto serían declarar todas las variables al principio
o en el método o función que se vayan a usar.*/

//Tipos básicos

fun main(args:Array<String>){
    
    //Numerales
        //Int
    var intl: Int
    var int2: Int

    int1 = 5
    int2 = 2
    //var resInt: Int = sumaInt(int1,int2)
        //Float
    var flo1: Float
    var flo2: Float
    //var resFlo: Float = sumaFloat(flo1,flo2)

    flo1 = 2.5f
    flo2 = 5.2f
        //Double
    var d1: Double
    var d2: Double
    //var resD: Double = sumaDouble(d1,d2)

    d1 = 5.2    
    d2 = 2.5

    println("Resultado suma int = "+ sumaInt(int1,int2))
    println("Resultado suma float = "+ sumaFloat(flo1, flo2))
    println("Resultado suma double = "+ sumaDouble(d1, d2))


    //Strings
    val name = "Yago"
    println(name)
    val birthyear = 1997
    val year = 2022
    println("Hola soy  $name , tengo ${year - birthyear} años y soy de Galicia")


    //Booleanos
    val day:Boolean=true
    val night:Boolean=true
    val cold: Boolean=true
    val hot: Boolean=true  

    //OR
    if(day || cold){
        println("No me apetece paseíto.")
    }

    // AND
    if(night && cold){
        println("Me lo pienso.")
    }
             
    // NOT (+ AND)
    if(!cold && !night ){
        print("¿Voy a la playa)")
    }

    //ARRAYS
    val animales = arrayOf("Gaviota", "Tortuga", "Salamandra", "Yo, ¡ups!")
    println(animales[4])
     //IntArray
    val numeros = intArrayOf(1,2,3)
    println(numeros[2])
}

//Hechos para los ejemplos de numerales
fun sumaInt(int1: Int, int2: Int): Int{
    return int1 + int2
}

fun sumaFloat(flo1: Float, flo2: Float): Float{
    return flo1 + flo2
}

fun sumaDouble(d1: Double, d2: Double): Double{
    return d1 + d2
}

