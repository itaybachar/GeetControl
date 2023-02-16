function init_touchpad()
{
  touchpad = document.getElementById("touchpad");
  set_handlers("touchpad");
}

// Touch Point cache
var tpCache = new Array();
var rightClick = false;
function start_handler(ev)
{
  for (var i = 0; i < ev.targetTouches.length; i++)
  {
    tpCache.push(ev.targetTouches[i]);
  }
  if (ev.targetTouches.length > 0)
  {
    prevX = ev.targetTouches[0].clientX
    prevY = ev.targetTouches[0].clientY
  }

  if (ev.targetTouches.length > 1)
  {
    rightClick = true;
  }
}
let prevX = undefined, prevY = undefined;

function move_handler(ev)
{
  ev.preventDefault();

  if (ev.touches.length == 1)
  {
    var diffX = ev.targetTouches[0].clientX - prevX;
    var diffY = ev.targetTouches[0].clientY - prevY;
    var magnitude = Math.sqrt(diffX * diffX + diffY * diffY)

    if (diffX == 0 && diffY == 0 || magnitude == 0)
      return
    oom = 1 / magnitude //1 over magnitude

    var force = magnitude;

    mouseMove(diffX * oom, diffY * oom, force)

    prevX = ev.targetTouches[0].clientX;
    prevY = ev.targetTouches[0].clientY;
  }
}

function end_handler(ev)
{
  if (ev.targetTouches.length == 0)
  {
    tpCache = [];
    prevX = undefined;
    prevY = undefined;

    if (rightClick)
    {
      mouseClick('right')
      setTimeout(() =>
      {
        rightClick = false;
      }, 500);
    }
    else
      mouseClick('left');
  }
}

function set_handlers(name)
{
  // Install event handlers for the given element
  var el = document.getElementById(name);
  el.ontouchstart = start_handler;
  el.ontouchmove = move_handler;

  // Use same handler for touchcancel and touchend
  el.ontouchcancel = end_handler;
  el.ontouchend = end_handler;
}