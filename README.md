# README (Project Report)

## Overview

This project implements a simple arcade-style game using a Finite State Machine (FSM) approach in Verilog. The concept is a basic “Catch the Falling Object” game:

- A player controls a paddle at the bottom of a display area.
- An object falls from the top to the bottom.
- The player must move the paddle horizontally to catch the falling object.
- Each successful catch increments the score. Missing the object ends the game.

The game is structured around a set of well-defined states and transitions, demonstrating how complex behaviors can be built from simple finite state principles.

## Game Concept

**States:**
1. **IDLE:** The game awaits the player’s start command.
2. **PLAYING:** The object falls from top to bottom. The player can move the paddle left or right. Each time the object reaches the bottom:
   - If it’s caught by the paddle, the score increases, and the object resets to the top for another round.
   - If it’s missed, the game transitions to the GAME_OVER state.
3. **GAME_OVER:** The final score is displayed, and the game is over. A reset command returns the system to IDLE.

**Transitions:**
- IDLE → PLAYING: On start button press.
- PLAYING → GAME_OVER: If the object reaches the bottom and is not caught.
- GAME_OVER → IDLE: On reset.

## Inputs and Outputs

**Inputs:**
- `clk`: System clock signal.
- `reset`: Resets the game to the IDLE state.
- `start_button`: Begins the game from the IDLE state.
- `left_button`/`right_button`: Control paddle movement.

**Outputs:**
- `paddle_x`: Paddle’s horizontal position.
- `object_x`, `object_y`: Object’s coordinates.
- `score`: Current player score.
- `game_state_indicator`: Indicates the current FSM state (for debugging or display).

These signals can be connected to external displays (e.g., VGA, LED matrix, seven-segment displays) to visualize the gameplay.

## FSM Implementation Details

1. **State Encoding:**
   - IDLE = `2'b00`
   - PLAYING = `2'b01`
   - GAME_OVER = `2'b10`

2. **State Transitions:**
   Using Verilog `always` blocks and case statements, the machine transitions based on input conditions. The logic ensures smooth and predictable state changes.

3. **Object Movement:**
   A counter triggered by `clk` determines when the object falls one step. Adjusting this counter changes the falling speed and game difficulty.

4. **Paddle Movement:**
   Player inputs move the paddle’s position, with boundary checks ensuring it remains within the play area.

5. **Scoring:**
   Every time the object is caught at the bottom row, the score increments before resetting the object’s position.

## Karnaugh Maps (K-Maps)

K-maps were used to simplify the logic for next-state calculations. By translating desired state transitions into a truth table and applying K-map minimization, we reduced logic complexity. Don’t care conditions for unused states further simplified the final Boolean expressions.

## Challenges and Solutions

1. **Timing Control:**  
   To ensure smooth gameplay, we implemented a timing counter for object movement. This provided consistent and adjustable falling speed.

2. **Debouncing Inputs (Practical Consideration):**  
   In real hardware, button inputs may be noisy. While we assumed ideal inputs for this project, a debouncing mechanism would be included in a real-world implementation.

3. **Boundary Checking:**
   Ensuring the paddle and object remain within defined coordinates required careful conditional logic.

4. **Logic Minimization:**
   Utilizing K-maps simplified complex conditional statements into more compact Boolean formulas, reducing the hardware resources and potentially increasing the circuit’s operating speed.

## Connections to Digital Logic Concepts

This project integrates key digital logic principles:

- **Finite State Machines:** Demonstrating how a real-world scenario (a simple game) can be directly implemented using FSMs.
- **Synchronous Design:** All operations are synchronized to a clock, reinforcing the importance of timing in digital systems.
- **Boolean Algebra and Minimization:** Applying K-map techniques to simplify logic matches course teachings on efficient circuit design.
- **Hierarchical Design:** Breaking the game into smaller functional blocks (state control, object movement, scoring) promotes clarity and scalability.

## Conclusion

This FSM-based arcade game illustrates how fundamental digital logic concepts translate into a tangible project. By leveraging state machines, timing counters, and Karnaugh maps, we constructed a functional and logically elegant system. The result is a framework that can be easily extended for more complex games or integrated into larger digital systems.

Overall, the project reinforces the relationship between theory and practice, showing how well-understood digital logic principles can create engaging and interactive hardware-based applications.
