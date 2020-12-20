const rp = require('request-promise');
const url = 'https://www.blognone.com/';

rp(url)
  .then(function(html){
    //success!
    console.log(html);
  })
  .catch(function(err){
    //handle error
  });