import {query, queryAll} from "./utils.js";
import {ChessBoard} from "./board.js";
import {PromotionPopUp} from "./promotionPopUp.js";
import {pieceChosen} from "./events.js";

export class ChessField extends HTMLElement {
    constructor(id, piece, color) {
        super();
        this.id = id;
        this.piece = piece;
        this.color = color;
        this.listenerMode = 'initial';
    }

    init(mountpoint) {
        this.innerHTML = this.load_icon(this.piece, this.color);
        mountpoint.append(this);
        this.onclick = async () => {
            console.log(`${ this.piece } | ${ this.color } | ${ this.listenerMode } `);
            if (this.piece !== '' && this.listenerMode === 'initial' /*&& this.color === query`chessboard-element`.color*/) {
                queryAll`chessfield-element`.forEach((field)=> {
                    field.classList.remove('selected'); 
                    field.classList.remove('possible');
                })
                const kings_positions = query`chessboard-element`.getKings();
                const intact1 = query`chessboard-element`.getIntact();
                this.classList.add('selected');
                this.listenerMode = "move";
                console.log(intact1);
                console.log(kings_positions);
                const response = await fetch("/moves", {
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        position: this.getPosition(), board: query`chessboard-element`.getBoard(),
                        w_king: kings_positions.w_king, b_king: kings_positions.b_king,
                        intact: {'w_king': intact1.w_king_intact, 'w_short': intact1.w_short, 'w_long': intact1.w_long,
                            'b_king': intact1.b_king_intact, 'b_short': intact1.b_short, 'b_long': intact1.b_long},
                        player: localStorage.getItem('color'),
                        en_passant: query`chessboard-element`.getEnPassant()
                    })

                })

                const data = await response.json();
                console.log(data)
                data.result.forEach((element) => {
                    let id = element[0] * 8 + element[1];
                    console.log(element)
                    queryAll`chessfield-element`.forEach(e => {

                        if (+e.id === id) {
                            console.log(e)
                            e.classList.add('possible')
                            e.listenerMode = 'move'

                        }

                    })
                })
                console.log(data);
            } else if (this.listenerMode === 'move' && this.classList.contains('selected')) {
                ChessBoard.removeSelected()
            } else if (this.listenerMode === 'move' && this.classList.contains('possible')) {
                if (query`.selected`.piece === 'P' && ((this.id>=0 && this.id <=7) || (this.id>=56 && this.id<=63))){
                    const position = query`.selected`.getPosition();
                    this.promotionPopup = new PromotionPopUp(query`.selected`.color, position.x, position.y);
                    this.promotionPopup.init(document.body);

                    document.body.addEventListener('piecechosen', async () => {
                    const initial = query`.selected`.getPosition();
                    const intact1 = query`chessboard-element`.getIntact();
                    const kings_positions = query`chessboard-element`.getKings();
                    const response = await fetch('/changePosition', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            board: query`chessboard-element`.getBoard(),
                            w_king: kings_positions.w_king, b_king: kings_positions.b_king,
                            initial: {'x': initial.x, 'y': initial.y},
                            final: {'x': this.getPosition().x, 'y': this.getPosition().y},
                            intact: {'w_king': intact1.w_king_intact, 'w_short': intact1.w_short, 'w_long': intact1.w_long,
                            'b_king': intact1.b_king_intact, 'b_short': intact1.b_short, 'b_long': intact1.b_long},
                            player: localStorage.getItem('color'),
                            en_passant: query`chessboard-element`.getEnPassant()

                        })
                    })
                    // const data = JSON.parse(await response.json());
                    const data = await response.json();
                    const newBoard = ChessBoard.parseNewBoardFromServer(data);
                    console.log(newBoard);
                    this.listenerMode = "initial"
                    ChessBoard.rerender(newBoard);
                })
                }
                else{
                    const initial = query`.selected`.getPosition();
                    const kings_positions = query`chessboard-element`.getKings();
                    const intact1 = query`chessboard-element`.getIntact();
                    console.log(intact1);
                    const response = await fetch('/changePosition', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'Accept': 'application/json'
                        },
                        body: JSON.stringify({
                            board: query`chessboard-element`.getBoard(),
                            w_king: kings_positions.w_king, b_king: kings_positions.b_king,
                            initial: {'x': initial.x, 'y': initial.y},
                            final: {'x': this.getPosition().x, 'y': this.getPosition().y},
                            intact: {'w_king': intact1.w_king_intact, 'w_short': intact1.w_short, 'w_long': intact1.w_long,
                            'b_king': intact1.b_king_intact, 'b_short': intact1.b_short, 'b_long': intact1.b_long},
                            player: localStorage.getItem('color'),
                            en_passant: query`chessboard-element`.getEnPassant()
                        })
                    })
                    // const data = JSON.parse(await response.json());
                    const data = await response.json();
                    const newBoard = ChessBoard.parseNewBoardFromServer(data);
                    console.log(newBoard);
                    this.listenerMode = "initial"
                    ChessBoard.rerender(newBoard);

                }


            }
        }


    }
    changeInnerHTML(content){
        this.innerHTML = this.load_icon(content.piece, content.color);
        this.classList.remove('selected');
        this.classList.remove('possible');
        this.piece = content.piece;
        this.color = content.color;
    }

    getPosition() {
        return {
            x: Math.floor(this.id / 8),
            y: this.id % 8
        };
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

if (!window.customElements.get('chessfield-element'))
    window.customElements.define('chessfield-element', ChessField);

