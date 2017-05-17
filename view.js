var express = require('express');
var bodyParser = require('body-parser');
var http = require('http');

var app = express();
var server = http.createServer(app);

module.exports = function (port) {
  app.use(express.static(__dirname + '/view'));
  app.use(bodyParser.urlencoded({ extended: true }));
  app.use(bodyParser.json());

  server.port = port || 25001;
  server.listen(server.port, function () {
    console.log('Start http server on http://localhost:' + server.port + ' for view');
  });

  return server;
};
