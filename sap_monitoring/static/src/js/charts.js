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
                    borderWidth: 1.5,           // ← línea fina
                    pointRadius: 3,             // ← puntos visibles y pequeños
                    pointHoverRadius: 6,        // ← puntos grandes al hover
                    tension: 0.3,               // ← suavizado agradable
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
