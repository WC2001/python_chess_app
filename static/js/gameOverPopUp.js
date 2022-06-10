import { query,create } from "./utils.js";

export class GameOverPopUp extends HTMLElement {
    constructor(winner) {
        super();
        this.winner = winner;
    }

    init(mountpoint) {

        const container = create`div${['pop-up-container']}`;
        const title = document.createElement("h1");

        if (this.winner === "draw"){
            title.innerHTML = `Stalemate, game drawn !!!`
        }
        else{
            title.innerHTML = `${ this.winner } Player Won The Game !!!`
        }
        container.append(title);
        if ( this.winner === "w" ) {
            const white = create`i${['far','fa-chess-king']}`;
            container.append(white);
        } else {
            const black = create`i${['fas','fa-chess-king']}`;
            container.append(black);
        }

        this.append(container);
        mountpoint.append(this)

        this.addEventListener('click', ()=>{
            localStorage.clear()
            location.reload()
        })
    }

    close() {
        this.remove();
    }
}

if (!window.customElements.get('gameover-pop-up-element'))
    window.customElements.define('gameover-pop-up-element', GameOverPopUp);
