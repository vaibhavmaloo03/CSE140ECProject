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

| Current State (S1 S0) | Sb | M | Next State (N1 N0) | Notes                         |
|------------------------|----|---|--------------------|-------------------------------|
| 00 (IDLE)              | 0  | X | 00 (IDLE)          | Stay if Sb=0                  |
| 00 (IDLE)              | 1  | X | 01 (PLAYING)       | Start game if Sb=1            |
| 01 (PLAYING)           | X  | 0 | 01 (PLAYING)       | Continue if not missed        |
| 01 (PLAYING)           | X  | 1 | 10 (GAME_OVER)     | Missed object → GAME_OVER     |
| 10 (GAME_OVER)         | X  | X | 10 (GAME_OVER)     | Remain in GAME_OVER           |

`X` = don't care.

## Karnaugh Maps for Next State Bits

We have four variables: `S1`, `S0`, `Sb`, and `M`.

- Rows: `S1 S0` in Gray code order: `00, 01, 11, 10`
- Columns: `Sb M` in Gray code order: `00, 01, 11, 10`

### K-Map for N1

| S1 S0 \ Sb M | 00 | 01 | 11 | 10 |
|--------------|----|----|----|----|
| 00 (IDLE)    | 0  | 0  | 0  | 0  |
| 01 (PLAYING) | 0  | 1  | 1  | 0  |
| 11 (UNUSED)  | X  | X  | X  | X  |
| 10 (GAME_OVER)| 1  | 1  | 1  | 1  |

**Identifying Adjacencies and Priority Encoding:**

1. **Largest Groupings First:** In K-map simplification, we prioritize finding the largest power-of-2 groupings (8,4,2) to minimize the sum-of-products (SOP) form. We have a row of all 1’s in `GAME_OVER (10)` and a row of don’t cares `(11)` which can be treated as 1’s. Together, these can form a large grouping.

2. **Using Don’t Cares:** The unused state (11) can be assigned as needed. Treating these as 1’s allows a vertical grouping of eight cells (if we consider both rows `10` and `11`) or a horizontal grouping of four cells. By applying these don’t cares wisely, we minimize the final expression.

3. **Resulting Groupings:**
   - Group 1: The entire `GAME_OVER` row (10) can be combined with the `UNUSED` row (11) as don’t cares, forming a large group. This suggests that whenever `S1=1`, `N1=1`.
   - Group 2: The cells in `PLAYING (01)` with `M=1` can form a group of two along the M=1 columns (01 and 11). This indicates that when `S0=1` and `M=1`, `N1=1`.

**Minimal SOP for N1:**
- The large grouping indicates `N1` is 1 for all conditions when `S1=1`.
- The smaller grouping from `PLAYING` row indicates `N1` can also be 1 if `S0=1` and `M=1` even if `S1=0`.

Putting it together:

N1 = S1 + (S0 & M)
This form is minimal because:
- We took advantage of the don’t cares to simplify logic.
- We formed the largest possible groups, reducing the number of product terms.

### K-Map for N0

| S1 S0 \ Sb M | 00 | 01 | 11 | 10 |
|--------------|----|----|----|----|
| 00 (IDLE)    | 0  | 0  | 1  | 1  |
| 01 (PLAYING) | 1  | 0  | 0  | 1  |
| 11 (UNUSED)  | X  | X  | X  | X  |
| 10 (GAME_OVER)| 0  | 0  | 0  | 0  |

**Identifying Adjacencies:**

1. **Focus on IDLE and PLAYING Rows:** We see that for `IDLE (00)`, N0 is set to 1 only when `Sb=1` (columns 11 and 10). For `PLAYING (01)`, N0=1 occurs when `M=0` (groups in columns 00 and 10).  
2. **Priority in Grouping:** Again, start with largest possible groups. Notice:
   - In the `IDLE` state row, a group of two can be made (columns 11 and 10) where `N0=1`. This indicates `N0` depends on `Sb` in some conditions.
   - In the `PLAYING` row, a group of two (columns 00 and 10) can be formed where `M=0`.
   - Don’t cares in `11` can help form larger groups if needed, but here the patterns are clear enough.

**Minimal SOP for N0:**
- From `IDLE (00)`, `N0=1` occurs only when `Sb=1`, which suggests `(¬S1 & ¬S0 & Sb)` contributes to `N0`. However, we notice that `¬S1 & Sb` alone distinguishes `IDLE` from other states when combined with conditions. To incorporate this insight, we look at common factors:
   - For `PLAYING (01)`, when `M=0`, `N0=1`. This suggests `(S0 & ¬M)` as part of the expression.

Combining these observations:
This minimal SOP form comes from:
- Grouping the `IDLE` row cells where `Sb=1` gives `(¬S1 & Sb)` since `S0=0` in IDLE but this condition also aligns with possible expansions using don’t cares.
- Grouping the `PLAYING` row cells where `M=0` yields `(S0 & ¬M)`.

By carefully choosing groups and utilizing don’t cares, we achieve the minimal sum-of-products form. We favored larger groups where possible, then formed the smallest number of product terms. Priority in encoding was given to identifying conditions that cover multiple adjacent 1-cells, ensuring minimal complexity.

## Conclusion

By employing Karnaugh maps and strategically using don’t cares, we derived minimal SOP expressions for the next-state logic. The process involves:

1. **Identifying State and Input Variables:** Clearly define `S1`, `S0`, `Sb`, and `M`.
2. **Filling the K-Map:** Place 1’s and 0’s according to the truth table, and assign don’t cares (X) to unused or irrelevant states.
3. **Forming Largest Possible Groups:** Prioritize 8-, 4-, and 2-cell groupings to reduce the number of product terms.  
4. **Ensuring Minimal SOP:** After grouping, extract the simplest possible boolean expressions.

For `N1`:N1 = S1 + (S0 & M)

For `N0`:N0 = (¬S1 & Sb) + (S0 & ¬M)
