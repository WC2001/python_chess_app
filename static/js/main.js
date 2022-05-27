import {ChessBoard} from "./board.js";
import {ColorPopUp} from "./colorPopUp.js";
import {GameOverPopUp} from "./gameOverPopUp.js";
import {blackWin} from "./events.js";
import {MoveList} from "./moveList.js";
import {query} from "./utils.js";

class Game {
  static instance;
  #board;
  #moveList;
  constructor() {
    this.start();
    if ( Game.instance ) throw new Error("Singleton classes can't be instantiated more than once.")
    document.body.addEventListener('gamestarted', async () => {
        this.#board = new ChessBoard(100, localStorage.getItem('color'));
        this.#moveList = new MoveList();
        this.#moveList.init(query`#container`);
        this.#moveList.update([...this.#moveList.whiteMoves], [...this.#moveList.blackMoves]);
        const response = await fetch('/firstMove', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                board: query`chessboard-element`.getBoard(),
                w_king: query`chessboard-element`.getKings().w_king,
                b_king: query`chessboard-element`.getKings().b_king,
                intact: {
                    'w_king': 1, 'w_short': 1, 'w_long': 1,
                    'b_king': 1, 'b_short': 1, 'b_long': 1
                },
                player: localStorage.getItem('color'),
                en_passant: query`chessboard-element`.getEnPassant()
            })

        })
        const data = await response.json();
        this.#board = ChessBoard.parseNewBoardFromServer(data);
        console.log(this.#board);
        ChessBoard.rerender(this.#board);
    })
  }
  static getInstance(){
    if( !Game.instance ) Game.instance = new Game()
    return Game.instance;
  }
  start(){
      localStorage.clear();
      this.popUp = new ColorPopUp();
      this.popUp.init(document.body);
      document.body.addEventListener('gameover', (e)=>{
          const gameoverPopUp = new GameOverPopUp(e.detail.winner);
          gameoverPopUp.init(document.body);
      });

      // document.body.dispatchEvent(blackWin);
  }




}


document.addEventListener('DOMContentLoaded', () => {

    const game = Game.getInstance();
});



