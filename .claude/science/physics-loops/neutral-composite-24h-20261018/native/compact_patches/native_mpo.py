"""Exact finite open cubic compass H; one 2-state tensor per physical site."""
import itertools
import numpy as np
import quimb.tensor as qtn
I=np.eye(2);X=np.array([[0.,1],[1,0]]);A=np.array([[0.,1],[-1,0]]);Z=np.diag([1.,-1])

def geometry(shape):
 nx,ny,nz=shape
 sites=[(x,y,z) for z in range(nz) for y in range(ny) for x in range(nx)]
 ix={p:i for i,p in enumerate(sites)};bonds=[]
 for p,i in ix.items():
  for a in range(3):
   if p[a]+1<shape[a]:
    v=list(p);v[a]+=1;bonds.append((i,ix[tuple(v)],a))
 return sites,bonds

def build(shape):
 sites,bonds=geometry(shape);N=len(sites);ops=[X,A,Z];coefs=[-1,1,-1];ts=[]
 for k in range(N):
  left=['s','t']+[e for e,(i,j,a) in enumerate(bonds) if i<k<=j]
  right=['s','t']+[e for e,(i,j,a) in enumerate(bonds) if i<=k<j]
  W=np.zeros((len(left),len(right),2,2));W[0,0]=I;W[1,1]=I
  for e,(i,j,a) in enumerate(bonds):
   if i==k:W[0,right.index(e)]=coefs[a]*ops[a]
   elif j==k:W[left.index(e),1]=ops[a]
   elif i<k<j:W[left.index(e),right.index(e)]=I
  if k==0:W=W[0]
  elif k==N-1:W=W[:,1]
  ts.append(W)
 return qtn.MatrixProductOperator(ts,shape='lrud')

def expectation(a,H,b):return float(np.real(qtn.expec_TN_1D(a.H,H,b)))
def residual(g,H,e):
 h2=float(np.real(qtn.expec_TN_1D(g.H,H,H,g)))
 return np.sqrt(max(0,h2-e*e)),h2-e*e
