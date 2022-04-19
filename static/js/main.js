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
    document.body.addEventListener('gamestarted', ()=>{
        this.#board = new ChessBoard(0, localStorage.getItem('color'));
        this.#moveList = new MoveList();
        this.#moveList.init(query`#container`);
        this.#moveList.update([...this.#moveList.whiteMoves],[...this.#moveList.blackMoves]);
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
          console.log('akmckal');
          const gameoverPopUp = new GameOverPopUp(e.detail.winner);
          gameoverPopUp.init(document.body);
      });
      // document.body.dispatchEvent(blackWin);
  }




}


document.addEventListener('DOMContentLoaded', () => {

    const game = Game.getInstance();
});



