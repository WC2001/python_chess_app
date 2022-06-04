import {create, query} from "./utils.js";

export class MoveList extends HTMLElement{
    constructor() {
        super();
        this.whiteMoves = ['e3', 'e4', 'e3', 'e4', 'e3', 'e4', 'e3', 'e4'];
        this.blackMoves = ['e6', 'e5', 'e3', 'e4', 'e3', 'e4', 'e3'];
    }

    init(mountpoint){
        this.rerender();
        mountpoint.append(this);
        this.addListeners();
    }

    rerender(){
      this.innerHTML = "";
      const titleW = create`div${['titleW']}`;
      titleW.innerHTML = `<i class="far fa-chess-king"></i>`
      const titleB = create`div${['titleB']}`;
      titleB.innerHTML = `<i class="fas fa-chess-king"></i>`

      const whiteMovesContainer = create`div${['white']}`;
      const blackMovesContainer = create`div${['black']}`;

      this.whiteMoves.forEach( move => {
        const newMove = create`div${['move', 'white']}`;
        newMove.innerHTML = move;
        whiteMovesContainer.append(newMove)
      })

      this.blackMoves.forEach( move => {
        const newMove = create`div${['move', 'black']}`;
        newMove.innerHTML = move;
        blackMovesContainer.append(newMove)
      })

      this.append(titleW);
      this.append(titleB);
      this.append(whiteMovesContainer);
      this.append(blackMovesContainer);
    }

    addListeners(){
        query`move-list-element>.white`.addEventListener('scroll',(e)=>{
            const black = query`move-list-element>.black`;
            black.scrollTo(0, e.target.scrollTop);
        })

        query`move-list-element>.black`.addEventListener('scroll',(e)=>{
            const white = query`move-list-element>.white`;
            white.scrollTo(0, e.target.scrollTop);
        })
    }

    update(whiteMove, blackMove) {
      this.whiteMoves.push(whiteMove);
      this.blackMoves.push(blackMove);
      this.rerender();
      document.querySelector("move-list-element>.white").scrollTop = document.querySelector("move-list-element>.white").scrollHeight;
      document.querySelector("move-list-element>.black").scrollTop = document.querySelector("move-list-element>.white").scrollHeight;
      this.addListeners();
    }
}
if (!window.customElements.get('move-list-element'))
    window.customElements.define('move-list-element', MoveList);