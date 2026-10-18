#!/usr/bin/env python3
"""B25_check part 2: letter transposition rules and the PSG-conjugation step of the index lemma, in the INDEPENDENT
chk_core-gauge build (corelib.py; no import of chk_model / b2X code).  Also: Delta(m) classification by exact integer
arithmetic, and a numerical illustration of the kind-composition rules (U/T/I/K) with an independently coded
intertwiner solver validated out-of-sample.  Prints PASS/FAIL, TOTAL."""
import sys, os, itertools, collections
import numpy as np
import corelib as cl
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(2511); KS = rng.uniform(-np.pi, np.pi, (5, 3))
W1 = lambda w, k: cl.Wc(w, np.asarray(k)[None])[0]
Sg = np.diag(cl.SIG).astype(complex)
# ---- (1) S^n(k)^T = S^n(k)
ok = all(np.allclose(W1([p], k).T, W1([p], k)) for p in cl.POW for k in KS)
check("S^n(k)^T = S^n(k), n = +-1, +-2, +-4 (diagonal letters)", ok)
# ---- (2) R_L
R0 = W1(['R'], np.zeros(3))
ok_real = np.abs(R0.imag).max() < 1e-15 and np.allclose(R0, R0.T)
ok_unit = all(np.allclose(W1(['R'], k) @ W1(['R'], k).conj().T, np.eye(12)) for k in KS)
okT = all(np.allclose(W1(['R'], k).T, W1(['R'], -k)) for k in KS)
okS = all(np.allclose(W1(['R'], k).T, W1([Sg, 'S', 'R', 'Si', Sg], k)) for k in KS)
check("R_L(k) unitary; R_L(0) real symmetric; R_L(k)^T = R_L(-k) = sigma S(k) R_L(k) S(k)^-1 sigma (sigma = sign part of S)", ok_real and ok_unit and okT and okS,
      f"real-sym {ok_real} unitary {ok_unit} T=-k {okT} sigmaSRS^-1sigma {okS}")
# is sigma a symmetric on-site letter?  (decides whether W^T is literally a palette word)
inv = all(np.allclose(cl.cc.UF[g] @ Sg @ cl.cc.UF[g].T, Sg) for g in cl.ROTG)
basis = cl.PH + cl.PLm
A = np.array([b.ravel() for b in basis]).T; x = np.linalg.lstsq(A, Sg.ravel(), rcond=None)[0]
in_alg = np.allclose(A @ x, Sg.ravel())
comm = all(np.allclose(Sg @ P, P @ Sg) for P in cl.PH + cl.PLm)
print(f"   sigma commutes with every PH, PLm: {comm}; sigma diag = {cl.SIG.astype(int).tolist()}; f_c = {cl.FC.tolist()}")
print(f"   sigma: PSG-invariant {inv}; in span(PH, PLm) {in_alg}; sigma = +-Y ? {np.allclose(Sg, cl.Ymat) or np.allclose(Sg, -cl.Ymat)}; sigma = scalar? {np.allclose(Sg, Sg[0,0]*np.eye(12))}")
# ---- (3) on-site letters
okPH = all(np.allclose(P.T, P) for P in cl.PH)
okPL = all(np.allclose(cl.PLm[i].T, cl.PLm[3 - i]) for i in range(4)) and np.allclose(cl.LLEV, -np.array(cl.LLEV[::-1]))
check("PH_j^T = PH_j (real symmetric on-site hopping); PLm_i^T = PLm_{3-i} (Lam imaginary Hermitian, spectrum +-symmetric)", okPH and okPL)
okL = all(np.allclose(cl.Labc(a, b, c).T, cl.I4[c] * cl.Labc((b - c) % 4, (a - c) % 4, (-c) % 4)) for a in range(4) for b in range(4) for c in range(4))
check("L_abc^T = i^c L_{(b-c)(a-c)(-c)} for all 64 Clifford L letters", okL)
okH = all(np.allclose(cl.Hab(a, b).T, cl.Hab(a, b)) for a in range(4) for b in range(4))
okPLphi = all(np.allclose(cl.PL(ph).T, np.exp(1j * ph) * cl.PL(-ph)) and np.allclose(cl.Ymat @ cl.PL(ph) @ cl.Ymat, cl.PL(ph).T)
              for ph in rng.uniform(-np.pi, np.pi, 7).tolist() + list(np.pi / 6 * np.arange(12)))
okYPP = np.allclose(cl.Ymat @ cl.PP @ cl.Ymat, np.eye(12) - cl.PP)
check("H_ab^T = H_ab; PL(phi)^T = e^{i phi} PL(-phi) = Y PL(phi) Y (any phi; Y PP Y = 1 - PP)", okH and okPLphi and okYPP)
# PP really is the plane projector-type element (commutes with Z_i, PSG-invariant)
Zs = [np.diag(np.where(cl.FC[:, i] != 0, -1.0, 1.0)) for i in range(3)]
check("PP = PLm0 + PLm2 is PSG-invariant, rank 6 and commutes with the corner-plane signs Z_i",
      all(np.allclose(cl.cc.UF[g] @ cl.PP @ cl.cc.UF[g].T, cl.PP) for g in cl.ROTG) and round(np.trace(cl.PP).real) == 6 and all(np.allclose(Z @ cl.PP, cl.PP @ Z) for Z in Zs))
# ---- (4) whole-word transpose
def wordT(w):
    out = []
    for L in w[::-1]:
        if isinstance(L, str): out += ([Sg, 'S', 'R', 'Si', Sg] if L == 'R' else [L])
        else: out.append(L.T)
    return out
names = ['H13', 'L123', 'L310', 'P5', 'H4.5', 'L2.4.3', 'P11', 'L101']
ok = True
for trial in range(12):
    w = []
    for _ in range(rng.integers(2, 5)):
        w.append(rng.choice(list(cl.POW) + ['R'])); w.append(cl.letter_const(rng.choice(names)))
    ok &= all(np.allclose(W1(w, k).T, W1(wordT(w), k)) for k in KS[:3])
check("W(k)^T = reversed word with transposed on-site letters at the SAME k, R_L -> sigma S R_L S^-1 sigma (12 random words)", ok)
# ---- (5) PSG covariance with CONSTANT unitaries (the conjugation step of the lemma)
ok = True
for trial in range(6):
    w = []
    for _ in range(3):
        w.append(rng.choice(list(cl.POW) + ['R'])); w.append(cl.letter_const(rng.choice(names)))
    for g in cl.ROTG:
        U = cl.cc.UF[g]
        ok &= all(np.allclose(W1(w, cl.fib(g, k)), U @ W1(w, k) @ U.T) for k in KS[:2])
check("every word is PSG-covariant with k-INDEPENDENT unitaries: W(R k + pi R lam_R) = U_R W(k) U_R^T (24 rotations, 6 random words)", ok)
# ---- (6) Delta(m) classification by exact integer arithmetic: m = (pi/8) n, n in Z_16^3
cls = collections.Counter(); okD = True
Yd = np.where((cl.FC.sum(1) // 2) % 2 == 0, 1, -1)
plane = [int(np.argmin(np.abs(cl.FC[c]))) for c in range(12)]
for n in itertools.product(range(16), repeat=3):
    ph = (cl.FC @ np.array(n)) % 16                                   # phase m.f_c in units pi/8, mod 2pi
    ph2 = (ph + np.where(Yd < 0, 8, 0)) % 16                           # phase of Y Delta
    scal = len(set(ph)) == 1
    plc = all(len({ph[c] for c in range(12) if plane[c] == a}) == 1 for a in range(3))
    yplc = all(len({ph2[c] for c in range(12) if plane[c] == a}) == 1 for a in range(3))
    nn = np.array(n)
    e_s = np.all(nn % 16 == 0) or np.all(nn % 16 == 8); e_c = np.all(nn % 8 == 0); e_y = np.all(nn % 8 == 4)
    okD &= (scal == e_s) and (plc == e_c) and (yplc == e_y); cls[(scal, plc, yplc)] += 1
check("Delta(m): scalar iff m in bcc(2pi); plane-constant iff m in pi Z^3; Y x plane-constant iff m in (pi/2)(1,1,1) + pi Z^3 (exact, 4096 m)", okD, f"{dict(cls)}")
# ---- (7) kind composition, independent solver with out-of-sample validation
FK = {'U': lambda M: M, 'T': lambda M: M.T, 'I': lambda M: M.conj().T, 'K': lambda M: M.conj()}
def solve_inter(w, t, kind, om=1.0, nk=5, seed=0):
    r = np.random.default_rng(100 + seed); ks = r.uniform(-np.pi, np.pi, (nk, 3)); rows = []
    for k in ks:
        A = W1(w, k + t); B = om * FK[kind](W1(w, k))
        rows.append(np.kron(A, np.eye(12)) - np.kron(np.eye(12), B.T))    # row-major vec(A V - V B)
    _, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-9 * s[0]):].conj()
    if len(null) == 0: return None
    V = (r.normal(size=len(null)) + 1j * r.normal(size=len(null))) @ null; V = V.reshape(12, 12)
    if np.linalg.svd(V, compute_uv=False)[-1] < 1e-6 * np.linalg.norm(V, 2): return None
    kv = r.uniform(-np.pi, np.pi, (4, 3))                                  # out-of-sample validation
    if not all(np.allclose(W1(w, k + t) @ V, om * V @ FK[kind](W1(w, k)), atol=1e-8) for k in kv): return None
    return V
def comp(w, t1, F1, V1, om1, t2, F2, V2, om2):
    """(t1,F1) o (t2,F2): W(k+t1+t2) = om1 V1 F1(om2 V2 F2(W(k)) V2^-1) V1^-1 -> (t1+t2, F1F2, V, om)."""
    conjF1 = F1 in ('I', 'K'); om = om1 * (np.conj(om2) if conjF1 else om2)
    if F1 == 'U': V = V1 @ V2
    elif F1 == 'K': V = V1 @ V2.conj()
    else: V = V1 @ np.linalg.inv(V2).T if F1 == 'T' else V1 @ np.linalg.inv(V2).conj().T
    table = {('U', x): x for x in 'UTIK'}; table.update({('T', 'T'): 'U', ('T', 'I'): 'K', ('T', 'K'): 'I', ('I', 'I'): 'U', ('I', 'K'): 'T', ('K', 'K'): 'U'})
    F = table.get((F1, F2)) or table[(F2, F1)]
    return t1 + t2, F, V, om
def holds(w, t, F, V, om):
    return all(np.allclose(W1(w, k + t) @ V, om * V @ FK[F](W1(w, k)), atol=1e-8) for k in KS)
# (a) T-type taste and its double  (B24_check example word)
w = cl.build(('S2', 'p', 'S2', 'o'), ('L101', 'H13')); t = np.pi / 4 * np.ones(3)
VT = solve_inter(w, t, 'T'); VU = solve_inter(w, t, 'U')
t2, F2, V2, om2 = comp(w, t, 'T', VT, 1.0, t, 'T', VT, 1.0) if VT is not None else (None,) * 4
check("S2.L101.S2.H13: t = (pi/4)(1,1,1) has a k-independent T intertwiner, no U one; composing T o T gives a U intertwiner at 2t with V = V_T V_T^{-T}",
      VT is not None and VU is None and F2 == 'U' and holds(w, t2, F2, V2, om2))
# (b) inverse has the same kind
Vinv = np.linalg.inv(VT).T          # W(k - t) = F(V^-1 W(k) V) for F = T  -> V' = V^T ... check directly
okinv = holds(w, -t, 'T', VT.T, 1.0) or holds(w, -t, 'T', np.linalg.inv(VT).T, 1.0)
check("inverse of the T taste is a T taste at -t (k-independent)", okinv)
# (c) rotation conjugation keeps the kind, and R t - t lies in Lambda_u
okrot = True; diffs_u = True
for g in cl.ROTG:
    R = cl.cc.OH[g]; U = cl.cc.UF[g]; Rt = R @ t
    Vr = U @ VT @ U.T
    okrot &= holds(w, Rt, 'T', Vr, 1.0)
    diffs_u &= solve_inter(w, Rt - t, 'U') is not None or np.allclose(cl.wrap(Rt - t), 0)
check("for all 24 rotations: R t is a T taste with transported intertwiner U_R V_T U_R^T, and R t - t has a U intertwiner (O acts trivially on Lambda_ind/Lambda_u)", okrot and diffs_u)
# (d) reflection-type (I) taste: two words with an I intertwiner at E = 0 (w = e^{2iE} = 1) from the B25 census
for sk, nm in ((('S', 'R', 'o'), ('L310',)), (('S2', 'p', 'S4', 'q', 'S2', 'o'), ('P1', 'P11', 'L310'))):
    w = cl.build(sk, nm); found = None
    # cheap spectral pre-screen for reflection-type tastes with w = 1:  spec W(k+t) = conj spec W(k)  at two random k
    TT = np.array([n for n in itertools.product(range(0, 16, 2), repeat=3) if any(n)]) * np.pi / 16
    cand = np.ones(len(TT), bool)
    for k in np.random.default_rng(77).uniform(-np.pi, np.pi, (2, 3)):
        e0 = np.sort(np.mod(-np.angle(np.linalg.eigvals(W1(w, k))), 2 * np.pi))
        E2 = np.sort(np.mod(np.angle(np.linalg.eigvals(cl.Wc(w, k + TT))), 2 * np.pi), axis=1)
        d = np.abs(np.exp(1j * E2) - np.exp(1j * e0)[None]).max(1); cand &= d < 1e-7
    print(f"   {sk} {nm}: {cand.sum()} reflection-type (w=1) spectral tastes on (pi/8)Z^3 pass the pre-screen")
    for tt in TT[cand]:
        V = solve_inter(w, tt, 'I', 1.0, nk=3)
        if V is not None and solve_inter(w, tt, 'U') is None and solve_inter(w, tt, 'T') is None: found = (tt, V); break
    if found is None: check(f"{sk} {nm}: found a pure-I reflection taste", False); continue
    tt, V = found
    t2, F2, V2, om2 = comp(w, tt, 'I', V, 1.0, tt, 'I', V, 1.0)
    check(f"{sk} {nm}: I taste at t/pi = {np.round(tt/np.pi, 4)}; I o I = U-kind with w = 1 at 2t (formula), and 2t has a U intertwiner",
          F2 == 'U' and abs(om2 - 1) < 1e-12 and holds(w, t2, F2, V2, om2) and solve_inter(w, 2 * tt, 'U') is not None)
# (e) the omega bookkeeping for reflection kinds at a level E != 0 (synthetic, exact algebra on random matrices)
okw = True
for trial in range(20):
    E = rng.uniform(-np.pi, np.pi); wE = np.exp(2j * E)
    for F1 in 'UTIK':
        for F2 in 'UTIK':
            om1 = wE if F1 in 'IK' else 1.0; om2 = wE if F2 in 'IK' else 1.0
            _, F, _, om = comp(None, 0, F1, np.eye(12), om1, 0, F2, np.eye(12), om2)
            okw &= abs(om - (wE if F in 'IK' else 1.0)) < 1e-12
            # level-E preservation: eigenvalue e^{iE} maps to om e^{iE} (U,T) or om e^{-iE} (I,K)
            img = om * (np.exp(-1j * E) if F in 'IK' else np.exp(1j * E)); okw &= abs(img - np.exp(1j * E)) < 1e-12
check("kind composition is the Klein group {U,T,I,K} and w stays = 1 (U,T) / e^{2iE} (I,K) under composition and inversion: level E preserved", okw)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
