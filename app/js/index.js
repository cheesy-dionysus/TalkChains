/* 

I built this login form to block the front end of most of my freelance wordpress projects during the development stage. 

This is just the HTML / CSS of it but it uses wordpress's login system. 

Nice and Simple

*/

function loginCheck(){
	document.getElementById('login').onsubmit = function (){
	    var user = document.getElementById("user").value;
	    var pass = document.getElementById("pass").value;
	    alert(user + " " + pass);
		return true;
	}
}

