AUDIT_INPUT_PATHS = ('docs/THE_SPIN10_GAPPING_CHANNEL_CARRIES_THE_HIGGS_DOUBLETS_BUT_AS_THE_ELECTROWEAK_HIGGS_IT_FORCES_ZERO_QUARK_MIXING_AND_AN_UNSPLIT_HEAVY_TEN_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""higgs-gapping-channel: is the electroweak Higgs the 10-channel of the forced far-wall gapping term?
Rule under test (H10, NOT adopted): the Higgs is B_a = psi_1^T C Gamma^a psi_2 (or its Hubbard-Stratonovich boson phi_a),
with Yukawa 16.16.10 and no Higgs added by hand.
 A  quantum numbers of the channel from the explicit oscillator 16 and pair matrices; Schur (no doublet-triplet splitting).
 B  Yukawa relations of one 10 coupling and of family-local 10 channels; CKM; comparison with supplied running masses.
 C  scale: <B> = 0 in the unique ground state; the 10 level at 10 g (so(12) Casimir formula of spin10-two-flavour);
    reduced Spin(6) diagonalisation; proton-decay bound on a degenerate triplet (estimate).
Labels: [T] exact, [F] finite diagnostic, [E] estimate against measurement (supplied numbers).
Supplied: the 16 with one orbital per weight, the 10-channel form (forced by spin10-two-flavour), the SM embedding
Y = (1/3) sum_colour h - (1/2) sum_weak h, GUT-scale running masses (Xing-Zhang-Zhou 2008, SM, mu = 2e16 GeV),
|V_us| (PDG 2024), Super-K tau(p -> e+ pi0), lattice hadronic alpha_H, chiral-Lagrangian D + F."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
from fractions import Fraction as Fr
import numpy as np

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = NF = 0
def check(name, ok, info=""):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

def ann(n):
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        A = np.zeros((dim, dim)); src = st[(st >> j) & 1 == 1]
        A[src ^ (1 << j), src] = 1 - 2 * (np.bitwise_count(src & ((1 << j) - 1)).astype(np.int64) & 1)
        out.append(A)
    return out

def spinor(n):
    """chiral spinor of Spin(2n) on even states of n oscillators: t_ab, pair matrices M_a = (C g_a)|_+, even states"""
    b = ann(n); G = []
    for k in range(n): G += [b[k] + b[k].T, 1j * (b[k] - b[k].T)]
    ev = [s for s in range(1 << n) if bin(s).count('1') % 2 == 0]
    t = [(-0.25j * (G[a] @ G[c] - G[c] @ G[a]))[np.ix_(ev, ev)] for a, c in itertools.combinations(range(2 * n), 2)]
    for C in (np.linalg.multi_dot(G[0::2]) if n > 1 else G[0], np.linalg.multi_dot(G[1::2]) if n > 1 else G[1]):
        M = [(C @ g)[np.ix_(ev, ev)] for g in G]
        if all(np.abs(m).max() > 0.5 for m in M): return t, M, ev
    raise RuntimeError("no charge conjugation found")

def vec_rep(t, M):
    B = np.array([m.ravel() for m in M]).T; R = []
    for tt in t:
        Y = np.array([(-(tt.T @ m + m @ tt)).ravel() for m in M]).T
        x, *_ = np.linalg.lstsq(B, Y, rcond=None); R.append(x)
    return R

# ------------------------------------------------------------------ A
print("== A. quantum numbers of the gapping channel B_a (10 of Spin(10)) under the SM embedding")
t16, M16, ev = spinor(5)
W = [np.array([0.5 - ((s >> k) & 1) for k in range(5)]) for s in ev]          # weights h_k = 1/2 - n_k (even # of minus: the 16)
Yh = lambda w: Fr(round(6 * (sum(w[:3]) / 3 - sum(w[3:]) / 2)), 6)
def name(w):
    cp = int(sum(w[:3] > 0)); wk = tuple(int(x > 0) for x in w[3:])
    if cp == 3: return 'nu^c' if wk == (1, 1) else 'e^c'
    if cp == 2: return 'u' if wk == (1, 0) else 'd'
    if cp == 1: return 'u^c' if wk == (1, 1) else 'd^c'
    return 'nu' if wk == (1, 0) else 'e'
cont = {}
for w in W: cont[(name(w), Yh(w))] = cont.get((name(w), Yh(w)), 0) + 1
want = {('u', Fr(1, 6)): 3, ('d', Fr(1, 6)): 3, ('u^c', Fr(-2, 3)): 3, ('d^c', Fr(1, 3)): 3, ('nu', Fr(-1, 2)): 1,
        ('e', Fr(-1, 2)): 1, ('e^c', Fr(1)): 1, ('nu^c', Fr(0)): 1}
# complex directions: (M[2k] + s i M[2k+1])/2 = C b_k^+ or C b_k
dirs = {}
ok_w = True; mods = set()
for k in range(5):
    for s in (+1, -1):
        Mc = (M16[2 * k] + s * 1j * M16[2 * k + 1]) / 2
        nz = list(zip(*np.nonzero(np.abs(Mc) > 1e-12)))
        sums = {tuple(W[i] + W[j]) for i, j in nz}
        ok_w &= len(sums) == 1
        wt = np.array(next(iter(sums))); mods |= {float(round(abs(Mc[i, j]), 12)) for i, j in nz}
        pairs = sorted({tuple(sorted((name(W[i]), name(W[j])))) for i, j in nz})
        dirs[tuple(wt.astype(int))] = pairs
wts = sorted(dirs)
unit_wts = all(sorted(np.abs(w)) == [0, 0, 0, 0, 1] for w in wts) and len(wts) == 10
check("A1 [T] every complex pair direction of B pairs 16 weights with w1 + w2 = +-e_k, once each: the channel is the 10",
      ok_w and unit_wts, f"{len(wts)} distinct weights")
def qn(w):
    w = np.array(w); col = 'singlet' if not any(w[:3]) else ('3' if sum(w[:3]) < 0 else '3bar')
    Y = Fr(round(6 * (sum(w[:3]) / 3 - sum(w[3:]) / 2)), 6); T3 = Fr(int(w[3] - w[4]), 2)
    return col, Y, T3, Y + T3
decomp = {}
for w in wts:
    col, Y, T3, Q = qn(w); decomp[(col, Y)] = decomp.get((col, Y), 0) + 1
check("A2 [T] 16 content is Q(6), u^c(3), d^c(3), L(2), e^c, nu^c with standard Y; the 10 = (1,2)_{+1/2} + (1,2)_{-1/2} "
      "+ (3,1)_{-1/3} + (3bar,1)_{+1/3}", cont == want and decomp == {('singlet', Fr(1, 2)): 2, ('singlet', Fr(-1, 2)): 2,
      ('3', Fr(-1, 3)): 3, ('3bar', Fr(1, 3)): 3}, ", ".join(f"({c},{Y}):{n}" for (c, Y), n in sorted(decomp.items(), key=str)))
neutral = {w: dirs[w] for w in wts if qn(w)[0] == 'singlet' and qn(w)[3] == 0}
hu = [p for w, p in neutral.items() if qn(w)[1] == Fr(-1, 2)]; hd = [p for w, p in neutral.items() if qn(w)[1] == Fr(1, 2)]
print("   neutral doublet directions: " + "; ".join(f"Y{qn(w)[1]}: {p}" for w, p in neutral.items()))
check("A3 [T] the colour-singlet doublets carry exactly the measured Higgs numbers (1,2)_{+-1/2}; their neutral components "
      "pair (u,u^c)+(nu,nu^c) and (d,d^c)+(e,e^c); every nonzero entry has modulus 1 (one Clebsch: M_u = M_nu, M_d = M_e^T)",
      sorted(map(tuple, hu + hd)) == sorted([(('nu', 'nu^c'), ('u', 'u^c')), (('d', 'd^c'), ('e', 'e^c'))]) and mods == {1.0},
      f"moduli {sorted(mods)}")
R10 = vec_rep(t16, M16)
L = np.vstack([np.kron(r, np.eye(10)) - np.kron(np.eye(10), r.T) for r in R10])
cdim = 10 * 10 - np.linalg.matrix_rank(L, tol=1e-9)
check("A4 [T] Schur: the Spin(10) commutant on the 10 is 1-dimensional, so the forced Spin(10)-invariant term gives the "
      "doublets and the triplets the SAME mass and the SAME Yukawa matrix; nothing in the term splits them", cdim == 1,
      f"commutant dim {cdim}")
trip = {w: dirs[w] for w in wts if qn(w)[0] != 'singlet'}
tp = sorted({p for ps in trip.values() for p in ps})
bviol = all(any(set(p) <= {'u', 'd'} for p in ps) for ps in trip.values())
check("A5 [T] the triplet directions pair qq (B = 2/3) and q^c l^c-type modes with the same matrix: baryon-number-violating "
      "couplings fixed by the doublet Yukawas", any(set(p) <= {'u', 'd'} for p in tp) and any('e^c' in p for p in tp),
      f"triplet pairs {tp}")

# ------------------------------------------------------------------ B
print("== B. Yukawa relations: M_f = Y <phi_f>, Y symmetric in family (the 10 is symmetric in 16 x 16)")
def ckm(Mu, Md):
    Uu, su, _ = np.linalg.svd(Mu); Ud, sd, _ = np.linalg.svd(Md)
    return Uu[:, np.argsort(su)].conj().T @ Ud[:, np.argsort(sd)], np.sort(su), np.sort(sd)
err1 = 0; rat = 0
for _ in range(200):
    A = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Y = A + A.T
    vu, vd = rng.normal(size=2) + 1j * rng.normal(size=2)
    V, su, sd = ckm(Y * vu, Y * vd); err1 = max(err1, np.abs(np.abs(V) - np.eye(3)).max())
    rat = max(rat, np.abs(su / sd - abs(vu / vd)).max())
check("B1 [T] one 10 coupling: M_u = Y v_u, M_d = M_e^T = Y v_d, so |V_CKM| = 1 exactly and m_u/m_d = m_c/m_s = m_t/m_b "
      "= |v_u/v_d| per family (200 seeded Y)", err1 < 1e-10 and rat < 1e-9, f"max ||V|-1| {err1:.0e}")
err2 = 0
for _ in range(200):
    y = rng.normal(size=3); Vu = rng.normal(size=3) + 1j * rng.normal(size=3); Vd = rng.normal(size=3) + 1j * rng.normal(size=3)
    V, _, _ = ckm(np.diag(y * Vu), np.diag(y * Vd)); P = np.abs(V)
    err2 = max(err2, np.abs(np.sort(P, axis=1)[:, :2]).max(), np.abs(P.max(axis=1) - 1).max())
check("B2 [T] family-local channels (each family's mirror carries its own 10, any VEVs): M_u, M_d both diagonal, so |V_CKM| "
      "is a permutation: no mixing angle at all", err2 < 1e-10, f"max off-permutation {err2:.0e}")
vus2 = []
for _ in range(200):
    Y1 = rng.normal(size=(3, 3)); Y1 = Y1 + Y1.T; Y2 = rng.normal(size=(3, 3)); Y2 = Y2 + Y2.T
    V, _, _ = ckm(Y1 + 0.3 * Y2, Y1 - 0.3 * Y2); vus2.append(abs(V[0, 1]))
check("B3 [F] contrast (escape, NOT forced): two independent symmetric couplings (10 + a second channel) give generic "
      "mixing", np.median(vus2) > 0.05, f"median |V_us| {np.median(vus2):.2f}")
# supplied running values at mu = 2e16 GeV (SM; Xing-Zhang-Zhou 2008), GeV
mu_, mc, mt = 0.48e-3, 0.235, 74.0; md, ms, mb = 1.14e-3, 21.7e-3, 1.00; me, mm, mtau = 0.4696e-3, 99.14e-3, 1.6853
Vus, dVus = 0.2250, 0.00067
print(f"   [E] GUT-scale ratios: m_b/m_tau {mb/mtau:.2f}, m_s/m_mu {ms/mm:.2f}, m_d/m_e {md/me:.2f}; "
      f"m_c/m_t {mc/mt:.1e} vs m_s/m_b {ms/mb:.1e}; m_u/m_t {mu_/mt:.1e} vs m_d/m_b {md/mb:.1e}")
check("B4 [E] verdict against measurement: the single-10 rule (B1) and the family-local rule (B2) predict |V_us| = 0; measured "
      "0.2250(7): excluded at > 300 sigma, independent of the matching scale (V_us barely runs)", Vus / dVus > 300,
      f"{Vus/dVus:.0f} sigma")
check("B5 [E] mass relations: m_s/m_mu = 0.22 and m_d/m_e = 2.4 (predicted 1, off by > 2x); m_c/m_t vs m_s/m_b differ "
      "by > 5x (predicted equal); only m_b/m_tau = 0.59 is near 1 (within 50%, SM running)",
      ms / mm < 0.5 and md / me > 2 and (ms / mb) / (mc / mt) > 5 and abs(mb / mtau - 1) < 0.5,
      f"(m_s/m_b)/(m_c/m_t) = {(ms/mb)/(mc/mt):.1f}")

# ------------------------------------------------------------------ C
print("== C. scale of the 10 composite (H = -g F, F = 144 - 2S(S+1) - C2_10 - J^2, spin10-two-flavour)")
F = lambda S, C2, J: 144 - 2 * S * (S + 1) - C2 - J * J
E0 = F(0, 0, 0); lev = {'pair (10, J=+-1)': E0 - F(0, 9, 1), 'fermion (16, J=1/2)': E0 - F(Fr(1, 2), Fr(45, 4), Fr(1, 2)),
                        'charge-4 singlet': E0 - F(0, 0, 2)}
check("C1 [T] levels above the unique ground state: 10 composite at 10 g (all 10 components, Schur), fermion at 13 g, "
      "lowest excitation the charge-4 singlet at 4 g: the 10 is a heavy, non-condensed excitation",
      lev == {'pair (10, J=+-1)': 10, 'fermion (16, J=1/2)': 13, 'charge-4 singlet': 4}, ", ".join(f"{k} {v} g" for k, v in lev.items()))
# reduced analogue: Spin(6) 4-spinor, two flavours, 8 modes (2^8): <B_a> = 0, the B^+|GS> states degenerate
t4, M4, _ = spinor(3); c = ann(8); cd = [x.T for x in c]
Bs = [sum(M[a, b] * c[a] @ c[4 + b] for a in range(4) for b in range(4)) for M in M4]
H = -0.5 * sum(B @ B.conj().T + B.conj().T @ B for B in Bs)
ev_, U = np.linalg.eigh(H); gs = U[:, 0]
expB = max(abs(gs.conj() @ B @ gs) for B in Bs)
Ep = [np.real((B.conj().T @ gs).conj() @ H @ (B.conj().T @ gs)) / np.real((B.conj().T @ gs).conj() @ (B.conj().T @ gs))
      for B in Bs if np.linalg.norm(B.conj().T @ gs) > 1e-9]
check("C2 [F] reduced Spin(6) site (2^8, full diagonalisation): unique ground state, <B_a> = 0, the B_a^+|GS> states all at "
      "one energy (no splitting of the channel components)", ev_[1] - ev_[0] > 1e-6 and expB < 1e-12 and np.ptp(Ep) < 1e-10,
      f"gap {ev_[1]-ev_[0]:.3f} g, max|<B>| {expB:.0e}, pair level {Ep[0]-ev_[0]:.3f} g x{len(Ep)}")
# proton decay through the degenerate colour triplet with the predicted (first-family) couplings
v = 246.0; yu, yd = np.sqrt(2) * mu_ / v, np.sqrt(2) * md / v
mp, aH, fpi, DF = 0.938, 0.012, 0.130, 2.27
tau_lim = 2.4e34 * 3.156e7 / 6.582e-25          # GeV^-1
MT_min = (mp / (32 * np.pi) * (aH / fpi) ** 2 * DF ** 2 * (yu * yd) ** 2 * tau_lim) ** 0.25
check("C3 [E] p -> e+ pi0 via the triplet with Yukawas fixed by B1 needs M_T > 1e10 GeV; Spin(10) keeps M_T = M_doublet, "
      "so a doublet at the weak scale is excluded unless something splits the 10 by > 1e8", MT_min > 1e10,
      f"M_T > {MT_min:.1e} GeV vs 125 GeV")
print(f"   [open] v = 246 GeV is not produced: the 10 sits at 10 g with <B> = 0; v/(10 g) at a cell scale ~ 1e16-1e19 GeV is 1e-14-1e-17")
print(f"TOTAL: PASS={NP} FAIL={NF}   ({time.time()-T0:.1f} s)")
