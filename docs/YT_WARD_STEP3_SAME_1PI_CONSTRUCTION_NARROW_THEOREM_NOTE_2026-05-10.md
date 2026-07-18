---
claim_id: yt_ward_step3_same_1pi_construction_narrow_theorem_note_2026-05-10
claim_type_author_hint: bounded_theorem
runner_path: scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py
audit_authority: independent audit lane only
---

# YT_WARD Step 3 Doubly Conditional Coefficient Theorem

**Date:** 2026-05-10 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** exact coefficient bookkeeping under two separately supplied
local hypotheses: H-MATRIX supplies the physical-to-abstract matrix bridge
needed to obtain the Rep-B coefficient, and SAME-1PI supplies the equality of
the Rep-A and Rep-B projected 1PI representations. Without H-MATRIX the
Rep-B coefficient remains symbolic; without SAME-1PI the two coefficients
cannot be equated.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py`](../scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py)

## Independent coefficient input

On the separately specified projected channel, the D12 color-singlet Fierz
coefficient and scalar Clifford magnitude give the Rep-A coefficient

```text
C_A(g_bare) = c_S g_bare^2 / (2 N_c).
```

The source for the SU(`N_c`) coefficient is
[`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md),
and the bare-action context is
[`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md).
The sign `c_S=+1` is a separately supplied sign choice; the cited Clifford
input fixes only `|c_S|=1`.

## Local conditional hypotheses

The following are ordinary hypotheses of this bounded theorem. They are not
new framework axioms, admissions, premise-registry entries, or derived
physical facts.

**H-MATRIX (supplied, not derived).** For every parameter value under
discussion, a physical construction supplies a matrix `K(g_bare)` on a
fixed normalized `n=N_iso N_c` dimensional basis and establishes

```text
K(g_bare) >= 0,
[K(g_bare),E_jk] = 0 for every matrix unit E_jk,
Tr(K(g_bare)^dagger K(g_bare)) = 1,
F_RepB(g_bare) = <e_j,K(g_bare)e_j>.
```

The
[central-positive Hilbert--Schmidt unit theorem](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
then gives, conditionally,

```text
K(g_bare) = I_n / sqrt(n),
F_RepB(g_bare) = 1 / sqrt(N_c N_iso),
C_B = F_RepB(g_bare)^2 = 1 / (N_c N_iso).
```

The abstract theorem does not establish H-MATRIX for a physical `H_unit`.
The separate
[Rep-B conditional corollary](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
records the same boundary.

**SAME-1PI (supplied, not derived).** The OGE contraction and the Rep-B
decomposition are supplied as two complete representations of the same
projected amputated 1PI Green's function on the scalar-singlet four-fermion
channel. No Wick-level proof is supplied here. Equating their coefficients
without this hypothesis would assume the equality under review.

## Conditional coefficient chain

Under H-MATRIX alone, the two exact coefficient expressions are

```text
C_A(g_bare) = c_S g_bare^2 / (2 N_c),
C_B          = 1 / (N_c N_iso).
```

Their formal difference is

```text
C_A - C_B
  = (N_iso c_S g_bare^2 - 2) / (2 N_c N_iso).                    (R)
```

This difference is a diagnostic, not an asserted equality. Only under
SAME-1PI as well may one impose `C_A=C_B`, obtaining

```text
c_S g_bare^2 = 2 / N_iso.                                      (G)
```

At the separately supplied arithmetic specialization
`N_c=3`, `N_iso=2`, `c_S=+1`, `(R)` becomes

```text
(g_bare^2 - 1) / 6.
```

Under both H-MATRIX and SAME-1PI, `(G)` then gives `g_bare^2=1`. Without
SAME-1PI, `g_bare=2` instead gives the explicit nonzero residual `1/2`.

## Missing-premise branches

- **Without H-MATRIX**, write the physical Rep-B form factor as the
  unconstrained symbol `f(g_bare)`. Then `C_B=f(g_bare)^2`, and the abstract
  matrix theorem supplies no value or parameter independence for it.
- **Without SAME-1PI**, even with H-MATRIX, `(R)` is merely the computed
  difference of two proposed representations. It is not identically zero in
  `g_bare`.
- **Without the sign choice**, `|c_S|=1` does not select the positive branch
  used in the arithmetic specialization.

## What this theorem does not claim

- It does not derive H-MATRIX, SAME-1PI, or `c_S=+1`.
- It does not derive a physical `H_unit` normalization, a Wick-state
  identification, a free-field residue, a Ward normalization, a tree-level
  gauge-sector equality, `g_bare=1`, or a top-Yukawa observable.
- It does not assign physical meanings to `N_iso` and `N_c` from the abstract
  factorization of `n`.
- It introduces no new axiom, admission, primitive, carrier, physical input,
  or premise-registry entry.

## Downstream citation contract

Downstream use of `C_B=1/(N_c N_iso)` must name H-MATRIX as supplied.
Downstream use of the gate equation `(G)` must name both H-MATRIX and
SAME-1PI as supplied. Neither hypothesis may be cited as derived from this
note or from the abstract matrix theorem.

The unconditional reusable content is limited to the Rep-A coefficient
algebra, the displayed formal residual after explicitly assuming H-MATRIX,
and the two missing-premise boundaries.

## Declared dependencies

- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  for the abstract matrix implication, conditional on H-MATRIX.
- [G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
  for the matching conditional physical-boundary statement.
- [YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  for the D12 color-singlet Fierz coefficient and `|c_S|=1` input.
- [NATIVE_GAUGE_CLOSURE_NOTE.md](NATIVE_GAUGE_CLOSURE_NOTE.md)
  for the bare-action and OGE vertex context.

## Validation

The primary runner independently reconstructs the six-dimensional
centralizer constraints, applies positivity and Hilbert--Schmidt
normalization, verifies the SU(3) Fierz coefficient, derives `(R)` and `(G)`,
and recomputes both missing-premise branches. Expected output is
`PASS>0, FAIL=0`.
