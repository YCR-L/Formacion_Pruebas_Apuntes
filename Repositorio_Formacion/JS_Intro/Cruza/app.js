//CONSTANTES
//Tiempo y resultado
const displayTiempo = document.querySelector('#tiempo')
const displayResultado = document.querySelector('#resultado')
//Pausa
const botonIniPausa = document.querySelector('#boton-inicio')
//Casillas y objetos
const squares = document.querySelectorAll('.grid div')
const cochesD = document.querySelectorAll('.coche-d')
const cochesI = document.querySelectorAll('.coche-i')
const maderasD = document.querySelectorAll('.madera-d')
const maderasI = document.querySelectorAll('.madera-i')

//Valores
let currentIndex = 76
const width = 9
let timerId
let outcomeTimerId
let currentTime = 20

//MOVIMIENTOS
//Movimientos Principales

//Rana
function moverRana(e) {
    squares[currentIndex].classList.remove('rana')

    switch(e.key) {

        case 'ArrowLeft' :
             if (currentIndex % width !== 0) currentIndex -= 1
            break
        case 'ArrowRight' :
            if (currentIndex % width < width - 1) currentIndex += 1
            break
        case 'ArrowUp' :
            if (currentIndex - width >=0 ) currentIndex -= width
            break
        case 'ArrowDown' :
            if (currentIndex + width < width * width) currentIndex += width
            break

    }
    
    squares[currentIndex].classList.add('rana')
}

//Elementos (General)
function moverElementos() {
    currentTime--
    displayTiempo.textContent = currentTime
    cochesD.forEach(cocheD => moverCochesD(cocheD))
    cochesI.forEach(cocheI => moverCochesI(cocheI))
    maderasD.forEach(maderaD => moverMaderaD(maderaD))
    maderasI.forEach(maderaI => moverMaderaI(maderaI))
}

//Movimientos Objetos

//Coches
function moverCochesD(cocheD) {

    switch(true) {

        case cocheD.classList.contains('c1') :
            cocheD.classList.remove('c1')
            cocheD.classList.add('c3')
            break
        case cocheD.classList.contains('c2') :
            cocheD.classList.remove('c2')
            cocheD.classList.add('c1')
            break
        case cocheD.classList.contains('c3') :
            cocheD.classList.remove('c3')
            cocheD.classList.add('c2')
            break

    }
}

function moverCochesI(cocheI) {

    switch(true) {

        case cocheI.classList.contains('c1') :
            cocheI.classList.remove('c1')
            cocheI.classList.add('c2')
            break
        case cocheI.classList.contains('c2') :
            cocheI.classList.remove('c2')
            cocheI.classList.add('c3')
            break
        case cocheI.classList.contains('c3') :
            cocheI.classList.remove('c3')
            cocheI.classList.add('c1')
            break

    }

}

//Madera
function moverMaderaD(maderaD) {

    switch(true) {

        case maderaD.classList.contains('l1') :
            maderaD.classList.remove('l1')
            maderaD.classList.add('l5')
            break
        case maderaD.classList.contains('l2') :
            maderaD.classList.remove('l2')
            maderaD.classList.add('l1')
            break
        case maderaD.classList.contains('l3') :
            maderaD.classList.remove('l3')
            maderaD.classList.add('l2')
            break
        case maderaD.classList.contains('l4') :
            maderaD.classList.remove('l4')
            maderaD.classList.add('l3')
            break
        case maderaD.classList.contains('l5') :
            maderaD.classList.remove('l5')
            maderaD.classList.add('l4')
            break

    }

}

function moverMaderaI(maderaI) {
    
    switch(true) {

        case maderaI.classList.contains('l1') :
            maderaI.classList.remove('l1')
            maderaI.classList.add('l2')
            break
        case maderaI.classList.contains('l2') :
            maderaI.classList.remove('l2')
            maderaI.classList.add('l3')
            break
        case maderaI.classList.contains('l3') :
            maderaI.classList.remove('l3')
            maderaI.classList.add('l4')
            break
        case maderaI.classList.contains('l4') :
            maderaI.classList.remove('l4')
            maderaI.classList.add('l5')
            break
        case maderaI.classList.contains('l5') :
            maderaI.classList.remove('l5')
            maderaI.classList.add('l1')
            break

    }
}




//CONDICIONES Y REVISIONES DE VICTORIA
function revisar() {
    perder()
    ganar()
}

function perder() {

    if (
        squares[currentIndex].classList.contains('c1') ||
        squares[currentIndex].classList.contains('l4') ||
        squares[currentIndex].classList.contains('l5') ||
        currentTime <= 0
    ) {
        displayResultado.textContent = 'PERDISTE'
        clearInterval(timerId)
        clearInterval(outcomeTimerId)
        squares[currentIndex].classList.remove('rana')
        document.removeEventListener('keyup', moverRana)
    }

}

function ganar() {

    if (squares[currentIndex].classList.contains('casilla-meta')) {
        displayResultado.textContent = 'GANASTE'
        clearInterval(timerId)
        clearInterval(outcomeTimerId)
        document.removeEventListener('keyup', moverRana)
    }

}

botonIniPausa.addEventListener('click', () => {

    if (timerId) {
        clearInterval(timerId)
        clearInterval(outcomeTimerId)
        outcomeTimerId = null
        timerId = null
        document.removeEventListener('keyup', moverRana)
    } else {
        timerId = setInterval(moverElementos, 1000)
        outcomeTimerId = setInterval(revisar, 50)
        document.addEventListener('keyup', moverRana)
    }

})