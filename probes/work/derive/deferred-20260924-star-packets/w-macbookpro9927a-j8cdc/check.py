#!/usr/bin/env python3
"""deferred-20260924-star-packets, first pass a1 (worker w-macbookpro9927a-j8cdc, claude-opus-5-5).

Energy coherence of the electric star's actual GKLS occurrence versus a prepared actual output (batch 14, PR8929's
deferred coherent-fuel statement).  The supplied star is rebuilt from the landed definitions: A vertex 0, B leaves 1-3,
charges q in {-1,0,1}, Gauss E_0b = -q_b, outward transport F, formation marks j_(0b),sigma, H = delta eps^-4 (W - eps F)^T
(W - eps F) + K lam E2, dressed input psi = (A + eps F A)/sqrt(1 + 3 eps^2), jumps sqrt(kappa)/eps j.  Exact families use
sympy; the float families integrate the full 256-dimensional GKLS superoperator and are labelled.
"""
import itertools
import sys
import time

import numpy as np
import sympy as sp
from scipy.linalg import expm

T0 = time.time()
FAILS = []


def check(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""))
    if not ok:
        FAILS.append(tag)


# ================================================================ the supplied physical star (exact integer matrices)
states = [q for q in itertools.product((-1, 0, 1), repeat=4) if sum(q) == 1]   # Gauss: E_0b = -q_b forces sum q = 1
idx = {q: i for i, q in enumerate(states)}
n = len(states)
nrec = [sum(1 for x in q if x) for q in states]
N1 = [i for i in range(n) if nrec[i] == 1]
N3 = [i for i in range(n) if nrec[i] == 3]
occ3 = [i for i in N3 if states[i][0] != 0]


OUT_OF_SECTOR = []


def op(fn):
    M = sp.zeros(n, n)
    for q in states:
        for amp, q2 in fn(q):
            if q2 not in idx:                 # a move that breaks Gauss's law or hard-core occupancy
                OUT_OF_SECTOR.append((q, q2))
                continue
            M[idx[q2], idx[q]] += amp
    return M


def hop(q):   # outward transport: the A charge moves to an empty leaf (E_0b changes by -q_0)
    out = []
    if q[0] != 0:
        for b in (1, 2, 3):
            if q[b] == 0:
                q2 = list(q)
                q2[b], q2[0] = q[0], 0
                out.append((1, tuple(q2)))
    return out


def mark(b, sg):   # formation mark on edge (0,b): both endpoints empty, creates (sg, -sg), E_0b changes by sg
    def f(q):
        if q[0] == 0 and q[b] == 0:
            q2 = list(q)
            q2[0], q2[b] = sg, -sg
            return [(1, tuple(q2))]
        return []
    return f


F = op(hop)
W = sp.diag(*[1 if q[0] == 0 else 0 for q in states])
E2 = sp.diag(*[sum(1 for b in (1, 2, 3) if q[b]) for q in states])
JRES = [op(mark(b, sg)) for b in (1, 2, 3) for sg in (1, -1)]
JCOH = [op(mark(b, 1)) + op(mark(b, -1)) for b in (1, 2, 3)]
Avec = sp.zeros(n, 1)
Avec[idx[(1, 0, 0, 0)]] = 1
svec = (F * Avec) / sp.sqrt(3)
eps, lam, K, dl, kap = sp.symbols("epsilon lambda K delta kappa", positive=True)
a = 1 + 3 * eps ** 2
Mh = W - eps * F
h = Mh.T * Mh

# ---------------------------------------------------------------- E1: the landed model facts, rebuilt
ok = n == 16 and len(N1) == 4 and len(N3) == 12 and not OUT_OF_SECTOR
ok &= all(abs(x) <= 1 for q in states for x in q) and all(sum(q) == 1 for q in states)
ok &= sp.expand(h - (W - eps * (F + F.T) + eps ** 2 * F.T * F)) == sp.zeros(n, n)
h3 = h.extract(N3, N3)
ok &= sp.expand(h3 * h3 - a * h3) == sp.zeros(12, 12) and sp.expand(h3.trace() - 3 * a) == 0
xx = sp.Symbol("x")
ok &= sp.expand(h.extract(N1, N1).charpoly(xx).as_expr() - xx * (xx - 1) ** 2 * (xx - a)) == 0
for Js in (JRES, JCOH):
    G = sum((j.T * j for j in Js), sp.zeros(n, n))
    ok &= G.extract(N1, N1) == 4 * W.extract(N1, N1) and G.extract(N3, N3) == sp.zeros(12, 12)
    ok &= all(j * Avec == sp.zeros(n, 1) and j[:, N3] == sp.zeros(n, 12) and j[N1, :] == sp.zeros(4, n) for j in Js)
psi_un = Avec + eps * sp.sqrt(3) * svec
ok &= sp.expand(Mh * psi_un) == sp.zeros(n, 1)
check("E1 model", ok, "16 physical states (4 with one record, 12 with three), every hop and mark stays in the Gauss sector; h = (W - eps F)^T (W - eps F); on N=3 h^2 = (1+3eps^2)h "
      "(energies 0 x9, Omega x3), on N=1 spectrum {0, 1, 1, 1+3eps^2}; loss sum j^T j = 4W on N=1 and 0 on N=3 (both "
      "instruments); every mark annihilates A and vanishes on N=3; the dressed input is annihilated by W - eps F")

# ---------------------------------------------------------------- E2: why the born branch factorizes (all lambda)
Hl = dl * eps ** -4 * h + K * lam * E2
P2 = sp.Matrix.hstack(Avec, svec)
ok = True
for v in (Avec, svec):
    for M in (Hl, sum((j.T * j for j in JRES), sp.zeros(n, n))):
        w_ = sp.expand(M * v)
        coef = P2.T * w_
        ok &= sp.expand(w_ - P2 * coef) == sp.zeros(n, 1)
ok &= all(sp.expand(Hl[i, k]) == 0 for i in N1 for k in N3) and all(sp.expand(Hl[i, k]) == 0 for i in N3 for k in N1)
Jss = {nm: sum((j * svec * svec.T * j.T for j in Js), sp.zeros(n, n)) for nm, Js in (("res", JRES), ("coh", JCOH))}
ok &= all(Jss[k].trace() == 4 and all(x.is_rational for x in Jss[k]) for k in Jss)
check("E2 born branch", ok, "span{A, s} is invariant under H_lam and the loss, H_lam does not mix N=1 and N=3, and no mark or loss "
      "acts on N=3; so rho(t) = |v><v| + (4 kappa/eps^2) int_0^t |<s,v(u)>|^2 e^{-iH(t-u)} rho_prep e^{iH(t-u)} du with the "
      "eps-free prepared first-event ensemble rho_prep = J(ss^T)/4 (trace 4 exactly): every coherence block P_E rho P_E' of "
      "the born branch is P_b(t) phi(E-E') P_E rho_prep P_E', phi the birth-time characteristic function")

# ---------------------------------------------------------------- E3: lambda = 0, the slow no-event eigenvector
H1 = sp.Matrix([[3 * eps ** 2, -sp.sqrt(3) * eps], [-sp.sqrt(3) * eps, 1]]) * dl / eps ** 4
Gm = -sp.I * H1 - (2 * kap / eps ** 2) * sp.diag(0, 1)
ell = sp.Matrix([1, sp.sqrt(3) * eps]) / sp.sqrt(a)
rr = sp.Matrix([sp.sqrt(3) * eps, -1]) / sp.sqrt(a)
Q = sp.Matrix.hstack(ell, rr)
Gq = sp.simplify(Q.T * Gm * Q)                                   # low/high coordinates
z, c2 = sp.symbols("z c2")
cp = sp.expand((Gq - z * sp.eye(2)).det() * eps ** 4)
ser = sp.Poly(sp.expand(sp.series(cp.subs(z, -6 * kap + c2 * eps ** 2), eps, 0, 3).removeO()), eps).all_coeffs()[::-1]
ok = sp.expand(ser[0]) == 0 and sp.expand(ser[1]) == 0
c2v = sp.solve(ser[2], c2)
ok &= len(c2v) == 1 and sp.simplify(c2v[0] - (18 * kap - 12 * sp.I * kap ** 2 / dl)) == 0
hi_comp = sp.series(((-6 * kap + c2v[0] * eps ** 2) - Gq[0, 0]) / Gq[0, 1], eps, 0, 5).removeO()
ok &= sp.simplify(hi_comp + 2 * sp.sqrt(3) * sp.I * kap / dl * eps ** 3) == 0
check("E3 no-event coherence", ok, "slow root z_s = -6kappa + (18kappa - 12i kappa^2/delta) eps^2 + O(eps^4) and the slow eigenvector's "
      "high component (low component 1) is -2 sqrt3 i (kappa/delta) eps^3 + O(eps^5): the unborn branch carries coherence "
      "C_no(t) = 2|<d,v><r,v>| = 4 sqrt3 (kappa/delta) eps^3 e^{-12 kappa t} (1 + O_T(eps^2)) (fast part O(eps^3) e^{-2kappa t/eps^2})")

# ---------------------------------------------------------------- E4: lambda > 0 splits the zero cluster
FtF = (F.T * F).extract(occ3, occ3)
ev = {e: vs for e, m, vs in FtF.eigenvects()}


def emb(v):
    y = sp.zeros(n, 1)
    for k, i in enumerate(occ3):
        y[i] = v[k]
    return y


null = sp.GramSchmidt([emb(v) for v in ev[0]], True)
sym = sp.GramSchmidt([emb(v) for v in ev[3]], True)
ok = len(null) == 6 and len(sym) == 3
ok &= all(sp.expand(Hl * v - 2 * K * lam * v) == sp.zeros(n, 1) for v in null)
blk = sp.Matrix([[3 * eps ** 2, -sp.sqrt(3) * eps], [-sp.sqrt(3) * eps, 1]]) * dl / eps ** 4 + K * lam * sp.diag(2, 3)
for sv in sym:
    fv = F * sv / sp.sqrt(3)
    B2 = sp.Matrix.hstack(sv, fv)
    ok &= sp.simplify(B2.T * B2 - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify(B2.T * Hl * B2 - blk) == sp.zeros(2, 2)
    ok &= sp.simplify(Hl * B2 - B2 * (B2.T * Hl * B2)) == sp.zeros(n, 2)
Mpd = blk - 2 * K * lam * sp.eye(2)
ok &= sp.simplify(Mpd.det() - 3 * K * lam * dl * eps ** -2) == 0 and sp.simplify(Mpd.trace() - (dl * a / eps ** 4 + K * lam)) == 0
mu_minus = sp.Rational(1, 2) * (blk.trace() - sp.sqrt(blk.trace() ** 2 - 4 * blk.det()))
split = sp.series(mu_minus - 2 * K * lam, eps, 0, 5).removeO()
ok &= sp.simplify(split - 3 * K * lam * eps ** 2 * (1 - 3 * eps ** 2)) == 0
Psym = sum((v * v.T for v in sym), sp.zeros(n, n))
Pnull = sum((v * v.T for v in null), sp.zeros(n, n))
consts = {}
for k in ("res", "coh"):
    X = Pnull * (Jss[k] / 4) * Psym
    svs = sorted(sp.nsimplify(sp.sqrt(e)) for e, m in (X * X.T).eigenvals().items() for _ in range(m) if e != 0)
    Y = (Jss[k] / 4) * F.T
    tn = sum(sp.sqrt(sp.nsimplify(e)) * m for e, m in (Y * Y.T).eigenvals().items() if e != 0)
    consts[k] = (sp.nsimplify(2 * sum(svs)), sp.nsimplify(sp.radsimp(2 * tn)))
ok &= consts["res"][0] == 2 * sp.sqrt(2) / 9 and consts["coh"][0] == 4 * sp.sqrt(2) / 9
ok &= sp.simplify(consts["res"][1] - (1 + sp.sqrt(6) / 3)) == 0 and sp.simplify(consts["coh"][1] - (sp.sqrt(3) / 3 + 2 * sp.sqrt(6) / 3)) == 0
check("E4 split cluster", ok, "for every lam > 0 the six F-null occupied states are exact eigenvectors at 2K lam, the rest of N=3 is three "
      "identical 2x2 blocks delta eps^-4 [[3eps^2, -sqrt3 eps], [-sqrt3 eps, 1]] + K lam diag(2,3), and mu_- - 2K lam > 0 (det of the "
      "shifted block is 3K lam delta/eps^2, trace positive) with mu_- - 2K lam = 3 K lam eps^2 + O(eps^4): the lam = 0 zero cluster "
      "splits.  The prepared ensemble's coherence between the two parts is exactly 2||P_null rho_prep P_sym||_1 = %s (resolved), %s "
      "(coherent); its energy coherence at lam = 0 is 2||rho_prep F^T||_1 eps + O(eps^2) = (%s) eps, (%s) eps"
      % (consts["res"][0], consts["coh"][0], consts["res"][1], consts["coh"][1]))

# ================================================================ float families: the full GKLS superoperator
Fn, Wn, E2n = (np.array(M.tolist(), dtype=float) for M in (F, W, E2))
JRn = [np.array(j.tolist(), dtype=float) for j in JRES]
JCn = [np.array(j.tolist(), dtype=float) for j in JCOH]
An, sn = np.array(Avec.tolist(), dtype=float).ravel(), np.array(svec.tolist(), dtype=float).ravel()
Pnull_n = np.array(Pnull.tolist(), dtype=float)
kappa_v, delta_v, K_v, t_v = 1.0, 1.0, 1.0, 0.1


def ham(e, lm):
    M = Wn - e * Fn
    return delta_v * e ** -4 * (M.T @ M) + K_v * lm * E2n


def gkls(e, lm, inst):
    H = ham(e, lm)
    Ls = [np.sqrt(kappa_v) / e * j for j in (JRn if inst == "res" else JCn)]
    I = np.eye(n)
    Lv = -1j * (np.kron(I, H) - np.kron(H.T, I))
    Gam = sum(L.T @ L for L in Ls)
    for L in Ls:
        Lv = Lv + np.kron(L, L)
    Lv = Lv - 0.5 * (np.kron(I, Gam) + np.kron(Gam.T, I))
    psi = An + e * np.sqrt(3) * sn
    psi /= np.linalg.norm(psi)
    r = (expm(t_v * Lv) @ np.outer(psi, psi).astype(complex).reshape(-1, order="F")).reshape(n, n, order="F")
    return r, H, psi


def eig_groups(H):
    w, V = np.linalg.eigh(H)
    gs = []
    for i, x in enumerate(w):
        if gs and abs(x - w[gs[-1][-1]]) <= 1e-9 * max(1.0, abs(x)):
            gs[-1].append(i)
        else:
            gs.append([i])
    return w, V, gs


def coh(rho, H):
    w, V, gs = eig_groups(H)
    rt = V.T @ rho @ V
    D = np.zeros_like(rt)
    for g in gs:
        D[np.ix_(g, g)] = rt[np.ix_(g, g)]
    return np.abs(np.linalg.eigvalsh(rt - D)).sum()


def formula0(e, inst):
    """lambda = 0: C_no + 2 (kappa/eps^2) |J(t)| ||P_0 J(ss^T) P_Omega||_1, from the 2x2 no-event solution in closed form."""
    aa, Om = 1 + 3 * e ** 2, delta_v * (1 + 3 * e ** 2) / e ** 4
    H1n = delta_v * np.array([[3 / e ** 2, -np.sqrt(3) / e ** 3], [-np.sqrt(3) / e ** 3, 1 / e ** 4]])
    Gn = -1j * H1n - (2 * kappa_v / e ** 2) * np.diag([0.0, 1.0])
    ln, rn = np.array([1, np.sqrt(3) * e]) / np.sqrt(aa), np.array([np.sqrt(3) * e, -1]) / np.sqrt(aa)
    zz, U = np.linalg.eig(Gn)
    c = np.linalg.solve(U, ln)
    v = U @ (c * np.exp(zz * t_v))
    b = U[1, :] * c
    Jt = sum(b[i] * np.conj(b[k]) * np.exp(1j * Om * t_v) * (np.exp((zz[i] + np.conj(zz[k]) - 1j * Om) * t_v) - 1) /
             (zz[i] + np.conj(zz[k]) - 1j * Om) for i in range(2) for k in range(2))
    Ib = sum(b[i] * np.conj(b[k]) * (np.exp((zz[i] + np.conj(zz[k])) * t_v) - 1) / (zz[i] + np.conj(zz[k]))
             for i in range(2) for k in range(2)).real
    Jm = np.array(Jss[inst].tolist(), dtype=float)
    w, V, gs = eig_groups(ham(e, 0.0))
    Ph = sum(V[:, [i]] @ V[:, [i]].T for g in gs for i in g if abs(w[g[0]] - Om) < 1e-6 * Om)
    P0 = sum(V[:, [i]] @ V[:, [i]].T for g in gs for i in g if abs(w[g[0]]) < 1e-6 * Om)
    tn = np.linalg.svd(P0 @ Jm @ Ph, compute_uv=False).sum()
    Cno = 2 * abs(ln @ v) * abs(rn @ v)
    return Cno, 2 * (kappa_v / e ** 2) * abs(Jt) * tn, 1 - np.linalg.norm(v) ** 2, 2 * tn / 4, abs(Jt) / Ib


rows, okN1 = [], True
for inst in ("res", "coh"):
    for e in (0.3, 0.2, 0.15):
        rho, H, _ = gkls(e, 0.0, inst)
        C = coh(rho, H)
        Cno, Cb, Pb, Cp, ph = formula0(e, inst)
        okN1 &= abs(C - Cno - Cb) < 1e-9 * C and abs(np.trace(rho).real - 1) < 1e-12
        rows.append((inst, e, C, Cno, Cb, Cp, ph))
print("N1 (float, lam = 0, t = 0.1, delta = K = kappa = 1): direct 256-dim GKLS C_H vs C_no + P_b C_prep |phi(Omega)|: " +
      "; ".join("%s eps %.2f %.6e = %.6e + %.2e (C_prep %.4f, |phi| %.1e)" % (i, e, C, Cn, Cb, Cp, ph) for i, e, C, Cn, Cb, Cp, ph in rows if e != 0.2))
check("N1 identity", okN1, "the exact decomposition matches the direct superoperator to 1e-9 relative at 6 points")

lead = []
for e in (0.1, 0.05, 0.025):
    Cno, Cb, Pb, Cp, ph = formula0(e, "res")
    lead.append((e, (Cno + Cb) / (4 * np.sqrt(3) * e ** 3 * np.exp(-12 * t_v)), Cb / e ** 5, Cp / e, ph / e ** 4))
print("N2 (float, lam = 0) C_H / [4 sqrt3 eps^3 e^{-12 kappa t}], C_born/eps^5, C_prep/eps, |phi(Omega)|/eps^4: " +
      "; ".join("eps %.3f: %.5f %.3f %.4f %.2f" % x for x in lead))
okN2 = abs(lead[-1][1] - 1) < 4 * lead[-1][0] ** 2 * 10 and abs(lead[-1][1] - 1) < abs(lead[0][1] - 1) and all(x[2] < 50 for x in lead)
okN2 &= abs(lead[-1][3] - float(consts["res"][1])) < 0.01
check("N2 lam = 0 asymptotics", okN2, "C_H = 4 sqrt3 (kappa/delta) eps^3 e^{-12 kappa t} (1 + O(eps^2)); the born branch is O(eps^5): "
      "|phi(Omega)| = O(eps^4) cuts the prepared ensemble's (1 + sqrt6/3) eps")

res3, okN3 = [], True
for inst in ("res", "coh"):
    lim = (1 - np.exp(-12 * kappa_v * t_v)) * float(consts[inst][0])
    for lm in (0.25, 1.0):
        vals = []
        for e in (0.2, 0.1, 0.05):
            rho, H, psi = gkls(e, lm, inst)
            w, V, gs = eig_groups(H)
            gm = [g for g in gs if any(np.linalg.norm(Pnull_n @ V[:, i]) < 1e-6 and np.linalg.norm(V[occ3, i]) > 0.5 for i in g)
                  and abs(w[g[0]] - 2 * K_v * lm) > 1e-12 and abs(w[g[0]] - 2 * K_v * lm) < 1.0]
            Pm = sum((V[:, [i]] @ V[:, [i]].T for g in gm for i in g), np.zeros((n, n)))
            low = 2 * np.linalg.svd(Pnull_n @ rho @ Pm, compute_uv=False).sum()
            cin = coh(np.outer(psi, psi), H)
            vals.append((e, coh(rho, H), low - cin))
        okN3 &= all(x[2] > 0.25 * lim for x in vals) and abs(vals[-1][1] - lim) < abs(vals[0][1] - lim) and abs(vals[-1][1] - lim) < 0.01 * lim + 0.004
        res3.append((inst, lm, lim, vals))
print("N3 (float, lam > 0, t = 0.1) C_H(rho) and the obstruction 2||P_null rho P_mu-||_1 - C_H(psi) vs the limit (1 - e^{-12 kappa t}) Chat: " +
      "; ".join("%s lam %.2f lim %.5f: " % (i, lm, L) + " ".join("%.5f/%.5f" % (C, lo) for e, C, lo in v) for i, lm, L, v in res3))
check("N3 lam > 0", okN3, "for lam = 1/4 and 1 the coherence approaches the lam-free limit (eps = 0.2, 0.1, 0.05) and the obstruction "
      "lower bound stays positive: an energy-stationary supply misses the lam > 0 occurrence by an O(1) trace distance")

print("time %.0f s" % (time.time() - T0))
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS))
    sys.exit(1)
print("SUMMARY: PARTIAL (first pass on batch 14; PR8929's deferred coherent-fuel statement, preparation vs occurrence). Exact: the "
      "star's born branch is the eps-free prepared first-event ensemble evolved from a birth time tau, so each coherence block is "
      "P_b(t) E[e^{-i omega(t-tau)}] times the prepared one. With an energy-stationary supply (stationary reservoir, conserving "
      "unitary) the best trace error is the distance to the stationary set: at lam = 0 exactly C_H(rho(t)) = 4 sqrt3 (kappa/delta) "
      "eps^3 e^{-12 kappa t}(1 + O(eps^2)), carried by the unborn branch, versus 2 sqrt(p(1-p)) ~ 2 sqrt(c) eps to prepare one "
      "actual output. For every lam in (0,1] the electric term splits the zero cluster by 3K lam eps^2 and the error tends to "
      "(1 - e^{-12 kappa t}) 2 sqrt2/9 (resolved; 4 sqrt2/9 coherent): not uniform in lam.")
print("HIT: the actual star occurrence needs far less energy coherence than a prepared output at lam = 0 (C_H = 4 sqrt3 (kappa/"
      "delta) eps^3 e^{-12 kappa t} versus 2 sqrt(p(1-p)) per output, because the birth-time characteristic function at the Bohr "
      "frequency multiplies every born coherence), but for every lam in (0,1] an energy-stationary supply misses it by a "
      "lam-independent (1 - e^{-12 kappa t}) 2 sqrt2/9 (resolved) or 4 sqrt2/9 (coherent) as eps -> 0")
