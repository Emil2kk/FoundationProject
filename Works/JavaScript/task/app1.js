let a = 1;
let c = 1



function Tekrarla() {
    a++

    if (a % 2 == 1) {
        console.log(a)
    }
    if (a < 3000) {
        Tekrarla()
        c += a
    }
}
Tekrarla()
console.log(c);