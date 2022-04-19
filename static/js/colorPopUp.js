import {create, query} from "./utils.js";
import {gameStarted} from "./events.js";

export class ColorPopUp extends HTMLElement{

    constructor() {
        super();
    }

    init(mountpoint){
        const container = create`div${['pop-up-container']}`;
        const white = create`i${['far','fa-chess-king']}`;
        white.id = "wPopUp";
        const black = create`i${['fas','fa-chess-king']}`;
        black.id = "bPopUp";

        container.append(white);
        container.append(black);

        this.append(container);
        mountpoint.append(this);

        query`#wPopUp`.addEventListener('click', ()=>{
            localStorage.setItem('color', 'w');
            document.body.dispatchEvent(gameStarted);
            this.close();
        });
        query`#bPopUp`.addEventListener('click', ()=>{
            localStorage.setItem('color', 'b');
            document.body.dispatchEvent(gameStarted);
            this.close();
        });
    }

    close(){
        this.remove();
    }


}
if (!window.customElements.get('color-pop-up-element'))
    window.customElements.define('color-pop-up-element', ColorPopUp);