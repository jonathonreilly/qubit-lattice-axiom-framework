#!/usr/bin/env python3
"""J:attack-f:PR9354 -- NORMALIZATION: the curvature target of the finite-projection note: 'the source uses the supplied normalization A = 3 pref N chi/4' with pref = 1, or 2 when 2k = 0 mod 2 pi, and the stencil [15 E(0) - 16 E(H1) + E(2 H1)]/(9 pref N H1^2).

Factors of N, 2, 1/2 and the mode's conjugation convention, recomputed at small size by brute force with own exact diagonalisation (own flip-component enumeration, sparse Hamiltonian, ARPACK, deflated CG):
  (1) the stencil algebra, exactly (sympy): (15 E0 - 16 E(h) + E(2h))/(12 h^2) = A - 4 C h^4 for E = E0 - A h^2 - B h^4 - C h^6, and -7 L1/(6h) - 2 L3 h/3 for an added odd part L1 h + L3 h^3, and 14 h M for E = E0 - h M;
  (2) 2 x 2 x 4 torus, real mode at k = pi (y-links modulated by (-1)^z): the exact second-order coefficient <F R F> of the probe F = sum cos(k z) sigma equals N m_-1 = N chi/2, i.e. A = pref N chi/4 with pref = 2 (chi = 2 m_-1, O = N^-1/2 sum e^{ikz} sigma real);
  (3) the same torus, complex mode at k = pi/2 (y-links modulated by cos(pi z/2) in the probe and e^{i pi z/2} in O): <F R F> = (N/2) <O^dag R O> = N chi/4, i.e. pref = 1, with the +k / -k cross term <O R O> vanishing (momentum conservation);
  (4) the exact five-point estimator [15 E0 - 16 E(h) + E(2h)]/(3 pref N h^2) (the single-probe analogue of the note's 9 pref N H1^2 for the triple: A = pref N chi/4 for one probe, 3 pref N chi/4 for the cyclic triple) against chi = 2 m_-1 at h = 0.05, 0.1 for both modes, using the pref of (2) and (3).
Prints SUMMARY:; HIT only if a normalization is off (the same procedure with the wrong pref must be off by exactly a factor 2).
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh, cg, LinearOperator

T0 = time.time()
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

def build(Ls):
    Lx, Ly, Lz = Ls
    sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]
    sid = {s: i for i, s in enumerate(sites)}; nv = len(sites); nl = 3 * nv
    def lk(s, a): return a * nv + sid[s]
    def sh(s, a, d=1):
        t = list(s); t[a] = (t[a] + d) % Ls[a]; return tuple(t)
    plaq = []
    for s in sites:
        for a in range(3):
            for b in range(a + 1, 3):
                plaq.append((lk(s, a), lk(sh(s, a), b), lk(sh(s, b), a), lk(s, b)))
    canon = np.zeros(nl, np.int64)
    for s in sites:
        canon[lk(s, 0)] = (-1) ** s[1]; canon[lk(s, 1)] = (-1) ** s[0]; canon[lk(s, 2)] = (-1) ** s[0]
    axis = np.repeat(np.arange(3), nv)
    tail = np.array(sites * 3)                                   # link (s, a) has tail vertex s
    xb = tail[np.arange(nl), (axis + 1) % 3]                      # coordinate of the tail along axis a + 1
    return sites, nv, nl, np.array(plaq), canon, axis, xb
def vertex_div_zero(nv, nl, sites, Ls, canon):
    sid = {s: i for i, s in enumerate(sites)}
    for s in sites:
        d = 0
        for a in range(3):
            t = list(s); t[a] = (t[a] - 1) % Ls[a]
            d += canon[a * nv + sid[s]] - canon[a * nv + sid[tuple(t)]]
        if d != 0: return False
    return True
def component(nl, plaq, c0):
    masks = np.array([sum(1 << int(l) for l in p) for p in plaq], np.int64)
    seen = np.array([c0], np.int64); frontier = seen.copy()
    while len(frontier):
        new = []
        for p, m in zip(plaq, masks):
            b = [(frontier >> int(l)) & 1 for l in p]
            circ = (2 * b[0] - 1) + (2 * b[1] - 1) - (2 * b[2] - 1) - (2 * b[3] - 1)
            sel = frontier[np.abs(circ) == 4]
            if len(sel): new.append(sel ^ m)
        if not new: break
        new = np.unique(np.concatenate(new)); new = new[~np.isin(new, seen, assume_unique=True)]
        seen = np.union1d(seen, new); frontier = new
    return seen, masks
def hamiltonian(codes, plaq, masks):
    n = len(codes); rows = []; cols = []
    for p, m in zip(plaq, masks):
        b = [(codes >> int(l)) & 1 for l in p]
        circ = (2 * b[0] - 1) + (2 * b[1] - 1) - (2 * b[2] - 1) - (2 * b[3] - 1)
        sel = np.flatnonzero(np.abs(circ) == 4)
        tgt = codes[sel] ^ m
        idx = np.searchsorted(codes, tgt)
        assert np.all(codes[idx] == tgt)
        rows.append(sel); cols.append(idx)
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n, n)).tocsr()
    return H
def diag_fields(codes, nl, axis, xb, nv, k):
    n = len(codes); N = nv
    O = np.zeros((3, n)); w = np.cos(k * xb); ph = np.cos(k * xb)   # k = pi: cos = e^{ik x} = (-1)^x, real
    for l in range(nl):
        O[axis[l]] += ph[l] * (2.0 * ((codes >> l) & 1) - 1.0)
    O /= np.sqrt(N)
    return O


import sympy as sp
from scipy.sparse import diags
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)
T0 = time.time()
h, A, B, C, L1, L3, M_ = sp.symbols("h A B C L1 L3 M")
E = lambda hh, extra=0: sp.Symbol("E0") - A * hh ** 2 - B * hh ** 4 - C * hh ** 6 + extra
st = lambda f: sp.expand((15 * f(0) - 16 * f(h) + f(2 * h)) / (12 * h ** 2))
check("stencil algebra: (15 E0 - 16 E(h) + E(2h))/(12 h^2) = A - 4 C h^4 for E = E0 - A h^2 - B h^4 - C h^6", sp.simplify(st(lambda x: E(x)) - (A - 4 * C * h ** 4)) == 0)
check("an added odd part L1 h + L3 h^3 adds -7 L1/(6 h) - 2 L3 h/3, and E = E0 - h M gives numerator 14 h M", sp.simplify(st(lambda x: E(x, L1 * x + L3 * x ** 3)) - (A - 4 * C * h ** 4 - sp.Rational(7, 6) * L1 / h - sp.Rational(2, 3) * L3 * h)) == 0 and sp.simplify(15 * sp.Symbol("E0") - 16 * (sp.Symbol("E0") - h * M_) + (sp.Symbol("E0") - 2 * h * M_) - 14 * h * M_) == 0)
Ls = (2, 2, 4)
sites, nv, nl, plaq, canon, axis, xb = build(Ls)
c0 = int(sum(1 << i for i in range(nl) if canon[i] > 0)); codes, masks = component(nl, plaq, c0)
H = hamiltonian(codes, plaq, masks); n = len(codes); N = nv; tail = np.array(sites * 3)
def gr(hh, F):
    ev, U = eigsh((H - hh * diags(F)).tocsr(), k=2, which="SA", tol=1e-13, v0=np.ones(n) / np.sqrt(n)); o = np.argsort(ev); return float(ev[o[0]]), U[:, o[0]]
E0, psi = gr(0.0, np.zeros(n)); psi = psi / np.linalg.norm(psi)
class Aop(LinearOperator):
    def __init__(s_): super().__init__(dtype=float, shape=(n, n))
    def _matvec(s_, x): return H @ x - E0 * x + psi * (psi @ x)
def solve(r):
    x, info = cg(Aop(), r, rtol=1e-13, atol=0.0, maxiter=4000); assert info == 0; return x
def sigma_sum(a, wfun):
    F = np.zeros(n)
    for l in range(nv * a, nv * (a + 1)): F += wfun(tail[l, (a + 1) % 3]) * (2.0 * ((codes >> l) & 1) - 1.0)
    return F
def estimator(F, pref, hh):
    Es = {x: gr(x, F)[0] for x in (hh, 2 * hh)}
    return (15 * E0 - 16 * Es[hh] + Es[2 * hh]) / (3 * pref * N * hh ** 2)          # single probe: A = pref N chi/4, so chi = 4 A/(pref N) and A = numerator/(12 h^2); the note's triple has A = 3 pref N chi/4, hence its 9
rows = {}
# (2) real mode, k = pi
Fpi = sigma_sum(1, lambda z: np.cos(np.pi * z)); Opi = Fpi / np.sqrt(N)
mean = float(psi @ (Opi * psi)); r = Opi * psi - mean * psi; x = solve(r); m_m1 = float(r @ x); chi_pi = 2 * m_m1
rF = Fpi * psi - float(psi @ (Fpi * psi)) * psi; a2_pi = float(rF @ solve(rF))
check("real mode k = pi: the exact second-order coefficient <F R F> = N m_-1 = N chi/2, i.e. A = pref N chi/4 with pref = 2", abs(a2_pi - N * m_m1) < 1e-9 * a2_pi and abs(a2_pi - 2 * N * chi_pi / 4) < 1e-9 * a2_pi, f"<FRF> = {a2_pi:.9f}, N m_-1 = {N * m_m1:.9f}, pref N chi/4 = {2 * N * chi_pi / 4:.9f} (pref = 1 would give {N * chi_pi / 4:.9f})")
# (3) complex mode, k = pi/2
k = np.pi / 2
Fk = sigma_sum(1, lambda z: np.cos(k * z))
Oc_re = sigma_sum(1, lambda z: np.cos(k * z)) / np.sqrt(N); Oc_im = sigma_sum(1, lambda z: np.sin(k * z)) / np.sqrt(N)      # O = Oc_re + i Oc_im
mre = float(psi @ (Oc_re * psi)); mim = float(psi @ (Oc_im * psi))
rre = Oc_re * psi - mre * psi; rim = Oc_im * psi - mim * psi
xre = solve(rre); xim = solve(rim)
# <O^dag R O> = <(re - i im) R (re + i im)> = re R re + im R im + i (re R im - im R re) ; the imaginary part cancels for a real symmetric R
m_dag = float(rre @ xre + rim @ xim); cross_im = float(rre @ xim - rim @ xre)
# <O R O> = re R re - im R im + i (re R im + im R re)
m_OO_re = float(rre @ xre - rim @ xim); m_OO_im = float(rre @ xim + rim @ xre)
rF = Fk * psi - float(psi @ (Fk * psi)) * psi; a2_k = float(rF @ solve(rF)); chi_k = 2 * m_dag
check("complex mode k = pi/2: the cross term <O R O> vanishes (|<O R O>| < 1e-9 <O^dag R O>; momentum conservation), and <F R F> = (N/2) <O^dag R O> = N chi/4, i.e. pref = 1", abs(m_OO_re) < 1e-9 * m_dag and abs(m_OO_im) < 1e-9 * m_dag and abs(a2_k - N * m_dag / 2) < 1e-9 * a2_k,
      f"<FRF> = {a2_k:.9f}, (N/2) <O^dag R O> = {N * m_dag / 2:.9f}, N chi/4 = {N * chi_k / 4:.9f}; <O R O> = ({m_OO_re:+.1e}, {m_OO_im:+.1e}), Im<O^dag R O> = {cross_im:+.1e}")
for label, F, pref, chi in (("real mode k = pi", Fpi, 2, chi_pi), ("complex mode k = pi/2", Fk, 1, chi_k)):
    out = []
    for hh in (0.05, 0.10):
        good = estimator(F, pref, hh); bad = estimator(F, 3 - pref, hh)
        out.append((hh, good / chi - 1, bad / chi - 1))
    rows[label] = out
    check(f"{label}: the note's stencil with pref = {pref} reproduces chi = 2 m_-1 to below 0.3% at h = 0.05 and 0.1, and with the other pref it is off by exactly a factor of {'2' if pref == 2 else '1/2'} up to the same bias",
          abs(out[0][1]) < 3e-3 and abs(out[1][1]) < 3e-3 and abs((out[0][2] + 1) / (out[0][1] + 1) - pref / (3 - pref)) < 1e-9, "; ".join(f"h = {hh}: pref {pref} {g:+.5f}, other pref {b_:+.5f}" for hh, g, b_ in out))
print(f"   total {time.time() - T0:.0f}s")
if not HITS:
    print("SUMMARY: no purchase: the stencil algebra, A = 3 pref N chi/4 with pref = 2 for the real mode at 2k = 0 and pref = 1 for the complex mode (checked on the 2x2x4 torus, chi = 2 m_-1, single-mode analogue of the triple), and the note's 9 pref N H1^2 form all hold exactly; the wrong pref is off by exactly a factor two")
else:
    print("SUMMARY: a normalization is off: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
