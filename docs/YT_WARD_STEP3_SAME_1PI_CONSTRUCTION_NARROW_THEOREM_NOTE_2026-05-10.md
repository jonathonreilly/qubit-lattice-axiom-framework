---
claim_id: yt_ward_step3_same_1pi_construction_narrow_theorem_note_2026-05-10
claim_type_author_hint: bounded_theorem
runner_path: scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py
audit_authority: independent audit lane only
---

# YT_WARD Step 3 Conditional Coefficient Theorem

**Date:** 2026-05-10 (source-boundary repair 2026-07-18)
**Type:** bounded_theorem
**Claim scope:** exact coefficient bookkeeping after separately supplying a
physical-to-abstract H-MATRIX bridge, a REP-B-RESIDUE convention that turns a
form factor into a two-insertion coefficient, and SAME-1PI equality in the
fermion-only effective-action convention stated below. Without any one of
those bridges, the corresponding coefficient or equality remains symbolic.
**Status authority:** independent audit lane only.
**Primary runner:**
[`scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py`](../scripts/yt_ward_step3_same_1pi_construction_2026_05_10.py)

## Rep-A coefficient convention and input

Integrate out the gauge field at tree level and consider the resulting
connected amputated four-fermion kernel, equivalently the four-fermion vertex
of the fermion-only effective action. The one-gauge-boson graph is not 1PI in
the full gauge-plus-fermion theory; every use of "1PI" below is restricted to
this fermion-only effective-action convention.

In the direct/exchange color-tensor coordinate basis, the exact completeness
identity has direct-singlet coordinate `-1/(2N_c)`. This is a coordinate in a
nonorthogonal Fierz basis, not the Hilbert--Schmidt projection of the complete
color tensor onto `delta_ij delta_kl`. With the explicitly chosen
Fierz-reordered Dirac index pairing and scalar convention `c_S`, the
small-momentum continuum-kernel coefficient is supplied as

```text
C_A(g_bare) = c_S g_bare^2 / (2 N_c).
```

Here `q^2` denotes the continuum/small-lattice-momentum propagator
normalization. The exact Wilson-lattice kernel would instead contain lattice
momentum, gauge-projector, and vertex form factors and is not derived here.

The source context for the SU(`N_c`) completeness identity is
[`YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md),
while
[`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md) is only
nonabelian structural context and supplies no Wilson dynamics or OGE kernel.
The runner independently reconstructs the two color-tensor coordinates and
the scalar Clifford coordinate in one explicit gamma-matrix/index convention.
The physical sign choice `c_S=+1` remains separately supplied because the
cited Clifford input fixes only `|c_S|=1` across conventions.

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
F_RepB(g_bare) = 1 / sqrt(N_c N_iso).
```

The abstract theorem does not establish H-MATRIX for a physical `H_unit`.
The separate
[Rep-B conditional corollary](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
records the same boundary.

**REP-B-RESIDUE (supplied, not derived).** In the same fermion-only kernel
normalization, a separate construction proves the unit residue/source
normalization, equal left and right insertions, and kernel convention needed
for

```text
C_B(g_bare) = F_L(g_bare) F_R(g_bare),
F_L(g_bare) = F_R(g_bare) = F_RepB(g_bare).
```

Only under H-MATRIX and REP-B-RESIDUE together does
`C_B=1/(N_c N_iso)` follow. Hilbert--Schmidt normalization of `K` is not a
proof of this residue or two-insertion factorization.

**SAME-1PI (supplied, not derived).** The OGE contraction and the Rep-B
decomposition are supplied as two complete representations of the same
projected four-fermion vertex of the gauge-integrated fermion effective
action on the scalar-singlet channel. No Wick-, integration-, or
kernel-matching proof is supplied here. Equating their coefficients without
this hypothesis would assume the equality under review.

## Conditional coefficient chain

Under the Rep-A convention plus H-MATRIX and REP-B-RESIDUE, the two
conditional coefficient expressions are

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

Under H-MATRIX, REP-B-RESIDUE, and SAME-1PI, `(G)` then gives
`g_bare^2=1`. Without SAME-1PI, `g_bare=2` instead gives the explicit
nonzero residual `1/2`.

## Missing-premise branches

- **Without H-MATRIX**, write the physical Rep-B form factor as the
  unconstrained symbol `f(g_bare)`. Even if REP-B-RESIDUE is supplied,
  `C_B=f(g_bare)^2`, and the abstract theorem supplies no value or parameter
  independence for it.
- **Without REP-B-RESIDUE**, H-MATRIX fixes the form factor but leaves the
  actual Rep-B coefficient as an unconstrained symbol `r_B(g_bare)`.
- **Without SAME-1PI**, even with both preceding bridges, `(R)` is merely the
  computed difference of two proposed representations. It is not identically
  zero in `g_bare`.
- **Without the sign choice**, `|c_S|=1` does not select the positive branch
  used in the arithmetic specialization.

## What this theorem does not claim

- It does not derive H-MATRIX, REP-B-RESIDUE, SAME-1PI, or `c_S=+1`.
- It does not derive a physical `H_unit` normalization, a Wick-state
  identification, a free-field residue, a Ward normalization, a tree-level
  gauge-sector equality, `g_bare=1`, or a top-Yukawa observable.
- It does not assign physical meanings to `N_iso` and `N_c` from the abstract
  factorization of `n`.
- It introduces no new axiom, admission, primitive, carrier, physical input,
  or premise-registry entry.

## Downstream citation contract

Downstream use of `C_B=1/(N_c N_iso)` must name both H-MATRIX and
REP-B-RESIDUE as supplied. Downstream use of the gate equation `(G)` must
also name SAME-1PI as supplied. None may be cited as derived from this note
or from the abstract matrix theorem.

The unconditional reusable content is limited to the abstract color and
Clifford coordinate algebra and the displayed missing-premise boundaries.

## Declared dependencies

- [UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md](UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02.md)
  for the abstract matrix implication, conditional on H-MATRIX.
- [G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md](G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md)
  for the matching conditional physical-boundary statement.
- [YT_WARD_IDENTITY_DERIVATION_THEOREM.md](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  for the D12 color-singlet Fierz coefficient and `|c_S|=1` input.
- [NATIVE_GAUGE_CLOSURE_NOTE.md](NATIVE_GAUGE_CLOSURE_NOTE.md)
  as non-load-bearing nonabelian structural context only; it explicitly does
  not supply Wilson dynamics, coupling normalization, or the OGE kernel.

## Validation

The primary runner independently reconstructs the six-dimensional
centralizer constraints, applies positivity and Hilbert--Schmidt
normalization, verifies the SU(3) Fierz coordinates and one explicit
Clifford-scalar coordinate, derives `(R)` and `(G)` under all named
conditions, and recomputes the missing-H-MATRIX, missing-REP-B-RESIDUE, and
missing-SAME-1PI branches. Expected output is `PASS>0, FAIL=0`.
