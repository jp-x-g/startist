
////////////////////////////////////////////////////////////////////////////////
// Here be Javascripts.
// JPxG, February 2022
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////
// Listener to clear all boxes when the "clear all" button is pressed
////////////////////////////////////////

document.getElementById("clearall").addEventListener("click", function() {
	var inputs = document.getElementsByTagName("input");
	for(var i = 0; i < inputs.length; i++) {
		if(inputs[i].type == "checkbox") {
			inputs[i].checked = false;
		} // If it's a checkbox.
	} // For all inputs.
	SyncListener("boxns", "boxnsca", "boxnssa");
	SyncListener("boxnst", "boxnscat", "boxnssat");
	SyncListener("boxnb", "boxnbca", "boxnbsa", "boxnbsatop");
	SyncListener("boxrd", "boxrdca", "boxrdsa", "boxrdsatop");
	SyncListener("boxvp", "boxvpca", "boxvpsa", "boxvpsatop");
	SyncListener("boxth", "boxthca", "boxthsatop");
}) // end of event listener

////////////////////////////////////////
// Script for "select all", "clear all", "invert" boxes
////////////////////////////////////////

function setAll(button, classname, setTo, flag) {
	//if (flag == "onTrue") { if (document.getElementById(button).checked == false) {return;}}
	//if (flag == "onFalse") { if (document.getElementById(button).checked == false) {return;}}
	document.getElementById(button).addEventListener("click", function() {
		//if (this.checked == true) {	var boolCheck = true } else { var boolCheck = false }
		var boxes = document.getElementsByClassName(classname); // Get all noticeboard boxes.
		for (var i = 0; i < boxes.length; i++) {
			if ((setTo == true) || (setTo == false)) {	boxes[i].checked = setTo; }
			else {
				if (boxes[i].checked == false) { boxes[i].checked = true; }
				else { boxes[i].checked = false; }
			} // If it's "toggle"
		} // For each checkbox
		if (flag == "reset") {
			document.getElementById(button).checked = false;
		}
	}); // End of event listener
} // end of function 

setAll("boxnssa", "boxns", true, "onTrue");
setAll("boxnsca", "boxns", false, "onTrue");
setAll("boxnsia", "boxns", "invert", "reset");

setAll("boxnssat", "boxnst", true, "onTrue");
setAll("boxnscat", "boxnst", false, "onTrue");
setAll("boxnsiat", "boxnst", "invert", "reset");

setAll("boxnbsa", "boxnb", true, "onTrue");
setAll("boxnbca", "boxnb", false, "onTrue");
setAll("boxnbia", "boxnb", "invert", "reset");

setAll("boxrdsa", "boxrd", true, "onTrue");
setAll("boxrdca", "boxrd", false, "onTrue");
setAll("boxrdia", "boxrd", "invert", "reset");

setAll("boxvpsa", "boxvp", true, "onTrue");
setAll("boxvpca", "boxvp", false, "onTrue");
setAll("boxvpia", "boxvp", "invert", "reset");

setAll("boxnbsatop", "boxnb", true, "onTrue");
setAll("boxrdsatop", "boxrd", true, "onTrue");
setAll("boxvpsatop", "boxvp", true, "onTrue");
setAll("boxthsatop", "boxth", true, "onTrue");

////////////////////////////////////////
// Script for synchronizing doppelganger boxes
////////////////////////////////////////

function syncUp(button, doppelganger) {
	document.getElementById(button).addEventListener("click", function() {
		var val = document.getElementById(button).checked;
		document.getElementById(doppelganger).checked = val;
	}) // end of event listener
	document.getElementById(doppelganger).addEventListener("click", function() {
		var val = document.getElementById(doppelganger).checked;
		document.getElementById(button).checked = val;
	}) // end of event listener
} // end of function 

syncUp("boxns01t", "boxns01ttop")
syncUp("boxns03", "boxns03top")

////////////////////////////////////////
// Script to sync up "all" and "none" boxes. Expensive but necessary for completeness.
////////////////////////////////////////

function SyncListener(classname, none, all, all2) {
	console.log("Woof")
	var bice = document.getElementsByClassName(classname);
	var allChecked = 1;
	var allUnchecked = 1;
	for (var j = 0; j < bice.length; j++) {
		if (bice[j].checked == false) { allChecked = 0;}
		if (bice[j].checked == true) { allUnchecked = 0;}
	} // Scan each box.
	document.getElementById(none).checked = false;
	document.getElementById(all).checked = false;
	if (!(all2 === undefined)) { 
		document.getElementById(all2).checked = false;
	} // If second all has been provided
	if (allChecked == 1) {
		document.getElementById(all).checked = true;
		if (!(all2 === undefined)) { 
			document.getElementById(all2).checked = true;
		} // If second all has been provided
	} // If all checked
	if (allUnchecked == 1) {
		document.getElementById(none).checked = true;
	} // If all unchecked
}; // addSyncListener

function addGroupSyncListener(classname, none, all, all2) {
	var boxes = document.getElementsByClassName(classname);
	for (var i = 0; i < boxes.length; i++) {
		boxes[i].addEventListener("click", function() {
			SyncListener(classname, none, all, all2);
		}); // Event listener for box
	} // For each box.
	document.getElementById(none).addEventListener("click", function() {
		SyncListener(classname, none, all, all2);
	}); // Event listener for none
	document.getElementById(all).addEventListener("click", function() {
		SyncListener(classname, none, all, all2);
	}); // Event listener for all
	if (!(all2 === undefined)) {
		document.getElementById(all2).addEventListener("click", function() {
			SyncListener(classname, none, all, all2);
		}); // Event listener for all2
	} // If there even is an all2
} // addGroupSyncListener

/*

			// Append none, all, and all2 to the listeners because they change this state too.
			bice.push(document.getElementById(none));
			bice.push(document.getElementById(all));
			if (!(all2 === undefined)) { 
				bice.push(document.getElementById(all2));
			} // If all2 is specified
			*/
addGroupSyncListener("boxns", "boxnsca", "boxnssa");
document.getElementById("boxnsia").addEventListener("click", function() {
		SyncListener("boxns", "boxnsca", "boxnssa");
	})

addGroupSyncListener("boxnst", "boxnscat", "boxnssat");
document.getElementById("boxnsiat").addEventListener("click", function() {
		SyncListener("boxnst", "boxnscat", "boxnssat");
	})

addGroupSyncListener("boxnb", "boxnbca", "boxnbsa", "boxnbsatop");
document.getElementById("boxnbia").addEventListener("click", function() {
		SyncListener("boxnb", "boxnbca", "boxnbsa", "boxnbsatop");
	})

addGroupSyncListener("boxrd", "boxrdca", "boxrdsa", "boxrdsatop");
document.getElementById("boxrdia").addEventListener("click", function() {
		SyncListener("boxrd", "boxrdca", "boxrdsa", "boxrdsatop");
	})

addGroupSyncListener("boxvp", "boxvpca", "boxvpsa", "boxvpsatop");
document.getElementById("boxvpia").addEventListener("click", function() {
		SyncListener("boxvp", "boxvpca", "boxvpsa", "boxvpsatop");
	})

addGroupSyncListener("boxth", "boxthca", "boxthsatop");
document.getElementById("boxthia").addEventListener("click", function() {
		SyncListener("boxth", "boxthca", "boxthsatop");
	})

// Run them when the page loads, too.
SyncListener("boxns", "boxnsca", "boxnssa");
SyncListener("boxnst", "boxnscat", "boxnssat");
SyncListener("boxnb", "boxnbca", "boxnbsa", "boxnbsatop");
SyncListener("boxrd", "boxrdca", "boxrdsa", "boxrdsatop");
SyncListener("boxvp", "boxvpca", "boxvpsa", "boxvpsatop");
SyncListener("boxth", "boxthca", "boxthsatop");
