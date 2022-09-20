# Greedy (2022)

In the following sections, you can click the blue [hyperlinks](https://www.computerhope.com/jargon/h/hyperlink.htm) at the headings to access the problem on Online Judge (OJ) Website.

## [POJ 1700](http://poj.org/problem?id=1700) Crossing River

**Description**

A group of N people wishes to go across a river with only one boat, which can at most carry two persons. Therefore some sort of shuttle arrangement must be arranged in order to row the boat back and forth so that all people may cross. Each person has a different rowing speed; the speed of a couple is determined by the speed of the slower one. Your job is to determine a strategy that minimizes the time for these people to get across.

**Input**

The first line of the input contains a single integer T (1 <= T <= 20), the number of test cases. Then T cases follow. The first line of each case contains N, and the second line contains N integers giving the time for each people to cross the river. Each case is preceded by a blank line. There won't be more than 1000 people and nobody takes more than 100 seconds to cross.

**Output**

For each test case, print a line containing the total number of seconds required for all the N people to cross the river.

**Sample Input**

```
1
4
1 2 5 10
```

**Sample Output**

```
17
```



## \[NOIP2013 提高组] 积木大赛

### 题目描述

春春幼儿园举办了一年一度的“积木大赛”。今年比赛的内容是搭建一座宽度为 $n$ 的大厦，大厦可以看成由 $n$ 块宽度为 $1$ 的积木组成，第 $i$ 块积木的最终高度需要是 $h\_i$。

在搭建开始之前，没有任何积木（可以看成 $n$ 块高度为 $0$ 的积木）。接下来每次操作，小朋友们可以选择一段连续区间 $\[l, r]$，然后将第 $L$ 块到第 $R$ 块之间（含第 $L$ 块和第 $R$ 块）所有积木的高度分别增加 $1$。

小 M 是个聪明的小朋友，她很快想出了建造大厦的最佳策略，使得建造所需的操作次数最少。但她不是一个勤于动手的孩子，所以想请你帮忙实现这个策略，并求出最少的操作次数。

### 输入格式

包含两行，第一行包含一个整数 $n$，表示大厦的宽度。

第二行包含 $n$ 个整数，第 $i$ 个整数为 $h\_i$。

### 输出格式

建造所需的最少操作数。

### 样例 #1

#### 样例输入 #1

```
5
2 3 4 1 2
```

#### 样例输出 #1

```
5
```

### 提示

【样例解释】

其中一种可行的最佳方案，依次选择：$\[1,5]$，$ \[1,3]$，$\[2,3]$，$\[3,3]$，$ \[5,5]$。

【数据范围】

* 对于 $30%$ 的数据，有 $1 \leq n \leq 10$；
* 对于 $70%$ 的数据，有 $1 \leq n \leq 1000$；
* 对于 $100%$ 的数据，有 $1 \leq n \leq 100000$，$0 \leq h\_i \leq 10000$。
