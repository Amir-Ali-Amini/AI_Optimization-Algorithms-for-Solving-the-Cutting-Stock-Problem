
# Optimization Algorithms for Solving the Cutting Stock Problem

## Overview

The Cutting Stock Problem involves optimizing the cutting of stock materials, such as rolls of paper or sheets of metal, into specific sizes while minimizing material wastage. This problem is recognized as NP-hard in computational complexity.

In this project, we assume a paper machine can produce an unlimited number of original rolls, and we receive various requests for different roll lengths. The goal is to efficiently cut these rolls to fulfill all requests with minimal waste and the least number of rolls used.

### Problem Statement

Given ten-meter paper rolls, we need to find optimal cutting patterns to satisfy specific requests, such as cutting rolls of 3, 5, and 7 meters. The optimal solution for this example utilizes two rolls with waste minimization.

### Objectives

The code strive to achieve the following targets for different input scenarios:

1. **Input 1:** Use fewer than 56 rolls.
2. **Input 2:** Use fewer than 80 rolls.
3. **Input 3:** Use fewer than 115 rolls.
4. **Input 4:** Use fewer than 235 rolls.

### Algorithms Used

To solve the Cutting Stock Problem, we will implement the following algorithms:

- **Genetic Algorithm**: A heuristic search and optimization technique inspired by natural selection.
- **Simulated Annealing**: A probabilistic technique that explores the solution space by emulating the annealing process.
- **Hill Climbing**: A local search algorithm that continuously moves toward the direction of increasing value to find the optimum.

## Performance Summary

The project includes a comprehensive report detailing:

- **SA:**
  - Input1:

    ![SA_input1](./someResults/SA_input1.png)
  - Input4:

    ![SA_input4](./someResults/SA_input4.png)
- **Genetic Algorithm:**
  - Input1:

    ![Gen_input1](./someResults/Gen_input1.png)
  - Input4:

    ![Gen_input4](./someResults/Gen_input4.png)
- **HC:**
  - Input1:

    ![HC_input1](./someResults/HC_input1.png)
  - Input4:

    ![HC_input4](./someResults/HC_input4.png)
