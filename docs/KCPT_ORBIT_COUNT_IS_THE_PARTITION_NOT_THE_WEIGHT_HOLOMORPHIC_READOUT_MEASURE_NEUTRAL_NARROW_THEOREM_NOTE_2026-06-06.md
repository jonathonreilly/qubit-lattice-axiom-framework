# The K/CPT-Orbit Count Delivers the 2-Sector Partition, Not the Inter-Block Weight r; the Holomorphic Readout Clears the Anticommuting No-Go but is Measure-Neutral — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (structural; the value r=1/2 is a registered pattern, not forced)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/kcpt_orbit_count_is_partition_not_weight_runner.py`](../scripts/kcpt_orbit_count_is_partition_not_weight_runner.py)
**Cached output:** [`logs/runner-cache/kcpt_orbit_count_is_partition_not_weight_runner.txt`](../logs/runner-cache/kcpt_orbit_count_is_partition_not_weight_runner.txt)

## Audit context

A find-the-escape panel tested whether the framework forces the **holomorphic/multiplicity count**
of the generation doublet — weighting the complex coefficient `b` once → `(1,1)` → `r=1/2` →
`Q=2/3` — over the **real/vector count** → `(1,2)` → `r=1` → `Q=1`. The proposed escape: the
RECORD axiom registers the **K/CPT orbit** of the realized central sector, which merges
`omega ↔ omega-bar` into one orbit, so the doublet is "one complex `b`" → count once → `r=1/2`.

This note records the verdict: the escape is a **weight-leak** (it delivers the partition, not the
weight), with two genuinely new structural sharpenings. It closes the candidate escape, answers
the KEY question of the open lead
[`SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04`](SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md)
(`unaudited`), and corrects that note's `(1,1)→r=1/2` framing.

Anchors:
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
(`retained_bounded`, GAP B = the partition the orbit count re-derives),
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
(`retained_bounded`, the anticommuting grading the holomorphic readout clears),
[`FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS_DO_NOT_FORCE_R_HALF_NO_GO_NOTE_2026-06-02`](FLAVOR_OPERATOR_SPECTRAL_FUNCTIONALS_DO_NOT_FORCE_R_HALF_NO_GO_NOTE_2026-06-02.md)
(`retained_no_go`).

## Safe statement

Generations = `C3` regular rep on `C^3` = singlet (trivial) ⊕ doublet (`omega, omega-bar`);
`r = |b|^2/a^2`, `Q = 1/3 + (2/3) r`.

**Theorem.**

1. **Orbit count = the 2-sector partition.** The K/CPT (complex-conjugation) orbit set of the
   `C3` irreps is `{{trivial}, {omega, omega-bar}}` = **2 orbits** = the einselected
   `{P0 (rank 1), P1 (rank 2)}` 2-sector partition. So the orbit clause *re-derives GAP B's
   partition* directly — a legitimate Record-safe **multiplicity** readout (which sector / how many
   blocks).

2. **The orbit count is r-invariant** (the escape's fatal flaw). The K/CPT action is `b → b-bar`,
   and `r = |b|^2/a^2` depends only on `|b| = |b-bar|`, so `max|r(a,b) − r(a,b-bar)| = 0` (10^5
   draws). Explicit `r=1/2` and `r=1` states have **identical** orbit cardinality (= 2). The orbit
   count carries **zero** inter-block-weight information — it moves only `arg(b)` (the `delta=0`
   chirality pin), which is `Q`-orthogonal to the modulus that sets `r`. So "count `b` once → `r=1/2`"
   converts a cardinality into a per-sector weight — the registered pattern `r`, which remains
   registered data.

3. **The holomorphic readout clears the anticommuting no-go (the open lead's KEY question).** The
   complex structure implementing "count `b` once" is `J_cs = (C − C^2)/sqrt(3)`: `[J_cs, C] = 0`,
   `J_cs^2 = −P_doublet`, and `[J_cs, M] = 0` for **every** `C3`-invariant mass `M`. So `J_cs`
   **commutes** with the mass operator and is `C3`-equivariant — strictly **weaker than** and
   **distinct from** the anticommuting chiral grading `Gamma_chi` that the retained
   `koide_z3_equivariant_anticommuting_no_go` forecloses (`{J_cs, Gamma_chi} = 2.83 ≠ 0`). A
   `C3`-equivariant `Z2` block-grading suffices to *define* the index/readout, and it **exists** —
   the holomorphic readout is a genuinely weaker requirement and **clears the no-go**.

4. **But the holomorphic readout is measure-neutral — clearing the no-go buys no forcing.** Precisely
   because `J_cs` commutes with `M`, `exp(theta·J_cs)` is **orthogonal with det = +1** for all
   `theta`: it preserves **both** the real-trace and complex-trace measures, so it adjudicates
   neither count and carries **zero** weight-selection power. A commuting complex structure is a
   mode-relabeling, not a dynamical pairing.

5. **A genuine complex-trace count gives r=1, not r=1/2** (correcting the open lead). Complex-trace
   equal-block-energy (`a^2 = |b|^2`) gives `r = 1`. The value `r=1/2` appears only via the
   **separate** equal-power-per-block balance `3a^2 = 6|b|^2` — the registered weight. So the
   open lead's "`(1,1)→r=1/2`" is fold + balance, not a pure count.

6. **The antiunitary points the opposite way.** `omega` has Frobenius-Schur indicator `0` (complex
   type), so by Wigner an antiunitary `K` can only **realify** `(omega, omega-bar)` into a
   2-real-dim block = the `(1,2) → r=1` side; `K` on the doublet 2-plane is a `det = −1` reflection
   (realifying), not the `det = +1` `U(1)` rotation a complex-count `det_C` would require.

**Verdict: `r=1/2` is a registered pattern, not forced by the minimal axioms.** The `(1,1)`-vs-`(1,2)`
count is a free choice of trace base-field on the doublet Wedderburn block; nothing in the minimal axioms, and
nothing in the K/CPT-orbit count, makes that choice.

## The genuine open piece (the one live route)

The single un-falsified path to *force* the field/measure choice is to **source the
reduced-over-`C` / chiral Pfaffian trace from the gated staggered-Dirac mass/Yukawa
fluctuation-determinant** (the substep-4 realization, off `main`; `main` carries the kinetic-only
surface). The decisive artifact is a runner that builds the realized staggered-Dirac mass operator
on the `hw=1` orbit and tests whether its fermion fluctuation determinant weights `b` by its
`C`-measure (once → `det_C` → `r=1/2`) or its `R`-measure (twice → `det_R` → `r=1`). Until
substep-4 lands on `main`, that artifact cannot be built — which is itself the sharp statement of
where the gate sits.

## Boundary (honest)

- **Honest negative + structural sharpenings.** No non-circular forcing of `r=1/2` was found; the
  value is a registered pattern. The landable content is the structural facts (orbit = partition
  not weight; `J_cs` weaker than and clearing the anticommuting no-go; measure-neutrality;
  complex-trace → `r=1`).
- **Closes a candidate escape, not the lane.** It forecloses the K/CPT-orbit *forcing* of `r=1/2`;
  it does **not** foreclose the gated substep-4 holomorphy route (live, the one frontier).
- **Forces no value.** `r` stays the registered charged-lepton pattern; quarks/ν register other `r`.
  No fitted value is used as input (the `r=1/2` and `r=1` states are both constructed; `|b|` sampled
  randomly; the characters/isotype split are pure group theory).

## What this is not (no-go hygiene on the closed-escape clause)

The closed-escape clause is **route-specific**, not a global no-go: it shows the *K/CPT-orbit count*
does not force `r=1/2` (it is r-invariant), and that the *commuting* holomorphic readout is
measure-neutral. It does **not** claim `r=1/2` is underivable in general — the gated substep-4
fluctuation-determinant holomorphy remains a live route. No finite enumeration of routes is claimed.

## Forbidden imports check

No new axiom/import. Pure `C3` group theory (characters, Wedderburn `R[Z3]=R⊕C`, Frobenius-Schur,
the complex structure `J_cs`) plus the retained partition (`flavor_einselection`), the retained
anticommuting no-go, and the retained spectral-functionals no-go. All computations are exact
finite-dimensional arithmetic. The open route is named, not asserted.

## Runner check breakdown

Class A: (1) 2 K/CPT orbits = the rank-1/rank-2 partition; (2) `r`-invariance under `b→b-bar`
(10^5 draws, max = 0); (3) `J_cs` commutes with `C` and every `C3`-invariant `M`, `J_cs^2 =
−P_doublet`, `{J_cs, Gamma_chi} ≠ 0`; (4) `exp(theta J_cs)` orthogonal, `det = +1`; (5) complex-trace
→ `r=1`, `r=1/2` needs the `3a^2=6|b|^2` balance; (6) `FS(omega) = 0`, `K` is a `det=−1` reflection.
Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact `C3` group theory. The K/CPT-orbit set has 2 orbits = the einselected
2-sector partition (re-deriving GAP B's partition from the orbit clause), and the orbit count is
exactly `r`-invariant (`b→b-bar` fixes `|b|`), so it is a multiplicity readout that carries no
inter-block weight — "count `b` once → `r=1/2`" is a weight-leak. The complex structure `J_cs`
implementing the holomorphic readout commutes with `C3` and the mass operator (clearing the retained
anticommuting no-go, which is a strictly stronger requirement) but is orthogonal/measure-neutral, so
it forces nothing; a genuine complex-trace count gives `r=1`, and the `FS=0` antiunitary realifies
toward `r=1`. The honest outcome is `r=1/2` = registered pattern; the one live route is the gated
staggered-Dirac substep-4 fluctuation-determinant holomorphy. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/kcpt_orbit_count_is_partition_not_weight_runner.py
```
