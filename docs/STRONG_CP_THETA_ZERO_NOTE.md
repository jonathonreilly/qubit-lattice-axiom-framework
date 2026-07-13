# Strong CP / θ = 0 Conditional Action-Surface Closure

**Date:** 2026-04-16 (status line narrowed 2026-04-28 per audit-lane verdict; action-surface firewall clarified 2026-05-26; cited-selection repair 2026-07-12)
**Status:** `bounded_theorem` source-side boundary: conditional `θ_eff = 0` closure on the **bounded Wilson-plus-staggered / K-real Case-A selected action surface** constructed by the runner. The decisive action-surface selection is now wired to the bounded authorities below rather than stipulated by the runner. Not a retained or tier-ratifiable strong-CP solution beyond those authorities' own conditions: the canonical real-positive Wilson class, the character/orientation-even/odd-support positive-class hypotheses, the supplied scalar-mass boundary and positive-mass convention, and the supplied K-real Case-A determinant-channel reading. The sector-weight leg is additionally conditional on a supplied or separately derived integer-valued emergent `Q` with populated support; its existence, integrality, nonvacuity, and susceptibility remain open. An admitted CP-odd action term or complex mass phase re-opens the question.
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_strong_cp_theta_zero.py`

## Load-bearing dependencies

| Authority | Source claim boundary | Consumed content |
|---|---|---|
| [Native Positive-Class Adjudication (2026-07-04)](THETA_GAUGE_NATIVE_POSITIVE_CLASS_EMERGENT_SECTOR_WEIGHTING_NARROW_THEOREM_NOTE_2026-07-04.md) | `bounded_theorem` author-side classification; audit grade is not assigned here | In the canonical imported Wilson + staggered-Wilson class, non-negative native sector pushforwards make a positive relative emergent gauge-side theta weighting vacuous or zero; zero is selected on gcd-one populated support (adjacent populated sectors suffice). Existence, integrality, nonvacuity, and susceptibility of an emergent `Q` remain outside the authority. |
| [Gauge Z2 Character Collapse and Positive-Class Zero-Branch Selection (2026-07-03)](THETA_GAUGE_Z2_CHARACTER_COLLAPSE_ODD_SUPPORT_AND_POSITIVE_CLASS_ZERO_BRANCH_SELECTION_BOUNDED_THEOREM_NOTE_2026-07-03.md) | `bounded_theorem` author-side classification; audit grade is not assigned here | For a multiplicative theta character, orientation-evenness plus odd support collapses the gauge branch to `{0, π}`; membership in the strictly positive conjugation-paired class excludes the odd-support `π` branch and selects zero. Character form, orientation-evenness, odd support, and positive-class membership are load-bearing, and physical-action-class membership is not supplied by this authority itself. |
| [Single-Plaquette CP-Odd Slot Rejection and Quark-Mass Orientation (2026-05-19)](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) | `bounded_theorem` author-side classification on a supplied-premise surface; audit grade is not assigned here | Under P1-P5 on the canonical real-positive Wilson surface, excludes the reviewed CP-odd single-plaquette action slot `i θ Σ_P Im Tr U_P`; under staggered anti-Hermiticity, the supplied real-positive determinant boundary, and the supplied scalar-mass class, excludes non-real scalar mass phases. It does not exclude clover or other multi-plaquette slots, and the positive mass sign is convention-aligned rather than derived. |
| [Mass-Orientation Zero Branch on the K-Real Staggered Surface (2026-07-01)](THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md) | `bounded_theorem` author-side classification; historical Tier-A/admission references supply no ready premise; audit grade is not assigned here | On the supplied staggered-only Case-A K-real surface (real antisymmetric `M_KS`, bipartite `ε` grading, a reality-preserving background, and real scalar mass or a Hermitian flavor operator on the flavor tensor factor), exact `±iλ` pairing makes the determinant non-negative for either real sign; its orientation phase is zero on the nonzero-determinant locus. The determinant-channel K-real reading remains supplied; Wilson shifts, non-commuting flavor-kinetic couplings, and non-K-real flavor blocks are outside scope. |

## 2026-07-12 cited-selection correction

The action-surface dependencies were previously uncited, and the runner
previously hard-coded `θ_bare = 0` and positive-real masses before checking
closure. This repair wires the four bounded authorities above and makes the
runner construct candidate gauge and per-flavor mass-phase slots, compute the
allowed conditional basis, and only then run the unchanged determinant,
axial, effective-action, and topological-sector closure legs. The repair does
not enlarge any authority's claim boundary or predict an audit outcome.

## 2026-05-26 action-surface firewall

This row is a bounded selected-action-surface theorem, not an unconditional
strong-CP solution. Its load-bearing premises are:

1. the reviewed gauge action lies in the canonical real-positive Wilson class
   and, where the sector-character result is used, satisfies character form,
   orientation-evenness, odd support, and positive-class membership;
2. the reviewed fermion action lies in the supplied scalar-mass class with the
   convention-aligned positive representative and on the K-real Case-A
   determinant-channel surface; and
3. the topological-weight argument is applied only after the cited conditional
   selectors have computed the zero gauge branch and the selected positive,
   nonzero mass representatives lie on the zero-phase determinant locus.

The note therefore licenses only the statement

    θ_eff = 0 on the bounded Wilson-plus-staggered / K-real Case-A selected action surface.

It does not derive from the minimal axiom surface that every gauge action on
the `Z^3` spatial substrate forbids all CP-odd topological discretizations.
The single-plaquette exclusion, positive-class branch selection, scalar-mass
boundary, positive-mass convention, and K-real determinant-channel reading
retain their cited conditions. Downstream use must inherit them explicitly.

**Named conditional:** an ADMITTED CP-odd action term or complex mass phase
re-opens the strong-CP question; the supplied structure does not silently set
such admitted data to zero.

## Theorem

**Theorem (bounded selected-action-surface `θ_eff = 0` closure).**
On the bounded Wilson-plus-staggered / K-real Case-A selected action surface
constructed and tested by the runner, conditional on every load-bearing
dependency and condition in the table above,

    θ_eff = θ_QCD + arg det(M_u M_d) = 0

with no surviving loophole from:

1. fermion determinant / exact fermion-effective-action phase,
2. admissible axial or chiral basis rephasing inside the selected scalar-mass
   action class,
3. strong-sector phase generation when the fermions are integrated out, or
4. positive-weight topological-sector weighting away from `θ = 0`.

This is a **bounded selected-action-surface** closure theorem. It is not a
claim about every continuum formulation, every regulator, every possible
CP-odd discretization on the `Z^3` spatial substrate, or axion-model exclusion
beyond that selected surface.

## The Standard Strong CP Problem

In the Standard Model, the effective QCD vacuum angle is

    θ_eff = θ_QCD + arg det(M_u M_d)

where `θ_QCD` is the bare vacuum angle in the gluon action and
`arg det(M_u M_d)` is the phase of the quark-mass determinant. Both are
independent free parameters, generically `O(1)`, while experiment requires

    |θ_eff| < 10^-10

from the neutron electric dipole moment bound.

The question here is narrower and sharper: on the selected
Wilson-plus-staggered action surface on the `Z^3` spatial substrate, does any
strong-sector CP phase survive at all?

## Four Closure Legs

### Leg A: Fermion phase closure

The staggered Dirac operator `D[U]` on the selected lattice surface is
anti-Hermitian:

    D† = -D.

For real mass `m > 0`, the eigenvalues of `D+mI` occur as conjugate pairs
`m ± i λ`, so

    det(D+mI) = Π_k (m^2 + λ_k^2) > 0.

This already removes the usual fermion-determinant phase on the selected
surface. The runner checks the fermion side more strongly than before:

1. the `3+1` APBC staggered operator remains anti-Hermitian on sampled
   selected-surface `SU(3)` configurations,
2. `det(D+mI)` remains real positive there,
3. the exact fermion effective action is Gaussian,

       Γ_f = -Tr ln(D+m),

   so there are no higher fermion loops beyond that determinant, and
4. the sublattice generator `ε(x)=(-1)^{Σx}` gives `εD + Dε = 0`, forcing
   exact `±λ` pairing of the eigenvalues of `iD`, hence

       Im Γ_f = -Σ_k arctan(λ_k / m) = 0.

So the fermion phase is not merely small or sampled away. On the selected
surface it closes exactly, with the `3+1` APBC spectral audit serving as the
explicit verification layer.

### Leg B: Axial / chiral non-generation

The usual continuum loophole is an axial rotation that shifts phase between the
mass term and `θ_QCD`. On the selected staggered surface, the candidate axial
generator is the sublattice operator `ε`, and the admissible unitary transform
is

    U_α = exp(i α ε / 2).

Because `εD + Dε = 0`, the kinetic operator is invariant:

    U_α D U_α = D.

But the mass term rotates as

    U_α (mI) U_α = m (cos α I + i sin α ε).

Therefore:

1. only `α ∈ πZ` preserves a real mass operator,
2. any nontrivial continuous axial rotation introduces an imaginary
   pseudoscalar mass component,
3. that rotated mass operator is no longer a real scalar mass term, so it
   exits the selected Wilson-plus-staggered scalar-mass action class.

This closes the chiral/basis loophole on the selected surface. Within the
supplied scalar-mass action class, no continuous admissible axial freedom can
move phase between the mass term and a strong-sector `θ` while remaining in
that class.

### Leg C: Gauge-sector radiative non-generation

The runner constructs the bounded selected action surface by starting from a
candidate gauge slot `θ` and one scalar phase `α_f` per staggered flavor. It
then applies the bounded selectors in the dependency table before any closure
check. The background package inputs remain:

1. one-qubit operator algebra,
2. `Z^3` spatial substrate,
3. finite Grassmann / staggered-Dirac partition,
4. physical-lattice reading,
5. canonical normalization.

Canonical normalization fixes the Wilson gauge coupling at

    β = 6.

Within the authorities' stated conditions, the computed gauge branch is zero
and every convention-aligned positive-real mass representative has
`α_f = 0`. The resulting conditional action class is:

    S_sel[U, ψ, ψ̄] = S_Wilson[U] + ψ̄(D[U] + m)ψ

The absence of the reviewed CP-odd slot here is a computed result of the cited
conditional selectors. It is not a claim that every clover, multi-plaquette,
higher-trace, axion-coupled, or signed action is excluded.

Integrating out the fermions is exact on this surface:

    Z = ∫ DU det(D[U] + m) e^{-S_Wilson[U]}
      = ∫ DU exp(-S_eff[U]),

where

    S_eff[U] = S_Wilson[U] - ln det(D[U] + m).

Leg A already gives `det(D[U]+m) > 0`, so `ln det(D[U]+m)` is real. The
Wilson action is real and CP-even. Therefore `S_eff[U]` remains real and
strong-sector CP-even on the selected action surface.

The runner now checks this directly on sampled selected-surface `3+1`
configurations:

- `S_Wilson[U]` is real,
- the exact fermion effective action is real,
- the full selected-surface effective action is real,
- linkwise complex conjugation preserves the full selected-surface effective
  action.

This is the selected-surface version of radiative non-generation: exact
fermion integration does not generate a CP-odd strong-sector phase inside the
selected Wilson-plus-staggered action class.

### Leg D: Topological-sector positivity and the `θ = 0` minimum

Conditional on a supplied or separately derived integer-valued emergent sector
functional `Q` with populated support, the selected partition function can be
written formally as

    Z = Σ_Q Z_Q

with sector weights

    Z_Q = ∫_{Q[U]=Q} DU det(D[U] + m) e^{-S_Wilson[U]}.

Leg A and Leg C imply every selected-surface integrand factor is real and
positive, so

    Z_Q >= 0.

The `θ`-deformed partition is therefore

    Z(θ) = Σ_Q Z_Q e^{i θ Q}.

By the triangle inequality,

    |Z(θ)| <= Σ_Q Z_Q = Z(0),

so the selected-surface free energy

    F(θ) = -ln |Z(θ)|

is minimized at `θ = 0`.

This is the exact conditional sector-weight inequality needed here. It does
**not** derive the existence, integrality, nonvacuity, or susceptibility of an
emergent `Q`, and it does not require a closed-form first-principles expression
for the detailed lattice measure `Z_Q`. Positivity of the sector weights is
enough once that sector functional and populated support are supplied.

The runner mirrors this mechanism with a sampled selected-surface `3+1`
positive-weight clover-style `Q` proxy rather than a derived emergent `Q` or a
literal computed exact sector decomposition:

- sampled selected-surface positive weights are strictly positive,
- the sampled `θ`-sum obeys `|Z(θ)| <= Z(0)`,
- the sampled free energy is minimized at `θ = 0`.

## Relation to CKM CP Violation

Within this bounded selected-action-surface package, the explicit CP-violating datum
carried by the runner is the weak-sector CKM phase. The separate `Z_3` source
acts through the electroweak `1+2` split and produces

    δ_std = arctan(√5) = 65.905°.

The color `SU(3)` is the graph-first commutant of the selected weak `SU(2)`.
The `Z_3` source does not provide a continuous strong-sector `θ`; it remains a
discrete weak-sector source. The runner keeps the exact finite checks:

- selected-axis `su(2)` closure,
- joint commutant dimension `10 = gl(3) ⊕ gl(1)`,
- `Z_3` eigenvalues are discrete cube roots of unity,
- `|det V_CKM| = 1`,
- explicit positive-mass `arg det(M_u M_d) = 0`.

Thus the runner finds no CKM-to-`θ_eff` leakage on this bounded selected
surface. This does not exclude a strong-sector phase after admitting a CP-odd
action term or complex mass phase outside that surface.

## Combined Result

The four legs now close together:

1. no fermion phase survives,
2. no admissible axial rephasing can move phase into a strong-sector `θ`,
3. exact fermion integration leaves the selected-surface effective action real and
   CP-even,
4. positive topological-sector weights force the free-energy minimum to
   `θ = 0`.

Therefore, on the bounded Wilson-plus-staggered / K-real Case-A selected
action surface,

    θ_bare = 0,
    arg det(M_u M_d) = 0,
    θ_eff = 0.

This is a **bounded selected-action-surface strong-CP closure package**.

## What Is Actually Proved

### Exact theorem-grade statements

1. the selected action class has 5 explicit inputs,
2. canonical normalization fixes the Wilson gauge coupling at `β = 6`,
3. `ε^2 = I`,
4. `U_α = exp(i α ε/2)` is unitary,
5. `U_α D U_α = D`,
6. `U_α (mI) U_α = m(cos α I + i sin α ε)`,
7. only `α ∈ πZ` preserves a real mass operator on the selected action class,
8. the selected-axis weak `su(2)` closes exactly,
9. the joint commutant has dimension `10 = gl(3) ⊕ gl(1)`,
10. the `Z_3` weak-sector source does not commute with the selected-axis
    `SU(2)`,
11. `Z_3` has only discrete cube-root eigenvalues,
12. `|det V_CKM| = 1`,
13. positive selected-surface sector weights imply `|Z(θ)| <= Z(0)`, hence
    `F(θ)` is minimized at `θ = 0`.

### Cited conditional selection statements re-verified by the runner

1. a multiplicative orientation-even theta character on odd support collapses
   to `{0, π}`;
2. strictly positive weights on odd support exclude `π` and select the zero
   branch;
3. an exact positive native-history pushforward with gcd-one populated support
   likewise leaves only the zero relative branch;
4. the reviewed single-plaquette CP-odd Wilson slot is rejected on the
   canonical real-positive P1-P5 surface;
5. operator-basis reality reduces each scalar mass phase to `{0, π}`;
6. exact K-real `±iλ` pairing makes the determinant non-negative for both real
   mass signs on the supplied Case-A surface, with zero phase only on the
   nonzero-determinant locus; and
7. the convention-aligned positive-real representative is `α_f = 0` for every
   constructed flavor slot.

The runner also admits one nonzero gauge theta probe and one nonzero complex
mass-phase probe as data. Each check passes only by detecting the out-of-surface
datum and printing the named conditional; neither probe is silently replaced
by zero.

### Selected-surface compute checks

1. exact toy-scale construction of the candidate gauge and per-flavor mass
   slots,
2. exact algebraic Z2 collapse, positive-class zero-branch selection, and native
   positive pushforward selection,
3. exact operator-basis reality, K-real pairing, and positive-real
   representative selection,
4. detection and naming of deliberately admitted nonzero gauge and mass-phase
   data,
5. free-field and gauged `Z^3` staggered determinant positivity,
6. `3+1` APBC determinant positivity on sampled selected-surface `SU(3)`
   configurations,
7. sampled nontrivial clover-style topological-charge proxy without determinant
   phase generation,
8. `εD + Dε = 0` on the selected `3+1` APBC surface,
9. sampled exact `±λ` pairing of `iD`,
10. sampled `Im Γ_f = 0`,
11. sampled agreement between the spectral phase and the determinant phase,
12. sampled axial-grid audit matches the exact statement that only `α ∈ πZ`
   preserves a real mass operator,
13. explicit nontrivial axial rotation exits the selected scalar-mass action
   class,
14. the only admissible selected-surface axial endpoints keep zero determinant
    phase,
15. the constructed positive-mass quark surface gives
    `arg det(M_u M_d)=0`,
16. sampled selected-surface effective action is real,
17. linkwise complex conjugation preserves the full selected-surface effective
    action,
18. sampled selected-surface positive-weight `Q`-proxy family obeys
    `|Z(θ)| <= Z(0)`,
19. the sampled selected-surface free energy is minimized at `θ = 0`.

### Support only

1. Vafa-Witten sign-discipline consistency,
2. the statement that a detailed closed-form `Z_Q` measure is unnecessary for
   the selected-surface `θ = 0` minimum theorem.

These support items are not counted as theorem-grade closure.

## What Is Not Claimed

1. **Unrestricted all-formulations closure.**
   The theorem is only about the bounded Wilson-plus-staggered / K-real Case-A
   selected action surface on the `Z^3` spatial substrate, with every cited
   condition inherited.

2. **Emergent-`Q` existence or a closed-form `Z_Q` measure.**
   The conditional closure uses positivity and the `θ`-sum bound after an
   integer-valued sector functional with populated support is supplied; it does
   not derive that functional, its nonvacuity or susceptibility, or a
   closed-form instanton measure.

3. **Axion exclusion beyond the selected action surface.**
   The theorem does not exclude axion models or other regulators outside the
   selected surface.

4. **Observable neutron-EDM matrix elements.**
   The surviving observable lane is the separate CKM neutron-EDM corollary /
   bounded-prediction note: the exact corollary `d_n(QCD) = 0` and
   CKM-only structure are bounded consequences only when this selected-surface
   theorem and the relevant CKM package premises are both admitted, while
   the numerical `d_n(CKM)` scale remains EFT-bridged.

5. **Closure after admitting excluded data.**
   An admitted CP-odd action term, including an unreviewed topological slot, or
   an admitted complex mass phase re-opens the question. The runner detects
   those inputs; it does not remove them by definition.

## How This Changes The Paper

The strong-CP lane has a bounded selected-action-surface closure package:

- fermion phase closure,
- axial/chiral non-generation,
- gauge-sector radiative non-generation inside the selected action class,
- topological-sector positivity with the `θ = 0` minimum.

The safe paper sentence is:

> Conditional on the cited canonical positive gauge class, its character and
> support hypotheses, and the supplied scalar-mass / K-real Case-A
> determinant-channel conditions, the runner constructs the zero-branch action
> surface and finds no additional generated strong-sector phase: the
> determinant phase vanishes, admissible axial rotations do not move phase into
> `θ`, exact fermion integration stays real, and, conditional on a supplied
> populated integer-sector functional, positive sampled proxy weights place the
> selected-surface free-energy minimum at `θ = 0`.

## Experimental Predictions

1. **`θ_eff = 0` exactly on the bounded selected action surface, conditional on
   all cited surface and channel conditions.**
2. **`d_n(QCD) = 0` on that selected surface, conditional on the same surface
   premises.**
   The surviving observable neutron-EDM estimate is the separate CKM-only
   corollary / bounded quantitative lane, currently
   `d_n(CKM) ~ 8 x 10^-33 e cm`.
3. **Any observed strong-sector CP phase requires structure beyond the selected
   action surface.**

## References

- Vafa, C. and Witten, E. (1984). *Restrictions on Symmetry Breaking in
  Vector-Like Gauge Theories*, PRL 53, 535.
- Leutwyler, H. and Smilga, A. (1992). *Spectrum of Dirac operator and role of
  winding number in QCD*, PRD 46, 5607.
- Witten, E. (1979). *Current algebra theorems for the U(1) Goldstone boson*,
  Nucl. Phys. B 156, 269.
- Veneziano, G. (1979). *U(1) without instantons*, Nucl. Phys. B 159, 213.

## Commands Run

```bash
python3 scripts/frontier_strong_cp_theta_zero.py
# Exit code: 0
# THEOREM PASS=13  FAIL=0
# SELECTED-SURFACE COMPUTE PASS=42  FAIL=0
# SUPPORT=4
# TOTAL PASS=55  FAIL=0
```

## Historical audit boundary (2026-04-28)

Audit verdict (`audited_conditional`, high criticality, 124 transitive
descendants):

> Issue: the decisive step is not a computed strong-CP cancellation
> but the retained-action-surface selection: the runner/support text
> takes 'no bare θ slot' and `θ_bare = 0` from the action-class
> definition, and it uses an explicit positive real quark-mass
> surface for `arg det(M_u M_d) = 0`. Why this blocks: the 13
> theorem and 30 retained-surface compute passes show internal
> consistency of that restricted θ-free Wilson-plus-staggered
> scalar-mass surface, but they do not derive from the provided
> audit packet that the physical Cl(3)/Z^3 action forbids an
> allowed CP-odd F̃F term, fixes the real-mass orientation, or
> dynamically selects θ = 0 rather than merely evaluating the
> θ-free surface.

> Claim boundary until fixed: it is safe to claim that on the
> explicitly θ-free Wilson-plus-staggered scalar-mass surface, the
> implemented determinant, axial-grid, effective-action, and sampled
> positive-weight checks find no generated strong-sector phase; it
> is not yet an audited solution of strong CP beyond that selected
> action surface.

The 2026-07-12 repair responds to that historical wiring defect by citing the
four bounded selection authorities and constructing the conditional basis in
the runner. This source note does not set or predict the resulting audit
status.

## Remaining conditional boundary

1. Gauge-side exclusion is no broader than the cited authorities: the
   single-plaquette Wilson-slot theorem requires P1-P5; the character theorem
   requires character form, orientation-evenness, odd support, and
   positive-class membership; and the native theorem remains inside the
   canonical imported Wilson + staggered-Wilson positive class while leaving
   Q-structure existence and nonvacuity open.
2. Mass-side selection retains the supplied scalar-mass boundary, the
   convention-aligned positive representative, and the K-real Case-A
   determinant-channel identification. The K-real pairing theorem makes the
   determinant non-negative for both real signs and fixes its phase only on the
   nonzero-determinant locus; it does not independently derive the positive
   sign. The runner's selected positive nonzero masses lie on that locus.
3. An ADMITTED CP-odd action term or complex mass phase is outside the
   constructed selected surface and re-opens the strong-CP question. A choice
   to admit such data is not fixed by the supplied structure and remains a
   named conditional or open dependency.
