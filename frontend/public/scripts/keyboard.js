function init_keypad() {
    keypad = document.getElementById("keypad");

    //Init keypad
    keypad.addEventListener("keydown", keyTyped);
}

function keyTyped(e) {
    e.preventDefault();
    //Take key code and send it
    typeKey(e.key)
    return false;
}