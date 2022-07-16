//Usings(Imports)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Palabras.Utilidades
{
    internal class Lector
    {
        public string[] Leer (string nombreArchivo)
        {
            string[] contenido;
            try
            {
                contenido = File.ReadAllLines(nombreArchivo);
            }
            catch (Exception excepcion)
            {
                throw new Exception(excepcion.Message);
            }
            return contenido;
        }

    }
}
