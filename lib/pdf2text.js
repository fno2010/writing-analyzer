var extractor = require('pdf-text-extract');
var path = require('path');

var absolute_path_to_pdf = path.join(__dirname, process.argv[2]);

console.log('Extract text from pdf:', absolute_path_to_pdf);

//var options = {
  //type: 'text'
//};

//var processor = extractor(absolute_path_to_pdf, options, function(err) {
  //if (err) {
    //throw err;
  //}
//});

//processor.on('complete', function(data) {
  //console.log(data.text_pages);
//})

//processor.on('error', function(err) {
  //console.error(err);
//});

extractor(absolute_path_to_pdf, function (err, pages) {
  if (err) {
    console.dir(err);
    return;
  }
  
  console.dir(pages);
})
