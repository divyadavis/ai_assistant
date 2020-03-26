class Evaluate: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
  
    # The main function that converts given infix expression 
    # to postfix expression 
    def evaluatePostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        for i in exp: 
              
            # If the scanned character is an operand 
            # (number here) push it to the stack 
            if isinstance(i, float): 
                self.push(i) 
  
            # If the scanned character is an operator, 
            # pop two elements from stack and apply it. 
            else: 
                val1 = self.pop() 
                print(type(val1))
                val2 = self.pop()
                print(type(val2))
                print(type(i))
                if i == '+':
                    result = float(val2) + float(val1)
                elif i == '-':
                    result = float(val2) - float(val1)
                elif i == '*':          
                    result = float(val2) * float(val1)
            
                elif i == '/':
                    result = float(val2) / float(val1)
            
                self.push(str(result)) 
  
        return float(self.pop()) 
                  
  
              
# Driver program to test above function 
exp = [45.0, 56.0, '+']
obj = Evaluate(len(exp)) 
print ("postfix evaluation: %d"%(obj.evaluatePostfix(exp)))