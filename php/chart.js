var ctx = document.getElementById('chart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chart_x,
        datasets: [
            {
                label: 'Requests',
                data: chart_y_requests,
                fill: false,
                borderColor: 'rgb(0, 158, 255)',
                pointRadius: 5,
                pointBorderColor: 'rgb(0, 158, 255)',
                pointBackgroundColor: 'rgb(0, 158, 255)',
                pointBorderWidth: 2,
            },
            {
                label: 'Blocked URLs',
                data: chart_y_blocked,
                fill: false,
                borderColor: 'rgb(255, 0, 0)',
                pointRadius: 5,
                pointBorderColor: 'rgb(255, 0, 0)',
                pointBackgroundColor: 'rgb(255, 0, 0)',
                pointBorderWidth: 2,
            },
        ],
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Time graph',
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                },
            }],
        },
    },
});





const d = new Date();
let hour = d.getHours();
var chart_x = [];

for (var i = hour + 1; i < hour + 24; i++) {
    if (i > 24) {
        i = i - 24;
    }
    chart_x.push(i);
}

var chart_y_requests = [];
var chart_y_blocked = [];

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    
    chart.update();
}

async function fetch_requests_requests(i) {
    let response0 = await fetch('/api_chart_requests#'+String(i));
    let responseText0 = await response0.text();
    chart_y_requests.push(Number(responseText0));
}

for (var i = hour + 1; i < hour + 24; i++) {
    if (i > 24) {
        i = i - 24;
    }
    (async() => {
        await fetch_requests_requests(i);
        
        
    })();
    
}



async function fetch_requests_blocked(i) {
    let response1 = await fetch('/api_chart_blocked#'+String(i));
    let responseText1 = await response1.text();
    chart_y_blocked.push(Number(responseText1));
}

for (var i = hour + 1; i < hour + 24; i++) {
    if (i > 24) {
        i = i - 24;
    }
    (async() => {
        await fetch_requests_blocked(i);
    })();
}

chart.data.datasets[0].data = chart_y_requests;
chart.data.datasets[1].data = chart_y_blocked;
chart.data.labels = chart_x;
chart.update();