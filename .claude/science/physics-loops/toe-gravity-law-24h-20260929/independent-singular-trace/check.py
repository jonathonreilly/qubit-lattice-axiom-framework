"""Singular-trace independent symbolic and exact finite-stencil checks."""
import sympy as s
from itertools import product
alpha,K,w=s.symbols('alpha K w',positive=True)
x,y,z=s.symbols('px py pz',real=True); pv=s.Matrix([x,y,z]); ps=(pv.T*pv)[0]
h=s.Matrix(s.symbols('hxx hyy hzz hxy hxz hyz',real=True))
P=s.Matrix(s.symbols('Pxx Pyy Pzz Pxy Pxz Pyz',real=True))
u,mu=s.symbols('u mu',real=True)
hm=s.Matrix([[h[0],h[3],h[4]],[h[3],h[1],h[5]],[h[4],h[5],h[2]]])
pm=s.Matrix([[P[0],P[3]/2,P[4]/2],[P[3]/2,P[1],P[5]/2],[P[4]/2,P[5]/2,P[2]]])
tau=s.trace(pm); ph=(pv.T*hm*pv)[0]; pp=(pv.T*pm*pv)[0]
R1=ps*s.trace(hm)-ph
R2=-ps*s.trace(hm*hm)/4+(hm*pv).dot(hm*pv)/2-ph*s.trace(hm)/2+ps*s.trace(hm)**2/4
T=(s.trace(pm*pm)-tau**2/3)/(4*alpha)
pb=lambda f,g:s.expand(sum(s.diff(f,h[a])*s.diff(g,P[a])-s.diff(f,P[a])*s.diff(g,h[a]) for a in range(6)))
C=-K*R1; H=w*(T-K*R2+u*C)+mu*tau
assert s.simplify(pb(tau,C)-2*K*ps)==0
assert s.simplify(pb(tau,H)-K*w*(2*ps*u+R1/2))==0
assert s.simplify(pb(C,H)-(K*w*(pp-ps*tau/3)/(2*alpha)-2*K*ps*mu))==0
v=s.Matrix(s.symbols('v0:6')); vm=s.Matrix([[v[0],v[3],v[4]],[v[3],v[1],v[5]],[v[4],v[5],v[2]]])
Lkin=alpha*(s.trace(vm*vm)-s.trace(vm)**2/3)/w
LH=s.hessian(Lkin,v); sv=s.Matrix([1,1,1,0,0,0])
assert LH*sv==s.zeros(6,1) and LH.rank()==5
assert s.expand(sum(s.diff(Lkin,v[j]) for j in range(3)))==0
print('A: rank-five kinetic Hessian, primary trace constraint, and general-p scalar brackets verified exactly.')
# General-p relabelling symmetry and its conserved momentum charges.
xi=s.Matrix(s.symbols('xi0:3')); gh=pv*xi.T+xi*pv.T
gv=s.Matrix([gh[0,0],gh[1,1],gh[2,2],gh[0,1],gh[0,2],gh[1,2]])
G=P.dot(gv)
assert pb(G,C)==0 and pb(G,tau)==0 and pb(G,H)==0
r=s.Matrix([[s.diff(R1,a) for a in h]])
proj=s.eye(6)-sv*r/(2*ps)
assert s.simplify(proj*proj-proj)==s.zeros(6)
assert s.simplify(r*proj)==s.zeros(1,6)
assert s.simplify(proj*sv)==s.zeros(6,1)
print('B: spatial momentum charges commute with scalar pair and Hamiltonian; Dirac mixed-bracket projector verified.')
# Include the lapse as a canonical coordinate: (tau,C,pu,chi) rank four for p!=0.
pu=s.symbols('pu'); chi=2*ps*u+R1/2
def pbu(f,g): return s.expand(pb(f,g)+s.diff(f,u)*s.diff(g,pu)-s.diff(f,pu)*s.diff(g,u))
cc=s.Matrix([[pbu(a,b) for b in [tau,C,pu,chi]] for a in [tau,C,pu,chi]])
assert s.factor(cc.det())==16*K**2*ps**4
print('C: extended lapse/trace constraint matrix determinant = 16 K^2 (p^2)^4; rank four at p!=0.')
# Aligned-p canonical reduction, with phi=0 and Pphi=-Pxi/2.
a,b,cx,cy,ell,Pa,Pb,Pcx,Pcy,Pell,k=s.symbols('a b cx cy ell Pa Pb Pcx Pcy Pell k',real=True)
sub={x:0,y:0,z:k,h[0]:a,h[1]:-a,h[2]:2*ell,h[3]:b,h[4]:cx,h[5]:cy,
P[0]:Pa/2-Pell/4,P[1]:-Pa/2-Pell/4,P[2]:Pell/2,P[3]:Pb,P[4]:Pcx,P[5]:Pcy}
Hred=s.simplify((w*(T-K*R2)).subs(sub))
expected=w*(Pa**2+Pb**2+Pcx**2+Pcy**2)/(8*alpha)+3*w*Pell**2/(32*alpha)+K*w*k*k*(a*a+b*b)/2
assert s.expand(Hred-expected)==0
omega=s.diff(Hred,Pa,2)*s.diff(Hred,a,2)
assert omega==K*w*w*k*k/(4*alpha)
print('D: reduced Hamiltonian has two TT oscillators, two free vector pairs and one free longitudinal scalar pair.')
print('   omega_TT^2 = K w^2 p^2/(4 alpha); longitudinal kinetic coefficient = 3w/(32 alpha).')
# Finite real-space staggered 3^3 torus, no Fourier diagonalization or production code.
n=3; sites=list(product(range(n),repeat=3)); index={v:i for i,v in enumerate(sites)}; nv=len(sites)
ident=s.eye(nv); shifts=[]
for j in range(3):
    tj=s.zeros(nv)
    for a,xyz in enumerate(sites):
        nxt=list(xyz);nxt[j]=(nxt[j]+1)%n;tj[a,index[tuple(nxt)]]=1
    shifts.append(tj)
fwd=[t-ident for t in shifts]; back=[ident-t.T for t in shifts]
delta=[fwd[j]*back[j] for j in range(3)]; lap=-sum(delta,s.zeros(nv))
S=s.zeros(6*nv,nv)
for j in range(3): S[j*nv:(j+1)*nv,:]=ident
R=s.zeros(nv,6*nv); A=s.zeros(6*nv,3*nv)
for j in range(3):
    R[:,j*nv:(j+1)*nv]=lap+delta[j]
    A[j*nv:(j+1)*nv,j*nv:(j+1)*nv]=2*back[j]
for ij,(i,j) in enumerate([(0,1),(0,2),(1,2)],start=3):
    R[:,ij*nv:(ij+1)*nv]=2*back[i]*back[j]
    A[ij*nv:(ij+1)*nv,j*nv:(j+1)*nv]=fwd[i]
    A[ij*nv:(ij+1)*nv,i*nv:(i+1)*nv]=fwd[j]
assert R*S==2*lap
assert R*A==s.zeros(nv,3*nv)
erank=lambda m:m.to_DM().convert_to(s.QQ).rank()
assert erank(lap)==nv-1 and erank(R)==nv-1 and erank(A)==3*(nv-1)
constraint_pb=(s.zeros(nv).row_join(2*lap)).col_join((-2*lap).row_join(s.zeros(nv)))
assert erank(constraint_pb)==2*(nv-1)
print('E: exact 3^3 staggered stencil: rank(L)=26, rank(R1)=26, rank(symgrad)=78; rank scalar Poisson matrix=52.')
# Real-space quadratic R2 Hessian assembled from its tensor polynomial.
W=s.diag(*([1]*(3*nv)+[2]*(3*nv)))
L6=s.diag(*([lap]*6)); B=-A.T*W/2
php=lap*S.T-R
Q=-W*L6/2+B.T*B-(S*php+php.T*S.T)/2+S*lap*S.T/2
assert Q==Q.T
assert S.T*Q==R/2
assert Q*A==s.zeros(6*nv,3*nv)
kin=s.diag(*([s.eye(nv)/2]*3+[s.eye(nv)/4]*3))-S*S.T/6
assert kin*S==s.zeros(6*nv,nv)
print('F: independently assembled real-space R2 Hessian satisfies S^T Q=R1/2 and Q symgrad=0; tracefree kinetic Hessian kills S.')
# all lapse profiles, including kernel; integer example N at origin is not admissible in vacuum.
N=s.zeros(nv,1);N[0]=1
assert (2*lap*N)[0]==12
assert 2*lap*s.ones(nv,1)==s.zeros(nv,1)
zero={x:0,y:0,z:0}
assert R1.subs(zero)==0 and R2.subs(zero)==0 and pb(tau,H).subs(zero)==0
print('G: delta lapse produces trace-consistency residual 12 K w at its site; uniform lapse lies in kernel. At p=0, R1=R2=0 and tau is first-class.')
print('per_element: general symbolic canonical differentiation includes independent off-diagonal momenta with full-matrix entry Pij/2.')
print('per_site: exact integer 3^3 torus certifies the trace-curvature Laplacian and a nonuniform lapse residual.')
print('per_mode: general real p identities and aligned-basis reduction prove the stated nonzero-mode class; p=0 separately checked.')
print('per_block: rank 52 scalar Poisson matrix, rank 78 symgrad, and exact R2 Hessian identities tested without primary-runner imports.')
print('lattice_wide: connected periodic-lattice proof uses the exact positive Laplacian kernel; no nonlinear lapse-weighted V2 is inferred.')
print('TOTAL: PASS=7 FAIL=0')
