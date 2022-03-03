set1={1,2,3,4,5,6,7,8,9}
print(f"\n initial set1= {set1}")
set1.remove(1)
print(f"set1 after the removal of 1 from the original set= {set1}")
set1.discard(2)
print(f"set1 after the discard of 2 from set1= {set1}")
set1.discard(2)
print(f"set1 after the discard of already discarded number 2 from set1 ={set1}")