import { Child } from '../child/child.js';
import {registry} from "@web/core/registry";
import {Component} from '@odoo/owl';
export class Example extends Component {
    static template = "test18e_default.Example";
    static components = { Child };

    setup() {
        this.message = "Hello World!";
    }

    alertMessage(event) {
        alert(this.message);
    }
}
registry.category("view_widgets").add("example", {component: Example});