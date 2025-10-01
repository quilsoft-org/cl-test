import {registry} from "@web/core/registry";
import {Component} from '@odoo/owl';
export class Example extends Component {
    static template = "test18e_default.Example";
}

registry.category("view_widgets").add("example", {component: Example});