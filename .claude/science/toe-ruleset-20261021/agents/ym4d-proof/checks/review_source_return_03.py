from fractions import Fraction as F
import json
n=3
a=[({i},{(i,i):F(1)}) for i in range(n)]
b=[({i,3},{(i,i):F(1)}) for i in range(n)]
def norms(atoms):
 rows=[F(0)]*n;cols=[F(0)]*n;marked={v:F(0) for v in range(4)}
 for label,matrix in atoms:
  mass=sum(abs(x) for x in matrix.values())
  for (i,j),x in matrix.items():rows[i]+=abs(x);cols[j]+=abs(x)
  for v in label:marked[v]+=mass
 return max(rows+cols),max(marked.values())
product=[]
for la,aa in a:
 for lb,bb in b:
  matrix={}
  for (i,k),x in aa.items():
   for (kk,j),y in bb.items():
    if k==kk:matrix[i,j]=matrix.get((i,j),F(0))+x*y
  if matrix:product.append((la|lb,matrix))
ma,ba=norms(a);mb,bb=norms(b);mc,bc=norms(product)
checks={
 'supports_connected':all(len(label)==1 or 3 in label for label,matrix in a+b+product),
 'supports_contain_endpoints':all(i in label and j in label for label,matrix in a+b+product for i,j in matrix),
 'two_term_incidence_bound':bc<=ba*mb+ma*bb,
 'omitted_marked_right_term_rejected':bc>ba*mb,
}
assert all(checks.values())
print(json.dumps({'checks':checks,'M_A':str(ma),'B_A':str(ba),'M_B':str(mb),'B_B':str(bb),'B_AB':str(bc),'one_term_bound':str(ba*mb),'two_term_bound':str(ba*mb+ma*bb),'all_passed':all(checks.values())},indent=2))
