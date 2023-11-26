const express = require('express');
const fetch = require('node-fetch');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:5500');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    res.setHeader('Access-Control-Allow-Credentials', 'true');

    if (req.method === 'OPTIONS') {
        res.sendStatus(200);
    } else {
        next();
    }
});

app.get('/tweets', async (req, res) => {
    const apiUrl = 'https://api.twitter.com/2/tweets';
    const response = await fetch(apiUrl, {
        headers: {
            // Insert Bearer Access Token Here
            'Authorization': `AAAAAAAAAAAAAAAAAAAAAFvWrAEAAAAAEACeFBq8gPpQ4n2WvFkU5Yixyvs%3DwDiPfNvk0R74Nam8qfAIgTVmcz1q9DLulvVED2Q5EvbVJPPD7W`
        }
    });

    const data = await response.json();
    res.json(data);
});

app.listen(port, () => {
    console.log(`Server listening at http://localhost:${port}`);
});
