import {ChessField} from "./field.js";
import {query, queryAll} from "./utils.js";

export class ChessBoard extends HTMLElement {
    board;
    constructor(id, color='w') {
        super();
        this.id = id;
        this.color = color;
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
        let array = JSON.parse(response.result);
        console.log(array.board)
        // const newArray = Object.keys(array).map((key)=> JSON.parse(array[key]))
        for (let i=0;i<8;i++){
            for(let j=0;j<8;j++)
                array.board[i][j] = JSON.parse(array.board[i][j])
        }
        console.log(array.board)
        return array.board;
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

    setBoard(board) {
        this.board = board
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

