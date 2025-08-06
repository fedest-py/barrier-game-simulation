# barrier-game-simulation

This Python program simulates a simple stochastic game inspired by a "barrier option" in finance. It uses Monte Carlo simulation to estimate:

- The **average amount of money won** per game
- The **probability of winning at least $1**

## Game Rules:

- Three integers (x1, x2, x3) are chosen randomly between 50 and 70 (inclusive).
- If **any number is ≥ 65**, you are "knocked out" and win $0.
- If **all are < 65**, and if `x3 > 55`, then you win `(x3 - 55)` dollars.

## Simulation:
- 100,000 games are simulated
- For each game, winnings are calculated according to the rules
- Results:
  - Average winnings (if any)
  - Probability of winning at least $1

## Concepts Demonstrated:
- Monte Carlo simulation
- Conditional logic
- Probability estimation
- Random number generation

## 🔍 Sample Output:

- Average amount earned: 1.0541
- Probability of winning at least one dollar: 0.2247
