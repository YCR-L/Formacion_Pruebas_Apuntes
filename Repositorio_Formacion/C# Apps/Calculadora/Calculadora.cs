//Using(imports)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{
    internal class Calculadora
    {
        public double Calcular(string argOperacion, double argPrimerN, double argSegundoN)
        {
            double resultado;
            switch (argOperacion.ToLower())

            {
                case "SUMA":
                case "+":
                    resultado = argPrimerN + argSegundoN;
                    break; //Corta ejecución

                case "RESTA":
                case "-":
                    resultado = argPrimerN - argSegundoN;
                    break; //Corta ejecución

                case "MULTIPLICA":
                case "*":
                    resultado = argPrimerN * argSegundoN;
                    break; //Corta ejecución

                case "DIVIDE":
                case "/":
                    resultado = argPrimerN / argSegundoN;
                    break; //Corta ejecución

                default:
                    throw new InvalidOperationException("Operación Desconocida/No válida");
            }

            return resultado;
        }
    }
}
