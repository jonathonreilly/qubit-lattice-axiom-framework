# alpha_s CMT-Coupling-Map Derivation Theorem (bounded, narrow)

**Date:** 2026-05-17
**Type:** positive_theorem (bounded under named admissions)
**Claim scope:** the algebraic-derivation step that converts the retained
Combined Mean-Field Theory (CMT) correlator change-of-variables identity
`<O(U)> = u_0^{n_link} <O_V(V)>_eff` (D14 of
[`YT_EW_COLOR_PROJECTION_THEOREM.md`](YT_EW_COLOR_PROJECTION_THEOREM.md))
into the canonical tadpole coupling-rescaling map

```text
alpha_eff(O) = alpha_bare / u_0^{n_link}                              (M)
```

as an exact algebraic consequence on the polynomial ring in
`(alpha_bare, u_0, 1/u_0)`, treating `n_link` as an abstract positive
integer symbol. The map `(M)` is the *missing brick* between the CMT
correlator identity (retained) and the two definitions

```text
alpha_LM    :=  alpha_bare / u_0     = (M) at n_link = 1              (D1)
alpha_s(v)  :=  alpha_bare / u_0^2   = (M) at n_link = 2              (D2)
```

used by [`ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md)
as definitions and by [`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md)
as the framework-side carrier identity.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.

**Primary runner:** [`scripts/frontier_alpha_s_cmt_coupling_map_derivation.py`](../scripts/frontier_alpha_s_cmt_coupling_map_derivation.py)

**Authority role:** narrow theorem that closes ONE algebraic step in the
`alpha_s_derived_note` chain. Specifically, the step where existing
`alpha_s_derived_note`-adjacent notes have asserted `(D2)` as a
definition or "coupling map" without proving it from the CMT identity.
Block 08 (PR #1426) closed the operator-level `n_link = 2` count for
the gauge vacuum-polarization correlator
([`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md)).
Block 10 closes the *partition-function-side* step: given that count
plus the CMT correlator identity, the bare-to-effective coupling
rescaling factor is exactly `u_0^{n_link}` in the indicated direction.

This narrow theorem does NOT close the full alpha_s lane. It explicitly
does NOT touch:

- the upstream `u_0 = <P>^{1/4}` plaquette analytic-insertion gap
  (open in `plaquette_self_consistency_note`);
- the downstream `v -> M_Z` low-energy running bridge
  (bounded in `qcd_low_energy_running_bridge_note_2026-05-01`);
- any numerical value of `alpha_s(M_Z)`, `alpha_s(v)`, or `u_0`;
- the staggered-Dirac realization gate.

It supplies the algebraic glue between two retained / bounded pieces.

## Inputs (cited, not re-derived)

The theorem consumes three cited inputs as abstract algebraic facts:

```text
(I1) CMT correlator identity (retained D14 of yt_ew_color_projection_theorem):
       <O(U)> = u_0^{n_link} <O_V(V)>_eff
     where O is any lattice operator with n_link explicit gauge-link
     insertions, U is the bare lattice link variable, and V is the
     tadpole-rescaled link via U = u_0 V. The identity is the exact
     partition-function change of variables proven in
     YT_EW_COLOR_PROJECTION_THEOREM.md Section 2.4 (page reference: lines
     258-266, statement `<O(U)> = u_0^{n_link} <O_V(V)>_eff`).

(I2) Bare-coupling normalization of a 2-point correlator:
       <O[U]> = alpha_bare * K_U(kinematics)
     where K_U is the bare-scheme kinematic factor (defined to absorb all
     non-coupling structure). This is a definition of how the coupling
     enters at tree-level: a 2-point function with n_link external link
     insertions is, at lowest order, the bare coupling times a kinematic
     factor that depends on momenta and lattice spacing but not on
     u_0. The convention is standard Lepage-Mackenzie tadpole improvement.

(I3) V-scheme effective-coupling extraction:
       <O_V[V]>_eff = alpha_eff(O) * K_V(kinematics)
     where K_V is the V-scheme kinematic factor, related to K_U by
     K_U = K_V (no u_0 dressing in the purely kinematic factor; all
     u_0 dependence is absorbed into the link operator itself, as
     guaranteed by (I1)).

(I1) is consumed from a retained source. (I2) and (I3) are convention
definitions of effective coupling at tree-level in the bare and V
schemes respectively.

## Statement

Let `alpha_bare, u_0` be abstract positive-real symbols, and let
`n_link` be an abstract positive-integer symbol. Suppose the three
cited inputs `(I1), (I2), (I3)` hold. Then the bare-to-effective
coupling rescaling map

```text
alpha_eff(O) = alpha_bare / u_0^{n_link}                              (M)
```

holds exactly as an identity on the rational-function field
`Q(alpha_bare, u_0, 1/u_0)`.

## Proof

Pure algebraic substitution.

Step 1. By `(I2)`,
```text
<O[U]> = alpha_bare * K_U.                                            (1)
```

Step 2. By `(I3)` applied in the V-scheme,
```text
<O_V[V]>_eff = alpha_eff * K_V = alpha_eff * K_U                      (2)
```
where the second equality uses the convention `K_U = K_V` from `(I3)`.

Step 3. By `(I1)`,
```text
<O[U]> = u_0^{n_link} * <O_V[V]>_eff.                                 (3)
```

Step 4. Substituting `(1)` and `(2)` into `(3)`:
```text
alpha_bare * K_U = u_0^{n_link} * alpha_eff * K_U.                    (4)
```

Step 5. Since `K_U` is the bare kinematic factor and is by definition
nonzero (kinematic factors of 2-point functions at generic momenta are
nonzero), divide both sides by `K_U`:
```text
alpha_bare = u_0^{n_link} * alpha_eff.                                (5)
```

Step 6. Solving algebraically for `alpha_eff`:
```text
alpha_eff = alpha_bare / u_0^{n_link}.                                (M)
```

∎

## Direction-of-rescaling sanity check

The factor is `1 / u_0^{n_link}`, not `u_0^{n_link}`. The reason is
the direction in which the correlator identity `(I1)` is read: the
*bare* correlator equals `u_0^{n_link}` times the V-scheme correlator,
so to keep the kinematic factor fixed, the V-scheme coupling must
absorb the inverse factor. With `u_0 < 1` (standard SU(3) plaquette
gives `u_0 ~ 0.88`), `alpha_eff > alpha_bare`, which matches the
direction of tadpole improvement: the V-scheme couplings are *larger*
than bare because the bare lattice action absorbs the loop-suppressed
tadpole contributions.

## Derivable corollaries

By specializing `n_link`:

```text
At n_link = 1 (single-vertex gauge coupling, retained D15):
  alpha_eff(hopping) = alpha_bare / u_0 = alpha_LM.                   (C1)

At n_link = 2 (vacuum-polarization correlator, block 08 lemma +
                retained D15):
  alpha_eff(VP) = alpha_bare / u_0^2 = alpha_s(v).                    (C2)
```

`(C1)` reproduces `(D1)` of
`ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10`.
`(C2)` reproduces `(D2)` of the same note. Combined with the existing
narrow theorem's algebra `(P1) alpha_LM^2 = alpha_bare * alpha_s(v)`
and `(P2) alpha_s(v) / alpha_LM = 1 / u_0`, the chain from the CMT
identity to the canonical coupling map is closed.

## Admissions (named, not closed)

1. **CMT correlator identity (I1) is consumed as retained.** Its proof
   in `YT_EW_COLOR_PROJECTION_THEOREM.md` Section 2.4 invokes the
   partition-function change of variables `U = u_0 V`, which is exact
   on the abstract lattice but inherits the upstream
   `plaquette_self_consistency_note` analytic-insertion scope. The
   present theorem does NOT re-derive that.

2. **Bare normalization convention (I2)** is a definition of how the
   coupling enters the 2-point correlator at tree-level. It is the
   standard tadpole-improvement convention (Lepage & Mackenzie 1993).
   The theorem assumes this convention; it does not claim to derive
   the convention from a deeper principle.

3. **V-scheme kinematic-factor equality `K_U = K_V` (I3)** is the
   convention that the kinematic factor is u_0-independent, with all
   u_0 dressing absorbed into the operator. This is consistent with
   the CMT change-of-variables but is a convention choice on how to
   split the correlator into coupling and kinematic parts.

4. **n_link is the operator-level link count.** The block 08 lemma
   (`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`)
   verifies `n_link(VP) = 2` from the staggered Dirac operator
   structure. The present theorem holds for any positive integer
   `n_link`; specialization to `n_link = 2` consumes the block 08
   lemma as one-hop support.

## Hard rules compliance

- A_min only: pure symbolic algebra (sympy). No PDG observations
  imported. No fitted alpha_s value. No PDG comparators load-bearing.
  No `canonical_plaquette_surface` import. No audit-data touches.
- No claim of audit verdict: the source note explicitly disclaims
  status authority and defers to the independent audit lane.
- No merge / no main push: PR only.

## Independence from block 08

Block 08 closed an *operator-level* lemma on the staggered Dirac
operator:

- S1: `D'[lambda U] = lambda * D'[U]` (degree-1 vertex)
- S2: `Pi = -Tr[D^{-1} D' D^{-1} D']` has log-log slope = 2
- S3: `n_link(VP) = 2 * n_link(hopping)`

Those are numerical lattice-operator tests that the gauge
vacuum-polarization bubble is degree-2 in the gauge link.

Block 10 (this note) closes a *partition-function-level* algebraic
step:

- Given the CMT identity `<O(U)> = u_0^{n_link} <O_V(V)>_eff` and the
  convention split of correlator into coupling and kinematic factors,
  derive `alpha_eff = alpha_bare / u_0^{n_link}`.

Different theorem, different surface, different proof technique. Block
08's `n_link = 2` value is consumed as one specialization input here;
the present theorem's content is the algebra of the rescaling map
itself, which is `n_link`-independent in its proof.

## Cited-retained authority links

- `YT_EW_COLOR_PROJECTION_THEOREM.md` (retained, D14 CMT identity,
  D15 n_link counts)
- `YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`
  (block 08 conditional-bounded, n_link = 2 operator-level proof)
- `ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md`
  (consumes (D1), (D2); now grounded by (C1), (C2) of this theorem)
- `ALPHA_S_DERIVED_NOTE.md` (parent unaudited row; benefits from this
  partial closure but is not promoted by it)

## Validation Snapshot

Runner `frontier_alpha_s_cmt_coupling_map_derivation.py` runs 7
exact-symbolic tests (T1-T7) over abstract positive-real symbols
`(alpha_bare, u_0)` and positive-integer `n_link`. All seven pass
with zero residual under sympy `simplify`:

- T1: `(M)` substitution from `(I1) + (I2) + (I3)` yields exactly
  `alpha_eff = alpha_bare / u_0^{n_link}`
- T2: round-trip — substituting `(M)` back into `(2)` and `(3)`
  reproduces `(I1)`
- T3: specialization `n_link = 1` gives `alpha_LM = alpha_bare / u_0`
  (matches `(D1)` of the existing narrow theorem)
- T4: specialization `n_link = 2` gives `alpha_s(v) = alpha_bare / u_0^2`
  (matches `(D2)` of the existing narrow theorem)
- T5: composition with `(P1)` of `ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10`
  closes a self-consistent chain
- T6: direction-of-rescaling check — with `0 < u_0 < 1`, predict
  `alpha_eff > alpha_bare`
- T7: counterfactual probe — if the CMT identity were reversed
  (`<O(U)> = u_0^{-n_link} <O_V(V)>_eff`), the derivation would
  flip sign and give `alpha_eff = alpha_bare * u_0^{n_link}` instead;
  the asymmetry is genuine, not a convention.

## V1-V5 Disposition

PASS. See
`.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block10/REVIEW_HISTORY.md`.

## Package Role

Narrow theorem. Does not retroactively retain `alpha_s_derived_note`
because the upstream `u_0` analytic-insertion gap and the downstream
running bridge remain bounded. Provides the algebraic glue that has
been an unstated assumption in adjacent notes, raising the chain's
*structural* completeness without changing any numerical lane.

Not a new package carrier. Not a runner-promotion candidate. Pure
algebraic closure of one previously assertion-only step.
