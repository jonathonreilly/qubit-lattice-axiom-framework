# Flavor — what axiom (not import) forces r=1/2? A measure axiom, best realized as a revision of A1 (carrier = ℝ[Z₃] in tracial standard form)

**Date:** 2026-05-30
**Claim type:** foundational analysis (axiom-level), not a derivation on the current axioms. Explicitly steps outside A1+A2 minimality at user request.
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_missing_axiom_carrier_measure_2026_05_30.py` (SCORECARD PASS=6).
**Source:** 18-agent panel `wf_9d4261e9` — 14 foundational architects (distinct traditions) + convergence/skeptic/overshoot evaluators + synthesis.

## Question (user)
Without assuming A1+A2 are fixed or minimal, and without an import: what AXIOM would let the
framework derive the charged-lepton modulus `r=|b|²/a²=1/2` (Koide Q=2/3), and what SHAPE would it have?

## Answer — the missing ingredient is a MEASURE, not a dynamical law
Fourteen architects (MaxEnt, least-action, KMS/Tomita, MaxEP, spectral-action/Connes, Kähler,
bootstrap, holographic, records/Darwinism, structural-revisionist, RG fixed-point, constructor
theory, sum-over-geometries, PT/exceptional-point) all reach r=1/2 — but the three cross-evaluators
agree the convergence is on **one arithmetic identity**: equal Hilbert-Schmidt weight on the two
trace-orthogonal C₃-isotypic generator channels,
`3a² = 6b²  ⟺  ‖aI‖²_HS = ‖b(J−I)‖²_HS  ⟺  r = ‖I‖²/‖J−I‖² = 1/(N−1) = 1/2 at N=3`.
Nine of fourteen reduce *literally* to this line; the dynamical/variational/equilibrium dressings
(entropy, action, modular flow, dissipation, RG) add **no content** over the bare relation. So the
framework is incomplete **as pure kinematics**, but it is incomplete by a **measure** (which invariant
inner product and which partition are physical), not by a force law. A dynamical A3 is *over-machinery*
for fixing one ratio.

## The real gap is a three-way fork (rep theory ranks none)
The same operator gives three different r under three partitions of the algebra:
| partition | condition | r |
|---|---|---|
| isotypic **generator channels** (I vs J−I) | `3a²=6b²` | **1/2** |
| **eigenvalue / idempotent** content | `(a+2b)²=2(a−b)²` | `17/2−6√2 ≈ 0.0147` |
| **per-mode** (3 equal components) | — | `1` |
The missing axiom's only real job is to **break this fork structurally**, not by fiat.

## Best concrete candidate — REVISE A1, don't bolt on A3
**A1′ (carrier + canonical metric):** the on-site generation carrier is `ℝ[Z₃]` in its **tracial
standard form** — acting on its GNS / `L²(ℝ[Z₃], τ)` space with the canonical normalized group trace.
This singles out the group-element ONB `{e, g, g²}`; the mass operator is the C₃-unbiased
`H = a·e + b·(g+g²)`; and the `(1,2)` weight (one identity direction vs two non-identity directions)
is the **forced dimension count of the carrier's canonical basis**, not a postulated measure.
Equipartition `a²·1 = b²·2 → r=1/2` is then **inherited from what H is built on**, not selected from a
fixed H. Every layered selection proposal must first postulate *both* the HS form *and* a scoring
functional; A1′ discharges both into one structural choice of carrier + canonical metric.

**Why revise A1 rather than add A3:** A1 currently says "a qubit `M₂(ℂ)=Cl(3)_even` per site" but is
**silent on which inner product and partition govern the generation algebra** — exactly the silence the
three-way fork exploits. A1′ closes that silence at the source. The price — re-deriving the qubit /
Cl(3) structure as an operator *on* this carrier — is the right kind of debt (it pushes the question to
foundations rather than papering over it with a selection principle).

## Falsifiable content (this is not "positing the number")
1. **`r = 1/(N−1)` ties r=1/2 to the derived generation count 3** — r=1/2 is *forced by* `n_gen=3`, not
   tuned. (N=2→r=1; N=4→r=1/3; N=6→r=1/5 → Q=7/15.) The strongest handle.
2. **Cross-sector universality with a structural escape:** any sector realized as the unbiased C₃
   group-algebra element → Q=2/3 (neutrinos predicted at 2/3 *unless* off-carrier / Majorana); CKM-mixed
   quark sectors deviate — consistent with observed quark Koide ≠ 2/3.
3. **Coheres with the derived signed/Hermitian (Dirac `H=iD`) readout** — the τ/HS form *is* the
   invariant of that readout class, not the singular-value/Yukawa class.

## Two independent corroborators worth keeping alive
- **Kähler / moment-map (#6):** reaches r=1/2 by a *structurally distinct* computation (rank-weighted
  phase-averaged moments `1·(a²+4b²)=2·(a²+b²)`; same final relation `a²=2b²`, different machinery), so
  r=1/2 is a fixed point of **more than one** principle. Predicts `Q=2/3 ⟺ complex b ⟺ Dirac/U(1)-gauged
  sector`, so **Majorana neutrinos (real b, frozen Brannen phase) must depart from 2/3** — a structural
  prediction — and it explains the derived δ-independence as the gauge direction of the quotient.
- **PT / exceptional-point (#14):** the only proposal checkable against PDG *today*. Charged leptons sit
  at `r=0.5000` exactly (the reality edge / exceptional point); up-quarks `r≈0.773` and down-quarks
  `r≈0.597` are both PT-broken (`r>1/2`). Recasts lepton "fine-tuning" as saturation of a stability edge.

## What it costs / does not break
r=1/2 is an **interior point of the commuting circulant family**: `[H,S]=0` holds, so the candidate
axiom introduces **no** chiral/anticommuting operator and therefore does **not** trip the
generation-chirality no-go (`comm(S) ∩ anticomm(Γ_χ) = {0}`). **The VALUE lane is clean and decoupled
from the chirality gate** — a structurally separate (and more tractable) question. A1′ preserves every
retained derivation (3 generations, C₃ regular rep, signature (3,1)/emergent time, the Koide identity).
The residual cost is the one all proposals share — privileging the tracial/HS form + isotypic-generator
split over the Plancherel-per-dimension (→r=1) or eigenvalue/idempotent (→0.0147) partitions — carried
by A1′ in its minimal, named form (a single structural commitment about the carrier's metric).

## Honest bottom line
> **r=1/2 is not waiting on a new dynamical law — it is waiting on a decision about which invariant
> measure and partition the substrate algebra canonically carries, and the most defensible place to make
> that decision is in A1 itself (A1′ = ℝ[Z₃] tracial standard form), where the (1,2) isotypic weight
> becomes a carrier property and `r=1/(N−1)=1/2` is inherited rather than selected.**

## Stale-citation flags
- Anchors retained on main: `KOIDE_Q23_BLOCK_WEIGHT_FRONTIER` (retained_bounded),
  `koide_z3_equivariant_anticommuting_no_go` (retained_bounded). `koide_signed_eigenvalue_vs_singular_value_readout` is audited_FAILED (used only qualitatively).
