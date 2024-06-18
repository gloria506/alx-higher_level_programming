#!/usr/bin/node

const length = process.argv.legnth - 2;

if (length === 0) {
    console.log('No argument');
} else if (length === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
