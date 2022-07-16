using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Palabras.Datos;
using System.IO;

namespace Palabras.Utilidades
{
    internal class EmparejaPalabras
    {
        public List<PalabraEmparejada> Emparejar(string[] palabrasDesordenadas, string[] wordList)
        {
            var palabraEmparejadas = new List<PalabraEmparejada>();

            foreach (var palabraDesordenada in palabrasDesordenadas)
            {
                foreach (var palabra in wordList)
                {
                    if (palabraDesordenada.Equals(palabra, StringComparison.OrdinalIgnoreCase))
                    {
                        palabraEmparejadas.Add(FormarPalabraEmparejada(palabraDesordenada, palabra));
                    }
                    else
                    {
                        var ArrayPDesordenadas = palabraDesordenada.ToCharArray();
                        var ArrayP = palabra.ToCharArray();

                        Array.Sort(ArrayPDesordenadas);
                        Array.Sort(ArrayP);

                        var pdOrganizadas = new string(ArrayPDesordenadas);
                        var pOrganizadas = new string(ArrayP);

                        if (pdOrganizadas.Equals(pOrganizadas, StringComparison.OrdinalIgnoreCase))
                        {
                            palabraEmparejadas.Add(FormarPalabraEmparejada(palabraDesordenada, palabra));
                        }
                    }
                }
            }

            return palabraEmparejadas;
        }

        private PalabraEmparejada FormarPalabraEmparejada(string palabraDesordenada, string palabra)
        {
            PalabraEmparejada palabraEmparejada = new PalabraEmparejada
            {
                PalabraDesordenada = palabraDesordenada,
                Palabra = palabra
            };

            return palabraEmparejada;
        }
    }

}

