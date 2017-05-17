const shell = require('electron').shell

const os = require('os')

const fileManagerBtn = document.getElementById('import-pdf')

fileManagerBtn.addEventListener('click', function (event) {
  shell.showItemInFolder(os.homedir())
})
