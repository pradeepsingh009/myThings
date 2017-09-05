var express = require('express');

var app = express();
app.set('view engine','ejs');
app.use('/static',express.static('public'));

require('./route.js')(app);



app.listen(3000);
console.log('listening at port 3000');
