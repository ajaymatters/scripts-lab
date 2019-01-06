function mult_2(){
	var x = document.getElementById('num').value;
	if (x == "") {
		document.getElementById('res_2').innerHTML = 'Please enter a valid number'
	}
	else
		document.getElementById('res_2').innerHTML = x*2;
}

function mult_itself() {
	var x = document.getElementById('num').value;
	if (x == "") {
		document.getElementById('res_itself').innerHTML = 'Please enter a valid number'
	}
	else
		document.getElementById('res_itself').innerHTML = x*x;
}
