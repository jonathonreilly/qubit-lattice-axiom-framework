"""C8 check (b), (c), (e): antiunitary letters, exponential letters, L1, Pi-taste, scoping probes.
Own code on the B26 checker's model (mymodel.py); no C8 / b26lib / chklib / chk_model import."""
import os, sys, itertools, collections, time
os.environ.setdefault('OMP_NUM_THREADS', '3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mymodel import *
from scipy.linalg import expm
P = F = 0
def check(n, ok, d=""):
    global P, F; P += bool(ok); F += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {n}  {d}", flush=True)
t0 = time.time(); rng = np.random.default_rng(8802)
kst = np.array([1, -1, 1]) * np.pi / 2; PI = np.pi * np.ones(3); I12 = np.eye(12)
A0i = A0m.conj().T
def Rk(k): return bloch(RL, k)
def Rtk(k): return bloch(RTX, k)
def Ek(k, s=1, th=np.pi / 4): return np.cos(th) * I12 + 1j * s * np.sin(th) * Rk(k)
def letter(t, k):
    if not isinstance(t, str): return t
    if t == 'R': return Rk(k)
    if t == 'Rt': return Rtk(k)
    if t in ('S', 'Si', 'S2', 'S2i'): return Sk(k, {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}[t])
    if t == 'E+': return Ek(k, 1)
    if t == 'E-': return Ek(k, -1)
    if t == 'A0': return A0m
    raise KeyError(t)
def W(w, k):
    M = I12.astype(complex)
    for t in w: M = M @ letter(t, k)
    return M
def nS(w): return sum({'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}.get(t, 0) for t in w if isinstance(t, str))
def randword(rng, toks, n, onsite=True):
    w = [str(rng.choice(toks)) for _ in range(n)]
    return [rand_onsite_unitary(rng) if t == 'o' else t for t in w]
def specdist(A, B):
    a = np.sort_complex(np.round(np.linalg.eigvals(A), 9)); b = np.linalg.eigvals(B)
    # matching distance (greedy)
    b = list(b); d = 0
    for x in a:
        j = int(np.argmin([abs(x - y) for y in b])); d = max(d, abs(x - b[j])); b.pop(j)
    return d

# ================= (b) class 2: antiunitary letters
realok = all(np.abs(B.imag).max() < 1e-15 for X in (S1, RL, RTX) for B in X.values()) and np.abs(A0m.imag).max() < 1e-15 \
    and all(np.abs(g['U'].imag).max() == 0 for g in PSG)
check("S, R_L, Rt, A0 and the dressed rotation matrices are real (K commutes with them)", realok)
conjok = True; cmap = {}
for n, Lt in PC.items():
    hit = None
    for m, M in PC.items():
        z = np.vdot(M.flatten(), Lt.conj().flatten()) / 12
        if abs(abs(z) - 1) < 1e-9 and np.allclose(Lt.conj(), z * M): hit = (m, np.round(z, 6)); break
    conjok &= hit is not None; cmap[n] = hit
check("PC (80 letters) is closed under complex conjugation up to a global phase", conjok, f"e.g. L123* = {cmap['L123']}, H12* = {cmap['H12']}")
okv = okp = True
for _ in range(100):
    w = randword(rng, ['S', 'Si', 'S2', 'R', 'Rt', 'o'], int(rng.integers(2, 6)))
    wc = [t if isinstance(t, str) else t.conj() for t in w]
    k = rng.uniform(-np.pi, np.pi, 3)
    U2 = W(w, k) @ W(w, -k).conj()                         # Bloch form of V K V K  (K: k -> -k)
    U2w = W(w, k) @ W(wc, k)                               # V V*: the conjugated word
    okv &= np.allclose(U2, U2w)
    U2m = W(w, -k) @ W(w, k).conj()
    okp &= specdist(U2m, U2.conj()) < 1e-7
check("(VK)^2 = V V*, with V* = the word with conjugated letters (100 random old words)", okv)
check("spec (VK)^2(-k) = conj spec (VK)^2(k)", okp)
k = rng.uniform(-np.pi, np.pi, 3)
check("note: (E+ K)^2 = E+ E+* = E+ E- = 1 (E+* = E-, R_L real)", np.allclose(Ek(k, 1) @ Ek(-k, 1).conj(), I12))

# ================= (c) class 3
A0x = {Z0: A0m}
ExpA = {Z0: (I12 + A0m) / np.sqrt(2)}
uok = np.allclose(ExpA[Z0] @ ExpA[Z0].conj().T, I12)
cov = []
for g in PROPER:
    Y = conjG(g, ExpA)[Z0]
    exp_minus = (I12 + g['chi'] * A0m) / np.sqrt(2)
    z = np.vdot(ExpA[Z0].flatten(), Y.flatten()) / 12
    cov.append((g['chi'], np.allclose(Y, exp_minus), np.allclose(Y, z * ExpA[Z0]) and abs(abs(z) - 1) < 1e-9))
nT = sum(1 for c in cov if c[2]); oddbad = all((not c[2]) for c in cov if c[0] == -1)
check("exp(pi/4 A0) = (1+A0)/sqrt2 unitary; G exp G^-1 = exp(chi pi/4 A0); covariant up to a phase only for the 12 chi=+1 (T) rotations",
      uok and all(c[1] for c in cov) and nT == 12 and oddbad, f"covariant: {nT}/24")
k = rng.uniform(-np.pi, np.pi, 3); R = Rk(k)
ok = np.allclose(R @ R, I12) and np.allclose(R, R.conj().T)
Ep, Em = Ek(k, 1), Ek(k, -1)
ok &= np.allclose(Ep @ Ep.conj().T, I12) and np.allclose(Ep @ Em, I12) and np.allclose(Ep @ Ep, 1j * R) and np.allclose(Ep @ R, 1j * Em)
ok &= np.allclose(expm(1j * np.pi / 4 * R), Ep)
check("R_L^2 = 1, Hermitian; E+- = (1 +- i R_L)/sqrt2 = exp(+-i pi/4 R_L) unitary; E+E- = 1; E+^2 = i R_L; E+ R_L = i E-", ok)
okrt = all(np.allclose(expm(1j * s * np.pi / 4 * Rtk(k)), Sk(k, 1) @ Ek(k, -s) @ Sk(k, -1)) for s in (1, -1) for k in rng.uniform(-np.pi, np.pi, (5, 3)))
okrt &= all(np.allclose(Rtk(k), -Sk(k, 1) @ Rk(k) @ Sk(k, -1)) for k in rng.uniform(-np.pi, np.pi, (5, 3)))
check("Rt = -S R_L S^-1 and exp(+-i pi/4 Rt) = S E-+ S^-1", okrt)
Ex = {a: 1j * B / np.sqrt(2) for a, B in RL.items()}; Ex[Z0] = Ex.get(Z0, 0) + I12 / np.sqrt(2)
check("E+ is O-symmetric (G E+ G^-1 = E+ for all 24 dressed rotations)", all(bl_eq(conjG(g, Ex), Ex) for g in PROPER))
nnz = collections.Counter(); vals = set()
for c in range(12):
    nnz[sum(int(np.abs(B[:, c]).max() > 1e-12) * int(np.sum(np.abs(B[:, c]) > 1e-12)) for B in Ex.values())] += 1
    for B in Ex.values(): vals |= set(np.round(np.abs(B[:, c][np.abs(B[:, c]) > 1e-12]), 6))
check("E+ is not a phased permutation: 3 nonzeros per column, |entries| in {1/sqrt2, 1/2}", dict(nnz) == {3: 12} and vals == {0.707107, 0.5}, f"{dict(nnz)} {vals}")
# scalars on D+- at +-k*, zero compressed derivative
def compressed(Xf, k, D, h=1e-6):
    X = Xf(k); XD = D.conj().T @ X @ D
    pres = np.allclose(X @ D, D @ XD, atol=1e-9); sc = np.allclose(XD, XD[0, 0] * np.eye(2), atol=1e-9)
    hs = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G = (Xf(k + dk) - Xf(k - dk)) / (2 * h)
        hs.append(-1j * D.conj().T @ X.conj().T @ G @ D)
    return pres and sc, XD[0, 0], max(np.abs(x).max() for x in hs)
tab = []; okd = True
for nm, Xf in (('E+', lambda k: Ek(k, 1)), ('E-', lambda k: Ek(k, -1)), ('R_L', Rk), ('Rt', Rtk), ('S', lambda k: Sk(k, 1))):
    for kk, kn in ((kst, '+k*'), (-kst, '-k*')):
        for D, dn in ((DP, 'D+'), (DM, 'D-')):
            sc, val, hmax = compressed(Xf, kk, D); tab.append((nm, kn, dn, sc, np.round(val, 4), round(hmax, 4)))
            if nm != 'S': okd &= sc and hmax < 1e-8
for x in tab: print("   ", x)
check("E+-, R_L, Rt: scalars on D+ and D- at +-k* with zero compressed derivative (S: scalar 1, nonzero derivative)", okd)
# L1 for random E-words
def dpt(w, k, E, m_expect=None, h=1e-6):
    W0 = W(w, k); e, V = np.linalg.eig(W0); sel = np.abs(wrap(np.angle(e) - E)) < 1e-6; m = int(sel.sum())
    Q, _ = np.linalg.qr(V[:, sel]); hj = []
    for j in range(3):
        dk = np.zeros(3); dk[j] = h; G = (W(w, k + dk) - W(w, k - dk)) / (2 * h)
        x = -1j * np.exp(-1j * E) * Q.conj().T @ G @ Q; hj.append((x + x.conj().T) / 2)
    return m, Q, hj
def iso(hj):
    tr = max(abs(np.trace(x)) for x in hj); Gm = np.array([[np.trace(hj[i] @ hj[j]).real / len(hj[0]) for j in range(3)] for i in range(3)])
    v2 = np.trace(Gm) / 3; return tr, np.abs(Gm - v2 * np.eye(3)).max(), np.sqrt(max(v2, 0))
worst = 0; nlev = 0; okl = True; n4 = 0
for _ in range(250):
    w = randword(rng, ['S', 'Si', 'S2', 'S2i', 'R', 'Rt', 'E+', 'E-', 'o'], int(rng.integers(3, 8)))
    W0 = W(w, kst); e = np.linalg.eigvals(W0); vs = abs(nS(w)) * np.sqrt(2) / 3
    for D in (DP, DM):
        lam = (D.conj().T @ W0 @ D)[0, 0]; E = np.angle(lam)
        m, Q, hj = dpt(w, kst, E)
        if m == 2:
            tr, an, v = iso(hj); worst = max(worst, tr, an, abs(v - vs)); nlev += 1
        elif m == 4: n4 += 1
check("L1 for E-words (250 random words incl. S, R_L, Rt, E+-, random symmetric on-site unitaries): 2-fold D+/D- levels are untilted isotropic cones at |n_S| sqrt2/3",
      worst < 1e-6, f"{nlev} levels, worst deviation {worst:.1e} ({n4} D+-coincident 4-fold levels skipped)")
# letter rules
okr = True
for k in rng.uniform(-np.pi, np.pi, (5, 3)):
    okr &= np.allclose(Ek(k + PI, 1), Ek(k, -1)) and np.allclose(Ek(k, 1).T, Ek(-k, 1)) and np.allclose(Rk(k).T, Rk(-k))
check("E(k+Pi) = E-+(k) (D_Pi conjugation flips R_L); E(k)^T = E(-k), R_L(k)^T = R_L(-k)", okr)
# does the Pi spectral taste survive in E-words?  (C8: 'E letters break the universal Pi-taste, -k* is no longer a copy of k*')
cnt = collections.Counter(); ex_keep = None
for _ in range(200):
    w = randword(rng, ['S', 'Si', 'S2', 'R', 'Rt', 'E+', 'E-', 'o'], int(rng.integers(3, 7)))
    if not any(isinstance(t, str) and t[0] == 'E' for t in w): continue
    ks = rng.uniform(-np.pi, np.pi, (3, 3))
    keep = all(specdist(W(w, k + PI), W(w, k)) < 1e-7 for k in ks)
    keepm = all(specdist(W(w, k + PI), -W(w, k)) < 1e-7 for k in ks)
    cnt['Pi taste (omega=+1)' if keep else ('Pi taste (omega=-1)' if keepm else 'no Pi taste')] += 1
    if (keep or keepm) and ex_keep is None: ex_keep = [t if isinstance(t, str) else 'o' for t in w]
print("   random E-words, spectral Pi taste:", dict(cnt), "example with Pi taste:", ex_keep)
# a structural family that keeps it exactly: words where E+ and E- occur in D_Pi-related pairs, e.g. W = E+ o E- o'
w = ['E+', rand_onsite_unitary(rng), 'S', 'E-', rand_onsite_unitary(rng), 'Si', 'S2']
ks = rng.uniform(-np.pi, np.pi, (3, 3))
kp = [specdist(W(w, k + PI), W(w, k)) for k in ks]
print("   E+ o S E- o Si S2: spec distance W(k+Pi) vs W(k):", np.round(kp, 3))
check("Pi spectral taste is not universal for E-words but survives in a fraction of them (C8's 'no longer a copy' needs 'in general')",
      cnt['no Pi taste'] > 0 and (cnt['Pi taste (omega=+1)'] + cnt['Pi taste (omega=-1)']) > 0, f"{dict(cnt)}")

# ================= (e) scoping probes: other natural non-monomial O-symmetric involutions
ks = rng.uniform(-np.pi, np.pi, (4, 3))
def rel(A, B):
    c = max(np.abs(A @ B - B @ A).max() for A, B in [(A(k), B(k)) for k in ks]); a = max(np.abs(A @ B + B @ A).max() for A, B in [(A(k), B(k)) for k in ks])
    return 'commute' if c < 1e-9 else ('anticommute' if a < 1e-9 else f'neither (|[,]|={c:.2f}, |{{,}}|={a:.2f})')
S2R = lambda k: Sk(k, 2) @ Rk(k) @ Sk(k, -2)
pairs = {'R_L,Rt': rel(Rk, Rtk), 'R_L,S2 R_L S-2': rel(Rk, S2R), 'R_L,H_on': rel(Rk, lambda k: HON0), 'R_L,Lambda': rel(Rk, lambda k: LAM),
         'Rt,H_on': rel(Rtk, lambda k: HON0), 'H_on,H_link': rel(lambda k: HON0, lambda k: bloch(HLINK, k))}
for a, b in pairs.items(): print(f"   {a}: {b}")
s2rold = any(np.allclose(S2R(ks[0]), z * X) for z in (1, -1) for X in (Rk(ks[0]), Rtk(ks[0])))
check("S^2 R_L S^-2 is not +-R_L or +-Rt (a further Hermitian involution, but an S-conjugate, so exp(i pi/4 .) = S^2 E S^-2 is generated)", not s2rold)
# symmetric on-site operators commuting with R_L(k) for all k (would give involutions R_L P + (1-P))
rows = []
for k in ks:
    R = Rk(k); rows.append(np.array([(R @ B - B @ R).flatten() for B in ONB]).T)
A = np.vstack(rows); sv = np.linalg.svd(A, compute_uv=False); dimc = int(np.sum(sv < 1e-9)) + max(0, len(ONB) - len(sv))
check("on-site symmetric algebra elements commuting with R_L(k) for all k: only the scalars (no R_L P + (1-P) involutions)", dimc == 1, f"commutant dim {dimc}")
# rotation angle family: exp(i theta R_L) for theta in (pi/6)Z is O-symmetric, parameter-free, not generated by E+- and R_L
th = np.pi / 6; k = ks[0]; E6 = Ek(k, 1, th)
gen = [z * np.linalg.matrix_power(Ek(k, 1), n) for n in range(8) for z in [np.exp(1j * np.pi * m / 6) for m in range(12)]]
check("exp(i pi/6 R_L) is unitary, O-symmetric, and not z * E+^n for any n, z in 12th roots (outside the E-word letter set)",
      np.allclose(E6 @ E6.conj().T, I12) and not any(np.allclose(E6, G_) for G_ in gen))
# its taste behaviour: exp(i th R)(k+Pi) = exp(-i th R)(k); L1 still holds (function of R_L)
okt = np.allclose(Ek(k + PI, 1, th), Ek(k, -1, th))
sc, val, hmax = compressed(lambda q: Ek(q, 1, th), kst, DP)
check("exp(i pi/6 R_L): Pi-taste flip and scalar on D+ at k* with zero compressed derivative (no velocity source)", okt and sc and hmax < 1e-8)
# H = H_on + H_link: is a normalised version an involution? (spectrum of H(k) at random k)
sp = np.round(np.linalg.eigvalsh(HON0 + bloch(HLINK, ks[0])), 4)
print("   spec(H_on + H_link) at a random k:", sp)
check("the full nearest-neighbour hop H_on + H_link is not proportional to an involution (k-dependent spectrum), so exp(i pi/4 .) needs a parameter",
      len(set(np.abs(sp))) > 1)
print(f"\nTOTAL: PASS={P} FAIL={F}   [{time.time() - t0:.0f}s]")
