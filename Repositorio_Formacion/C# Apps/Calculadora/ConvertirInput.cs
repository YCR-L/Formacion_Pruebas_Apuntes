//Using(imports)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculadora
{
    internal class ConvertirInput
    {
        public double ConvertirInputANumeral(string argInput)
        {
            double numeroConvertido;

            if (!double.TryParse(argInput, out numeroConvertido)) throw new ArgumentException("Se esperaba un valor numérico");
            return numeroConvertido;
        }
    }

}