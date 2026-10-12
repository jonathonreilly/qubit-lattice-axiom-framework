"""Deliberate resonant-branch sampling + 1D control.
(a) d=3: Moller shells within 2% of an O(e) pole (intermediate transverse photon nearly on shell, lattice-scale umklapp
    Q); T there; odd scalar null space using ONLY those shells.
(b) d=3: special total momenta: K on the reduced-zone boundary (K_i = -pi/2) and K = 0 (pair-like) shells.
(c) d=1 control: Coulomb-only staggered QED; generic sampler finds only trivial (permutation) shells -> every f passes;
    special branch K = pi/2: (k, pi/2-k) -> (-k, pi/2+k) is a nontrivial resonance; test sin 2k there."""
import itertools, numpy as np
from s2_core import *
rng = np.random.default_rng(99)
def md_only(S, k1, k2, k3, k4):
    out = np.inf
    for (ka, kc) in ((k1, k3), (k1, k4)):
        for mv in itertools.product(range(2), repeat=S.d):
            Q = wrapf(ka - kc + np.pi*np.array(mv)); w = omega(Q)
            if w < 1e-9: continue
            Dl = eps(ka, S.m) - eps(kc, S.m); out = min(out, abs(w*w - Dl*Dl)/w**2)
    return out
for m in (0.0, 0.5):
    S = Stag(3, m)
    cand = sample_moller(S, 30000, rng, mode='generic')
    res = [q for q in cand if md_only(S, *q) < 0.02]
    print(f"(a) d=3 m={m}: {len(cand)} shells scanned, {len(res)} within 2% of an O(e) pole", flush=True)
    res = res[:600]
    rat = []; big = []
    for q in res:
        T, U = moller_T(S, *q); sv = np.linalg.svd(T, compute_uv=False); rat.append(sv[-1]/sv[0]); big.append(sv[0])
    if res:
        print(f"    T near pole: max-sv median {np.median(big):.2e}; min-sv/max-sv min {np.min(rat):.2e} median {np.median(rat):.2e}")
        for R in (2, 3, 4):
            B = odd_basis(3, R)
            A = np.array([np.sin(2*B@k1)+np.sin(2*B@k2)-np.sin(2*B@k3)-np.sin(2*B@k4) for (k1,k2,k3,k4) in res])/np.sqrt(len(res))
            sv = np.linalg.svd(A, compute_uv=False)
            print(f"    resonant-only rows, R={R}: cols {len(B)}, rows {len(res)}, null dim {nullity(sv, len(B))}, sv min {sv[-1]:.3e} max {sv[0]:.3e}")
    # (b) special K
    for name, Kfix in (("K on zone boundary (-pi/2,*,*)", None), ("K = 0", np.zeros(3))):
        rows = []; rr = []
        for t in range(400):
            k1 = rng.uniform(-np.pi/2, np.pi/2, 3)
            if Kfix is None:
                K = rng.uniform(-np.pi/2, np.pi/2, 3); K[0] = -np.pi/2
            else: K = Kfix
            k2 = wrapr(K - k1); E = eps(k1, m) + eps(k2, m)
            k30 = rng.uniform(-np.pi/2, np.pi/2, 3); ax = rng.integers(3); g = np.linspace(-np.pi/2, np.pi/2, 801)
            Tm = np.tile(k30, (801, 1)); Tm[:, ax] = g
            fv = eps(Tm, m) + eps(wrapr(K - Tm), m) - E
            idx = np.nonzero(np.sign(fv[:-1])*np.sign(fv[1:]) < 0)[0]
            for ii in idx[:1]:
                a, b = g[ii], g[ii+1]
                def F(tt):
                    x = k30.copy(); x[ax] = tt; return eps(x, m) + eps(wrapr(K - x), m) - E
                fa = F(a)
                for _ in range(70):
                    c = 0.5*(a+b); fc = F(c)
                    if np.sign(fa)*np.sign(fc) <= 0: b = c
                    else: a, fa = c, fc
                k3 = k30.copy(); k3[ax] = 0.5*(a+b); k3 = wrapr(k3); k4 = wrapr(K - k3)
                if min(np.max(np.abs(wrapr(k3-k1))), np.max(np.abs(wrapr(k3-k2)))) < 1e-3: continue
                T, U = moller_T(S, k1, k2, k3, k4); sv = np.linalg.svd(T, compute_uv=False); rr.append(sv[-1]/sv[0])
                rows.append((k1, k2, k3, k4))
        B = odd_basis(3, 4)
        A = np.array([np.sin(2*B@k1)+np.sin(2*B@k2)-np.sin(2*B@k3)-np.sin(2*B@k4) for (k1,k2,k3,k4) in rows])/np.sqrt(len(rows))
        sv = np.linalg.svd(A, compute_uv=False)
        print(f"(b) d=3 m={m} {name}: {len(rows)} shells; T min-sv/max-sv min {np.min(rr):.2e}; odd R=4 null dim {nullity(sv, len(B))} (rows {len(rows)} < cols {len(B)} => underdetermined if so); sv min {sv[-1]:.3e}")
# (c) 1D control
S1 = Stag(1, 0.5)
q1 = sample_moller(S1, 200, rng, mode='generic', maxtries=20000)
print(f"(c) d=1 m=0.5: generic sampler found {len(q1)} nontrivial shells (expected 0: 1D two-body shells are permutations except special K)")
B = odd_basis(1, 8)
k = rng.uniform(-np.pi/2, np.pi/2, 200)
rows = []; Tn = []
for kk in k:
    k1, k2, k3, k4 = np.array([kk]), wrapr(np.array([np.pi/2 - kk])), wrapr(np.array([-kk])), wrapr(np.array([np.pi/2 + kk]))
    assert abs(eps(k1,.5)+eps(k2,.5)-eps(k3,.5)-eps(k4,.5)) < 1e-12
    T, U = moller_T(S1, k1, k2, k3, k4, include_tr=False); Tn.append(np.abs(T).max())
    rows.append(np.sin(2*B@k1)+np.sin(2*B@k2)-np.sin(2*B@k3)-np.sin(2*B@k4))
A = np.array(rows)/np.sqrt(len(rows)); sv = np.linalg.svd(A, compute_uv=False)
print(f"    K=pi/2 branch (k,pi/2-k)->(-k,pi/2+k): Coulomb T median |T| {np.median(Tn):.3e}; odd f, R=8: null dim {nullity(sv, len(B))} of {len(B)}; sin2k defect {np.abs(A[:,0]).max()*np.sqrt(len(rows)):.3f}")
# trivial-only control: permutation shells give zero rows -> every f passes, nullity = full with abs tolerance
Atriv = np.array([np.sin(2*B@np.array([a]))+np.sin(2*B@np.array([b]))-np.sin(2*B@np.array([b]))-np.sin(2*B@np.array([a])) for a, b in rng.uniform(-1.5, 1.5, (50, 2))])
sv = np.linalg.svd(Atriv, compute_uv=False)
print(f"    permutation-only control: null dim {nullity(sv, len(B))} of {len(B)} (abs 1e-10 + rel 1e-9 tolerance; relative-only would misreport)")
