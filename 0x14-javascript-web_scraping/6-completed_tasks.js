#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const done = data.filter(task => task.completed);
  const group = done.reduce((char, task) => {
    char[task.userId] = (char[task.userId] || 0) + 1;
    return char;
  }, {});
  console.log(group);
});
