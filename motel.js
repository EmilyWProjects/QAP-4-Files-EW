// Object:

const person = {
    firstName: "Emil",
    lastName: "Woodford",
    birthDate: "1994/01/30",
    birthyear: "1994",
    gender: "male",
    paymentMethod: "cash",
    address: {
      streetNumber: "11 Eleven Street",
      city: "TownsVille",
      province: "NL",
      postalCode: "A0A4E0",
      
    },
    phoneNumber: "(709) 786-0123",
    checkDates: {
      checkIn: "2024/04/01",
      checkOut: "2024/04/29",
    },
  },
  roomPref = [
    "single room",
    "double room",
    "suite",
    "penthouse"
  ];

let age;
age = person.getAge();
console.log("The customer is " + age +" years old.");

let dateIn = new Date("2024/04/01");
let dateOut = new Date("2024/04/29");
 
// Calculating the time difference
// of two dates
let diffTime =
    dateOut.getTime() - dateIn.getTime();
 
// Calculating the no. of days between
// two dates
let diffDays =
    Math.round
        (diffTime / (1000 * 3600 * 24));
 
// To display the final no. of days (result)
console.log
    ("The duration of the customer's stay from\n" +
        dateIn.toDateString() + " and " +
        dateOut.toDateString() +
        " is " + diffDays + " days");
        