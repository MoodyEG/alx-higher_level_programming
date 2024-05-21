#!/usr/bin/node
const request = require('request');
/* const urlId = 'https://swapi-api.alx-tools.com/api/people/18/'; */
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const data = JSON.parse(body).results;
  for (const films in data) {
    const chars = data[films].characters;
    for (const char in chars) {
      if (chars[char].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
