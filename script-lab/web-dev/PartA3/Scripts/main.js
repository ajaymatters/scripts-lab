function len(){
	var sentence = document.getElementById('input').value;
	var s = sentence.split(" ");
	var max = s[0].length;
	for (var i = 1; i < s.length; i++) {
		if(s[i].length > max){
			max = s[i].length;
		}
	}

	document.getElementById('long').innerHTML = max;

}