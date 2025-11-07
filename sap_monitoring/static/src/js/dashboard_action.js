/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, useState, onWillStart } from "@odoo/owl";
import { generateMockSeries } from "./mock_data";
import { createLineChart, destroyChart } from "./charts";

class SapMonitoringDashboard extends Component {
    static template = "sap_monitoring.dashboard_template";

    setup() {
        this.state = useState({
            range: "last_2_days",
            start: null,
            end: null,
        });
        this.charts = {};

        onWillStart(() => {
            this._applyRange("last_2_days");
        });
    }

    _getRangeDates(key) {
        const now = new Date();
        const start = new Date(now);
        const ranges = {
            last_24_hours: 1,
            last_2_days: 2,
            last_7_days: 7,
            last_30_days: 30,
        };
        start.setDate(now.getDate() - (ranges[key] || 2));
        return { start, end: now };
    }

    _applyRange(key) {
        const { start, end } = this._getRangeDates(key);
        this.state.range = key;
        this.state.start = start;
        this.state.end = end;
        this._renderAllCharts();
    }

    _renderAllCharts() {
        const categories = ["Precios", "Clientes", "Productos", "Preventa", "Reparto"];
        Object.values(this.charts).forEach((c) => destroyChart(c));
        this.charts = {};
        const { start, end } = this.state;
        categories.forEach((name, i) => {
            const canvas = document.getElementById(`chart_${i}`);
            if (!canvas) return;
            const series = generateMockSeries(start, end, 30, 200, 60);
            const limitProfiles = [
                { green: 180, yellow: 120, red: 60 },   // Precios
                { green: 300, yellow: 200, red: 100 }, // Clientes
                { green: 90,  yellow: 60,  red: 30 },  // Productos
                { green: 140, yellow: 90,  red: 50 },  // Preventa
                { green: 80,  yellow: 50,  red: 20 },  // Reparto
            ];

            this.charts[i] = createLineChart(
                canvas,
                name,
                series.labels,
                series.values,
                limitProfiles[i]
            );

        });
    }

    onChangeRange(ev) {
        this._applyRange(ev.target.value);
    }
}

registry.category("actions").add("sap_monitoring.dashboard_action", SapMonitoringDashboard);
