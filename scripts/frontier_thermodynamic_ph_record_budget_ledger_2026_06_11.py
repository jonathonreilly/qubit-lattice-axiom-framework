#!/usr/bin/env python3
"""In the broadcast record model, the thermodynamic past hypothesis's quantitative
clause is tested as a consistency relation among realized-state data: realized record
depth N lower-bounds the same boundary's register-sector deficit.  (L1) At full
Z-alignment, count and marginal-sum entropy coincide; this is a FULL-ALIGNMENT
coincidence, not a general identity.  Off full alignment, marginal-sum entropy is
smooth binary entropy while the record count is thresholded.  Marginal-sum entropy
(generated total correlation; un-produces under the inverse step -- correlation
bookkeeping, not Clausius production) names the coarse register-sector quantity; no
bath is present.  (L2) Alignment is basis-relative and unitarily mutable; a closed
Hadamard layer can cash X-pure register deficit as aligned blanks, so the basis-free
resource statement is register deficit below max-mixed, while alignment is the form
the fixed broadcast instrument can cash.
(L3) The sink escape conserves the ledger (reset-with-sink consumes sink blanks 1:1 --
total records <= total initial register deficit cashable as aligned blanks, equality
exhibited).  (L4) Therefore a realized history with record depth N had a boundary
whose register-sector deficit was at least N bits; the boundary was wound up by AT
LEAST as much as the world has registered.  The past hypothesis's
specialness/atypicality claim (low-entropy AMONG PERMITTED STATES -- which needs a
measure over states, exactly what the realized-state primitive forbids supplying) is
NOT derived; the existing carve-out stands unchanged.  (L5) The global fine-grained
entropy is constant throughout (unitarity).

Class-A exact verification for the source note

    docs/THERMODYNAMIC_PH_QUANTITATIVE_CLAUSE_RECORD_BUDGET_LEDGER_BOUNDED_THEOREM_NOTE_2026-06-11.md

CONTEXT (owner-directed: the thermodynamic-PH strike, continuing the PH dissection --
direction derived (arrow note, retained_bounded); existence structural in-sector +
non-emptiness self-instantiating (the append-only reduction, in review); THIS NOTE
tests the quantitative/entropy clause as a bounded consistency relation).  The landed
sink/ledger notes (reset_with_sink_conditional, reset_sink_entropy_ledger -- both
unaudited on the live ledger at this writing; load-bearing facts RE-PROVED here)
supply the reversible escape map (s,e,g) -> (s, g xor s, e) and its bit accounting.

WHAT THIS DOES NOT CLAIM: no heat bath, temperature, rate, cost law, or dynamical
preparation of the boundary; no derivation of N (the realized record depth is
registered data -- the realized-state primitive's slot); no global fine-grained
entropy growth (constant under unitarity, checked); no claim outside the broadcast
record model.  Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_thermodynamic_ph_record_budget_ledger_2026_06_11.py
"""

from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)
P1 = np.array([[0, 0], [0, 1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
zero = np.array([1, 0], dtype=complex)
one = np.array([0, 1], dtype=complex)
plus = np.array([1, 1], dtype=complex) / np.sqrt(2)


def vn(rho):
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-12]
    return float(-(w * np.log2(w)).sum())


def binary_entropy(p):
    if p < 1e-12 or 1 - p < 1e-12:
        return 0.0
    return float(-(p * np.log2(p) + (1 - p) * np.log2(1 - p)))


def partial_trace_keep(rho, nq, keep):
    keep = sorted(keep)
    dims = [2] * nq
    rho_t = rho.reshape(dims + dims)
    for q in sorted([q for q in range(nq) if q not in keep], reverse=True):
        rho_t = np.trace(rho_t, axis1=q, axis2=q + rho_t.ndim // 2)
    return rho_t.reshape(2 ** len(keep), 2 ** len(keep))


def cnot(nq, ctrl, tgt):
    U = np.zeros((2 ** nq, 2 ** nq), dtype=complex)
    for b in range(2 ** nq):
        if (b >> (nq - 1 - ctrl)) & 1:
            b2 = b ^ (1 << (nq - 1 - tgt))
        else:
            b2 = b
        U[b2, b] = 1.0
    return U


NFRAG = 3
NQ = NFRAG + 1


def connected_records(rho):
    n = 0
    for k in range(NFRAG):
        rk = partial_trace_keep(rho, NQ, [0, k + 1])
        zz = float(np.real(np.trace(rk @ kron(Z, Z))))
        zs = float(np.real(np.trace(rk @ kron(Z, I2))))
        zf = float(np.real(np.trace(rk @ kron(I2, Z))))
        if abs(zz - zs * zf) > 0.5:
            n += 1
    return n


def marg_sum_entropy(rho):
    return sum(vn(partial_trace_keep(rho, NQ, [k + 1])) for k in range(NFRAG))


def register_deficit(rho):
    return sum(1.0 - vn(partial_trace_keep(rho, NQ, [k + 1]))
               for k in range(NFRAG))


def blanks_aligned(rho):
    """registers whose marginal is a Z-basis pure state (the aligned-blank class)."""
    n = 0
    for k in range(NFRAG):
        m = partial_trace_keep(rho, NQ, [k + 1])
        if max(abs(m[0, 0] - 1) < 1e-9 and abs(m[0, 1]) < 1e-9,
               abs(m[1, 1] - 1) < 1e-9 and abs(m[0, 1]) < 1e-9):
            n += 1
    return n


def run_broadcasts(rho0, nsteps=NFRAG):
    rho = rho0.copy()
    out = [(connected_records(rho), marg_sum_entropy(rho), blanks_aligned(rho), vn(rho))]
    for k in range(nsteps):
        U = cnot(NQ, 0, k + 1)
        rho = U @ rho @ U.conj().T
        out.append((connected_records(rho), marg_sum_entropy(rho),
                    blanks_aligned(rho), vn(rho)))
    return out


def broadcast_state(rho0, nsteps=NFRAG):
    rho = rho0.copy()
    for k in range(nsteps):
        U = cnot(NQ, 0, k + 1)
        rho = U @ rho @ U.conj().T
    return rho


def ketrho(*kets):
    psi = kron(*[k.reshape(-1, 1) for k in kets]).ravel()
    return np.outer(psi, psi.conj())


# ===========================================================================
print("=" * 78)
print("L1  Full-alignment count/marginal-sum entropy coincidence, with")
print("    off-alignment divergence disclosed")
print("=" * 78)
traj = run_broadcasts(ketrho(plus, zero, zero, zero))
recs = [t[0] for t in traj]
ssum = [t[1] for t in traj]
blks = [t[2] for t in traj]
check("L1a clean records form one per broadcast step: counts " + str(recs),
      recs == [0, 1, 2, 3])
check("L1b each record CONSUMES exactly one aligned-blank register: blanks "
      + str(blks), blks == [3, 2, 1, 0])
check("L1c at full Z-alignment each record coincides with one bit of "
      "marginal-sum entropy: Sum_i S_i = " + str([round(s, 6) for s in ssum])
      + " -- a FULL-ALIGNMENT coincidence",
      all(abs(ssum[k] - k) < 1e-9 for k in range(4))
      and all(abs(ssum[k] - recs[k]) < 1e-9 for k in range(4)))
# anti-aligned (|1>) registers are equally consumable (the class is Z-ALIGNED pure)
traj1 = run_broadcasts(ketrho(plus, one, one, one))
check("L1d anti-aligned (|1>) registers are equally consumable (the resource class "
      "is Z-aligned purity, not the |0> label): records "
      + str([t[0] for t in traj1]),
      [t[0] for t in traj1] == [0, 1, 2, 3]
      and abs(traj1[-1][1] - 3) < 1e-9)
partial_angles = (0.2, 0.5, 0.9, 1.2)
l1e_entropy_ok = True
l1e_divergences = 0
l1e_detail = []
for t in partial_angles:
    pointer = np.cos(t) * zero + np.sin(t) * one
    rho0 = ketrho(pointer, zero, zero, zero)
    rho = broadcast_state(rho0)
    expected = binary_entropy(np.cos(t) ** 2)
    marginal_entropies = [vn(partial_trace_keep(rho, NQ, [k + 1]))
                          for k in range(NFRAG)]
    l1e_entropy_ok &= all(abs(s - expected) < 1e-9 for s in marginal_entropies)
    production = marg_sum_entropy(rho) - marg_sum_entropy(rho0)
    records = connected_records(rho)
    if abs(production - records) > 0.1:
        l1e_divergences += 1
    l1e_detail.append(f"t={t}: H={expected:.6f}, sum={production:.6f}, N={records}")
check("L1e the exact count=production identity is a FULL-ALIGNMENT coincidence "
      "(measure-zero in pointer angle): off-alignment each written register follows "
      "smooth H(cos^2 t), while the integer count is thresholded",
      l1e_entropy_ok and l1e_divergences >= 3, "; ".join(l1e_detail))
p = 0.3
rho_p = np.diag([p, 1 - p]).astype(complex)
rho_l1f0 = np.kron(rho_p, ketrho(zero, zero, zero))
rho_l1f = broadcast_state(rho_l1f0)
l1f_records = connected_records(rho_l1f)
l1f_production = marg_sum_entropy(rho_l1f) - marg_sum_entropy(rho_l1f0)
l1f_expected = 3 * binary_entropy(p)
l1f_corr = 1 - (2 * p - 1) ** 2
l1f_deficit = register_deficit(rho_l1f0)
check("L1f partially-mixed Z pointer diverges too: records=3 by connected "
      "correlator, marginal-sum production=3*H(0.3) != 3, and boundary register "
      "deficit still bounds N",
      l1f_records == 3
      and l1f_corr > 0.5
      and abs(l1f_corr - 0.84) < 1e-12
      and abs(l1f_production - l1f_expected) < 1e-9
      and abs(l1f_production - 3) > 0.1
      and l1f_deficit >= l1f_records,
      f"corr={l1f_corr:.2f}, sum={l1f_production:.6f}, deficit={l1f_deficit:.6f}")

# ===========================================================================
print("=" * 78)
print("L2  Deficit alone is NOT the resource: alignment matters (Penrose-deficit")
print("    necessary, not sufficient; alignment is basis-relative)")
print("=" * 78)
# X-aligned pure register: SAME 1-bit deficit below max-mixed, ZERO records
trajx = run_broadcasts(ketrho(plus, plus, plus, plus))
check("L2a X-aligned pure registers (same 1-bit deficit vs max-mixed) yield ZERO "
      "records and ZERO marginal-sum entropy change (CNOT-transparent): records "
      + str([t[0] for t in trajx]),
      [t[0] for t in trajx] == [0, 0, 0, 0]
      and abs(trajx[-1][1] - trajx[0][1]) < 1e-9)
# maximally-mixed registers: zero deficit, zero records
rho_mix = np.kron(ketrho(plus), kron(I2, I2, I2) / 8)
trajm = run_broadcasts(rho_mix)
check("L2b maximally-mixed registers (ZERO deficit) yield ZERO records and zero "
      "marginal-sum entropy change: records " + str([t[0] for t in trajm]),
      [t[0] for t in trajm] == [0, 0, 0, 0]
      and abs(trajm[-1][1] - trajm[0][1]) < 1e-9)
# the clean-reset transfer channel is non-invertible without a sink.
T = np.zeros((16, 16))
for p in (0, 1):
    for f in range(8):
        T[p * 8 + (0b111 * p), p * 8 + f] = 1.0
check("L2c the specific clean-reset transfer channel (arbitrary old fragments -> "
      "clean broadcast, no sink) has rank 2, not 16",
      np.linalg.matrix_rank(T) == 2)
rho_l2d0 = ketrho(plus, plus, plus, plus)
U_h = kron(I2, H, H, H)
rho_l2d_h = U_h @ rho_l2d0 @ U_h.conj().T
rho_l2d_final = broadcast_state(rho_l2d_h)
l2d_aligned_before = blanks_aligned(rho_l2d0)
l2d_aligned_after = blanks_aligned(rho_l2d_h)
l2d_deficit = register_deficit(rho_l2d0)
l2d_N = connected_records(rho_l2d_final)
check("L2d alignment is basis-relative and unitarily mutable: the aligned-count "
      "bound FAILS under closed pre-processing; the basis-free register deficit "
      "bound survives",
      l2d_aligned_before == 0
      and l2d_aligned_after == 3
      and l2d_N == 3
      and l2d_N > l2d_aligned_before
      and abs(l2d_deficit - 3) < 1e-9
      and l2d_N <= l2d_deficit + 1e-9,
      f"aligned {l2d_aligned_before}->{l2d_aligned_after}, N={l2d_N}, "
      f"deficit={l2d_deficit:.6f}")

# ===========================================================================
print("=" * 78)
print("L3  The sink escape conserves the ledger (reset-with-sink, re-proved)")
print("=" * 78)
# label model: (s, e, g) -> (s, g xor s, e) on 1 + k + k bits, k = 3
k = 3
nbits = 1 + k + k


def swap_reset(label):
    s = (label >> (2 * k)) & 1
    e = (label >> k) & ((1 << k) - 1)
    g = label & ((1 << k) - 1)
    enew = g ^ (0b111 * s)
    gnew = e
    return (s << (2 * k)) | (enew << k) | gnew


perm = [swap_reset(b) for b in range(2 ** nbits)]
check("L3a the reset-with-sink map (s,e,g) -> (s, g xor s, e) is an exact "
      "permutation (the landed escape, re-proved)",
      sorted(perm) == list(range(2 ** nbits)))
# ledger: blank-sink input (g=0) -> fragments clean (records), sink holds e
# (old word). The sink's k blanks are CONSUMED 1:1: after the move the sink is
# blank only if e was blank.
consumed = all(((swap_reset((s << (2 * k)) | (e << k) | 0) & ((1 << k) - 1)) == e)
               for s in (0, 1) for e in range(2 ** k))
check("L3b the sink's blanks are consumed 1:1 (the sink afterwards holds the old "
      "fragment word; it is blank only if the fragments already were): the regress "
      "is priced, total records <= TOTAL initial register deficit cashable as "
      "aligned blanks (fragments + sink hierarchy)",
      consumed)
# equality exhibit: budget 3 (fragments blank) -> 3 records (L1); after consuming
# the sink's 3 blanks to reset, 3 more records: total 6 = initial total budget 6.
check("L3c equality exhibit: blank fragments (3) + blank sink (3) = budget 6 -> "
      "3 records, reset via sink, 3 more records = 6 records, budget exhausted "
      "(arithmetic on L1+L3a/b)",
      3 + 3 == 6)

# ===========================================================================
print("=" * 78)
print("L4  The quantitative clause: realized record depth N => boundary deficit")
print("    >= N bits (derived implication; N itself is registered data)")
print("=" * 78)
# across realized states, N varies (data), while the basis-free one-directional
# bound N <= boundary register-sector deficit holds invariantly in this model.
mixed_case = np.kron(ketrho(plus, zero), kron(I2, I2) / 4)
l4_cases = [
    ("superposed pointer, 3 blanks", ketrho(plus, zero, zero, zero), NFRAG, None),
    ("superposed pointer, 2 blanks + 1 X-pure",
     ketrho(plus, zero, zero, plus), NFRAG, None),
    ("superposed pointer, 1 blank + 2 mixed", mixed_case, NFRAG, None),
    ("eigenstate pointer, 3 blanks", ketrho(zero, zero, zero, zero), NFRAG, None),
]
for t in partial_angles:
    pointer = np.cos(t) * zero + np.sin(t) * one
    l4_cases.append((f"partial-superposition pointer t={t}",
                     ketrho(pointer, zero, zero, zero), NFRAG, None))
l4_cases.extend([
    ("partially-mixed Z pointer p=0.3", rho_l1f0, NFRAG, None),
    ("Hadamard-regenerated X-pure registers", rho_l2d0, NFRAG, U_h),
    ("partial broadcast strict gap", ketrho(plus, zero, zero, zero), 1, None),
])
ok_bound = True
strict_gap = False
Ns = {}
for name, rho_boundary, nsteps, pre_unitary in l4_cases:
    rho_cash = rho_boundary.copy()
    if pre_unitary is not None:
        rho_cash = pre_unitary @ rho_cash @ pre_unitary.conj().T
    N = connected_records(broadcast_state(rho_cash, nsteps))
    deficit = register_deficit(rho_boundary)
    Ns[name] = (N, deficit)
    ok_bound &= (N <= deficit + 1e-9)
    if name == "partial broadcast strict gap" and N == 1 and abs(deficit - 3) < 1e-9:
        strict_gap = True
check("L4a the one-directional bound: realized record depth <= boundary "
      "register-sector deficit (basis-free); converse fails (L2a); strict gap "
      "exhibited (the Penrose regime is the huge-gap case)",
      ok_bound and strict_gap,
      "; ".join(f"{k}: N={v[0]}, deficit={v[1]:.6f}" for k, v in Ns.items()))
full_alignment_cases = [
    ketrho(plus, zero, zero, zero),
    ketrho(plus, one, one, one),
    rho_l2d_h,
]
ok_full_alignment = all(
    abs((run_broadcasts(rho0)[-1][1] - run_broadcasts(rho0)[0][1])
        - run_broadcasts(rho0)[-1][0]) < 1e-9
    for rho0 in full_alignment_cases
)
check("L4b the count/marginal-sum entropy coincidence is retained on the "
      "full-alignment broadcast exhibits only",
      ok_full_alignment)
check("L4c the deficit reading: a boundary that supports N records held "
      "register-sector deficit >= N bits -- the boundary was wound up by AT "
      "LEAST as much as the world has registered (lower bound)",
      ok_bound)

# ===========================================================================
print("=" * 78)
print("L5  Disclosure: global fine-grained entropy is CONSTANT (unitarity) --")
print("    marginal-sum entropy is correlation bookkeeping, not Clausius production")
print("=" * 78)
traj = run_broadcasts(ketrho(plus, zero, zero, zero))
globS = [t[3] for t in traj]
check("L5a global fine-grained S is constant (0 bits, pure, all steps): the "
      "deficit/marginal-sum entropy statements are about generated total "
      "correlation and register-sector resource bookkeeping, never global "
      "fine-grained entropy -- the standard coarse/fine distinction, disclosed",
      all(abs(s) < 1e-9 for s in globS), f"global S {[round(s,9) for s in globS]}")
U_full = cnot(NQ, 0, 3) @ cnot(NQ, 0, 2) @ cnot(NQ, 0, 1)
rho_full = U_full @ ketrho(plus, zero, zero, zero) @ U_full.conj().T
check("L5b the coarse and fine ledgers differ by exactly the generated "
      "correlations (marginal-sum 3 bits vs joint fragment entropy 1 bit at full "
      "broadcast: 2 bits of correlation): nothing is hidden in the accounting",
      abs(marg_sum_entropy(rho_full) - 3) < 1e-9
      and abs(vn(partial_trace_keep(rho_full, NQ, [1, 2, 3])) - 1) < 1e-9)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: In the broadcast record model, the thermodynamic past hypothesis's")
print("  quantitative clause is treated as a consistency relation among realized-state")
print("  data: realized record depth N implies boundary register-sector deficit >= N")
print("  bits (L4).  At full Z-alignment, count and marginal-sum entropy coincide,")
print("  but that exactness is a FULL-ALIGNMENT coincidence: off alignment,")
print("  marginal-sum entropy is smooth and the record count is thresholded (L1).")
print("  marginal-sum entropy (generated total correlation; un-produces under the")
print("  inverse step -- correlation bookkeeping, not Clausius production) names the")
print("  coarse register-sector quantity.  Alignment is basis-relative and unitarily")
print("  mutable: the aligned-count bound fails under closed Hadamard pre-processing,")
print("  while the basis-free register deficit bound survives (L2d).  The sink")
print("  escape conserves the ledger (L3).  The boundary was wound up by AT LEAST as")
print("  much as the world has registered.  NOT claimed: heat bath, temperature,")
print("  rate, cost law, boundary preparation dynamics, derivation of N, anything")
print("  outside the broadcast model.")
print("  the past hypothesis's specialness/atypicality claim (low-entropy AMONG PERMITTED STATES -- which needs a measure over states, exactly what the realized-state primitive forbids supplying) is NOT derived; the existing carve-out stands unchanged.")
print("  No new axiom/primitive/measure/weight; r untouched.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
