import mpmath as mp,json,time
from itertools import combinations
iv=mp.iv;iv.dps=30
rays=[tuple(int(i in Q) for i in range(4)) for Q in combinations(range(4),2)]
def graph(F):
 states=[(0,0,0,0)]+rays;idx={h:i for i,h in enumerate(states)};edges=[(i,j,'x' if x!=u else 'y') for i,(x,y) in enumerate(F) for j,(u,v) in enumerate(F) if i<j and abs(x-u)+abs(y-v)==1];terms=[];tails=[]
 for h,i in idx.items():
  for a,b,axis in edges:
   for z in set([h[a],h[a]+1])&set([h[b],h[b]+1]):
    v=list(h);sa=1 if z>h[a] else -1;sb=1 if z>h[b] else -1;v[a]+=sa;v[b]+=sb;m=min(v);v=tuple(x-m for x in v);sign=-1 if axis=='x' else sa*sb
    if v in idx:terms.append((idx[v],i,sign,sa+sb))
    elif i and max(v)==2:tails.append((i-1,sign,sa+sb))
 return terms,tails

def cert(terms,tails,j):
 k=iv.pi*(iv.mpf(j)/128-1);phase={n:iv.exp(-iv.j*k*n/4) for n in [-2,0,2]};H=[[iv.mpc(0) for _ in range(7)] for _ in range(7)];t=[iv.mpc(0) for _ in range(6)]
 for a,b,s,n in terms:H[a][b]+=s*phase[n]
 for a,s,n in tails:t[a]+=s*phase[n]
 for a in range(7):H[a][a]+=iv.mpf(19)/4
 for a in range(6):q=t[a].real**2+t[a].imag**2;H[a+1][a+1]+=(-5+iv.sqrt(25-4*q))/2
 # Verified interval LDL*: positivity of allrealpivot intervals certifiespositiveM-.25I.
 L=[[iv.mpc(0) for _ in range(7)] for _ in range(7)];d=[]
 for a in range(7):
  pivot=H[a][a].real
  for b in range(a):pivot-=(L[a][b].real**2+L[a][b].imag**2)*d[b]
  assert pivot.a>0,(j,a,pivot);d.append(pivot);L[a][a]=iv.mpc(1)
  for b in range(a+1,7):
   v=H[b][a]
   for c in range(a):v-=L[b][c]*iv.mpc(L[a][c].real,-L[a][c].imag)*d[c]
   L[b][a]=v/pivot
 return min(float(x.a) for x in d)

def run_all():
 rows=[]
 for F in combinations([(x,y) for y in range(3) for x in range(2)],4):
  terms,tails=graph(F);m=min(cert(terms,tails,j) for j in range(257));rows.append(dict(F=F,min_pivot_lower_display=m))
 return rows
