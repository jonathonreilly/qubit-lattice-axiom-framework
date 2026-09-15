from itertools import product
from pathlib import Path
import json,time
st=time.monotonic();n=6;cases=0
# Ternary label words, independently construct reflected copies from chosen contiguous halves.
def longest(word):
 return max(sum(1 for _ in group) for group in groups(word))
def groups(word):
 # explicit cyclic runs, constant case handled first
 if len(set(word))==1:return [range(len(word))]
 start=next(i for i in range(len(word)) if word[i]!=word[i-1]);out=[];current=[]
 for k in range(len(word)):
  j=(start+k)%len(word)
  if current and word[j]!=word[current[-1]]:out.append(current);current=[]
  current.append(j)
 out.append(current);return out
for word in product(range(3),repeat=n):
 if len(set(word))==1:continue
 children=[]
 for start in range(n):
  half=[word[(start+j)%n] for j in range(n//2)];other=[word[(start+n//2+j)%n] for j in range(n//2)];a=tuple(half+half[::-1]);b=tuple(other+other[::-1]);children.extend((a,b))
  assert all(a.count(x)+b.count(x)==2*word.count(x) for x in range(3))
 assert max(map(longest,children))>longest(word);cases+=1
out={'scope':'Independent ternary length6 reflection-extension/count averaging, beyond canonical binary controls; analytical all-alphabet proof separately read','nonconstant_words':cases,'seconds':time.monotonic()-st};Path(__file__).with_name('control-reflection.json').write_text(json.dumps(out,indent=2));print(out)
