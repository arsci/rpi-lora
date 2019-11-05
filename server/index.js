#!/usr/bin/node

const express = require('express')
const os = require("os");
const { spawn } = require('child_process');
const app = express()
const port = 3000
var cors = require('cors')

app.get('/', (req, res) => {

    try {
        resp = child.kill()
        console.log(resp)
        console.log('killed process')
    }
    catch {
        console.log("none");
    }
    child = spawn('python3', ['scripts/send-single-packet-lora2.py', '{test-api}'], [], function(err, stdout, stderr) { 
        if(err) { console.log(err) }
        if(stderr) { console.log(err) }
        console.log(stdout); 
    });   

    child.stdout.on('data',function(chunk){

        var textChunk = chunk.toString('utf8');// buffer to string

        console.log(textChunk);
    })

    res.send('Sending Packet \n')

})


var corsOptions = {
  origin: '*',
  optionsSuccessStatus: 200
}

app.listen(port, () => console.log(os.hostname + ' listener starting on ' + port))