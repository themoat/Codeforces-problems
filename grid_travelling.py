def memoize_grid_traveller(func):
  memo = {}
  key = m+','+n
  
  def inner(m,n):
    if key not in memo:
      memo[key] = func(m,n)
     return memo[key]
  return inner


@memoize_grid_traveller
def grid_traveller(m,n):
  if m==1 or n==1:
    return 1
  
  elif m==0 or n==0:
    return 0
  
  return grid_traveller(m-1,n) + grid_traveller(m,n-1)




#or other simple object oriented way to do this


class Solution():
  
  def __init__(self):
    self.memo={}
    
    
  def grid_traveller(self,int(m),int(n)):
    
    if m==1 or n==1:
      return 1
    
    elif m==0 or n==0:
      return 0
    
    elif (m,n) in self.memo:
      return self.memo[(m,n)]

    else:
      self.memo[(m,n)] = self.grid_traveller(m-1,n) + self.grid_traveller(m,n-1)
      return self.memo[(m,n)]
    
    
  
      

