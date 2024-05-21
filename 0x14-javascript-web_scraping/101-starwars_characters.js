#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const charUrl = data.characters;
  /* Ai used here */
  const promises = charUrl.map((charUrl, index) => {
    return new Promise((resolve) => {
      request.get(charUrl, (err, res, body) => {
        if (err) {
          console.log(err);
          return;
        }
        resolve({ index, actor: JSON.parse(body).name });
      });
    });
  });
  Promise.all(promises)
    .then(data => {
      data.sort((a, b) => a.index - b.index);
      data.forEach(item => {
        console.log(item.actor);
      });
    });
});
