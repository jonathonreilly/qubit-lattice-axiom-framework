#!/usr/bin/env python3
"""Which slot assignments carry the tensor constraints as exact additive Gauss laws.

Question (open routes of probes 10, 14, 15; 2026-09-28): the constructed
finite-slot assignments store the momentum on every slot (probes 10, 14) or
the metric on every slot (probe 15). Could a mixed assignment keep a full
tensor rule as an exact additive Gauss law? Pre-registered in the probe's
scratch file. Revised after the first referee's FAILS verdict: 'additive' is
defined in Weyl form, supports are derived from the stencils, the exact
counts are asserted, and the rotor extension is withdrawn to a conditional
remark.

Definition. A rule row G = sum_a c_a X_a (one Hermitian operator per touched
slot) is an exact additive Gauss law if exp(i theta G) acts on each touched
slot a as a translation of the variable conjugate to X_a by the c-number
c_a theta (Weyl form). On a slot, a stored (diagonal) variable D with
discrete spectrum cannot be translated by a c-number: a unitary conjugation
preserves the spectrum. So each touched slot must store X_a itself (whose
conjugate phase is what gets translated).

Checks:
  A  finite slots: tr [C, D] = 0 for every C (the landed per-site CCR
     trace identity), so no generator translates a stored variable; the
     Weyl form for any discrete spectrum is the spectral argument above.
  B  supports derived from the landed stencils on the 4^3 torus: each
     momentum row touches slot types {jj, ij, jk}, the scalar row all six,
     and every slot at every position is touched by some momentum row and
     by some scalar row (no zero column), so the column support is the same
     for any generating set of the rule. Over all 64 slot-type assignments:
     the full momentum rule is additive only in the all-momentum assignment,
     the scalar rule only in the all-metric one; 15 mixed assignments make
     one momentum row additive, 3 make two, none all three; among
     cubic-symmetric assignments only the two pure ones keep any additive
     row. Because every slot is touched, the same holds for arbitrary
     per-slot (translation-breaking) assignments.
Prints one line per check, the N5 lines and TOTAL.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


rng = np.random.default_rng(20260928)
E3 = np.eye(3, dtype=int); FACE = {(0, 1): 3, (1, 2): 4, (0, 2): 5}


def spin(S):
    d = int(round(2 * S + 1)); ms = S - np.arange(d)
    return np.diag(ms)


# ---------------------------------------------------------------- A: finite slots: no generator translates a stored variable
worst = 0.0; dims = []
for S in (0.5, 1, 1.5, 2, 3):
    D = spin(S); d = D.shape[0]; dims.append(d)
    for _ in range(20):
        X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); C = X + X.conj().T
        worst = max(worst, abs(np.trace(C @ D - D @ C)))
check("A: finite slots: tr[C, D] = 0 for every C (the landed per-site CCR trace identity), so [C, D] = i c 1 with c != 0 is impossible and no one-parameter unitary group translates a stored variable by a c-number; the Weyl form holds for any discrete spectrum by spectral invariance",
      worst < 1e-10, f"max |tr[C, D]| over 20 random Hermitian C for spins 1/2..3 (dimensions {dims}): {worst:.1e}")

# ---------------------------------------------------------------- B: supports from the stencils, and all assignments
L = 4
cells = list(itertools.product(range(L), repeat=3)); cidx = {c: i for i, c in enumerate(cells)}; nslot = 6 * len(cells)
def sl(c, a):
    return 6 * cidx[tuple(np.array(c) % L)] + a
Gm = np.zeros((3 * len(cells), nslot), dtype=int); Sm = np.zeros((len(cells), nslot), dtype=int)
for c in cells:
    x = np.array(c)
    for j in range(3):
        r = 3 * cidx[c] + j
        Gm[r, sl(x + E3[j], j)] += 1; Gm[r, sl(x, j)] -= 1
        for i in range(3):
            if i != j:
                f = FACE[tuple(sorted((i, j)))]; Gm[r, sl(x, f)] += 1; Gm[r, sl(x - E3[i], f)] -= 1
    r = cidx[c]
    for j in range(3):
        for i in range(3):
            if i != j:
                Sm[r, sl(x + E3[i], j)] += 1; Sm[r, sl(x - E3[i], j)] += 1; Sm[r, sl(x, j)] -= 2
    for (i, j), f in FACE.items():
        Sm[r, sl(x, f)] -= 1; Sm[r, sl(x - E3[i], f)] += 1; Sm[r, sl(x - E3[j], f)] += 1; Sm[r, sl(x - E3[i] - E3[j], f)] -= 1
gsup = [sorted(set(int(k) % 6 for k in np.nonzero(Gm[3 * cidx[(1, 1, 1)] + j])[0])) for j in range(3)]
ssup = sorted(set(int(k) % 6 for k in np.nonzero(Sm[cidx[(1, 1, 1)]])[0]))
no_zero_col = bool(np.all(np.abs(Gm).sum(0) > 0) and np.all(np.abs(Sm).sum(0) > 0))
one_row = two_rows = all_rows = s_add = 0; cubic_ok = True
for bits in itertools.product([0, 1], repeat=6):                   # 1: momentum-stored type, 0: metric-stored type
    pd = {t for t in range(6) if bits[t]}
    rows_add = [j for j in range(3) if set(gsup[j]) <= pd]
    S_add = set(ssup) <= (set(range(6)) - pd)
    mixed = 0 < len(pd) < 6
    if mixed and len(rows_add) == 1:
        one_row += 1
    if mixed and len(rows_add) == 2:
        two_rows += 1
    if len(rows_add) == 3:
        all_rows += 1; cubic_ok &= len(pd) == 6
    if S_add:
        s_add += 1; cubic_ok &= len(pd) == 0
cubic = [(1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1)]
cub = []
for bits in cubic:
    pd = {t for t in range(6) if bits[t]}
    cub.append((bits, [j for j in range(3) if set(gsup[j]) <= pd], set(ssup) <= (set(range(6)) - pd)))
cub_ok = [b for (b, g_, s_) in cub if g_ or s_] == [(1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0)]
okB = gsup == [[0, 3, 5], [1, 3, 4], [2, 4, 5]] and ssup == list(range(6)) and no_zero_col and one_row == 15 and two_rows == 3 and all_rows == 1 and s_add == 1 and cubic_ok and cub_ok
check("B: supports derived from the landed stencils (4^3 torus): momentum rows touch {jj, ij, jk}, the scalar row all six, and every slot is touched by both rules (no zero column, so any generating set has the same support); over all 64 slot-type assignments the full momentum rule is additive only in the all-momentum assignment and the scalar rule only in the all-metric one; 15 mixed assignments keep one momentum row additive, 3 keep two, none all three; among cubic-symmetric assignments only the pure ones keep any additive row; the same holds for arbitrary per-slot assignments",
      okB, f"momentum-row supports {gsup}, scalar-row support {ssup}; no zero column in G or S: {no_zero_col}; mixed with one additive row {one_row}, with two {two_rows}; all three rows additive in {all_rows} assignment(s), scalar additive in {s_add}; cubic-symmetric with any additive row: {[(b, g_, s_) for (b, g_, s_) in cub if g_ or s_]}")

print("N5 resolution 1: on discrete-spectrum slots an exact additive (Weyl-form) Gauss law needs its variable stored on every slot it touches.")
print("N5 resolution 2: the full momentum rule is an exact additive law only in the all-momentum assignment and the scalar rule only in the all-metric one; 15 mixed assignments keep one momentum row, 3 keep two, none all three; cubic-symmetric mixed assignments keep none.")
print("per_element: the trace of random commutators on spin slots.")
print("per_site: the row supports at a site of the 4^3 torus; every column of G and S checked nonzero.")
print("per_mode: checked and not executed - no dispersion is computed here.")
print("per_block: all 64 slot-type assignments and the four cubic-symmetric ones.")
print("lattice_wide: checked and not executed - the orders of the 18 partially additive mixed models; non-additive realisations; any state or phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
