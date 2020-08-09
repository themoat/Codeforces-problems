"""This is a stock span, problem, an ingeniuous way of using stacks ot solve the problem. We have to here
calculate the span of stock prices at each day. Now what does the span even mean? Well, span is basically
nummber of consecutive days with prices of stock less than or equal to its cureent price or the i'th price
Mind this also, that if there are 0 prices less than current, span is actually 1, since the current price is
equal to the current price(weird, I know)."""

def calculate_span(price,span):

    n = len(price)

    stack = []
    stack.append(0)

    # Span value of first day is always 1.
    span[0] = 1

    # Calculate span values for the rest of the elements.

    for i in range(1,n):

        #Pop elements from stack while stack is not empty and top of stack is smaller than price[i]

        while(len(stack)>0 and stack[-1]<=price[i]):
            stack.pop()

            # If stack becomes empty, then price[i] is greater
            # than all elements on left of it, i.e. price[0],
            # price[1], ..price[i-1]. Else the price[i] is
            # greater than elements after top of stack
            span[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])

            # Push this element to stack
            stack.append(i)


