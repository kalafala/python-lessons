// credit:  https://github.com/tonypujals/express-demo/blob/master/lesson-03-B/app.js
// credit https://github.com/tonypujals/express-demo/tree/master/lesson-03-A
// credit https://github.com/tonypujals/express-demo/blob/master/lesson-03-C/app.js
// credit https://github.com/tonypujals/express-demo/blob/master/lesson-04/app.js
// credit https://github.com/tonypujals/express-demo/blob/master/lesson-06/app.js


var express = require('express'),
	app = express(),
	pythonShell = require('python-shell'),
	port = process.env.PORT || 3003;


// Simple route handler example
app.get('/python',function(req,res,next) {
var data = '<h1>Python is active !</h1>';
res.writeHead(200, {'Content-Type': 'text/html'});
console.log('Python started');
pythonShell.run('sleeping.py', function(err) {
	if (err) throw err;
	console.log('Python finished');
	res.end(data);
})
});

app.get('/',function(req,res,next) {
var data = '<h1>Homepage</h1>';
res.writeHead(200, {'Content-Type': 'text/html'});
res.end(data);
});

app.listen(port);

console.log('server started on port %s', port);
