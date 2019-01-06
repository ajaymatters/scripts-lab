var authors = {"Person1":{"name":"abc","title":"life"}, "Person2":{"name":"def","title":"love"}, "Person3":{"name":"geh","title":"power"}, "Person4":{"name":"xyz","title":"pqr"}};

document.getElementById('p1').innerHTML = authors.Person1["name"];
document.getElementById('t1').innerHTML = authors.Person1["title"];