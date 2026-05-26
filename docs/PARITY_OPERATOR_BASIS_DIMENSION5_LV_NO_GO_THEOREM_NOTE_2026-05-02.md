# Parity-Operator Basis: Formal Dimension-5 P-Weight Identities

**Date:** 2026-05-02; formal-scope repair 2026-05-26
**Runner:** `scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py`
**Claim type:** bounded_theorem
**Status:** formal Dirac-algebra and derivative-sign bounded theorem only;
no lattice-action coefficient no-go is claimed.

## Scope

The prior version mixed two different statements:

1. an exact formal statement about Dirac parity weights combined with the
   standard derivative-side sign character; and
2. a stronger lattice-action statement that the combined staggered parity
   `P = P_inv * epsilon` acts on the actual lattice derivative
   representatives with no extra sign bridge needed.

The audit correctly found that (2) was not derived by the packet. This repair
takes the auditor's narrowing option. The binding claim is now only (1):
formal P-weight identities for the listed dimension-5 SME-style operator
basis, independent of any lattice derivative-action bridge.

No new axiom, lattice-current selector, or audit verdict is introduced.

## Formal Setting

Use the chiral-basis Dirac algebra with `P_Dirac = gamma^0`:

```text
gamma^0 -> + gamma^0
gamma^i -> - gamma^i
gamma_5 -> - gamma_5
sigma^{ij} -> + sigma^{ij}
sigma^{0i} -> - sigma^{0i}
```

Use the formal derivative-side sign convention:

```text
partial_0 -> + partial_0
partial_i -> - partial_i.
```

Define the total spatial-index count `N` as:

- one for each spatial `gamma^i`;
- three for `gamma_5`;
- the number of spatial indices in `sigma^{mu nu}`; and
- one for each spatial derivative `partial_i`.

This note does not claim that the formal derivative-side sign convention has
been derived from the full staggered lattice derivative representatives under
`P_inv * epsilon`.

## Binding Theorem

For the four formal dimension-5 single-flavor fermion-bilinear structures

```text
gamma^mu partial_nu partial_rho
partial_mu partial_nu
gamma_5 gamma^mu partial_nu
sigma^{mu nu} partial_rho
```

with at least one spatial occurrence:

- if the total spatial-index count `N` is odd, the formal P-weight is `-1`
  and the P-symmetric projection `(O + P O P^{-1}) / 2` vanishes;
- if `N` is even, the formal P-weight is `+1` and the P-antisymmetric
  projection `(O - P O P^{-1}) / 2` vanishes.

The theorem covers the formal operator basis and sign convention only. It is
not a retained Lorentz-violation action no-go and does not eliminate lattice
operators whose derivative representatives require additional staggered
parity analysis.

## Diagnostic Lattice Check

The runner also checks the free staggered hopping identity
`epsilon H_0 epsilon = -H_0` on even periodic lattices `L = 4, 6, 8`. In
this repaired row that check is diagnostic support for the historical
staggered context. It is not used to derive the formal derivative-side sign
character for the dimension-5 lattice derivative representatives.

## What This Note Does Not Claim

- It does not derive how `P_inv * epsilon` conjugates every actual lattice
  derivative representative in the dimension-5 basis.
- It does not claim an action-level Lorentz-violation no-go.
- It does not claim that epsilon contributes no extra sign in all derivative
  factors.
- It does not add any axiom or convention.
- It does not apply an audit verdict.

## Runner Certificate

The companion runner exhaustively enumerates all allowed index assignments
in the four structures, checks the formal P-weight, and checks the matching
P-symmetric/P-antisymmetric projection identity. It also reports the
diagnostic staggered `H_0` anticommutation check described above.

Expected local certificate:

```text
PASS=237  FAIL=0
```

## Reopen Conditions

Reopen the stronger lattice-action no-go only with a retained bridge theorem
or runner that directly constructs the dimension-5 lattice derivative
representatives and verifies their conjugation under `P_inv * epsilon`.
Until then, this row is a formal bounded theorem about parity signs, not an
action-level SME/LV exclusion theorem.
