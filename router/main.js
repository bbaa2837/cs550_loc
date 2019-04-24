const testFolder = './public/images/champion_images/';
const fs = require('fs');
var i = 0;
var files = new Array();
fs.readdirSync(testFolder).forEach(file => {
  files[i] = file;
  i = i + 1;
});
module.exports = function(app)
{
    app.get('/',function(req,res){
        res.render('index.html', {});
    });
    app.get('/about',function(req,res){
       res.render('about.html');
    });
    app.get('/call',function(req,res){
        res.render('call.html');
    });
    app.get('/champ_list',function(req,res){
        res.json({files: files});
    });
}