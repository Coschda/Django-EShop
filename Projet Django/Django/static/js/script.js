var alertRedInput = "#8C1010";
var trueGreenInput = "#07D86C"
var defaultInput = "rgba(10, 180, 180, 1)";

function userNameValidation(usernameInput) {
    var username = document.getElementById("username");
    var issueArr = [];

    if (username.value.length<1)
      username.style.borderColor = defaultInput;

    if (/([^\w!\&+=-_]+)/.test(usernameInput)) {// /([^\w!\&+=-_]+|&+)+/
        username.style.borderColor = alertRedInput;
        issueArr.push("Pas de caractères spéciaux !");

    }else{
        username.setCustomValidity("");
        username.style.borderColor = trueGreenInput;
    }
}

function passwordValidation(passwordInput) {
    var password = document.getElementById("password");
    var issueArr = [];
    if (!/^.{7,15}$/.test(passwordInput)) {
        issueArr.push("Password must be between 7-15 characters.");
    }
    if (!/\d/.test(passwordInput)) {
        issueArr.push("Must contain at least one number.");
    }
    if (!/[a-z]/.test(passwordInput)) {
        issueArr.push("Must contain a lowercase letter.");
    }
    if (!/[A-Z]/.test(passwordInput)) {
        issueArr.push("Must contain an uppercase letter.");
    }
    if (password.value.length<1){
      return password.style.borderColor = defaultInput;
    }
    if (issueArr.length > 0) {
        password.setCustomValidity(issueArr.join("\n"));
        password.style.borderColor = alertRedInput;
    } else {
        password.setCustomValidity("");
        password.style.borderColor = trueGreenInput;
    }
}

function passwordConfirmation(passwordToConfirm){
  const true_password = document.getElementById("password");
  var password_to_confirm = document.getElementById("password2");

  if(password_to_confirm.value.length <1){
    return password_to_confirm.style.borderColor = defaultInput;
  }if(true_password.value === password_to_confirm.value){
    password_to_confirm.style.borderColor = trueGreenInput;
  }else{
    password_to_confirm.style.borderColor = alertRedInput;
  }
}