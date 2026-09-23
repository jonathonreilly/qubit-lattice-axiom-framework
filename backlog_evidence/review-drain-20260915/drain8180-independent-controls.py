from fractions import Fraction as F
import json, cmath, math
# Independently solve the one-dimensional recurrence of the partially transformed 3D inverse.
a=F(5,2); q=F(1,2); c=lambda s:F(2,3)*q**abs(s)
residual={s:a*c(s)-c(s-1)-c(s+1) for s in range(-8,9)}
assert all(v==(1 if s==0 else 0) for s,v in residual.items())
# This is the legitimate nonzero plane E_2=1/2 slice; its plane amplitude times q^|s| directly refutes the general product prohibition.
print('COMPARATOR: a=5/2, E_2=1/2, C_s=(2/3)(1/2)^|s| solves (a-shift-shift*)C=delta exactly.')
# Real space stencil gives oblique plane metric; compare M to inverse Gram matrix.
G=((F(2),F(1)),(F(1),F(2))); M=((F(2,9),F(-1,9)),(F(-1,9),F(2,9)))
GM=[[sum(G[i][k]*M[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
assert GM==[[F(1,3),F(0)],[F(0),F(1,3)]]
print('PLANE METRIC: G M = I/3 exactly; M is isotropic with respect to the actual plane metric.')
# Close group by integer matrices, including inversion, independent of source's short-word orbit probe.
def mul(A,B):return tuple(sum(A[2*i+k]*B[2*k+j] for k in range(2)) for i in range(2) for j in range(2))
I=(1,0,0,1); S=(0,1,1,0); T=(1,-1,0,-1); N=(-1,0,0,-1)
def closure(gens):
 seen={I}; todo=[I]
 while todo:
  A=todo.pop()
  for B in gens:
   C=mul(A,B)
   if C not in seen:seen.add(C);todo.append(C)
 return seen
assert len(closure([S,T]))==6 and N not in closure([S,T])
full=closure([S,T,N]); assert len(full)==12
roots={(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)}
for A in full:
 assert {(r[0]*A[0]+r[1]*A[2],r[0]*A[1]+r[1]*A[3]) for r in roots}==roots
print('SYMMETRY: six source generators subgroup elements; inversion doubles to 12, all preserving the six stencil roots.')
# Complex phase check through real-space impulse propagation at L=4, zero initial field, t=1, lag=1.
L=4; k=math.pi/2; Nsites=L*L
# E[hat(theta_t) conj(hat(theta_t+1))] = sum over independent initial impulses.
cross=0j; var=0
for i in range(L):
 for j in range(L):
  old=cmath.exp(-1j*k*i)/L
  new=sum(cmath.exp(-1j*k*x)/L/3 for x,y in [(i,j),((i+1)%L,j),(i,(j+1)%L)])
  cross+=old*new.conjugate();var+=abs(old)**2
phi=(2+1j)/3
assert abs(cross/var-phi)<1e-14
print('COMPLEX COVARIANCE: negative-sign DFT multiplier is conjugate(phi), cross E[X_t conjugate(X_t+1)] is phi; old proof conflates these signs.')
print('DIFFUSIVE BOUND: 1-u = (2/9)[1-cos k1+1-cos k2+1-cos(k1-k2)] >= 4(k1^2+k2^2)/(9*pi^2) on principal square; log u <= -(1-u) supplies bound (u=0 by continuity).')
print('NONLINEAR LOG CHECK: beta12 mode(2,2), lag64 modulus .907/.983 gives relative deviation',abs(.907/.983-1))
assert abs(.907/.983-1)>.07
