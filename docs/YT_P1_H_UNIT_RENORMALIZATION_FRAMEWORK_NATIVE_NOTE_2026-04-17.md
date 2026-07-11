# P1 H_unit 1-Loop Renormalization: Framework-Native IR Diagnostic

**Date:** 2026-04-17 (re-authored as an infrared diagnostic)

This note documents the framework-native 1-loop renormalization of the
composite-scalar bilinear `H_unit = (1/√6) Σ_{α,a} ψ̄_{α,a} ψ_{α,a}` on
the `Cl(3) × Z^3` Wilson-plaquette + 1-link staggered-Dirac canonical
surface. It carries the symbolic diagram/Feynman-rule reduction of the
`C_F` channel to the single gluon-sandwich stand-in `D_S1`, and then
**certifies an infrared obstruction**: the displayed zero-external-momentum
scalar kernel is not integrable at the Brillouin-zone origin, so the
displayed reduction does not by itself deliver a finite matching
coefficient. The obstruction is stated through structural constants only
(the small-momentum ray slope, the halving factor, the leading
coefficient, and the quadratic growth of the origin-ball integral), with
no external numerical target.

## What earlier drafts claimed and this revision withdraws

An earlier draft of this note carried a numerical **envelope bound** and a
consistency argument. Those are withdrawn here, for the reasons the
diagnostic below makes explicit:

1. **Envelope bound withdrawn.** The earlier "`|I_S^{framework}| ≤ …`"
   magnitude bound was constructed as `16 · (1 − 1/⟨P⟩)^{-1}` from an
   imported plaquette average. A max-integrand × BZ-volume envelope does
   not exist for this kernel: the integrand's supremum over the zone is
   `+∞` (§4.3), so no finite envelope brackets it. The bound is retracted.
2. **External comparator withdrawn.** The earlier draft compared the
   would-be value to an externally cited bracket and reported a
   fraction-of-envelope figure. The cited bracket belongs to the
   comparator class `imported_literature_series` and is not a
   framework-native derivation input; the comparison and the fraction are
   retracted. No external numeric appears in this note.
3. **Lower "continuum floor" withdrawn.** The earlier `I_S ≥ 2·(1 − u_0)`
   floor depended on the same imported constants and is retracted.
4. **"External-leg `Z_q` cancellation" withdrawn.** The earlier draft
   asserted that the two external-leg self-energy diagrams are absorbed so
   that the amplitude reduces to a single diagram with nothing left over.
   That absorption is an assembly *convention*, not a computed
   cancellation; the independent external-leg `Z_q` is **currently
   omitted** from the displayed kernel (§2.2). The clean-cancellation
   claim is retracted.
5. **Three-piece "bounded reduction" framing withdrawn.** The earlier
   `I_S^{framework} = I_S^{tadpole} + I_S^{log} + I_S^{fin}` split, with a
   log-coefficient asserted "exactly 1", is retracted as a *derivation of
   a finite coefficient*. The displayed scalar kernel is preserved below
   only as a historical stand-in (a pseudo-kernel under stress test), and
   it hits the quadratic IR obstruction of §4 rather than yielding a
   finite residue.

Consistent with points 1–3, the two dependency edges that existed only to
supply those imported constants — the plaquette self-consistency note and
`scripts/canonical_plaquette_surface.py` — are demoted from links to
backticked context mentions below (the paired runner likewise carries no
import from that module). The structural edges that support the kept
kernel, tree anchor, and axiom foundation are preserved.

## Historical cross-references (dependency pointers; no numeric import)

The following are preserved as neutral pointers to the surrounding P1
chain. This diagnostic imports **no** numerical value from any of them.

- **Master obstruction context:** `YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md`.
- **Color-tensor decomposition:** `YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md`
  — `Δ_R = C_F · I_1 + C_A · I_2 + T_F n_f · I_3`.
- **Fierz sub-theorem:** `YT_P1_SHARED_FIERZ_NO_GO_SUB_THEOREM_NOTE_2026-04-17.md`
  — no algebraic shortcut between `I_1`, `I_2`, `I_3`.
- **Conserved-current reduction:** [`scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`](../scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py)
  — `I_V = 0` giving `I_1 = I_S`; source of the displayed lattice Feynman rules.
- **Prior citation / verification context:** `YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md`,
  `YT_P1_I_S_REVISION_VERIFICATION_NOTE_2026-04-17.md` — external comparator
  material; not an input here.
- **Loop-tail context:** `YT_P1_LOOP_GEOMETRIC_BOUND_NOTE_2026-04-17.md`.
- **Vertex power:** [`docs/YT_VERTEX_POWER_DERIVATION.md`](YT_VERTEX_POWER_DERIVATION.md)
  — `n_link = 1` per single vertex (D15).
- **Ward / action authorities:** [`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  (`H_unit = (1/√6) Σ ψ̄ ψ` on `Q_L`);
  [`docs/MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
  (Wilson-plaquette + staggered-Dirac action).
- **Demoted context (formerly linked; imported constants withdrawn):**
  `docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md`, `scripts/canonical_plaquette_surface.py`.

---

## Abstract — the infrared diagnostic

On the framework's `Cl(3) × Z^3` canonical surface, the `C_F`-channel
1-loop renormalization of `H_unit` reduces symbolically to a single
gluon-sandwich diagram `D_S1`, whose zero-external-momentum scalar
stand-in kernel is

```
    K(k)  =  N_S(k) · [ D_ψ(k)^{-1} ]^2 · D_g(k)^{-1}
```

with the framework's lattice forms (§1.2)

```
    D_ψ(k)  =  Σ_μ sin²(k_μ)                       (staggered fermion)
    D_g(k)  =  4 Σ_ρ sin²(k_ρ / 2)                 (Wilson plaquette gluon)
    N_S(k)  =  Σ_μ cos²(k_μ / 2)                    (scalar-bilinear numerator)
```

At small momentum `k = r·q̂` (unit direction `q̂`, `r = |k| → 0`),

```
    D_ψ(k) → r²,     D_g(k) → r²,     N_S(k) → 4,
    K(k)   → 4 · r^{-6}.
```

The four-dimensional measure factorizes as `d^4k = r³ dr dΩ_3` with the
unit-3-sphere area `|S^3| = 2π²`. The origin-ball integral therefore
behaves as

```
    J(ε; R)  =  ∫_ε^R r³ · ⟨K⟩_{S^3}(r) · |S^3| dr
             ≈  8π² ∫_ε^R r^{-3} dr
             =  4π² ( ε^{-2} − R^{-2} )   →   4π² · ε^{-2}   as ε → 0,
```

a **quadratic** infrared divergence (integrand degree `6`, spatial
dimension `4`, so `6 − 4 = 2`). Equivalently, halving the inner cutoff `ε`
multiplies `J` by `4 = 2²`, and `ε² · J(ε; R) → 4π² ≈ 39.478`.

Because `K(k) → +∞` as `k → 0`, the supremum of the integrand over the
zone is unbounded: there is **no** finite "maximum-integrand × BZ-volume"
envelope for this kernel. The displayed scalar reduction, taken by itself,
does not deliver a finite matching coefficient. What the reduction is
missing — a full staggered-vertex/gauge-tensor contraction, an independent
external-leg `Z_q` with a specified assembly convention, and a specified
tadpole-subtraction prescription — is set out in §5 as the paths this
diagnostic opens.

Note on the numerator. An earlier draft wrote the numerator inconsistently
(with and without a stray overall factor of `4`, and once with an
incorrect continuum limit `→ 1`). The framework-native form is
`N_S(k) = Σ_μ cos²(k_μ / 2)`, whose small-momentum limit is
`N_S → 4` (four unit terms), fixing the leading coefficient of `r^6 K(k)`
to `4`. The historical amplitude also carried an overall `16π² · C_F`
normalization; that is an overall constant and does not affect any
power-law or divergence statement in this note (the paired runner works
with the normalization-stripped `K` above).

---

## 1. Framework-native foundations

### 1.1 Canonical action

From the framework's canonical action (Wilson plaquette + 1-link
staggered Dirac; `docs/MINIMAL_AXIOMS_2026-04-11.md` and the derivation
chain D1–D17):

```
    S[ψ, ψ̄, U]  =  S_staggered[ψ, ψ̄, U]  +  S_Wilson[U]
    S_staggered  =  Σ_x  ψ̄_x · [ Σ_μ η_μ(x) / (2 a) · ( U_{x,μ} ψ_{x+μ̂}
                                    − U†_{x−μ̂,μ} ψ_{x−μ̂} ) ]
    S_Wilson     =  β · Σ_plaq  ( 1 − (1/N_c) · Re Tr[U_plaq] )
    η_μ(x)       =  (-1)^{Σ_{ν<μ} x_ν}                (staggered sign; D2)
    β            =  2 N_c / g_bare²                    (canonical surface, D13)
```

The staggered η-phases carry the `Cl(3)` action in taste space (D4), the
SU(2) weak structure (D5), and — through the graph-first selector on
taste-cube complementary axes — the `su(3)` color structure (D6–D7). No
numerical value of the plaquette average, mean link, or coupling is used
in this note.

### 1.2 Lattice Feynman rules

From [`scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`](../scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py)
(Block 1), the framework's lattice propagators and scalar-bilinear
numerator are, in lattice units (`a = 1`):

```
    D_ψ(k)  =  Σ_μ sin²(k_μ)                    (staggered fermion)        (FR1)
    D_g(k)  =  4 Σ_ρ sin²(k_ρ / 2)             (Wilson plaquette gluon)   (FR2)
    N_S(k)  =  Σ_μ cos²(k_μ / 2)               (scalar-bilinear numerator)(FR3)
```

Small-momentum limits: `D_ψ(k) → |k|²`, `D_g(k) → |k|²`, `N_S(k) → 4`.
Both propagators reduce to the continuum `k²` at small momentum, as
required. These are the forms used throughout the diagnostic and in the
paired runner.

### 1.3 The composite operator and tree anchor

From [`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
(T1, T2), the composite scalar `H_unit = (1/√6) Σ_{α,a} ψ̄_{α,a} ψ_{α,a}`
is the unique unit-norm `(1,1)` singlet on the `Q_L` block, with the
tree-level anchor

```
    <0 | H_unit | tt̄ >^{(0)}  =  1 / √6                                    (WT)
```

The 1-loop renormalization constant `Z_S` is defined by
`<0 | H_unit | tt̄ >^{ren} = Z_S(μ = 1/a) · (1/√6)`; the diagnostic below
concerns the `C_F`-channel contribution to `Z_S`.

---

## 2. 1-loop diagrams and the currently-omitted external leg

### 2.1 Diagram topologies

From [`scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`](../scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py)
(Block 2), the `C_F`-channel 1-loop topologies contributing to
`<0 | H_unit | tt̄>` are three:

```
    D_S1  :  gluon sandwich       — gluon line connecting the two legs
                                     of H_unit inside the blob
    D_S2  :  left-leg self-energy  — 1PI gluon self-energy on the incoming
                                      fermion line
    D_S3  :  right-leg self-energy — 1PI gluon self-energy on the outgoing
                                      fermion line
```

`D_S2` and `D_S3` are mirror-symmetric under charge-conjugation × parity
on the amputated 2-point function (Block 2); their contributions to the
external-leg factor are equal.

### 2.2 Assembly convention and the currently-omitted external-leg Z_q

Assembling the renormalization constant from the vertex diagram and the
external-leg factor is a *convention*, not a computed cancellation. Write
the vertex coefficient of `D_S1` as `v_{D_S1}` and the external-leg
coefficient as `z_q`; to one loop the assembled constant is

```
    Z_S^{total}  =  Z_S^{D_S1} · Z_q^{-1}
                 =  1  +  g² ( v_{D_S1} − z_q )  +  O(g⁴)                  (A1)
```

so that the assembled result depends on **both** `v_{D_S1}` and the
external-leg coefficient `z_q`. The independent external-leg `Z_q` — the
quantity carrying `z_q` — is **currently omitted** from the displayed
scalar kernel of §3: that kernel carries the `D_S1` vertex structure only.
An earlier draft asserted that the external-leg self-energies are absorbed
so that nothing remains beyond a single diagram; that clean absorption is
withdrawn. Computing the assembled `Z_S^{total}` requires an independent
determination of the **external-leg `Z_q`** together with a specified
assembly convention (§5).

---

## 3. The `D_S1` scalar stand-in kernel (historical, under stress test)

The formula displayed here is preserved from the earlier draft as a
**historical stand-in** for the `D_S1` contribution — a pseudo-kernel
whose infrared behaviour §4 stress-tests. It is **not** a derivation of a
finite matching coefficient, and it is not the full staggered-taste +
gauge-tensor vertex contraction (§5).

### 3.1 Kernel structure

After amputation at zero external momentum (`p = 0`), the displayed
`D_S1` stand-in is

```
    I_S^{D_S1}(p=0)  =  16 π² · ∫_{BZ} d^4k / (2π)^4
                         · N_S(k)
                         · [ D_ψ(k)^{-1} ]^2
                         · D_g(k)^{-1}
                         · C_F                                            (R6)
```

with `D_ψ(k)`, `D_g(k)`, `N_S(k)` the framework forms (FR1–FR3) and
`C_F = (N_c² − 1) / (2 N_c)` the group-theory color Casimir (from D7 + D12;
a framework-native constant, not an import). The overall `16 π² · C_F` is
an overall normalization and does not affect the power-law or divergence
statements of §4; the normalization-stripped kernel
`K(k) = N_S(k) · [D_ψ(k)]^{-2} · D_g(k)^{-1}` is what the paired runner
probes.

### 3.2 Tadpole bookkeeping (historical pointer, not a numerical subtraction)

The following symbolic bookkeeping line is preserved from the earlier
draft as a historical pointer to the tadpole-subtraction *structure*. It
is **not** a derivation of a numerical subtraction, and no value of `u_0`
is imported here:

```
    I_S^{D_S1}  =  I_S^{tadpole}  +  I_S^{D_S1, TI}                       (R7)
    I_S^{tadpole}  =  constant-propagator piece   (absorbed by u_0 via D14)
    I_S^{D_S1, TI}  =  tadpole-subtracted piece
```

Which constant piece is removed, and with what coefficient, is a
scheme choice (a tadpole-subtraction *prescription*); the diagnostic of §4
concerns the origin behaviour of the displayed kernel *before* any such
prescription is fixed, and the prescription itself is listed among the
paths of §5. See [`docs/YT_VERTEX_POWER_DERIVATION.md`](YT_VERTEX_POWER_DERIVATION.md)
for the `n_link = 1` single-vertex bookkeeping context.

---

## 4. The infrared obstruction

The displayed kernel `K(k) = N_S(k) · [D_ψ(k)]^{-2} · D_g(k)^{-1}` is
singular at the Brillouin-zone origin. This section certifies the
singularity through structural constants only — the ray slope, the
halving factor, the leading coefficient, and the quadratic growth of the
origin-ball integral — with no external target.

### 4.1 Small-momentum asymptotics

Along any fixed ray `k = r·q̂` with unit direction `q̂` (the runner uses
`q̂ = (1, 2, 3, 4) / √30`), the small-`r` limits of §1.2 give

```
    K(r·q̂)  =  N_S / (D_ψ² · D_g)  →  4 / r^6.
```

Two structural constants follow, each falsifiable by a wrong kernel:

- **Ray log-slope `−6`.** `log K` versus `log r` has slope `−6` as
  `r → 0`. A kernel with one fewer inverse-propagator (an `r^{-4}`
  softening) gives slope `−4` and is rejected.
- **Halving factor `64 = 2^6`.** Halving `r` multiplies `K` by
  `2^6 = 64`. The successive ratios `K(r/2) / K(r)` approach `64` from
  below (`≈ 63.83, 63.96, 63.99, …`); the `r^{-4}` softening gives `16`
  and is rejected.
- **Leading coefficient `4`.** `r^6 · K(r·q̂) → 4` (the `N_S → 4` limit).
  The approach is `O(r²)`, so successive errors contract by a factor near
  `2^{-2} = 0.25` per halving (band `[0.20, 0.30]`). A kernel missing the
  `N_S` numerator gives leading coefficient `0` and is rejected.

### 4.2 Origin-ball partial integral and quadratic growth

With the four-dimensional measure `d^4k = r³ dr dΩ_3` and unit-3-sphere
area `|S^3| = 2π²`, define the origin-ball partial integral out to a fixed
outer radius `R = 1/4`:

```
    J(ε; R)  =  |S^3| · ∫_ε^R r³ · ⟨K⟩_{S^3}(r) dr
             =  2π² ∫_ε^R r³ · ⟨K⟩_{S^3}(r) dr.
```

Using the leading angular average `⟨K⟩_{S^3}(r) → 4 / r^6`,

```
    J(ε; R)  ≈  8π² ∫_ε^R r^{-3} dr  =  4π² ( ε^{-2} − R^{-2} ).
```

Two structural facts, each falsifiable:

- **Quadratic growth exponent `2`.** As `ε → 0`, halving `ε` multiplies
  `J` by `4 = 2²`; equivalently `log( J(ε/2) / J(ε) ) / log 2 → 2`. A
  kernel that diverges only logarithmically gives exponent `0` and is
  rejected.
- **Coefficient `ε² · J → 4π² ≈ 39.478`.** The rescaled integral
  approaches `4π²`, with the `O(ε²/R²)` tail contracting by a factor near
  `0.25` per halving (band `[0.20, 0.30]`).

The origin-ball integral therefore grows without bound as the inner
cutoff shrinks: the displayed kernel is not integrable at the origin.

### 4.3 No finite maximum-integrand × volume envelope

Because `K(k) → +∞` as `k → 0`, the supremum of the integrand over the
zone is `+∞`. Concretely, the shell maximum `S_m = max_{|k| = r_m} K(k)`
over a symmetric node set grows as `S_m → 4 / r_m^6`: halving `r_m`
multiplies `S_m` by `2^6 = 64`, and `r_m^6 · S_m → 4`. A
"`max-integrand × BZ-volume`" envelope requires a finite maximum
integrand; here there is none, so no such envelope exists. This is the
precise sense in which the earlier draft's magnitude bound is withdrawn:
the object it bounded is divergent. A bounded negative control — the same
kernel with a fixed mass regulator on the propagators — has a finite
maximum and `r^6 · S_m → 0`, confirming that the `64`/leading-`4`
signature is specific to the unregulated origin singularity.

---

## 5. Currently-omitted ingredients and the paths they open

The displayed scalar reduction hits the quadratic IR obstruction of §4
because it is not yet the full physical assembly. Three ingredients are
currently omitted; each is a concrete path this diagnostic opens.

1. **Full staggered-vertex / gauge-tensor contraction.** The kernel of §3
   is a scalar stand-in, not the full staggered-taste + gauge-Lorentz
   contraction of the `D_S1` vertex. The full numerator carries taste and
   Lorentz index structure whose small-momentum behaviour can soften the
   origin degree; deriving that full contraction from D2–D9 is the first
   path. Until it is carried, the scalar stand-in over-counts the origin
   singularity.

2. **Independent external-leg `Z_q` and assembly convention.** By (A1),
   the assembled `Z_S^{total}` depends on the external-leg coefficient
   `z_q`, which is **currently omitted** from the displayed kernel. An
   independent lattice computation of the fermion wavefunction
   renormalization `Z_q`, together with a specified assembly convention
   relating `Z_S^{D_S1}` and `Z_q`, is the second path. The mirror-symmetric
   `D_S2`/`D_S3` self-energies (§2.1) are where `z_q` is carried.

3. **Specified tadpole-subtraction prescription.** The bookkeeping of §3.2
   names a constant piece to be removed but fixes no prescription. A
   specified tadpole-subtraction scheme (which constant piece, with what
   coefficient) is required before the origin behaviour of the
   *subtracted* kernel is defined; supplying it is the third path.

None of these is closed by the present note; each is a next step this
diagnostic makes precise. The diagnostic's positive content is the
certified structural signature of §4 — ray slope `−6`, halving factor
`64`, leading coefficient `4`, quadratic origin-ball growth with
`ε² J → 4π²`, and the unbounded integrand supremum — which any full
assembly must confront.

The `C_A` channel (`I_2`) and the `T_F n_f` channel (`I_3`) of `Δ_R`, and
the Representation-A / Representation-B Ward comparison, are outside the
scope of this note and are unaffected by it.

---

## 6. Validation

The paired runner `scripts/frontier_yt_p1_h_unit_renormalization.py`
emits deterministic PASS/FAIL lines and probes the displayed kernel
`K(k) = N_S(k) · [D_ψ(k)]^{-2} · D_g(k)^{-1}` directly, comparing to **no**
external numerical target — only to the structural constants derived
above. Each gate is discriminating: it fails if the implemented kernel
were wrong, via an explicit wrong-kernel negative control or a
convergence-ratio requirement. The seven gates are:

1. **`IR_RAY_LOG_SLOPE_MINUS_SIX`** — the small-`r` log-log slope of
   `K(r·q̂)` is `−6`. Falsified by the `r^{-4}` softened control (slope
   `−4`).
2. **`IR_RAY_HALVING_FACTOR_64`** — successive halving ratios
   `K(r/2)/K(r)` converge to `2^6 = 64`, with the residual error
   contracting per halving. Falsified by the softened control (`16`).
3. **`IR_LEADING_COEFFICIENT_FOUR`** — `r^6 · K(r·q̂) → 4` with `O(r²)`
   contraction (successive `|c − 4|` ratio `→ 1/4`). Falsified by a
   unit-numerator control (`N_S` replaced by `1`, leading coefficient `1`).
4. **`FOUR_D_PARTIAL_INTEGRAL_QUADRATIC_GROWTH`** — the origin-ball
   integral `J(ε; R)` at `R = 1/4` satisfies
   `log( J(ε/2)/J(ε) ) / log 2 → 2` and `ε² · J → 4π²`. Falsified by a
   log-divergent control (exponent `0`).
5. **`NO_FINITE_MAX_TIMES_VOLUME_ENVELOPE`** — the shell maximum `S_m`
   grows as `2^6` per halving with `r^6 · S_m → 4`, so no finite
   maximum-integrand × volume envelope exists. Falsified by a
   mass-regularized control (bounded maximum, `r^6 · S_m → 0`).
6. **`EXTERNAL_LEG_ZQ_REQUIRED_AND_OMITTED`** — a structural check that
   the assembly convention (A1) requires an independent external-leg
   coefficient `z_q` that is **currently omitted** from the displayed
   kernel. The runner reads this note and verifies that the external-leg
   `Z_q` is documented as required, that the omission is stated, and that
   the displayed `D_S1` kernel block of §3 carries no `Z_q` factor. This
   certifies the omission structurally — never a claim that `Z_q` has been
   computed or that the assembled slope has been evaluated.
7. **`TADPOLE_COEFFICIENT_IS_SCHEME_DEPENDENT`** — the constant-piece
   projector is scheme-dependent: a soft (point) projector and a
   BZ-average projector of the numerator `N_S` disagree, so the tadpole
   coefficient is not scheme-invariant. Falsified by a genuinely constant
   numerator (the two projectors agree).

The runner prints the observed asymptotic values alongside each gate and
terminates with `SUMMARY: PASS=7  FAIL=0`. It consumes no external target
and imports no framework module.
