# README (Project Report)

## Overview

This project implements a simple arcade-style “Catch the Falling Object” game using a Finite State Machine (FSM) design. Originally, the FSM logic and transitions were developed for a Verilog-based hardware implementation. To make the concepts more accessible and testable, two supplementary files are provided:

1. **Python Simulation File:** A Python script that simulates the game logic.  
   [**Link to Python File**](./game.py)

2. **K-Map Design and Logic Minimization Markdown:** A markdown document detailing the use of Karnaugh maps (K-maps) to simplify the next-state logic, illustrating the full logical reasoning and steps for minimal SOP (Sum of Products) implementation.  
   [**Link to K-Map Design Markdown**](./fsmdesign.md)

These files guide you through both the conceptual design process and a tangible simulation of the game’s behavior.

## Game Concept

**States:**
1. **IDLE:** The game awaits the player’s start command.
2. **PLAYING:** The object falls from the top to the bottom. The player can move the paddle left or right. Each time the object reaches the bottom:
   - If it’s caught by the paddle, the score increments, and the object resets for another round.
   - If it’s missed, the system transitions to GAME_OVER.
3. **GAME_OVER:** The final score is displayed until a reset command takes the system back to IDLE.

**Transitions:**
- IDLE → PLAYING on `start_button` press.
- PLAYING → GAME_OVER if the falling object is missed.
- GAME_OVER → IDLE on `reset`.

## Inputs and Outputs

**Inputs:**
- `clk`: System clock (in hardware)
- `reset`: Resets to IDLE
- `start_button`: Begins the game from IDLE
- `left_button` / `right_button`: Move the paddle horizontally

**Outputs:**
- `paddle_x`: Horizontal paddle position
- `object_x`, `object_y`: Object coordinates
- `score`: Current score
- `game_state_indicator`: Indicates current FSM state (for debugging/visualization)

In a hardware setup, these outputs would connect to LEDs, a VGA display, or other peripherals. In the provided Python simulation, they are represented as printed text or simple console interactions.

## FSM Implementation Details

1. **State Encoding:**
   - IDLE = `2'b00`
   - PLAYING = `2'b01`
   - GAME_OVER = `2'b10`

2. **Transitions:**
   In hardware, state transitions are typically described using `always` blocks and case statements in Verilog. In the Python version, conditional logic and a simple loop simulate these transitions.

3. **Object Movement:**
   A counter (in hardware) or a timing loop (in Python) moves the object downward at regular intervals, controlling difficulty and pacing.

4. **Paddle Movement:**
   Player inputs change `paddle_x` within boundary limits.

5. **Scoring:**
   On a successful catch at the bottom row, the `score` increments, demonstrating state-based event handling.

## Karnaugh Maps (K-Maps) and Logic Minimization

The [K-Map Design Markdown](./kmap_design.md) shows the step-by-step logic minimization. It presents:

- The state diagram and truth table.
- K-map derivations for next-state bits.
- Logic minimization leading to minimal SOP expressions.
- Use of don’t cares and priority encoding to achieve the simplest possible logic.

This section connects theoretical digital logic concepts to practical FSM design optimization.

## Challenges and Solutions

1. **Timing Control:**  
   Ensuring steady object movement required a reliable timing approach. In hardware, this involves a clock and counters; in the Python simulation, `time.sleep()` is used to simulate delays.

2. **Input Debouncing (Hardware Consideration):**  
   The simulation assumes clean inputs. In a hardware environment, a debouncing circuit would be necessary to ensure stable button presses.

3. **Boundary Checking:**
   Keeping the paddle and object within bounds required simple conditional checks in both hardware and software.

4. **Logic Minimization:**
   The K-Map approach ensured a cleaner, more efficient logic design. This reduces hardware complexity and can improve performance.

## Connections to Digital Logic Concepts

- **Finite State Machines:** The project exemplifies how game mechanics map neatly onto states and transitions.
- **Synchronous Design:** Synchronizing events with a clock is crucial in hardware; the Python simulation mimics this timing behavior conceptually.
- **Boolean Algebra and Minimization:** K-map simplification is a core digital logic skill, demonstrated by deriving minimal SOP forms.
- **Hierarchical Design:** The problem is broken down into modules (state control, object movement, scoring), reflecting industry best practices.

## Conclusion

This project bridges theory and practice by providing both a conceptual hardware-based FSM design and a functional Python simulation. The accompanying markdown file on K-map design underscores the logical rigor behind the scenes, showing how raw concepts like truth tables and boolean minimization shape a more elegant final design.

For hands-on experimentation, run the Python script to experience the game logic, and review the K-map markdown to appreciate the digital logic optimization that drives the FSM’s simplicity and reliability.
