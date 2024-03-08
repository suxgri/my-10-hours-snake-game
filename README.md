# my-10-hours-snake-game
just a snake game, with all the steps (commits) it took to make it work (10 hours is the time it did take me to make it!).

I decided to take a couple of days free from Laravel to play with some python basics and decided to try to make the snake game, 
i have never been into games and the only time i spent on them was while reading the book Eloquent Javascript ch.16 A Platform Game.

-Added kyboard events functionality (snippet copied and pasted from https://kivy.org/doc/stable/api-kivy.core.window.html)

-added a square representing the area where the snake is allowed to move

-added fixed square representing the initial snake

-added button to start the game

-added movement (with keypresses) to snake

-allow snake movements within boundaries

-add continuous movement to snake with kivy clock.
At the moment the hardcoded right direction is applied every n seconds to the snake that is stopped by the boundary collision.

-removed unnecessary canmove() method

-implemented game lost mechanism, when the snake next move collides with border the game is lost

-added logic to allow snake to change direction on keypress

-introduced food to game at start, game has logic to introduce food on a free grid spot 