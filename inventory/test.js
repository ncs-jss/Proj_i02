const {c, cpp, node, python, java} = require('compile-run')
const sourcecode = `print("Hell0 W0rld!")`
let resultPromise = python.runSource(sourcecode)
resultPromise
  .then(result => {
    console.log(result)
  })
  .catch(err => {
    console.log(err)
  })
