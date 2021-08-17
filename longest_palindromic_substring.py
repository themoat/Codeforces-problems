class Solution:

  def solution(self,s):
  
  
  res=""
  res_len = 0
  
  
  #we are going to expand from the centre
  #so let's start iterating over the given string s
  
  
  for i in range(n):
    #let's take the case when the length of the string is odd.
    l,r = i,i
    while(l>=0 and r<len(s) and s[l] == s[r]:
          
          if (r-l+1)>res_len:
            res = s[l:r+1]
            res_len = len(res)
          
          l-=1
          r+=1
        
    l,r=i,i+1
    while(l>=0 and r<len(s) and s[l] == s[r]):
          
          if (r-l+1)>res_len:
            res = s[l:r+1]
            res_len = len(res)
          
          l-=1
          r+=1
          
    return res
          
          
          
          
          
          
          
    
    
    
    
    
  
















