// function disp_grade(id) {
// 	var m = "sub"+id;
// 	var d = "sub"+id+"_grade";
// 	var marks = document.getElementById(m).value;

// 	if(isNaN(marks)){
// 		document.getElementById(d).innerHTML = "Please enter a number"
// 	}

// 	else if (marks > 100) {
// 		document.getElementById(d).innerHTML = "Please enter a value below 100"
// 	}

// 	else if (marks < 0) {
// 		document.getElementById(d).innerHTML = "Please enter a value above 0"
// 	}

// 	else {
// 		document.getElementById(d).innerHTML = grade(marks)
// 	}
// }


// function grade(marks) {	

// 			if (marks >= 90) {
// 				return "S"
// 			}
// 			else if (marks >= 80 && marks <90) {
// 				return "A"	
// 			}
// 			else if (marks >= 70 && marks < 80) {
// 				return "B"	
// 			}
// 			else if (marks >= 60 && marks < 70) {
// 				return "C"	
// 			}
// 			else {
// 				return "Fail"
// 			}

// }



// function total(){
// 	var x = parseInt(document.getElementById("sub1").value);
// 	var y = parseInt(document.getElementById("sub2").value);
// 	if (isNaN(x)) {
// 		document.getElementById('total').innerHTML = "Please enter sub1 marks"
// 	}
// 	else if (isNaN(y)) {
// 		document.getElementById('total').innerHTML = "Please enter sub2 marks"
// 	}
// 	else{
// 	document.getElementById("total").innerHTML = x + y
// 	}
// }


function divis(){
	var x = document.getElementById('div').value;

	if (x < 0 || isNaN(x)) {
		document.getElementById('check_divis').innerHTML = "Enter a valid number";
	}
	else if( x % 3 == 0 || x % 7 == 0){
		document.getElementById('check_divis').innerHTML = "Divisible by 3 or 7";	
	}
	else{
		document.getElementById('check_divis').innerHTML = "Not divisible by 3 or 7";	
	}

}