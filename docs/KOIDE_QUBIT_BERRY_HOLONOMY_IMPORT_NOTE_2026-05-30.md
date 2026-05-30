# Koide: the qubit-factor Berry holonomy is import-sourced and r-non-selective

**Date:** 2026-05-30
**Claim type:** bounded structural localization / narrow no-go (negative, positive content)
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the Hermitian-vs-Kähler convention tier.
**Primary runner:**
`scripts/frontier_koide_qubit_berry_holonomy_import_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_qubit_berry_holonomy_import_2026_05_30.txt`.

## Result (one sentence)

The one open seam for sourcing the missing symplectic form `omega` (and hence
`r=1/2`, `Q=2/3`) on the native qubit factor — the qubit-factor Berry holonomy of
the `delta=arg(b)` loop on `R^3 (x) C^2`, where the equivariant `eta`-index is blind
— is **zero for the faithful embedding**, **nonzero only via an imported
non-collinear chiral coin**, and **r-non-selective even then**: it does **not**
natively source `omega`/`r=1/2`/`Q=2/3`.

## Why this seam was the live candidate

The charged-lepton value `Q=2/3 <=> r=|b|^2/a^2 = 1/2` reduces to whether the native
generation matter geometry is Kähler (`omega` present `->` count 1 `->` `Q=2/3`) or only
Hermitian (`omega` absent `->` count 2 `->` `Q=1`) — see the static
`Hermitian-not-Kähler` localization. On the **bare** generation `R^3` factor `omega`
is forced-absent: the C₃-equivariant mass operator
`Hgen(a,br,bi) = a I + br B + bi (i Jcs)` is circulant for all `(br,bi)`, hence
simultaneously diagonal in the **b-independent** C₃-Fourier basis, so the Berry
curvature over the complex-`b` plane vanishes (the
`koide_z3_equivariant_anticommuting_no_go` wall, retained_bounded). The
equivariant-`eta`/spectral-asymmetry route named exactly one dodge: tensor with the
**native qubit `C^2`** (axiom A1). There the C₃-equivariant anticommutant of
`B (x) sigma_z` is **dim 6** (vs **dim 0** for `B (x) I2`), so a Berry phase can be
nonzero precisely where the `eta`-index is blind (the tensor-coin spectrum is
`±`-symmetric `-> eta = 0`). A Berry phase is natively radian-valued, so it was the
one object that could simultaneously source the odd term on the auxiliary factor and
collapse the dimensionless-weight `-> ` radian-phase wall.

## The computation (runner, from scratch; gauge-invariant, three-method)

**F1 — `sigma_z` is unprivileged.** The C₃-equivariant anticommutant
`{X : {X, B(x)s}=0, [X, C(x)I2]=0}` has complex dimension **0** for `s=I2` and **6**
for **each** of `s=sigma_x, sigma_y, sigma_z`. The three are related by qubit-`SU(2)`
rotations `I3 (x) U` (which commute with the generation action `C (x) I2`), so no qubit
axis is canonically selected.

**F2 — faithful embedding `-> ` Berry = 0 EXACTLY.** The faithful image of
`b = |b| e^{i delta}` is `M(delta) = (cos d * B + sin d * (i Jcs)) (x) sigma_z`
(any single fixed coin axis), with coin term `t I3 (x) sigma_x`. Because `B` and
`i Jcs` are circulant and commute, in each Fourier mode the qubit block has
`sigma_y` component **identically 0** (`max|d_y| = 0`): the loop is **planar**, sweeps
zero solid angle. Every gapped Fourier-mode lower-band Berry phase is `0`, and the
non-abelian (Wilczek-Zee) holonomy on the isolated lower-3-band subspace (gap to
upper `= 2t`) is trivial (det-phase `0`). The bare-`R^3` circulant flatness **persists
verbatim into the tensor seam**, even where the `eta`-index is blind.

**F3 — nonzero requires an IMPORT.** A nonzero, robustly-gapped holonomy appears only
for the **non-collinear** coin `B (x) (cos d * sigma_z + sin d * sigma_y)`. But
`B (x) sigma_y` is Hilbert-Schmidt **orthogonal** to the entire `(i Jcs) (x) *`
sector (`max overlap = 0`), so the `sin d * sigma_y` term is **not** the faithful
image of `arg(b)` — it is the C₃-orbit-splitting chiral grading inserted by hand
(`Escape Hatch II`). The operative ingredient is the **inter-axis relative `i`**
between two non-commuting qubit couplings (breaking the qubit-`SU(2)` frame symmetry),
not `sigma_z` per se. Its lowest-band holonomy is
`Gamma(r) = -pi (1 - 1/sqrt(1 + 4r))` (Wilson-loop and Uhlmann agree to `1e-6`).

**F4 — the import is r-NON-SELECTIVE.** `Gamma(r)` is smooth and strictly monotone:
`dGamma/dr = -1.21 != 0` at `r=1/2` (no stationarity, no quantization, no kink). It
attains `|Gamma| = 2/9` rad at `r ~ 0.0395`, `2pi/9` at `r ~ 0.163`, and the clean
`-2pi/3` at `r = 2` — **never** at the value point `r = 1/2` (where
`Gamma = -pi(1 - 1/sqrt3)`, an irrational multiple of `pi`). The `r=1/2` / `2/9` values
are **never** smuggled in; only the holonomy's existence is, and that existence is
import-sourced.

## Boundary

This is **not** a closure of the `Q=2/3` question. It maps **where** the
`r=1/2`-selecting principle is missing: the qubit-factor Berry route re-expresses the
**single chiral import** shared with Koide-`Q` and generation-identification (a
C₃-orbit-splitting qubit grading / the inter-axis relative `i`, which is **not** in the
`A1+A2+`retained inventory) in radian form — it does **not** supply it. The framework
reproduces `Q=2/3` to `<0.05%`, so the true matter action carries `omega`; this result
shows the qubit-factor Berry holonomy is not its native source.

**Tier honesty.** The bare-tensor wall (`B (x) I2` anticommutant `= 0`) and the
bare-`R^3` flatness are retained_bounded and reproduced exactly here. The dynamical /
Berry spine on the live ledger (`koide_berry_phase_theorem`,
`koide_berry_bundle_obstruction`, `koide_z3_qubit_radian_bridge_no_go`) is **unaudited**;
this Berry-route reasoning does not carry retained weight until audited. This result
extends the unaudited `koide_berry_phase_theorem`'s "the Berry connection is zero on
the retained charged-lepton circulant moduli" to the `R^3 (x) C^2` coin seam.

**The next open path** (a distinct program, not foreclosed here): does `A1+A2` force a
**nontrivial qubit `Z_3` / chiral action** that partially breaks the qubit-`SU(2)`
frame symmetry and canonically selects the relative axis (`-> ` would make the import
native)? It is not in the retained inventory and would need its own derivation from
`A1+A2`. A parallel path is the `sqrt(m)`-sign / readout-class datum (signed-eigenvalue
`det_R` vs singular-value Yukawa), which may be the unforced datum that is actually
fixable, distinct from `r=1/2` itself.

## Anchors (live-ledger tiers)

retained / retained_bounded: `koide_z3_equivariant_anticommuting_no_go`,
`koide_anticommuting_operator_derivation`, `koide_circulant_q_two_thirds_algebraic`,
`site_phase_cube_shift_intertwiner`, `cpt_exact_real_anti_hermitian_d`. Unaudited
(named for context, not load-bearing): `koide_berry_phase_theorem`,
`koide_berry_bundle_obstruction`, `koide_z3_qubit_radian_bridge_no_go`,
`flavor_equivariant_eta_complementarity`.
