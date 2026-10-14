"""K3-T1: signed linear response of F3's U_g arc vacuum (pre-registered in ../PREREG.md).
U_g copied from F3 scripts/r1f2_vertex.py. Light sector (eps_+ ~ 0) absorbs w>0;
pi sector (eps_+ ~ pi) has quasi-energy change 2eps_+ = 2pi - w == -w: it emits at w.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1, -1]).astype(complex)
S = np.array([sx, sy, sz])


def ab(k):
    """k: (...,3). returns a (...), b (...,3) with U = a - i b.sigma (F3's U_g)."""
    c = np.cos(k); s = np.sin(k)
    a = np.prod(c, axis=-1)
    s2 = (s ** 2).sum(-1)
    g = np.sqrt(np.clip(1 - a ** 2, 0, None) / np.where(s2 > 1e-300, s2, 1.0))
    g = np.where(s2 > 1e-300, g, 1.0)
    return a, g[..., None] * s


def eps_plus(k):
    a, b = ab(k)
    return np.arccos(np.clip(a, -1, 1))  # in [0, pi]; sin eps = |b|


def Umat(k):
    a, b = ab(k)
    return a[..., None, None] * np.eye(2) - 1j * np.einsum('...j,jab->...ab', b, S)


def vertex2(k, e=1e-7):
    """sum_j |<u+| dU/dk_j |u->|^2, u+ = +1 eigvec of bhat.sigma (U u+ = e^{-i eps+} u+)."""
    a, b = ab(k)
    bn = b / np.linalg.norm(b, axis=-1, keepdims=True)
    H = np.einsum('...j,jab->...ab', bn, S)
    w, v = np.linalg.eigh(H)
    um = v[..., :, 0]; up = v[..., :, 1]   # eigh ascending: -1 then +1
    tot = np.zeros(k.shape[:-1])
    for j in range(3):
        d = np.zeros(3); d[j] = e
        dU = (Umat(k + d) - Umat(k - d)) / (2 * e)
        m = np.einsum('...a,...ab,...b->...', up.conj(), dU, um)
        tot += np.abs(m) ** 2
    return tot


def fib_sphere(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1 - 2 * i / n); th = np.pi * (1 + 5 ** 0.5) * i
    return np.stack([np.cos(th) * np.sin(phi), np.sin(th) * np.sin(phi), np.cos(phi)], -1)


corners = np.array([[x, y, z] for x in (0, np.pi) for y in (0, np.pi) for z in (0, np.pi)])
a_c, _ = ab(corners + 1e-12)
ndir = 3000
nh = fib_sphere(ndir)


def shell_weight(K, target, rmax=0.6, iters=60):
    """(2pi)^-3 Int d^3q sum|M|^2 delta(2 eps+(K+q) - target), restricted to the corner shell."""
    F = lambda r: 2 * eps_plus(K + r[:, None] * nh) - target
    lo = np.full(ndir, 1e-9); hi = np.full(ndir, rmax)
    flo = F(lo); fhi = F(hi)
    ok = np.sign(flo) != np.sign(fhi)
    for _ in range(iters):
        mid = 0.5 * (lo + hi); fm = F(mid)
        left = np.sign(fm) == np.sign(flo)
        lo = np.where(left, mid, lo); flo = np.where(left, fm, flo)
        hi = np.where(left, hi, mid)
    r = 0.5 * (lo + hi)
    h = 1e-6
    dF = (F(r + h) - F(r - h)) / (2 * h)
    q = K + r[:, None] * nh
    M2 = vertex2(q)
    integrand = r ** 2 * M2 / np.abs(dF)
    val = (4 * np.pi * integrand[ok].mean() * ok.mean() / (2 * np.pi) ** 3) if ok.any() else 0.0
    if not ok.any():
        return 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    eps = eps_plus(q)
    dE = 2 * np.sin(eps)  # Delta E for the - -> + transition, E = sin H_F (F3's E)
    return val, ok.mean(), M2[ok].mean(), np.median(np.abs(dF[ok])), np.median(r[ok]), np.median(dE[ok])


print("corner a values (+1: eps=0 node, -1: eps=pi node):", np.round(a_c, 6))
print()
print(f"{'w':>6} {'A_abs(light)':>14} {'A_em(pi)':>14} {'A_em/A_abs':>11} {'net/A_abs':>10}  "
      f"{'pi-abs at +w':>12}  dE'(light) dE'(pi)")
rows = []
for w in (0.2, 0.1, 0.05, 0.02, 0.01):
    Aabs = 0.0; Aem = 0.0; Api_abs = 0.0; fr = []; dEl = []; dEp = []
    for K, a0 in zip(corners, a_c):
        if a0 > 0:   # eps=0 node: absorption at 2eps+ = w
            v, f, m2, dfm, rm, de = shell_weight(K, w); Aabs += v; fr.append(f); dEl.append(de)
        else:        # eps=pi node: quasi-energy change 2eps+ = 2pi - w  == -w -> emission at w
            v, f, m2, dfm, rm, de = shell_weight(K, 2 * np.pi - w); Aem += v; fr.append(f); dEp.append(de)
            # pi-sector ABSORPTION at +w would need 2eps+ = w near the pi node: impossible there
            v2, f2, *_ = shell_weight(K, w, rmax=0.6)
            Api_abs += v2
    rows.append((w, Aabs, Aem))
    print(f"{w:6.2f} {Aabs:14.6e} {Aem:14.6e} {Aem/Aabs:11.6f} {(Aabs-Aem)/Aabs:10.2e}  {Api_abs:12.3e}  "
          f"{np.mean(dEl):.4e} {np.mean(dEp):.4e}   root-ok frac min {min(fr):.4f}")

# continuum single-Weyl reference: 4 nodes x (2pi)^-3 * 4pi (w/2)^2 * <M2>=2 / (dF/dr=2)
print()
for w, Aabs, Aem in rows:
    ref = 4 * 4 * np.pi * (w / 2) ** 2 * 2 / 2 / (2 * np.pi) ** 3
    print(f"w={w:5.2f}: A_abs/ref = {Aabs/ref:.6f}   A_em/ref = {Aem/ref:.6f}")

# full-BZ cross-check: no small-|2eps+| or near-2pi weight outside corner balls of radius 0.25
N = 72
g1 = (np.arange(N) + 0.5) * 2 * np.pi / N
KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing='ij')
kk = np.stack([KX, KY, KZ], -1).reshape(-1, 3)
ep = eps_plus(kk)
dist = np.min(np.linalg.norm(((kk[:, None, :] - corners[None] + np.pi) % (2 * np.pi)) - np.pi, axis=-1), axis=1)
out = dist > 0.25
print()
print(f"full-BZ grid N={N}: outside corner balls (r>0.25): min 2eps+ = {2*ep[out].min():.4f}, "
      f"max 2eps+ = {2*ep[out].max():.4f} (2pi = {2*np.pi:.4f})")
w = 0.2
ok = (2 * ep[out].min() > w) and (2 * ep[out].max() < 2 * np.pi - w)
print("no weight at |2eps+| < 0.2 or 2eps+ > 2pi-0.2 outside the shells:", ok)

ratio = rows[-1][2] / rows[-1][1]
ratio2 = rows[-2][2] / rows[-2][1]
if abs(ratio - 1) < 0.05 and abs(ratio2 - 1) < 0.05:
    verdict = "KILL-(b)-READING"
elif abs(ratio - 1) > 0.20:
    verdict = "F3-A-READING-SURVIVES (no cancellation)"
else:
    verdict = "INCONCLUSIVE"
print("\nPre-registered verdict:", verdict)
