//For Riot API Call
// const request = require('request');
// const rp = require('request-promise');

const key = '?api_key=RGAPI-2df11584-d47d-455f-bcd1-94ff695c6ec2';
const kor_url = 'https://kr.api.riotgames.com';
const summoner = '/lol/summoner/v4/summoners/by-name/';
const matchbyaccountid = '/lol/match/v4/matchlists/by-account/';
// var name = encodeURIComponent("프제짱");
var name = "hide on bush";

var accountid = "";

// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
// request.open('GET', kor_url+summoner+name+key, true)

const proxyurl = "http://localhost:4000/";
const url = kor_url+summoner+name+key; 
fetch(proxyurl + url)
.then(response => console.log(response))
.then(response => response.text())
.then(contents => console.log(contents))
.catch(() => console.log("Can’t access " + url + " response. Blocked by browser?"))

// request.onload = function () {
//     // Begin accessing JSON data here
//     var data = JSON.parse(this.response);
//     console.log(data);
// }

// Send request
// request.send()

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
//     }).then(function(html) {
//     console.log("match info");
//     console.log("==============================");
//     console.log(accountid);
//     console.log(html);
//     console.log("==============================");
//     })