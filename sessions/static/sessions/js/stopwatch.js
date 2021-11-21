// REFERENCE: https://tinloof.com/blog/how-to-build-a-stopwatch-with-html-css-js-react-part-2/

// Convert time to a format of hours, minutes, seconds, and milliseconds

function timeToString(time) {
    let diffInHrs = time / 3600000;
    let hh = Math.floor(diffInHrs);
  
    let diffInMin = (diffInHrs - hh) * 60;
    let mm = Math.floor(diffInMin);
  
    let diffInSec = (diffInMin - mm) * 60;
    let ss = Math.floor(diffInSec);
  
    let diffInMs = (diffInSec - ss) * 100;
    let ms = Math.floor(diffInMs);
  
    let formattedHH = hh.toString().padStart(2, "0");
    let formattedMM = mm.toString().padStart(2, "0");
    let formattedSS = ss.toString().padStart(2, "0");
    let formattedMS = ms.toString().padStart(2, "0");
  
    return `${formattedHH}:${formattedMM}:${formattedSS}:${formattedMS}`;
  }
  
  // Declare variables to use in our functions below
  
  let startTime;
  let elapsedTime;
  let timerInterval;
  
  // Create function to modify innerHTML
  
  function print(txt) {
    document.getElementById("display").innerHTML = txt;
  }
  
  // Remove items from storage
  function clean_storage() {
     //Remove initial time from Storage 
     localStorage.removeItem('initialTime');
     //Remove sessionID from storage 
     localStorage.removeItem('current_session');
  }


  // Create "start" and  "finish" functions
  function start() {
    // Save initial time in Local Storage
    // (Safe method: https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API)
    localStorage.setItem('initialTime', String(Date.now()));
    
    /* localStorage.setItem('initialTime', Date.now().toString()); */
    elapsedTime = 0;
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
      elapsedTime = Date.now() - startTime;
      print(timeToString(elapsedTime));
    }, 10);
    showButton("FINISH");
  }
  
  function finish() {
    // Check if session is shorter than 15 minutes
    if (Math.floor(elapsedTime / 10000) < 90) {
      if (confirm("Session too short. Are sure you want to finish? The session won't be saved.")) {
        clean_storage();
        // GO TO MAIN PAGE
        window.location = document.getElementById("href").getAttribute("href");
      }
    }else if (confirm("Are you sure you want to finish this session?")) {
      clearInterval(timerInterval);
      clean_storage();
      // We insert duration value into form to POST to our view for processing 
      document.getElementById("duration").value = elapsedTime;
      document.getElementById("sendForm").click()
    } 
  }

  // Create function to display buttons

  function showButton(buttonKey) {
    const buttonToShow = buttonKey === "START" ? startButton : finishButton;
    const buttonToHide = buttonKey === "START" ? finishButton : startButton;
    buttonToShow.style.display = "block";
    buttonToHide.style.display = "none";
  }
  
  // Create event listeners
  let startButton = document.getElementById("startButton");
  let finishButton = document.getElementById("finishButton");
  
  
  startButton.addEventListener("click", start);
  finishButton.addEventListener("click", finish);  // When click on finishButton, we get first a verification popup
    

// Reference:https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event
// Checks if a Session is already running, sets the timer accordingly and saves the session URL if necessary
  function session_status() {
    // Check if there's and initial time already saved in the storage
    if (localStorage.getItem('initialTime')) {
      showButton("FINISH");
      timerInterval = setInterval(function printTime() {
        elapsedTime = Date.now() - Number(localStorage.getItem('initialTime'));
        print(timeToString(elapsedTime));
      }, 10);    
    }
    // Save Session URL
    if (!localStorage.getItem('current_session')) {
      localStorage.setItem('current_session', window.location.href);
    }
  }
  

  if (document.readyState === 'loading') {  // Loading hasn't finished yet
    document.addEventListener('DOMContentLoaded', session_status);
  } else {  // `DOMContentLoaded` has already fired
    session_status();
  }



