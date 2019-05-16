//For Riot API Call
const request = require('request');
const rp = require('request-promise');
const fs = require('fs');
// const ejs = require('ejs');

const key = 'api_key=RGAPI-2df11584-d47d-455f-bcd1-94ff695c6ec2';
const kor_url = 'https://kr.api.riotgames.com';
const summoner = '/lol/summoner/v4/summoners/by-name/';
const matchbyaccountid = '/lol/match/v4/matchlists/by-account/';
const matchbymatchid = '/lol/match/v4/matches/';
var name = encodeURIComponent("레피토스");
var gameid = [], accountids = [];
var usedmatchid = [];
var iter = 0;
var ran = 0;
var matchinfo = "";
var numofiterations = 9999;
var testfile = "test2.csv"

// fs.writeFile(testfile, "Match Id, Game Duration, Win Team, Champion Id\n", function(err) {
//   if(err) {
//     return console.log(err);
//   }
//   console.log("The file was saved!");
// }); 
// fs.writeFile("summonernames.csv", "", function(err) {
//   if(err) {
//     return console.log(err);
//   }
//   console.log("The file was saved!");
// }); 
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function myFunc(accountid){
  // rp(kor_url+summoner+name+key).then(function (html) {
  //   console.log("From KOR Server kor name")
  //   console.log("==============================")
  //   var raw = html.replace('{','').replace('}','').split(",");
  //   var item = [];
  //   var value = [];
  //   for (var i = 0; i < raw.length; i++){
  //       console.log(raw[i]);
  //       raw[i] = raw[i].replace(/"/g, '');
  //       item[i] = raw[i].split(':')[0];
  //       value[i] = raw[i].split(':')[1];
  //   }
  //   console.log(item);
  //   console.log(value);
  //   accountid = value[1];
  //   console.log("==============================");
  //   return rp(kor_url+matchbyaccountid+accountid+key);
  // }).then(function(html) {
  rp(kor_url+matchbyaccountid+accountid+'?queue=420&'+key).then(function (html) {
    // console.log("match info");
    // console.log("==============================");
    var gameidx = [], result, kw = /gameId/g;
    while ((result = kw.exec(html))){
      gameidx.push(result.index);
    }
    for (var i = 0; i < gameidx.length; i++){
      gameid[i] = html.substring(gameidx[i] + 8,gameidx[i] + 18);
    }
    // console.log(gameid);
    // console.log("==============================");
    while(usedmatchid.includes(gameid[ran])){
      ran = Math.floor(Math.random() * gameidx.length);
    }
    usedmatchid[usedmatchid.length] = gameid[ran];
    // console.log(usedmatchid);
    // fs.appendFile('test.csv', gameid[ran] + ',', function (err) {
    //   if (err) throw err;
    //   console.log('Saved!');
    // });
    return rp(kor_url+matchbymatchid+gameid[ran]+'?'+key);
  }).then(async function(html) {
    // console.log("matches");;
    // console.log("================================");
    // html = html.replace(/",/gi,'\n');
    // console.log(html);
    var accountidx = [], accountidx2 = [], result;
    var kw = /accountId/g, kw2 = /summonerName/g;
    while ((result = kw.exec(html))){
      accountidx.push(result.index);
    }
    while ((result = kw2.exec(html))){
      accountidx2.push(result.index);
    }
    // while ((result = kw3.exec(html))){
    //   durationidx.push(result.index);
    // }
    // while ((result = kw4.exec(html))){
    //   championidx.push(result.index);
    // }
    // while ((result = kw4.exec(html))){
    //   championidx.push(result.index);
    // }
    for (var i = 0; i < accountidx.length; i++){
      accountids[i] = html.substring(accountidx[i] + 12,accountidx2[i] - 3);
    }
    aaaaa = JSON.parse(html);
    // console.log(aaaaa.gameDuration);
    // fs.appendFile('test.csv', aaaaa.gameDuration.toString() + ',', function (err) {
    //   if (err) throw err;
    //   console.log('Saved2!');
    // });
    matchinfo = gameid[ran] + ',' + aaaaa.gameDuration.toString() + ',' + aaaaa.teams[0].win + ',';
    var summonerdata = "";

    for(var i = 0; i < 10; i++){
      // console.log(aaaaa.participants[i].championId))
      summonerdata = summonerdata + aaaaa.participantIdentities[i].player.summonerName + ',' + aaaaa.participants[i].championId.toString() + '\n';
      // console.log(aaaaa.participantIdentities[i].player.summonerName);
      // console.log(summonerdata);
      matchinfo = matchinfo + aaaaa.participants[i].championId.toString() + ','
    }

    fs.appendFile('summonernames.csv', summonerdata, function (err) {
      if (err) throw err;
    });

    fs.appendFile(testfile, matchinfo + '\n', function (err) {
      if (err) throw err;
    });

    // console.log(accountids);
    // console.log(html.substring(durationidx[0] + 14, ))
    accountid = accountids[0];
    // var fso, f, r;
    // var ForReading = 1, ForWriting = 2;
    // fso = new ActiveXObject("Scripting.FileSystemObject");
    // f = fso.OpenTextFile("test.csv", ForWriting, true);
    // f.Write("aaaafsg");
    // f.Close();

    if(iter < numofiterations){
      iter = iter + 1;
      await sleep(2000);
      myFunc(accountid);
    }

    // return rp(kor_url+matchbyaccountid+accountid+key);
  });
}
// myFunc("DtnkSr7b3YmW5qm6A4Q1nviR9GBEy7YyfDiAYrfzsOBf");




//For nodejs-html
const express = require('express');
const app = express();
const router = require('./router/main')(app);

app.use(express.static('public'));
app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);
var server = app.listen(3000, function(){
  console.log("Express server has started on port 3000")
});

//For DB

const mongoose = require('mongoose');

var db = mongoose.connection;
db.once("open", function(){
  console.log("DB connected!");
})

db.on("error", function(err){
  console.log("DB ERROR:", err);
})


const Champion = require('./models/champion')

console.log(Champion)

app.get('/info', function(req, res){

  console.log("get INFO");
  // res.send("hello")
  
  Champion.find({name : 'Annie'})
    .then((champ) => {
      if(!champ.length) return res.status(404).send({err : 'Champion not found'});
      res.send(`find successfully : ${champ}`);
    })
    .catch(err => res.status(500).send(err))
});


// //my sql try
// const mysql = require('mysql')
// const dbconfig = require('./config/database.js');
// const connection = mysql.createConnection(dbconfig);



