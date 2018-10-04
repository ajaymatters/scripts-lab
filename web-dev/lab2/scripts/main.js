

function dispGrade_sub1() {	

		var x = parseInt(document.getElementById("sub1").value);
		
		if (x >= 90) {
			document.getElementById("sub1_grade").innerHTML = "S"
		}

		else if (x >= 80 && x <90) {
			document.getElementById("sub1_grade").innerHTML = "A"	
		}

		else if (x >= 70 && x < 80) {
			document.getElementById("sub1_grade").innerHTML = "C"	
		}

		else {
			document.getElementById("sub1_grade").innerHTML = "Fail" + x
		}

}

function dispGrade_sub2() {
	var sub2 = (document.getElementById('sub2'));

	if (sub2 > 100) {
		document.getElementById('sub2_grade').innerHTML = "Please enter a value below 100"
	}

	else if (sub2 < 0) {
		document.getElementById('sub2_grade').innerHTML = "Please enter a value above 0"		
	}

	else {

		if (sub2 >= 90) {
			document.getElementById('sub2_grade').innerHTML = "S"
		}

		else if (sub2 >= 80 && sub2 <90) {
			document.getElementById('sub2_grade').innerHTML = "A"	
		}

		else if (sub2 >= 70 && sub2 < 80) {
			document.getElementById('sub2_grade').innerHTML = "C"	
		}

		else {
			document.getElementById('sub2_grade').innerHTML = "Fail"
		}

	}
}