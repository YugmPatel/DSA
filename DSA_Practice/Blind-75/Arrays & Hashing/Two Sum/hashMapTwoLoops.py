sum = {}
for i, n in enumerate(nums): 
  sum[n] = i
for i,n in enumerate(nums):
  diff = target - n
  if diff in sum and sum[diff] != i:
    return [i, sum[diff]]
