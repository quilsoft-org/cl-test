
import {Component} from '@odoo/owl';

export class Child extends Component {
    static template = "test18e_default.Child";
    static props = {
        title: {type: String},
        list: {type: Array},
    };
}
