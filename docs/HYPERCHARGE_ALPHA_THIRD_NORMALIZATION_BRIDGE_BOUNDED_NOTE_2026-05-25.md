# Hypercharge α = 1/3 Normalization Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/hypercharge_alpha_third_normalization_runner.py`](../scripts/hypercharge_alpha_third_normalization_runner.py)

## Claim

Given the existing retained eigenvalue-ratio surface for the unique
traceless U(1) generator on the LH-doublet sector C^8, and given the
admitted SM-convention Gell-Mann–Nishijima relation `Q = T_3 + Y/2`
together with the empirical assignment `Q(electron) = -1` (electron
electric charge as the unit of elementary charge), the normalization
scale of the one-parameter family
`Y_α = α (P_sym − 3 P_anti)` is uniquely fixed at

```text
α = +1/3   (doubled convention),
```

equivalently `Y(L_L) = -1` and `Y(Q_L) = +1/3`. The proof-walk uses
only:

1. The retained eigenvalue ratio `+1 : (-3)` on the
   (Sym², Anti²) sub-decomposition (i.e. `Y(L_L) = -3 Y(Q_L) = -3α`);
2. The admitted Gell-Mann–Nishijima relation `Q = T_3 + Y/2` and the
   admitted weak-isospin assignment `T_3(e_L) = -1/2`;
3. The empirical assignment `Q(electron) = -1` (electron charge
   chosen as the unit; this is the standard SI convention for the
   elementary-charge unit and is taken as a single empirical input).

The bridge consists of a one-line rational arithmetic identity that
re-bases the existing parent admission `Y(L_L) = -1` (currently
imported as a "SM-convention SM-Y match") onto the more primitive
empirical admission `Q(electron) = -1` plus the admitted GMN relation.

This is a bounded proof-walk satisfying the auditor's explicit
"cheapest repair" hint on the parent
[`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
(`notes_for_re_audit_if_any`: "cheapest repair is a retained bridge
deriving or formally ratifying the α = 1/3 normalization"). It does
not add a new axiom or a new repo-wide theory class.

## Proof-walk

| Step | Statement | Load-bearing input | Lattice-action input? |
|---|---|---|---|
| (B1) | `Y(L_L) = -3α` on the LH-doublet (2, 1) sub-block | Retained ratio theorem | no |
| (B2) | `Q(e_L) = T_3(e_L) + Y(L_L)/2` | Admitted GMN | no |
| (B3) | `T_3(e_L) = -1/2` | Admitted weak-isospin assignment | no |
| (B4) | `Q(e_L) = -1` | Admitted empirical input (electron-charge unit) | no |
| (B5) | Substitute (B2)–(B4): `-1 = -1/2 + (-3α)/2` | Rational arithmetic | no |
| (B6) | Solve for α: `α = 1/3` | Rational arithmetic | no |

The bridge does not cite the Wilson plaquette action, staggered phases,
Brillouin-zone labels, link unitaries, lattice scale `u_0`, a Monte
Carlo measurement, or a fitted observational value.

## Exact arithmetic check

From (B5):

```text
Q(e_L)       =  T_3(e_L) + Y(L_L)/2
            =  T_3(e_L) + (-3α)/2          [by (B1)]
-1           =  -1/2 + (-3α)/2              [by (B3), (B4)]
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

## Dependencies

- [`HYPERCHARGE_IDENTIFICATION_NOTE.md`](HYPERCHARGE_IDENTIFICATION_NOTE.md)
  — the parent whose admitted α = 1/3 normalization this bridge
  formally ratifies. The bridge does not duplicate or re-derive the
  parent's chain-assembly; it only supplies the missing scale-fixing
  identity.
- [`LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md`](LH_DOUBLET_TRACELESS_ABELIAN_EIGENVALUE_RATIO_NARROW_THEOREM_NOTE_2026-05-02.md)
  — supplies the retained eigenvalue ratio `+1 : (-3)` on the
  (Sym², Anti²) sub-decomposition used in step (B1).
- [`HYPERCHARGE_SQUARED_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md`](HYPERCHARGE_SQUARED_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md)
  — companion squared-trace bookkeeping confirming that at α = 1/3
  the GUT-consistency identity `Tr[Y_GUT²] = Tr[T_a²]_simple` holds on
  three generations (independent consistency check; not load-bearing
  for this bridge).
- `LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`
  — the matter-assignment authority that lets `L_L` be identified with
  the (2, 1) sub-block (chained out, not derived here).

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

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
TOTAL: PASS=4 FAIL=0
VERDICT: bounded bridge passes; α = 1/3 follows from retained
ratio + admitted GMN + admitted Q(electron) = -1 by rational
arithmetic.
```
