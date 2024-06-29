
function validateForm() {
    var fname = document.getElementById("fn").value;
    var pass = document.getElementById("p1").value;
    var checkp = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    var checkname = /^[A-Za-z]+$/;

    if (checkname.test(fname) && checkp.test(pass) && pass.length >= 8) {

        window.location.href = "Home.html";
        return false; // Prevent form submission
    } else {
        // Show error message(s) and prevent form submission
        if (!checkname.test(fname)) {
            alert("First name should only contain letters.");
        }
        if (!checkp.test(pass) || pass.length < 8) {
            alert("Password should be at least 8 characters long and contain a special character.");
        }
        return false;
    }
}

// validate.js

function validateSignUPForm() {
    // Regular expressions
    var nameRegex = /^[A-Za-z]+$/;
    var ageRegex = /^[0-9]+$/;
    var numberRegex = /^[0-9]+$/;
    var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    var contactNumberRegex = /^\d{10}$/;
    var passwordRegex = /^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;

    // Input fields
    var firstName = document.getElementById("fn").value;
    var lastName = document.getElementById("ln").value;
    var age = document.getElementById("age").value;
    var weight = document.getElementById("Weight").value;
    var height = document.getElementById("Height").value;
    var email = document.getElementById("e1").value;
    var contactNumber = document.getElementById("n1").value;
    var password = document.getElementById("p1").value;

    if(nameRegex.test(lastName) && nameRegex.test(lastName) && ageRegex.test(age) && numberRegex.test(weight) && numberRegex.test(height) && emailRegex.test(email) && contactNumberRegex.test(contactNumber) && passwordRegex.test(password)){
        window.location.href = "Home.html";

        return true
    }
else{

    // Validate first name
    if (!nameRegex.test(firstName)) {
        alert("Invalid first name. Only letters are allowed.");
        // return false;
    }

    // Validate last name
    if (!nameRegex.test(lastName)) {
        alert("Invalid last name. Only letters are allowed.");
        // return false;
    }

    // Validate age
    if (!ageRegex.test(age)) {
        alert("Invalid age. Only numbers are allowed.");
        // return false;
    }

    // Validate weight
    if (!numberRegex.test(weight)) {
        alert("Invalid weight. Only numbers are allowed.");
        // return false;
    }

    // Validate height
    if (!numberRegex.test(height)) {
        alert("Invalid height. Only numbers are allowed.");
        // return false;
    }

    // Validate email
    if (!emailRegex.test(email)) {
        alert("Invalid email format.");
        // return false;
    }

    // Validate contact number
    if (!contactNumberRegex.test(contactNumber)) {
        alert("Invalid contact number. Must be 10 digits.");
        // return false;
    }

    // Validate password
    if (!passwordRegex.test(password)) {
        alert("Invalid password. Must be at least 8 characters long and include special characters.");
        // return false;
    }
    return false;
}


    // If all validations pass
}
