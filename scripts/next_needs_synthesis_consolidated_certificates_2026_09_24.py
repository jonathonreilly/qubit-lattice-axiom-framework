#!/usr/bin/env python3
"""Synthesis of the next-needs blocks: one fast certificate per block, and the register of decision points.

The evening blocks (open PRs 9140, 9142, 9144, 9145, 9146, 9148, 9149, 9153) each supply structure and certify what
it costs. This runner recomputes one identity per block in a fast, independent form and checks the register of
decision points: every supplied choice is named, none is adopted. Supplied models, finite certificates, no physical
reading.

1. 9140: local record menus along four axes rebuild a random two-site state exactly; the graded pair
   (|01> +- |10>)/sqrt2 agrees on every parity-even local product; half the swap operator is positive on product states
   with smallest eigenvalue -1/2.
2. 9142: an isolated site's Bloch vector precesses about the record field, r.h is conserved, and two different clocks
   give the same field-menu odds.
3. 9144: a star of four dimers has the three-flavour free spectrum -3e, -e, e, 3e (32, 96, 96, 32) and an exactly
   conserved matter spin.
4. 9145: the scalar-gauge pattern is a null direction of the momentum form and the form changes only off ker G.
5. 9146: the fine Z_4^3 torus has 9600 ice states in 937 flip classes (largest 864), and the Jastrow optimum on the
   largest class is alpha = 0.14.
6. 9148: a short guided projector run on the fine torus reproduces the exact ground energy within errors.
7. 9149: on two composite sites with one link, the dressed bond commutes with both Gauss operators and the bare one
   does not; the partner product commutes with both.
8. 9153: the canonical zero-winding ice state with q reversed lines is ice with winding (2q, 0, 0), slab-independent.
9. The register: 14 decision points across the eight blocks, each used by at least one block, none adopted.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 600

RESULTS = []
T0 = time.time()
rng = np.random.default_rng(2424)


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0 + 0j, -1.0])
SIG = [X, Y, Z]
SP = np.array([[0, 1], [0, 0]], dtype=complex)
SM = SP.T.copy()


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def site_op(n, i, M):
    return kron(*([I2] * i + [M] + [I2] * (n - i - 1)))


# ------------------------------------------------ 1. composition (9140)
tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]) / np.sqrt(3.0)
proj = [0.5 * (I2 + n[0] * X + n[1] * Y + n[2] * Z) for n in tet]
menus = [kron(p, q) for p in proj for q in proj]
A_ = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
rho = A_ @ A_.conj().T
rho /= np.trace(rho).real
freqs = np.array([np.trace(rho @ m).real for m in menus])
gram = np.array([[np.trace(a.conj().T @ b) for b in menus] for a in menus]).real
rho_re = sum(c * m for c, m in zip(np.linalg.solve(gram, freqs), menus))
c1, c2 = kron(SM, I2), kron(Z, SM)
n1, n2 = c1.conj().T @ c1, c2.conj().T @ c2
psi_p, psi_m = np.zeros(4, dtype=complex), np.zeros(4, dtype=complex)
psi_p[1] = psi_p[2] = 1 / np.sqrt(2)
psi_m[1], psi_m[2] = 1 / np.sqrt(2), -1 / np.sqrt(2)
rp, rm = np.outer(psi_p, psi_p.conj()), np.outer(psi_m, psi_m.conj())
same = max(abs(np.trace((rp - rm) @ m)) for m in (np.eye(4), n1, n2, n1 @ n2))
W = 0.25 * (np.eye(4) + kron(X, X) + kron(Y, Y) + kron(Z, Z))
pos = min(np.trace(W @ kron(0.5 * (I2 + a @ np.array(SIG)) if False else 0.5 * (I2 + a[0] * X + a[1] * Y + a[2] * Z),
                             0.5 * (I2 + b[0] * X + b[1] * Y + b[2] * Z))).real
          for a, b in ((rng.normal(size=3), rng.normal(size=3)) for _ in range(500)) for a, b in [(a / np.linalg.norm(a), b / np.linalg.norm(b))])
check("9140: local record menus rebuild a two-site state; the graded pair is locally indistinguishable; half the swap is positive on products but not a state",
      np.abs(rho_re - rho).max() < 1e-12 and same < 1e-12 and abs(np.linalg.norm(rp - rm, 'nuc') / 2 - 1) < 1e-12
      and pos > -1e-12 and abs(np.linalg.eigvalsh(W).min() + 0.5) < 1e-12,
      f"reconstruction {np.abs(rho_re - rho).max():.0e}; graded pair agrees on local products to {same:.0e} with trace distance 1; "
      f"<ab|W|ab> >= {pos:.3f} over 500 product states, smallest eigenvalue {np.linalg.eigvalsh(W).min():+.2f}")

# ------------------------------------------------ 2. formation clock (9142)
hhat = np.array([0.6, 0.0, 0.8])
r0 = np.array([0.5, 0.6, 0.4])
r0 = 0.8 * r0 / np.linalg.norm(r0)
H1 = 0.5 * sum(hhat[a] * SIG[a] for a in range(3))
ts = np.arange(0, 40, 2e-3)
Kx = np.array([[0, -hhat[2], hhat[1]], [hhat[2], 0, -hhat[0]], [-hhat[1], hhat[0], 0]])
rt = np.array([(np.eye(3) + np.sin(t) * Kx + (1 - np.cos(t)) * Kx @ Kx) @ r0 for t in ts])
ev_t = np.linalg.eigvalsh(H1)
cons = np.abs(rt @ hhat - r0 @ hhat).max()


def recorded(f):
    F = np.concatenate([[0.0], np.cumsum(0.5 * (f[1:] + f[:-1]) * 2e-3)])
    dens = f * np.exp(-F)
    dens /= np.trapezoid(dens, dx=2e-3)
    return np.trapezoid(dens * 0.5 * (1 + rt @ hhat), dx=2e-3)


p_const, p_pur = recorded(np.ones(len(ts))), recorded(np.sum(rt * rt, axis=1))
check("9142: precession conserves r.h, so two different clocks record the same field-menu odds",
      cons < 1e-12 and abs(p_const - p_pur) < 1e-12 and abs(p_const - 0.5 * (1 + r0 @ hhat)) < 1e-12,
      f"r.h conserved to {cons:.0e}; constant and purity clocks both record {p_const:.4f} = (1 + r.h)/2")

# ------------------------------------------------ 3. composite sites (9144)
nq = 8
Jc = {1: (0, 1.0), 2: (1, 0.8), 3: (2, 0.6)}
tau = lambda i, a: site_op(nq, 2 * i, SIG[a])
sig = lambda i, a: site_op(nq, 2 * i + 1, SIG[a])
Hst = sum(J * (tau(0, lam) @ tau(l, lam)) @ sum(sig(0, a) @ sig(l, a) for a in range(3)) for l, (lam, J) in Jc.items())
Stot = [0.5 * sum(sig(i, a) for i in range(4)) for a in range(3)]
evs = np.linalg.eigvalsh(Hst)
e_ = np.sqrt(sum(J * J for _, J in Jc.values()))
levels = sorted({round(x, 8) for x in evs})
degs = [int(np.sum(np.abs(evs - lv) < 1e-6)) for lv in levels]
check("9144: a star of four dimers has the three-flavour free spectrum and an exactly conserved matter spin",
      len(levels) == 4 and np.allclose(levels, [-3 * e_, -e_, e_, 3 * e_], atol=1e-8) and degs == [32, 96, 96, 32]
      and max(np.abs(Hst @ S - S @ Hst).max() for S in Stot) < 1e-12,
      f"levels {[round(float(l), 6) for l in levels]} with degeneracies {degs}; [H, S] = 0")

# ------------------------------------------------ 4. linear graviton (9145)
L = 4
E3 = np.eye(3, dtype=int)


def key(x, i, j):
    return (tuple(int(c) % L for c in x), (min(i, j), max(i, j)))


cells = list(itertools.product(range(L), repeat=3))
slots = [key(x, j, j) for x in cells for j in range(3)] + [key(x, i, j) for x in cells for (i, j) in [(0, 1), (1, 2), (0, 2)]]
sid = {k: n for n, k in enumerate(slots)}
G = np.zeros((3 * L ** 3, len(slots)))
for r_, (x, j) in enumerate((x, j) for x in cells for j in range(3)):
    x = np.array(x)
    for k, c in [(key(x + E3[j], j, j), 1), (key(x, j, j), -1)] + [t for i in range(3) if i != j for t in [(key(x, i, j), 1), (key(x - E3[i], i, j), -1)]]:
        G[r_, sid[k]] += c
Spat = np.zeros((L ** 3, len(slots)))
for r_, c in enumerate(cells):
    x = np.array(c)
    for n_ in range(3):
        a, b = [q for q in range(3) if q != n_]
        for (j, i) in ((a, b), (b, a)):
            for s_ in (1, -1):
                Spat[r_, sid[key(x + s_ * E3[i], j, j)]] += 1
            Spat[r_, sid[key(x, j, j)]] -= 2
        i, j = min(a, b), max(a, b)
        for sh, cc in [((0, 0, 0), -1), (tuple(-E3[i]), 1), (tuple(-E3[j]), 1), (tuple(-E3[i] - E3[j]), -1)]:
            Spat[r_, sid[key(x + np.array(sh), i, j)]] += cc
weights = np.array([1.0 if k[1][0] == k[1][1] else 2.0 for k in slots])
diag_of = {c: [sid[key(c, j, j)] for j in range(3)] for c in cells}


def M_form(Ev):
    tr = np.array([Ev[diag_of[c]].sum() for c in cells])
    return float(np.sum(weights * Ev * Ev) - 0.5 * np.sum(tr * tr))


u_, sv_, vt_ = np.linalg.svd(G)
null = vt_[int(np.sum(sv_ > 1e-9)):]
s_vec = Spat.T @ rng.normal(size=len(cells))
E_in = null.T @ rng.normal(size=null.shape[0])
check("9145: the scalar-gauge pattern is a null direction of the momentum form, which is invariant on ker G only",
      np.abs(G @ Spat.T).max() == 0 and abs(M_form(s_vec)) < 1e-9 and abs(M_form(E_in + s_vec) - M_form(E_in)) < 1e-9
      and abs(M_form(rng.normal(size=len(slots)) + s_vec) - M_form(rng.normal(size=len(slots)))) > 1e-2,
      f"G S^T = 0; s.M0 s = {abs(M_form(s_vec)):.0e}; change on ker G {abs(M_form(E_in + s_vec) - M_form(E_in)):.0e}")

# ------------------------------------------------ 5-6. the ring model on the fine torus (9146, 9148)
Lc = 2
verts = list(itertools.product(range(Lc), repeat=3))
vid = {v: i for i, v in enumerate(verts)}
tail, head = np.zeros(24, dtype=int), np.zeros(24, dtype=int)
for v in verts:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % Lc
        tail[3 * vid[v] + a], head[3 * vid[v] + a] = vid[v], vid[tuple(w)]
plaq = []
for v in verts:
    for a, b in ((0, 1), (1, 2), (0, 2)):
        va, vb = list(v), list(v)
        va[a] = (va[a] + 1) % Lc
        vb[b] = (vb[b] + 1) % Lc
        plaq.append([3 * vid[v] + a, 3 * vid[tuple(va)] + b, 3 * vid[tuple(vb)] + a, 3 * vid[v] + b])
plaq = np.array(plaq)
psign = np.tile([1, 1, -1, -1], (24, 1))
states = []
for chunk in range(16):
    idx = np.arange(chunk * 2 ** 20, (chunk + 1) * 2 ** 20, dtype=np.int64)
    bits = ((idx[:, None] >> np.arange(24)) & 1) * 2 - 1
    out = np.zeros((len(idx), 8), dtype=int)
    for l in range(24):
        out[:, tail[l]] += (bits[:, l] == 1)
        out[:, head[l]] += (bits[:, l] == -1)
    states.append(bits[np.all(out == 3, axis=1)])
states = np.vstack(states)
code = {tuple(s): i for i, s in enumerate(states)}
rows, cols = [], []
nflip = np.zeros(len(states), dtype=int)
for i, s in enumerate(states):
    fl = np.abs((s[plaq] * psign).sum(axis=1)) == 4
    nflip[i] = fl.sum()
    for p in np.flatnonzero(fl):
        t = s.copy()
        t[plaq[p]] *= -1
        rows.append(i)
        cols.append(code[tuple(t)])
F = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(states),) * 2)
ncomp, labels = connected_components(F, directed=False)
sizes = np.bincount(labels)
big = np.flatnonzero(labels == sizes.argmax())
Hb = -F[big][:, big].toarray()
Nb = nflip[big].astype(float)
alphas = np.linspace(0, 1, 101)
curve = []
for a in alphas:
    w = np.exp(a * Nb)
    psi = w / np.linalg.norm(w)
    curve.append(psi @ Hb @ psi)
ev0 = np.linalg.eigvalsh(Hb)[0]
check("9146: the fine torus has 9600 ice states in 937 flip classes, largest 864; the Jastrow optimum is alpha = 0.14",
      len(states) == 9600 and ncomp == 937 and sizes.max() == 864 and abs(alphas[int(np.argmin(curve))] - 0.14) < 1e-9,
      f"{len(states)} states, {ncomp} classes, largest {sizes.max()}; alpha* = {alphas[int(np.argmin(curve))]:.2f}; exact E0 {ev0:.4f}")

# a short guided projector run on the largest class
pol = [[] for _ in range(24)]
for p, links in enumerate(plaq):
    for l in links:
        pol[l].append(p)
aff_of = [sorted({q for l in links for q in pol[l]}) for links in plaq]


def local_rates(s, alpha=0.2):
    C = (s[plaq] * psign).sum(axis=1)
    P = np.flatnonzero(np.abs(C) == 4)
    out = []
    for p in P:
        t = s.copy()
        t[plaq[p]] *= -1
        Cn = (t[plaq[aff_of[p]]] * psign[aff_of[p]]).sum(axis=1)
        dN = int((np.abs(Cn) == 4).sum()) - int((np.abs(C[aff_of[p]]) == 4).sum())
        out.append((p, np.exp(alpha * dN)))
    return out


n_w, dtau, blocks = 150, 0.1, 250
walk = [states[big[k]].copy() for k in rng.integers(len(big), size=n_w)]
E_ref, Eb = ev0, []
for b in range(blocks):
    w = np.ones(n_w)
    EL = np.zeros(n_w)
    for i in range(n_w):
        t = 0.0
        while True:
            rates = local_rates(walk[i])
            lam = sum(r for _, r in rates)
            E_loc = -lam
            dt = rng.exponential(1 / lam)
            if t + dt >= dtau:
                w[i] *= np.exp(-(E_loc - E_ref) * (dtau - t))
                EL[i] = E_loc
                break
            w[i] *= np.exp(-(E_loc - E_ref) * dt)
            t += dt
            probs = np.array([r for _, r in rates]) / lam
            p = rates[rng.choice(len(rates), p=probs)][0]
            walk[i][plaq[p]] *= -1
    Wt = w.sum()
    Eb.append((w * EL).sum() / Wt)
    cum = np.cumsum(w) / Wt
    picks = np.searchsorted(cum, (np.arange(n_w) + rng.random()) / n_w)
    walk = [walk[k].copy() for k in picks]
    E_ref = 0.9 * E_ref + 0.1 * Eb[-1]
Eb = np.array(Eb[blocks // 3:])
bins = Eb[:len(Eb) // 10 * 10].reshape(10, -1).mean(axis=1)
E_g, dE_g = Eb.mean(), bins.std(ddof=1) / np.sqrt(10)
check("9148: a short guided projector run on the largest class reproduces the exact ground energy",
      abs(E_g - ev0) < 3 * dE_g + 1e-3 * abs(ev0),
      f"exact {ev0:.4f}, projector {E_g:.4f} +- {dE_g:.4f}")

# ------------------------------------------------ 7. gauged composite charge (9149): two dimers, one link
n5 = 5                                                   # sigma_1, sigma_2, tau_1, tau_2, link
S1, S2, T1, T2 = (lambda a: site_op(n5, 0, SIG[a])), (lambda a: site_op(n5, 1, SIG[a])), (lambda a: site_op(n5, 2, SIG[a])), (lambda a: site_op(n5, 3, SIG[a]))
Elink = 0.5 * site_op(n5, 4, Z)
sp_l, sm_l = site_op(n5, 4, SP), site_op(n5, 4, SM)
n_1, n_2 = 0.5 * (np.eye(32) + S1(2)), 0.5 * (np.eye(32) + S2(2))
G1, G2 = Elink - n_1, -Elink - n_2 + np.eye(32)         # link oriented 1 -> 2; background 1 on the odd vertex 2
zz = S1(2) @ S2(2)
hop_d = site_op(n5, 0, SP) @ sp_l @ site_op(n5, 1, SM) + site_op(n5, 0, SM) @ sm_l @ site_op(n5, 1, SP)
hop_b = site_op(n5, 0, SP) @ site_op(n5, 1, SM) + site_op(n5, 0, SM) @ site_op(n5, 1, SP)
tt = T1(0) @ T2(0)
Hd, Hbare = tt @ (zz + 2 * hop_d), tt @ (zz + 2 * hop_b)
cn = lambda A, B: float(np.abs(A @ B - B @ A).max())
check("9149: the dressed composite bond commutes with both Gauss operators and the bare one does not; the partner product commutes with both",
      cn(G1, Hd) < 1e-12 and cn(G2, Hd) < 1e-12 and cn(G1, Hbare) > 0.5 and cn(T1(2) @ T2(2), Hd) < 1e-12,
      f"|[G, H_dressed]| = {max(cn(G1, Hd), cn(G2, Hd)):.0e}, |[G, H_bare]| = {cn(G1, Hbare):.1f}, |[tau^z tau^z, H]| = {cn(T1(2) @ T2(2), Hd):.0e}")

# ------------------------------------------------ 8. winding sectors (9153): canonical states on the 4^3 torus
Lw = 4
vw = list(itertools.product(range(Lw), repeat=3))
vidw = {v: i for i, v in enumerate(vw)}
tailw, headw, axw, cow = (np.zeros(3 * Lw ** 3, dtype=int) for _ in range(4))
for v in vw:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % Lw
        l = 3 * vidw[v] + a
        tailw[l], headw[l], axw[l], cow[l] = vidw[v], vidw[tuple(w)], a, v[a]
ok8 = True
detail8 = []
for q in (0, 1, 2):
    sigma = np.zeros(3 * Lw ** 3, dtype=int)
    for v in vw:
        i = vidw[v]
        sigma[3 * i], sigma[3 * i + 1], sigma[3 * i + 2] = (-1) ** v[1], (-1) ** v[0], (-1) ** v[0]
    for qq in range(q):
        for x in range(Lw):
            sigma[3 * vidw[(x, 1, qq)]] *= -1
    out = np.zeros(Lw ** 3, dtype=int)
    np.add.at(out, tailw, (sigma == 1).astype(int))
    np.add.at(out, headw, (sigma == -1).astype(int))
    Wslabs = [[int(sigma[(axw == a) & (cow == x)].sum()) for x in range(Lw)] for a in range(3)]
    ok8 &= np.all(out == 3) and all(len(set(s)) == 1 for s in Wslabs) and Wslabs[0][0] == 2 * q and Wslabs[1][0] == 0 and Wslabs[2][0] == 0
    detail8.append(f"q = {q}: ice {bool(np.all(out == 3))}, W = ({Wslabs[0][0]}, {Wslabs[1][0]}, {Wslabs[2][0]})")
check("9153: the canonical zero-winding ice state with q reversed lines is ice with winding (2q, 0, 0), slab-independent",
      ok8, "; ".join(detail8))

# ------------------------------------------------ 9. the register of decision points
REGISTER = {
    "D-tomo": ("readout locality of Record read as local tomography of reconstructions", ["9140"]),
    "D-alg": ("the composite's observables form the algebra generated by commuting local copies", ["9140"]),
    "D-form": ("a memoryless formation clock with a rate that is a function of the site's conditional state", ["9142"]),
    "D-menu": ("field-aligned antipodal menus where a recorded neighbour exists, a supplied axis elsewhere", ["9142"]),
    "D-comp": ("composite sites: a dynamical site paired with a partner qubit", ["9144", "9149"]),
    "D-roles": ("doubled-coordinate roles; here vertex matter, link U(1) field, cube Z2 partner", ["9144", "9149"]),
    "D-bond": ("the Yao-Lee bond and its odd three-dimer companion, dressed by link operators when gauged", ["9144", "9149"]),
    "D-background": ("the staggered background charge of the gauged composite model", ["9149"]),
    "D-osc": ("oscillator (Fock-type) slots for the tensor field, in place of rotor or clock slots", ["9145"]),
    "D-gauss": ("the exact vertex Gauss law of the link field", ["9146", "9148", "9149", "9153"]),
    "D-ring": ("the covariant plaquette clause -g (U + U^dag)", ["9146", "9148", "9149", "9153"]),
    "D-RK": ("the Rokhsar-Kivelson potential V N_flip", ["9146"]),
    "D-guide": ("the Jastrow guiding function exp(alpha N_flip) of the projector", ["9148", "9153"]),
    "D-dyn": ("the dynamics clause of the morning campaign, at its Heisenberg or compass point", ["9142", "9144"]),
}
BLOCKS = ["9140", "9142", "9144", "9145", "9146", "9148", "9149", "9153"]
used = {b: [d for d, (_, bl) in REGISTER.items() if b in bl] for b in BLOCKS}
check("the register: 14 decision points across eight blocks, each used by at least one block, none adopted",
      len(REGISTER) == 14 and all(len(u) >= 1 for u in used.values()) and all(len(bl) >= 1 for _, bl in REGISTER.values()),
      "; ".join(f"{b}: {', '.join(u)}" for b, u in used.items()))

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)} ({time.time() - T0:.0f} s)")
sys.exit(0 if all(RESULTS) else 1)
