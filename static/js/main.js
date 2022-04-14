import {ChessBoard} from "./board.js";

class Game {
  static instance;
  #board;
  constructor() {
    if ( Game.instance ) throw new Error("Singleton classes can't be instantiated more than once.")
     this.#board = new ChessBoard(0);
  }
  static getInstance(){
    if( !Game.instance ) Game.instance = new Game()
    return Game.instance;
  }
  start(color){

  }

}


document.addEventListener('DOMContentLoaded', () => {

    const game = Game.getInstance();
});



