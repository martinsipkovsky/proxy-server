

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

    // status color blocks
    async function status_proxy() {
        let response = await fetch('/proxy_status');
        let responseText = await response.text();
        if (responseText == "offline") {
            document.getElementById('proxy-status').style.backgroundColor = "#ff0000";
        } else if (responseText == "online") {
            document.getElementById('proxy-status').style.backgroundColor = "#00ff00";
        } else {
            document.getElementById('proxy-status').style.backgroundColor = "#ffd900";
        }
        
    }

    async function status_ghost() {
        let response = await fetch('/ghost_status');
        let responseText = await response.text();
        if (responseText == "offline") {
            document.getElementById('ghost-status').style.backgroundColor = "#ff0000";
        } else if (responseText == "online") {
            document.getElementById('ghost-status').style.backgroundColor = "#00ff00";
        } else {
            document.getElementById('ghost-status').style.backgroundColor = "#ffd900";
        }
        
    }

    async function status_vpn() {
        let response = await fetch('/vpn_status');
        let responseText = await response.text();
        if (responseText == "offline") {
            document.getElementById('vpn-status').style.backgroundColor = "#ff0000";
        } else if (responseText == "online") {
            document.getElementById('vpn-status').style.backgroundColor = "#00ff00";
        } else {
            document.getElementById('vpn-status').style.backgroundColor = "#ffd900";
        }
        
    }

    async function status_tor() {
        let response = await fetch('/tor_status');
        let responseText = await response.text();
        if (responseText == "offline") {
            document.getElementById('tor-status').style.backgroundColor = "#ff0000";
        } else if (responseText == "online") {
            document.getElementById('tor-status').style.backgroundColor = "#00ff00";
        } else {
            document.getElementById('tor-status').style.backgroundColor = "#ffd900";
        }
        
    }
        
    (async() => {
        while (true) {
            await fetch_requests(); 
            await fetch_blocked();

            await status_proxy();
            await status_ghost();
            await status_vpn();
            await status_tor();

            await sleep(2000);
 
        };

    })();
  });