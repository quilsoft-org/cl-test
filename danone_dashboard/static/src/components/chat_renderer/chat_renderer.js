/** @odoo-module **/

import { Component, onMounted, onWillUpdateProps, useRef } from "@odoo/owl";

export class ChartRenderer extends Component {
    static template = "sap_monitoring_dashboard.ChartRenderer";
    static props = {
        title: { type: String },
        chartData: { type: Object },
    };

    setup() {
        this.canvasRef = useRef("chart_canvas");
        this.chart = null;

        onMounted(() => {
            this.renderChart();
        });

        onWillUpdateProps((nextProps) => {
            if (this.chart) {
                this.chart.data.labels = nextProps.chartData.labels;
                this.chart.data.datasets[0].data = nextProps.chartData.datasets[0].data;
                this.chart.options.plugins.title.text = nextProps.title;
                this.chart.update();
            }
        });
    }

    renderChart() {
        if (this.chart) {
            this.chart.destroy();
        }
        this.chart = new Chart(this.canvasRef.el, {
            type: 'line',
            data: this.props.chartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false,
                    },
                    title: {
                        display: true,
                        text: this.props.title,
                        font: { size: 16 }
                    }
                },
                scales: {
                    x: {
                        type: 'time',
                        time: {
                            unit: 'day',
                            tooltipFormat: 'PPpp',
                        },
                        title: {
                            display: true,
                            text: 'Tiempo'
                        }
                    },
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Cantidad'
                        }
                    }
                }
            }
        });
    }
}