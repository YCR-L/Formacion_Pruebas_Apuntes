////Using(imports)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{

    class Program
    {

        static void Main(string[] args)
        {
            try
            {

                ConvertirInput convertirInput = new ConvertirInput();
                Calculadora calculadora = new Calculadora();

                //Pedimos el primer número
                Console.WriteLine("Escriba el primer número: ");
                double primerN = convertirInput.ConvertirInputANumeral(Console.ReadLine());

                //Pedimos el operador
                Console.WriteLine("Escriba el operador: ");
                string operacion = Console.ReadLine();

                //Pedimos el segundo número
                Console.WriteLine("Escriba el segundo número: ");
                double segundoN = convertirInput.ConvertirInputANumeral(Console.ReadLine());

                //Imprimimos por consola el resultado
                double resultado = calculadora.Calcular(operacion, primerN, segundoN);

                Console.WriteLine("El resultado es:" + resultado);
                Console.WriteLine("---SE CORTA EJECUCIÓN DEL PROGRAMA---");

            }
            catch (Exception excepcion)
            {
                // TODO: start logging exceptions
                Console.WriteLine(excepcion.Message);
            }

        }

    }

}
