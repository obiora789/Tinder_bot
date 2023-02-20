<h1>Tinder Bot</h1>
This bot automates the process of finding a date on Tinder, by logging into Tinder; and using other factors such as proximity, and number of pictures uploaded, to get that perfect date. Enjoy!!<br>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8 or higher.</li>
  <li>Pycharm 2022.3.2 or higher.</li>
  <li>Selenium Webdriver(Chrome)</li>
  <li>Install and Import Selenium Undetected Chrome Driver.</li>
</ul>
<hr>
<h3>What to do</h3>
<ol>
  <li>Fork this Git and clone to your local PC.</li>
  <li>Download the selenium webdriver for your browser(I use Chrome i.e., chromedriver).</li>
  <li>Ensure you have updated Pycharm or other good updated IDE. I used Pycharm 2022.3.2 (Community Edition).</li>
  <li>Install Selenium undetected chromedriver within Pycharm console. e.g., pip install undetected-chromedriver</li>
  <li>Install python-dotenv within Pycharm console to translate environment variables. e.g., pip install python-dotenv</li>
  <li>Populate the environment variable with the actual path of your Selenium Chrome Webdriver.</li>
  <li>Specify your Tinder username and password as environment variables.</li>
  <li>Populate the environment variables as stated below</li>
  <ul>
    <li>CHROME_PATH=pathToChromeDriverOnYourPC</li>
    <li>TINDER_USERNAME=twitterUsername</li>
    <li>TINDER_PASSWORD=twitterPassword</li>
    <li>NAME=yourTinderNameToBeUsedToInitiateAConversationWhenAMatchIsFound</li>
  </ul>
  <li>That's all you need to do for now.😉</li>
</ol>
<p>Simply put, this program will ensure you get that perfect date by liking accounts which have met these two conditions which are:</p>
<ul>
  <li>Accounts with at least 3 pictures(to avoid scammers).</li>
  <li>Accounts located within 50km(can be altered though) from your current location.</li>
</ul>
<p>Once a match is found, the bot initiates the conversation automatically.</p>
<hr>
<h3>Results</h3>
<img src="https://twitter.com/md_changer/status/1627660352887422976/photo/1" alt="tinderLoginPage.jpg">
<img src="https://twitter.com/md_changer/status/1627660352887422976/photo/2" alt="loginThroughGmail.jpg">
<img src="https://twitter.com/md_changer/status/1627660352887422976/photo/3" alt="loginSuccessful.jpg">
<img src="https://twitter.com/md_changer/status/1627660352887422976/photo/4" alt="analyzingAccount.jpg">

<hr>
<h3>Bugs</h3>
<p>None as at the time of this report.</p>
