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
  
    let formattedMM = mm.toString().padStart(2, "0");
    let formattedSS = ss.toString().padStart(2, "0");
    let formattedMS = ms.toString().padStart(2, "0");
  
    return `${formattedMM}:${formattedSS}:${formattedMS}`;
  }
  
  // Declare variables to use in our functions below
  
  let startTime;
  let elapsedTime = 0;
  let timerInterval;
  
  // Create function to modify innerHTML
  
  function print(txt) {
    document.getElementById("display").innerHTML = txt;
  }
  
  // Create "start" and  finish" functions
  
  function start() {
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(function printTime() {
      elapsedTime = Date.now() - startTime;
      print(timeToString(elapsedTime));
    }, 10);
    showButton("FINISH");
  }
  
  function finish() {
    // Check if session is shorter than 15 minutes
    if ((elapsedTime / 1000) < 15) {
      if (confirm("Session too short. Are sure you want to finish? The session won't be saved.")) {
        // GO TO MAIN PAGE
        window.location = document.getElementById("href").getAttribute("href");
      }
    }else if (confirm("Are you sure you want to finish this session?")) {
      clearInterval(timerInterval);
      // We insert duration value into form to POST to our view for processing 
      document.getElementById("duration").value = elapsedTime;
      document.getElementById("sendForm").click()
      /* print("00:00:00");
      elapsedTime = 0; */
      //showButton("START");
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
  //let finishButton = document.getElementById( finishButton");
  
  startButton.addEventListener("click", start);
  finishButton.addEventListener("click", finish);  // When click on finishButton, we get first a verification popup
  /* finishButton.addEventListener("click", finish); */
  