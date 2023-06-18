const express = require('express');
const fs = require('fs');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.post('/upload', async (req, res) => {
    console.log(req);
  
    res.json(true);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

