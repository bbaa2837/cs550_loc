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
    app.get('/predict-score/:champ1.:champ2.:champ3.:champ4.:champ5.:champ6.:champ7.:champ8.:champ9.:champ10', function(req, res) {
      var champ1 = req.params.champ1;
      var champ2 = req.params.champ4;
      var champ3 = req.params.champ5;
      var champ4 = req.params.champ8;
      var champ5 = req.params.champ9;
      var champ6 = req.params.champ2;
      var champ7 = req.params.champ3;
      var champ8 = req.params.champ6;
      var champ9 = req.params.champ7;
      var champ10 = req.params.champ10;

      console.log(champ1+champ2+champ3+champ4+champ5);
      console.log(champ6+champ7+champ8+champ9+champ10);

      var spawn = require('child_process').spawn;
      var subprocess = spawn('python3', [
                                './router/predict-score.py',
                                champ1, champ2, champ3,
                                champ4, champ5, champ6,
                                champ7, champ8, champ9, 
                                champ10]);

      subprocess.stdout.on('data', function(data) {
        console.log('data:' + data);
        res.send(data.toString());
      });

      subprocess.stderr.on('data', function(data) {
        console.log('error:' + data);
      });

      subprocess.stderr.on('close', function(data) {
        console.log('Closed');
      });
    });
}