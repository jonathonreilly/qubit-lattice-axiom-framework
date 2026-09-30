"""K2: independent rebuild of TM1/TM2 (own code, PDG-style extraction with explicit angle/phase fit, not the attack's formulas).
Checks: (a) sum rules; (b) column-3 mu-tau modulus residual alone (no reflection operator) -> s23^2=1/2 and cos d = 0 for TM1?;
(c) unitary P23 + SP23 -> theta13 = 0; (d) sign of delta free (both signs)."""
import numpy as np, math
from scipy.optimize import least_squares
def pdg(th12,th13,th23,d):
    s12,c12,s13,c13,s23,c23=math.sin(th12),math.cos(th12),math.sin(th13),math.cos(th13),math.sin(th23),math.cos(th23)
    e=np.exp(1j*d)
    return np.array([[c12*c13, s12*c13, s13/e],
                     [-s12*c23-c12*s23*s13*e, c12*c23-s12*s23*s13*e, s23*c13],
                     [s12*s23-c12*c23*s13*e, -c12*s23-s12*c23*s13*e, c23*c13]])
def extract(U):
    """fit (th12,th13,th23,delta) to |U| and Jarlskog sign by nonlinear least squares over a PDG-parametrised unitary (global phases removed via |.|, J)"""
    a=np.abs(U)**2
    J=(U[0,0]*U[1,1]*np.conj(U[0,1])*np.conj(U[1,0])).imag
    s13=a[0,2]; th13=math.asin(math.sqrt(s13)); th12=math.atan2(math.sqrt(a[0,1]),math.sqrt(a[0,0])); th23=math.atan2(math.sqrt(a[1,2]),math.sqrt(a[2,2]))
    best=None
    for d0 in np.linspace(0.05,2*math.pi-0.05,24):
        f=lambda x:np.concatenate([(np.abs(pdg(th12,th13,th23,x[0]))**2-a).ravel(),[ (lambda V:(V[0,0]*V[1,1]*np.conj(V[0,1])*np.conj(V[1,0])).imag)(pdg(th12,th13,th23,x[0]))-J]])
        r=least_squares(f,[d0]); 
        if best is None or r.cost<best.cost: best=r
    return math.sin(th12)**2,s13,math.sin(th23)**2,math.degrees(best.x[0])%360,best.cost
W=np.ones(3)/math.sqrt(3); XI=np.array([2,-1,-1])/math.sqrt(6); ETA=np.array([0,1,-1])/math.sqrt(2)
def tm1(theta,psi):
    """columns: nu1 = xi ; nu2,nu3 = rotation of (W,eta) by theta with relative phase psi; order by electron content"""
    c2=math.cos(theta)*W+math.sin(theta)*np.exp(1j*psi)*ETA
    c3=-math.sin(theta)*W+math.cos(theta)*np.exp(1j*psi)*ETA
    return np.column_stack([XI,c2,c3])
def tm2(theta,psi):
    c1=math.cos(theta)*XI+math.sin(theta)*np.exp(1j*psi)*ETA
    c3=-math.sin(theta)*XI+math.cos(theta)*np.exp(1j*psi)*ETA
    return np.column_stack([c1,W,c3])
th=math.radians(15.0)
print("theta = 15 deg (pi/12): TM1 s13^2 =", (math.sin(th)**2)/3, " (2-sqrt3)/12 =", (2-math.sqrt(3))/12)
for psi in (0.3,math.pi/2,1.0,2.0,3*math.pi/2):
    U=tm1(th,psi); assert np.allclose(U.conj().T@U,np.eye(3))
    s12,s13,s23,d,c=extract(U)
    print(f"TM1 psi={psi:.3f}: s12^2={s12:.5f} s13^2={s13:.5f} s23^2={s23:.5f} delta={d:.2f}  fitcost={c:.1e}")
for psi in (math.pi/2,3*math.pi/2):
    U=tm2(math.radians(10.574),psi); s12,s13,s23,d,c=extract(U)
    print(f"TM2 psi={psi:.3f}: s12^2={s12:.5f} s13^2={s13:.5f} s23^2={s23:.5f} delta={d:.2f}")
# (b) impose only |U_mu3|^2=|U_tau3|^2 on TM1 (lane's stipulated hypothesis) and scan psi
print("\nTM1 with column-3 mu-tau modulus residual only:")
from scipy.optimize import brentq
f=lambda psi: abs(tm1(th,psi)[1,2])**2-abs(tm1(th,psi)[2,2])**2
grid=np.linspace(0,2*math.pi,721); vals=[f(p) for p in grid]
roots=[brentq(f,grid[i],grid[i+1]) for i in range(len(grid)-1) if vals[i]*vals[i+1]<0]
for r in roots:
    s12,s13,s23,d,c=extract(tm1(th,r)); print(f"  psi={r:.4f}: s23^2={s23:.6f}, delta={d:.3f} deg")
# (c) unitary V4 -> theta13
S=2*np.outer(W,W)-np.eye(3); P23=np.array([[1,0,0],[0,0,1],[0,1,0.]])
rng=np.random.default_rng(1)
A=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); A=A+A.conj().T
M=A.copy()
for g in (np.eye(3),S,P23,S@P23): M=(M+g@M@g.T)/2
w,V=np.linalg.eigh(M); print("\nunitary V4-invariant Hermitian M: |U_e j|^2 =", np.round(np.sort(np.abs(V[0])**2),6))
# (c2) SP23-unitary + reflection: commutant dimension counting
def commutant_dim(constraints_unitary, reflect):
    basis=[]
    for i in range(3):
        for j in range(3):
            for ph in (1,1j):
                E=np.zeros((3,3),complex); E[i,j]=ph; E=E+E.conj().T   # Hermitian basis element
                X=E.copy()
                for g in constraints_unitary: X=(X+g@X@g.conj().T)/2
                if reflect: X=(X+P23@X.conj()@P23)/2
                basis.append(np.concatenate([X.real.ravel(),X.imag.ravel()]))
    return np.linalg.matrix_rank(np.array(basis),tol=1e-9)
print("real dim of Hermitian M with [M,S]=0        :",commutant_dim([S],False))
print("real dim with [M,S]=0 and reflection        :",commutant_dim([S],True))
print("real dim with [M,SP23]=0                    :",commutant_dim([S@P23],False))
print("real dim with [M,SP23]=0 and reflection     :",commutant_dim([S@P23],True))
print("real dim with [M,P23]=0 (unitary)           :",commutant_dim([P23],False))
print("real dim with V4 (S,P23) unitary            :",commutant_dim([S,P23],False))
