module.exports.index = function(req,res){

    var mongoose = require('mongoose');
    mongoose.connect('mongodb://localhost/sample');

    var db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', function() {
  console.log('db connected');
});
    res.render('content/index.ejs',{page_name : 'Index'});
}

module.exports.other = function(req,res){
    res.render('content/other.ejs',{page_name : 'Other'});
}
