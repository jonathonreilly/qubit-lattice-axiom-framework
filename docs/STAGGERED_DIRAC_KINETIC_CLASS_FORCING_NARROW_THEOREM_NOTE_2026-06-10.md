# Staggered-Dirac Kinetic-Class Forcing — Two-Flux-Class Collapse and Absorbing-Frame Theorem

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim evidence:** computed sharpness countermodel
**Claim scope:** On the adjacency-licensed, charge-conserving
nearest-neighbor bilinear surface over the qubit-reframe-closed per-site `C²`
(cited authorities in §4), covariance under the lattice
automorphisms (translations and the 24 proper cubic rotations, each up
to site-local `U(1)` frame) collapses the kinetic family to EXACTLY TWO
frame classes on simply connected regions: `K0` = uniform plaquette
flux `+1` (representative `t ≡ 1`, scalar tight-binding) and
`K1` = uniform plaquette flux `−1` (representative the Kawamoto-Smit
sign system `η⁰`) — Two-flux-class theorem. On the `K1` branch the site-local
unitary absorbing frame of premise P-SD EXISTS, lands exactly in `K1`,
and is unique up to site-local `U(1)` gauge times one global frame —
the absorbing-frame theorem, discharging P-SD as a theorem given the `K1` branch. The
final selection `K1` vs `K0` (one bit; the kinetic-order bit) is NOT
forced by the specified constraint set: `K0` is the computed countermodel
(boundary B-BIT). P-KIN's premise content is thereby reduced from an
infinite-dimensional declaration ("the kinetic term is the naive
nearest-neighbor Cl(3) hopping bilinear") to exactly the flux-`−1` selector bit.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; audit verdict and effective status
are set only by the independent audit lane.
**Primary runner:** [`scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py`](../scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py)
(`TOTAL: PASS=28 FAIL=0`)
**Authority role:** source-note proposal narrowing boundary B2 (P-KIN)
and discharging boundary B3 (P-SD) of the Kawamoto-Smit forcing note's
declared premise set, and the corresponding `P-SD` row of the
realization gate's premise table Π. It does not change any existing
row's status.

## 0. Changelog

- **2026-06-10.** First version. Written against the bounded-to-audit
  boundary declared in
  `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
  (boundaries B2 = P-KIN, B3 = P-SD) and consumed by
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (premise table
  Π, row P-SD).
- **2026-06-17.** Removed the load-bearing dependency edge to the
  `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md`
  renaming row. The no-spectator input is now stated directly from the
  current minimal Quantum axiom's one-site `M₂(C) ~= Cl(3,0)` qubit
  carrier, the retained Cl(3) Pauli-module classification, and the
  runner's CAR(2) dimension computation. U4 remains provenance context
  only; no audit status or retained-grade promotion is asserted here.

## 1. Question

The staggered-Dirac spine currently rests on two DECLARED premises:

- **P-KIN** — the kinetic term is the naive nearest-neighbor Cl(3)
  hopping bilinear (naive-Dirac form);
- **P-SD** — the naive-Dirac form is made compatible with the
  single-mode per-site matter by a site-local unitary spin
  diagonalization (the absorbing frame).

Can either be DERIVED from cited authorities — and if not in
full, what exactly is the irreducible residual?

## 2. Answer (narrow, with computed sharpness)

**P-SD: yes, on the surviving Dirac branch — it becomes the absorbing-frame theorem.** The current minimal Quantum axiom supplies the per-site
one-qubit carrier `A_x ~= M₂(C) ~= Cl(3,0)`; with the retained Cl(3)
Pauli-module classification this is the single `C²` site module, not a
spectator surface. A per-site 2-component spinor would need a faithful
CAR(2) module of dimension ≥ 4 (computed: CAR(2) generates the full
`M₄(C)`), so the Cl(3) vector vertex has nowhere to live except
site-local frames. The absorbing frame then exists
(`T(x) = σ₁^{x₁}σ₂^{x₂}σ₃^{x₃}`), its image is forced into the
flux-`(−1)` class (γ anticommutation: plaquette holonomy
`γ_ν γ_μ γ_ν γ_μ = −I`), and it is unique up to
`T(x) → g(x) T(x) V` (site-local `U(1)` gauge × one global frame).

**P-KIN: reduced to one bit, not discharged (two-flux-class theorem + boundary
B-BIT).** On the licensed kinetic surface, the constraints carried by
cited authorities (hermiticity, translation covariance, cubic
covariance up to frame, single-mode realizability) collapse the
a-priori infinite family of kinetic bilinears to EXACTLY TWO frame
classes, distinguished by the frame-invariant uniform plaquette flux
`φ ∈ {+1, −1}`:

```text
K0 :  φ = +1   representative t ≡ 1          (scalar tight-binding;
                                              extensive zero surface)
K1 :  φ = −1   representative η⁰             (Kawamoto-Smit class;
      η⁰_1 = 1, η⁰_2 = (−1)^{x₁},             8 isolated Dirac zeros;
      η⁰_3 = (−1)^{x₁+x₂}                     = absorbed naive Dirac)
```

`K0` is the computed countermodel: it satisfies every imposed
constraint and every cited separator tested (fermion-parity grading,
hermiticity, exact cubic and translation invariance), so the specified constraint set cannot force `K1`. The surviving premise content of P-KIN is
exactly the one-bit selector `φ = −1` — the same residual the
index-pairing no-go names as the "kinetic-order selector"
(first-order Dirac vs second-order scalar). A premise this sharp can
replace P-KIN as the **flux-`−1` selector** on the licensed surface.

## 3. Boundaries (stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B-S1 | Surface scope: charge-(`Q`-)conserving bilinears; pairing terms are outside the surface by declaration, not derivation (runner leg D4 exhibits a Hermitian, parity-even NN pairing term) | Two-flux-class theorem quantifies within this surface |
| B-S2 | Nearest-neighbor support is licensed by the Lattice axiom's adjacency (the same strict adjacency-license reading as the landed per-plaquette enumeration), not derived; NNN terms are admissible once the license is dropped (leg D3) | ditto |
| B-S3 | "Kinetic" = the edge-supported quadratic sector; on-site bilinears (mass / chemical potential) and quartic interactions are separate sectors | ditto |
| B-EQ | Cubic/translation covariance up to frame is imposed via the no-selector licensing lemma L-EQ (equivariance rubric, §5.0): an axiom-derived kinetic term cannot carry a direction selector absent from the axioms. Imposing only the PROPER rotation group (24 elements) avoids any parity-implementation premise | Lemmas K2, K3 |
| B-H | Two-flux-class theorem is stated on simply connected regions; finite tori add wrap-holonomy (PBC/APBC) convention data — same boundary as the Kawamoto-Smit note's B4 | classification at finite volume |
| B-SL | Absorbing-frame theorem is a SITE-LOCAL statement; blocked/thinned multi-site spinor realizations (taste bases) are outside its scope | the absorbing-frame theorem |
| B-BIT | The selector `φ = −1` (K1 vs K0) is NOT forced by the specified constraint set; `K0` is the explicit countermodel. This is the irreducible residual of P-KIN | §7 |

## 3.1 No-Go Discipline Gate for the selector-not-forced finding

**Status: PASS for the scoped negative only.** The negative claim is only
that the specified constraint set does not force `φ = −1`, because `K0`
has `φ = +1` and satisfies every imposed constraint on the licensed surface.
It is not a claim that no future principle can select `φ = −1`.

- **N1 alternative routes.** Translation/cubic equivariance fails to select:
  both `K0` and `K1` pass. Hermiticity, charge conservation, nearest-neighbor
  support, and fermion parity fail to select: `K0` passes all. The current RP
  route is not an available selector here because it is grounded on the
  staggered surface. A spectral point-zero selector and a graded-locality
  selector remain possible future routes, not inputs used here.
- **N2 wall independence.** The scoped residual is one bit: `φ = −1` versus
  `φ = +1`. The surface boundaries (charge-conserving, nearest-neighbor,
  site-local, simply connected) are scope declarations, not independent
  selector walls.
- **N3 hidden-wall scan.** The note declares every scope choice up front and
  supplies falsification legs for dropping cubic covariance, nearest-neighbor
  support, charge conservation, and qubit-reframe closure.
- **N4 residual matching.** The index-pairing no-go is cited only as a matching
  residual pointer: first-order/Dirac kinetic order versus scalar order. It is
  not load-bearing evidence for this proof.
- **N5 rhetoric audit.** "Not forced" means not forced by the specified
  constraint set on the licensed surface. It does not mean `φ = −1` is false,
  unnatural, or impossible to derive from a later selector.
- **N6 partial-closure path.** A future RP, spectral, graded-locality, or other
  selector could retire B-BIT without changing the axioms; this note leaves
  that route open.
- **N7 steelman.** A hostile reviewer should say the real theory may contain a
  dynamical or readout principle that favors isolated Dirac zeros and therefore
  picks `φ = −1`. This note accepts that as a future selector route.
- **N8 cross-cycle echo.** Prior statistics and kinetic-order no-go surfaces
  left exactly this kind of selector residual. This note narrows it to a
  concrete flux bit rather than rebranding it as a new primitive.

## 4. Cited authorities (one hop, with license statements)

Load-bearing (markdown links):

1. [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) —
   axiom premise node. License used: Lattice (site set `Z³`, standard
   translation action, nearest-neighbor cubic adjacency) and Quantum
   (one-site qubit carrier, `A_x ≅ M₂(C) ≅ Cl(3,0)`). This is the
   load-bearing source for the single primitive local carrier used in
   the no-spectator lemma and K4. Nothing else (no dynamics, no boundary
   condition, no kinetic selector) is drawn from the axioms.
2. [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
   — License used: the 2-dim faithful complex Cl(3) irreps with Pauli
   realization `γ_μ = σ_μ`; consumed only as the retained
   Pauli-module/classification statement that identifies the minimal
   Quantum carrier with the single `C²` site module.
3. [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
   — License used: the finite periodic tensor-product Fock
   surface, local ladder operators, `Q_total`, and the
   tensor-permutation translation covariance identities. This is the
   operator surface on which the kinetic bilinears of Definition D-kin
   live.
4. [`FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md`](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
   — License used: the `(−1)^Q` grading with bilinears
   `Z₂`-even; consumed as a tested cited separator (runner check 18
   shows it does not separate `K0` from `K1`).

Plain-text pointers (NOT load-bearing):

- `U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md`
  — audited-renaming/provenance context for older U4 language only.
  This note does not consume U4 as a load-bearing theorem dependency;
  the `C²`/no-spectator input is sourced directly from the current
  minimal Quantum axiom, the retained Cl(3) classification, and runner
  check 10.
- `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`
  — declares P-KIN (B2) and P-SD (B3); its Lemmas 2–4
  classify phase systems WITHIN the `−1` cocycle. Two-flux-class theorem here
  classifies the larger surface (both fluxes); Absorbing-frame theorem re-proves the
  needed existence/uniqueness facts self-contained so that note is not load-bearing.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — the consumer
  gate (premise table Π, row P-SD; its runner's check 18 exhibits the
  2-component alternative that the absorbing-frame theorem now excludes site-locally).
- `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16`
  (claim id; under parallel revision) — supplies the
  single-mode Grassmann reading of the matter surface. Two-flux-class theorem is
  deliberately frame-robust and does not depend on the
  fermion-vs-hard-core reading (flux is invariant in both).
- `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`
  — consistency: that no-go shows statistics is a
  frame choice; nothing here contradicts it, and the kinetic
  classification is performed on frame-invariant data.
- `INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`
  — consistency: its residual "kinetic-order selector"
  is the same one-bit residual as B-BIT, seen at the representation
  level; its conditional theorem (given first-order kinetic order, the
  spin lift is unique) matches leg D5's equivariance reduction.
- `GATE_RP_REGROUND_STAGGERED_ONLY_NARROW_THEOREM_NOTE_2026-05-23.md`
  and
  `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
  — reflection positivity is deliberately NOT
  imposed in the two-flux-class theorem: the RP authority is grounded on the
  staggered surface, so using it to SELECT the staggered class would
  be circular. RP is therefore not available as the B-BIT selector.
- `PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`
  — precedent for the strict adjacency-license
  surface reading used in B-S2.

Forbidden imports: no PDG values, no lattice-MC values, no fitted
coefficients, no new axioms.

## 5. Definitions, lemmas, theorems

### 5.0 Licensing lemma L-EQ (equivariance rubric; declared, B-EQ)

The axiom data (Lattice + Quantum) is invariant under the lattice
automorphisms `Aut = O ⋉ T` (`T` = translations, `O` = the 24 proper
cubic rotations; runner check 1 generates `O` from `C4z` and
`C3[111]`). Any kinetic term constructed from the axiom data WITHOUT an
additional direction/position selector must therefore be
`Aut`-covariant up to the declared frame redundancy. This is the same
orbit/equivariance rubric the substep-4 labeling no-go uses; it is a
licensing statement for the constraint set, not a hidden physical
input, and a kinetic term violating it would require exactly the kind
of selector premise the framework would have to declare separately.

### 5.1 Definition D-kin (the licensed kinetic surface)

On the cited tensor-product Fock surface (authority 4), the kinetic
surface is

```text
S = { H_t = Σ_{x,μ} ( t_μ(x) a†_{x+μ̂} a_x + conj ) :  t_μ(x) ∈ C },   (1)
```

the `Q`-conserving bilinears supported on the Lattice axiom's
nearest-neighbor edges (B-S1–B-S3). Frame redundancy: site-local
`U(1)`, `a_x → u(x) a_x`, acting as
`t_μ(x) → conj(u(x+μ̂)) t_μ(x) u(x)`; plus overall scale and lattice
automorphisms. The **plaquette flux**
`Φ_P = t_μ(x) t_ν(x+μ̂) conj(t_μ(x+ν̂)) conj(t_ν(x))` is
frame-invariant (runner check 2). In the qubit reading the same family
is the XY-type `σ₊σ₋` surface; the classification below uses only
frame-invariant data, so it is statistics-frame-robust (cf. the
statistics-agnostic no-forcing note).

### 5.2 Two-flux-class theorem (two-flux-class collapse)

**On the axioms (authority 1) and the surface D-kin, impose:
(K1) hermiticity (built into (1)); (K2) translation covariance up to
frame; (K3) cubic `O`-covariance up to frame (L-EQ); (K4) nonzero
kinetic term. Then on simply connected regions of `Z³`, up to frame ×
scale × lattice automorphism, there are EXACTLY TWO kinetic classes:
`K0` (uniform flux `+1`, representative `t ≡ 1`) and `K1` (uniform flux
`−1`, representative `η⁰`).**

*Proof sketch (each step runner-certified).*
(a) `|t_μ(x)|` is frame-invariant per edge; translations act
transitively on same-direction edges and `O` on the 6 directions
(check 1), so `|t| = const > 0`; normalize to 1.
(b) Translations preserve flux exactly, so flux is constant on each
plaquette plane class; `C3[111]` equates the three classes ⇒ uniform
flux `φ`.
(c) The `C2` rotation about an in-plane lattice axis maps every
axis-containing plaquette to itself-class with REVERSED orientation,
i.e. pushforward flux = `conj(φ)`; covariance up to frame then forces
`φ = conj(φ)`, so `φ ∈ {+1, −1}` (check 3; the uniform-flux-`i`
Landau-type witness is explicitly rejected — checks 3, 22).
(d) Flux classifies up to frame on simply connected regions: closed
one-cochains modulo exact ones — `nullity(d₁) = rank(d₀)` over GF(2) on
the `2³`, `3³`, `4³` boxes (checks 4–6) and exact integer rank
certificate `rank(d₁) = 5`, `rank(d₀) = 7`, `d₁ d₀ = 0` for the `U(1)`
case on the unit cube (check 7); exhaustive enumeration of all
`2^{12} = 4096` sign systems on the unit cube finds exactly
`128 = 2⁷` per uniform-flux bucket, each a single gauge orbit, with
`η⁰` in the `−1` bucket (check 8).
(e) Both classes are realized (check 9). ∎

### 5.3 Absorbing-frame theorem (P-SD discharged on the `K1` branch)

**On the minimal Quantum axiom's one-site qubit carrier (authority 1)
and Cl(3) classification (authority 2):**

**(i) No-spectator / scalarization forced.** The per-site physical
space is the single `C²` qubit carrier supplied by the minimal Quantum
axiom and identified with the retained Pauli/Cl(3) module by authority
2. Two independent fermion modes per site (a 2-component spinor) would
require a faithful CAR(2) module; CAR(2) generates the full `M₄(C)`
(computed dim 16, check 10), which is simple with unique faithful irrep
of dim `4 > 2`. So the
naive-Dirac kinetic structure `Σ_μ γ_μ ⊗ ∇_μ` admits NO site-local
realization with an explicit per-site spinor index; in any site-local
realization the Cl(3) vector vertex must be absorbed by site-local
unitaries `T(x)`, i.e. the scalarization condition
`T†(x) γ_μ T(x+μ̂) = η_μ(x) I` — P-SD's equation — is derived as the
unique site-local route, not declared (boundary B-SL for non-site-local
routes).

**(ii) Existence.** `T(x) = σ₁^{x₁} σ₂^{x₂} σ₃^{x₃}` satisfies the
scalarization exactly, with phases `η⁰` (check 11, exact sympy).

**(iii) Rigidity.** `γ_ν γ_μ γ_ν γ_μ = −I` for all `μ ≠ ν` (check 12),
so EVERY absorption carries plaquette flux `−1`: the absorption image
of the naive-Dirac class is exactly `K1`, and absorption into `K0` is
impossible (flux is frame-invariant). The naive-Dirac bilinear of
P-KIN and the `K1` class of the two-flux-class theorem are the same object on the
licensed surface.

**(iv) Uniqueness.** If `T, T'` scalarize with the same phases, then
`S(x) := T'(x) T(x)†` satisfies `S(x+μ̂) = γ_μ S(x) γ_μ`; the
propagation is path-consistent and the general solution is exactly
`S(x) = T(x) V T(x)†` with `V ∈ U(2)` arbitrary (check 13), i.e.
`T'(x) = T(x) V`. Different phases within `K1` differ by a site-local
gauge `g(x)` (check 14 + the two-flux-class classification). Hence the absorbing frame is
unique up to `T(x) → g(x) T(x) V`. ∎

P-SD therefore holds as a theorem given the `K1` branch:
`φ = −1` plus the specified constraint set implies P-SD.

### 5.4 Sharpness (the countermodel; boundary B-BIT)

`K0` (`t ≡ 1`) is Hermitian, exactly translation- and 24-rotation-
invariant (check 16), `Q`-conserving, fermion-parity-even (check 18),
and not frame-equivalent to `K1` (check 19; fluxes `+1` vs `−1`).
Spectral witness (check 20): `K1` has exactly 8 zero modes at `L = 4`
and `L = 8` (isolated Dirac points; the doubler corners), while `K0`
has an extensive zero set (20 → 68): genuinely distinct kinetic orders.
No cited authority tested separates them, and the RP
authority is staggered-scoped (circular as a selector). So the
specified constraint set does NOT force `K1`; the irreducible residual of P-KIN is
the single bit `φ = −1`.

### 5.5 What the qubit-reframe closure buys (why the collapse is to two points)

On a hypothetical 2-modes-per-site spectator surface (qubit-reframe closure
dropped), the Wilson family `M_μ(r) = γ_μ + r I` is `O`-equivariant
under the spin lift for EVERY real `r` (check 25): a one-parameter
CONTINUUM of kinetic classes interpolating the two orders survives all
symmetry constraints. Single-mode absorption kills it: `M(r)` is
proportional-to-unitary iff `r = 0`, and the projective plaquette
commutation `M_μ M_ν = λ M_ν M_μ` has scalar solutions only at `r = 0`
(`λ = −1`) (check 26, exact sympy). More generally the full
12-complex-parameter `O`-equivariant nearest-neighbor family collapses
under equivariance + reversed-edge hermiticity to
`M_μ = a I + i b σ_μ` (`a, b` real — the scalar ray and the Dirac ray;
check 27), and the single-mode constraint then leaves exactly the two
rays = the two classes of the two-flux-class theorem. The qubit-reframe closure is thus
precisely the input that turns a Wilson-type continuum into the sharp
two-point classification.

## 6. What the runner computes

[`scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py`](../scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py)
— deterministic, no network, no randomness, runtime well under one
minute. One source-dependency guard tagged `[S]`, plus 27 mathematical
checks in four sections tagged `[A]`/`[B]`/`[C]`/`[D]`
(two-flux-class theorem certificate; absorbing-frame theorem certificate; sharpness countermodel;
falsification legs), with `RESIDUAL (declared-open): ...` lines printed
at the point where each boundary is load-bearing. Exact sympy for all
2×2 algebra, GF(2)/integer linear algebra for the cohomology
certificates, dense eigensolves (≤ 512-dim) for the spectral witness.
Falsification legs: dropping cubic covariance admits anisotropic and
complex-flux classes (D1, D2); dropping the adjacency license admits an
NNN continuum (D3); dropping `Q`-conservation admits pairing terms
(D4); dropping the qubit-reframe closure admits the Wilson continuum (D5). Each leg verifies
both that the exotic member satisfies the remaining constraints and
that the named constraint rejects it.

## 7. What this does NOT close

- **The B-BIT selector.** Why `φ = −1` (first-order/Dirac) rather than
  `φ = +1` (second-order/scalar) is NOT derived. Candidate future
  selectors, none assumed here: an RP/transfer-positivity theorem grounded
  off-staggered-surface; a spin-statistics/graded-locality principle (the
  statistics no-go's N6 path); a dynamical/spectral principle requiring
  point-like zero sets (relativistic cones). Any of these would retire
  B-BIT; none is assumed here.
- The wrap-holonomy/APBC convention data at finite volume (B-H).
- Non-site-local (blocked/taste-basis) realizations (B-SL).
- The surface declarations B-S1–B-S3 (pairing, NNN, on-site/mass and
  interaction sectors are out of scope by license, with legs D3/D4
  showing they are genuine scope choices).
- Nothing here changes the substep-1 statistics conclusion: which
  frame (fermionic vs hard-core) is physical remains exactly as the
  no-forcing note left it.

## 8. What this supports (downstream citable text)

- The Kawamoto-Smit forcing note's boundary table can cite this row
  as: B2 (P-KIN) narrows to the **flux-`−1` selector** — "the kinetic phase system lies
  in the flux-`(−1)` class of the two-class classification
  (`staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10`,
  two-flux-class theorem), a one-bit premise"; and B3 (P-SD) is discharged —
  "site-local unitary scalarization exists and is unique up to gauge ×
  global frame given the flux-`−1` selector (ibid., absorbing-frame theorem)".
- The realization gate's premise table Π can replace the P-SD row by
  the flux-`−1` selector with this note as the carrying authority, shrinking the
  declared premise surface of the ~1163-row staggered spine to one
  explicitly-named bit plus convention data.
- The index-pairing kinetic-order no-go gains an action-level twin:
  its "first-order vs second-order" residual and B-BIT are the same
  wall, now certified by an exhaustive classification with a concrete
  countermodel on the licensed surface.

## 9. Command

```bash
python3 scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py
```

Expected output (deterministic): 28 `[PASS]` lines: one `[S]` source
dependency guard and 27 numbered mathematical checks in sections
`[A]`/`[B]`/`[C]`/`[D]` as described in §6, including
`|O| = 24, direction orbit size = 6`,
`V=64 E=144 P=108 rank(d1)=81 rank(d0)=63`,
`counts = (128, 128, 3840), orbit = 128`,
`computed algebra dim = 16`,
`zeros: K0 (L=4,8) = (20,68); K1 (L=4,8) = (8,8)`,
`solve(off-diag=0) = [0], projective sols = [{lam: -1, r: 0}]`, and
`surviving real dimension = 2`; five `RESIDUAL (declared-open): ...`
lines (B-H, surface scope, B-SL, B-BIT, bilinear-sector scope); then
exactly:

```text
TOTAL: PASS=28 FAIL=0
VERDICT: Two-flux-class theorem (two-flux-class collapse) and Absorbing-frame theorem
         (P-SD discharged on the flux(-1) branch) VERIFIED on
         the finite instantiation; the flux(+1) countermodel
         certifies that the final one-bit kinetic-order
         selector is NOT forced by the specified constraint set.
```

Exit code 0 iff FAIL=0.

## 10. Honest status

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "On the adjacency-licensed Q-conserving NN bilinear surface over the qubit-reframe-closed per-site C^2, translation+cubic covariance up to site-local frame collapses the kinetic family to exactly two flux classes {+1, -1}; the site-local absorbing frame of P-SD exists, is unique up to gauge x global frame, and lands exactly in the flux(-1) class; the final one-bit class selector is NOT forced (computed countermodel)."
upstream_dependencies:
  - minimal_axioms
  - axiom_first_cl3_per_site_uniqueness_theorem_note_2026-04-29
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25
  - fermion_parity_z2_grading_theorem_note_2026-05-02
admitted_context_inputs: []
source_sets_audit_outcome: false
```
