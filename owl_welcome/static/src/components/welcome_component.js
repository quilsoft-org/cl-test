// Component es la clase base para crear componentes en OWL
// useState es un hook que permite manejar el estado local en componentes funcionales o sea la reactividad
// registry es un objeto que permite registrar y gestionar componentes, servicios u otros elementos en la aplicación
import { Component, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class WelcomeComponent extends Component {
    // Definimos el template que usará este componente es donde se linkea con el XML
    static template = "owl_welcome.WelcomeComponent";

    // Definimos el estado inicial del componente
    setup() {
        this.nextId = 1; // Inicializamos un contador para los IDs
        this.state = useState({
            skills: [
                {id: this.nextId++, text: "Componente OWL creado", completed: true},
                {id: this.nextId++, text: "Template QWEB Funcionando", completed: true},
                {id: this.nextId++, text: "Estado Reactivo con useState", completed: true},
                {id: this.nextId++, text: "Registry pattern aplicado", completed: true},
                {id: this.nextId++, text: "Client Action Launcher", completed: false},
            ]
        });
    }
    removeSkill(skilId) {
        console.log("Removing skill with id:", skilId);
        this.state.skills = this.state.skills.filter(skill => skill.id !== skilId);
    }

    goToNextExercise() {}
}



// Encuentra una accion con el tag owl_welcome_component y lanza el componente WelcomeComponent
registry.category("actions").add("owl_welcome_component", WelcomeComponent);
