
////////////////////////////////////////////////////////////////////////////////
// Here be Javascripts.
// JPxG, February 2022
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////
// Script to enable collapsing sections 
////////////////////////////////////////

var coll = document.getElementsByClassName("collapser");

var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    collapseString = this.id;
    collapseContentString = collapseString.replace("collapser", "collapsecontent");
    // var content = document.getElementById("collapsecontent" + String(i+1))
    //var content = this.nextElementSibling;
    var content = document.getElementById(collapseContentString);
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
    
  }); // End of listener
} // End of collapsible-sections script.


var coll = document.getElementsByClassName("collapser-change");

var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
  	this.innerHTML = this.innerHTML.replace("Show", "Extremely implausible string")
  	this.innerHTML = this.innerHTML.replace("Hide", "Show")
  	this.innerHTML = this.innerHTML.replace("Extremely implausible string", "Hide")
  }); // End of listener
} // End of collapsible-sections script.