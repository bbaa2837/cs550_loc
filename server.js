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
var name = encodeURIComponent("프제짱");

var accountid = "";
// rp(kor_url+summoner+name+key).then(function (html) {
//     console.log("From KOR Server kor name")
//     console.log("==============================")
//     var raw = html.replace('{','').replace('}','').split(",");
//     var item = [];
//     var value = [];
//     for (var i = 0; i < raw.length; i++){
//         console.log(raw[i]);
//         raw[i] = raw[i].replace(/"/g, '');
//         item[i] = raw[i].split(':')[0];
//         value[i] = raw[i].split(':')[1];
//     }
//     console.log(item);
//     console.log(value);
//     accountid = value[1];
//     console.log("==============================");
//     return rp(kor_url+matchbyaccountid+accountid+key);
//   }).then(function(html) {
//     console.log("match info");
//     console.log("==============================");
//     console.log(accountid);
//     console.log(html);
//     console.log("==============================");
//   })

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

// http.createServer((request, response) => {
//   const path = url.parse(request.url, true).pathname;
//   if (request.method === 'GET') {
//     if (path === '/about') {
//       response.writeHead(200,{'Content-Type':'text/html'});
//       fs.readFile(__dirname + '/views/about.html', (err, data) => {
//         if (err) {
//           return console.error(err);
//         }
//         response.end(data, 'utf-8');
//       });
//     } else if (path === '/') {
//       response.writeHead(200,{'Content-Type':'text/html'});
//       fs.readFile(__dirname + '/views/index.html', (err, data) => {
//         if (err) {
//           return console.error(err);
//         }
//         response.end(data, 'utf-8');
//       });
//     } else {
//       response.statusCode = 404;
//       response.end('주소가 없습니다');
//     }
//   }
// }).listen(3000);