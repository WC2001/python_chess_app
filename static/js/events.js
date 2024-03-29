export const gameStarted = new CustomEvent('gamestarted', {
  detail: {}
});

export const whiteWin = new CustomEvent('gameover', {
  detail: {
      winner: "white"
  }
});

export const blackWin = new CustomEvent('gameover', {
  detail: {
      winner: "black"
  }
});

export const draw = new CustomEvent('gameover', {
  detail: {
      winner: "draw"
  }
});

export const pieceChosen = new CustomEvent('piecechosen', {
    detail: {}
});