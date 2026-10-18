#!/usr/bin/env python3
"""C8 parts 2-3 (exact/finite checks): antiunitary steps and parameter-free non-permutation letters.
Model: c8lib (b26lib/chklib/chk_model, read-only).
(2) K (complex conjugation in the real-space mode basis) commutes with every dressed rotation; S, R_L, A0 are real; the
    Clifford palette PC is closed under conjugation up to a global phase.  So for an antiunitary step U = V K with V an
    old-palette word, U^2 = V V* is again an old-palette word; and spec U^2(-k) = conj spec U^2(k).
(3) E+- = exp(+-i pi/4 R_L) = (1 +- i R_L)/sqrt2: unitary, O-symmetric, translation invariant, not a phased permutation;
    E+E- = 1, E+^2 = i R_L, E+ R_L = i E-; exp(i th Rt) = S exp(-i th R_L) S^-1.  exp(th A0) is only T-covariant
    (G e^{th A0} G^-1 = e^{chi th A0}); excluded.  At +-k*: E is scalar on D+, D- with zero compressed derivative (L1 extends);
    random-word check of L1 with E letters; letter gauge and transpose rules; spectral-taste lattice census of E-words."""
import sys, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
t0 = time.time()
from c8lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(8)
KS = rng.uniform(-np.pi, np.pi, (6, 3))

# ---------------- (2) antiunitary
check("dressed rotations and translations are real signed permutations (K commutes with every G_g)", all(set(np.unique(s)) <= {0, 1} for P, s in rots + trans))
A0r = onsite_real(A0)
check("S, R_L, A0 are real in the real-space mode basis (so K S K = S, K R_L K = R_L, K A0 K = A0)",
      np.allclose(np.imag(Sr), 0) and np.allclose(np.imag(RLr), 0) and np.allclose(np.imag(A0r), 0))
def in_PC_upto_phase(M):
    for nm, X in PC.items():
        z = np.vdot(X.ravel(), M.ravel()) / 12
        if abs(abs(z) - 1) < 1e-9 and np.allclose(M, z * X): return nm
    return None
conj_ok = all(in_PC_upto_phase(np.conj(X)) is not None for X in PC.values())
check("the 80-letter Clifford palette PC is closed under complex conjugation up to a global phase", conj_ok)
# Bloch: (K X K)(k) = conj X(-k) for translation-invariant X with these conventions
ok = True; okspec = True
for _ in range(10):
    w = [PC[list(PC)[i]] if i < 80 else ['S', 'Si', 'R', 'Rt', 'S2'][i - 80] for i in rng.integers(0, 85, 5)]
    wc = [np.conj(L) if not isinstance(L, str) else L for L in w]
    for k in KS[:3]:
        V = Wb(w, k[None])[0]; Vs = np.conj(Wb(w, -k[None])[0])
        ok &= np.allclose(Vs, Wb(wc, k[None])[0])
        U2k = V @ Vs; U2mk = Wb(w, -k[None])[0] @ np.conj(Wb(w, k[None])[0])
        a = np.sort(np.mod(np.angle(np.linalg.eigvals(U2mk)), 2 * np.pi)); b = np.sort(np.mod(-np.angle(np.linalg.eigvals(U2k)), 2 * np.pi))
        okspec &= np.allclose(a, b, atol=1e-8) or np.allclose(np.sort(np.mod(a + 1e-9, 2 * np.pi)), np.sort(np.mod(b + 1e-9, 2 * np.pi)), atol=1e-7)
check("(V K)^2 = V V* with V*(k) = conj V(-k) = the word with every on-site letter conjugated (an old-palette word)", ok)
check("spec (VK)^2(-k) = conj spec (VK)^2(k) (the antiunitary step pairs E <-> -E, k <-> -k)", okspec)

# ---------------- (3) E letters
ok = all(np.allclose(RLk(k) @ RLk(k), np.eye(12)) for k in KS)
Ep = lambda k: (np.eye(12) + 1j * RLk(k)) / np.sqrt(2); Em = lambda k: (np.eye(12) - 1j * RLk(k)) / np.sqrt(2)
uni = all(np.allclose(Ep(k) @ Ep(k).conj().T, np.eye(12)) for k in KS)
rel = all(np.allclose(Ep(k) @ Em(k), np.eye(12)) and np.allclose(Ep(k) @ Ep(k), 1j * RLk(k)) and np.allclose(Ep(k) @ RLk(k), 1j * Em(k)) for k in KS)
check("R_L(k)^2 = 1, E+- unitary, E+E- = 1, E+^2 = i R_L, E+ R_L = i E-", ok and uni and rel)
Er = (np.eye(nV) + 1j * RLr) / np.sqrt(2)
symE = all(np.allclose(conj(Er, P, s), Er) for P, s in rots + trans)
nz = np.abs(Er[np.abs(Er) > 1e-12])
check("E+ is O-symmetric and translation invariant in real space; not a phased permutation (3 nonzeros per column, |entries| in {1/sqrt2, 1/2})",
      symE and np.allclose(sorted(set(np.round(nz, 9))), [0.5, 1 / np.sqrt(2)]) and int((np.abs(Er[:, 0]) > 1e-12).sum()) == 3)
St = lambda k: Sk(k)
check("exp(+-i pi/4 Rt) = S E-+ S^-1 (so Rt-exponentials add nothing beyond E+-)",
      all(np.allclose((np.eye(12) + 1j * RLt(k)) / np.sqrt(2), St(k) @ Em(k) @ St(k).conj().T) for k in KS))
# exp(theta A0)
EA = (np.eye(12) + A0) / np.sqrt(2); EAr = onsite_real(EA); EAmr = onsite_real((np.eye(12) - A0) / np.sqrt(2))
cov = all(np.allclose(conj(EAr, P, s), EAr if ch > 0 else EAmr) for (P, s), ch in zip(rots, CHI))
notchar = not any(np.allclose(EA, z * (np.eye(12) - A0) / np.sqrt(2)) for z in (1, -1, 1j, -1j))
check("exp(pi/4 A0) = (1 + A0)/sqrt2 is unitary and G_g exp(pi/4 A0) G_g^-1 = exp(chi_A2(g) pi/4 A0), which is not a phase times exp(pi/4 A0): only T-covariant",
      np.allclose(EA @ EA.conj().T, np.eye(12)) and cov and notchar)
# on-site symmetric involutions: exp(i pi/4 (1-2P)) for P a sum of PH or PLm projectors is in PC up to phase
okc = True
for Ps in (PH, PLm):
    for r in range(1, len(Ps)):
        for sub in itertools.combinations(range(len(Ps)), r):
            P = sum(Ps[i] for i in sub); X = np.eye(12) - 2 * P
            okc &= in_PC_upto_phase(sla.expm(1j * np.pi / 4 * X)) is not None
check("exp(i pi/4 (1-2P)) for every sum P of H_on- or Lambda-eigenprojectors lies in PC up to a phase (old Clifford letter)", okc)
# L1 extension at +-k*
fgE = lambda s: (lambda k: letter_grad2('E+' if s > 0 else 'E-', k))
okL = True
for kk in (kst, -kst):
    for D in (Dp, Dm):
        for s in (1, -1):
            isc, sc, h = compressed_velocity(fgE(s), kk, D); okL &= isc and max(np.abs(x).max() for x in h) < 1e-12
check("E+- at +-k*: scalar on D+ and on D-, zero compressed derivative (functional calculus of R_L)", okL)
# random words with E letters: every 2-fold D+/D- level at k* has speed |n_S| sqrt2/3
TOK = ['S', 'Si', 'S2', 'S2i', 'R', 'Rt', 'E+', 'E-']
okw = True; nlev = 0; worst = 0.0
for it in range(300):
    n = rng.integers(3, 7); w = []
    for _ in range(n):
        if rng.random() < 0.4: w.append(rand_onsite_unitary(rng))
        else: w.append(TOK[rng.integers(0, len(TOK))])
    if not any(isinstance(x, str) and x[0] == 'E' for x in w): w.append('E+')
    W0, G_ = W_grad2(w, kst); e, V = np.linalg.eig(W0)
    for E, m in levels(W0):
        if m != 2: continue
        Vd = V[:, np.abs(wrap(np.angle(e) - E)) < 1e-6]; Q, _ = np.linalg.qr(Vd)
        if not (np.linalg.norm(Q.conj().T @ Dp) ** 2 > 1.999 or np.linalg.norm(Q.conj().T @ Dm) ** 2 > 1.999): continue
        h = [-1j * np.exp(-1j * E) * Q.conj().T @ G_[j] @ Q for j in range(3)]
        iso, v = iso_speed(h); nlev += 1; dev = abs(v - abs(nS2(w)) * np.sqrt(2) / 3); worst = max(worst, dev)
        okw &= iso and dev < 1e-8
check("L1 with E letters (random words, random symmetric on-site unitaries): every 2-fold D+/D- level at k* is an isotropic cone at |n_S| sqrt2/3",
      okw and nlev > 50, f"{nlev} levels, worst deviation {worst:.1e}")
# gauge and transpose rules
okg = True
for k in KS[:3]:
    for t in [np.array([np.pi / 2, 0, 0]), np.array([np.pi / 4, np.pi / 4, 0]), np.array([0.3, -0.2, 0.9])]:
        Dt = np.diag(np.exp(-1j * (fc @ t) / 2))
        okg &= np.allclose(RLk(k + t), Dt @ RLk(k) @ Dt.conj().T) and np.allclose(Ep(k + t), Dt @ Ep(k) @ Dt.conj().T)
    okg &= np.allclose(Ep(k).T, Ep(-k))
check("letter rules: R_L(k+t) = D_t R_L(k) D_t^-1 and E(k+t) = D_t E(k) D_t^-1 (D_t = diag e^{-i t.f_c/2}); E(k)^T = E(-k)", okg)

# ---------------- spectral-taste lattice census of random E-words (U/T kind: spec W(k+t) = w spec W(k), w = +-1)
GR = np.array(list(itertools.product(range(8), repeat=3))) * np.pi / 4
KT = rng.uniform(-np.pi, np.pi, (3, 3))
def spec(W): return np.sort_complex(np.round(np.linalg.eigvals(W), 7))
def taste_lattice(w):
    base = [np.sort(np.mod(np.angle(np.linalg.eigvals(Wb2(w, k[None])[0])), 2 * np.pi)) for k in KT]
    good = []
    for t in GR:
        okt = False
        for om in (0.0, np.pi):
            if all(np.allclose(np.sort(np.mod(np.angle(np.linalg.eigvals(Wb2(w, (k + t)[None])[0])) + om, 2 * np.pi)), b, atol=1e-7) or
                   np.allclose(np.sort(np.mod(np.angle(np.linalg.eigvals(Wb2(w, (k + t)[None])[0])) + om + 1e-6, 2 * np.pi)), np.sort(np.mod(b + 1e-6, 2 * np.pi)), atol=1e-6)
                   for k, b in zip(KT, base)): okt = True; break
        if okt: good.append(tuple(int(x) for x in np.round(t / (np.pi / 4))))
    return frozenset(good)
cens = collections.Counter(); NW = 120
for it in range(NW):
    n = rng.integers(3, 6); w = []
    for _ in range(n):
        if rng.random() < 0.35: w.append(PC[list(PC)[rng.integers(0, 80)]])
        else: w.append(TOK[rng.integers(0, len(TOK))])
    if not any(isinstance(x, str) and x[0] == 'E' for x in w): w.insert(int(rng.integers(0, len(w) + 1)), 'E+')
    Ls = taste_lattice(w)
    # identify the lattice: sc(a) = a Z^3, fcc/bcc via membership patterns
    pts = np.array(sorted(Ls)); key = None
    for nm, gens in [('sc(2pi)', [(8, 0, 0)]), ('bcc(2pi)', [(4, 4, 4)]), ('sc(pi)', [(4, 0, 0)]), ('fcc(pi)', [(4, 4, 0)]), ('bcc(pi)', [(2, 2, 2), (4, 0, 0)]),
                     ('sc(pi/2)', [(2, 0, 0)]), ('fcc(pi/2)', [(2, 2, 0)]), ('bcc(pi/2)', [(1, 1, 1), (2, 0, 0)]), ('sc(pi/4)', [(1, 0, 0)]), ('fcc(pi/4)', [(1, 1, 0)])]:
        # lattice generated by the O-orbit of the generators, mod 8
        orbitg = {tuple(int(x) % 8 for x in R @ np.array(g)) for g in gens for R in ROTS}
        Lset = {(0, 0, 0)}; frontier = [(0, 0, 0)]
        while frontier:
            p = frontier.pop(); 
            for g in orbitg:
                q = tuple((a + b) % 8 for a, b in zip(p, g))
                if q not in Lset: Lset.add(q); frontier.append(q)
        if Lset == set(Ls): key = nm; break
    cens[key or f"other({len(Ls)})"] += 1
print("  spectral (U/T-kind) taste lattices of", NW, "random E-words (within (pi/4)Z^3):", dict(cens))
check("every sampled E-word's spectral taste set is one of the rotation-invariant dyadic lattices of B24 (no new lattice)",
      all(not k.startswith('other') for k in cens), str(dict(cens)))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
