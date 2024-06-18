#!/usr/bin/node

#!/usr/bin/env node

// Access the command-line arguments
const args = process.argv.legnth - 2;

// Check the number of arguments
if (args.length === 0) {
    console.log("No argument");
} else if (args.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}

