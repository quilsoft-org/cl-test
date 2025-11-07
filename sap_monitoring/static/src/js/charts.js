/** @odoo-module **/

let chartInstances = {};

export function destroyChart(chart) {
    if (chart) {
        chart.destroy();
    }
}

export function createLineChart(canvas, title, labels, values) {
    const ctx = canvas.getContext("2d");

    const chart = new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                {
                    label: title,
                    data: values,
                    borderColor: "#4ea6f6",  // Azul principal Grafana
                    backgroundColor: "rgba(78,166,246,0.15)",
                    borderWidth: 1.6,
                    pointRadius: 3,
                    pointBackgroundColor: "#4ea6f6",
                    pointHoverRadius: 6,
                    tension: 0.35,
                },
            ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    mode: "nearest",
                    intersect: false,
                    callbacks: {
                        label: function (ctx) {
                            return ` ${ctx.raw} unidades`;
                        },
                    },
                },
            },
            scales: {
                x: {
                    ticks: { maxRotation: 0 },
                },
                y: {
                    beginAtZero: true,
                },
            },
        },
    });

    return chart;
}
