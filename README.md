# Python games for beginners
 
Three small games, each one rewritten a few times while learning. The point isn't the games themselves — it's what changes between versions: no imports and no loops, then a `while` loop, then a cleaner rebuild. Each version is intentionally left in the repo so the progression stays visible, instead of only keeping the "best" one.
 
**[Play the finished versions →](https://isabelgrau.github.io/Python-games-for-beginners/)**
 
## What's here
 
### Tic-tac-toe
Two-player, local, no AI opponent.
- `tictactoe_v1.py` — no imported packages, no loops. Every possible board state is handled by hand.
- `tictactoe_v2.py` — same game, rebuilt with a `while` loop to run turns instead of repeating code.
- `tictactoe_v3.py` — refactored again for cleaner win-checking.
### Rock, paper, scissors
- `rock-paper-scissors-v1.py` — both players' moves are picked at random, just to get the win-checking logic right first.
- `rock-paper-scissors-v2.py` — player 1's move is real user input; the computer still picks randomly.
### Word guess
- `wordguess.py` — picks a random word, tracks wrong guesses, reveals correct letters as you go.
## Why the versions stay
 
Each version solves the same problem with slightly better tools than the last. Keeping all of them — instead of squashing the history into one final file — makes the *progression* the actual teaching content: what a no-loop solution looks like versus a `while`-loop solution versus a cleaner rewrite, side by side.
 
If you're new to Python, read them in order. If you've written a few programs already, the later versions are the ones worth borrowing from.
 
## Playing in the browser
 
The `web/` folder has browser versions of the final logic for all three games, deployed via GitHub Pages. They're there so the games are playable without installing Python — the versioned `.py` files above are still the actual teaching content.
 
