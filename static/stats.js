

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
  }

$(document).ready(function() {
    async function fetch_requests() {
        let response = await fetch('/api_requests');
        let responseText = await response.text();
        document.getElementById('requests').innerHTML = responseText;
    }

    async function fetch_blocked() {
        let response = await fetch('/api_blocked');
        let responseText = await response.text();
        document.getElementById('blocked').innerHTML = responseText;
        
    }
        
    (async() => {
        while (true) {
            await fetch_requests(); 
            await fetch_blocked(); 
            await sleep(2000);

            
            
        };

    })();
  });