#!/usr/bin/node

const express = require('express')
const os = require("os");
const { spawn } = require('child_process');
const app = express()
const port = 3000
var cors = require('cors')

var bodyParser = require('body-parser')
app.use(bodyParser.urlencoded({ extended: false }))

app.post('/', (req, res) => {

    try {
        resp = child.kill()
        console.log(resp)
        console.log('killed process')
    }
    catch {
        console.log("none");
    }
    child = spawn('python3', ['scripts/send-single-packet-lora.py', JSON.stringify(req.body)], [], function(err, stdout, stderr) { 
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

app.get('/', (req, res) => {

    res.send('Server is UP \n')

})

app.get('/test', (req, res) => {

    try {
        resp = child.kill()
        console.log(resp)
        console.log('killed process')
    }
    catch {
        console.log("none");
    }
    child = spawn('python3', ['scripts/send-single-packet-lora.py', '{test-api}'], [], function(err, stdout, stderr) { 
        if(err) { console.log(err) }
        if(stderr) { console.log(err) }
        console.log(stdout); 
    });   

    child.stdout.on('data',function(chunk){

        var textChunk = chunk.toString('utf8');// buffer to string

        console.log(textChunk);
    })

    res.send('Sending Test Packet \n')

})


var corsOptions = {
  origin: '*',
  optionsSuccessStatus: 200
}

app.listen(port, () => console.log(os.hostname + ' listener starting on ' + port))