"""
T214 - two questions about the consistent record field of R136.

(1) IS THE EDGE POTENTIAL THE BORN WEIGHT?
    R136: phi = 1 + lam (v.v').   R100 (independent): the Born weight is
    Tr(rho rho').  For qubit pure states rho = (I + v.sigma)/2,
    Tr(rho rho') = (1 + v.v')/2.  So at lam = 1, phi = 2 Tr(rho rho') exactly,
    and lam = 1 is also the positivity boundary.  Checked here.

(2) DOES A CONTINUUM LIMIT FIX lambda?
    The gravity lane needs a -> 0.  A lattice field only has a continuum limit
    where its correlation length diverges in lattice units, i.e. at a critical
    point.  If the record field  mu ∝ prod_edges (1 + lam v_x.v_y)  on Z^3 has
    a critical lambda_c, then the requirement of a continuum limit FIXES the
    parameter the axioms leave free.  Located here by the Binder cumulant
    U = 1 - <m^4>/(3<m^2>^2), whose curves for different L cross at lambda_c.
"""
import numpy as np

S = [np.array([[0,1],[1,0]],dtype=complex),
     np.array([[0,-1j],[1j,0]],dtype=complex),
     np.array([[1,0],[0,-1]],dtype=complex)]

print("=== (1) edge potential vs Born weight ===")
rng = np.random.default_rng(0)
worst = 0.0
for _ in range(2000):
    v = rng.normal(size=3); v /= np.linalg.norm(v)
    w = rng.normal(size=3); w /= np.linalg.norm(w)
    rho  = (np.eye(2) + sum(v[i]*S[i] for i in range(3)))/2
    rhop = (np.eye(2) + sum(w[i]*S[i] for i in range(3)))/2
    worst = max(worst, abs(np.trace(rho@rhop).real - (1+v@w)/2))
print(f"  max |Tr(rho rho') - (1 + v.v')/2| over 2000 random pure pairs: {worst:.2e}")
print(f"  => phi(lam=1) = 1 + v.v' = 2 Tr(rho rho') EXACTLY.")
print(f"     lam = 1 is simultaneously the positivity boundary (phi >= 0) and")
print(f"     the point where the edge potential IS the framework's Born weight.")

# ------------------------------------------------------------------ (2) MC
def sweep(v, lam, rng, mask, ncone):
    L = v.shape[0]
    nb = (np.roll(v,1,0), np.roll(v,-1,0), np.roll(v,1,1),
          np.roll(v,-1,1), np.roll(v,1,2), np.roll(v,-1,2))
    prop = v + ncone*rng.normal(size=v.shape)
    prop /= np.linalg.norm(prop, axis=-1, keepdims=True)
    wold = np.ones(v.shape[:3]); wnew = np.ones(v.shape[:3])
    for n in nb:
        wold *= 1 + lam*np.sum(v*n, axis=-1)
        wnew *= 1 + lam*np.sum(prop*n, axis=-1)
    acc = (rng.random(v.shape[:3]) < np.clip(wnew/np.maximum(wold,1e-300),0,1)) & mask
    v[acc] = prop[acc]
    return acc[mask].mean()

def run(L, lam, nwarm=3000, nmeas=12000, seed=0):
    rng = np.random.default_rng(seed)
    v = rng.normal(size=(L,L,L,3)); v /= np.linalg.norm(v,axis=-1,keepdims=True)
    i,j,k = np.indices((L,L,L))
    A = ((i+j+k) % 2 == 0); B = ~A
    ncone = 1.0
    for t in range(nwarm):
        a = 0.5*(sweep(v,lam,rng,A,ncone) + sweep(v,lam,rng,B,ncone))
        if t % 100 == 99:
            ncone *= 1.15 if a > 0.55 else (0.87 if a < 0.35 else 1.0)
            ncone = min(max(ncone, 0.05), 4.0)
    m2 = []; m4 = []
    for t in range(nmeas):
        sweep(v,lam,rng,A,ncone); sweep(v,lam,rng,B,ncone)
        if t % 5 == 0:
            m = np.linalg.norm(v.sum(axis=(0,1,2)))/L**3
            m2.append(m*m); m4.append(m**4)
    m2 = np.mean(m2); m4 = np.mean(m4)
    return m2, 1 - m4/(3*m2*m2)

if __name__ == "__main__":
    print("\n=== (2) Binder cumulant scan: where does the record field order? ===")
    lams = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
    print("  lam    " + "".join(f"  L={L}: <m^2>   U    " for L in (6,8,10)))
    for lam in lams:
        row = f"  {lam:4.2f}  "
        for L in (6,8,10):
            m2, U = run(L, lam, seed=12345+L)
            row += f"   {m2:7.4f} {U:6.3f}"
        print(row)
