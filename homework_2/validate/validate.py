def validate_stack_sequences(pushed, popped):
    stack = []
    i_popped = 0
    for x in pushed:
        stack.append(x)
        while stack and i_popped < len(popped) and stack[-1] == popped[i_popped]:
            stack.pop()
            i_popped += 1
    return i_popped == len(popped)
