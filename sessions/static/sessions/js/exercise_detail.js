// Check if there's a session running and display button to navigate to Session accordingly
function check_session() {
    
    if (localStorage.getItem('current_session')) {
        document.getElementById("current_session").href = localStorage.getItem('current_session');
        const my_button = document.getElementById("current_session");
        my_button.style.display = "block";
    }
}

check_session();