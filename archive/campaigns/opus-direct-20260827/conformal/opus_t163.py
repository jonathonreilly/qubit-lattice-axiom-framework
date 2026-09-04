"""T163 - DOES COMPLETE POSITIVITY BOUND THE PROPAGATION SPEED?

R95/R96: the curl channel gives a spectral splitting linear in |k| with slope
delta/3 -- the framework's candidate speed.  R94 bounded the GRADIENT coefficient
gamma_0 but never bounded DELTA on its own.  If CP bounds delta, the framework has
a DERIVED SPEED LIMIT, which would be the sharpest possible statement of a light
cone from axiom content.

And R98 raises the companion question.  The rule is a CPTP channel, and channels
CONTRACT: for the pure V channel v -> alpha v, so det rho = 1/4 - |v|^2 INCREASES
toward the maximally mixed value 1/4.  Records require det rho = 0 (null).  So the
rule drives states AWAY from the light cone while the Record axiom pulls them back
onto it -- two opposing processes, exactly as the axioms separate Admissibility
from Record.  Quantify the trade-off.

Three measurements:
 (1) the CP bound on delta alone (alpha = beta = 0): the maximum curl, hence the
     maximum slope delta/3 of the splitting;
 (2) the joint CP region in (alpha, delta) -- how much speed costs how much
     coherence;
 (3) purity flow: how det rho moves under one application, versus alpha.

CONTROLS: delta = 0 must be CP for every alpha in [-1/3,1] (R94); and a delta
beyond the bound must be rejected, or the bound is vacuous."""
import numpy as np
S=[np.array([[0,1],[1,0]],dtype=complex),
   np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
I2=np.eye(2,dtype=complex)
def choi(M,gam):
    def Psi(X):
        a0=np.trace(X)/2
        a=np.array([np.trace(X@S[k])/2 for k in range(3)])
        b=M@a+gam*a0
        return a0*I2+sum(b[k]*S[k] for k in range(3))
    C=np.zeros((4,4),dtype=complex)
    for i in range(2):
        for j in range(2):
            E=np.zeros((2,2),dtype=complex); E[i,j]=1
            C[2*i:2*i+2,2*j:2*j+2]=Psi(E)
    return C
def is_cp(M,gam=np.zeros(3)):
    C=choi(M,gam); return np.linalg.eigvalsh(0.5*(C+C.conj().T))[0]>-1e-10
n=np.array([0,0,1.0])
def Mof(al,be,de):
    P=np.outer(n,n); X=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    return al*np.eye(3)+be*P+de*X
print("T163  does complete positivity bound the propagation speed?")
print()
print("   CONTROLS")
print(f"      delta=0, alpha=0.5   CP? {is_cp(Mof(0.5,0,0))}   (must be True)")
print(f"      delta=0, alpha=-1/3  CP? {is_cp(Mof(-1/3,0,0))}  (must be True)")
print(f"      delta=5, alpha=0     CP? {is_cp(Mof(0,0,5))}   (must be False, or the bound is vacuous)")
print()
print("(1) maximum delta at each alpha (beta = 0)")
print(f"   {'alpha':>8} {'max |delta|':>13} {'=> max slope delta/3':>22}")
rows=[]
for al in (1.0,0.8,0.5,0.25,0.0,-0.25,-1/3):
    lo,hi=0.0,5.0
    for _ in range(60):
        mid=0.5*(lo+hi)
        if is_cp(Mof(al,0,mid)): lo=mid
        else: hi=mid
    d=0.5*(lo+hi); rows.append((al,d))
    print(f"   {al:8.4f} {d:13.6f} {d/3:22.6f}")
print()
A=np.array([r[0] for r in rows]); D=np.array([r[1] for r in rows])
print("   closed forms tested against the measured bound:")
for nm,f in (("sqrt(1-alpha^2)",lambda a:np.sqrt(np.maximum(1-a*a,0))),
             ("1-alpha",lambda a:1-a),
             ("sqrt((1-a)(1+3a))/2",lambda a:0.5*np.sqrt(np.maximum((1-a)*(1+3*a),0))),
             ("sqrt((1-a)(1+3a))",lambda a:np.sqrt(np.maximum((1-a)*(1+3*a),0)))):
    r=np.abs(D-f(A)).max()
    print(f"      {nm:>24}  max residual {r:.2e}{'   <-- EXACT' if r<1e-6 else ''}")
print()
print("(3) purity flow: det rho after one application (pure V channel, input pure)")
print(f"   {'alpha':>8} {'|v| in':>8} {'|v| out':>9} {'det in':>9} {'det out':>9} {'moves':>10}")
for al in (1.0,0.8,0.5,0.0):
    vin=0.5; vout=al*vin
    print(f"   {al:8.2f} {vin:8.3f} {vout:9.3f} {0.25-vin**2:9.4f} {0.25-vout**2:9.4f}"
          f" {'toward mixed' if vout<vin else 'stays null':>10}")
print()
print("   A finite max delta at every alpha = a CP-DERIVED SPEED LIMIT.")
