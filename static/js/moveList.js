import {create, query} from "./utils.js";

export class MoveList extends HTMLElement{
    constructor() {
        super();
        this.whiteMoves = [];
        this.blackMoves = [];
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

      if (this.whiteMoves.length>0){
            this.whiteMoves.forEach( move => {
                const newMove = create`div${['move', 'white']}`;
                newMove.innerHTML = this.getRepresentation(move,'w');
                whiteMovesContainer.append(newMove)
            })
      }

      if (this.blackMoves.length>0){
            this.blackMoves.forEach( move => {
                const newMove = create`div${['move', 'black']}`;
                newMove.innerHTML = this.getRepresentation(move,'b');
                blackMovesContainer.append(newMove)
            })
      }

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

    getRepresentation(move, color){
        let res = ''
        if (move[0]==='P'){
            return [move[1] , move[2]].join('')
        }
        if (move[0] === 'k'){
            return [this.load_icon('k',color), move[1] , move[2]].join('')
        }
        if (move[0] === 'K'){
            return [this.load_icon('K',color), move[1] , move[2]].join('')
        }
        if (move[0] === 'B'){
            return [this.load_icon('B',color), move[1] , move[2]].join('')
        }
        if (move[0] === 'Q'){
            return [this.load_icon('Q',color), move[1] , move[2]].join('')
        }
        if (move[0] === 'R'){
            return [this.load_icon('R',color), move[1] , move[2]].join('')
        }
    }

    updateLists(move1, move2){
        if(this.whiteMoves.length === this.blackMoves.length){
            this.whiteMoves.push(move1)
            if(move2 !== '')
            this.blackMoves.push(move2)
        }
        else{
            this.blackMoves.push(move1)
            if(move2 !== '')
            this.whiteMoves.push(move2)
        }
    }
    getLists(){
        let res = {white:this.whiteMoves, black:this.blackMoves}
        return res
    }

    update(whiteMoves, blackMoves) {
      this.whiteMoves = whiteMoves;
      this.blackMoves = blackMoves;
      this.rerender();
      document.querySelector("move-list-element>.white").scrollTop = document.querySelector("move-list-element>.white").scrollHeight;
      document.querySelector("move-list-element>.black").scrollTop = document.querySelector("move-list-element>.white").scrollHeight;
      this.addListeners();
    }

    load_icon(piece, color) {
        if (piece === "R" && color === "b")
            return `<i class="fas fa-chess-rook"></i>`;
        if (piece === "R" && color === "w")
            return `<i class="far fa-chess-rook"></i>`;
        if (piece === "B" && color === "b")
            return `<i class="fas fa-chess-bishop"></i>`;
        if (piece === "B" && color === "w")
            return `<i class="far fa-chess-bishop"></i>`;
        if (piece === "K" && color === "b")
            return `<i class="fas fa-chess-king"></i>`;
        if (piece === "K" && color === "w")
            return `<i class="far fa-chess-king"></i>`;
        if (piece === "k" && color === "b")
            return `<i class="fas fa-chess-knight"></i>`;
        if (piece === "k" && color === "w")
            return `<i class="far fa-chess-knight"></i>`;
        if (piece === "Q" && color === "b")
            return `<i class="fas fa-chess-queen"></i>`;
        if (piece === "Q" && color === "w")
            return `<i class="far fa-chess-queen"></i>`;
        if (piece === "P" && color === "b")
            return `<i class="fas fa-chess-pawn"></i>`;
        if (piece === "P" && color === "w")
            return `<i class="far fa-chess-pawn"></i>`;

        return ""
    }
}
if (!window.customElements.get('move-list-element'))
    window.customElements.define('move-list-element', MoveList);