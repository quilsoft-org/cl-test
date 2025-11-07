/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { ChartRenderer } from "../chart_renderer/chart_renderer";

export class SapMonitoringDashboard extends Component {
    static template = "sap_monitoring_dashboard.SapMonitoringDashboard";
    static components = { ChartRenderer };

    setup() {
        this.mockDataService = useService("mockDataService");

        this.state = useState({
            timeRange: "last_2_days",
            chartData: {},
        });

        this.entities = [
            { key: "Precios", color: "#3366CC" },
            { key: "Clientes", color: "#DC3912" },
            { key: "Productos", color: "#FF9900" },
            { key: "Preventa", color: "#109618" },
            { key: "Reparto", color: "#990099" },
        ];

        onWillStart(async () => {
            await this.loadChartData();
        });
    }

    async loadChartData() {
        const rawData = this.mockDataService.getChartData(this.state.timeRange);
        const formattedData = {};

        for (const entity of this.entities) {
            formattedData[entity.key] = {
                datasets: [{
                    label: entity.key,
                    data: rawData[entity.key],
                    borderColor: entity.color,
                    backgroundColor: `${entity.color}33`, // Color con transparencia para el área
                    fill: true,
                    tension: 0.2,
                }],
            };
        }
        this.state.chartData = formattedData;
    }

    async onTimeRangeChange(ev) {
        this.state.timeRange = ev.target.value;
        await this.loadChartData();
    }
}