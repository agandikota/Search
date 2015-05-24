def fibo(n):
	if (n == 0):
		return 0
	elif (n <= 2):
		return 1
	return fibo(n-1) + fibo(n-2)

def matrix_multiply(A, B):
    answer = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            value = 0
            for k in range(len(B)):
                value += A[i][k] * B[k][j]
            row.append(value)
        answer.append(row)
    return answer
 
#returns the nth Neo-Fibonacci number
def neo_fib(n):
    if n <= 3:
        return 1
    n -= 3
    #note A * (x1, x2, x3) = (x1+x2+x3, x1, x2), which is what we need
    matrix = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    result = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(matrix, result)
        matrix = matrix_multiply(matrix, matrix)
        n /= 2
    answer = matrix_multiply(result, [[1], [1], [1]])[0][0]
    return answer
def fiboIter(n):
	a = 1
	b=
	i = 2

	while (i < n):
		a,b = b, a + b
		i += 1

	return b


print neo_fib(40000)
#print fiboIter(4000)
