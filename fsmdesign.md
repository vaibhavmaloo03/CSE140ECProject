# State Diagram, Truth Table, and K-Maps

## State Encoding

- `IDLE = 00`
- `PLAYING = 01`
- `GAME_OVER = 10`
- `11` is unused.

For inputs, we consider:
- `Sb` = start_button
- `M` = missed condition (object at bottom and not caught)

## State Diagram
![IMG_248C04C0BABD-1](https://github.com/user-attachments/assets/696b4f07-9470-4244-be24-9e1d50821bbd)



## Truth Table for Next State

| Current State (S1 S0) | Sb | M | Next State (N1 N0) | Notes                       |
|------------------------|----|---|--------------------|-----------------------------|
| 00 (IDLE)              | 0  | X | 00 (IDLE)          | Remain in IDLE if Sb=0      |
| 00 (IDLE)              | 1  | X | 01 (PLAYING)       | Start game on Sb=1          |
| 01 (PLAYING)           | X  | 0 | 01 (PLAYING)       | Continue playing if not missed |
| 01 (PLAYING)           | X  | 1 | 10 (GAME_OVER)     | Missed object → GAME_OVER   |
| 10 (GAME_OVER)         | X  | X | 10 (GAME_OVER)     | Remain in GAME_OVER         |

`X` = don't care.

## Karnaugh Maps for Next State Bits

We have four variables: `S1`, `S0`, `Sb`, `M`.

- Rows: `S1 S0` in order `00, 01, 11, 10`
- Columns: `Sb M` in order `00, 01, 11, 10`

### K-Map for N1

| S1 S0 \ Sb M | 00 | 01 | 11 | 10 |
|--------------|----|----|----|----|
| 00 (IDLE)    | 0  | 0  | 0  | 0  |
| 01 (PLAYING) | 0  | 1  | 1  | 0  |
| 11 (UNUSED)  | X  | X  | X  | X  |
| 10 (GAME_OVER)| 1  | 1  | 1  | 1  |

**Possible Simplification:**

