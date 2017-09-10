
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/pradeep');

var schema = mongoose.Schema;

var studentSchema = new schema({
  StudentName : {type : String,required : true,unique : true},
  Section : {type : String},
  Marks : {type : Number},
  Subject : {type : Array}
});

var studentModel = mongoose.model('Student',studentSchema,'Student');

module.exports = studentModel;
