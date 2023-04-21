Node.js-based project supporting parsing of many different backends as well as ad networks, JavaScript libraries, and server setups. You can also run Wappalyzer via Docker. To first download the Docker image, run:

$ docker pull wappalyzer/cli
docker run wappalyzer/cli https://www.example.com/ | jq . 

Finding the owner of a website
$pip install python-whois