/** @odoo-module **/

export function destroyChart(chart) {
    if (chart) {
        chart.destroy();
    }
}

export function createLineChart(canvas, title, labels, values, limits) {
    const ctx = canvas.getContext("2d");

    const chart = new Chart(ctx, {
        type: "line",
        data: {
            labels,
            datasets: [
                // Datos reales
                {
                    label: title,
                    data: values,
                    borderColor: "#4ea6f6",
                    backgroundColor: "rgba(78,166,246,0.15)",
                    borderWidth: 1.6,
                    pointRadius: 3,
                    pointBackgroundColor: "#4ea6f6",
                    pointHoverRadius: 6,
                    tension: 0.35,
                },
                // Verde (OK)
                {
                    label: "OK",
                    data: Array(labels.length).fill(limits.green),
                    borderColor: "#3aff74",
                    borderWidth: 1,
                    pointRadius: 0,
                    borderDash: [6, 6],
                },
                // Amarillo (Advertencia)
                {
                    label: "Advertencia",
                    data: Array(labels.length).fill(limits.yellow),
                    borderColor: "#ffd93b",
                    borderWidth: 1,
                    pointRadius: 0,
                    borderDash: [6, 6],
                },
                // Rojo (Crítico)
                {
                    label: "Crítico",
                    data: Array(labels.length).fill(limits.red),
                    borderColor: "#ff5959",
                    borderWidth: 1,
                    pointRadius: 0,
                    borderDash: [6, 6],
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
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });

    return chart;
}
