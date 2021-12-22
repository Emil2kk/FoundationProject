let a = 1;
let c = 1



function Tekrarla() {
    a++

    if (a % 3 == 0 && a % 7 == 1) {
        console.log(a)
        c += a
    }
    if (a < 3000) {
        Tekrarla()

    }
}
Tekrarla()
console.log(c);