#!/usr/bin/node
const argLength = parseInt(process.argv.length);
if (argLength <= 3) {
  console.log('0');
} else {
  let biggest = parseInt(process.argv[2]);
  for (let i = 2; i < argLength; i++) {
    if (biggest < parseInt(process.argv[i])) {
      biggest = parseInt(process.argv[i]);
    }
  }
  let secondBiggest = -Infinity;
  for (let i = 2; i < argLength; i++) {
    if (secondBiggest < parseInt(process.argv[i]) &&
    parseInt(process.argv[i]) < biggest) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
