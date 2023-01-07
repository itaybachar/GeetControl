async function send(path, data, method = 'GET') {
    data = {
        'op': 'remote',
        'data': data
    };

    const res = await (await fetch(`${path}`, {
        method: method,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: (method === 'POST') ? JSON.stringify(data): undefined
    })).text();

    console.log(res);
}

async function typeKey(key){
    data = {
        'action' : 'keyboard',
        'key': key
    };

    send('/keyboard',data,'POST');
}

async function mouseMove(xVel, yVel) {
    data = {
        'action': 'mouse-move',
        'dx': xVel,
        'dy': yVel
    };

    send('/mouse',data,'POST');
}

async function mouseClick(mouseKey = "left")
{
    data = {
        'action': 'mouse-click',
        'btn': mouseKey
    };

    send('/mouse',data,'POST');
}

async function volumeRocker(change){
    data = {'action': 'volume'};
    switch(change) {
        case "+":
            data['change'] = 'UP';
            break;
        case "-":
            data['change'] = 'DOWN';
            break;
        default:
            return
    }
    send('volume',data,'POST');
}

async function sendQuickAction(action) {
    data = {
        'action': 'quick-action',
        'service': action
    };

    send('/quick-action',data,'POST');
}