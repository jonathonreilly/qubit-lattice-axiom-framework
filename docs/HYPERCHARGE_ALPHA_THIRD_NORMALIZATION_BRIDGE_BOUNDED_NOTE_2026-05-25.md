# Hypercharge α = 1/3 Normalization Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/hypercharge_alpha_third_normalization_runner.py`](../scripts/hypercharge_alpha_third_normalization_runner.py)

## Claim

Given the retained graph-first 6+2 split of the left-handed doublet
sector and the traceless two-eigenvalue U(1) ansatz on that split,
together with the admitted SM-convention Gell-Mann–Nishijima relation
`Q = T_3 + Y/2` and the empirical assignment `Q(electron) = -1`
(electron electric charge as the unit of elementary charge), the
normalization scale of the one-parameter family
`Y_α = α (P_sym − 3 P_anti)` is uniquely fixed at

```text
α = +1/3   (doubled convention),
```

equivalently `Y(L_L) = -1` and `Y(Q_L) = +1/3`. The proof-walk uses
only:

1. The retained 6-state Sym² and 2-state Anti² split from the
   graph-first SU(3) surface, plus tracelessness of the two-eigenvalue
   U(1) ansatz: `6α + 2β = 0`, hence `β = -3α`;
2. The notation/readout convention that the Anti² branch is the
   left-handed lepton doublet branch for this bounded bridge, so
   `Y(L_L) = β = -3α`;
3. The admitted Gell-Mann–Nishijima relation `Q = T_3 + Y/2` and the
   admitted weak-isospin assignment `T_3(e_L) = -1/2`;
4. The empirical assignment `Q(electron) = -1` (electron charge
   chosen as the unit; this is the standard SI convention for the
   elementary-charge unit and is taken as a single empirical input).

The bridge consists of a one-line rational arithmetic identity that
re-bases the existing parent admission `Y(L_L) = -1` (currently
imported as a "SM-convention SM-Y match") onto the more primitive
empirical admission `Q(electron) = -1` plus the admitted GMN relation.

This is a bounded proof-walk responding to the existing conditional
parent row's repair request for a narrow α-normalization bridge. The
parent `HYPERCHARGE_IDENTIFICATION_NOTE.md` is context, not a
load-bearing dependency for this proof. This note does not add a new
axiom or a new repo-wide theory class.

## Proof-walk

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (B1) | 6+2 graph-first split and traceless two-eigenvalue ansatz give `6α + 2β = 0`, hence `β = -3α` | Retained graph-first split + algebra | no |
| (B2) | The Anti² branch is the `L_L` branch on this bounded readout surface, so `Y(L_L) = β = -3α` | Admitted readout/notation convention | no |
| (B3) | `Q(e_L) = T_3(e_L) + Y(L_L)/2` | Admitted GMN | no |
| (B4) | `T_3(e_L) = -1/2` | Admitted weak-isospin assignment | no |
| (B5) | `Q(e_L) = -1` | Admitted empirical input (electron-charge unit) | no |
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
Y(L_L)       =  β = -3α                      [admitted readout convention]
Q(e_L)       =  T_3(e_L) + Y(L_L)/2
            =  T_3(e_L) + (-3α)/2
-1           =  -1/2 + (-3α)/2
-1 + 1/2     =  (-3α)/2
-1/2         =  (-3α)/2
α            =  (-1/2) · (2 / -3)
            =  1/3.
```

Cross-check on the (2, 3) sub-block at α = 1/3:

```text
Y(Q_L)  =  α            =  +1/3,
Q(u_L)  =  T_3(u_L) + Y(Q_L)/2  =  +1/2 + 1/6  =  +2/3,
Q(d_L)  =  T_3(d_L) + Y(Q_L)/2  =  -1/2 + 1/6  =  -1/3.
```

These match the empirical SM electric charges of (u_L, d_L), giving an
independent rational consistency check.

## Accepted Premises Registration (2026-05-26 audit-repair)

In response to the 2026-05-26 `audited_conditional` verdict
(`notes_for_re_audit_if_any`: "supply retained or explicitly
accepted-premise packet entries for the Anti²-as-L_L readout, GMN
relation, T_3(e_L) assignment, and Q(electron) unit convention"), this
section formally registers the four non-framework inputs the proof-walk
uses, in named-premise form. No new admissions are introduced; this is
a structural re-statement of admissions already present in §"Claim"
and §"Proof-walk" steps (B2)–(B5).

- **(P1)** *Anti²-as-`L_L` branch readout convention.* On the
  retained graph-first 6+2 split (Sym² 6-state ⊕ Anti² 2-state), the
  2-state Anti² branch is identified with the left-handed lepton
  doublet `L_L` for the bounded readout surface of this bridge. This
  is a notation/readout convention; the matter-sector identification
  itself is supplied by
  [`LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`](LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md)
  as chain-assembly context. **Status:** accepted-premise packet entry
  (admitted readout convention, not derived in this bridge).
- **(P2)** *Gell-Mann–Nishijima relation `Q = T_3 + Y/2`.* The SM
  convention bridge relating electric charge `Q`, weak isospin `T_3`,
  and hypercharge `Y` in the doubled convention. **Status:**
  accepted-premise packet entry (admitted SM-convention bridge, not
  derived in this bridge).
- **(P3)** *Weak-isospin assignment `T_3(e_L) = -1/2`.* The standard
  SM assignment placing the left-handed electron as the `T_3 = -1/2`
  weak-isospin doublet partner. **Status:** accepted-premise packet
  entry (admitted SM-convention weak-isospin assignment, not derived
  in this bridge).
- **(P4)** *Electron-charge unit `Q(electron) = -1`.* The standard SI
  convention assigning the electron's electric charge as the unit of
  elementary charge, with sign convention `Q(electron) = -1` (modern
  elementary-charge unit). **Status:** accepted-premise packet entry
  (empirical unit convention; this is a single empirical input, not
  derived in this bridge).

The four registered premises (P1)–(P4) jointly feed steps (B2)–(B5)
of the §"Proof-walk" table. Step (B1) (`β = -3α` from the 6+2
tracelessness) uses only the retained graph-first split below; it
does not consume any of (P1)–(P4). The composition `(B1)+(P1)+(P2)+
(P3)+(P4)` then closes `α = 1/3` by rational arithmetic in steps
(B6)–(B7).

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

The non-framework inputs are admitted conventions/empirical units:
GMN, `T_3(e_L) = -1/2`, the Anti²-as-`L_L` readout convention, and
`Q(electron) = -1` in elementary-charge units. The row remains unaudited
until the independent audit lane reviews this note, its retained
dependencies, admissions, and runner.

## Boundaries

This bridge does not close:

- derivation of the empirical `Q(electron) = -1` value itself
  (admitted as the electron-charge unit);
- derivation of the GMN relation `Q = T_3 + Y/2` (admitted as SM
  convention bridge);
- derivation of the chiral matter content itself;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values;
- any parent theorem/status promotion (the bridge ratifies α = 1/3 as
  a separate retainable identity; downstream status of the parent
  hypercharge note is decided by the audit lane).

The bridge re-bases the parent's existing α = 1/3 admission onto a
more primitive empirical admission (`Q(electron) = -1`) plus a more
universally-admitted bridge convention (GMN). It does not eliminate
admission — it formally ratifies the chain.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/hypercharge_alpha_third_normalization_runner.py
```

Expected:

```text
TOTAL: PASS=5 FAIL=0
VERDICT: bounded bridge passes; α = 1/3 follows from retained
6+2 split/tracelessness + admitted GMN + admitted Q(electron) = -1
by rational arithmetic.
```
