const express = require('express');
const process = require('process');
const app=express()
const port=3000

app.get("/",(req,res)=>{
    res.send("Hello world")
})

app.listen(port,()=>{
    console.log("hello world");
})

process.on('SIGINT',()=>{
    process.exit();
})