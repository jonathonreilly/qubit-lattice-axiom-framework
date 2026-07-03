# y_t/g_s Tadpole-Cancellation: Premise Derivation + Equal-Dressing Robustness

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Status:** review-loop source proposal. This note adds no axiom, no fitted
input, and no audit verdict. It writes no audit verdict and supplies no direct
effective-status change.
**Primary runner:**
[`scripts/frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.py`](../scripts/frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.txt`](../logs/runner-cache/frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.txt)

---

## Role

Companion to the `audited_conditional` narrow theorem
`YT_WARD_RATIO_TADPOLE_CANCELLATION_NARROW_THEOREM_NOTE_2026-05-17.md`
(`yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17`). That note
proves the algebraic cancellation

```text
    y_t(M_Pl) / g_s(M_Pl)  =  y_t_bare / g_bare                          (P1)
```

**conditional on** three inputs, which it attributes to
`yt_ew_color_projection_theorem` ("lines 213-256, 311-312"):

- **(D14)** a CMT change-of-variables identity `<O(U)> = u_0^{n_link} <O_V(V)>_eff`;
- **(D15)** `n_link = 1` per single-vertex coupling insertion;
- **(sqrt-readout)** `coupling_canonical = coupling_bare / sqrt(u_0)`.

The independent audit returned `audited_conditional` with the verdict that the
cited one-hop authority "is a retained_no_go kappa-family note and does not
provide the claimed CMT D14 identity, n_link=1 D15 premise, or
operator-square-root coupling readout needed to justify D1 and D2."

**The audit is correct, and the citation is broken.**
`YT_EW_COLOR_PROJECTION_THEOREM.md` is the 102-line *EW Color Projection
Kappa-Family No-Go* (`claim_type: no_go`) about the EW coefficient
`K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)`. It contains none of D14/D15/sqrt-readout,
and the cited line numbers `213-256` / `311-312` do not exist in a 102-line file
(runner Block E). The three premises had no real authority.

This companion **supplies the premises from real primitives**, to the extent each
is derivable, **and sharpens the cancellation**. The exact content is in the
runner (SCORECARD 22/22 PASS).

## (A) D14 (CMT change-of-variables) = link-monomial homogeneity (EXACT)

On the Lepage-Mackenzie mean-field surface every gauge link is written
`U_mu(x) = u_0 V_mu(x)` with the mean link `u_0 = <P>^{1/4}` (retained
[U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md)).
Any observable that is a **monomial of link-degree `n`** obeys
`O(u_0 V) = u_0^n O(V)` by homogeneity, hence
`<O(U)> = u_0^n <O_V(V)>_eff`. Verified for `n = 1..4`; the plaquette is the
`n = 4` case, consistent with `u_0 = <P>^{1/4}`. This is the exact statement
D14 names.

## (B) sqrt-readout = "the coupling is the square root of the strength" (EXACT)

The coupling `g = sqrt(4 pi alpha)`. If the strength `alpha` of an `n_link = n`
vertex is dressed by `alpha -> alpha / u_0^n`, then
`g -> g / u_0^{n/2}`. At `n = 1` this is exactly the canonical-surface single-
vertex readout `g = g_bare / sqrt(u_0)` used in (D1)/(D2). Verified for
`n = 0..3`.

## (C) Cancellation robustness (the sharpening, EXACT)

The cancellation `(P1)` is **far more robust** than its `n_link = 1` framing
suggests:

- **(C1)** For *any* common dressing factor `f(u_0)` shared by both couplings
  (`g_s = g_bare f`, `y_t = y_t_bare f`), the ratio is `y_t_bare/g_bare`,
  identically `u_0`-free -- regardless of the form of `f`.
- **(C2)** In particular it holds for *any equal* `n_link = n` (verified
  `n = 1, 2, 3`), not only `n = 1`.
- **(C3 / C4) Teeth.** It *fails* iff the two couplings carry **unequal**
  dressing: unequal `n_link` (`g_s:1, y_t:2`) leaves `1/sqrt(u_0)` in the ratio;
  an on-site Yukawa (`n = 0`) against the `n = 1` gauge vertex leaves
  `sqrt(u_0)`.

So the load-bearing premise is the **symmetry** "`g_s` and `y_t` are dressed
identically", not the specific value `n_link = 1` or the square-root power. This
reframes D14/D15/sqrt-readout: what `(P1)` actually requires is *equal single-
vertex dressing for the two couplings*.

## (D) Gauge-side grounding: the staggered hopping vertex is single-link

The operator-counting lemma S1
([YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md))
is reproduced in the runner: with the link-exponential convention
`U = exp(i a A)` (`dU/d eps|_0 = i a U_0`) the staggered Dirac vertex
`D' = dD/d eps` is supported on nearest-neighbour bonds and carries exactly one
power of the link (the mass term is `U`-independent and drops). Hence
`n_link(g_s) = 1` for the gauge-fermion vertex.

## Scope and honest residual

This companion (i) corrects the broken citation, (ii) gives exact reproofs of
D14 and the sqrt-readout, (iii) sharpens the cancellation to the equal-dressing
**symmetry** with the gauge side grounded at `n_link = 1`, and (iv) reduces the
remaining conditionality to a **single structural equality**:

```text
    n_link(y_t)  =  n_link(g_s)  ( = 1 ).
```

This equality is **named, not discharged**, because in this framework `y_t` is
*not a fundamental coupling*: it is generated from `g` by single-gluon exchange
(matching `y_t^2 = g^2/(2 N_c)`), so its tadpole dressing is *inherited* from the
gauge sector -- but that routing uses the open same-1PI construction gate
([YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md](YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-10.md)).
At the pure operator level the equality is a structural premise on the `H_unit`
composite's single-link content. The further admissions are framework-canonical
and shared across the `_yt` cluster, not introduced here:

1. the Lepage-Mackenzie mean-field **scheme** `U = u_0 V` (the framework's
   canonical tadpole-improved surface);
2. the **staggered-Dirac realization** open gate
   ([MINIMAL_AXIOMS_2026-05-20.md](MINIMAL_AXIOMS_2026-05-20.md));
3. the `H_unit` single-link composite structure / the same-1PI matching that
   ties `y_t` to `g`.

So the cancellation note moves from "conditional on three premises cited to a
wrong no-go note" to "conditional on the single structural equality
`n_link(y_t) = n_link(g_s)`, with the gauge side grounded, D14 and the
sqrt-readout exact, and the cancellation robust to the common value." This does
not by itself lift the note to retained; it materially repairs and tightens its
footing.

## Reprove-and-cite ledger

- **Reproven here** (runner, exact sympy): D14 link-monomial homogeneity
  (`n = 1..4`) and the `u_0 = <P>^{1/4}` consistency; the sqrt-readout
  (`n = 0..3`); the equal-dressing robustness of `(P1)` (C1/C2) and its failure
  under unequal dressing (C3/C4); the single-link structure of `D' = dD/dA`
  (Block D); the broken-citation arithmetic (Block E).
- **Cited** (authorities reused, not re-derived): `u_0 = <P>^{1/4}` (retained
  `u0_plaquette_quartic_derivation`); the staggered hopping single-link count
  (`yt_vertex_power_operator_counting_lemma`); the cancellation algebra `(P1)`
  itself (the parent narrow theorem). No PDG value, numerical comparator, or
  fitted selector is consumed.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links so the audit
citation graph can track them. The target row is named as a plain label, not as
a reciprocal source-graph dependency. This section does not promote this note
or change any audited claim scope.

Target row label:

- `YT_WARD_RATIO_TADPOLE_CANCELLATION_NARROW_THEOREM_NOTE_2026-05-17.md`

Dependency links:

- [U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md](U0_PLAQUETTE_QUARTIC_DERIVATION_NARROW_THEOREM_NOTE_2026-05-17.md)
- [YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md)
- [ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
