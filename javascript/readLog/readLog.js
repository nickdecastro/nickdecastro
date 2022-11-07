const fs = require('node:fs');
const readline = require('node:readline');

const rl = readline.createInterface({
  input: fs.createReadStream('./javascript/test/testdata.txt'),
  crlfDelay: Infinity
});

function findSeries(sequence) {
    let newSequence = [];
    for (let removeIndex = 0; removeIndex < sequence.length; removeIndex++) {
        newSequence = [...sequence];
        newSequence.splice(removeIndex, 1);
        console.log(`newSequence: `+ newSequence);
        for (let currentIndex = 0; currentIndex < newSequence.length-1; currentIndex++) {
            if (newSequence[currentIndex] >= newSequence[currentIndex+1]) {
                result = false;
                break;
            } else {
                result = true;
            }
        }
        if (result === true) {
            return result;
        }
    }
    return false;
}

rl.on('line', (line) => {
  console.log(`Line from file: ${line}`);
  
  let sequence = JSON.parse(line);
  console.log(`Result: `+ findSeries(sequence));
  console.log(`\n-------------------------New Test Case-----------------------\n`);
});

