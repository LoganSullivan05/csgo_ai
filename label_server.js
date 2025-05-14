const fs = require('fs');
const express = require('express');
const http = require('http');

let index = Number(fs.readFileSync("last_index.txt").toString());
let labels = [];
const app = express();
const httpServer = http.createServer(app);

app.get("/",(req,res)=>{res.sendFile(__dirname+"/label_client.html")});
app.get("/next",(req,res)=>{
    res.sendFile(__dirname+"/raw_data/screenshot_"+(++index)+".png");
});

app.get("/label",(req,res)=>{
    console.log(req.query);
    const dest = "images2/"+req.query.team+"/screenshot_"+index+".png";
    fs.copyFileSync("raw_data/screenshot_"+index+".png",dest);
    res.sendFile(__dirname+"/raw_data/screenshot_"+(++index)+".png");
});

app.get("/save",(req,res)=>{
    const labels_old = JSON.parse(fs.readFileSync("labels.json"));
    const labels_new = [...labels_old, labels];
    fs.writeFileSync("labels.json", JSON.stringify(labels_new));
    saved_index = index - 1;
    fs.writeFileSync("last_index.txt", saved_index.toString());
    
    console.log("saved label data");
    res.send("Saved");
});

httpServer.listen(80);
console.log("Label server started on port 80");