function eded(a) {
    console.log(a);
    return String(a)
}
eded(5)

function increase(a) {

    let c = a + 1
    console.log(c);
    return c
}
increase(3)

function decrease(a) {

    let c = a - 1
    console.log(c);
    return c
}
decrease(10)

function add(x, y) {

    let z = x + y
    console.log(z);
    return z
}
add(4, 6)

function subtract(x, y) {

    let z = x - y
    console.log(z);
    return z
}
subtract(3, 4)

function multiply(x, y) {
    let z = x * y
    console.log(z);
    return z
}
multiply(3, 6)

function divide(x, y) {
    let z = x / y
    console.log(z);
    return z
}
divide(10, 5)

function square(a) {
    let z = a * a
    console.log(z);
    return z
}
square(5)


function minimum(a, b) {
    if (a > b) {
        console.log(b);
        return b
    } else if (a < b) {
        console.log(a);
        return a

    }

}
minimum(2, 7)

function max(a, b) {
    if (a > b) {
        console.log(a);
        return a
    } else if (a < b) {
        console.log(b);
        return b
    }
}
max(2, 1)

function isEven(n) {
    if (n % 2 == 0) {
        n = true
        console.log(n);
        return true

    }
}
isEven(4)

function isOdd(n) {
    if (n % 2 == 1) {
        n = true
        console.log(n);
        return true

    }
}
isOdd(4)

function lettergrade(n) {
    if (n < 60 & n > 0) {
        console.log("F");
        return "F"
    }
    if (n < 70 & n > 59) {
        console.log("D");
        return "D"
    }
    if (n < 80 & n > 69) {
        console.log("C");
        return "C"
    }
    if (n < 90 & n > 79) {
        console.log("B");
        return "B"
    }
    if (n <= 100 & n > 89) {
        console.log("A");
        return "A"
    }

}
lettergrade(100)