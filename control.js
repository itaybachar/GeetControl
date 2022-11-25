const http = require('http');
const WebSocket = require('ws');

const static = require('node-static');
const file = new static.Server('./');

var connection = new WebSocket('ws://localhost:8000');
var info = undefined
connection.onopen = function ()
{
    connection.send('GET_INFO');
    // connection.send('CLOSE');
};
connection.onerror = function (error)
{
    console.log('WebSocket Error ', error);
    alert('WebSocket Error ', error);
};
connection.onmessage = function (e)
{
    info = e.data
    console.log('Server: ', e.data);
}

const server = http.createServer((req, res) =>
{
    if (req.url == "/INFO")
    {
        if (info)
            res.write(info);
        else
            res.write("RETRY")
        res.end();
    }
    console.log(req.url);
    req.addListener('end', () => file.serve(req, res)).resume();

});
const port = 80;
server.listen(port, () => console.log(`Server running at http://localhost:${port}`));