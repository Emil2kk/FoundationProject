let a = 1;
let c = 1



function Tekrarla() {
    a++
    c += a
    if (a) {
        console.log(a)
    }
    if (a < 3000) {
        Tekrarla()
        console.log(c);
    }
}
Tekrarla()