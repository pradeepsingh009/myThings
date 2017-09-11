var studentModel = require('../models/db/student.js');

module.exports.list = function(req,res){

var name = req.params.name;
if(name){
  studentModel.find({StudentName : name},function(err,student){
    res.send(student);
  });
}else{
  studentModel.find({},function(err,students){
    res.send(students);
  });
}

// var newStudent = new studentModel({
//   StudentName : "Pradeep Singh",
//   Section : "X",
//   Marks : 100,
//   Subject : ["Node","PHP","Java"]
// });
//
// newStudent.save(function(err) {
//   if (err) throw err;
//
//   console.log('Student saved successfully!');
// });

//     var db = mongoose.connection;
// db.on('error', console.error.bind(console, 'connection error:'));
// db.once('open', function() {
//   console.log('db connected');
// });
    // res.render('content/index.ejs',{page_name : 'Index'});
}

module.exports.other = function(req,res){
  // get all the users
  var findStudentName = req.params.studentName;
  console.log(findStudentName);
studentModel.find({ StudentName : findStudentName }, function(err, students) {
  if (err) throw err;
  res.send(students);
});

    // res.render('content/other.ejs',{page_name : 'Other'});
}

module.exports.add = function(req,res){
  var studentName = req.body.StudentName;
  var section = req.body.Section;
  var marks = req.body.Marks;
  var subjects = req.body.Subject;

  var newStudent = new studentModel({
    StudentName : studentName,
    Section : section,
    Marks : marks,
    Subject : subjects
  });

  newStudent.save(function(err){
    if(err) throw err;
    console.log('New student added');
    res.send(true);
  });
}

// function to update
module.exports.update = function(req,res){
  
  var studentName = req.body.StudentName;
  condition = {StudentName : studentName};
  setter = {
    Section : req.body.Section,
    Marks : req.body.Marks,
    Subject : req.body.Subject
  }
  studentModel.findOneAndUpdate(condition,setter,function(err,student){
    if(err){
      throw err;
      res.send(false);
    }else{
        res.send(student);
        console.log("Student "+studentName+" updated successfully");
    }


  });
}
