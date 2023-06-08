//Constantes Grid y Display de puntos
const grid = document.querySelector('.grid')
const resultadosDisplay = document.querySelector('.resultados')
//Necesarios para la posicion y identificacion correctas
let posicionDisparador = 202
let ancho = 15
let direccion = 1
let invasoresId
let dirDer = true
let muertos = []
let resultados = 0

for (let i = 0; i < 225; i++) {
  const square = document.createElement('div')
  grid.appendChild(square)
}

const squares = Array.from(document.querySelectorAll('.grid div'))

//Aliens
const aliens = [
  0,1,2,3,4,5,6,7,8,9,
  15,16,17,18,19,20,21,22,23,24,
  30,31,32,33,34,35,36,37,38,39
]

//Dibuja en pantalla
function draw() {
  for (let i = 0; i < aliens.length; i++) {
    if(!muertos.includes(i)) {
      squares[aliens[i]].classList.add('invasor')
    }
  }
}

draw()

//Eliminacion de Aliens
function remove() {
  for (let i = 0; i < aliens.length; i++) {
    squares[aliens[i]].classList.remove('invasor')
  }
}

squares[posicionDisparador].classList.add('disparador')

//MOVIMIENTOS (BORRAN Y PINTAN LOS ELEMENTOS)
//Movimiento aliado
function moverDisparador(e) {
  squares[posicionDisparador].classList.remove('disparador')
  switch(e.key) {
    case 'ArrowLeft': //izq
      if (posicionDisparador % ancho !== 0) posicionDisparador -=1
      break
    case 'ArrowRight' : //der
      if (posicionDisparador % ancho < ancho -1) posicionDisparador +=1
      break
  }
  squares[posicionDisparador].classList.add('disparador')
}
document.addEventListener('keydown', moverDisparador)

//Movimiento enemigo
function moverInvasores() {

  const leftEdge = aliens[0] % ancho === 0
  const rightEdge = aliens[aliens.length - 1] % ancho === ancho -1

  remove()

  if (rightEdge && dirDer) {

    for (let i = 0; i < aliens.length; i++) {
      aliens[i] += ancho +1
      direccion = -1
      dirDer = false
    }

  }

  if(leftEdge && !dirDer) {

    for (let i = 0; i < aliens.length; i++) {
      aliens[i] += ancho -1
      direccion = 1
      dirDer = true
    }

  }

  for (let i = 0; i < aliens.length; i++) {
    aliens[i] += direccion
  }

  draw()

  if (squares[posicionDisparador].classList.contains('invasor', 'disparador')) {

    resultadosDisplay.innerHTML = 'GAME OVER'
    clearInterval(invasoresId)

  }

  for (let i = 0; i < aliens.length; i++) {
    if(aliens[i] > (squares.length)) {

      resultadosDisplay.innerHTML = 'GAME OVER'
      clearInterval(invasoresId)

    }
  }
  if (muertos.length === aliens.length) {
    resultadosDisplay.innerHTML = 'GANASTE'
    clearInterval(invasoresId)
  }
}
invasoresId = setInterval(moverInvasores, 600)

//ATAQUE
function disparar(e) {

  let idLaser
  let currentLaserIndex = posicionDisparador
  //MOVIMIENTO DISPARO
  function movimientoLaser() {

    squares[currentLaserIndex].classList.remove('laser')
    currentLaserIndex -= ancho
    squares[currentLaserIndex].classList.add('laser')

    if (squares[currentLaserIndex].classList.contains('invasor')) {

      squares[currentLaserIndex].classList.remove('laser')
      squares[currentLaserIndex].classList.remove('invasor')
      squares[currentLaserIndex].classList.add('boom')

      setTimeout(()=> squares[currentLaserIndex].classList.remove('boom'), 300)
      clearInterval(idLaser)

      const muerto = aliens.indexOf(currentLaserIndex)
      muertos.push(muerto)
      resultados++
      resultadosDisplay.innerHTML = resultados
      console.log(muertos)

    }

  }
  switch(e.key) {
    case 'D': //Disparamos con la D
      idLaser = setInterval(movimientoLaser, 100)
  }
}

document.addEventListener('keydown', disparar)