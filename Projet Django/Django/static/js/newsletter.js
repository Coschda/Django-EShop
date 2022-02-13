var alertRedInput = "#8C1010";
var defaut = "#ced4da";

function EmailCheck(mail){
    var box = document.getElementById('form5Example21');
    var issueArr = [];

    if (box.value.length<1)
        issueArr = [];
        box.style.outline = 'none';

    if (/([^\w!\&+@-Z.]+)/.test(mail)){
        box.style.outline = '2px solid #8C1010';
        issueArr.push("Pas de caractères spéciaux !");
        
    }else{
        issueArr = [];
        box.style.outline = 'none';
    }
    document.getElementById('form5Example21label').innerHTML=issueArr;
}