//Constantes
const resultado = document.querySelector('#resultado')
const mostrar_e = document.querySelector('#elecciones')
const elecciones = [' piedra', ' papel', 'tijeras']

//Creamos el handler que va a registrar el click de la opción que queremos elegir y actuar en consecuencia
const handler = (e) => {

  ver_resultados(e.target.innerHTML, elecciones[Math.floor(Math.random() * elecciones.length)])

}

//Por cada opcion para elegir (Piedra, Papel o Tijeras, generamos un botón)
elecciones.forEach(eleccion => {

  const button = document.createElement('button')
  button.innerHTML = eleccion
  button.addEventListener('click', handler)
  mostrar_e.appendChild(button)

})

//Concatenamos las opciones elegidas (nuestras y de la maquina), y dependiendo del resultado devuelve un valor o otro.
const ver_resultados = (nuestraEleccion, eleccionMaquina) => {

  switch (nuestraEleccion + eleccionMaquina) {

    case ' tijeras papel':
    case ' piedra tijeras':
    case ' papel piedra':
     resultado.innerHTML = 'Elegiste ' + nuestraEleccion + ' y la máquina elige ' + eleccionMaquina + ' , le machacaste! ¡Adiós Skynet!'
      break
    case ' papel tijeras':
    case ' tijeras piedra':
    case ' piedra papel':
     resultado.innerHTML = 'Elegiste ' + nuestraEleccion + ' y la máquina elige ' + eleccionMaquina + ' , perdiste, "mala suerte", a la próxima podrás (o no)'
      break
    case ' piedra piedra':
    case ' papel papel':
    case ' tijeras tijeras':
     resultado.innerHTML = 'Elegiste ' + nuestraEleccion + ' y la máquina elige ' + eleccionMaquina + ' , ...¿empate?'
      break

  }

}