function myfunction() {
	var node = document.createElement("p");
    var textnode = document.createTextNode("Water");
    node.innerHTML(textnode);
    document.getElementById("listings").appendChild(node);

}