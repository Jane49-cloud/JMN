// good old functions

    function greetings() {
        console.log('Hello Jane' )
        alert('Hello  Jane' )
    }

    greetings()

    //With arguments
    function greet(name){
        console.log('Hello there '  + name)
    }
    greet('Bob');
    greet('jane');
    greet('Susan');

    //return
    const wallHeight = 200

function calculate(value) {
    const newValue  = value * 2.54;
    console.log('the value is ' + newValue + 'cm') ;
    return newValue;
} 
const width = calculate(50)
const height = calculate(wallHeight)
const dimensions =[width, height]
console.log(dimensions) ;

function sum(){
const a = 10
const b = 50
sum =a+ b
return sum
    }
const addition = sum()
console.log(addition) ;