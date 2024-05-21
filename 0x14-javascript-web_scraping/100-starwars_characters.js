#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  for (const char in data.characters) {
    request.get(data.characters[char], (err, res, body) => {
      if (err) {
        console.log(err);
        return;
      }
      const actor = JSON.parse(body).name;
      console.log(actor);
    });
  }
});
