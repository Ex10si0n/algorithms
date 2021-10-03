# MPI Algorithms Interest Group

# Introduction

Lecturer: Steve Yan [![](https://img.shields.io/badge/Web-aspires.cc-blue)](https://www.aspires.cc)

Location: TBA

Time Schedule: TBA

Semester: 1

## Useful URLs

Typora: https://typora.io  ![](https://img.shields.io/badge/Web-.md-red)

Google Colab: https://colab.research.google.com  ![](https://img.shields.io/badge/Web-Python-green)

LeetCode: https://leetcode.com/problemset/all/  ![](https://img.shields.io/badge/Web-OJ-blue)

POJ: http://poj.org/problemlist  ![](https://img.shields.io/badge/Web-OJ-blue)

 OIWiki: https://oi-wiki.org ![](https://img.shields.io/badge/Web-Wiki-blue)

## Covered Topic Abstract

Fundamental, Graph Theroy, Searching, Dynamic Programming, Misc.

## How to use this repository?

Clone via HTTPS using following command or Click `Code` then `Download ZIP`.

```bash
git clone https://github.com/Ex10si0n/MPI-Interest-Group.git
```

You can open `README.md` (Markdown File: open via [Typora](https://typora.io) or notepad.exe) locally or on [this](https://github.com/Ex10si0n/MPI-Interest-Group) page.

## About this lecture

This lecture will specifically focus on the Algorithms implementation. My example code will be demostrated in Python, but you can adopt any kind of programming language if you prefer.

No slides are distributed (cuz. I do not regard slides as effecient format to display codes) but all of the codes and explanations are showed on this `README.md`.

**Following topics will be covered in the Interest Group**

* Fundamental
  * `Greedy (贪心)` ![](https://img.shields.io/badge/-basic-red)
  * `Binary Search (二分)` ![](https://img.shields.io/badge/-basic-red)
  * `Recursion (递归)` ![](https://img.shields.io/badge/-basic-red)
  * `Data Structure (数据结构) ` ![](https://img.shields.io/badge/-basic-red)
    * Linear Structure
      * `Queue (队列)`
      * `Stack (栈)`
    * Generic Tree
      * `Tree (树)`
      * `Binary Tree (二叉树)` 
      * `Linear Structure (maintained by Tree) (由树维护的线性结构)`
    * Generic Graph
      * `Graph (图)`
      * `Directed Graph (有向图)`
      * `Bipartite Graph (二分图)`
* Graph Theory  (图论)
  * `Minimal Spanning Tree (最小生成树)`
  * `Shortest Path (最短路径)`
    * `Floyed-Warshall`
    * `Dijkstra`
    * `SPFA`
  * `Network Flow (网络流)`
    * `Ford-Fulkerson (最大流算法)`

# Chapter 1. Fundamental Algorithms

## Greedy

Greedy Algorithms can be adopted when a specific problem can be proofed that when locally optimal choice in each stages can produce a globally optimal choice. But in many problems, all stages is optimized does not means that it will be globally optimized.

### [LC11](https://leetcode.com/problems/container-with-most-water/) Container With Most Water

Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)`and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

**Example 1:**

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Constraints:**

- `n == height.length`
- `2 <= n <= 105`
- `0 <= height[i] <= 104`

#### Sol.

![Picture0.png](https://pic.leetcode-cn.com/1628780627-VtSmcP-Picture0.png)

* If in Brute Force way, we can encount `n * n` possibilities then calculate each area to get the max area.
* Greedy Approach can optimize the complexity from `O(n^2)` to `O(n)`
  * Let `i` be the first line and `j` be the last line.
  * For each pair of lines selected, the covered area size is `A(i, j) = min(height_i, height_j) * (j - i)`.
  * If we move the longer line inner, `min(height_i', height_j') <= min(height_i, height_j)`
  * If we move the shorter line inner, `min(height_i', height_j') > or <= min(height_i, height_j)`
  * If the area will be larger, the contribution of updating lines will be positive.
  * Hence, we can only encount only `n - 1` times then we can get the largest area.
  * Ref. https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/

```python
class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, height[i] * (j - i))
                i += 1
            else:
                ans = max(ans, height[j] * (j - i))
                j -= 1
        return ans
```

### [LC55](https://leetcode.com/problems/jump-game/) Jump Game

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return `true` *if you can reach the last index, or* `false` *otherwise*.

**Example 1:**

```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

**Example 2:**

```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

**Constraints:**

- `1 <= nums.length <= 104`
- `0 <= nums[i] <= 105`

