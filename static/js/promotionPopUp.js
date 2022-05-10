import {create, query} from "./utils.js";
import {pieceChosen} from "./events.js";


export class PromotionPopUp extends HTMLElement{
    constructor(color, row, column) {
        super();
        this.color = color;
        this.row = row;
        this.column = column;
    }

    init(mountpoint){

        const container = create`div${['promotion-pop-up-container']}`;

        if(this.color === 'w'){
            const knight = create`i${['far','fa-chess-knight']}`;
            const bishop = create`i${['far','fa-chess-bishop']}`;
            const queen = create`i${['far','fa-chess-queen']}`;
            const rook = create`i${['far','fa-chess-rook']}`;

            knight.id = "wKnightPromotion";
            bishop.id = "wBishopPromotion";
            rook.id = "wRookPromotion";
            queen.id = "wQueenPromotion";


            container.append(knight);
            container.append(bishop);
            container.append(rook);
            container.append(queen);
            this.append(container);

            mountpoint.append(this);

            query`#wKnightPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"k",color:"w"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            });
            query`#wBishopPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"B",color:"w"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
            query`#wRookPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"R",color:"w"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
            query`#wQueenPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"Q",color:"w"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })

        }
        else{
            const knight = create`i${['fas','fa-chess-knight']}`;
            const bishop = create`i${['fas','fa-chess-bishop']}`;
            const queen = create`i${['fas','fa-chess-queen']}`;
            const rook = create`i${['fas','fa-chess-rook']}`;

            knight.id = "bKnightPromotion";
            bishop.id = "bBishopPromotion";
            rook.id = "bRookPromotion";
            queen.id = "bQueenPromotion";



            container.append(knight);
            container.append(bishop);
            container.append(rook);
            container.append(queen);

            this.append(container);

            mountpoint.append(this);

            query`#bKnightPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"k",color:"b"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
            query`#bBishopPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"B",color:"b"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
            query`#bRookPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"R",color:"b"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
            query`#bQueenPromotion`.addEventListener('click', ()=>{
                query`chessboard-element`.promotePawn(this.row, this.column, {piece:"Q",color:"b"})
                document.body.dispatchEvent(pieceChosen);
                this.close();
            })
        }


    }
    close(){
        this.remove();
    }
}
if (!window.customElements.get('promotion-pop-up-element'))
    window.customElements.define('promotion-pop-up-element', PromotionPopUp);