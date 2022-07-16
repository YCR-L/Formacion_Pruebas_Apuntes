//Usings(Imports)
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Palabras
{
    internal class Constantes
    {
        //Lista con la que compara el programa, por defecto estando en el bin/debug del proyecto
        public const string ArchivoListaPalabras = "lista.txt";

        //Menús
        public const string MetodoEntrada = "¿Como se introducirán las palabras?: A - mediante archivo / M - manual ";
        public const string ContinuarPrograma = "¿Quieres continuar? S/N ";

        //Mensajes
        public const string PalabrasViaArchivo = "Escribe la ruta completa del archivo:  ";
        public const string PalabrasViaManual = "Escribe las palabras manualmente, y en caso de ser varias, sepáralas mediante ',':  ";
        public const string PalabrasOpcionDesconocida = "Opción desconocida/inválida";

        //Opciones Entrada
        public const string Archivo = "A";
        public const string Manual = "M";

        //Opciones Continuar
        public const string Si = "S";
        public const string No = "N";

        //Mensajes Resultado
        public const string Emparejadas = "vvv  COINCIDENCIA ENCONTRADA PARA {0}: {1}  vvv";
        public const string NoEmparejadas = "xxx  NO SE HAN ENCONTRADO COINCIDENCIAS  xxx";

        //Errores
        public const string EPalabrasNoCarga = "La carga de 'Palabras' ha fallado debido a un error  ";
        public const string EProgramExit = "La ejecución del programa se cerrará  ";

        

    }
}
