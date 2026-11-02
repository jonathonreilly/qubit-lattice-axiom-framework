"""Independent exact controls, written before inspecting the author checker.
Finite geometry/algebra evidence; not a continuum or mass-gap proof.
"""
from itertools import combinations, permutations, product
from collections import deque
from fractions import Fraction as Q
import json
import sympy as s

report = {}
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def unit(j): return tuple(int(i==j) for i in range(4))
def height(x,j,k,sgn): return x[j]+sgn*x[k]
def mirror(x,j,k,sgn):
    h=height(x,j,k,sgn); z=list(x); z[j]-=h; z[k]-=sgn*h; return tuple(z)

# General proof reduces to nearest-neighbor height increments; this samples
# every axis pair and both diagonal normals without author helper routines.
planes=[(j,k,sgn) for j,k in combinations(range(4),2) for sgn in (-1,1)]
count=cross=0
for b in product(range(-1,2),repeat=4):
 for a,c in combinations(range(4),2):
  square=[b,add(b,unit(a)),add(add(b,unit(a)),unit(c)),add(b,unit(c))]
  for j,k,sgn in planes:
   count+=1; hs=[height(x,j,k,sgn) for x in square]
   if min(hs)<0<max(hs):
    cross+=1
    assert sorted(hs)==[-1,0,0,1]
    assert set((a,c))==set((j,k))
    fixed=[i for i,h in enumerate(hs) if h==0]
    assert (fixed[0]-fixed[1])%4==2
    assert {mirror(x,j,k,sgn) for x in square}==set(square)
    assert all(mirror(square[i],j,k,sgn)==square[i] for i in fixed)
report['diagonal_plaquette_geometry']={'pairs':count,'straddlers':cross}

# Enumerate actual complete-axial contours, including the straight middle leg.
def segment(x,target,order):
 out=[x]; z=list(x)
 for a in order:
  while z[a]!=target[a]:
   z[a]+=1 if target[a]>z[a] else -1;out.append(tuple(z))
 return out
orders=list(permutations(range(4)))
paths=vertices=0; boundary_witness=None
for L in (3,5):
 r=(L-1)//2;c=(L,0,0,0)
 for sgn in (-1,1):
  for mu in range(4):
   d=tuple(c[i]+L*(i==mu) for i in range(4))
   if height(d,0,1,sgn)<=0:continue
   for y0 in product(range(-r,r+1),repeat=4):
    y=add(c,y0);yp=tuple(y[i]+L*(i==mu) for i in range(4))
    for order in orders:
     contour=segment(c,y,order)+segment(y,yp,(mu,))+list(reversed(segment(d,yp,order)))
     paths+=1;vertices+=len(contour)
     assert min(height(z,0,1,sgn) for z in contour)>=1
     assert all(all(abs(z[i]-c[i])<=r for i in range(4)) or all(abs(z[i]-d[i])<=r for i in range(4)) for z in contour)
 y=(-r,r,0,0);d=(0,0,L,0);yp=(-r,r,L,0)
 contour=segment((0,0,0,0),y,(1,0,2,3))+segment(y,yp,(2,))+list(reversed(segment(d,yp,(1,0,2,3))))
 assert min(height(z,0,1,-1) for z in contour)==-(L-1)
 boundary_witness={'L':L,'point':y,'height':height(y,0,1,-1)}
report['actual_contours']={'paths':paths,'vertex_visits':vertices,'boundary_witness':boundary_witness}

clover=set()
for a,b in combinations(range(4),2):
 for da,db in product((0,-1),repeat=2):
  root=tuple(da*(i==a)+db*(i==b) for i in range(4))
  clover.update((root,add(root,unit(a)),add(root,unit(b)),add(add(root,unit(a)),unit(b))))
radii=[max(abs(height(z,*p)) for z in clover) for p in planes]
assert set(radii)=={2}
# A geometric plaquette belongs to four site clovers and two ordered axes.
f=s.symbols('f0:4');coefficient=sum(2*x/s.Integer(4) for x in f)
assert coefficient==sum(f)/2
report['clover']={'diagonal_radii':radii,'plaquette_source_coefficient':str(coefficient),'constant_source_sum_multiplier':2}

# SU(2) identity via quaternion multiplication, independent of matrix products.
def qm(a,b):
 w,x,y,z=a;v,r,t,u=b
 return (w*v-x*r-y*t-z*u,w*r+x*v+y*u-z*t,w*t-x*u+y*v+z*r,w*u+x*t-y*r+z*v)
def qc(a):return (a[0],-a[1],-a[2],-a[3])
a=(Q(3,5),Q(4,5),0,0);b=(Q(5,13),0,Q(12,13),0)
c=(Q(8,17),0,0,Q(15,17));d=(Q(7,25),Q(24,25),0,0)
P=qm(a,b);N=qm(c,d)
correct=2*qm(P,qc(N))[0];dot=2*sum(x*y for x,y in zip(P,N));wrong=2*qm(P,N)[0]
assert correct==dot and wrong!=correct
# exp(lambda Re tr(U_i U_j^dagger)) for {I,-I}; lambda=+/- log(2)/2.
pos=s.Matrix([[2,s.Rational(1,2)],[s.Rational(1,2),2]])
neg=s.Matrix([[s.Rational(1,2),2],[2,s.Rational(1,2)]])
v=s.Matrix([1,-1]);assert (v.T*pos*v)[0]>0 and (v.T*neg*v)[0]<0
report['crossing_orientation']={'correct':str(correct),'wrong':str(wrong),'positive_quadratic':str((v.T*pos*v)[0]),'negative_quadratic':str((v.T*neg*v)[0])}

# Normalized product kernels with fine +/-1 variables and no interaction.
# k(v|u)=(1+alpha*v*u)/2 is reflection covariant, each sum_v k=1.
alpha=Q(1,2);fine=list(product((-1,1),repeat=2));coarse=fine
def kernel(v,u):return (1+alpha*v[0]*u[0])*(1+alpha*v[1]*u[1])/4
assert all(sum(kernel(v,u) for v in coarse)==1 for u in fine)
marg=[sum(Q(1,4)*kernel(v,u) for v in coarse) for u in fine]
assert marg==[Q(1,4)]*4
fixed=(1,-1);den=sum(Q(1,4)*kernel(fixed,u) for u in fine)
form=sum(Q(1,4)*kernel(fixed,u)*u[0]*u[1] for u in fine)/den
assert form==-alpha*alpha<0
coarse_reflected=sum(Q(1,4)*kernel(v,u)*v[0]*v[1] for u in fine for v in coarse)
assert coarse_reflected==0
report['normalizer_control']={'integrated_fine_marginal':list(map(str,marg)),'fixed_coarse_RP_form':str(form),'integrated_coarse_RP_form':str(coarse_reflected)}

# Torus covariance via six symmetry orbits, solving Green equations on orbits.
# This is neither a 16x16 inversion nor a Fourier sum.
def orbit(t,x):return tuple(sorted((min(t%4,(-t)%4),min(x%4,(-x)%4))))
orbits=sorted({orbit(t,x) for t,x in product(range(4),repeat=2)})
z=s.symbols('z0:'+str(len(orbits)));zmap=dict(zip(orbits,z));eq=[]
for t,x in orbits:
 eq.append(5*zmap[orbit(t,x)]-sum(zmap[orbit(t+dt,x+dx)] for dt,dx in ((1,0),(-1,0),(0,1),(0,-1)))-int((t,x)==(0,0)))
sol=s.solve(eq,z,dict=True);assert len(sol)==1
C=lambda t,x:sol[0][zmap[orbit(t,x)]]
sites=[(1,0),(3,1)]
G=s.Matrix([[C(a[1]-b[0],a[0]-b[1]) for b in sites] for a in sites])
assert G.det()<0
coord_sites=[(1,x) for x in range(4)]
Gc=s.Matrix([[C(-a[0]-b[0],a[1]-b[1]) for b in coord_sites] for a in coord_sites])
assert all(ev>=0 for ev in Gc.eigenvals())
remaining={(t,x) for t,x in product(range(4),repeat=2) if t!=x};todo=deque([next(iter(remaining))]);seen=set(todo)
while todo:
 t,x=todo.popleft()
 for dt,dx in ((1,0),(-1,0),(0,1),(0,-1)):
  nb=((t+dt)%4,(x+dx)%4)
  if nb in remaining and nb not in seen:seen.add(nb);todo.append(nb)
assert seen==remaining
report['periodic_scalar_control']={'orbit_values':{str(o):str(C(*o)) for o in orbits},'diagonal_gram':str(G),'determinant':str(G.det()),'coordinate_eigenvalues':{str(e):m for e,m in Gc.eigenvals().items()},'connected_nonfixed_sites':len(seen)}

# Independent rational rotation: cosine 5/13, sine 12/13, not author's 3/5.
p=s.symbols('p0:4');rot=(s.Rational(5,13)*p[0]-s.Rational(12,13)*p[1],s.Rational(12,13)*p[0]+s.Rational(5,13)*p[1],p[2],p[3])
q=sum(x**4 for x in p);qr=sum(x**4 for x in rot);denom=sum(x*x for x in p)+1
numer=s.expand(qr**2-q**2);pole={p[0]:s.I,p[1]:0,p[2]:0,p[3]:0};pole_value=s.expand(numer.subs(pole))
assert denom.subs(pole)==0 and pole_value!=0
quot,rem=s.div(numer,denom,*p);assert rem!=0
iso=sum(x*x for x in p)**2;iso_r=sum(x*x for x in rot)**2
assert s.expand(iso_r**2-iso**2)==0
for j,k,sgn in planes:
 pp=list(p);pp[j]=-sgn*p[k];pp[k]=-sgn*p[j]
 assert s.expand(sum(x**4 for x in pp)-q)==0
for j in range(4):
 pp=list(p);pp[j]=-pp[j];assert s.expand(sum(x**4 for x in pp)-q)==0
report['derivative_gaussian']={'rational_rotation':'5/13, 12/13','complex_pole_numerator':str(pole_value),'polynomial_remainder_nonzero':rem!=0,'isotropic_control':'exact zero','mirror_identities':16}

# Cone-coordinate algebra independently verifies half factors in the Laplace step.
v,u,omega,momentum=s.symbols('v u omega momentum',real=True)
t=(v+u)/2;x=(v-u)/2
assert s.expand(-omega*t+s.I*momentum*x-(-((omega-s.I*momentum)/2)*v-((omega+s.I*momentum)/2)*u))==0
report['spectral_algebra']={'v_u_transform':'exact half factors; analytic proof required','mass_gap_proved':False,'full_spatial_cone_proved':False}
print(json.dumps(report,indent=2,sort_keys=True))
