#!/usr/bin/env python3
"""J:derive:internal-hop-energy-and-the-two-masses:a1 -- worker w-macbookpro90c72-jdb03 (claude-opus-5-5).

Block 60's curvature member (bond form) with content that has hop energy and a supplied on-site confining agent.
'ok' lines are exact (sympy, Fractions); 'note' lines are floating point (sparse eigenvectors, box Green functions).
"""
import itertools, math, sys, time
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

T0 = time.time(); FAILS = []
def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)

# ------------------------------------------------------------------ A.eqs: the field equations with hop energy and the agent's stress
# 1D box, interior sites 1..3, walls 0 and 4 held at w = chi = 1; bonds crossed at sqrt(w_x w_y)/(chi_x chi_y) (blocks 59, 60);
# on-site energy per tick r_z + A_z(lam_z) timed by w_z (A the agent, its dependence on the local length supplied);
# F = -8K sum over bonds with an interior end of (N_y - N_x)(chi_y - chi_x), N = w chi (block 60's bond form).
K = sp.symbols("K", positive=True)
u = sp.symbols("u1:4", real=True); lam = sp.symbols("l1:4", real=True)
h = sp.symbols("h12 h23", real=True); r = sp.symbols("r1:4", real=True)
Af = [sp.Function(f"A{z}") for z in (1, 2, 3)]
w = [sp.exp(x) for x in u]; chi = [sp.exp(x / 2) for x in lam]; N = [wi * ci for wi, ci in zip(w, chi)]
Wc = [1] + chi + [1]; WN = [1] + N + [1]; Ww = [1] + w + [1]
t = [h[0] * sp.sqrt(w[0] * w[1]) / (chi[0] * chi[1]), h[1] * sp.sqrt(w[1] * w[2]) / (chi[1] * chi[2])]
Hc = sum(t) + sum(w[z] * (r[z] + Af[z](lam[z])) for z in range(3))
F = -8 * K * sum((WN[b + 1] - WN[b]) * (Wc[b + 1] - Wc[b]) for b in range(4))
Ecal = Hc + F
lapc = [Wc[z] + Wc[z + 2] - 2 * Wc[z + 1] for z in range(3)]; lapN = [WN[z] + WN[z + 2] - 2 * WN[z + 1] for z in range(3)]
good = True
for z in range(3):
    e = sp.diff(Hc, u[z]); tau = sp.Rational(1, 2) * sum(t[b] for b in (z - 1, z) if 0 <= b < 2)
    s = -sp.diff(w[z] * Af[z](lam[z]), lam[z])
    good &= sp.simplify(sp.diff(Ecal, u[z]) - (e + 8 * K * N[z] * lapc[z])) == 0
    good &= sp.simplify(sp.diff(Ecal, lam[z]) - (-tau - s + 4 * K * (N[z] * lapc[z] + chi[z] * lapN[z]))) == 0
    good &= sp.simplify(sp.diff(Hc, lam[z]) + tau + s) == 0 and sp.simplify(e - tau - w[z] * (r[z] + Af[z](lam[z]))) == 0
# the solved forms and P - Q per site: with e = w(r + a) + tau, N = w chi
ww, cc, tt, ss, rr, KK = sp.symbols("w chi tau s r K", positive=True)
ee = ww * rr + tt
Pz = (ee + 2 * tt + 2 * ss) / (8 * KK * cc); Qz = ee / (8 * KK * ww * cc)
good &= sp.simplify(8 * KK * (Pz - Qz) - (tt * (3 * ww - 1) / ww + 2 * ss - rr * (1 - ww)) / cc) == 0
ok("A.eqs", good, "from the bond form with hop energy and an agent: dE/du_z = e_z + 8K N_z (Lap chi)_z and dE/dlam_z = -tau_z - s_z + "
   "4K[N_z (Lap chi)_z + chi_z (Lap N)_z], e - tau = w (rest + agent), s = the agent's stress; so Lap chi = -e/(8K N), "
   "Lap N = (e + 2 tau + 2 s)/(8K chi) at every strength, and per site 8K(P - Q) = [tau (3w - 1)/w + 2s - r(1 - w)]/chi "
   "(r = on-site energy per tick, agent included); at weak field Lap lam = -e/(4K), Lap u = (e + tau + s)/(4K): the lengths "
   "carry E, the rates E + T + S")

# ------------------------------------------------------------------ A.virial: the two-step dilation on Z^3 (exact, finitely supported vectors)
def add(dst, k, v):
    if v[0] or v[1]:
        a = dst.get(k, (Fr(0), Fr(0))); dst[k] = (a[0] + v[0], a[1] + v[1])
def cmul(c, v):
    return (c[0] * v[0] - c[1] * v[1], c[0] * v[1] + c[1] * v[0])
def lin(*terms):
    out = {}
    for c, vec in terms:
        for k, v in vec.items():
            add(out, k, cmul(c, v))
    return {k: v for k, v in out.items() if v[0] or v[1]}
ONE, I_, HALF = (Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(1, 2), Fr(0))
def shift(vec, j, s):          # (T_j^s psi)(p) = psi(p + s e_j)
    out = {}
    for (p, c), v in vec.items():
        q = list(p); q[j] -= s; out[(tuple(q), c)] = v
    return out
def Sop(vec, j): return lin(((Fr(0), Fr(-1, 2)), shift(vec, j, 1)), ((Fr(0), Fr(1, 2)), shift(vec, j, -1)))
def Cop(vec, j): return lin((HALF, shift(vec, j, 1)), (HALF, shift(vec, j, -1)))
def Kop(vec, j): return lin(((Fr(0), Fr(-1, 4)), shift(vec, j, 2)), ((Fr(0), Fr(1, 4)), shift(vec, j, -2)))
def diag(vec, f): return {k: cmul((f(k[0]), Fr(0)), v) for k, v in vec.items() if f(k[0]) != 0}
def Xop(vec, j): return diag(vec, lambda p: Fr(p[j]))
def sig(vec, j):
    out = {}
    for (p, c), v in vec.items():
        if j == 0: add(out, (p, 1 - c), v)
        elif j == 1: add(out, (p, 1 - c), cmul(I_ if c == 0 else (Fr(0), Fr(-1)), v))
        else: add(out, (p, c), v if c == 0 else (-v[0], -v[1]))
    return out
eps_ = lambda p: Fr((-1) ** (sum(p) % 2))
Vf = lambda p: Fr(1, 3) * p[0] ** 2 - Fr(2, 5) * p[0] * p[1] + Fr(p[2], 7)
Mf = lambda p: Fr(1, 2) + Fr(1, 4) * (p[0] ** 2 + p[1] ** 2 + p[2] ** 2) - Fr(p[0] * p[2], 3)
def Hhop(vec): return lin(*[(ONE, sig(Sop(vec, j), j)) for j in range(3)])
def GP(vec): return lin(*[(HALF, Xop(Kop(vec, j), j)) for j in range(3)] + [(HALF, Kop(Xop(vec, j), j)) for j in range(3)])
def Aop(vec): return lin((ONE, diag(vec, Vf)), (ONE, diag(diag(vec, eps_), Mf)))
def H3(vec): return lin(*[(ONE, sig(Cop(Kop(vec, j), j), j)) for j in range(3)])
def S3(vec): return lin(*[(ONE, sig(Sop(Sop(Sop(vec, j), j), j), j)) for j in range(3)])
def comm_i(Aa, Bb, vec):       # i[A, B] vec
    return lin((I_, Aa(Bb(vec))), ((Fr(0), Fr(-1)), Bb(Aa(vec))))
good = True; nvec = 0
for p in itertools.product((-1, 0, 1, 2), repeat=3):
    for c in (0, 1):
        d = {(p, c): ONE}; nvec += 1
        good &= lin((ONE, comm_i(Hhop, GP, d)), ((Fr(-1), Fr(0)), H3(d))) == {}
        good &= lin((ONE, Hhop(d)), ((Fr(-1), Fr(0)), H3(d)), ((Fr(-1), Fr(0)), S3(d))) == {}
        good &= comm_i(GP, lambda v: diag(v, eps_), d) == {}
        good &= comm_i(GP, lambda v: lin((ONE, diag(v, lambda q: Fr(5, 3))), ((Fr(7, 2), Fr(0)), diag(v, eps_))), d) == {}
        W = comm_i(GP, Aop, d)
        good &= all(abs(q[0][j] - p[j]) <= 2 for q in W for j in range(3))
# finite-box no-go: i[H, G] = H forces tr H^2 = tr(i[H,G] H) = 0; the walk on a 2x2x2 box has tr H^2 > 0
trH2 = Fr(0)
for p in itertools.product((0, 1), repeat=3):
    for c in (0, 1):
        v = Hhop({(p, c): ONE}); v = {k: x for k, x in v.items() if all(0 <= k[0][j] <= 1 for j in range(3))}
        trH2 += sum(x[0] ** 2 + x[1] ** 2 for x in v.values())
good &= trH2 > 0
ok("A.virial", good, f"on Z^3 ({nvec} basis vectors, exact): the two-step dilation G_P = (1/2) sum {{x_j, K_j}}, K_j = (T_j^2 - T_j^-2)/4i, "
   "gives i[H_hop, G_P] = H3 = sum sigma_j C_j K_j and H_hop - H3 = sum sigma_j S_j^3; G_P commutes with the staggered term and "
   "with constant agents, so W = i[G_P, A] sees only the agent's gradients (reach 2): every stationary state has "
   f"T = <W> + <sum sigma_j S_j^3> exactly; and no G makes i[H_hop, G] = H_hop on a box (tr H_hop^2 = {trH2} on 2^3, not 0)")

# ------------------------------------------------------------------ B.dimer: a symmetric two-site body at strong field, exactly
mu, eta, G, X = sp.symbols("mu eta G chi", positive=True)
Q = mu / X + eta / (2 * X ** 3)                         # Q = e/(8K N) with e = m w + tau, tau = h w/(2 chi^2), w = N/chi
A = (mu + sp.Rational(3, 2) * eta / X ** 2) / X ** 2    # P = (e + 2 tau)/(8K chi) = N A, N = 1 - P G  =>  P = A/(1 + A G)
good = True
etaPQ = sp.solve(sp.Eq(A * (2 - X), Q), eta)            # P = Q  <=>  A (1 - Q G) = Q  <=>  A (2 - chi) = Q  (chi = 1 + Q G)
good &= len(etaPQ) == 1 and sp.simplify(etaPQ[0] - 2 * mu * X ** 2 * (X - 1) / (3 - 2 * X)) == 0
fGmu = sp.simplify(sp.solve(sp.Eq(X, 1 + G * Q.subs(eta, etaPQ[0])), mu)[0] * G)
good &= sp.simplify(fGmu - X * (X - 1) * (3 - 2 * X) / (2 - X)) == 0
num = sp.factor(sp.numer(sp.together(sp.diff(fGmu, X))))
good &= sp.expand(num + (4 * X ** 3 - 17 * X ** 2 + 20 * X - 6)) == 0 or sp.expand(num - (4 * X ** 3 - 17 * X ** 2 + 20 * X - 6)) == 0
cub = sp.Poly(4 * X ** 3 - 17 * X ** 2 + 20 * X - 6, X)
roots = [rt for rt in cub.real_roots() if 1 < rt < sp.Rational(3, 2)]
good &= len(roots) == 1
xs = roots[0]; fmax = fGmu.subs(X, xs)
good &= sp.Rational(2236, 10000) < fmax < sp.Rational(2238, 10000) and sp.Rational(1314, 1000) < xs < sp.Rational(1316, 1000)
wPQ = (2 - X) / X                                       # N = 1 - QG = 2 - chi on the locus
tau_over_mw = sp.simplify((etaPQ[0] / (2 * X ** 2)) / mu)
Wsym = sp.symbols("w", positive=True)
good &= sp.simplify(tau_over_mw.subs(X, 2 / (1 + Wsym)) - (1 - Wsym) / (3 * Wsym - 1)) == 0
ok("B.dimer", good, "two sites with rest energy m each and one internal bond of bare hop energy h (mu = m/8K, eta = h/8K, "
   "G = g(z,z) + g(z,z')): Q = mu/chi + eta/(2chi^3), P = A/(1 + AG), A = (mu + 3eta/(2chi^2))/chi^2, chi = 1 + QG; P = Q iff "
   "eta = 2 mu chi^2 (chi - 1)/(3 - 2chi) and G mu = chi(chi - 1)(3 - 2chi)/(2 - chi), chi in (1, 3/2) (w = (2 - chi)/chi > 1/3, "
   f"tau/(m w) = (1 - w)/(3w - 1)); the locus reaches G mu = {float(fmax):.5f} at the root chi = {float(xs):.5f} of "
   "4chi^3 - 17chi^2 + 20chi - 6 and no further")

# ------------------------------------------------------------------ floating point: bags of the staggered mass (weak field, part (a))
import scipy.sparse as sps, scipy.sparse.linalg as spla
sgm = [sps.csr_matrix(np.array(m_, complex)) for m_ in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
I2 = sps.identity(2, format="csr")
def bag(L, m0, v):
    I = sps.identity(L, format="csr"); T1 = sps.diags([np.ones(L - 1)], [1], shape=(L, L), format="csr")
    S1 = (T1 - T1.T) / 2j; C1 = (T1 + T1.T) / 2; K1 = (S1 @ C1 + C1 @ S1) / 2; x = np.arange(L) - (L - 1) / 2
    def emb(Aa, j):
        m_ = [I, I, I]; m_[j] = Aa; return sps.kron(sps.kron(m_[0], m_[1]), m_[2], format="csr")
    g = np.indices((L, L, L)).reshape(3, -1); co = [x[g[j]] for j in range(3)]; ep = (-1.0) ** g.sum(0)
    S = [emb(S1, j) for j in range(3)]; C = [emb(C1, j) for j in range(3)]; Kk = [emb(K1, j) for j in range(3)]
    Xx = [emb(sps.diags(x), j) for j in range(3)]
    Hh = sum(sps.kron(S[j], sgm[j]) for j in range(3))
    H3m = sum(sps.kron((C[j] @ Kk[j] + Kk[j] @ C[j]) / 2, sgm[j]) for j in range(3))
    Gp = sum(sps.kron((Xx[j] @ Kk[j] + Kk[j] @ Xx[j]) / 2, I2) for j in range(3))
    r2 = sum(c_ ** 2 for c_ in co); Am = sps.kron(sps.diags((m0 + v * r2) * ep), I2, format="csr")
    xgA = sps.kron(sps.diags(2 * v * r2 * ep), I2, format="csr")
    wv, U = spla.eigsh((Hh + Am).tocsc(), k=4, sigma=0.9 * m0, which="LM")
    i = int(np.argmin(np.where(wv > 0, wv, np.inf))); psi = U[:, i]; E = wv[i]
    ev = lambda O: float(np.real(psi.conj() @ (O @ psi)))
    Wm = 1j * (Gp @ Am - Am @ Gp); T = ev(Hh)
    return E, T, ev(H3m) - ev(Wm), (T - ev(xgA)) / E, math.sqrt(ev(sps.kron(sps.diags(r2), I2)))
rows = []
for L, m0, v in ((16, 0.3, 0.04), (20, 0.2, 0.02), (24, 0.15, 0.01)):
    E, T, dv, res, rad = bag(L, m0, v)
    rows.append(f"radius {rad:.2f}: E {E:.4f}, T/E {T/E:.3f} (rates/lengths {1 + T/E:.3f} with a stressless agent), "
                f"<H3>-<W> {dv:.0e}, (T - <x.grad A>)/E {res:+.4f}")
print("note (floating) staggered-mass bags M = m0 + v r^2 on L^3 boxes, lowest positive state: " + "; ".join(rows))

# ------------------------------------------------------------------ floating point: the dimer on a box (part (b)), with a ledger control
from scipy.optimize import brentq
nx, ny, nz = 8, 7, 7; Kn = 0.5; n = nx * ny * nz
idx = lambda a, b, c: (a * ny + b) * nz + c
ins = lambda p: 0 <= p[0] < nx and 0 <= p[1] < ny and 0 <= p[2] < nz
rw, cl, vl = [], [], []
for p in itertools.product(range(nx), range(ny), range(nz)):
    i = idx(*p); rw.append(i); cl.append(i); vl.append(6.0)
    for dp in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        q = tuple(a + b for a, b in zip(p, dp))
        if ins(q):
            rw.append(i); cl.append(idx(*q)); vl.append(-1.0)
Lap = sps.csr_matrix((vl, (rw, cl)), shape=(n, n)).tocsc()
z1, z2 = idx(nx // 2 - 1, ny // 2, nz // 2), idx(nx // 2, ny // 2, nz // 2)
g1 = spla.spsolve(Lap, np.eye(1, n, z1).ravel()); g2 = spla.spsolve(Lap, np.eye(1, n, z2).ravel()); Gb = g1[z1] + g1[z2]
def dimer(mu_, eta_):
    ch = brentq(lambda c_: c_ - 1 - Gb * (mu_ / c_ + eta_ / (2 * c_ ** 3)), 1.0, 1e3)
    A_ = (mu_ + 1.5 * eta_ / ch ** 2) / ch ** 2; P_ = A_ / (1 + A_ * Gb); Q_ = mu_ / ch + eta_ / (2 * ch ** 3)
    return ch, P_, Q_
scan = []
for Gmu in (0.20, 0.25, 0.40):
    mu_ = Gmu / Gb; best = max(dimer(mu_, e_)[1] - dimer(mu_, e_)[2] for e_ in np.logspace(-4, 3, 300) * mu_)
    scan.append(f"G mu {Gmu}: max over eta >= 0 of (P - Q) {best:+.4f}")
c0 = 1.25; mu_ = float(fGmu.subs(X, c0)) / Gb; eta_ = 2 * mu_ * c0 ** 2 * (c0 - 1) / (3 - 2 * c0)
ch, P_, Q_ = dimer(mu_, eta_); chiF = 1 + Q_ * (g1 + g2); NF = 1 - P_ * (g1 + g2)
nb = []
for p in itertools.product(range(-1, nx + 1), range(-1, ny + 1), range(-1, nz + 1)):
    for dp in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
        q = tuple(a + b for a, b in zip(p, dp))
        if ins(p) or ins(q):
            nb.append((idx(*p) if ins(p) else -1, idx(*q) if ins(q) else -1))
nb = np.array(nb)
def ledger(uu, ll):
    wq = np.exp(uu); cq = np.exp(ll / 2); Nq = wq * cq
    Na = np.append(Nq, 1.0); ca = np.append(cq, 1.0)
    Fv = -8 * Kn * np.sum((Na[nb[:, 1]] - Na[nb[:, 0]]) * (ca[nb[:, 1]] - ca[nb[:, 0]]))
    return Fv + 8 * Kn * eta_ * np.sqrt(wq[z1] * wq[z2]) / (cq[z1] * cq[z2]) + 8 * Kn * mu_ * (wq[z1] + wq[z2])
u0, l0 = np.log(NF / chiF), 2 * np.log(chiF); dd = 1e-6; gmax = 0.0
for i in range(n):
    for which in (0, 1):
        a_, b_ = u0.copy(), l0.copy(); c_, d_ = u0.copy(), l0.copy()
        if which == 0: a_[i] += dd; c_[i] -= dd
        else: b_[i] += dd; d_[i] -= dd
        gmax = max(gmax, abs(ledger(a_, b_) - ledger(c_, d_)) / (2 * dd))
bend = 1 + 2 * Q_ / (P_ + Q_)
print(f"note (floating) dimer on an 8x7x7 box (G = {Gb:.4f}): on the locus at chi = 1.25 P - Q = {P_ - Q_:.0e}, bending/fall "
      f"{bend:.6f}, the full ledger's gradient over all {2 * n} variables {gmax:.0e}; " + "; ".join(scan))
print(f"runtime {time.time() - T0:.0f} s")

if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL at weak field the rates exceed the lengths by the hop energy plus the confining agent's stress, and the "
      "exact two-step virial ties the hop energy to the agent's gradients, so the two masses agree only when the agent's stress "
      "cancels it; at strong field P = Q needs a tuned internal hop energy that exists only up to a finite strength")
print("HIT: (a) with an on-site agent A of stress S (minus its energy's derivative in a uniform log-length), the weak-field "
      "lengths carry E and the rates E + T + S, T the hop energy; for every stationary state the two-step dilation G_P = "
      "(1/2) sum {x_j, (T_j^2 - T_j^-2)/4i} (commuting with the staggered term) gives exactly T = <i[G_P, A]> + <sum sigma_j S_j^3>: "
      "a stressless agent leaves the rates heavier by T (about half of E in the executed bags); an agent following stretched "
      "distances levels them only up to lattice terms.")
print("HIT: (b) at every strength 8K(P - Q) = sum_z [tau_z (3w_z - 1)/w_z + 2 s_z - r_z (1 - w_z)]/chi_z: internal hop energy "
      "raises P where clocks run faster than a third and lowers it where slower; a symmetric two-site body has P = Q iff "
      f"eta = 2 mu chi^2 (chi - 1)/(3 - 2 chi) with G mu = chi (chi - 1)(3 - 2 chi)/(2 - chi) <= {float(fmax):.5f}, so (c) beyond that "
      "strength P < Q and bending exceeds twice the fall for every internal hop energy.")
