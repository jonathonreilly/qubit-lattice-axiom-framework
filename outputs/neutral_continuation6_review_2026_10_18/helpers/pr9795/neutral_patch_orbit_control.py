from itertools import product
import json
rows=[]
for m in range(2,7):
 patterns=set();minimum=m*m
 for bits in product([0,1],repeat=2*m-1):
  a=bits[:m];b=bits[m:]+(0,)
  mask=sum((a[x]^b[y])<<(x*m+y) for x in range(m) for y in range(m))
  assert all(((mask>>(x*m+y))^(mask>>((x+1)*m+y))^(mask>>(x*m+y+1))^(mask>>((x+1)*m+y+1)))&1==0 for x in range(m-1) for y in range(m-1))
  patterns.add(mask)
  if mask:minimum=min(minimum,mask.bit_count())
 assert len(patterns)==2**(2*m-1) and minimum==m
 rows.append(dict(m=m,orbit_size=len(patterns),minimum_column_difference=minimum,minimum_physical_difference_allowing_singletons=4*m-2,order4_flip_limit=8))
print(json.dumps(dict(status='pass',rows=rows,scope='exact finite flat-pattern subgroup and locality count; not a microscopic spectrum simulation')))
