#!/usr/bin/node
const request = require('request');
const urlId = 'https://swapi-api.alx-tools.com/api/people/18/';
const film = process.argv[2];
request.get(film, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const movies = data.results.filter(
    movie => movie.characters.includes(urlId));
  console.log(movies.length);
});
