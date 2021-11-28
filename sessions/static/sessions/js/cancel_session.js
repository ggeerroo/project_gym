// Remove items from storage
function clean_storage() {
    //Remove initial time from Storage 
    localStorage.removeItem('initialTime');
    //Remove sessionID from storage 
    localStorage.removeItem('current_session');
 }


  // Create event listeners
  let cancelButton = document.getElementById("cancelButton");

  cancelButton.addEventListener("click", clean_storage);