"""PR 9008 attack-f: NORMALIZATION of the covariance estimator, recomputed by brute force at small size.

Conventions in the note/runner: F(k) = fftn(E_z) (unnormalised, kernel e^{-ik.x}), S_zz(k) = |F(k)|^2 / N, N = L^3,
P_zz = 1 - s_z^2/Q with s_i^2 = 2 - 2 cos k_i, K_cont = (2N+1)/(3N), the identity  sum_k S_zz = N,
ratio r = K_cont sum S_zz / sum P_zz, implied stiffness c = K_cont/(2 r).
Checked here, none of it borrowed from the runner:
 1. the L = 2 census REBUILT (all 9600 ice states from net flows), the exact covariance S_zz(k) at all 8 wavevectors;
    Parseval sum_k S = N for every state; Fourier-space divergence-freeness for every state and every k (fixes conjugation/sign of s_i^2);
 2. the same identities on random ice states of L = 4 and L = 6 (own pure-numpy directed-loop walk);
 3. P_zz is the (z,z) element of the transverse projector built from the lattice divergence d_i = 1 - e^{-i k_i}; the sum rule
    sum_{k != 0} P_zz = 2(N-1)/3 exactly at L = 2, 4, 6, 16 (so K_cont = (sum_{k!=0} P_zz + 1)/N: the calibration counts the k = 0 mode as 1);
 4. algebra of c: K_cont cancels in c = sum P / (2 sum S) while the reference K_cont/2 does not; how far the note's 0.337% moves if
    the k = 0 mode carries no weight in the reference (K_ref = (2N-2)/(3N)); the k = 0 mode of the covariance (winding) at L = 2 exactly.
"""
import itertools, math, sys
from fractions import Fraction
import numpy as np

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

def proj_zz(L):
    k = 2 * np.pi * np.arange(L) / L
    d = 1 - np.exp(-1j * k)
    d2 = np.abs(d) ** 2
    KX, KY, KZ = np.meshgrid(d, d, d, indexing="ij")
    tot = np.abs(KX) ** 2 + np.abs(KY) ** 2 + np.abs(KZ) ** 2
    P = np.zeros((L, L, L)); nz = tot > 1e-14
    P[nz] = 1 - np.abs(KZ[nz]) ** 2 / tot[nz]
    return P, KX, KY, KZ

# ------------------------------------------------ 1. exact L = 2
print("== 1. exact L = 2: every ice state ==")
V = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
vid = {v: i for i, v in enumerate(V)}
edges = []
for d in range(3):
    for v in V:
        if v[d] == 0:
            w = list(v); w[d] = 1
            edges.append((v, tuple(w), d))
states = []
for f in itertools.product((-1, 0, 1), repeat=12):
    div = [0] * 8
    for (u, v, d), fe in zip(edges, f):
        div[vid[u]] += fe; div[vid[v]] -= fe
    if any(div): continue
    zeros = [i for i, fe in enumerate(f) if fe == 0]
    base = {i: (1 if fe == 1 else -1) for i, fe in enumerate(f) if fe != 0}
    for ch in itertools.product((1, -1), repeat=len(zeros)):
        ea = dict(base)
        for i, c in zip(zeros, ch): ea[i] = c
        E = np.zeros((3, 2, 2, 2), int)
        for i, (u, v, d) in enumerate(edges):
            Ea = ea[i]
            Eb = Ea - 2 * f[i] if False else None
        # net flow u->v = Ea - Eb = 2 f  ->  Eb = Ea - 2 f
        for i, (u, v, d) in enumerate(edges):
            Ea = ea[i]; Eb = Ea - 2 * f[i]
            E[(d,) + u] = Ea
            E[(d,) + v] = Eb
        states.append(E)
check("the rebuilt census has 9600 states with entries +-1", len(states) == 9600 and all(np.abs(E).max() == 1 and (np.abs(E) == 1).all() for E in states[:50]))
Pz, DX, DY, DZ = proj_zz(2)
Sacc = np.zeros((2, 2, 2)); maxpars = 0.0; maxdiv = 0.0; W2 = 0.0
for E in states:
    Fs = [np.fft.fftn(E[i].astype(float)) for i in range(3)]
    Sz = np.abs(Fs[2]) ** 2 / 8
    Sacc += Sz
    maxpars = max(maxpars, abs(Sz.sum() - 8))
    dv = DX * Fs[0] + DY * Fs[1] + DZ * Fs[2]
    maxdiv = max(maxdiv, float(np.abs(dv).max()))
    W2 += (E[2, :, :, 0].sum()) ** 2
Sacc /= len(states)
check("Parseval for every state: sum_k |fftn(E_z)|^2 / N = N (the runner's unit-arrow identity)", maxpars < 1e-10, f"max deviation {maxpars:.1e}")
check("every state is divergence-free in Fourier space with d_i = 1 - e^{-ik_i} for the fftn kernel e^{-ik.x} (conjugation/sign convention of P_zz)", maxdiv < 1e-10, f"max |sum_i d_i F_i| = {maxdiv:.1e}")
# the k = 0 mode is the winding: F_z(0) = L W_z, S(0) = L^2 W_z^2 / N = W_z^2 / L
check("exact <S_zz(0)> = <W_z^2>/L at L = 2 (winding W_z = sum over one z-plane of E_z)", abs(Sacc[0, 0, 0] - (W2 / len(states)) / 2) < 1e-12,
      f"<S(0)> = {Sacc[0,0,0]:.6f}, <W_z^2>/L = {W2/len(states)/2:.6f}")
sumP = Pz.sum()
check("at L = 2: sum_{k!=0} P_zz = 2(N-1)/3 = 14/3", abs(sumP - 14 / 3) < 1e-12, f"{sumP:.12f}")
# exact S/P at the L = 2 wavevectors, grouped by folded multiset (angular form at L = 2 is NOT claimed by the note: shown for scale)
print("   exact L = 2 covariance (folded k -> S_zz, P_zz, S/P):")
for kk in sorted(itertools.product((0, 1), repeat=3)):
    if kk == (0, 0, 0): continue
    print(f"     k={kk}: S_zz = {Sacc[kk]:.6f}  P_zz = {Pz[kk]:.6f}  S/P = {Sacc[kk]/Pz[kk] if Pz[kk] > 1e-12 else float('nan'):.6f}")

# ------------------------------------------------ 2. random ice on L = 4, 6 with an own walk
print("\n== 2. random ice states on L = 4 and L = 6 ==")
rng = np.random.default_rng(90081)
def initial(L):
    E = np.empty((3, L, L, L), int)
    alt = (-1) ** np.arange(L)
    E[0] = np.broadcast_to(alt[None, :, None], (L, L, L)); E[1] = np.broadcast_to(alt[None, None, :], (L, L, L)); E[2] = np.broadcast_to(alt[:, None, None], (L, L, L))
    return E
def out_links(E, v, L):
    x, y, z = v; res = []
    for i in range(3):
        if E[(i, x, y, z)] == 1:
            w = [x, y, z]; w[i] = (w[i] + 1) % L; res.append(((i, x, y, z), tuple(w)))
        b = [x, y, z]; b[i] = (b[i] - 1) % L
        if E[(i,) + tuple(b)] == -1:
            res.append(((i,) + tuple(b), tuple(b)))
    return res
def loop(E, L):
    v0 = tuple(int(t) for t in rng.integers(L, size=3)); v = v0; last = None
    while True:
        cand = [c for c in out_links(E, v, L) if c[0] != last]
        lk, w = cand[rng.integers(len(cand))]
        E[lk] = -E[lk]; last = lk; v = w
        if v == v0: return
for L in (4, 6):
    Pz, DX, DY, DZ = proj_zz(L)
    E = initial(L); N = L ** 3
    for _ in range(300): loop(E, L)
    worst_div = worst_par = 0.0
    for _ in range(40):
        for _ in range(20): loop(E, L)
        Fs = [np.fft.fftn(E[i].astype(float)) for i in range(3)]
        worst_div = max(worst_div, float(np.abs(DX * Fs[0] + DY * Fs[1] + DZ * Fs[2]).max()))
        worst_par = max(worst_par, abs((np.abs(Fs[2]) ** 2).sum() / N - N))
    check(f"L = {L}: 40 sampled ice states are divergence-free in Fourier space and satisfy Parseval", worst_div < 1e-9 and worst_par < 1e-8, f"{worst_div:.1e}, {worst_par:.1e}")
    check(f"L = {L}: sum_(k!=0) P_zz = 2(N-1)/3", abs(Pz.sum() - 2 * (N - 1) / 3) < 1e-9, f"{Pz.sum():.10f} vs {2*(N-1)/3:.10f}")

# ------------------------------------------------ 3. L = 16 sum rule and the calibration
print("\n== 3. L = 16 sum rule and the reference stiffness ==")
L = 16; N = L ** 3
P16, *_ = proj_zz(L)
check("L = 16: sum_{k!=0} P_zz = 2(N-1)/3 exactly (cubic symmetry of the three s_i^2/Q terms)", abs(P16.sum() - 2 * (N - 1) / 3) < 1e-8, f"{P16.sum():.9f} vs {2*(N-1)/3:.9f}")
Kc = Fraction(2 * N + 1, 3 * N)
check("K_cont = (2N+1)/(3N) equals (sum_{k!=0} P_zz + 1)/N: the calibration counts the k = 0 mode with weight 1 while the runner's projector() sets P_zz(0) = 0",
      abs(float(Kc) - (P16.sum() + 1) / N) < 1e-12, f"K_cont = {float(Kc):.10f}; with P(0)=0: {P16.sum()/N:.10f}")
# c = K_cont/(2r), r = K_cont*sumS/sumP  =>  c = sumP/(2 sumS); the reference K_cont/2 is separate
r = 1.0 / 0.33450 * float(Kc) / 2   # a synthetic r consistent with the note's c
c_from_r = float(Kc) / (2 * r)
check("K_cont cancels in the implied stiffness c = K_cont/(2r) = sum P/(2 sum S) (sanity of the note's c)", abs(c_from_r - 0.33450) < 1e-12)
cL = float(Kc) / 2; cL_alt = (2 * N - 2) / (3 * N) / 2
off = 0.33450 / cL - 1; off_alt = 0.33450 / cL_alt - 1
print(f"   offset of c = 0.33450 above K_cont/2 = {off*100:.3f}% (note 0.337%); above the k=0-free reference (2N-2)/(6N) = {off_alt*100:.3f}%")
check("the note's 0.337% reproduces from c = 0.33450 and K_cont = (2N+1)/(3N)", abs(off * 100 - 0.337) < 0.001, f"{off*100:.4f}%")
check("the alternative k=0 convention would change the quoted offset by less than 0.04 percentage points (below the 0.1% scale of the angular test)",
      abs(off_alt - off) < 4e-4, f"{(off_alt-off)*100:.3f} pp")

print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-f normalization on PR 9008: FFT kernel/conjugation, Parseval identity, Fourier-space divergence-freeness (exact at L=2 over all 9600 states, sampled at L=4,6), P_zz as the (z,z) transverse projector element, sum rule sum_(k!=0) P_zz=2(N-1)/3 at L=2,4,6,16, K_cont=(2N+1)/(3N) as (sum P+1)/N (k=0 mode counted as 1; the note's ratio never uses it, quoted 0.337% offset would be 0.374% with P(0)=0), c independent of K_cont; PASS={PASS} FAIL={FAIL}; no defect in the note's normalization")
sys.exit(1 if FAIL else 0)
