#!/usr/bin/node

const express = require('express')
const os = require("os");
const { spawn } = require('child_process');
const app = express()
const port = 3000
var cors = require('cors')

app.get('/', (req, res) => res.send('Test \n'))

var corsOptions = {
  origin: '*',
  optionsSuccessStatus: 200
}

app.listen(port, () => console.log(os.hostname + ' listener starting on ' + port))