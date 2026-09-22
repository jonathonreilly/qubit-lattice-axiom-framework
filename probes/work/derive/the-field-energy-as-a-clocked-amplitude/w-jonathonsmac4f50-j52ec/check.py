"""the-field-energy-as-a-clocked-amplitude, attempt a3 (w-jonathonsmac4f50-j52ec).  Route: FIXED modes of the rate-independent generator.

Rates w = phi^2; the walk H = sum_a sigma_a S_a (block 54), S_a = (T_a - T_a^dag)/(2i); clocked generator phi H phi.  A background of many
amplitudes = the filled lower band of H (its modes do NOT depend on the rates); its clocked energy E_fix[phi] = tr(P_- phi H phi).
Exact: Fractions and sympy (Q(sqrt2, sqrt3) on the 4^3 torus).  Floating point only in the labelled NUMERIC lines.
"""
import itertools
import math
import random
from fractions import Fraction as F

import numpy as np
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


rng = random.Random(20260922)

# ================================================================== (a) the rewriting, exactly (3^3 torus)
L = 3
sites = list(itertools.product(range(L), repeat=3)); idx = {s: n for n, s in enumerate(sites)}; N = len(sites)
bonds = [(idx[s], idx[tuple((s[d] + (1 if d == a else 0)) % L for d in range(3))]) for s in sites for a in range(3)]
phi = [F(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(N)]
c = F(7, 3)
Lam = [[F(0)] * N for _ in range(N)]
for x, y in bonds:
    Lam[x][x] += 1; Lam[y][y] += 1; Lam[x][y] -= 1; Lam[y][x] -= 1
lhs = c * sum((phi[x] - phi[y]) ** 2 for x, y in bonds)
rhs = sum(phi[x] * c * Lam[x][y] * phi[y] for x in range(N) for y in range(N))           # <1| phi (c Lambda) phi |1>
zero_mode = all(sum(Lam[x][y] * phi[y] * (1 / phi[y]) for y in range(N)) == 0 for x in range(N))  # Lambda phi (1/phi) = Lambda 1 = 0
want("A1 (a) EXACT (3^3 torus, random rational rates): c sum_bonds (phi_x - phi_y)^2 = <1| phi (c Lambda) phi |1>; and (b)'s key identity "
     "phi Lambda phi (1/phi) = 0: the clocked uniform background is not stationary, the stationary one 1/phi carries zero energy (attempt a1)",
     lhs == rhs and zero_mode)

# ================================================================== (c) fixed modes: the clocked energy is exactly bilinear
# Filled: every negative-energy mode of H (the lower band of s.sigma, s = sin k); the eight k with s = 0 carry H(k) = 0 and cannot matter.
# For fixed modes E_fix[phi] = sum_{x,y} phi_x phi_y tr(P_-(y,x) H(x,y)) exactly; H is nearest-neighbour and P_- is translation invariant,
# so E_fix = beta sum_bonds phi_x phi_y with beta = (1/N) sum_k sin k_a tr(P_-(k) sigma_a) = -(1/N) sum_k s_a^2/|s|, the same for each a.
L4 = 4
ks = list(itertools.product(range(L4), repeat=3))
sin4 = [0, 1, 0, -1]
beta = sp.Integer(0)
for nk in ks:
    s = [sin4[n] for n in nk]
    ss = sum(v * v for v in s)
    if ss == 0: continue
    beta += -sp.Rational(s[0] ** 2) / sp.sqrt(ss)
beta = sp.simplify(beta / L4 ** 3)
c_fix = sp.simplify(-beta / 2)
closed = sp.simplify(c_fix - (3 + 3 * sp.sqrt(2) + sp.sqrt(3)) / 48) == 0
# direct: build the lower-band eigenvectors explicitly (plane waves times the -|s| coin) and sum <psi|phi H phi|psi> for a random phi
sites4 = list(itertools.product(range(L4), repeat=3)); idx4 = {s: n for n, s in enumerate(sites4)}; N4 = len(sites4)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]]); SIG = [sx, sy, sz]
coef = [sp.Integer(0)] * 3
for nk in ks:
    s = [sin4[n] for n in nk]; ss = sum(v * v for v in s)
    if ss == 0: continue
    Hk = s[0] * sx + s[1] * sy + s[2] * sz
    Pm = (sp.eye(2) - Hk / sp.sqrt(ss)) / 2                               # projector on the -|s| coin
    # sum over the (one) filled mode at k of <psi| phi H phi |psi> = (1/N) sum_bonds phi_x phi_y 2 Re[e^{i k_a} tr(Pm sigma_a)/(2i)]
    for a in range(3):
        ph = sp.exp(sp.I * sp.pi * nk[a] / 2)
        coef[a] += sp.simplify(2 * sp.re(ph * (Pm * SIG[a]).trace() / (2 * sp.I))) / N4     # site-independent bond amplitude
exact_ok = all(sp.simplify(cf - beta) == 0 for cf in coef)                                    # the same beta on every bond direction
want("C1 (c) EXACT, FIXED MODES (4^3 torus, Q(sqrt2, sqrt3)): filling the lower band of the rate-independent walk and clocking it, "
     "E_fix[phi] = sum_{x,y} phi_x phi_y tr(P_-(y,x) H(x,y)) = beta sum_bonds phi_x phi_y (the bond amplitude summed over the filled modes is site-independent and equal on the three directions), with beta = -(1/N) sum_k s_a^2/|s| "
     "= -(24 + 24 sqrt2 + 8 sqrt3)/192; hence E_fix = 3 beta sum_x w_x + c sum_bonds (phi_x - phi_y)^2 EXACTLY (every rate field, every "
     "order), c = -beta/2 = (3 + 3 sqrt2 + sqrt3)/48 > 0: block 56's simplest member plus a volume term", closed and exact_ok,
     f"c = {c_fix} = {float(c_fix):.6f}")

# identity sqrt(w_x w_y) = (w_x + w_y)/2 - (phi_x - phi_y)^2/2 and the u-form of the gradient term
p1, p2 = sp.symbols("p1 p2", positive=True)
ident = sp.simplify(p1 * p2 - ((p1 ** 2 + p2 ** 2) / 2 - (p1 - p2) ** 2 / 2)) == 0
u1, u2 = sp.symbols("u1 u2", real=True)
uform = sp.simplify(((sp.exp(u1 / 2) - sp.exp(u2 / 2)) ** 2 - sp.exp((u1 + u2) / 2) * 4 * sp.sinh((u1 - u2) / 4) ** 2).rewrite(sp.exp)) == 0
want("C2 (c) THE FORM: phi_x phi_y = (w_x + w_y)/2 - (phi_x - phi_y)^2/2 and (phi_x - phi_y)^2 = sqrt(w_x w_y) 4 sinh^2((u_x - u_y)/4), "
     "so the gradient part is (c/4) sum sqrt(w_x w_y)(u_x - u_y)^2 (1 + O((du)^2)): the task's form, with a definite sign (c > 0 because "
     "the filled band has negative bond energy)", ident and uform)

# ================================================================== (c) NUMERIC: Z^3 value, the variational bound, and the line
# Z^3: c = I/6 with I = int |s(k)| d^3k/(2pi)^3 (midpoint rule, labelled numeric)
M = 96
g = (np.arange(M) + 0.5) * 2 * np.pi / M
S2 = np.sin(g)[:, None, None] ** 2 + np.sin(g)[None, :, None] ** 2 + np.sin(g)[None, None, :] ** 2
I3 = float(np.sqrt(S2).mean())
cZ3 = I3 / 6


def walk_matrix(Lr, phi_vec):
    sites_ = list(itertools.product(range(Lr), repeat=3)); ix = {s: n for n, s in enumerate(sites_)}; Nn = len(sites_)
    SG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    Hm = np.zeros((2 * Nn, 2 * Nn), complex)
    for s_ in sites_:
        for a in range(3):
            t = tuple((s_[d] + (1 if d == a else 0)) % Lr for d in range(3))
            x, y = ix[s_], ix[t]
            Hm[2 * x:2 * x + 2, 2 * y:2 * y + 2] += SG[a] / (2j)
            Hm[2 * y:2 * y + 2, 2 * x:2 * x + 2] += -SG[a] / (2j)
    D = np.kron(np.diag(phi_vec), np.eye(2))
    return Hm, D @ Hm @ D, sites_, ix


Lr = 6
Hm, _, sites6, ix6 = walk_matrix(Lr, np.ones(Lr ** 3))
ev, V = np.linalg.eigh(Hm)
Pm = V[:, ev < -1e-12] @ V[:, ev < -1e-12].conj().T
nprng = np.random.default_rng(7)
bound_ok = True; fix_ok = True; rows = []
for trial in range(3):
    phv = np.exp(0.3 * nprng.standard_normal(Lr ** 3))
    _, Hw, _, _ = walk_matrix(Lr, phv)
    Efix_n = float(np.real(np.trace(Pm @ Hw)))
    evw = np.linalg.eigvalsh(Hw); Eopt = float(evw[evw < 0].sum())
    beta_n = float(np.real(np.trace(Pm @ Hm))) / (3 * Lr ** 3)
    bs = sum(phv[ix6[s_]] * phv[ix6[tuple((s_[d] + (1 if d == a else 0)) % Lr for d in range(3))]] for s_ in sites6 for a in range(3))
    fix_ok = fix_ok and abs(Efix_n - beta_n * bs) < 1e-9
    bound_ok = bound_ok and Eopt <= Efix_n + 1e-9
    rows.append(f"E_opt = {Eopt:.4f} <= E_fix = {Efix_n:.4f}")
want("C3 NUMERIC (6^3 torus, three random rate fields): E_fix = beta sum phi phi to 1e-9, and the self-consistent sea (the modes of phi H phi, "
     "attempt a1's reading) lies below: E_opt[phi] <= E_fix[phi] for EVERY rate field (variational principle; equal at uniform rates), so "
     "after the common volume term the re-optimised field energy is bounded by block 56's member with c = -beta/2; on Z^3 c = I/6 with "
     "I = int |sin k| d^3k/(2pi)^3", fix_ok and bound_ok, "; ".join(rows) + f"; Z^3: I = {I3:.6f}, c = {cZ3:.6f}, gamma = 2/c = {2 / cZ3:.4f}")

# the line (the task's numeric check): ring walk sigma_x (x) S, fixed lower band: beta_1D = -(1/N) sum |sin k| -> -2/pi, c = 1/pi
Nring = 512
kk = 2 * np.pi * np.arange(Nring) / Nring
beta1 = -np.abs(np.sin(kk)).mean()
Sring = np.zeros((Nring, Nring), complex)
for x in range(Nring):
    Sring[x, (x + 1) % Nring] += 1 / (2j); Sring[(x + 1) % Nring, x] += -1 / (2j)
Hring = np.kron(Sring, np.array([[0, 1], [1, 0]]))
evr, Vr = np.linalg.eigh(Hring); Pr = Vr[:, evr < -1e-12] @ Vr[:, evr < -1e-12].conj().T
phr = np.exp(0.2 * np.cos(2 * np.pi * 3 * np.arange(Nring) / Nring))
Dr = np.kron(np.diag(phr), np.eye(2))
Efr = float(np.real(np.trace(Pr @ (Dr @ Hring @ Dr))))
line_ok = abs(Efr - beta1 * sum(phr[x] * phr[(x + 1) % Nring] for x in range(Nring))) < 1e-8 and abs(beta1 + 2 / np.pi) < 1e-3
want("C4 NUMERIC, the line: the ring walk sigma_x (x) S with its lower band FIXED and clocked gives exactly beta sum_bonds phi phi, beta = "
     "-(1/N) sum |sin k| -> -2/pi, so c_fix = 1/pi on the line; by the variational bound the self-consistent sea of attempt a1 lies below it "
     "at every rate field", line_ok, f"beta = {beta1:.6f}, -2/pi = {-2 / np.pi:.6f}")

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL, exact: a background of many amplitudes read literally as FIXED filled modes of the rate-independent walk has "
          "clocked energy exactly beta sum_bonds sqrt(w_x w_y) = 3 beta sum w + c sum_bonds (phi_x - phi_y)^2 for every rate field (not only "
          f"at second order), c = -beta/2 > 0 computed from the filled band ((3 + 3 sqrt2 + sqrt3)/48 on 4^3; I/6 = {cZ3:.4f} on Z^3, gamma = "
          f"2/c = {2 / cZ3:.3f}): block 56's simplest member plus a volume term that normal ordering must remove; the self-consistent sea of "
          "attempt a1 lies below it at every rate field (variational bound); so the reading is a structure, not a rewriting, once the filled "
          "modes and normal ordering are supplied")
    print("HIT: the clocked energy of the filled lower band of the rate-independent walk is EXACTLY beta sum_bonds sqrt(w_x w_y) = 3 beta "
          "sum_x w_x + (-beta/2) sum_bonds (phi_x - phi_y)^2 for every rate field, with beta = -(1/(3N)) sum_k |sin k| (on 4^3: -beta/2 = "
          "(3 + 3 sqrt2 + sqrt3)/48): block 56's simplest member with a computed coefficient plus a volume term, and an upper bound for the "
          "self-consistent sea's field energy at every rate field")
