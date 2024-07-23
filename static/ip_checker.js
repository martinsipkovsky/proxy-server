function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

async function get_ip() {
    let response_ip = await fetch('/get_ip');
    let responseText_ip = await response_ip.text();
    document.getElementById('ip').innerHTML = responseText_ip;
}

(async() => {
    while (1 < 5) {
        await get_ip();
        await sleep(2000);
    }
})();