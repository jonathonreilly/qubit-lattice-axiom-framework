# Hypercharge α = 1/3 Normalization Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/hypercharge_alpha_third_normalization_runner.py`](../scripts/hypercharge_alpha_third_normalization_runner.py)

## Claim

Given the retained graph-first 6+2 split of the left-handed doublet
sector and the traceless two-eigenvalue U(1) ansatz on that split,
together with the accepted-premise packet below, the normalization
scale of the one-parameter family
`Y_α = α (P_sym − 3 P_anti)` is uniquely fixed at

```text
α = +1/3   (doubled convention),
```

equivalently `Y(L_L) = -1`. The proof-walk uses only:

1. The retained 6-state Sym² and 2-state Anti² split from the
   graph-first SU(3) surface, plus tracelessness of the two-eigenvalue
   U(1) ansatz: `6α + 2β = 0`, hence `β = -3α`;
2. The explicitly accepted premise packet P1-P4 below.

The bridge consists of a one-line rational arithmetic identity. It
does not claim to derive the premise packet, and it does not promote
those premises to axioms.

This is a bounded proof-walk responding to the existing conditional
parent row's repair request for a narrow α-normalization bridge. The
parent `HYPERCHARGE_IDENTIFICATION_NOTE.md` is context, not a
load-bearing dependency for this proof. This note does not add a new
axiom or a new repo-wide theory class.

## Accepted-premise packet (not axioms)

The following entries are the complete non-framework premise packet for
this bounded bridge. They are accepted only for this row's conditional
normalization arithmetic; no new axiom is introduced.

- **P1 Anti^2-as-L_L readout convention.** On this bounded readout
  surface, the Anti² branch is named the left-handed lepton doublet
  branch, so `Y(L_L) = β`.
- **P2 Gell-Mann-Nishijima convention.** Electric charge and doubled
  hypercharge are related by `Q = T_3 + Y/2`.
- **P3 weak-isospin assignment.** The left-handed electron component has
  `T_3(e_L) = -1/2`.
- **P4 electron-charge unit convention.** The electron charge is the
  elementary charge unit, written `Q(e_L) = -1`.

This row proves: **if** the retained 6+2 traceless ratio is used with
P1-P4, **then** `α = 1/3`. It does not claim to derive P1, P2, P3, or
P4 from `Cl(3)` on `Z^3`.

## Proof-walk

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (B1) | 6+2 graph-first split and traceless two-eigenvalue ansatz give `6α + 2β = 0`, hence `β = -3α` | Retained graph-first split + algebra | no |
| (B2) | The Anti² branch is the `L_L` branch on this bounded readout surface, so `Y(L_L) = β = -3α` | P1 accepted readout convention | no |
| (B3) | `Q(e_L) = T_3(e_L) + Y(L_L)/2` | P2 accepted GMN convention | no |
| (B4) | `T_3(e_L) = -1/2` | P3 accepted weak-isospin assignment | no |
| (B5) | `Q(e_L) = -1` | P4 accepted electron-charge unit convention | no |
| (B6) | Substitute (B3)–(B5): `-1 = -1/2 + (-3α)/2` | Rational arithmetic | no |
| (B7) | Solve for α: `α = 1/3` | Rational arithmetic | no |

The bridge does not cite the Wilson plaquette action, staggered phases,
Brillouin-zone labels, link unitaries, lattice scale `u_0`, a Monte
Carlo measurement, or a fitted observational value.

## Exact arithmetic check

From (B5):

```text
6α + 2β      =  0                            [tracelessness on 6+2 split]
β            =  -3α
Y(L_L)       =  β = -3α                      [P1 accepted readout convention]
Q(e_L)       =  T_3(e_L) + Y(L_L)/2
            =  T_3(e_L) + (-3α)/2
-1           =  -1/2 + (-3α)/2
-1 + 1/2     =  (-3α)/2
-1/2         =  (-3α)/2
α            =  (-1/2) · (2 / -3)
            =  1/3.
```

No quark electric-charge cross-check is load-bearing in this row. The
only charge-unit input is P4.

## Load-Bearing Dependencies

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  — supplies the retained graph-first 6-state Sym² plus 2-state Anti²
  decomposition used in step (B1).
- [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
  — supplies the retained selected-axis surface on which the
  two-eigenvalue traceless U(1) ansatz is evaluated.

## Non-Load-Bearing Context

- `HYPERCHARGE_IDENTIFICATION_NOTE.md` is the conditional parent whose
  missing α-normalization bridge this note is meant to support after
  independent audit; it is not a dependency of this proof.
- `LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`
  records the same `+1 : (-3)` ratio as a prior decoration row. This
  note duplicates the two-line ratio derivation instead of depending on
  that row.
- `HYPERCHARGE_SQUARED_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md` is a
  companion squared-trace consistency check, not a load-bearing input.
- `LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`
  is chain-assembly context. This bounded bridge admits only the branch
  readout/notation convention needed to call the Anti² branch `L_L`;
  it does not claim to rederive the matter assignment.

The non-framework inputs are exactly P1-P4. The row remains unaudited
until the independent audit lane reviews this note, its retained
dependencies, accepted-premise packet, and runner.

## Boundaries

This bridge does not close:

- derivation of the `Q(electron) = -1` charge-unit convention itself;
- derivation of the GMN relation `Q = T_3 + Y/2`;
- derivation of the `T_3(e_L) = -1/2` weak-isospin assignment;
- derivation of the Anti²-as-`L_L` readout convention;
- derivation of the chiral matter content itself;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values;
- any parent theorem/status promotion (the bridge ratifies α = 1/3 as
  a separate retainable identity; downstream status of the parent
  hypercharge note is decided by the audit lane).

The bridge re-bases the parent's existing α = 1/3 admission onto the
explicit P1-P4 premise packet. It does not eliminate admission; it
formally exposes and ratifies the chain.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/hypercharge_alpha_third_normalization_runner.py
```

Expected:

```text
TOTAL: PASS=22 FAIL=0
VERDICT: bounded premise-packet bridge passes; alpha = 1/3 follows
from retained 6+2 split/tracelessness + accepted premise packet P1-P4
by rational arithmetic.
```
