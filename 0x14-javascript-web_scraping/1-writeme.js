#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filePath, string, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
