function init_keypad() {
    keypad = document.getElementById("keypad");

    //Init keypad
    keypad.addEventListener("keydown", keyTyped);
}

function keyTyped(e) {
    e.preventDefault();
    console.log(e)

    //Take key code and send it
    typeKey(e.key)
    return false;
}