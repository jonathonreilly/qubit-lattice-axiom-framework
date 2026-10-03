# A39 c3: loophole (c). Two-ripple (bound-state) branches over a calm product vacuum that is
# the ground state, on an LxL square torus (L=64). Hard-core flips, total momentum K,
# relative coordinate r != 0, twisted BC f(r+L e_mu) = (-1)^{n_mu} f(r), bosonic sector P=+1.
# Model 1: aligned vacuum of the frustration-free rule sum_b (1 - sigma.sigma)/2 = sum_b 2 P_singlet:
#          one flip eps(k) = 2 sum_mu (1-cos k_mu); NN pair attraction V=-2 (exact mapping).
# Model 2: gapped flips eps(k) = m + 2 sum(1-cos k), NN attraction tuned so the K=0 pair sits at E=0
#          (a gapless composite over a gapped calm vacuum).
import signal, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import eigsh
signal.alarm(55)
L = 64
coords = [(x, y) for y in range(L) for x in range(L) if (x, y) != (0, 0)]
ix = {c: k for k, c in enumerate(coords)}; D = len(coords)

def build(nK, eps0, V, tau=1.0):
    s = [(-1.0)**nK[0], (-1.0)**nK[1]]
    K = [2*np.pi*nK[0]/L, 2*np.pi*nK[1]/L]
    rows, cols, vals = [], [], []
    for (x, y), k in ix.items():
        nn = (abs(((x + L//2) % L) - L//2) + abs(((y + L//2) % L) - L//2)) == 1
        rows.append(k); cols.append(k); vals.append(2*eps0 + (V if nn else 0.0))
        for mu in (0, 1):
            amp = -2*tau*np.cos(K[mu]/2)
            c = [x, y]; c[mu] += 1
            sign = 1.0
            if c[mu] == L: c[mu] = 0; sign = s[mu]
            c = tuple(c)
            if c == (0, 0): continue
            j = ix[c]
            rows += [k, j]; cols += [j, k]; vals += [amp*sign, amp*sign]
    H = sp.csr_matrix((vals, (rows, cols)), shape=(D, D))
    # parity P: f(r) -> sign * f(-r mod L)
    pr, pc, pv = [], [], []
    for (x, y), k in ix.items():
        sg = (s[0] if x != 0 else 1.0)*(s[1] if y != 0 else 1.0)
        pr.append(k); pc.append(ix[((-x) % L, (-y) % L)]); pv.append(sg)
    P = sp.csr_matrix((pv, (pr, pc)), shape=(D, D))
    assert abs(H - H.T).max() < 1e-12 and abs(H @ P - P @ H).max() < 1e-10
    return H + 25.0*(sp.identity(D) - P)

def lowest(nK, eps0, V, k=2):
    H = build(nK, eps0, V)
    sig = min(0.0, 2*eps0 + V) - 9.0   # Gershgorin: every eigenvalue lies above sig, so nearest = lowest
    w = eigsh(H, k=k, sigma=sig, which="LM", return_eigenvectors=False, tol=1e-12)
    return np.sort(w)

def fit(Es, Ks):
    sl = [np.log(Es[i+1]/Es[i])/np.log(Ks[i+1]/Ks[i]) for i in range(len(Es)-1)]
    return sl

print(f"L={L}, relative-coordinate dimension {D}; even n only (odd n carry a half-step twist offset in the relative momentum)")
print("== Model 1: aligned vacuum, frustration-free rule (eps0 = 4, V = -2) ==")
for direc in ((1, 0), (1, 1)):
    Es, Ks, Ec = [], [], []
    for n in (2, 4, 6, 8, 10):
        nK = (n*direc[0], n*direc[1]); K = 2*np.pi*n/L*np.hypot(*direc)
        w = lowest(nK, 4.0, -2.0)
        ec = sum(4*(1-np.cos(2*np.pi*nk/L/2)) for nk in nK)   # continuum bottom 2 eps(K/2)
        Es.append(w[0]); Ks.append(K); Ec.append(ec)
        print(f"  K={K:.4f} along {direc}: lowest two-ripple E={w[0]:.6e}, continuum bottom 2eps(K/2)={ec:.6e}, E/K^2={w[0]/K**2:.4f}")
    print("   local exponents d ln E / d ln K:", np.round(fit(Es, Ks), 3))
w0 = lowest((0, 0), 4.0, -2.0, k=3)
print("  K=0: lowest bosonic energies", np.round(w0, 8), "(zero mode = uniformly rotated vacuum family, as expected)")

print("== Model 2: gapped flips (m = 0.5), NN attraction tuned to put the K=0 pair at E=0 ==")
m = 0.5; eps0 = 4.0 + m
lo, hi = -40.0, -0.0
for _ in range(40):
    mid = 0.5*(lo+hi)
    if lowest((0, 0), eps0, mid, k=1)[0] > 0: hi = mid
    else: lo = mid
Vs = 0.5*(lo+hi)
print(f"  tuned V* = {Vs:.6f}; single-flip gap m = {m}; two-flip continuum bottom at K=0 = {2*m}")
Es, Ks = [], []
for n in (0, 2, 4, 6, 8, 10):
    w = lowest((n, 0), eps0, Vs, k=2)
    K = 2*np.pi*n/L
    if n > 0: Es.append(w[0]); Ks.append(K)
    print(f"  K={K:.4f}: bound pair E={w[0]:.6e}" + (f", E/K^2={w[0]/K**2:.4f}" if n > 0 else "") + f"; next state {w[1]:.4f}")
print("   local exponents d ln E / d ln K:", np.round(fit(Es, Ks), 3))
# energy of a classical 2x2 block of 4 flips vs 2 separated pairs at the same V* (n=4 instability hint)
print(f"  classical check, t=0: pair 2*eps0+V* = {2*eps0+Vs:.3f}; 2x2 block 4*eps0+4V* = {4*eps0+4*Vs:.3f}; 3x3 block 9*eps0+12V* = {9*eps0+12*Vs:.3f}")
