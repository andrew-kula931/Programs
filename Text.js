// Import the http module
const http = require('http');
let strObject = 'Test string';
// Create a server
const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write('Hello World!');
    res.write(`Here is real text    and here is ${strObject}`)
    res.end();
});

// Server listens on port 3000
server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
