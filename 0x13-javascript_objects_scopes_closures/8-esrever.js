#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    reversed[j] = list[i];
  }
  return reversed;
};
