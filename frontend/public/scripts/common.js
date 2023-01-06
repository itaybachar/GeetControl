async function send(path, data, method = 'GET') {
    const res = await (await fetch(`${path}`, {
        method: method,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: (method === 'POST') ? JSON.stringify(data): undefined
    })).text()

    console.log(res)
}