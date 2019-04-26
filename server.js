// const http = require('http');
// const url = require('url');
// const fs = require('fs');

//For Riot API Call
const request = require('request');
const rp = require('request-promise');

const key = '?api_key=RGAPI-2df11584-d47d-455f-bcd1-94ff695c6ec2';
const kor_url = 'https://kr.api.riotgames.com';
const summoner = '/lol/summoner/v4/summoners/by-name/';
const matchbyaccountid = '/lol/match/v4/matchlists/by-account/';
const matchbymatchid = '/lol/match/v4/matches/';
var name = encodeURIComponent("레피토스");

var accountid = "";
rp(kor_url+summoner+name+key).then(function (html) {
    console.log("From KOR Server kor name")
    console.log("==============================")
    var raw = html.replace('{','').replace('}','').split(",");
    var item = [];
    var value = [];
    for (var i = 0; i < raw.length; i++){
        console.log(raw[i]);
        raw[i] = raw[i].replace(/"/g, '');
        item[i] = raw[i].split(':')[0];
        value[i] = raw[i].split(':')[1];
    }
    console.log(item);
    console.log(value);
    accountid = value[1];
    console.log("==============================");
    return rp(kor_url+matchbyaccountid+accountid+key);
  }).then(function(html) {
    console.log("match info");
    console.log("==============================");
    var gameid = [], gameidx = [], result, kw = /gameId/g;
    while ((result = kw.exec(html))){
      gameidx.push(result.index);
    }
    for (var i = 0; i < gameidx.length; i++){
      gameid[i] = html.substring(gameidx[i] + 8,gameidx[i] + 18);
    }
    // console.log(gameid);
    console.log("==============================");
    return rp(kor_url+matchbymatchid+gameid[0]+key);
  }).then(function(html) {
    console.log("matches");;
    console.log("================================");
    console.log(html);
  })

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