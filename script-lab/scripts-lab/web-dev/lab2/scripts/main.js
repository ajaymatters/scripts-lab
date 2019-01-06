

function dispGrade_sub1() {	

		var x = parseInt(document.getElementById("sub1").value);

		if (x > 100) {
			document.getElementById("sub2_grade").innerHTML = "Please enter a value below 100"
		}

		else if (x < 0) {
			document.getElementById("sub2_grade").innerHTML = "Please enter a value above 0"		
		}

		else {
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
				document.getElementById("sub1_grade").innerHTML = "Fail"
			}
	}

}

function dispGrade_sub2() {

	var y = parseInt(document.getElementById("sub2").value);

	if (y > 100) {
		document.getElementById("sub2_grade").innerHTML = "Please enter a value below 100"
	}

	else if (y < 0) {
		document.getElementById("sub2_grade").innerHTML = "Please enter a value above 0"		
	}

	else {

		if (y >= 90) {
			document.getElementById("sub2_grade").innerHTML = "S"
		}

		else if (y >= 80 && y <90) {
			document.getElementById("sub2_grade").innerHTML = "A"	
		}

		else if (y >= 70 && y < 80) {
			document.getElementById("sub2_grade").innerHTML = "C"	
		}

		else {
			document.getElementById("sub2_grade").innerHTML = "Fail"
		}

	}
}

function total(){
	var x = parseInt(document.getElementById("sub1").value);
	var y = parseInt(document.getElementById("sub2").value);

	document.getElementById("total").innerHTML = x + y
}