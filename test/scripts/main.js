myHeading = document.querySelector('h1');
myHeading.textContent = 'Homepage';

var myButton = document.querySelector('button');

function warnUser() {
  var myName = prompt('Please enter your name.');
  localStorage.setItem('name', myName);
  myHeading.textContent = 'Get out of here, ' + myName;
}

if(!localStorage.getItem('name')) {
  warnUser();
} else {
  var storedName = localStorage.getItem('name');
  myHeading.textContent = 'Get out of here, ' + storedName;
}

myButton.onclick = function() {
  warnUser();
}