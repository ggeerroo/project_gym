/* Reference: https://www.w3schools.com/howto/howto_js_sidenav.asp */

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  } 


// If there's a session running
function check_session() {
  // If we are in the Session page don't show Back to Session button
  if (window.location.href === localStorage.getItem('current_session')) {
    document.getElementById("back_to_session").style.display = "none";
  }
  // If we are on another page and there's an active Session we show the Back to Session button
  else if (localStorage.getItem('current_session')) {
    // Show Back-to-Session
    document.getElementById("back_to_session").href = localStorage.getItem('current_session');
    document.getElementById("back_to_session").style.display = "block";
  }
  // If no Session active
  else
  {
    // Show New-Session button
    document.getElementById('new_session').style.display = 'block';
  }
} 


check_session();

