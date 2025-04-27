# Inventory Management System Enhancement

## Background
This project was developed for a coding interview scenario with a retail company seeking to improve its inventory management system. The company requires a specific feature: for every product with a stock count of zero, the system must duplicate that entry to represent an order for restocking, while shifting the subsequent product entries to the right. All modifications must happen in place within the inventory array.

## Objective
Create an efficient algorithm that:
- Duplicates each occurrence of zero (out-of-stock product) in the inventory list.
- Shifts the following elements to the right.
- Performs the operation in place without using additional arrays.
- Ensures elements beyond the original array length remain unchanged.

## Problem Statement
Given an array `inventory` where each element is an integer representing the stock count of a product:
- Duplicate each zero and shift subsequent elements right.
- Perform modifications **in place**.
- Do not add extra elements beyond the original array size.

## Input Format
- An array `inventory` of integers representing product stock counts.

## Output Format
- No new array is returned; the input array is modified in place.

## Examples

**Example 1:**
```
Input: inventory = [4,0,1,3,0,2,5,0]
Output: [4,0,0,1,3,0,0,2]
Explanation: Each zero is duplicated, shifting elements rightward.
```

**Example 2:**
```
Input: inventory = [3,2,1]
Output: [3,2,1]
Explanation: No out-of-stock products; inventory remains unchanged.
```

## Requirements

### Github Submission
- Source code
- Diagrams/flowcharts to explain the solution
- List of clarifying questions
- Unit test cases (minimum 3 normal cases and 3 edge cases)
- Time and space complexity analysis

### Video Submission
- Record a video showing your screen and your face
- Talk through your coding and diagramming process
- Demonstrate running test cases
- Present time and space complexity analysis
- Discuss any optimizations and trade-offs

### Evaluation Criteria
- Algorithm accuracy and efficiency
- Clear understanding of the business need
- Communication clarity
- Code readability and use of appropriate data structures
- Understanding of time and space complexities
