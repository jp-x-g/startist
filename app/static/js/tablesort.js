
////////////////////////////////////////////////////////////////////////////////
// Here be Javascripts.
// JPxG, February 2022
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////
// Script to enable table sorting 
////////////////////////////////////////

/*
function sortTable(n) {
  var table, rows, switchingEnabled;
  // The table itself, array of rows, whether switching is active...
  var i, x, y;
  // Iterator, and variables for the current/next cell.
  var direction, switchcount = 0;
  // Asc/desc, and count of all switches hitherto.
  table = document.getElementById("editsTable");
  switchingEnabled = true;
  direction = "asc";
  rows = table.rows;
  for (j = 1; j < (rows.length - 1); j++) {
  while (switchingEnabled) {
    switchingEnabled = false;
    for (i = 1; i < (rows.length - 1); i++) {
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      if (((direction == "asc") && (x.innerHTML > y.innerHTML)) || ((direction == "desc") && (x.innerHTML < y.innerHTML))) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows [i]);
        switchingEnabled = true;
        switchCount ++;
      } // if desc and less than the next one... or if asc and more than the next one
    } // For every row in the table.
    if (switchcount == 0 && direction == "asc") {
      direction = "desc";
      switchingEnabled = true;
    }
  } // While switching is enabled.
  }
} */

function sortTable(n, tableId) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("editsTable");
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  // Make a loop that will continue until no switching has been done:
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    // Loop through all table rows (except the
    // first, which contains table headers):
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      // Get the two elements you want to compare,
      // one from current row and one from the next:
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      // Check if the two rows should switch place,
      // based on the direction, asc or desc:
      xText = x.innerHTML.toLowerCase().replaceAll("/*", "").replaceAll("*/", "")
      yText = y.innerHTML.toLowerCase().replaceAll("/*", "").replaceAll("*/", "")
      console.log(xText.href);
      if (xText.href) {
        console.log("woof");
        xText = xText.innerHTML;
      }
      if (yText.href) {
        yText = yText.innerHTML;
      }

      if ((dir == "asc") && (xText > yText)) {
        console.log(xText)
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
      } else if ((dir == "desc") && (xText < yText)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
      }
    }
    if (shouldSwitch) {
      // If a switch has been marked, make the switch
      // and mark that a switch has been done:
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      // If no switching has been done AND the direction is "asc",
      // set the direction to "desc" and run the while loop again.
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
