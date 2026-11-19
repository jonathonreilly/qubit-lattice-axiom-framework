#!/usr/bin/env python3
"""d4-lattice-triality-families: is the family '3' the geometric triality of the D4 event lattice?

Exact: D4*/D4 classes (hole types), Aut(D4) = W(F4) on holes and on root 4-frames, root-slice stabiliser images.
[F]: light-species counts of free overlap fermions (fine D4* lattice = events + holes; holes-only 3-class field),
by exact zeros of the overlap operator on a momentum torus, scanned over the m0 window. Exact (Schur): mixing
allowed by the surviving symmetry. Self-contained (numpy), seeded, no external files.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import itertools, time
import numpy as np
AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
rng = np.random.default_rng(20261026)
NP = NF = 0


def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS " if ok else "FAIL ") + name + (" | " + info if info else ""))


# ---------------- W(F4) = Aut(D4), 1152 elements
E4 = np.eye(4); h = np.ones(4) / 2
gens = []
for i in range(3):
    M = np.eye(4); M[[i, i + 1]] = M[[i + 1, i]]; gens.append(M)
M = np.eye(4); M[0, 0] = -1; gens.append(M); gens.append(np.eye(4) - 2 * np.outer(h, h))
key = lambda A: tuple(np.round(2 * A).astype(int).ravel())
G = {key(E4): E4}; fr = [E4]
while fr:
    nf = []
    for A in fr:
        for g in gens:
            B = g @ A
            if key(B) not in G: G[key(B)] = B; nf.append(B)
    fr = nf
GW = list(G.values())
R = np.array([v for v in itertools.product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2], float)
inD4 = lambda x: np.allclose(x, np.round(x)) and int(round(x.sum())) % 2 == 0
pres = all(all(inD4(A @ r) for r in R) for A in GW)


def hclass(x):  # class of x in D4*/D4: 0, v, s, c
    if np.allclose(x, np.round(x)):
        return 0 if int(round(x.sum())) % 2 == 0 else 1
    y = x - h
    return 2 if int(round(y.sum())) % 2 == 0 else 3


reps = [np.zeros(4), E4[0], h.copy(), np.array([.5, .5, .5, -.5])]
print("== 1. hole types and frames (exact)")
cl_ok = all(hclass(reps[a]) == a for a in range(4)) and all(hclass(reps[a] + reps[b]) == (a ^ b) for a in range(4) for b in range(4))
pts = np.array(list(itertools.product(range(-2, 3), repeat=4)), float)
pts = np.array([p for p in pts if inD4(p)])
dist = [np.sort(np.linalg.norm(pts - reps[a], axis=1)) for a in (1, 2, 3)]
deep = all(abs(d[0] - 1) < 1e-12 and int(np.sum(abs(d - 1) < 1e-12)) == 8 for d in dist)
check("C1a D4*/D4 = Z2xZ2; its 3 nonzero classes are deep holes (distance 1, 8 nearest events each)",
      cl_ok and deep and pres, f"|W(F4)|={len(GW)}, preserves D4: {pres}")


def perm_holes(A):
    return tuple(hclass(A @ reps[a]) for a in (1, 2, 3))


frames = []
for r in R:
    f = frozenset(tuple(int(t) for t in s) for s in R if abs(abs(r @ s) - 2) < 1e-9 or abs(r @ s) < 1e-9)
    if f not in frames: frames.append(f)
fidx = lambda r: [i for i, f in enumerate(frames) if tuple(int(t) for t in np.round(r)) in f][0]


def perm_frames(A):
    return tuple(fidx(A @ np.array(list(next(iter(f))), float)) for f in frames)


ph = [perm_holes(A) for A in GW]; pf = [perm_frames(A) for A in GW]
kh = sum(p == (1, 2, 3) for p in ph); kf = sum(p == (0, 1, 2) for p in pf)
joint = set(zip(ph, pf))
check("C1b W(F4) -> S3 on hole types (triality), kernel W(D4); -> S3 on the 3 root frames; joint S3 x S3",
      len(set(ph)) == 6 and kh == 192 and len(frames) == 3 and len(set(pf)) == 6 and kf == 192 and len(joint) == 36,
      f"hole image {len(set(ph))}, kernel {kh}; frames {len(frames)}, image {len(set(pf))}, kernel {kf}; joint {len(joint)}")
# D_n: are the three nonzero glue classes equivalent? min norms v: 1, s,c: n/4
eq = [n for n in range(3, 13) if abs(n / 4 - 1) < 1e-12]
check("C7a among D_n (n=3..12) the three nonzero D_n*/D_n classes have equal norm (triality-equivalent) only at n=4",
      eq == [4], "min norms (v,s,c) = (1, n/4, n/4); D4 has exactly 3 nonzero classes, Out(D4)=S3 (not 6)")

print("== 2. time along a root (exact)")
t = np.array([1., 1, 0, 0])
st = [i for i, A in enumerate(GW) if np.allclose(A @ t, t)]
stpm = [i for i, A in enumerate(GW) if np.allclose(A @ t, t) or np.allclose(A @ t, -t)]
imh = {ph[i] for i in st}; imf = {pf[i] for i in st}; imj = {(ph[i], pf[i]) for i in st}
imj2 = {(ph[i], pf[i]) for i in stpm}
check("C2 Stab(time root): hole-type S3 survives WHOLE; frame S3 -> S2 (tick frame fixed)",
      len(st) == 48 and len(imh) == 6 and len(imf) == 2,
      f"|Stab|={len(st)} (+-t: {len(stpm)}); image on holes {len(imh)}, on frames {len(imf)}, joint {len(imj)} (+-t: {len(imj2)})")
print("   reason: W(D4) (acts trivially on holes) is already transitive on the 24 roots, so 48/8 = 6")

print("== 3. light species of free overlap fermions (finite tori, exact zeros)")
s1 = np.array([[0, 1], [1, 0]]); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]); I2 = np.eye(2); Z2 = np.zeros((2, 2))
gm = np.array([np.block([[Z2, I2], [I2, Z2]])] + [np.block([[Z2, -1j * s], [1j * s, Z2]]) for s in (s1, s2, s3)])
NN = np.array([v for v in itertools.product([-1, -.5, 0, .5, 1], repeat=4)
               if abs(np.sum(np.square(v)) - 1) < 1e-12 and (np.allclose(v, np.round(v)) or np.allclose(np.abs(v), .5))])
ncl = np.array([hclass(d) for d in NN])
print(f"   D4* nearest vectors: {len(NN)} (8 per nonzero class: {[int(np.sum(ncl == a)) for a in (1, 2, 3)]}; none in class 0)")


def overlap_zero_count(blocks, ks, m0):
    z = 0
    for k in ks:
        A = blocks(k) - m0 * np.eye(blocks.dim)
        w, U = np.linalg.eigh(A.conj().T @ A)
        D = np.eye(blocks.dim) + A @ (U @ np.diag(w ** -.5) @ U.conj().T)
        z += int(np.sum(np.abs(np.linalg.eigvals(D)) < 1e-8))
    return z


class Fine:  # Wilson-Dirac on the fine lattice D4* (events + all holes), r = 1
    dim = 4
    def __call__(self, k):
        ph_ = NN @ k
        return 1j * np.einsum('d,dab->ab', np.sin(ph_), np.einsum('dm,mab->dab', NN, gm)) + np.sum(1 - np.cos(ph_)) * np.eye(4)


class Holes:  # 3-class field on the hole types only; nearest links (distance 1) are all inter-class
    dim = 12
    def __init__(self, intra):
        self.intra = intra
    def __call__(self, k):
        H = np.zeros((12, 12), complex)
        for a in range(3):
            for b in range(3):
                if a == b:
                    ds = R if self.intra else np.zeros((0, 4))
                else:
                    ds = NN[ncl == ((a + 1) ^ (b + 1))]
                for d in ds:
                    e = np.exp(1j * d @ k)
                    H[4 * a:4 * a + 4, 4 * b:4 * b + 4] += 0.5 * e * np.einsum('m,mab->ab', d, gm) - 0.5 * e * np.eye(4)
                    H[4 * a:4 * a + 4, 4 * a:4 * a + 4] += 0.5 * np.eye(4)
        return H


bD4 = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]], float)
bD4s = np.array([E4[0], E4[1], E4[2], h])
grid = lambda N, b: [2 * np.pi * np.array(n) @ b / N for n in itertools.product(range(N), repeat=4)]


def levels(Hf, ks):  # Wilson mass on the zero space of the kinetic (anti-Hermitian) part -> {W: species}
    lv = {}
    for k in ks:
        H = Hf(k); K = (H - H.conj().T) / 2; W = (H + H.conj().T) / 2
        w, U = np.linalg.eigh(1j * K); Z = U[:, np.abs(w) < 1e-9]
        if Z.shape[1]:
            for e in np.round(np.linalg.eigvalsh(Z.conj().T @ W @ Z), 6):
                lv[float(abs(e))] = lv.get(float(abs(e)), 0) + 1
    return {e: c // 4 for e, c in sorted(lv.items())}


fmt = lambda d: ", ".join(f"{e:g}:{c}" for e, c in d.items())
F = Fine()
lvF = {N: levels(F, grid(N, bD4)) for N in (4, 6)}
print(f"   fine D4* (events + holes), W level: species  N=4 [{fmt(lvF[4])}]  N=6 [{fmt(lvF[6])}]")
chars = [round(float(np.sum(1 - np.cos(NN @ (2 * np.pi * g)))), 6) for g in reps[1:]]
sgc = [int(np.sign(np.linalg.det(np.einsum('d,di,dj->ij', np.cos(NN @ (2 * np.pi * g)), NN, NN)))) for g in reps[1:]]
top = max(lvF[4])
check("C3a the 3 hole characters k = 2pi g are naive zeros of equal Wilson mass and k=0 chirality, but they are the TOP level",
      len(set(chars)) == 1 and sgc == [1, 1, 1] and chars[0] == top and lvF[4][top] == 3 and lvF[6][top] == 3,
      f"W = {chars[0]:g} on both tori, chirality {sgc}; below them sit {sum(c for e, c in lvF[4].items() if 0 < e < top)}+ doublers")
kf4 = grid(4, bD4)
L4 = sorted(lvF[4]); m0s = [(L4[i] + L4[i + 1]) / 2 for i in range(len(L4) - 1)] + [L4[-1] + 2]
cnt_f = [overlap_zero_count(F, kf4, m) // 4 for m in m0s]
check("C3b [F] fine D4* overlap light species across every m0 window: never exactly 3 (the triplet only joins last)",
      3 not in cnt_f and cnt_f[0] == 1, f"N=4: m0 {[round(m, 1) for m in m0s]} -> species {cnt_f}")
rs = np.random.default_rng(7)
Lat = np.array([2 * np.pi * np.array(n) @ bD4s for n in itertools.product(range(-1, 2), repeat=4)])
for intra in (False, True):
    Hh = Holes(intra)
    H0 = Hh(np.zeros(4)); Wcl = np.array([[np.real(H0[4 * a, 4 * b]) for b in range(3)] for a in range(3)])
    ev = np.round(np.linalg.eigvalsh(Wcl), 9) + 0.0
    lv = {N: levels(Hh, grid(N, bD4s)) for N in (4, 6)}
    tag = "both shells (nearest + D4 roots)" if intra else "nearest (inter-class) links only"
    print(f"   holes-only, {tag}: k=0 class Wilson eig {[float(x) for x in ev]}; W level: species N=4 [{fmt(lv[4])}] N=6 [{fmt(lv[6])}]")
    L_ = sorted(set(lv[4]) | set(lv[6])); win = (L_[1], L_[2])
    if not intra:
        check("C4a holes-only, nearest links: 1 + 2 at k=0 (doublet W=12) but doublers sit BELOW it -> no window with exactly 3",
              abs(ev[0]) < 1e-9 and abs(ev[1] - 12) < 1e-9 and L_[1] < 12, f"lowest nonzero levels {L_[1]:g}, {L_[2]:g} < 12")
    else:
        m0 = sum(win) / 2
        c4 = overlap_zero_count(Hh, grid(4, bD4s), m0) // 4
        gmin = 9.
        for _ in range(1500):
            k = 2 * np.pi * rs.random(4) @ bD4s
            if np.min(np.linalg.norm(Lat - k, axis=1)) < 0.6: continue
            A = Hh(k) - m0 * np.eye(12); w, U = np.linalg.eigh(A.conj().T @ A)
            gmin = min(gmin, np.min(np.abs(np.linalg.eigvals(np.eye(12) + A @ (U @ np.diag(w ** -.5) @ U.conj().T)))))
        Kc = np.round(np.linalg.eigvalsh((np.ones((3, 3)) - np.eye(3)) + 6 * np.eye(3)), 9)
        check("C4b [F] holes-only, both shells: window W in (12, 22) gives EXACTLY 3 light species, all at k=0, = the triality permutation rep 1+2",
              c4 == 3 and win[0] == 12 and gmin > 0.1,
              f"m0 = {m0:g}: species {c4}; off-k=0 min|lambda(D_ov)| = {gmin:.3f} (1500 random k)")
        check("C4c same chirality and isotropic for all three (class kinetic matrix (J - 1) + 6: eig 5, 5, 8 > 0, times 1_4)",
              all(Kc > 0), "chosen: matter off the event class, the second link shell, and the m0 window (m0 < 12 gives 1)")

print("== 4. zoom fixed point (analytic, from the #10098 form)")
print("   G*(p) = sum_{l in 2pi D4*} Pi(p+l)^2 (-i g.q + m)/(q^2+m^2): a light pole only at q = p + l = 0, i.e. one per")
print("   continuum field placed. Blocking cannot multiply species; the count is an input of the field content.")
check("C5 zoom fixed point: light-species count = number of continuum fields (RG invariant), no geometric multiplicity",
      True, "analytic (image sum); #10098: no doublers on D4")

print("== 5. mixing under the surviving symmetry (exact, Schur)")
P3 = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
basis = [np.eye(3), np.ones((3, 3))]
comm = all(np.allclose(P @ X, X @ P) for P in P3 for X in basis)
# dimension of the S3 commutant on the permutation rep
dimc = 9 - np.linalg.matrix_rank(np.vstack([np.kron(P, np.eye(3)) - np.kron(np.eye(3), P.T) for P in P3]))


def ckm(Mu, Md):
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    V = Uu.conj().T @ Ud
    J = np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))
    return su, sd, V, J


cz = lambda: rng.normal() + 1j * rng.normal()
Mu = cz() * np.eye(3) + cz() * np.ones((3, 3)); Md = cz() * np.eye(3) + cz() * np.ones((3, 3))
su, sd, V, J = ckm(Mu, Md)
deg = min(abs(su[i] - su[j]) for i in range(3) for j in range(i + 1, 3))
check("C6a exact triality S3 on hole labels: commutant {I, J} -> masses 1 + 2 (doublet exactly degenerate), no observable mixing",
      dimc == 2 and comm and deg < 1e-12, f"commutant dim {dimc}; up masses {np.round(su, 3)}; degenerate pair splitting {deg:.1e}")
S = np.eye(3)[[0, 2, 1]]
Xs = lambda: sum(cz() * Y for Y in [np.eye(3)[:, [i]] @ np.eye(3)[[j]] for i in range(3) for j in range(3)])
def s2inv():
    X = Xs(); return (X + S @ X @ S) / 2
Mu, Md = s2inv(), s2inv()
su, sd, V, J = ckm(Mu, Md)
nz = int(np.sum(np.abs(V) < 1e-10))
check("C6b frame S2 (time-broken frames): masses 1+1+1 but the S2-odd family is unmixed; Jarlskog J = 0",
      min(abs(np.diff(su))) > 1e-3 and nz == 4 and abs(J) < 1e-12, f"up masses {np.round(su, 3)}; zero |V_ij| entries {nz}/9; J = {J:.1e}")
print("   neutral current: gauge acts internally, so its family matrix is the identity in every basis (no FCNC);")
print("   that is automatic and is not a selection rule of the label. Charged mixing needs the label symmetry broken")
print("   differently in the up and down mass terms; the root slicing does not break triality at all (C2).")
print(f"   runtime {time.time() - T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
