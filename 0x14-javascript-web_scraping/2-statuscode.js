#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log('code:', data.statusCode);
});
