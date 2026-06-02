# Flavor — "why not both?" : Q=1 makes the rank-1 democratic sector; the det_C/det_R axis ORGANIZES the fermion spectrum; but charge-selection does NOT close the pin

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded result on a productive reframe (not a closure) + one new positive (sector ordering) + a corrected sub-claim.
**Runner:** `scripts/flavor_both_readings_charge_selects_2026_05_30.py` (SCORECARD PASS=5).
**Source:** 6-agent build `wf_fad9743b` (map → 4 tests → adjudication), with an independent correction to the adjudicator's neutrino claim.

## The reframe (user)
Instead of a fork (det_C *or* det_R), maybe **both** readings are realized and a physical property selects
which: charged → det_C → Q=2/3 (leptons); neutral → det_R → Q=1 (rank-1/democratic). Would close the
measure-selection pin by making the electric-charge U(1) the thing that orients/uses `J_cs`.

## What Q=1 physically makes — CONFIRMED
`H=aI+bC+b̄C²` with **real b** at `r=|b|²/a²=1` (b=a) has eigenvalues **exactly `{3a, 0, 0}`** — **one heavy
generation + two massless** = the textbook **rank-1 / democratic** mass matrix. (At r=0, fully degenerate
`{a,a,a}`; the det_C/Brannen branch at r=1/2 gives the three distinct charged leptons, Q=2/3.) Airtight.

## NEW POSITIVE — the det_C/det_R axis organizes the whole charged-fermion spectrum
The Koide Q of the real fermion sectors is **monotone**, bookended by the two readout extremes:

| sector | Q | r |
|---|---|---|
| charged leptons | **0.6667** (=2/3, det_C complex end) | 0.500 |
| down quarks (d,s,b) | 0.7314 | 0.597 |
| up quarks (u,c,t) | 0.8490 | 0.773 |
| rank-1 limit `{3,0,0}` | **1.0000** (det_R democratic end) | 1.000 |

So the complex(det_C, Q=2/3) → real-democratic(det_R, Q=1) axis is not a mere binary — it is a
**one-parameter ladder that all the charged sectors sit on**, with leptons at the maximally-complex end and
up-quarks nearest the democratic end. This reframes "the Koide value" from an isolated lepton coincidence to
*where each species sits between the two native readings*.

## But charge-selection does NOT close the pin
The mechanism "carry a U(1) charge → activate `J_cs` → det_C" breaks at the first arrow:
- **The framework's gauge U(1)s are generation-blind.** Hypercharge, U(1)_em, the pseudoscalar U(1), and
  fermion-number all commute with the generation circulant and act as scalars `e^{iχ}I` on the triplet
  (Koide A1 **Probe 14**, runner-verified: all trivial on `A^{C₃}`). The charge lives on the
  spinor/chiral-cube factor, **not** the generation R³ where `(r, arg b)` live. Same generation-blindness as
  the qubit's central `i`.
- **A doublet-rephasing U(1)_b is incompatible with `C³=I`** (it would be a rephasing of C, quantized to the
  discrete C₃) — a new primitive, not a derived symmetry.
- **The quark sector refutes the naive rule.** Up (0.849) and down (0.731) are charged Dirac fermions
  carrying the very U(1) invoked, yet sit *above* 2/3 toward the democratic end. The CKM-mixing rescue fails
  **quantitatively** (CKM near-diagonal, far too small for a 30–50% spectral shift) **and directionally**
  (leptons land *exactly* on 2/3 despite **large** PMNS mixing; quarks miss 2/3 despite **small** CKM mixing
  — mixing anti-correlates with deviation).

## Corrected sub-claim (neutrinos)
The build's adjudicator claimed the neutrino Q "crosses 2/3 at m1≈3.2 meV." **This is wrong** — at that mass
`Q_ν≈0.44`. In the standard positive-√ readout (normal ordering, within the cosmological bound) `Q_ν ∈
[1/3, 0.585]` and **never reaches 2/3**. So neutrinos are *off* the det_C branch — weakly consistent with the
neutral/real reading, but this is consistent-not-predictive (a signed/Brannen readout could differ).

## Honest verdict: (b) productive reframe, not a closure
- **Real and verified:** Q=1 = rank-1 democratic; the det_C/det_R **sector ordering** (leptons < down < up <
  rank-1). The reframe correctly identifies that `J_cs` is forced-but-unoriented and that *some* continuous
  U(1)-type structure is the missing orienter.
- **Not a derivation:** electric charge cannot be that structure (it is generation-blind), so "charge selects
  the measure" relocates and dresses the *same* minimal flavor-U(1)/measure import without supplying it.

## Sharpest next step (now falsifiable)
Search for a **derived continuous *flavor/horizontal* U(1) that rephases the doublet (`b→e^{iθ}b`) relative
to the singlet `a`, reconcilable with `C³=I`** — e.g. a U(1) acting on the singlet⊕doublet idempotent
decomposition rather than on `C` itself. The reframe's **gift** is a falsification constraint: any such
mechanism must reproduce the **entire ordering** (leptons 2/3 < down 0.73 < up 0.85), not just the lepton
point — and without an anti-correlated mixing fudge. The orthogonal `r=1/2`-equipartition gate (trace-vs-block)
remains separate and untouched by charge-selection.

## Stale-citation flags
- Anchors: `generation-doublet-measure-detC-vs-detR-2026-05-29` (Step 4b gauge-blind theorem), Koide A1
  `Probe 14` (retained-U(1) hunt, all candidates trivial on the doublet), hypercharge-identification notes
  (retained_bounded, the charges are native but flavor-diagonal). `koide_c3_generator_rephasing_obstruction` (retained).
