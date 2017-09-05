var contentController = require('./controllers/contentController.js');

module.exports = function(app){

    app.get('/',contentController.index);

    app.get('*',contentController.other)

}
