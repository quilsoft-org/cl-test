/** @odoo-module **/

import { registry } from "@web/core/registry";

export const mockDataService = {
    start() {
        /**
         * Genera datos de serie temporal simulados.
         */
        const generateData = (hours, maxVal) => {
            const data = [];
            const now = new Date();
            for (let i = 0; i < hours * 2; i++) { // Genera un punto cada 30 mins
                const timestamp = new Date(now.getTime() - i * 30 * 60 * 1000);
                // Simula alguna variabilidad y posibles caídas
                const factor = Math.random() < 0.1 ? 0.5 : 1.0; // 10% de chance de una caída
                const value = Math.floor((Math.random() * (maxVal - maxVal * 0.7) + maxVal * 0.7) * factor);
                data.push({ x: timestamp, y: value });
            }
            return data.reverse();
        };

        return {
            /**
             * Obtiene los datos para todas las entidades basado en un rango de tiempo.
             */
            getChartData(timeRange) {
                let hours = 48; // Default a 2 días
                if (timeRange === "last_24_hours") {
                    hours = 24;
                } else if (timeRange === "last_7_days") {
                    hours = 7 * 24;
                }

                return {
                    "Precios": generateData(hours, 15000),
                    "Clientes": generateData(hours, 800),
                    "Productos": generateData(hours, 25000),
                    "Preventa": generateData(hours, 5000),
                    "Reparto": generateData(hours, 1200),
                };
            },
        };
    },
};

registry.category("services").add("mockDataService", mockDataService);