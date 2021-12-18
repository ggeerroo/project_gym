# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
This project is an attempt to create a useful tool for people who go to the gym and want to keep track of their progress. 
So far it only supports one specific routine: Push-Pull-Leg.

## **What you can do with this app:** 
- You can check the available Routines and their respective Exercises.
- You can check when was the last time you did each Routine.
- You can choose a Routine for your Session.
- You can check the information for each Exercise in your current Session.
- You can keep track of the duration of your Session.
- You can check your latest progress for each Exercise (sets, reps, weight, and personal notes related to the exercise).

## **What I'm hoping you will be able to do in the future:**
- See a chart with the progress for each Exercise through time.
- Get statistics and data derived from all your Sessions (e.g.: average Session duration, Exercise were most progress was achieved, preferred time for going to the gym, etc.).
- Get a calendar showing what Routine you did on which day.
- Getting a notice for which Routine is due and which Exercise should be updated.

## **Background**:
I started going to the gym using a Pull-Push-Leg workout routine from the internet as a guide. There was no coach available all the time at the gym so I needed to constantly check the file with the routines and exercises to see what exercise was next and how to perform the movement. Then I started using my phone's notepad to write each routine with the corresponding exercises' information, like sets, reps and weight, as well as some side notes that I thought useful. At the same time, I was using my phone's stopwatch to time my workouts. It wasn't long (or maybe it was) before I realized I could create an app that could help me manage all that information in a more convinient way, and that's when the idea for this app was born.

## **Why a web-based app?**
Even though I think an Android app would be more suitable (I'm just guessing), I decided to make a web app because it was the technology that I was learning. I had no Django backgound, just some experience with Flask from CS50x, so I had to learn it from scratch, but that was part of the reason why I chose it, to challenge myself and learn something new. I cannot say I'm any good at it, but at least I became familiar with the technology and the basic workflow.
However, I think the fact that a web app would allow anyone to have access to the app no matter what OS they are using is also pretty cool. If you have a web browser, you would be able to use the app.

## **Bro, do you even front-end?**
Barely. I was more focused on the server side of things so I'm well aware that my app is not particularly good looking. I'm trying to improve the interface as I go, starting with the more evidently ugly, but for now I'm not going much further than just keeping it clear and simple.

## **Simple problems require hacky solutions...?:**
####Two big challenges: keeping track of the time for the timer and keeping track of the Session id.
Something seemingly as simple as having a button to go back to an ongoing Session proved to be a big challenge because I needed to find a way to keep track of the Session id while navigating through the app. Something similar happened when I found out that when I left my web browser while my Session was running meant that the timer would restart once I came back to the Session. Basically anytime the page was refreshed.

So, for both problems I needed some sort of storage (wink wink) that kept its data through time (at least until the Session was over) no matter what page I was currently on. After some searching, I found two options that seemed to fulfill this requirement: Local Storage and Cookies. I guess the main reasons why I chose Local Storage over Cookies was that they were easier to work with using JS on the front-end of things, without having to deal with Cookies on the server side. I know there's also Session Storage but I thought it wasn't suitable as the data is lost once the browser is closed.

For the timer problem, I think Local Storage was definetely the right choice, because I only need to store a number with no security implications, and I use it only when I go back to the Session page, so there's no need to keep sending it back and forth as is the case with Cookies. For the Session id problem, I'm not so sure Local Storage is the best solution, because I'm actually storing the whole URL for the active Session and I'm not sure what the security implications might be.


## **What I hope to do better:**
I think I should learn how to use a more test-driven workflow, so it's easier to spot bugs and keep a clear goal in mind. Also, I know I've been lazy or too focused on getting results so I'm not catching all the exceptions and errors that may arise from running my code. But I will try to fix this.



