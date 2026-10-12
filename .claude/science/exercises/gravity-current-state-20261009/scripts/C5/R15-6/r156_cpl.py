"""R15-6 step 4: g today on a DESI-like late history (matter + CPL dark energy + any constant vacuum).
Content (units rho_crit,0 = 1): rho_m = Om a^-3, rho_DE = (1-Om) a^{-3(1+w0+wa)} exp(-3 wa (1-a)), w0 = -0.75, wa = -0.86
(the R14-5 / DESI-type values, comparator).  The constant vacuum is invisible to every reader below (they use only
derivatives of rho_tot).  The TRUE vacuum is constant, so any g != 0 is reader error.
Readers: (O) oracle R = rho_m + rho_DE -> g = 0 exactly;  (P2) R14-5's global Prony order 2;  (MR) memory reader of r156_mr.
Reported: g/H^2 = V'/R (identity), tracking eps = R/rho_nc - 1, H_model/H_true - 1 at a = 1, 0.5, 0.25.
"""
import numpy as np, sympy as sp
u = sp.symbols('u'); Om, w0, wa = 0.3, -0.75, -0.86
a = sp.exp(u)
rho = Om*a**-3 + (1-Om)*a**(-3*(1+w0+wa))*sp.exp(-3*wa*(1-a))
f = [sp.lambdify(u, sp.diff(rho, u, j), 'numpy') for j in range(6)]
us = np.linspace(np.log(0.05), 0.0, 4001)
d = [f[j](us) for j in range(6)]
rnc = d[0]
rm = Om*np.exp(-3*us); rde = rnc - rm
def report(name, R):
    V = rnc - R                       # + any constant: drops out of V'
    gH2 = np.gradient(V, us)/R
    eps = R/rnc - 1
    out = []
    for aa in (1.0, 0.5, 0.25, 0.1):
        i = np.argmin(np.abs(us - np.log(aa)))
        out.append(f"a={aa}: g/H^2={gH2[i]:+.3e}, eps={eps[i]:+.3e}")
    print(f"[{name}] " + "; ".join(out))
    sel = us > np.log(0.1)
    print(f"      over 0.1<a<1: g/H^2 in [{gH2[sel].min():+.3e}, {gH2[sel].max():+.3e}]; max|eps| = {np.max(np.abs(eps[sel])):.3e}")
report("O oracle", rnc.copy())
# P2: R14-5 global Prony order 2 on moments m_k = (-d/du)^k rho_tot, k = 1..4
R = np.empty_like(us); cplx = 0
for i in range(len(us)):
    M = [(-1)**k*d[k][i] for k in range(1, 5)]
    Hk = np.array([[M[0], M[1]], [M[1], M[2]]]); rhs = -np.array([M[2], M[3]])
    c0, c1 = np.linalg.solve(Hk, rhs); x = np.roots([1, c1, c0])
    if np.any(np.abs(np.imag(x)) > 1e-12*np.max(np.abs(x))): cplx += 1
    Vd = np.vander(x, 2, increasing=True).T
    nu = np.linalg.solve(Vd.astype(complex), np.array(M[:2], dtype=complex))
    R[i] = np.real(np.sum(nu/x))
print(f"   (P2 complex nodes at {cplx} of {len(us)} samples)")
report("P2 Prony-2", R)
# MR: h = -rho'/3, h' = -rho''/3, B = 4h + h', running min of e^{3u} B
h = -d[1]/3; hp = -d[2]/3; B = 4*h + hp
mhat = np.minimum.accumulate(np.exp(3*us)*B)
report("MR memory", 0.75*h + 0.25*mhat*np.exp(-3*us))
# DE effective w along the history (comparator check): w = -1 - rho_DE'/(3 rho_DE)
wde = -1 - np.gradient(rde, us)/(3*rde)
print(f"   CPL check: w_DE(a=1) = {wde[-1]:+.3f}, w_DE(a=0.5) = {wde[np.argmin(np.abs(us-np.log(0.5)))]:+.3f}; NEC of total: min (rho+p)_tot/rho_tot = {np.min(-d[1]/3/d[0]):+.3f}")
