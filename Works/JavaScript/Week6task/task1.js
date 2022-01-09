function a() {
    let l = 30
    let t = 30
    let element = document.createElement('div')
    element.className = 'box'
    element.style.left = `${l}%`
    element.style.top = `${t}%`
    document.body.appendChild(element)
}