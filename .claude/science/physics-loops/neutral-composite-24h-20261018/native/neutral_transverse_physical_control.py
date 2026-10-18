import numpy as np,json
LX=8;LY=8;LZ=10;N=LX*LY*LZ
idx=lambda x,y,z:((x%LX)+LX*(y%LY)+LX*LY*(z%LZ))
def bits(x,y,z,dx,dy,ell):
 return sum(1<<idx(x+u,y+v,z+w) for u,v in [(0,0),(dx,dy)] for w in range(ell))
def orbit(dx,dy,ell,Q):
 d={}
 for x in range(LX):
  for y in range(LY):
   for z in range(LZ):
    s=bits(x,y,z,dx,dy,ell);a=np.exp(-1j*(Q[0]*(x+dx/2)+Q[1]*(y+dy/2)+Q[2]*(z+(ell-1)/2)))/np.sqrt(N);assert s not in d;d[s]=a
 return d
edges=[(idx(x,y,z),idx(x+dx,y+dy,z),axis) for z in range(LZ) for y in range(LY) for x in range(LX) for dx,dy,axis in [(1,0,'x'),(0,1,'y')]]
def entry(bra,ket,Q):
 B=orbit(*bra,Q);K=orbit(*ket,Q);s=bits(0,0,0,*ket);v=0j
 for a,b,axis in edges:
  t=s^(1<<a)^(1<<b)
  if t in B:v+=np.conj(B[t])*(-1 if axis=='x' or ((s>>a)&1)!=((s>>b)&1) else 1)
 return N*K[s]*v
def run_checks():
 rows=[]
 
 for Q in [(0,np.pi,0),(np.pi/2,np.pi/2,2*np.pi/10)]:
  a,b,c=np.cos(np.array(Q)/2)
  tests=[((1,1,1),(0,1,1),-2*a),((0,2,1),(0,1,1),-2*b),((0,1,2),(0,1,1),2*c),((1,0,2),(1,0,1),-2*c)]
  for bra,ket,e in tests:
   v=entry(bra,ket,Q);assert abs(v-e)<1e-12;rows.append(dict(Q=Q,bra=bra,ket=ket,value=[v.real,v.imag],expected=e))
  # First-order C_Q source from physical bond flips, exact normalized orbit.
  for dx,dy,sign,e in [(1,0,-1,-a),(0,1,1,b)]:
   O=orbit(dx,dy,1,Q);v=0j
   for x in range(LX):
    for y in range(LY):
     for z in range(LZ):
      s=bits(x,y,z,dx,dy,1)
      # Distance-two longitudinal mismatch bond centers are z-1 and z+1 per spin.
      dc=sum(-2*np.exp(-1j*(Q[0]*(x+u)+Q[1]*(y+w)+Q[2]*(z+d))) for u,w in [(0,0),(dx,dy)] for d in [-1,1])/np.sqrt(N)
      v+=np.conj(O[s])*(-sign/8)*dc
   expected=e*np.cos(Q[2]);assert abs(v-expected)<1e-12;rows.append(dict(Q=Q,source_axis=(dx,dy),value=[v.real,v.imag],expected=expected))
 return rows
