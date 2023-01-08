function init_utility_buttons()
{
    vUp = document.getElementById("v-up");
    vDown = document.getElementById("v-down");
    sUp = document.getElementById("scroll-up");
    sDown = document.getElementById("scroll-down");
    quickActionButtons = document.getElementsByClassName('qa')

    vUp.addEventListener('click', volumeUp)
    vDown.addEventListener('click', volumeDown)
    sUp.addEventListener('click', scrollUp)
    sDown.addEventListener('click', scrollDown)

    for (qa of quickActionButtons)
    {
        qa.addEventListener('click', quickAction)
    }
}

function volumeUp()
{
    volumeRocker("+");
}

function volumeDown()
{
    volumeRocker("-");
}

function quickAction(e)
{
    action = e.target.parentElement.dataset.action;
    sendQuickAction(action);
}

function scrollUp()
{
    scrollWheel("up")
}

function scrollDown()
{
    scrollWheel("down")
}