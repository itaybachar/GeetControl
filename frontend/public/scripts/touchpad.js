function init_touchpad() {
  touchpad = document.getElementById("touchpad");
  set_handlers("touchpad");
}

// Touch Point cache
var tpCache = new Array();

function start_handler(ev) {
  for (var i = 0; i < ev.targetTouches.length; i++) {
    tpCache.push(ev.targetTouches[i]);
  }
}

function move_handler(ev) {
  ev.preventDefault();

  if (ev.touches.length == 1) {
    var diffX = ev.targetTouches[0].clientX - tpCache[0].clientX;
    var diffY = ev.targetTouches[0].clientY - tpCache[0].clientY;

    mouseMove(diffX, diffY)
  }
}

function end_handler(ev) {
  if (ev.targetTouches.length == 0) {
    tpCache = [];
  }
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
    mouseClick('left')
  })
}