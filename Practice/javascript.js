PRINTING 2 NUMBERS 

var a = 13;
var b = 25;
console.log(a+b)

ODD OR EVEN

var checkeven = n => n%2 ==0 ? "EVEN" : "ODD";
console.log(checkeven(7))

PRINT 5 NUMBERS

for (let i = 0; i < 5; i++)
{
    console.log(i+1)
}

REVERSE

const reverse = function(str)
{
   return str.split("").reverse().join("");
}
console.log(reverse("HELLO WORLD"))

ODD OR EVEN USING FOR IF

let check = function(n)
{
    for(let i = 0;i<n; i++)
    {
        if (i%2 ==0)
        console.log(i + " EVEN");
        else
        console.log(i + " ODD")
    }
}
check(10)

PRIME NUMBERS 

let chack = function(n)
{
    if(n==2||n==3){
        console.log("PRIME");
        return;
    }

    if(n%2==0||n%3==0){
        console.log("NOT A PRIME");
        return;
    }

    let a = n**0.5;
    let ans = true;
    for(let i =5;i<=a;i+=2)
    {
        if(n%i==0)
        {
            ans = false;
            break;
        }
    }
console.log(ans?"PRIME NUMBER":"NOT PRIME");
}
chack(25);

FACTORIAL

function factorial(n){
    let fact =1;
    for(let i = n;i>0;i--)
        fact*=i;
return fact;
}
console.log("FACTORIAL :"+ factorial(6))

SPLIT FUNCTIONS

let sentence = "apple 123 banana 456 cherry 789";
let space = sentence.split(" ");
let limited = sentence.split(" ",2);
let nonum = sentence.split(/\d+/)
console.log("SPACE: " , space )
console.log("LIMITED: " ,limited)
console.log("WHEN NUMBERS: " ,nonum)

ARRAY FUNCTIONS - SPLICE

let fruits = ["APPLE","BANANA","CHERRY","DATE","FIG"];
console.log("ORIGINAL: ",fruits);
let removed = fruits.splice(2,2)
console.log("AFTER REMOVE ORIGINAL: ",fruits);
console.log("REMOVED: ",removed);
fruits.splice(2,0,"KIWI","GAUVA")
console.log("AFTER ADDING: ",fruits)
fruits.splice(2,1,"KIWIRRR","GAUVASSS")
console.log("AFTER REPLACING: ",fruits)

ARRAY FUNC CONCAT, SLICE, INDEX OF AND FOREACH

fruits = [ 'APPLE', 'BANANA', 'FIG' ];
removed = [ 'CHERRY', 'DATE' ];
added = fruits.concat(removed);
sliced = fruits.slice(0,2);
console.log(added);
console.log(sliced);
console.log(fruits.indexOf('CHERRY'));
removed.forEach(function(i)
{
    console.log(i);
});

MAP AND FILTER 

let num = [1,2,3,4,5];
let sq = num.map(function(i)
{
    return i * 2;
});
let fil = num.filter(function(i)
{
    return i %2 ==0;
});
console.log("*2 ",sq)
console.log("EVEN ",fil)

OBJECT 

let person = {
    name : "HARITHA",
    age : 22,
    degree :"B.E"
}
console.log(person.degree)

MAP

const visits = new Map();

const user = { id: 1 };
visits.set(user, 5);
visits.set("anonymous", 1);

console.log(visits.get(user));    
console.log(visits.has("anonymous"));
console.log(visits.size);         

for (const [k, v] of visits.entries()) {
  console.log(k,"-->", v);
}

visits.delete("anonymous");
console.log(visits.size); 

SET 
let num = [1,2,6,3,5,1,1,10];
let sett = new Set(num)
console.log(sett)
console.log(sett.size)
console.log(sett.has(7))
sett.add(61)
console.log(Array.from(sett))

PROMPT AND alert

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script>
    let num1 = parseFloat(prompt("Enter the first number:"));
    let num2 = parseFloat(prompt("Enter the second number:"));

    let sum = num1 + num2;

    alert("The sum is: " + sum);
  </script>
</body>
</html>