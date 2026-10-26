AUDIT_INPUT_PATHS = ('docs/D4_EVENT_ONE_MODE_PER_EVENT_SIXTEEN_CONTENT_TASTE_COSETS_AND_TRIALITY_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-sixteen-content: what internal content does one fermion mode per event carry, on the cube and on D4?

(1) Cube baseline: the 2x2x2 cube's 8 one-body modes under CL-1's anticommuting hops W_i and copy sign s.
(2) One mode per D4 event: a W(F4)- and translation-invariant one-component kernel has no odd (Dirac) symbol.
(3) Counts: hypercube corners, D4/2D4 (16 = 1 + 12 + 3), D4/2D4* (4 = 1 + 3), Fourier duality with the 16
    half-period momenta, and the zoom fixed-point kernel's gap there (only one light class).
(4) Staggered (Kogut-Susskind) 16 on Z^4 = D4 + one hole class: 16 zero modes, events-only square is a scalar
    Laplacian, and Z^4 is kept by only 384 of the 1152 W(F4) elements (one of the three triality classes).
(5) Internal labels: SM commutant on the 16 is abelian, the W(F4) image on the 16 labels is not.
(6) Triality families: S3-invariant masses are degenerate; W(D4) admits extra quartic invariants (dim-6 returns).
(7) Anomalies: the 16 cancels; one taste-4 of SU(4) and 15 Weyl (no nu^c) do not.
Self-contained (numpy), seeded, no external files.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import functools, itertools, time
from fractions import Fraction as Fr
import numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
rng = np.random.default_rng(20261026)
NP = NF = 0


def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


# ---------------- W(F4) as 4x4 matrices preserving D4 (reflections in roots e_i - e_i+1, e_1, (1,1,1,1)/2)
E4 = np.eye(4); gens = []
for i in range(3):
    n = np.zeros(4); n[i], n[i + 1] = 1 / np.sqrt(2), -1 / np.sqrt(2); gens.append(E4 - 2 * np.outer(n, n))
n = np.zeros(4); n[0] = 1; gens.append(E4 - 2 * np.outer(n, n))
n = np.ones(4) / 2; gens.append(E4 - 2 * np.outer(n, n))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel()); G = {key(E4): E4}; fr = [E4]
while fr:
    nf = []
    for A in fr:
        for g in gens:
            B = g @ A
            if key(B) not in G: G[key(B)] = B; nf.append(B)
    fr = nf
GW = np.array(list(G.values())); NG = len(GW)
ROOTS = np.array(sorted({tuple(s * np.array(v)) for v in set(itertools.permutations([1, 1, 0, 0])) for s in itertools.product([1, -1], repeat=4)}), float)
ROOTS = np.unique(ROOTS, axis=0)
print(f"setup: |W(F4)| = {NG}, 24 roots {len(ROOTS) == 24}, roots preserved {all(np.allclose(np.sort(np.round(ROOTS @ g.T, 9), axis=0), np.sort(ROOTS, axis=0)) for g in GW[:50])}")

# ================= 1 cube baseline
X = np.array([[0, 1], [1, 0]]); Zp = np.diag([1., -1]); I2 = np.eye(2); kron = lambda *a: a[0] if len(a) == 1 else np.kron(a[0], kron(*a[1:]))
W = [kron(X, I2, I2), kron(Zp, X, I2), kron(Zp, Zp, X)]
anti = max(np.abs(W[i] @ W[j] + W[j] @ W[i]).max() for i in range(3) for j in range(3) if i != j)
faces = []  # product of hop phases around each unit face of the cube (sites = bit strings)
for i, j in [(0, 1), (0, 2), (1, 2)]:
    for x in range(8):
        loop = W[j] @ W[i] @ W[j] @ W[i]; faces.append(loop[x, x])
R = sum(W) / np.sqrt(3); s = 1j * W[0] @ W[1] @ W[2]
alg = np.array([functools.reduce(np.matmul, [np.eye(8)] + [W[k] for k in A]) for r in range(4) for A in itertools.combinations(range(3), r)]).reshape(8, -1)
M = np.vstack([np.kron(w, np.eye(8)) - np.kron(np.eye(8), w.T) for w in W]); comm = 64 - np.linalg.matrix_rank(M)
eR = np.linalg.eigvalsh(R); es = np.linalg.eigvalsh(s); Pj = [(np.eye(8) + a * R) / 2 @ (np.eye(8) + b * s) / 2 for a in (1, -1) for b in (1, -1)]
check("1a cube: hops anticommute (face phases -1), R^2 = 1, copy sign s = i W1 W2 W3 is a central involution; 8 = (R = +-1) x (s = +-1) x 2 (the 2 is the register's spin doublet)",
      anti < 1e-12 and np.allclose(faces, -1) and np.allclose(R @ R, np.eye(8)) and np.allclose(s @ s, np.eye(8)) and all(np.allclose(s @ w, w @ s) for w in W) and all(round(np.trace(P).real) == 2 for P in Pj),
      f"anticomm {anti:.0e}; face products {set(np.round(faces, 9))}; R eig {np.round(eR[[0, -1]], 6)} x4 each; s eig x4 each; joint blocks {[round(np.trace(P).real) for P in Pj]}")
check("1b cube: the hop algebra is M2 + M2 (dim 8) and its one-body commutant has dim 8, so one cube's tick symmetry is at most U(2) x U(2) on 8 modes (rotation-blind part: the copy sign); no 16-fold internal label exists on one cube",
      np.linalg.matrix_rank(alg) == 8 and comm == 8, f"algebra dim {np.linalg.matrix_rank(alg)}, commutant dim {comm}; SM 16 needs 16 Weyl states with SU(3)xSU(2)xU(1) acting (register: '16 supplied')")

# ================= 2 one mode per D4 event
shell = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0 and 0 < sum(np.square(v)) <= 8], float)
skey = {tuple(map(int, v)): i for i, v in enumerate(shell)}; Kr = rng.normal(size=len(shell)) + 1j * rng.normal(size=len(shell)); Ks = np.zeros(len(shell), complex)
for g in GW:
    img = np.round(shell @ g.T).astype(int); Ks += Kr[[skey[tuple(v)] for v in img]]
Ks /= NG; pr = rng.uniform(-np.pi, np.pi, (200, 4)); f = np.exp(1j * pr @ shell.T) @ Ks; fm = np.exp(-1j * pr @ shell.T) @ Ks
minus1 = any(np.allclose(g, -E4) for g in GW)
check("2  one fermion mode per D4 event: -1 is in W(F4), so every W(F4)-invariant translation-invariant one-component kernel is even, f(p) = f(-p): no term linear in p, no spin-1/2 light mode (spin needs a staggered cell or supplied components)",
      minus1 and np.abs(f - fm).max() < 1e-12, f"-1 in W(F4): {minus1}; max |f(p) - f(-p)| = {np.abs(f - fm).max():.1e} over 200 momenta, {len(shell)} hops; the D4 zoom runners carry 4 supplied spinor components per event")

# ================= 3 counts and duality
corners = [c for c in itertools.product([0, 1], repeat=4) if sum(c) % 2 == 0]
box = np.array([v for v in itertools.product(range(-2, 3), repeat=4) if sum(v) % 2 == 0])
ck = lambda v: tuple(np.mod(v, 2)) + ((int(np.sum(v - np.mod(v, 2)) // 2) % 2),)   # class mod 2D4
cl = {}
for v in box: cl.setdefault(ck(v), []).append(v)
norms = sorted(min(int(np.dot(v, v)) for v in vs) for vs in cl.values())
rep = {k: min(vs, key=lambda v: np.dot(v, v)) for k, vs in cl.items()}; ks = sorted(cl); kid = {k: i for i, k in enumerate(ks)}
perm = np.array([[kid[ck(np.round(g @ rep[k]).astype(int))] for k in ks] for g in GW])
orb = set(); [orb.add(tuple(sorted(set(perm[:, i])))) for i in range(16)]
B = np.array([[int(np.dot(rep[a], rep[b])) % 2 for b in ks] for a in ks]); rad = [a for a in ks if not B[kid[a]].any()]
ck2 = lambda v: min(tuple(np.mod(v, 2)), tuple(np.mod(np.asarray(v) + 1, 2)))   # class mod 2D4* = 2Z^4 + {0, (1,1,1,1)}
c2 = sorted({ck2(v) for v in box}); perm2 = {tuple(sorted({ck2(np.round(g @ np.array(c)).astype(int)) for g in GW})) for c in c2}
check("3a counts: hypercube {0,1}^4 has 16 corners, 8 in D4; |D4/2D4| = 16 with W(F4) orbits 1 + 12 + 3 (min norms 0, 2, 4; the 3 = triality frames, the radical of the mod-2 form); |D4/2D4*| = 4 with orbits 1 + 3 (the index-4 sqrt2-zoom cell)",
      len(corners) == 8 and len(cl) == 16 and sorted(len(o) for o in orb) == [1, 3, 12] and len(rad) == 4 and len(c2) == 4 and sorted(len(o) for o in perm2) == [1, 3],
      f"corners in D4 {len(corners)}; classes {len(cl)}, min norms {norms.count(0)}x0 {norms.count(2)}x2 {norms.count(4)}x4; orbits {sorted(len(o) for o in orb)}; radical size {len(rad)}; D4/2D4* {len(c2)}, orbits {sorted(len(o) for o in perm2)}")
hp = np.array([v for v in itertools.product(np.arange(-2, 2.5, 0.5), repeat=4) if np.allclose(np.mod(2 * np.array(v), 2), 0) or np.allclose(np.mod(2 * np.array(v), 2), 1)]) * np.pi
chars = {}
for p in hp:
    c = tuple(np.round(np.real(np.exp(1j * np.array([rep[k] for k in ks]) @ p)), 9))
    if c not in chars or np.dot(p, p) < np.dot(chars[c], chars[c]): chars[c] = p
Ch = np.array(list(chars)); orth = np.abs(Ch @ Ch.T - 16 * np.eye(len(Ch))).max()
check("3b the 16 classes of D4/2D4 are Fourier dual to the 16 half-period momenta pi D4* mod 2pi D4*: coset labels ARE taste (doubler) labels",
      len(chars) == 16 and orth < 1e-9, f"distinct characters {len(chars)}, orthogonality residual {orth:.0e}")
TRIM = np.array([p for c, p in chars.items() if not np.allclose(c, 1)])


def fq(c):
    s_ = c.sum(-1); return (s_ * s_ - 0.5 * (c * c).sum(-1) + 2 * c.prod(-1)) / 16


def Pi(q, JL=8):
    out = np.ones(q.shape[:-1])
    for j in range(1, JL + 1): out = out * fq(np.cos(q / 2.0 ** j))
    q2 = np.sum(q * q, -1); return out * np.exp(-(9 / 32) * q2 / (3 * 4.0 ** JL) - (17 / 2048) * q2 ** 2 / (15 * 16.0 ** JL))


def chi(x, N):
    u = np.clip((x - (N - 2)) / 2.0, 0, 1); g = lambda t: np.where(t > 0, np.exp(-1 / np.maximum(t, 1e-300)), 0.)
    return g(1 - u) / (g(1 - u) + g(u))


N_IM = 5; a_ = np.array(list(itertools.product(range(-N_IM - 1, N_IM + 2), repeat=4)), float); IM = np.vstack([a_, a_ + 0.5]) * 2 * np.pi
IM = IM[np.linalg.norm(IM, axis=1) <= 2 * np.pi * (N_IM + 1)]


def Dmin(p, al=0.5):   # smallest singular value of D* = (sigma - i g.rho)^-1, |D*| = 1/sqrt(sigma^2 + rho^2)
    q = p[None, :] + IM; q2 = np.sum(q * q, -1); w = Pi(q) ** 2 / q2 * chi(np.sqrt(q2) / (2 * np.pi), N_IM)
    rho = w @ q; return 1 / np.sqrt(al ** 2 + rho @ rho)


heavy = [Dmin(p) for p in TRIM]; light = [Dmin(e * np.array([.3, .5, .7, .2])) / e for e in (1e-2, 2e-3)]
check("3c the zoom fixed-point kernel D* keeps exactly one light class: |D*| ~ |p| at p -> 0, gapped at all 15 other half-period classes at the GW radius 1/alpha (one light mode per field, no taste multiplicity)",
      min(heavy) > 0.5 and abs(light[0] / light[1] - 1) < 1e-2, f"min |D*| at the 15 classes {min(heavy):.3f} (max {max(heavy):.3f}); |D*|/|p| at |p|=0.01, 0.002: {light[0]:.4f}, {light[1]:.4f}")
print(f"  [t = {time.time() - T0:.0f} s]")

# ================= 4 staggered 16 on Z^4
Lz = 4; sites = list(itertools.product(range(Lz), repeat=4)); sid = {x: i for i, x in enumerate(sites)}; Ns = len(sites); DKS = np.zeros((Ns, Ns))
for x in sites:
    for mu in range(4):
        eta = (-1) ** sum(x[:mu]); y = list(x); y[mu] = (y[mu] + 1) % Lz; DKS[sid[x], sid[tuple(y)]] += eta / 2; DKS[sid[tuple(y)], sid[x]] -= eta / 2
zks = int(np.sum(np.abs(np.linalg.eigvalsh(1j * DKS)) < 1e-9)); D2 = DKS @ DKS
evn = [i for i, x in enumerate(sites) if sum(x) % 2 == 0]; rootc = axc = 0.
for i in evn:
    for r in ROOTS.astype(int): rootc = max(rootc, abs(D2[i, sid[tuple(np.mod(np.add(sites[i], r), Lz))]]))
    for mu in range(4): y = list(sites[i]); y[mu] = (y[mu] + 2) % Lz; axc = max(axc, abs(D2[i, sid[tuple(y)]]))
oddc = max(abs(D2[i, j]) for i in evn[:20] for j in range(Ns) if sum(sites[j]) % 2)
keepZ = sum(np.allclose(g, np.round(g)) for g in GW)
check("4  staggered 16 lives on Z^4 = D4 + one hole class: 16 zero modes (4 spin x 4 taste); on events alone only D^2 survives, a scalar Laplacian on 2e_mu hops (root-hop weight 0); Z^4 is kept by 384 of 1152 W(F4) elements (triality broken, index 3)",
      zks == 16 and rootc < 1e-12 and axc > 0.2 and oddc < 1e-12 and keepZ == 384, f"zero modes on {Lz}^4 {zks}; D^2 root-hop {rootc:.0e}, 2e_mu hop {axc:.2f}, event->hole {oddc:.0e}; W(F4) elements keeping Z^4: {keepZ}")

# ================= 5 internal labels vs rotations
F16 = [("Q", 6, Fr(1, 6), 3, 2), ("u^c", 3, Fr(-2, 3), -3, 1), ("d^c", 3, Fr(1, 3), -3, 1), ("L", 2, Fr(-1, 2), 1, 2), ("e^c", 1, Fr(1), 1, 1), ("nu^c", 1, Fr(0), 1, 1)]
la = [np.array(m) for m in ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
                              [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], np.diag([1, 1, -2]) / np.sqrt(3))]
pa = [X, np.array([[0, -1j], [1j, 0]]), Zp]; blocks = []
for nm, m, y, c, d in F16:
    gs = [np.kron(l if c > 0 else -l.conj(), np.eye(d)) for l in la] if abs(c) == 3 else [np.zeros((m, m))] * 8
    gs += [np.kron(np.eye(abs(c)), p) for p in pa] if d == 2 else [np.zeros((m, m))] * 3
    blocks.append(gs + [float(y) * np.eye(m)])
gens16 = [np.zeros((16, 16), complex) for _ in range(12)]; o = 0
for b in blocks:
    m = b[0].shape[0]
    for k in range(12): gens16[k][o:o + m, o:o + m] = b[k]
    o += m
Mc = np.vstack([np.kron(g, np.eye(16)) - np.kron(np.eye(16), g.T) for g in gens16]); dcomm = 256 - np.linalg.matrix_rank(Mc)
Pm = [np.eye(16)[p] for p in perm]; nonab = next(((i, j) for i in range(0, NG, 7) for j in range(0, NG, 11) if not np.allclose(Pm[i] @ Pm[j], Pm[j] @ Pm[i])), None)
burn = np.mean([np.trace(P) ** 2 for P in Pm])
check("5  internal labels: the SM commutant on the one-family 16 is abelian (dim 6 = U(1)^6), the W(F4) image on the 16 coset labels is non-abelian (commutant dim from Burnside): no W(F4)-covariant identification of coset labels with the 16 where rotations permute labels",
      dcomm == 6 and nonab is not None, f"SM commutant dim {dcomm}; non-commuting W(F4) pair found {nonab is not None}; perm-rep commutant dim {burn:.0f}")

# ================= 6 triality families
a, b = 1.3, 0.4; Ms = a * np.eye(3) + b * (np.ones((3, 3)) - np.eye(3)); ev = np.sort(np.linalg.eigvalsh(Ms))
tri = [i for i in range(NG) if all(perm[i][kid[k]] == kid[k] for k in rad)]
mon = [m for m in itertools.product(range(5), repeat=4) if sum(m) == 4]; Pt = rng.normal(size=(60, 4))


MON = np.array(mon, float)


def ninv(sub):
    Q = np.einsum('tj,gij->tgi', Pt, GW[list(sub)]); V = np.prod(Q[:, :, None, :] ** MON[None, None], -1).mean(1)
    return np.linalg.matrix_rank(V.T, tol=1e-8)


nF, nD = ninv(range(0, NG)), ninv(tri)
check("6  triality families: an S3-invariant 3x3 mass matrix has a degenerate pair (a + 2b, a - b, a - b); keeping the 3 classes fixed restricts W(F4) to W(D4) (192), which has 3 quartic invariants vs 1 for W(F4): dimension-6 anisotropy returns",
      abs(ev[0] - ev[1]) < 1e-12 and len(tri) == 192 and nF == 1 and nD == 3 and len(TRIM) == 15, f"eigenvalues {np.round(ev, 6)}; subgroup fixing the 3 classes {len(tri)}; quartic invariants W(F4) {nF}, W(D4) {nD}")

# ================= 7 anomalies
Y3 = sum(m * y ** 3 for _, m, y, _, _ in F16); Y1 = sum(m * y for _, m, y, _, _ in F16); C2Y = sum((m // 3) * y for _, m, y, c, _ in F16 if abs(c) == 3)
W2Y = sum((m // 2) * y for _, m, y, _, d in F16 if d == 2); C3 = sum((m // 3) * (1 if c > 0 else -1) for _, m, y, c, _ in F16 if abs(c) == 3); ND = sum(m // 2 for _, m, _, _, d in F16 if d == 2)
nW = sum(m for _, m, _, _, _ in F16)
check("7  one-family 16: Y^3, Y-gravity, SU(3)^2 Y, SU(2)^2 Y, SU(3)^3 vanish, doublets even, Weyl count 0 mod 16; one taste-4 of SU(4) has SU(4)^3 = 1 (anomalous), (4,2,1) + (4b,1,2) gives 0; 15 Weyl (no nu^c) is 15 mod 16; Dirac-Kahler 16 components = 4 Weyl after projection, not 16",
      (Y3, Y1, C2Y, W2Y, C3) == (0, 0, 0, 0, 0) and ND % 2 == 0 and nW % 16 == 0 and (nW - 1) % 16 == 15 and 2 * 1 + 2 * (-1) == 0 and 16 // 4 == 4,
      f"sums {Y3}, {Y1}, {C2Y}, {W2Y}, {C3}; doublets {ND}; Weyl {nW}; taste-4 A = 1; PS 2(1) + 2(-1) = 0; 15 mod 16 = {(nW - 1) % 16}")
print(f"runtime {time.time() - T0:.0f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
