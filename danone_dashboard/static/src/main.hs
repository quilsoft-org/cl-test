/** @odoo-module **/

import { registry } from "@web/core/registry";
import { SapMonitoringDashboard } from "./components/dashboard/dashboard";

registry.category("actions").add("sap_monitoring_dashboard.dashboard_action", SapMonitoringDashboard);