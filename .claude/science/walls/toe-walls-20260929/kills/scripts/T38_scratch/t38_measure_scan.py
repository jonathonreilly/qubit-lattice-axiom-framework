"""T38 test 4: canonical-measure scan for the central value of r = |b|^2/a^2 (Q = (1+2r)/3).
Pre-registered in PREREG.md.  Seed 20260929, N = 4e6.  Run: python3 t38_measure_scan.py"""
import numpy as np
from math import gamma
rng = np.random.default_rng(20260929)
N = 4_000_000

def r_of_lam(lam):            # lam: (N,3) root-mass vector, r = (3Q-1)/2, Q = sum lam^2/(sum lam)^2
    s1 = lam.sum(1); s2 = (lam**2).sum(1)
    return 1.5*(s2/s1**2) - 0.5

def dirichlet(alpha, n=N):
    g = rng.gamma(alpha, size=(n,3)); return g/g.sum(1, keepdims=True)

results = []
def rec(name, r, note=""):
    r = np.asarray(r)
    results.append((name, float(np.mean(r)), float(np.median(r)), note))

# A Lebesgue in (a,bR,bI) on the positive-spectrum triangle == Dirichlet(1,1,1) on lam fractions
p = dirichlet(1.0); rec("A flat on positive-spectrum triangle (Dir(1,1,1) on lam fractions)", r_of_lam(p))
# B uniform positive octant of the sphere in lam == isotropic HS measure
g = np.abs(rng.normal(size=(N,3))); lam = g/np.linalg.norm(g, axis=1, keepdims=True); rec("B isotropic HS measure on positive octant (lam-sphere)", r_of_lam(lam))
# C Dirichlet(1,1,1) on mass fractions m/Sum m ; lam = sqrt(m)
m = dirichlet(1.0); rec("C uniform on mass simplex (Dir(1,1,1) on m fractions)", r_of_lam(np.sqrt(m)))
# D Dirichlet(1/2) on lam fractions (Bures, diagonal)
p = dirichlet(0.5); rec("D Bures-diagonal (Dir(1/2) on lam fractions)", r_of_lam(p))
# E Vandermonde |Delta(lam)|^beta on the positive octant sphere, rejection sampling
def vdm(beta, n=N):
    out = []
    tot = 0
    # estimate max of |Delta| on the octant sphere
    g0 = np.abs(rng.normal(size=(400000,3))); l0 = g0/np.linalg.norm(g0,axis=1,keepdims=True)
    D0 = np.abs((l0[:,0]-l0[:,1])*(l0[:,1]-l0[:,2])*(l0[:,0]-l0[:,2])); mx = D0.max()*1.05
    while tot < n:
        g = np.abs(rng.normal(size=(2_000_000,3))); l = g/np.linalg.norm(g,axis=1,keepdims=True)
        D = np.abs((l[:,0]-l[:,1])*(l[:,1]-l[:,2])*(l[:,0]-l[:,2]))
        acc = rng.uniform(size=len(D)) < (D/mx)**beta
        out.append(l[acc]); tot += acc.sum()
    return np.concatenate(out)[:n]
for beta in (1, 2):
    rec(f"E Vandermonde beta={beta} on octant sphere", r_of_lam(vdm(beta)))
# F Haar-random unit vector, all signs (median only meaningful)
x = rng.normal(size=(N,3)); x /= np.linalg.norm(x,axis=1,keepdims=True); rr = r_of_lam(x)
rec("F1 Haar real unit vector (all signs)", rr, "mean diverges; use median")
z = rng.normal(size=(N,3))+1j*rng.normal(size=(N,3)); z /= np.linalg.norm(z,axis=1,keepdims=True)
xz = np.abs(z.sum(1))**2/3.0; rec("F2 Haar complex unit vector: r=(1-x)/(2x), x=|<u|psi>|^2", (1-xz)/(2*xz), "mean diverges; use median")
# G,H,I fixed-weight rules  r = w_s/(2 w_d)
def rw(ns, nd): return nd/(2*ns)     # nu = slot weights (energy ~ nu): r = nu_d/(2 nu_s)
rec("G state counting: sector weights (1/3,2/3)", [rw(1/3,2/3)])
rec("H stack/groupoid: sector weights (1/2 : 1)", [rw(0.5,1.0)] , "same ray as G")
rec("I real Plancherel: sector weights (1,2)", [rw(1,2)], "same ray as G")
# J discs
th = np.sqrt(rng.uniform(size=N)); rec("J1 Lebesgue on disc |b|<=a (2x2-minor positivity only)", th**2, "drops the 3x3 positivity; triangle A is the PSD region")
# J2 projectivised R^3 with HS form: uniform on S^2 in lam, all signs -> F1 ; with literal flat coordinates:
y = rng.normal(size=(N,3)); rr = (y[:,1]**2+y[:,2]**2)/y[:,0]**2; rec("J2 uniform on S^2 in literal (a,bR,bI) coordinates, all signs", rr, "mean diverges; use median")
# K excluded
rec("K block counting (1/2,1/2)  [EXCLUDED: the quotient premise itself]", [rw(0.5,0.5)])
# L Dirichlet(alpha) family on lam fractions: mean Q = (alpha+1)/(3 alpha+1); mean r = ((alpha+1)/(3alpha+1)*3 -1)/2
al = np.linspace(0.05, 3, 100000)
mr = 1.5*(al+1)/(3*al+1)-0.5
i = np.argmin(abs(mr-0.5)); alpha_star = al[i]
rec(f"L Dirichlet(alpha) on lam fractions with mean r = 1/2: alpha* = {alpha_star:.4f} (=1/3?)", [mr[i]], "ONE FREE PARAMETER: excluded from PASS")

print(f"{'measure':78s} {'mean r':>9s} {'median r':>9s}")
for name, mean, med, note in results:
    print(f"{name:78s} {mean:9.4f} {med:9.4f}  {note}")

print()
hits = [(n, m, md) for (n, m, md, note) in results
        if n[0] in "ABCDEFJ" and ("mean diverges" not in " ".join([note]) and (0.49 <= m <= 0.51) or 0.49 <= md <= 0.51)]
print("entries A-J with mean or median r in [0.49,0.51]:")
for h in hits: print("  ", h)
print("(per pre-registration: J1 is a hit only if the 3x3 positivity may be dropped; it may not, since the framework's own region is the PSD triangle A)")
np.save("scan_alpha_star.npy", np.array([alpha_star]))
