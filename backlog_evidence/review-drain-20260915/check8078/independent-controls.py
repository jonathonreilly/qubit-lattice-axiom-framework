from fractions import Fraction as F
from itertools import combinations
import json,time
start=time.monotonic();checks=[]
def ok(name,v):
 assert v,name
 checks.append(name)
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)]for row in a]
def add(a,b):return [[x+y for x,y in zip(r,s)]for r,s in zip(a,b)]
def scale(a,c):return [[c*x for x in r]for r in a]
def kron(a,b):return [[x*y for x in row for y in rr]for row in a for rr in b]
I=[[1,0],[0,1]];X=[[0,1],[1,0]];Y=[[0,-1j],[1j,0]];Z=[[1,0],[0,-1]]
g=[kron(X,I),kron(Y,I),kron(Z,X),kron(Z,Y)]
for k,l,t,u in [(2,3,2,3),(5,7,-1,2)]:
 H=[[0]*4 for _ in range(4)]
 for i,e in enumerate([0,l,k,k+l]):H[i][i]=e
 B=scale(mm(g[0],add(scale(g[1],t),scale(g[2],u))),1j)
 c=B[0][0];lhs=mm(mm(B,H),B)[0][0];rhs=(t*t+u*u)*k+t*t*k+u*u*l+2*k*t*c
 ok('independent JW CAR covariance sign '+str(k),lhs==rhs and lhs==u*u*(k+l))
 ok('opposite covariance sign rejected '+str(k),lhs!=(t*t+u*u)*k+t*t*k+u*u*l-2*k*t*c)
pairs=list(combinations(range(6),2));T=[[int(not(set(a)&set(b)))for b in pairs]for a in pairs];T2=mm(T,T)
ok('common-neighbour identity',all(T2[i][j]==3+3*(i==j)-2*T[i][j]for i in range(15)for j in range(15)))
M=F(43,5);c=F(49,60);det=M*c-4;m=(M-4*c+c**3)/det
ok('moment matrix inverse',m==F(1269649,653040))
ok('moment majorant PSD throughout',M*F(3,4)>4)
ok('monotone inverse bound',2*M+16-M*M<0)
ok('quantitative direct overlap',135*m*m-180*m==F(506499805921,3158972160)>160)
# Complex Hermitian synthetic words test conjugation rather than only real matrices.
gamma=Z;R=[];W=[]
for i in range(15):
 z=complex(i%3,i%4);q=complex(i%2,1+i%3)
 R.append([[-4,z],[z.conjugate(),-9]]);W.append([[2,q],[q.conjugate(),-2]])
original=channel=0j
for a in range(15):
 for c in range(15):
  if not T[c][a]:continue
  direct=mm(R[c],R[a])[0][0]
  middle=mm(mm(mm(R[c],gamma),add(W[a],scale(W[c],-1))),R[a])[0][0]
  left=mm(mm(mm(W[c],R[c]),gamma),R[a])[0][0];right=mm(mm(mm(R[c],gamma),R[a]),W[a])[0][0]
  original+=3*direct+(middle-left-right)/2
  p=mm(gamma,add(mm(R[a],W[a]),scale(mm(W[a],R[a]),-1)))
  channel+=direct-mm(R[c],p)[0][0]
ok('complex ninety-word real Ward identity',original.real==channel.real and original.imag==0)
print(json.dumps(dict(status='PASS',checks=checks,count=len(checks),elapsed_seconds=time.monotonic()-start,scope='Independent synthetic JW CAR matrices, combinatorial Kneser identity and rational majorant; no primary or native calculation'),indent=2))
