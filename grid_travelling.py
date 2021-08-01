def memoize_grid_traveller(func):
  memo = {}
  
  def inner(m,n):
    if (m,n) not in memo:
      memo[m,n] = func(m,n)
     return memo[m,n]
  return inner


@memoize_grid_traveller
def grid_traveller(m,n):
  if m==1 or n==1:
    return 1
  
  elif m==0 or n==0:
    return 0
  
  return grid_traveller(m-1,n) + grid_traveller(m,n-1)

