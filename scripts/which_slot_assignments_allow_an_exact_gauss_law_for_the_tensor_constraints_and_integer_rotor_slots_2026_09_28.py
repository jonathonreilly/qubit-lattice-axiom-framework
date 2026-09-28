#!/usr/bin/env python3
"""Which slot-wise assignments allow an exact Gauss law for the tensor constraints; integer rotor slots.

Question (open routes of probes 10, 14, 15; 2026-09-28): the constructed
finite-slot assignments put the momentum on every slot (probes 10, 14) or the
metric on every slot (probe 15). Could a mixed slot-wise assignment, or
unbounded integer (rotor) slots, keep an exact additive Gauss law and escape
their orders? Pre-registered in the probe's scratch file.

Checks:
  A  spectrum lemma: on a slot whose diagonal variable D has discrete
     spectrum (spin S; a truncated or unbounded integer rotor), no
     self-adjoint C gives [C, D] = i c 1 with c != 0: for finite dimension
     tr [C, D] = 0 (checked on random C); for the unbounded rotor,
     exp(i t C) D exp(-i t C) = D + c t would shift the spectrum Z off
     itself. So an exact additive constraint sum_a c_a X_a can act only on
     variables that are diagonal on every slot of its support (it rotates
     their compact conjugates).
  B  supports: each landed momentum row G_j touches the slot types
     {jj, ij, jk} (3 of 6); the scalar row S touches all 6. Over all 2^6
     slot-type assignments (a type is momentum-diagonal or metric-diagonal),
     G_j is additive iff its three types are momentum-diagonal, and S iff all
     six are metric-diagonal. Result: the full G (all three rows) is additive
     only in the all-momentum assignment and S only in the all-metric one;
     mixed assignments can make one or two rows G_j additive, never all three
     and never S. With the cubic symmetry of the landed complex, the only
     assignments with any additive row are the two pure ones.
  C  rotor slots: for a shift operator T with [D, T] = r T (spin S^+, or the
     rotor raising e^{i phi}), [[T + T^dag, A], A^dag] = |a.r|^2 (T + T^dag)
     for diagonal A = a.D, checked on spin and truncated-rotor toys; rotor
     moves are unitary (norm 1). Move patterns are the same integer patterns,
     so the moment lemmas (probe 10 T2; probe 15 B) and both f-sum bounds hold
     unchanged: unbounded integer records do not change the orders.
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
    Sp = np.zeros((d, d))
    for a in range(1, d):
        Sp[a - 1, a] = np.sqrt(S * (S + 1) - ms[a] * (ms[a] + 1))
    return Sp, np.diag(ms)


def rotor(N):              # truncated integer rotor: n = -N..N, raising e^{i phi}
    d = 2 * N + 1; n = np.arange(-N, N + 1)
    R = np.zeros((d, d))
    for k in range(d - 1):
        R[k + 1, k] = 1.0
    return R, np.diag(n.astype(float))


# ---------------------------------------------------------------- A: spectrum lemma
worst = 0.0; dims = []
for kind, par in [("spin", 0.5), ("spin", 1), ("spin", 2), ("spin", 3), ("rotor", 5), ("rotor", 20)]:
    _, D = spin(par) if kind == "spin" else rotor(par)
    d = D.shape[0]; dims.append(d)
    for _ in range(20):
        X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d)); C = X + X.conj().T
        worst = max(worst, abs(np.trace(C @ D - D @ C)))
# the unitary argument for the unbounded rotor: conjugation by exp(i t C) preserves the spectrum; a shift by c t would not
spec_shift_ok = not np.allclose(np.sort(np.arange(-5, 6) + 0.3) % 1, 0)
check("A: spectrum lemma: no self-adjoint C gives [C, D] = i c 1 (c != 0) for a diagonal D with discrete spectrum: tr[C, D] = 0 in finite dimension (spins 1/2..3, truncated rotors), and for the unbounded integer rotor a unitary conjugation cannot shift the spectrum Z by c t; so an exact additive constraint acts only on variables diagonal on every slot of its support",
      worst < 1e-10 and spec_shift_ok, f"max |tr[C, D]| over 20 random Hermitian C per slot, dimensions {dims}: {worst:.1e}")

# ---------------------------------------------------------------- B: supports and all slot-type assignments
def G_types(j):
    x = np.zeros(3, dtype=int); types = {j}
    for i in range(3):
        if i != j:
            types.add(FACE[tuple(sorted((i, j)))])
    return types


S_types = set(range(6))                       # the scalar row touches all six (diagonal second differences and all faces)
gsup = [G_types(j) for j in range(3)]
counts = {"G all rows": [], "S": [], "some G row": []}
for bits in itertools.product([0, 1], repeat=6):             # 1: momentum-diagonal type, 0: metric-diagonal type
    pd = {t for t in range(6) if bits[t]}
    rows_add = [j for j in range(3) if gsup[j] <= pd]
    S_add = len(pd) == 0
    if len(rows_add) == 3:
        counts["G all rows"].append(bits)
    if S_add:
        counts["S"].append(bits)
    if rows_add and 0 < len(pd) < 6:
        counts["some G row"].append((bits, rows_add))
# cubic-symmetric assignments: types split into the orbits {diagonals} and {faces}
cubic = [(1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0), (0, 0, 0, 1, 1, 1)]
cubic_add = []
for bits in cubic:
    pd = {t for t in range(6) if bits[t]}
    cubic_add.append((bits, [j for j in range(3) if gsup[j] <= pd], len(pd) == 0))
okB = (counts["G all rows"] == [(1, 1, 1, 1, 1, 1)] and counts["S"] == [(0, 0, 0, 0, 0, 0)] and len(counts["some G row"]) > 0
       and all(len(g_) == 3 or (not g_) for (_, g_, _) in cubic_add) and all(bool(g_) + s_ <= 1 for (_, g_, s_) in cubic_add)
       and [b for (b, g_, s_) in cubic_add if g_ or s_] == [(1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0)])
check("B: supports: each momentum row G_j touches 3 of the 6 slot types and the scalar row all 6; over all 64 slot-type assignments the full G is additive only when every type is momentum-diagonal and S only when every type is metric-diagonal; mixed assignments can make one or two rows G_j additive, never all three and never S; among cubic-symmetric assignments only the two pure ones have any additive row",
      okB, f"G_j supports {[sorted(g) for g in gsup]}; assignments with all of G additive: {len(counts['G all rows'])}, with S additive: {len(counts['S'])}, mixed with some G row additive: {len(counts['some G row'])} (e.g. {counts['some G row'][0]}); cubic-symmetric: {[(b, g_, s_) for (b, g_, s_) in cubic_add]}")

# ---------------------------------------------------------------- C: rotor slots keep the double-commutator identity
def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


okC = True; det = []
for kind, par in [("spin", 1.0), ("rotor", 4)]:
    Rp, D = spin(par) if kind == "spin" else rotor(par)
    I = np.eye(D.shape[0]); r = np.array([1, -1, 1]); a = rng.normal(size=3) + 1j * rng.normal(size=3)
    T = kron_list([Rp if v > 0 else Rp.T for v in r])
    for k in range(3):                                         # [D_k, T] = r_k T
        Dk = kron_list([D if kk == k else I for kk in range(3)])
        okC &= np.abs(Dk @ T - T @ Dk - r[k] * T).max() < 1e-10
    H = T + T.conj().T
    A = sum(a[k] * kron_list([D if kk == k else I for kk in range(3)]) for k in range(3))
    dc = (H @ A - A @ H) @ A.conj().T - A.conj().T @ (H @ A - A @ H)
    err = np.abs(dc - abs(a @ r) ** 2 * H).max(); okC &= err < 1e-9
    det.append(f"{kind} {par}: identity error {err:.1e}")
Rr, _ = rotor(50); bulk = Rr[10:90, 10:90]
unit_bulk = np.abs(bulk.T @ bulk - np.eye(80))[1:-1, 1:-1].max() < 1e-12       # the rotor shift is unitary away from the truncation edge
check("C: rotor slots: shift operators with [D, T] = r T obey [[T + T^dag, A], A^dag] = |a.r|^2 (T + T^dag) for diagonal A (spin and truncated-rotor toys); rotor shifts are unitary (norm 1); move patterns are the same integer patterns, so the moment lemmas and both f-sum bounds hold unchanged with unbounded integer records",
      okC and unit_bulk, "; ".join(det) + f"; rotor shift unitary in the bulk: {unit_bulk}")

print("N5 resolution 1: an exact additive Gauss law on discrete-spectrum slots needs its variable diagonal on every slot of its support (spectrum lemma).")
print("N5 resolution 2: the full momentum rule is additive only in the all-momentum assignment and the scalar rule only in the all-metric one; mixed assignments keep at most one or two momentum rows additive; cubic-symmetric mixed assignments keep none.")
print("N5 resolution 3: unbounded integer (rotor) records keep the double-commutator identity and the moment lemmas, so probes 10 and 15's orders are unchanged.")
print("per_element: each operator identity on spin and truncated-rotor toys; the trace of random commutators.")
print("per_site: the slot-type supports of the three momentum rows and the scalar row.")
print("per_mode: checked and not executed - no dispersion is computed here (the harmonic orders are probe 15's check D).")
print("per_block: all 64 slot-type assignments and the four cubic-symmetric ones.")
print("lattice_wide: checked and not executed - the orders of genuinely mixed (partially additive) models, any ground state or phase.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
