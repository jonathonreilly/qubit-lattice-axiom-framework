# Koide: the qubit-factor Berry holonomy is import-sourced and r-non-selective

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** source-side bounded localization: an exact finite-dimensional
probe of the qubit-factor Berry route, not a `Q=2/3` closure.
**Status:** source proposal. Approves no axiom, primitive, or import; sets no
status verdict.
**Primary runner:**
`scripts/frontier_koide_qubit_berry_holonomy_import_2026_05_30.py`.

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
[`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
wall). The
equivariant-`eta`/spectral-asymmetry route named exactly one dodge: tensor with the
**native qubit `C^2`** from the Quantum baseline. There the C₃-equivariant anticommutant of
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
Lattice + Quantum + Record baseline or current sourced inventory) in radian form — it
does **not** supply it. The broader Koide package carries `Q=2/3` through separate
inputs; this result shows the qubit-factor Berry holonomy is not its native source.

**Boundary honesty.** The runner directly reproduces the bare-tensor wall
(`B (x) I2` anticommutant `= 0`) and bare-`R^3` flatness on this seam. The dynamical /
Berry spine (`koide_berry_phase_theorem`, `koide_berry_bundle_obstruction`,
`koide_z3_qubit_radian_bridge_no_go`) is context only; this Berry-route reasoning
does not inherit its status from those names.

**The next open path** (a distinct program, not foreclosed here): does the framework baseline force a
**nontrivial qubit `Z_3` / chiral action** that partially breaks the qubit-`SU(2)`
frame symmetry and canonically selects the relative axis (`-> ` would make the import
native)? It is not supplied here and would need its own derivation or an explicitly
approved input. A parallel path is the `sqrt(m)`-sign / readout-class datum (signed-eigenvalue
`det_R` vs singular-value Yukawa), which may be the unforced datum that is actually
fixable, distinct from `r=1/2` itself.

## No-Go Discipline Gate (N1-N8)

This gate scopes only the negative/localization component: the tested
qubit-factor Berry route for the `delta = arg(b)` loop does not natively supply
the missing `omega` / `r=1/2` / `Q=2/3` input.

### N1 - Alternative Route Enumeration

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Faithful fixed-coin embedding | Map `arg(b)` faithfully as `(cos d B + sin d iJcs) (x) s` for a fixed qubit axis `s`. | The Fourier-mode qubit blocks are planar; Wilson, Uhlmann, and lower-band checks give zero holonomy. | ATTEMPTED |
| Different fixed qubit axis | Pick `sigma_x` or `sigma_y` instead of `sigma_z`. | F1 shows the three axes have equal anticommutant dimension and are qubit-`SU(2)` related; no axis is canonical, and a fixed-axis faithful image remains the same planar case up to rotation. | ATTEMPTED |
| Non-collinear coin | Use `B (x) (cos d sigma_z + sin d sigma_y)` to get a nonzero Berry phase. | This is nonzero, but `B (x) sigma_y` is Hilbert-Schmidt orthogonal to the faithful `(iJcs) (x) *` sector; it is an inserted chiral coin, not the faithful `arg(b)` image. | ATTEMPTED |
| Imported coin selects `r=1/2` | Grant the non-collinear coin and ask whether its holonomy pins the Koide value. | `Gamma(r) = -pi(1 - 1/sqrt(1+4r))` is smooth and monotone; it is not stationary at `r=1/2`, and the `2/9` targets occur at other `r`. | ATTEMPTED |
| Equivariant-eta replacement | Use the eta/spectral-asymmetry route to force the needed chiral coin. | The companion eta note shows eta is silent on the tensor-coin sector where breaking becomes possible; it names this Berry route but does not supply the missing chiral action. | RULED OUT BY PRIOR |
| Off-generation chiral source | Source a chiral/nonzero-Berry coupling from a factor distinct from generation `R^3`. | This is outside this note's scope and remains open; the claim is only about the tested qubit-factor `arg(b)` route. | OUT OF SCOPE |

### N2 - Wall-Independence Audit

The scoped claim has three route-specific facts, not three independent global
walls: the faithful image is zero; the nonzero construction uses an inserted
chiral coin; and the inserted coin is still `r`-non-selective. Closing only one
does not close the others, but the note does not inflate them into a broad
no-go against every off-generation chiral source.

### N3 - Hidden-Wall Scan

The proof does not assume that the Lattice + Quantum + Record baseline supplies
a chiral qubit coin, a Kähler form, a signed readout, or the `r=1/2` value. The
non-collinear coin is explicitly classified as an inserted input, and the
`2/9` and `r=1/2` values are used only as comparator targets in F4.

### N4 - Residual Matching

| cited source | residual attacked | residual here | match? |
|---|---|---|---|
| [`FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30`](FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30.md) | Eta is silent on the tensor-coin sector and therefore does not force the chiral action. | This note tests the named Berry replacement on that tensor-coin sector. | yes |
| [`FLAVOR_QUBIT_BERRY_HOLONOMY_PROBE_NOTE_2026-05-30`](FLAVOR_QUBIT_BERRY_HOLONOMY_PROBE_NOTE_2026-05-30.md) | A simpler qubit Berry construction does not derive `2/9` or select `r=1/2`. | This note sharpens the result by separating faithful zero holonomy from non-collinear imported holonomy. | yes |
| [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31`](KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md) | Native circulant mass is zero-Berry; the positive route requires a chiral/nonzero-Berry criterion. | This note checks that the qubit-factor `arg(b)` seam does not supply that criterion natively. | yes |

### N5 - Rhetoric Audit

Phrases such as "import-sourced", "r-non-selective", and "does not natively
source" apply only to the tested qubit-factor Berry route. They do not claim
that all future off-generation chiral mechanisms are impossible.

### N6 - Partial-Closure Path Scan

Open paths remain: derive a nontrivial qubit `Z_3` / chiral action from the
framework baseline, add an explicitly approved chiral input, or close the
signed-readout route independently. None is declared a new axiom here.

### N7 - Steelman

A hostile reviewer could argue that the non-collinear coin is exactly what an
unwritten matter-action theorem should generate on the qubit factor, so the
right conclusion is not "Berry fails" but "Berry identifies the missing action
term." That objection is correct as an open program and is why the note preserves
the off-generation/chiral-source path. It does not break the scoped claim,
because the tested faithful `arg(b)` image has zero holonomy and the nonzero
coin is not derived inside this note.

### N8 - Cross-Cycle Echo

Prior Koide/2-over-9 routes overreached when a successful mathematical object
was treated as a physical selector without the carrier/readout bridge. This note
avoids that echo: the nonzero Berry object is recorded as a useful localization
of the missing chiral input, not as a closure of `Q=2/3`.

## Anchors (context, not status claims)

[`koide_z3_equivariant_anticommuting_no_go`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[`koide_anticommuting_operator_derivation`](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md),
[`koide_circulant_q_two_thirds_algebraic`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
[`site_phase_cube_shift_intertwiner`](SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md),
[`cpt_exact_real_anti_hermitian_d`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
[`koide_berry_phase_theorem`](KOIDE_BERRY_PHASE_THEOREM_NOTE_2026-04-19.md),
[`koide_berry_bundle_obstruction`](KOIDE_BERRY_BUNDLE_OBSTRUCTION_THEOREM_NOTE_2026-04-19.md),
[`koide_z3_qubit_radian_bridge_no_go`](KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md), and
[`flavor_equivariant_eta_complementarity`](FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30.md).
