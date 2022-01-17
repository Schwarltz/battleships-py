# battleships-py

A command line implementation of battleships to fight against an AI. Written in python 3.9.2.

## How To Play

### Rules

On 2 separate 10x10 boards representing the ocean, both you and the AI will place 5 ships down. 

<b>Ship Hulls:</b>
```
Aircraft Carrier (A)    : 5 units
Battleship (B)          : 4 units
Cruiser (C)             : 3 units
Submarine (S)           : 3 units
Destroyer (D)           : 2 units
```
- Ships can only be placed horizontally (H) or vertically (V).
- Ships cannot overlap with other ships or extend over the border.
- Ship locations cannot be changed once the game begins.

Once all ships are placed the game begins. The player cannot see where the opponent's ships are located under the fog of war.

Each turn, the player will be allowed to target a coordinate to shoot at. If the shot hits a ship, then the ship will be identified and a hit is recorded. If the shot misses, then the hit is recorded as a miss for that coordinate. The enemy will then be allowed to do the same thing towards your board.

If the next shot hits a ship and all sections of the ship have been hit, then the ship is deemed sunk by the game.

The game will end when all ships on either board are sunk.

<hr/>

### Setup

Run the command to begin executing the file. 

```
python3 main.py
```
<hr/>

### Playing the game

You will then be prompted to input locations to place your ships.

```
<ship hull> <row number> <column number> <direction>
```

For example on a 5x5 board, writing "B 0 3 V" places the ship down as:

```
.  .  .  B  .
.  .  .  B  .
.  .  .  B  .
.  .  .  B  .
.  .  .  .  .
```
Note that the board is indexed from 0.

Once all ships are placed, you can then input where your shot should land on the opponent's board.

```
<row number> <column number>
```

i.e. placing a shot as "2 3" that misses the opponent's ship registers on the board as:

```
.  .  .  .  .
.  .  .  .  .
.  .  .  M  .
.  .  .  .  .
.  .  .  .  .
```

Misses are registered as "M" while hits are registered as "H".

## <i>Enjoy!</i>