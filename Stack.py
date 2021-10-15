stack = []

message = "Hello World......"
for i in message:
    print(i)
    stack.append(i)

print('Initial stack')
print(stack)

print('\nElements popped from stack:')
for i in range(0,len(stack)):
    print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

