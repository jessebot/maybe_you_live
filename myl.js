// Hacked together poorly by DomoJesse aka Jessebot
var express = require("express");
var fs = require('fs');
//var https = require('https');
var http = require('http');
//var options = {
//  key: fs.readFileSync('/etc/letsencrypt/live/jessebot.io/privkey.pem'),
//  cert: fs.readFileSync('/etc/letsencrypt/live/jessebot.io/cert.pem')
//  };
var app = express();
var router = express.Router();
var path = __dirname + '/views/';
var ejs = require('ejs');

router.use(function (req,res,next) {
  console.log("/" + req.method);
  next();
});

router.get("/",function(req,res){

  // set templating engine
  app.engine('html', require('ejs').renderFile);
  app.set('view engine', 'html');
  app.set('views','./views');

  // display index.html
  res.render('index');
  // res.render('index', { json: json});
});

app.use("/",router);

app.use('/js', express.static(__dirname + '/node_modules/bootstrap/dist/js')); // redirect bootstrap JS

app.use('/js', express.static(__dirname + '/node_modules/jquery/dist')); // redirect JS jQuery

app.use('/js', express.static(__dirname + '/js')); // dfdsafdredirect JS jQuery

app.use('/css', express.static(__dirname + '/node_modules/bootstrap/dist/css')); // redirect CSS bootstrap

app.use('/css', express.static(__dirname + '/css')); // redirect CSS dafsfads

app.use('/fonts', express.static(__dirname + '/fonts')); // redirect images

app.use('/images', express.static(__dirname + '/images')); // redirect images

app.use("*",function(req,res){
  res.sendFile(path + "404.html");
});

http.createServer(app).listen(8083, function () {
  console.log('Maybeyou.live Started!');
});

/*
https.createServer(options, app).listen(8081, function () {
  console.log('Secure Maybeyou.live Started!');
});

app.listen(8081, function(){
  console.log("Live at Port 8081");
});
*/
