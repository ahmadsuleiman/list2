def count_evens(nums):
  c=0
  for i in nums:
    if i%2==0:
      c+=1
  return c

def big_diff(nums):
  ma=nums[0]
  mi=nums[0]
  for i in nums:
    if i<mi:
      mi=i
    if i>ma:
      ma=i
  return ma-mi
  
def centered_average(nums):
  c=len(nums)-2
  nums.sort()
  s=0
  for i in range(1,len(nums)-1):
    s+=nums[i]
  return s/c

def sum13(nums):
  s=0
  for i in range (0,len(nums)):
    if nums[i]==13 or i>0 and nums[i-1]==13:
      continue
    s+=nums[i]
  return s
  
def sum67(nums):
  s=0
  b=True
  for i in range (0,len(nums)):
    if nums[i]==6 and b:
      b=False
    if nums[i]==7 and not b:
      b=True
      continue
    if b:
      s+=nums[i]
  return s
  
def has22(nums):
  for i in range(0,len(nums)-1):
    if nums[i]==2 and nums[i+1]==2:
      return True
  return False