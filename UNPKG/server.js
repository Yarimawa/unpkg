const http = require('http')
const fs = require('fs')

const server = http.createServer(function(req, res){
    if (req.url == '/react-native') {
        res.writeHead(200, {'Content-Type': 'text/html'})
        fs.createReadStream(__dirname + '/UNPKG.html', 'utf-8').pipe(res)
    }
    else if (req.url == '/2'){
        res.writeHead(200, {'Content-Type': 'text/html'})
        fs.createReadStream(__dirname + '/UNPKG2.html', 'utf-8').pipe(res)
    }
    else if (req.url == '/file'){
        res.writeHead(200, {'Content-Type': 'text/html'})
        fs.createReadStream(__dirname + '/UNPKG_FILE.html', 'utf-8').pipe(res)
    }
    else if (req.url == '/raw'){
        res.writeHead(200, {'Content-Type': 'text/html'})
        fs.createReadStream(__dirname + '/UNPKG_RAWFILE.html', 'utf-8').pipe(res)
    }
})

server.listen(1234, "127.0.0.1")
console.log("Starting development server at http://127.0.0.1:1234/")
console.log("Quit the server with CTRL-BREAK.")
