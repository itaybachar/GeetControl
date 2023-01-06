let touchpad = undefined;
let keypad = undefined;

function boot() {
  touchpad = document.getElementById("touchpad");
  keypad = document.getElementById("keypad");

  //Init keypad
  keypad.addEventListener("keydown", keyTyped);

  //Init touchpad
  init();
}

// Log events flag
var logEvents = true;

// Touch Point cache
var tpCache = new Array();

function enableLog(ev) {
  logEvents = !logEvents;
}

function log(str, append = false) {
  // var o = document.getElementsByTagName('output')[0];

  // if (append)
  //   o.innerHTML += str;
  // else
  //   o.innerHTML = str;
}

function clearLog(event) {
  // var o = document.getElementsByTagName('output')[0];
  // o.innerHTML = "";
}


function start_handler(ev) {
  //  ev.preventDefault();
  //  if (ev.targetTouches.length == 2) {
  for (var i = 0; i < ev.targetTouches.length; i++) {
    tpCache.push(ev.targetTouches[i]);
  }

}

function move_handler(ev) {
  ev.preventDefault();

  if (ev.touches.length == 1) {
    var diffX = ev.targetTouches[0].clientX - tpCache[0].clientX;
    var diffY = ev.targetTouches[0].clientY - tpCache[0].clientY;

    // log(diffX + "," + diffY)
    send("",
      {
        "MOUSEMOVE": {
          "x": diffX,
          "y": diffY
        }
      }, 'POST')
  }
}

function end_handler(ev) {
  //   ev.preventDefault();
  if (ev.targetTouches.length == 0) {
    tpCache = [];
  }
  clearLog()
}

function set_handlers(name) {
  // Install event handlers for the given element
  var el = document.getElementById(name);
  el.ontouchstart = start_handler;
  el.ontouchmove = move_handler;
  // Use same handler for touchcancel and touchend
  el.ontouchcancel = end_handler;
  el.ontouchend = end_handler;
  el.onclick = ((ev) => {
    // ev.preventDefault();
    // log("clicked")
    send("", { "MOUSE": "click" }, 'POST')
  })
}

function init() {
  set_handlers("touchpad");

}

function keyTyped(e) {
  e.preventDefault();
  console.log(e)
  log(e.key, true)
  return false;
}

window.onload = boot;