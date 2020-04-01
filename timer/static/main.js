//When timer obj is on and user clicks start button, start that timer.
function Timer (name, length) {
	this.name = name;
	this.length = length;
}

// Define timer objects
var pomodoro = new Timer("pomodoro", .25);
pomodoro.count = 0;
var shortBreak = new Timer ("short", 5);
var longBreak = new Timer ("long", 20);

// Highlight function from https://stackoverflow.com/a/8644513
function highlight(text) {
	var searchText = document.getElementById("searchText");
	var innerHTML = searchText.innerHTML;
	var index = innerHTML.indexOf(text);
	if (index >= 0) {
		innerHTML = innerHTML.substring(0, index) + "<span class='highlight'>" + innerHTML.substring(index, index + text.length) + "</span>" + innerHTML.substring(index + text.length);
		searchText.innerHTML = innerHTML;
	}
};


var myClock = setInterval(myTimer, 1000);
function myTimer() {
	var time = new Date();
	document.getElementById("clock").innerHTML = time.toLocaleTimeString();
}

var choice;
document.getElementById('choices').onclick = function() {
	
	if (document.getElementById('r1').checked) {
		choice = document.getElementById('r1').value;
	} else if (document.getElementById('r2').checked) {
		choice = document.getElementById('r2').value;
	} else if (document.getElementById('r3').checked) {
		choice = document.getElementById('r3').value;
	}
}


document.getElementById("reset").onclick = function() {
	clearInterval(stopwatch);
	var display = document.querySelector('#bigben');
	if (choice === "pomodoro") {
		startTimer(pomodoro, display);
	} else if (choice === "short"){
		startTimer(shortBreak, display);
	} else if (choice === "long"){
		startTimer(longBreak, display);
	} else {
		return;
	}
}

function stopTimer() {
	clearInterval(stopwatch);
}


function zeroTimer(timerName) {
	clearInterval(stopwatch);
	window.alert("Session ended!")
	document.getElementById("tally").innerHTML = pomodoro.count;
	if (timerName === "pomodoro") {
		alert("Great job working on: " + task);
		window.open("http://127.0.0.1:8000/timer/pomodoro/create/");
		window.open("https://www.youtube.com/watch?v=DiGUnl7kEOw&feature=youtu.be");
	}
};

// startTimer function from https://stackoverflow.com/a/20618517
function startTimer(obj, display) {
	var timer = obj.length * 60, minutes, seconds;
	
	stopwatch = setInterval(function() {
		minutes = parseInt(timer / 60, 10);
		seconds = parseInt(timer % 60, 10);
		
		minutes = minutes < 10 ? "0" + minutes : minutes;
		seconds = seconds < 10 ? "0" + seconds : seconds;
		
		display.textContent = minutes + ":" + seconds;
		timer = timer - 1;
		if (0 > timer) {
			timer = obj.length;			
			if (obj.name === "pomodoro") {
				pomodoro.count = pomodoro.count + 1;
			}
			zeroTimer(obj.name);
		}
		
	}, 1000)

};

var task;
document.getElementById("start").onclick = function() {
	var display = document.querySelector('#bigben');
	if (choice === "pomodoro") {
		task = prompt("Describe what you'll be working on: ");
		startTimer(pomodoro, display);
	} else if (choice === "short"){
		startTimer(shortBreak, display);
	} else if (choice === "long"){
		startTimer(longBreak, display);
	} else {
		return;
	}
}

document.getElementById("stop").onclick = function() {
	stopTimer();
}

function toggle(obj) {
	if (obj.status === "off") {
		obj.status = "on";
	} else {
		obj.status = "off";
	}
}

/*
window.onload = function() {
	document.getElementById('helpForm').onsubmit = function() {
	
	alert('Thanks for submitting your feedback!');
	// return false to prevent form default behavior
	return false;
	}
}
*/
// processForm function from https://stackoverflow.com/a/5384732
function processForm(e) {
	if (e.preventDefault) e.preventDefault();
	alert('Thanks for submitting your feedback!');
	

	// return false to stop form default behavior
	return false
}

var form = document.getElementById('helpForm');
if (form.attachEvent) {
	form.attachEvent("submit", processForm);
} else {
	form.addEventListener("submit", processForm);
}