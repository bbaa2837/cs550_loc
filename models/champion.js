const mongoose = require('mongoose');

mongoose.connect("mongodb://test:testtest1@ds155626.mlab.com:55626/loc");

const championSchema = new mongoose.Schema({
    name : String,
    id : Number,
    champion_img : String,
    mastery_img : String,
    item_img : String
  }, {collection : 'info'})
  
var Champion = mongoose.model('Champion', championSchema, 'info');

module.exports = Champion;
  