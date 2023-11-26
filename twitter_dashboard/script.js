// Replace these values with your Twitter API credentials
const apiKey = '';
const apiSecretKey = '';
const accessToken = '';
const accessTokenSecret = '';

// Twitter API endpoint
const apiUrl = 'http://localhost:3000/tweets';;

// Function to fetch tweets from Twitter API
async function getTweets() {
    const response = await fetch(apiUrl, {
        headers: {
            'Authorization': `Bearer ${accessToken}`
        }
    });

    const data = await response.json();
    return data.data;
}

// Function to display tweets on the dashboard
function displayTweets(tweets) {
    const dashboard = document.querySelector('.dashboard');
    dashboard.innerHTML = '';

    tweets.forEach(tweet => {
        const tweetElement = document.createElement('div');
        tweetElement.classList.add('tweet');
        tweetElement.innerHTML = `<p>${tweet.text}</p>`;
        dashboard.appendChild(tweetElement);
    });
}

// Load tweets when the page is loaded
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const tweets = await getTweets();
        displayTweets(tweets);
    } catch (error) {
        console.error('Error fetching tweets:', error);
    }
});
