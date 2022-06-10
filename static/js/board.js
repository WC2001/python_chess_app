import {ChessField} from "./field.js";
import {query, queryAll} from "./utils.js";
import {blackWin, whiteWin, draw} from "./events.js";

export class ChessBoard extends HTMLElement {
    board;
    constructor(id, color='w') {
        super();
        this.id = id;
        this.color = color;
        this.intact = {w_king_intact:1, w_short:1, w_long:1, b_king_intact:1, b_short:1, b_long:1};
        this.en_passant = [-1, -1];
        this.init();


    }

    init(){

        this.initialiseFigures(this.color);

        for (let x=0; x<8; x+=1) {
            for (let y=0; y<8; y+=1){
                let tmp = new ChessField(x * 8 + y, this.board[x][y].piece, this.board[x][y].color)
                if((x+y)%2 === 0)
                    tmp.style.background = `#f2edd7ff`;
                else
                    tmp.style.background = `#9a7c6e`;
                tmp.init(this);
            }
        }

        let mountpoint = document.querySelector('#container');
        mountpoint.append(this);

    }

    static parseNewBoardFromServer(response){

        query`move-list-element`.updateLists(response.move_description[0], response.move_description[1])
        query`move-list-element`.update(query`move-list-element`.getLists().white, query`move-list-element`.getLists().black)
        let array = JSON.parse(response.result);

        if (array.stalemate === 1){
            document.body.dispatchEvent(draw)
        }

        query`chessboard-element`.setEnPassant(array.en_passant);
        query`chessboard-element`.setIntact(JSON.parse(array.intact));

        for (let i=0;i<8;i++){
            for(let j=0;j<8;j++)
                array.board[i][j] = JSON.parse(array.board[i][j])
        }

        console.group('array')
        console.log(query`chessboard-element`.getEnPassant());
        console.log(query`chessboard-element`.getIntact());
        console.log(array.board)
        console.log(array.mate)
        if(array.mate[0] === 1)
            document.body.dispatchEvent(blackWin)
        if(array.mate[1] === 1)
            document.body.dispatchEvent(whiteWin)

        console.groupEnd()

        return array.board;
    }

    getIntact(){
        let w_king = this.intact.w_king_intact;
        let b_king = this.intact.b_king_intact;
        let w_short = this.intact.w_short;
        let w_long = this.intact.w_long;
        let b_short = this.intact.b_short;
        let b_long = this.intact.b_long;
        return {
            'w_king_intact': w_king,
            'w_short': w_short,
            'w_long': w_long,
            'b_king_intact': b_king,
            'b_short': b_short,
            'b_long': b_long
        }
    }

    getKings(){
        let w_king;
        let b_king;
        queryAll`chessfield-element`.forEach((field)=>{
            if ( field.piece === 'K' && field.color === 'w')
                w_king = field.getPosition();
            if ( field.piece === 'K' && field.color === 'b')
                b_king = field.getPosition();
        })
        return {
            'w_king': w_king,
            'b_king': b_king
        }
    }

    getBoard(){
        return this.board;
    }

    getEnPassant(){
        return this.en_passant;
    }

    setEnPassant(content){
        this.en_passant = content

    }

    setBoard(board) {
        this.board = board
    }

    setIntact(content){
        this.intact.w_king_intact = content.w_king_intact;
        this.intact.b_king_intact = content.b_king_intact;
        this.intact.b_short = content.b_short;
        this.intact.b_long = content.b_long;
        this.intact.w_short = content.w_short;
        this.intact.w_long = content.w_long;
    }


    promotePawn(row, column, content){
        let field = document.getElementById(row*8+column);
        field.changeInnerHTML(content);
        field.classList.add('selected');
        this.board[row][column].piece = content.piece;
        this.board[row][column].color = content.color;

    }


    initialiseFigures(color){
        let res = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ];
        if(color==="w"){
            res[0].push({'piece':"R", 'color':"b"});
            res[0].push({'piece':"k", 'color':"b"});
            res[0].push({'piece':"B", 'color':"b"});
            res[0].push({'piece':"Q", 'color':"b"});
            res[0].push({'piece':"K", 'color':"b"});
            res[0].push({'piece':"B", 'color':"b"});
            res[0].push({'piece':"k", 'color':"b"});
            res[0].push({'piece':"R", 'color':"b"});

            for(let i=0;i<8;i++){
                res[1].push({'piece':"P", 'color':"b"});
                res[2].push({'piece':"", 'color':""});
                res[3].push({'piece':"", 'color':""});
                res[4].push({'piece':"", 'color':""});
                res[5].push({'piece':"", 'color':""});
                res[6].push({'piece':"P", 'color':"w"});
            }

            res[7].push({'piece':"R", 'color':"w"});
            res[7].push({'piece':"k", 'color':"w"});
            res[7].push({'piece':"B", 'color':"w"});
            res[7].push({'piece':"Q", 'color':"w"});
            res[7].push({'piece':"K", 'color':"w"});
            res[7].push({'piece':"B", 'color':"w"});
            res[7].push({'piece':"k", 'color':"w"});
            res[7].push({'piece':"R", 'color':"w"});
        }
        else{

            res[0].push({'piece':"R", 'color':"w"});
            res[0].push({'piece':"k", 'color':"w"});
            res[0].push({'piece':"B", 'color':"w"});
            res[0].push({'piece':"K", 'color':"w"});
            res[0].push({'piece':"Q", 'color':"w"});
            res[0].push({'piece':"B", 'color':"w"});
            res[0].push({'piece':"k", 'color':"w"});
            res[0].push({'piece':"R", 'color':"w"});

            for(let i=0;i<8;i++){
                res[1].push({'piece':"P", 'color':"w"});
                res[2].push({'piece':"", 'color':""});
                res[3].push({'piece':"", 'color':""});
                res[4].push({'piece':"", 'color':""});
                res[5].push({'piece':"", 'color':""});
                res[6].push({'piece':"P", 'color':"b"});
            }

            res[7].push({'piece':"R", 'color':"b"});
            res[7].push({'piece':"k", 'color':"b"});
            res[7].push({'piece':"B", 'color':"b"});
            res[7].push({'piece':"K", 'color':"b"});
            res[7].push({'piece':"Q", 'color':"b"});
            res[7].push({'piece':"B", 'color':"b"});
            res[7].push({'piece':"k", 'color':"b"});
            res[7].push({'piece':"R", 'color':"b"});
        }

        this.board = res;

    }

    static removeSelected() {
        queryAll`chessfield-element`.forEach( element => {
            element.classList.remove('selected');
            element.classList.remove('possible');
            element.listenerMode = "initial";
        })
    }

    static rerender(board) {
        queryAll`chessfield-element`.forEach( (field,i)=> {
            const element = board[Math.floor(i/8)][i%8]
            field.changeInnerHTML({ piece: element.piece, color: element.color })
            field.listenerMode = "initial";
        });
        query`chessboard-element`.setBoard(board);
    }

}

if (!window.customElements.get('chessboard-element'))
    window.customElements.define('chessboard-element', ChessBoard);

