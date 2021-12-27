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
    // Show New-Session button and Home button
    if (document.getElementById("new_session") !== null) {
      document.getElementById('new_session').style.display = 'block';
    }
    if (document.getElementById("home-button") !== null) {
      document.getElementById('home-button').style.display = 'block';
    }
  }
} 


check_session();

