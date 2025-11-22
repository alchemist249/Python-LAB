stack=[]
queue={"queue": False}

def push(x):
    stack.append(x)
    if x%2==0:
        queue["queue"]=True
    else:
        queue["queue"]=False

def pop():
    if not stack:
        return None
    if queue["queue"]:
        return stack.pop(0)
    else:
        return stack.pop()

    
push(2)
push(3)
print(stack)
push(4)
pop()
print(stack)
push(5)
print(stack)
pop()
push(22)
pop()
print(stack)
push(33)
print(stack)
push(23)
print(stack)