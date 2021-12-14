# Chapter 1. Fundamental Algorithms

## Recursion

The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called as recursive function. Using recursive methodology, certain problems can be solved quite easily. 

**A Mathematical Interpretation**

Let us consider a problem that a programmer have to determine the sum of first n natural numbers, there are several ways of doing that but the simplest approach is simply add the numbers starting from 1 to n. So the function simply looks like, (The markdown render of Github does not support LaTeX, better to read it in [Typora](https://typora.io))

>  $f(n) = \sum_{i=1}^n i $ or `f(n) = 1 + 2 + ... + n`

but there is another mathematical approach of representing this,

> $f(n) = 1\qquad(n = 1)$ or `f(n) = 1 when n == 1`
>
> $f(n) = n + f(n-1)\qquad(n>1)$ or `f(n) = n + f(n - 1) when n > 1`

**Can recursion make code more readable?**

Umm, when you understand recursion, it could. 

> Talk is cheap, show me the code. [ref.](https://www.goodreads.com/quotes/437173-talk-is-cheap-show-me-the-code)

Here is an example for calculating [Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number).

```python
# Recursion
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

An experienced programmer should have no problem understanding the logic behind the code. As we can see, in order to compute a Fibonacci number, **Fn**, the function needs to call **Fn**-1 and **Fn**-2. **Fn**-1 recursively calls **Fn**-2 and **Fn**-3, and **Fn**-2 calls **Fn**-3 and **Fn**-4. In a nutshell, each call recursively computes two values needed to get the result until control hits the base case, which happens when **n<=2**. 

You can write a simple **main()** that accepts an integer **n** as input and outputs the **n**’th Fibonacci by calling this recursive function and see for yourself how slowly it computes as **n** gets bigger. It gets horrendously slow once **n** gets past 40 on my machine.

Here is a non-recursive version that calculates the Fibonacci number:

```python
# Non-Recursion
def fibonacci(int n):
	if n <= 2:
		return 1
	last = 1
	nextToLast = 1
	result = 1
	for i in range(3, n+1):
		result = last + nextToLast
		nextToLast = last
		last = result
	return result
```

The logic here is to keep the values already computed in variables **last** and **nextToLast** in every iteration of the **for** loop so that every Fibonacci number is computed exactly once. In this case, every single value is computed only once no matter how big **n** is.
