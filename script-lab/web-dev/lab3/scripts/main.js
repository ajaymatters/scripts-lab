function yesnoCheck() {
    if (document.getElementById('Pizza').checked || document.getElementById('Burger').checked) {
        document.getElementById('ifPizza').style.visibility = 'visible';
    }
    else {
    	document.getElementById('ifPizza').style.visibility = 'hidden';
    }
}