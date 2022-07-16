using System;
using System.Collections.Generic;
using System.Linq;
using Palabras.Datos;
using Palabras.Utilidades;

namespace Palabras
{
    class Program
    {
        //Intanciamos el lector y el emparejador  
        private static readonly Lector lector = new Lector();
        private static readonly EmparejaPalabras ePalabras = new EmparejaPalabras();

        static void Main(string[] args)
        {
            try
            {
                bool continuarEjecucion = true;
                do
                {   
                    //Menu Principal, Entrada por archivo o por escrito(Manual)
                    Console.WriteLine(Constantes.MetodoEntrada);
                    var option = Console.ReadLine() ?? string.Empty;

                    switch (option.ToUpper())
                    {   
                        //Archivo
                        case Constantes.Archivo:
                            Console.Write(Constantes.PalabrasViaArchivo);
                            EjecucionArchivo();
                            break;
                        //Manual
                        case Constantes.Manual:
                            Console.Write(Constantes.PalabrasViaManual);
                            EjecucionManual();
                            break;
                        //Desconocida
                        default:
                            Console.WriteLine(Constantes.PalabrasOpcionDesconocida);
                            break;
                    }

                    var decisíonMenuContinuar = string.Empty;
                    do
                    {
                        //Menú ¿Continuar?
                        Console.WriteLine(Constantes.ContinuarPrograma);
                        decisíonMenuContinuar = (Console.ReadLine() ?? string.Empty);

                    } while (
                        //Poneruna opción diferente a Si/No, no está contemplado.
                        !decisíonMenuContinuar.Equals(Constantes.Si, StringComparison.OrdinalIgnoreCase) &&
                        !decisíonMenuContinuar.Equals(Constantes.No, StringComparison.OrdinalIgnoreCase));

                    continuarEjecucion = decisíonMenuContinuar.Equals(Constantes.Si, StringComparison.OrdinalIgnoreCase);

                } while (continuarEjecucion);
            }
            catch (Exception excepcion)
            {
                Console.WriteLine(Constantes.EProgramExit + excepcion.Message);
            }
        }

        //Método si escogemos la Opcion M en el menú inicial
        private static void EjecucionManual()
        {
            var manualInput = Console.ReadLine() ?? string.Empty;
            string[] palabrasDesordenadas = manualInput.Split(',');
            MostrarPalabrasNoDesordenadasEmparejadas(palabrasDesordenadas);
        }

        /*Método si escogemos la Opcion A en el menú inicial, siendo necesaria la ruta completa del archivo.
        Para realizar una prueba se podria realizar con el mismo archivo con el que compara.*/

        private static void EjecucionArchivo()
        {
            try
            {
                var nombreArchivo = Console.ReadLine() ?? string.Empty;
                string[] palabrasDesordenadas = lector.Leer(nombreArchivo);
                MostrarPalabrasNoDesordenadasEmparejadas(palabrasDesordenadas);
            }
            catch (Exception ex)
            {
                Console.WriteLine(Constantes.EPalabrasNoCarga + ex.Message);
            }
        }

        //Método para mostrar las palabras ordenadas correctamente que se emparejan con la/s introducida/s
        private static void MostrarPalabrasNoDesordenadasEmparejadas(string[] palabrasDesordenadas)
        {
            string[] listaPalabras = lector.Leer(Constantes.ArchivoListaPalabras);

            List<PalabraEmparejada> palabrasEmparejadas = ePalabras.Emparejar(palabrasDesordenadas,listaPalabras);

            if (palabrasEmparejadas.Any())
            {
                foreach (var palabraEmparejada in palabrasEmparejadas)
                {
                    Console.WriteLine(Constantes.Emparejadas, palabraEmparejada.PalabraDesordenada, palabraEmparejada.Palabra);
                }
            }
            else
            {
                Console.WriteLine(Constantes.NoEmparejadas);
            }
        }
    }
}

