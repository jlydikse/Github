// Replace these values with your Twitter API credentials
const apiKey = 'w9HezbN7BY0lzWQSz8euQT9yw';
const apiSecretKey = 'KkVJE0ydMbJl948ixvNDDuYx9qeaZuhUsBYNhR2grI5eqhcamh';
const accessToken = '3354462514-MQI4E59mGjEnuV0PP4xT4JBTDtefF79vOVsHFoe';
const accessTokenSecret = 'pmK2SOw74I8IFUdu4Q7HCUKkO4dAAbdYrU3OujHJiDpVV';

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
