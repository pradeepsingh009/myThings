var contentController = require('./controllers/contentController.js');

module.exports = function(app){

    app.get('/',contentController.list);

    app.get('/list',contentController.list);

    app.get('/list/:name',contentController.list);

    app.post('/',contentController.add);

    app.put('/',contentController.update);

    // app.get('*',contentController.other)

}
