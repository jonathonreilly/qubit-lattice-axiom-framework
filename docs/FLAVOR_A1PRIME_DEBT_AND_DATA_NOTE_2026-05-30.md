# Flavor — the candidate revised Axiom 1 debt does NOT discharge, and the data falsifies universality: both close honestly on r=1/2 as a genuine minimal import

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** bounded negative (two convergent builds) — tempers the prior architect-panel optimism.
**Runner:** `scripts/flavor_a1prime_debt_and_data_2026_05_30.py` (SCORECARD PASS=8).
**Source:** Build A `wf_7e231043` (candidate revised Axiom 1 measure-inheritance) + Build B `wf_e9277328` (predictions vs data).

## Two builds, opposite directions, same answer
Run in parallel to test the carrier-measure proposal (candidate revised Axiom 1: r=1/2 is *inherited* from the substrate's
canonical measure, and predicts a falsifiable family). Both came back negative, convergently.

## Build A — candidate revised Axiom 1 does NOT discharge its debt (it is a genuine new axiom, not a clarification)
- **The inherited measure is well-defined and retained-grade:** the unique tracial state from the qubit
  substrate (Powers UHF uniqueness, proved on framework baseline; provenance only, not an import). This part is solid.
- **But restricted to `ℝ[Z₃]`, its canonical orthonormal basis is the group-element basis `{e,g,g²}`**
  (Gram = I under `τ=Tr/3`) — the **dimension/Plancherel** basis, 3 = 1+2 modes. Equal weight per real
  mode is the **dimension partition → r=1 (Q=1)**. *That is the inherited framework default.*
- **candidate revised Axiom 1's claim is internally inconsistent:** in that ONB, `J−I = g+g²` occupies **two** orthonormal
  directions, not one. The ratio `r=1/(N−1)=1/2` is the weight of `e` against the *combined* two
  remaining directions packaged as **one complex slot** — i.e. the `det_C` / complex-counting regrouping,
  the opposite of equal-weight-per-mode.
- **And that regrouping is not merely absent but incompatible with the fixed order-three carrier:** complex
  `det_C` counting treats the doublet amplitude as a *continuous U(1) rephasing* of `C`, while the order-3
  relation `C³=I` permits only the three cube-root phases. The repaired runner checks this explicitly by
  verifying the `J-I` coefficient vector `(0,1,1)`, the two-mode support, the factorization
  `z³-1=(z-1)(z²+z+1)`, and a continuous-phase counterexample. Thus `r=1/2` requires overriding the
  inherited measure with a continuous/complex structure on the doublet — a genuine import, **converging with
  `koide_z3_equivariant_anticommuting_no_go`** and the existing `det_C-vs-det_R` derivation.

> **Build A bottom line:** the framework's *default* (inherited tracial measure + `C³=I`) is **r=1, Q=1**.
> The observed `Q=2/3` is **not** the default; it requires the complex-counting import.

## Build B — the universality prediction FAILS data (strains the axiom)
- **Charged leptons hit it to 5 digits:** `c²=2`, `r=0.49999`, `Q=0.66666`, zero free parameters — a
  real, striking, **1-of-4** fact.
- **The other three N=3 sectors miss, one-sided:** up `c²=3.09` (r=0.77), down `c²=2.39` (r=0.60) — both
  *above* the lepton value; neutrinos *below*. No single mechanism produces displacements in both directions.
- **The empirically-Koide quark triplet is the CROSS-sector `(c,b,t)`** (`c²≈2.02`, Q≈2/3 to 0.4%;
  Rodejohann-Zhang) — which **contradicts** the axiom's *within*-sector C₃ premise: the ~2/3 quark
  coincidence straddles the up/down divide, the opposite of "leptons special because unmixed."
- **Neutrinos exclude Q=2/3 by the splittings alone** (NO sweeps `[0.34, 0.585]`, never 2/3), *regardless*
  of Dirac/Majorana. The Kähler "Majorana = frozen phase → departs 2/3" is **mis-specified**: `dQ/dδ=0`
  (Q is independent of the Brannen phase), so freezing the phase cannot move Q.
- **The CKM off-carrier escape is an unfalsifiable fudge** *and* quantitatively fails as a closed mechanism:
  the quoted 17–37° generation-rotation inventory is `1.31–2.85×` the Cabibbo 13° angle (not the earlier
  stale "5×" phrasing), and the packet predicts neither the sign nor the ordering.

> **Build B bottom line:** universality is falsified; the escapes are fudges; `r=1/(N−1)` is untestable
> (no N≠3 fermion mass families); the PT reality-edge is numerology. What survives is *only* the narrow
> 1-of-4 fact: charged leptons sit at `c²=2` exactly.

## Combined honest verdict
The carrier-measure axiom does **not** work as the architect panel hoped, from *both* sides:
- It is **not** a clarification of A1 — the inherited measure gives r=1, and r=1/2 needs an import
  (complex/continuous doublet structure) that `C³=I` forbids as native.
- Its **falsifiable content fails** — only charged leptons obey; the cross-sector data contradicts the
  premise; the escapes are fudges.

This **reconfirms and sharpens** the campaign's standing conclusion: **r=1/2 is a genuine, precisely
characterized minimal import — the complex/continuous (`det_C` / U(1)) counting of the doublet
continuation amplitude — converging with the generation-chirality gate, not a theorem on framework baseline.** The
framework's honest *default* prediction is `Q=1` (democratic), and the observed `Q=2/3` marks exactly the
one place a continuous/chiral structure must be imported.

**What genuinely survives as an open, unexplained fact:** charged leptons sit at `c²=2` (r=1/2) to five
digits with zero free parameters, while the other three sectors do not — a real 1-of-4 regularity with no
derived reason yet. The next path the data opens (not a closure): explain the *monotone one-sided
displacement* (up > down > lepton above carrier; neutrinos below) from an independent structural quantity,
since CKM is not a closed magnitude/sign/order mechanism; and the cleanest future discriminator remains the absolute neutrino
mass scale + 0νββ, read through the **signed** (`det_R`/Brannen) branch rather than an amplitude shift.

## Repair notes (2026-06-03)

- The contested Build-A pass is no longer a hard-coded `True`: the runner now derives the `J-I=(0,1,1)`
  support in the inherited tracial ONB and checks the discrete `C³=I` phase classification against a
  continuous U(1) counterexample.
- The Brannen signed-readout phase statement is now checked symbolically:
  `Q_signed = 1/3 + 2|b|²/(3a²)`, hence `dQ/dδ=0`.
- The CKM angle inventory is corrected from stale "5×" wording to the actual `17/13–37/13 = 1.31–2.85`
  ratio range. This correction does not turn CKM into a derivation; it only fixes the arithmetic.

## Stale-citation flags
- Anchors: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded), Powers-UHF tracial uniqueness
  (proved inline on framework baseline), `det_C-vs-det_R` doublet-measure derivation. `koide_signed_eigenvalue_vs_singular_value_readout` is audited_FAILED (used qualitatively).
