#!/usr/bin/env python3
"""J:derive:a-chessboard-record-background-as-the-staggered-term:a2 - worker w-jonathonsmac4f50-j97fa (claude-opus-5-5).

Premise under test: 'Block 17 (#8151) found chessboard-ordered Gibbs states of the six-axis static law of records.'
Definitions: block 77 (open PR #8612): H_a = a0 + 2a sum_j cos k_j + sum_j sigma_j sin k_j on the qubit coin, eps(x) = (-1)^(x+y+z),
the staggered term m eps(x); block 53: rates u = log w, weak field u_x - (mean of u over the six neighbours) = source (zero-sum part on a
torus), a record enters as the additive source log kappa; block 54: clocked generator phi H phi, phi = e^(u/2).
Supplied clause of the task (stated, not adopted): a record's presence at a site adds a coin-scalar on-site energy c to the walker there.
Exact arithmetic: sympy; the torus spectrum check is floating point with its error stated.
"""
import itertools
import subprocess

import numpy as np
import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


# ================================================================ P1 the premise, read on block 17's own branch
B17 = 'physics-loop/admissibility-induced-law-block17-static-law-strong-coupling-order-chessboard-peierls-20260915'
NOTE = ('docs/ADMISSIBILITY_RULE_STATIC_SIX_AXIS_LAW_STRONG_COUPLING_LONG_RANGE_ORDER_AND_SEVERAL_GIBBS_STATES_'
        'REFLECTION_POSITIVITY_CHESSBOARD_PEIERLS_BOUNDED_THEOREM_NOTE_2026-09-15.md')
subprocess.run(['git', 'fetch', '-q', 'origin', B17], capture_output=True)
txt = subprocess.run(['git', 'show', f'origin/{B17}:{NOTE}'], capture_output=True, text=True).stdout
lines = txt.splitlines()
need = {
    'the chessboard is the estimate (T3 heading)': '## Theorem T3 — the chessboard estimate',
    'the states are translation invariant with aligned order': 'is a translation-invariant Gibbs state of',
    'the order parameter is agreement, not alternation': 'the static specification with `μ(v_0 = v_x) ≥ 1/2` for every `x`',
    'the claim scope': 'the torus law gives v_0 = v_x with probability above 1/2 for every x within a quarter of the side',
}
found = {k: [i + 1 for i, ln in enumerate(lines) if v in ln] for k, v in need.items()}
ok = len(lines) > 100 and all(found.values())
ok &= not any('sublattice' in ln.lower() or 'antiferro' in ln.lower() or 'staggered' in ln.lower() for ln in lines)
check('P1', ok, "TEXT (block 17's note on its PR branch): 'chessboard' in block 17 is the reflection-positivity chessboard "
      "ESTIMATE (T3), and its ordered Gibbs states are translation-invariant with mu(v_0 = v_x) >= 1/2 - agreement of "
      "contents, the same at every site; the note never mentions a sublattice, staggered or antiferromagnetic pattern. "
      "The premise 'chessboard-ordered Gibbs states' misreads the method's name as the phase's pattern",
      "; ".join(f"{k}: line(s) {v}" for k, v in found.items()))

# ================================================================ P2 what block 17's states give through the supplied clause
a0, a, c, m = sp.symbols('a0 a c m', real=True)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
ok = True
# in the static law every site carries a record, so the clause gives a0(x) = c at every site: H_a + c, no staggered term
for n in itertools.product((0, 1), repeat=3):
    kk = [sp.pi * v for v in n]
    s = [sp.sin(v) for v in kk]
    lev = a0 + c + 2 * a * sum(sp.cos(v) for v in kk)
    ok &= all(sp.simplify(x) == 0 for x in s) and sp.simplify(lev - (a0 + c + 2 * a * (3 - 2 * sum(n)))) == 0
check('P2', ok, "EXACT: in block 17's static law every site carries a record, so the supplied clause adds the same c at every "
      "site - an offset a0 -> a0 + c, no staggered term: at all eight zeros the coin vector still vanishes (block 77 T1), the "
      "species stay ungapped, and no rest energy arises. Block 17 supplies no chessboard record background: the route fails "
      "at its first step")

# ================================================================ C1 IF a chessboard background is supplied: the masses (block 77 T4 with m = c/2)
sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
I2 = sp.eye(2)
S = [sp.sin(k1), sp.sin(k2), sp.sin(k3)]
C = sp.cos(k1) + sp.cos(k2) + sp.cos(k3)
hk = 2 * a * C * I2 + S[0] * sx + S[1] * sy + S[2] * sz            # hops: flip sign under k -> k + (pi,pi,pi)
Hblk = sp.BlockMatrix([[hk + (c / 2) * I2, (c / 2) * I2], [(c / 2) * I2, -hk + (c / 2) * I2]]).as_explicit()
lam = sp.symbols('lambda', real=True)
ok = True
rows = []
for n in itertools.product((0, 1), repeat=3):
    sub = {k1: sp.pi * n[0], k2: sp.pi * n[1], k3: sp.pi * n[2]}
    ev = sorted(Hblk.subs(sub).eigenvals().keys(), key=lambda e: sp.N(e.subs({a: sp.Rational(1, 7), c: sp.Rational(3, 5)})))
    lev = 2 * a * (3 - 2 * sum(n))
    want = sorted([c / 2 - sp.sqrt(c ** 2 / 4 + lev ** 2), c / 2 + sp.sqrt(c ** 2 / 4 + lev ** 2)],
                  key=lambda e: sp.N(e.subs({a: sp.Rational(1, 7), c: sp.Rational(3, 5)})))
    ok &= len(ev) == 2 and all(sp.simplify(e - w) == 0 for e, w in zip(ev, want))
    rows.append(f"n={n}: {sp.simplify(want[1] - c / 2)}")
ok &= all(sp.simplify((sp.sqrt(c ** 2 / 4 + (2 * a * (3 - 2 * j)) ** 2)).subs(a, 0) - sp.Abs(c) / 2) == 0 for j in range(4))
check('C1', ok, "EXACT (the 4x4 block pairing k with k + (pi,pi,pi), at all eight zeros): IF records sit on one sublattice, the "
      "clause gives a0(x) = c/2 + (c/2) eps(x) and the energies are c/2 +- sqrt(c^2/4 + (2a(3 - 2|n|))^2): with a = 0 every "
      "species has the same rest energy |c|/2 (block 77 T3 - no species dependence, the task's HIT condition is not met); "
      "with a != 0 the (n, n+(111)) pairs have sqrt(c^2/4 + 36a^2) and sqrt(c^2/4 + 4a^2), block 77 T4's split with "
      "m = c/2 - the dependence is the a-term's, not the background's", "; ".join(rows[:2]) + " ...")

# ================================================================ C2 the same on an even torus, and the filling
def torus_H(L, av, cv, U=0.0, dl=0.0):
    sites = list(itertools.product(range(L), repeat=3))
    idx = {s_: i for i, s_ in enumerate(sites)}
    n = len(sites)
    sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
    H = np.zeros((2 * n, 2 * n), complex)
    eps = np.array([(-1) ** (sum(s_) % 2) for s_ in sites])
    u = U + dl * eps
    for s_ in sites:
        i = idx[s_]
        for j in range(3):
            t = list(s_); t[j] = (t[j] + 1) % L; t = tuple(t)
            jdx = idx[t]
            ph = np.exp((u[i] + u[jdx]) / 2)
            # symbol of (sigma_j sin k_j + 2a cos k_j): hop to +e_j with (a - i sigma_j/2)... use T_e psi(x) = psi(x - e)
            blk = av * np.eye(2) + 0.5j * sig[j]
            H[2 * i:2 * i + 2, 2 * jdx:2 * jdx + 2] += ph * blk.conj().T
            H[2 * jdx:2 * jdx + 2, 2 * i:2 * i + 2] += ph * blk
        H[2 * i:2 * i + 2, 2 * i:2 * i + 2] += np.exp(u[i]) * cv * (1 + eps[i]) / 2 * np.eye(2)
    return H, eps


L, av, cv = 4, 0.13, 0.6
H, eps = torus_H(L, av, cv)
ev = np.sort(np.linalg.eigvalsh(H))
ks = 2 * np.pi * np.arange(L) / L
pred = []
for kv in itertools.product(ks, repeat=3):
    Cv = sum(np.cos(kv)); sv = np.linalg.norm(np.sin(kv))
    for sgn in (1, -1):
        lamv = 2 * av * Cv + sgn * sv
        pred += [cv / 2 + np.sqrt(cv ** 2 / 4 + lamv ** 2) / 1, cv / 2 - np.sqrt(cv ** 2 / 4 + lamv ** 2)]
pred = np.sort(np.array(pred))
# each (k, k+pi) pair counted twice in the sum over all k: keep every other
pred = pred[::2] if len(pred) == 2 * len(ev) else pred
err = np.abs(np.sort(ev) - np.sort(pred)).max() if len(pred) == len(ev) else np.inf
prod_ok = sp.simplify((c / 2 + sp.sqrt(c ** 2 / 4 + lam ** 2)) * (c / 2 - sp.sqrt(c ** 2 / 4 + lam ** 2)) + lam ** 2) == 0
ok = err < 1e-10 and prod_ok and (ev <= 1e-12).sum() == (ev < cv / 2).sum()
check('C2', ok, "NUMERICAL (real-space generator on the 4^3 torus, a = 0.13, c = 0.6, spectrum against the formula) + EXACT: "
      "the two branches multiply to E_+ E_- = -lambda^2 <= 0, so one branch is never above zero and the other never below: "
      "the offset c/2 does not move the sea's filling (every state below the gap centre is at or below zero)",
      f"torus vs formula {err:.1e}")

# ================================================================ C3 the rates: felt only through the on-site term
U, dl = 0.37, 0.21
Hc, _ = torus_H(L, av, cv, U=U, dl=dl)
Href, _ = torus_H(L, av, cv * np.exp(dl), U=0.0, dl=0.0)
err_clock = np.abs(Hc - np.exp(U) * Href).max()
kap = sp.symbols('kappa', positive=True)
# block 53's weak-field rule with the zero-sum source: u - mean_nbrs(u) = (log kappa)(1 + eps)/2 - (log kappa)/2 = (log kappa/2) eps
dsym = sp.symbols('delta')
lhs_A = dsym - (-dsym)          # on eps = +1: u = delta, neighbours all -delta
eq = sp.Eq(lhs_A, sp.log(kap) / 2)
dsol = sp.solve(eq, dsym)[0]
ok = err_clock < 1e-12 and sp.simplify(dsol - sp.log(kap) / 4) == 0
check('C3', ok, "EXACT + NUMERICAL (4^3 torus): a chessboard of clocks u = U + delta eps rescales every nearest-neighbour hop by "
      "the same e^U (phi_x phi_y = e^U because eps_x + eps_y = 0) and the on-site term by e^(u_x): phi(H_hop + a0)phi = "
      "e^U [H_hop + (c/2) e^delta (1 + eps)], so the background is felt ONLY through the on-site term, whose amplitude it "
      "multiplies by e^delta; block 53's rule with the zero-sum part of the source log kappa (1 + eps)/2 gives delta = "
      "(log kappa)/4, i.e. m = (c/2) kappa^(1/4) in units of the hop",
      f"|phi H phi - e^U H(c e^delta)| = {err_clock:.1e}; delta = {dsol}")

# ================================================================ C4 covariance
def rot_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), int)
            for i, pi in enumerate(perm):
                M[i, pi] = signs[i]
            mats.append(M)
    return mats


G48 = rot_group()
proper = [M for M in G48 if round(np.linalg.det(M)) == 1]
pts = list(itertools.product(range(-3, 4), repeat=3))
epsf = lambda v: (-1) ** (int(sum(v)) % 2)
ok = len(proper) == 24 and all(epsf(M @ np.array(v)) == epsf(v) for M in G48 for v in pts)
ok &= all(epsf(np.array(v) + np.array(t)) == -epsf(v) for v in pts for t in ((1, 0, 0), (0, 1, 0), (1, 1, 1)))
check('C4', ok, "EXACT: eps is invariant under all 48 cube symmetries about a site (so under the 24 proper rotations) and "
      "changes sign under every odd translation: a chessboard background keeps the rotation covariance, breaks the odd "
      "translations, and comes in two copies (which sublattice); a coin scalar singles out no content direction")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: ROUTE FAILS AT step 1 (the premise): block 17's 'chessboard' is the reflection-positivity chessboard "
      "estimate and its ordered Gibbs states are translation-invariant with aligned contents; in its static law every site "
      "carries a record, so the supplied on-site clause gives a uniform offset and no staggered term. Conditional exact "
      "results if a sublattice background is supplied by other means: energies c/2 +- sqrt(c^2/4 + (2a(3-2|n|))^2) (one "
      "rest energy |c|/2 for all species when a = 0, block 77 T4's split otherwise), filling unchanged (E_+ E_- = -lambda^2), "
      "rates felt only through the on-site term with m = (c/2) kappa^(1/4)")
if all(RESULTS):
    print("HIT: the unit's premise is a misreading: block 17 (#8151) has no chessboard-ordered states - 'chessboard' names "
          "its reflection-positivity estimate (T3), and its Gibbs states are translation-invariant with mu(v_0 = v_x) >= 1/2 "
          "(T5-T6); every site carries a record in its static law, so a presence-sensitive coin-scalar clause gives only a "
          "uniform offset and no rest energy. If a sublattice record background were supplied otherwise, the walker's "
          "energies are exactly c/2 +- sqrt(c^2/4 + (2a(3-2|n|))^2), species-independent (|c|/2) for a = 0, the sea's filling "
          "unchanged, and a chessboard of clocks is felt only through the on-site term (m = (c/2) kappa^(1/4))")
