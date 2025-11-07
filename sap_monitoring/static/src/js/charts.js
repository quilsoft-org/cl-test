/** @odoo-module **/
// Wrapper helpers for Chart.js usage
let ChartJS = null;

function ensureChartJS() {
    if (ChartJS) return Promise.resolve(ChartJS);
    if (window.Chart) {
        ChartJS = window.Chart;
        return Promise.resolve(ChartJS);
    }
    // If Chart.js not available, reject - the template loads Chart.js from CDN.
    return Promise.reject(new Error('Chart.js not loaded'));
}

export function createLineChart(canvas, title, labels, data) {
    // canvas may be element or id
    const ctx = (typeof canvas === 'string') ? document.getElementById(canvas).getContext('2d') : canvas.getContext('2d');
    return ensureChartJS().then((Chart) => {
        const cfg = {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: title,
                    data: data,
                    fill: false,
                    tension: 0.2,
                    pointRadius: 2,
                }],
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        enabled: true,
                        mode: 'nearest',
                        intersect: false,
                    },
                },
                scales: {
                    x: {
                        display: true,
                        ticks: { maxRotation: 0, autoSkip: true },
                        title: { display: false },
                    },
                    y: {
                        display: true,
                        title: { display: true, text: 'Cantidad' },
                    }
                }
            }
        };
        const chart = new Chart(ctx, cfg);
        return chart;
    }).catch((err) => {
        console.error('Chart.js error', err);
        return null;
    });
}

export function destroyChart(chartPromiseOrInstance) {
    // if promise, resolve then destroy
    if (!chartPromiseOrInstance) return;
    // If it's a promise, try to handle it
    if (typeof chartPromiseOrInstance.then === 'function') {
        chartPromiseOrInstance.then((chart) => {
            if (chart && chart.destroy) chart.destroy();
        }).catch(()=>{});
    } else {
        if (chartPromiseOrInstance && chartPromiseOrInstance.destroy) chartPromiseOrInstance.destroy();
    }
}
