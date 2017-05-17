const electron = require('electron');
const view = require('./view');

const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const Menu = electron.Menu;

const path = require('path');
const url = require('url');

let mainWindow;

let template = [{
  label: 'File',
  role: 'file',
  submenu: [{
    label: 'New Document',
    accelerator: 'CmdOrCtrl+N',
    click: function (item, focusedWindow) {
      if (focusedWindow) {
        console.log('New Document!');
      }
    }
  }, {
    type: 'separator'
  }, {
    label: 'Import',
    click: function () {
      console.log('Import!');
    }
  }, {
    label: 'Export',
    click: function () {
      console.log('Export!');
    }
  }]
}, {
  label: 'Help',
  role: 'help',
  submenu: [{
    label: 'Learn More',
    click: function () {
      electron.shell.openExternal('https://github.com/fno2010/writing-analyzer#readme');
    }
  }]
}];

let mainView = view();

require('module').globalPaths.push(__dirname + '/renderer');

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    minWidth: 500,
    minHeight: 400,
    acceptFirstMouse: true
    // titleBarStyle: 'hidden'
  });

  // and load the view of the app.
  mainWindow.loadURL(url.format({
    protocol: 'http:',
    hostname: 'localhost',
    port: 25001,
    pathname: path.join('/', 'index.html'),
    slashes: true
  }));

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Clear objects
    mainWindow = null;
  });
}

function findReopenMenuItem () {
  const menu = Menu.getApplicationMenu();
  if (!menu) return;

  let reopenMenuItem;
  menu.items.forEach(function (item) {
    if (item.submenu) {
      item.submenu.items.forEach(function (item) {
        if (item.key === 'reopenMenuItem') {
          reopenMenuItem = item;
        }
      });
    }
  });

  return reopenMenuItem;
}

if (process.platform === 'darwin') {
  const name = electron.app.getName();
  template.unshift({
    label: name,
    submenu: [{
      label: `About ${name}`,
      role: 'about'
    }, {
      type: 'separator'
    }, {
      label: 'Services',
      role: 'services'
    }, {
      type: 'separator'
    }, {
      label: `Hide ${name}`,
      accelerator: 'Command+H',
      role: 'hide'
    }, {
      label: 'Hide Others',
      accelerator: 'Command+Alt+H',
      role: 'hideothers'
    }, {
      label: 'Show All',
      role: 'unhide'
    }, {
      type: 'separator'
    }, {
      label: 'Quit',
      accelerator: 'Command+Q',
      click: function () {
        app.quit();
      }
    }]
  });
}

app.on('ready', function () {
  const menu = Menu.buildFromTemplate(template);
  Menu.setApplicationMenu(menu);
  createWindow();
  console.log(template);
});

app.on('browser-window-created', function () {
  let reopenMenuItem = findReopenMenuItem();
  if (reopenMenuItem) reopenMenuItem.enabled = false;
});

app.on('window-all-closed', function () {
  let reopenMenuItem = findReopenMenuItem();
  if (reopenMenuItem) reopenMenuItem.enabled = true;
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    mainView.close();
    app.quit();
  }
});

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow();
  }
});
