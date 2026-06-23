# φ = −1 Kinetic-Order Selector Attack Proposal — Five Routes, One Verdict

**Type:** PROPOSAL
**Status:** hypothetical_axiom_status (`proposal_allowed = false`)
**Status authority:** the independent audit lane + owner ONLY. **This note sets
NO audit status** — it neither asserts, predicts, promotes, nor demotes any
audit outcome or effective status.
**Date:** 2026-06-23

> **This note touches NO canonical, audit, or publication file.** It does not
> edit any `MINIMAL_AXIOMS_*`, `AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`,
> `MISSING_DERIVATION_PROMPTS.md`, any `*_EFFECTIVE_STATUS.md`, or any
> `docs/audit/data/**` file. It registers no primitive and changes no axiom
> memo. It runs no script that rewrites tracked `outputs/`. It is a source-side
> proposal only; the independent audit lane is the sole status authority.

---

## PURPOSE

The `d ≤ 3` UPPER leg of the dimension derivation is conditional on exactly one
bit: `φ = −1`, the **kinetic-order selector** (first-order Dirac vs second-order
scalar). Given `φ = −1` (the `K1` Dirac ray) the `M₂(ℂ)` anticommutant cap of
[`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md)
forces `d ≤ 3`; on the `K0` scalar ray the qubit spectates and the cap is
**vacuous**. So discharging `φ = −1` from axioms + accepted primitives — without
re-importing the Dirac assumption — is exactly what would make the upper leg
unconditional and would license weakening the `A1` `Z³` lattice primitive to a
derived `Zᵈ` cap. This note is the adversarial attack on that bit, the companion
to the dimension-compression proposal
[`D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md`](D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md)
(whose Clause A is precisely this `φ = −1`, flagged UNAUDITED).

Five candidate selectors were developed, then independently re-tested with fresh
`numpy`/`sympy` code (every load-bearing number reproduced from scratch, not
trusted from the source notes). The honest verdict is **negative**: `φ = −1` is
an irreducible dynamics posit on the current primitive set. This note reports
that outcome without forcing a positive, names the minimal posit for a future
ledger decision, and states the exact per-route escape condition.

---

## THE WALL

### The two rays (settled)

On the adjacency-licensed, charge-conserving nearest-neighbor bilinear surface
over the qubit-reframe-closed per-site `C²`, translation + the 24 proper cubic
rotations (each up to site-local `U(1)` frame) collapse the kinetic family to
**exactly two frame classes**, the two rays of `M_μ = a·I + i·b·σ_μ` (`a, b`
real), distinguished by the frame-invariant uniform plaquette flux `φ`
(authority:
[`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
§5.2, §5.5, runner `PASS=28`):

```text
K0  φ = +1  (a-ray, SCALAR)  rep H(p) = (Σ_μ cos p_μ) I₂   second-order/Klein-Gordon
            qubit SPECTATES [H,σ_i]=0 exactly; EXTENSIVE zero surface {Σ cos p_μ=0}
            (20 → 68 → 140 zero modes at L=4,8,12). Hermitian, full O_h (cos parity-even,
            incl. inversion), Q-conserving, fermion-parity-even.
            RUNNER-CERTIFIED COUNTERMODEL — satisfies every imposed constraint.

K1  φ = −1  (b-ray, DIRAC)   rep H(p) = Σ_μ σ_μ sin p_μ    first-order (naive Dirac,
            absorbed Kawamoto-Smit η⁰). qubit ACTIVE [H,σ_i]≠0; EXACTLY 8 isolated
            Dirac zeros (doubler corners p_μ∈{0,π}). Caps spatial d≤3 via the M₂(ℂ)
            anticommutant bound.
```

The selection `K1` vs `K0` is the one residual bit `φ = −1` (boundary B-BIT).

### Selectors already settled to FAIL or be CIRCULAR (cited, not re-derived)

- translation + cubic `O`-equivariance — both `K0`, `K1` pass (kinetic-class §5.4);
- Hermiticity, charge conservation, NN support, fermion parity — `K0` passes all;
- positivity/stability — naive Dirac has a negative branch, the scalar Laplacian
  is bounded below, so positivity pulls toward `K0`, **not** first-order
  ([`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md)
  lines 81–82);
- Nielsen–Ninomiya — bites WITHIN the first-order class, does not force the class;
- isotropic linear Lorentz cone `|E| = |p|` — forces first-order but **IS** the
  Dirac assumption ⇒ CIRCULAR (index-pairing lines 85–89; isotropic `SO(3)` is
  not supplied by cubic `O_h`);
- on-staggered reflection positivity — the RP authority is grounded on the
  staggered surface ⇒ CIRCULAR as a staggered selector (kinetic-class §4, the
  `GATE_RP_REGROUND_STAGGERED_ONLY` pin);
- statistics frame (fermion vs hard-core boson) — FLUX-INVARIANT
  ([`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md))
  ⇒ naive spin-statistics does not directly pick `φ`.

**Accepted primitives a selector MAY consume non-circularly:** P2 kinetic-isotropy
(`c_t = c_s`,
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)),
P3 realized-state
([`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)),
A3 Record
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)). All three are
registered in `docs/audit/data/axiom_premise_nodes.json`.

### The circularity bar (applied ruthlessly)

A selector is CIRCULAR if it presupposes the first-order Dirac form, the linear
cone `|E|=|p|`, or `SO(3)` isotropy not supplied by cubic `O_h`. It is LEGITIMATE
only if it derives "`φ = −1` / isolated zeros / qubit-active kinetic term" from
inputs an independent auditor would accept as **not already** the Dirac
assumption. Every "forces" claim below must exhibit **why `K0` fails** the
route's principle with a concrete computation.

---

## THE FIVE ROUTES

Each route: thesis · does `K0` fail? · circularity verdict · outcome · concrete
computation (independently reproduced).

### ROUTE 1 — Off-staggered reflection positivity

**Thesis.** Bare-lattice Euclidean transfer-matrix positivity, with the time
reflection plane fixed geometrically (no staggered phase compensation), does
**not** force `φ = −1`. It FAVORS the scalar `K0` and PENALIZES the Dirac `K1`.

**Does `K0` fail?** **NO — `K0` is the SURVIVOR.** Off-staggered RP excludes
`K1`, the OPPOSITE of the target.

**Two-level structure.**

- **(A) Hamiltonian level is vacuous.** Both `H_K0` and `H_K1` are Hermitian by
  construction, so `T = exp(−aH)` is positive for BOTH — exactly the trivial
  `E1`–`E4` content of
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  (lines 484–500: "`exp(−aτH)` is positive if `H` is Hermitian"). It cannot
  separate the rays. The honest discriminator must be the **Euclidean/Lagrangian**
  transfer extracted from the lattice action under a geometric time reflection.

- **(B) Euclidean level favors the scalar.** Single-mode temporal transfer at
  fixed spatial momentum `p`, geometric (non-staggered) reflection:
  - `K1` (first-order, antisymmetric temporal hop): `α ψ_t + ½(ψ_{t+1}−ψ_{t−1}) = 0`,
    `α = m + i sin p` (spatial Dirac term imaginary on-site after frame
    absorption) ⇒ `T_K1 = [[−2α, 1],[1, 0]]`.
  - `K0` (second-order, parity-EVEN temporal Laplacian):
    `−(ψ_{t+1}+ψ_{t−1}−2ψ_t) + ω² ψ_t = 0`, `ω² = m² + 2(1−cos p) ≥ 0` ⇒
    `T_K0 = [[2+ω², −1],[1, 0]]`.

  **Mechanism:** the first-order temporal derivative combined with the imaginary
  spatial Dirac symbol tilts `α = m + i sin p` off the positive real axis, so the
  transfer spectrum leaves the positive real axis. The scalar's parity-even
  second-order temporal term keeps `ω² ≥ 0` real, so the transfer eigenvalues are
  reciprocal real positive `e^{±E}`.

- **(C) The staggered rescue is circular.** The ONLY thing that rescues `K1` to
  positivity is the 2-step `T_odd·T_even` with `α_even = m + i sin p`,
  `α_odd = m − i sin p` — the alternating staggered spatial phase `η₁(t)=(−1)^t`
  returning to its original sign over two spacings
  ([`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  lines 95–106, 110–137). Off-staggered there is no odd/even alternation, so the
  natural 2-step is plain `T²` — and `T²` is ALSO non-positive for `K1`. Any RP
  route that selects `K1` must invoke the staggered 2-step, i.e. presuppose the
  staggered (Dirac) frame: the `GATE_RP_REGROUND_STAGGERED_ONLY` circularity.

**Circularity verdict.** NOT circular in the Dirac/cone/`SO(3)` sense — and that
is precisely why it returns a negative for the target. The geometric reflection
treats both rays evenhandedly and the un-rigged answer is that the SCALAR has the
positive single-step Euclidean transfer (positivity of `exp(−aH)` pulls toward
bounded-below, real-symmetric Laplacians). The circularity lives on the OTHER
side: only the staggered 2-step rescues `K1`.

**Outcome: DOES NOT FORCE** (selects the wrong ray).

**Concrete computation (independently reproduced, `numpy`):**

```text
grid Lt∈{8,12,16} × m∈{0.1,0.5,1.0} × p over BZ (40 pts) = 120 points
K0: T fail 0/120, T² fail 0/120, max|Im(eig)| = 0.0, min decaying root = 0.1459  → POSITIVE
K1: T fail 120/120, T² fail 120/120, max|Im(eig)| = 1.78                          → NON-POSITIVE
    e.g. m=0.5,p=1.21: eig = {−1.331−1.498j, 0.331−0.373j} (complex)
         m=0.5,p=0   : eig = {−1.618,  0.618}              (real, one negative)
staggered rescue T_odd·T_even: fail 0/120, max|decaying − e^{−2E}| = 5.0e−16  (E=arcsinh√(m²+sin²p))
Hamiltonian guard (Z³, L=4): both H Hermitian; min eig e^{−aH} > 0 for BOTH (PSD) → level (A) vacuous
```

---

### ROUTE 2 — Isolated-zero spectral selector

**Thesis.** Principle: "the realized matter kinetic kernel's zero (massless) set
must be FINITE / point-like, not extensive." This DOES separate `K1` (8 isolated
zeros) from `K0` (codim-1 surface) by an exact computation. But the principle is
a NEW posit (clause B-Z2 of the P-FLUX no-gos), unsupplied by A3 / P3 / "finite
modes per BZ"; and its only working strengthening (FSB-K) bundles the circular
linear cone.

**Does `K0` fail?** **YES — `K0` is genuinely excluded BY THE PRINCIPLE.** What
is in doubt is the AUTHORITY to impose the principle, not the exclusion.

**Two-tier circularity.**

- **(i) The PURE finiteness predicate is NOT circular.** Independently confirmed
  geometry-blindness witness: a SECOND-order operator (scalar NN + on-site `−6`)
  has point-like zeros `1, 1, 1` at `L=4,8,12`. So "point-like zero set" is NOT a
  synonym for first-order/Dirac; it does not presuppose `|E|=|p|`, `SO(3)`, or the
  Dirac form. It escapes the cone-circularity bar.
- **(ii) BUT it fails the AUTHORITY bar.** It is unsupplied by any accepted
  primitive:
  - **A3 Record** ([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md))
    is a durable readout in a SUPPLIED context with a SUPPLIED finite central-sector
    decomposition; it "supplies no readout context, decomposition, … within-sector
    data, or occupancy rule." Its finiteness is about distinguishable registered
    OUTCOMES, not the spectral support of a propagator
    ([`P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md):
    "remain separate input rather than a consequence of those linked rows").
  - **P3 Realized-state** selects WHICH law-admissible STATE the world realized;
    `K0` and `K1` are two distinct law-admissible KINETIC LAWS, not two states of
    one law. The firewall "the laws do not pick the state; the world does" forbids
    selecting among law-admissible structures.
  - **finite-modes-per-BZ** is a derived FACT about each kernel (closed-form bands),
    not an axiom; nothing axiom-level rejects measure-zero zero surfaces.
- The repo's only working strengthening (the FSB-K composer
  [`P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`](P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md))
  bundles point-likeness WITH an invertible isotropic linear cone, cone data
  `(V,C,r) = (2I, 2/3, 1)` at all 8 corners. Wave-3
  ([`P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md))
  proves the thermal clause is "strictly stronger than bare point-like zero set
  (it also forces conical dispersion)" — and that conical/linear-cone half IS the
  Dirac assumption flagged circular by index-pairing. So: **pure finiteness =
  non-circular but UNSUPPLIED; cone-strengthened finiteness = supplied-as-posit but
  CIRCULAR.** No version is both non-circular AND derived from P2/P3/A3.

**Circularity verdict.** Tier (i) NON-circular but unsupplied; tier (ii) the only
landed strengthening is circular.

**Outcome: CONDITIONAL ON A NEW PREMISE** (the only route that genuinely excludes
`K0` by a non-circular principle; it fails on authority, not on circularity).

**Concrete computation (independently reproduced, `numpy`+`sympy`):**

```text
zero-mode counts on Z³ PBC single-mode hopping:
  K0 (t≡1)                = 20, 68, 140 at L=4,8,12   (extensive; N0·ln2/V = 0.2166, 0.0921, 0.0562 → 0)
  K1 (η⁰ Kawamoto-Smit)   =  8,  8,   8 at L=4,8,12   (L-constant, 8 isolated corners)
  scalar NN + on-site(−6) =  1,  1,   1               (2nd-order COMPARATOR ⇒ point-like ≠ Dirac)
sympy: cos(π/2+t)+cos(π/2−t)+cos(π/2) ≡ 0  ⇒ K0 zero set contains a continuous (uncountable) line
        (codim-1 regular surface; gradient (−1,−1,−1) ≠ 0 at (π/2,π/2,π/2))
predicate FINITE_POINTLIKE: K0 → FALSE, K1 → TRUE, scalar-comparator → TRUE
```

---

### ROUTE 3 — Kinetic isotropy (P2, `c_t = c_s`)

**Thesis.** P2 enforces axis-isotropy of the kinetic FORM, which a massless
second-order Klein-Gordon scalar satisfies exactly (`E²=|p|²` is isotropic with
`c_t=c_s`). P2 narrows the form to "isotropic" but leaves the first-order vs
second-order ORDER bit fully open; closing it needs a separate LINEAR-cone
premise = the circular Dirac assumption.

**Does `K0` fail?** **NO — `K0` survives, by two disjoint arguments.**

P2's defining text
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
lines 30–34, 65–77) is emphatic: P2 carries "no … selector," "is not a new
dynamics," "fixes only the one dimensionless graining ratio." Its landed firewall
([`EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
Audit Note, lines 86–91) explicitly REJECTS a PR that read P2 as supplying boost
generators / Poincaré covariance.

**Circularity verdict.** P2 alone is NOT circular (it is an owner-approved
primitive) but is INCONCLUSIVE. To reach `φ = −1` the route must ADD "the realized
cone is LINEAR in `E` (first-order), not quadratic" = the isotropic linear Lorentz
cone `|E|=|p|`, which index-pairing (lines 84–90) certifies is the circular
Dirac-form assumption. So **P2 alone = clean-but-inconclusive; P2 + linear-cone =
circular.**

**Outcome: DOES NOT FORCE.**

**Concrete computation (independently reproduced, `numpy`):**

```text
(1) axis-permutation blindness — Euclidean symbols on Z³×Z_tau, all 24 axis perms:
    second-order scalar S_E = Σ_μ(1−cos p_μ): max dev = 1.78e−15
    first-order Dirac  |D|² = Σ_μ sin² p_μ  : max dev = 8.88e−16        → BOTH isotropic, P2 blind
(2) cone order at realized zero (vanishing-order fit, ≥20 directions):
    scalar S_E order = 2.0000 ± 2.5e−7   |D| order = 1.0000 ± 4.2e−7    → discriminator is ORDER, not isotropy
(3) isolated-isotropic-cone NON-exclusion:
    massless KG scalar at isolated zero p=0: E²/|p|² = 1.00000000, var = 1.45e−16  → 2nd-order passes "isolated+isotropic"
note: framework K0=(Σ cos p_i) at p=0 equals +3 (band TOP, not a zero); its zeros are the band-center surface
```

---

### ROUTE 4 — Irreducibility / no-spectator (faithful `M₂(ℂ)`)

**Thesis.** The principle that legitimately follows from A2/Quantum is F1
(faithful representation) + F2 (no idle tensor factor). `K0` satisfies BOTH. The
only failing property — F3, kinetic-sector exercise of `σ` — is a separate
DYNAMICAL posit that A2 does not supply, and on the two-ray surface it is
logically identical to `φ = −1`.

**Does `K0` fail?** **NO — `K0` passes F1 and F2; it fails only F3.** A2 supplies
the one-site algebra and "does not supply a dynamics"
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)). The qubit is
freely exercisable by an on-site `σ₃` mass term or the A3 Record/CPT central-sector
decomposition, leaving the FREE kinetic order scalar.

**Three notions kept separate:** F1 = faithful irrep (commutant = scalars); F2 =
no extra tensor factor (site stays `dim 2`, not `dim 4`); F3 = the realized
kinetic term exercises off-diagonal `σ` (`[H,σ_i] ≠ 0`). The proven no-spectator
lemma (kinetic-class §5.3(i): a 2-component spinor needs faithful `CAR(2) =
M₄(ℂ)`, `dim 16`, unique irrep `dim 4 > 2`) excludes only the dim-4 spinor route —
which `K0` is NOT. The decisive landed precedent is the boost-faith no-go
([`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)):
its N1 table explicitly rules the "Clifford-action route" and "Dimension route"
non-sequiturs — faithful local algebra does NOT force faithful physical action,
and `dim C² = 2` does not exclude scalar (algebra-trivial-in-sector) actions.
Route 4's F2→F3 step is that identical inference applied to the kinetic kernel.

**Circularity verdict.** Route 4 in its forcing form is a DISGUISED RE-POSIT of
`φ = −1` (not cone/`SO(3)`-circular, but logically circular on the two-ray
surface): on `M_μ = a·I + i·b·σ_μ`, "`[M_μ,σ_i]=0` for all `i`" ⇔ `b=0` ⇔ scalar
ray `K0` / `φ=+1`; `b≠0` gives `M_μ M_ν = −M_ν M_μ` = `K1` / `φ=−1`. So asserting
F3 of the kinetic term IS asserting `φ=−1`.

**Outcome: DOES NOT FORCE.**

**Concrete computation (independently reproduced, `sympy`+`numpy`):**

```text
F1: solve [X,σ_i]=0 over all 8 real DOF of X∈M₂(C) → solution {a:d, b:0, c:0} = C·I₂ (scalar commutant). FAITHFUL.
F2: CAR(2) by Jordan-Wigner on 2 modes, closed algebra dim = 16 = M₄(C) (unique irrep dim 4 > 2). K0 stays dim 2.
F3: on (2π/L)Z³ grid (L=4): max‖[H_K0,σ_i]‖ = 0.0  vs  max‖[H_K1,σ_i]‖ = 2.8 (>0). K0 fails ONLY F3.
ray equivalence (sympy): [aI + i b σ_x, σ_y] = diag(−2b, 2b) ⇒ = 0 iff b=0 ⇒ F3 ⇔ φ=−1.
```

---

### ROUTE 5 — Graded locality beyond simple statistics

**Thesis.** Graded locality is a principle on the cross-site EXCHANGE SIGN
(statistics bit `ε`), which is provably orthogonal to the kinetic-order bit `φ`.
It does NOT force `φ = −1`; `K0` survives as a runner-certified countermodel.

**Does `K0` fail?** **NO — `K0` survives.** The kinetic-order bit `φ` and the
statistics bit `ε` factorize, and graded locality only constrains `ε`.

**Structure.** Two independent bits on the substep-1 surface: `ε ∈ {+1,−1}`
(hard-core boson commuting vs CAR anticommuting), and `φ ∈ {+1,−1}` (kinetic
order). `φ` is computed on STATISTICS-FRAME-INVARIANT data: the JW/Klein strings
cancel on nearest-neighbor bilinears, so the NN hopping Hamiltonian coincides in
the HCB and CAR frames up to a site-local `U(1)` frame, with IDENTICAL spectrum,
and the frame-invariant plaquette flux `Φ_P` (whose sign IS `φ`) is a c-number
function of the hopping COEFFICIENTS only — untouched by the frame change. So the
two bits factorize `{φ}×{ε}` and graded locality, which at most picks `ε`, cannot
move `φ`. The steelman — the GL_F multi-loop graded-net cocycle no-go
([`GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md`](GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md),
runner `PASS=44`, `proposal_allowed=false`) — formalizes the FULL graded-net
structure (MC1–MC4) and its classification theorem returns the symmetric SET
`{ε≡+1, ε≡−1}`: the commuting hard-core assignment passes every condition (a
runner-certified countermodel); the only frame-odd loop datum squares to `+1`,
satisfied by both signs. `K0` is itself a legitimate graded object on the same
graded Hilbert space with `F = ⊗σ₃`: F-even, Hermitian, full `O_h`, `[H_K0,σ_i]=0`.
None of MC1–MC4 reference the kinetic bilinear's flux.

**Circularity verdict.** As a clean input, graded locality (from the qubit
substrate + the retained parity grading `F`, both primitives) is NON-circular —
and that is why it is inert on `φ`. The only `φ`-touching variant ("the time
generator acts as an odd degree-+1 super-derivation with linear-in-momentum
symbol") is disqualified twice: the linear-symbol half is the `|E|=|p|` cone
(circular); the F-odd half BREAKS charge conservation (`[Q,H]≠0`), violating the
accepted `Q`-conserving kinetic surface (every legitimate `Q`-conserving NN
bilinear is F-even).

**Outcome: DOES NOT FORCE.**

**Concrete computation (independently reproduced, `numpy`):**

```text
open NN chain N=4, K0 (t≡1):
  H_HCB (ψ=σ⁺) vs H_CAR (c=(∏σ_z)σ⁻): coincide UP TO a site-local U(1) frame.
    precise JW telescoping: c†_{k+1}c_k = σ⁺_{k+1} σ_z^{(k)} σ⁻_k = −σ⁺_{k+1}σ⁻_k  (σ_z σ⁻ = −σ⁻),
    so H_CAR = −H_HCB per oriented bond; absorbed by u_k=(−1)^k ⇒ identical spectrum, identical flux.
  exchange algebra genuinely differs: HCB [ψ_0,ψ_2]=0 (commute);  CAR {c_0,c_2}=0 (anticommute) ⇒ real ε.
  plaquette flux (coefficient-only, frame-invariant): K0 → +1, K1 → −1.
  [F,H_K0]=0 and [Q,H_K0]=0 (F-even, charge-conserving).
  F-odd candidate (single σ⁺): {F,H}=0 BUT [Q,H]≠0 ⇒ breaks charge conservation (illegitimate).
```

---

## VERDICT

> **`φ = −1` is an IRREDUCIBLE DYNAMICS POSIT.**
> It is not discharged, and not conditionally dischargeable on P2 / P3 / A3.

No route forces `φ = −1` from axioms + accepted primitives non-circularly.
`K0 = (Σ_μ cos p_μ) I₂` is a genuine, independently re-certified COUNTERMODEL on
every non-circular route:

| Route | `K0` fails? | circularity | outcome |
|---|---|---|---|
| 1 Off-staggered RP | **NO** — `K0` is the survivor; off-staggered RP selects `K0`, `K1` rescued only by circular staggered 2-step | non-circular; points the wrong way | **does not force** |
| 2 Isolated-zero | **YES** — but by an UNSUPPLIED predicate | pure form non-circular but unsupplied; FSB-K strengthening circular | **conditional on new premise** |
| 3 Kinetic isotropy P2 | **NO** — both orders pass axis-isotropy; KG scalar has isolated isotropic order-2 zero | P2 clean but inconclusive; P2+linear-cone circular | **does not force** |
| 4 Irreducibility/no-spectator | **NO** — passes F1+F2; F3 ⇔ `φ=−1` (re-posit) | landed boost-faith no-go pattern (re-posit, not derivation) | **does not force** |
| 5 Graded locality | **NO** — runner-certified countermodel; `φ ⟂ ε` | non-circular but inert on `φ`; F-odd variant breaks `[Q,H]=0` | **does not force** |

**Best route for an auditor to scrutinize: Route 2.** It is the ONLY route that
genuinely excludes `K0` by a non-circular, geometry-blind principle (a second-order
comparator with point-zeros `1,1,1` passes it, so it is not a disguised Dirac
assumption). It fails only on AUTHORITY. It therefore pins the residual to the
cleanest, smallest, most defensible missing primitive.

### Minimal posit for the axiom ledger

To make the upper leg unconditional, ADMIT — as a NEW framework primitive, NOT
derivable from Lattice / Quantum / Record / P2 / P3 / A3 — the
**finite-massless-sector / kinetic-order primitive** (clause B-Z2 of the P-FLUX
no-gos):

```text
"The realized matter kinetic kernel has a FINITE, point-like massless zero set —
 finitely many propagating zero modes per Brillouin zone; equivalently ker = carrier,
 with no extra massless sectors beyond the embedded carrier."

Equivalent action-level form on the equivariance-forced two-ray surface
M_μ = a·I + i·b·σ_μ:
"the realized NN charge-conserving kinetic bilinear lies in the flux(−1) class,
 i.e. b ≠ 0 (its coupling matrix is not ∝ I₂; it does not commute with all σ_i)"
 — which is logically identical to φ = −1.
```

**Bar.** The WEAKER pure-finiteness form is non-circular (geometry-blind: a
second-order point-zero operator satisfies it) but unsupplied. Adding the
conical/linear cone `|E|=|p|` (the FSB-K strengthening) would make it forcing but
is CIRCULAR (the Dirac-form assumption). The minimal admissible posit is the
**pure finite-zero-set clause**, with the explicit understanding that it does NOT
by itself entail linear dispersion — strictly weaker, and more defensible, than
importing the linear cone.

### Per-route escape conditions (what each route would need to close `φ = −1`)

1. **Route 1 (off-staggered RP)** would close `φ=−1` only if an off-staggered,
   geometric-time-reflection positivity functional PENALIZED the bounded-below
   second-order scalar Laplacian relative to the first-order Dirac operator — i.e.
   `K0` FAILS single-step Euclidean transfer positivity while `K1` PASSES.
   **CONFIRMED FALSE** (`K0` 0/120, `K1` 120/120). Positivity/stability provably
   cannot do this (scalar bounded below; naive Dirac has a negative branch). The
   only `K1`-favoring variant requires the staggered 2-step ⇒ staggered-circular.
2. **Route 2 (isolated-zero)** would close `φ=−1` if the finite/point-like-zero
   clause (B-Z2) were entailed by an accepted primitive, OR were admitted as a new
   primitive. **CONFIRMED UNSUPPLIED** (A3 finiteness = registered OUTCOMES in a
   supplied decomposition, not propagator support; P3 forbids selecting among
   law-admissible laws; per-volume entropy density `N0·ln2/V → 0` on BOTH
   branches; per-volume IR log-det divergence coeff `2N0/V → 0` on BOTH). Escape:
   ADMIT a "finite-species-density / no-flat-zero-band" primitive — the cleanest
   path — but its only working strengthening (FSB-K) is circular.
3. **Route 3 (kinetic isotropy P2)** would close `φ=−1` if `c_t=c_s` entailed a
   LINEAR cone at the realized zero rather than a quadratic shell. **CONFIRMED
   FALSE**: both orders pass axis-isotropy (`~1e−15`); the massless KG scalar has
   an isolated isotropic order-2 zero (`E²/|p|² = 1.00000000`). The needed premise
   `E=|p|` IS the circular Dirac cone; P2 supplies no selector.
4. **Route 4 (irreducibility)** would close `φ=−1` if A2 entailed DYNAMICAL
   faithfulness of the FREE kinetic sector (`[H_kin,σ_i]≠0`). **CONFIRMED
   non-entailment**: A2 "does not supply a dynamics"; the qubit is exercisable by a
   mass term or Record; and `[H_kin,σ_i]=0 ⇔ b=0 ⇔ φ=+1`, so positing kinetic
   faithfulness IS positing `φ=−1`. Escape: an owner-approved "kinetic-sector
   dynamical faithfulness" admission (= the selector restated).
5. **Route 5 (graded locality)** would close `φ=−1` if a `Z₂`-graded-net principle
   forced the time generator to be an odd degree-+1 super-derivation with
   linear-in-momentum symbol. **CONFIRMED illegitimate/circular**: `φ` factorizes
   from `ε` (NN hopping coincides up to a site-local `U(1)` frame; flux
   frame-invariant); the multi-loop cocycle no-go classifies `ε` as the SET
   `{+1,−1}`; the F-odd operator breaks `[Q,H]=0`; the linear-symbol half is the
   circular cone. Escape: an emergent-continuum Haag–Kastler graded local net
   tying grading to dynamics — but that requires emergent Lorentz (the linear
   cone), circular for THIS claim and a different frontier than the static
   baseline where `d≤3` must be discharged.

---

## IMPACT

### On the `d ≤ 3` upper leg

Because `φ = −1` is irreducible on the current primitive set, the `d ≤ 3` leg of
the dimension derivation **rests on this dynamics posit**. On the `K0` countermodel
the qubit spectates and the `M₂(ℂ)` anticommutant cap is **VACUOUS**, so `d ≤ 3` is
**NOT unconditional**. The leg is exactly as strong as the conjunction of the named
posits in
[`D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md`](D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md)
(Clause A `φ = −1`, UNAUDITED). This note does not weaken that clause; it
adversarially confirms it is irreducible and names the smallest admission that
would discharge it.

### On weakening A1 to `Zᵈ`

`A1` cannot be weakened from the `Z³` lattice primitive to a derived `Zᵈ` cap
without this dynamics posit. The `M₂(ℂ) = Cl(3,0) = GA(3)` match remains a
**consistency, not a derivation** of spatial `d` (the #2586 / index-pairing
line-117/line-180 guardrail). Nothing here relocates `d = 3` onto the matter/Dirac
dynamics; it isolates the one bit that would have to be admitted to do so honestly.

### What an audit must check (if a future admission is contemplated)

- The pure finite/point-like-zero clause (B-Z2) is genuinely NOT entailed by
  Lattice / Quantum / Record / P2 / P3 / A3 (verify against the actual primitive
  texts; confirm the wave-2/wave-3 P-FLUX "no retained supplier" finding still
  holds).
- The FSB-K composer does NOT discharge `φ` for the axiom-grade question: its
  binding clause is the finite-species-density requirement in thermal currency,
  and its `(Z)` certificate bundles the circular isotropic linear cone; the
  selection is WITHIN the unaudited two-class surface at `retained_bounded` grade.
- The two-flux-class collapse is exhaustive (translation + 24 cubic rotations up to
  site-local `U(1)` ⇒ exactly `M_μ = a·I + i·b·σ_μ`), so Route 4's F3-forcing is a
  re-posit, not a derivation.

---

## RUNNER SPECS (deterministic; no fitted params, no network, no randomness)

Each verdict above has a checkable runner. The specifications below are the ones
this proposal independently reproduced; an audit lane can re-run them.

### RS-1 — Off-staggered transfer-matrix positivity (`K0` vs `K1`)

```text
for mode ∈ {K0, K1}, m ∈ {0.1,0.5,1.0}, p ∈ linspace(0.01, π−0.01, 40):
  T_K0(m,p) = [[2 + m² + 2(1−cos p), −1],[1, 0]]
  T_K1(m,p) = [[−2(m + i sin p), 1],[1, 0]]
  flag "RP-fail at (m,p)" if max|Im eig(T)| > 1e−9 OR any real decaying eigenvalue ≤ 0; same for T².
assert K0 fail-count == 0 (both T and T²); K1 fail-count == 120 (both).
Hamiltonian-vacuity guard: H_K0=(Σcos p_μ)I₂, H_K1=Σ σ_μ sin p_μ on Z³ (L=4); both Hermitian, both
  e^{−aH} PSD (min eig > 0) ⇒ Hamiltonian-level RP cannot separate the rays.
staggered-rescue guard: T_odd·T_even with α_even=m+i sin p, α_odd=m−i sin p ⇒ real-positive 0/120,
  decaying eigenvalue == e^{−2E}, E=arcsinh√(m²+sin²p), to ~1e−16; non-staggered T² stays non-positive.
VERDICT: route forces φ=−1 IFF K0 fail-count>0 AND K1 fail-count==0. OBSERVED: the reverse ⇒ does_not_force.
```

### RS-2 — Zero-set counting + continuity (`K0` extensive vs `K1` point-like)

```text
build single-mode hopping on Z³ PBC: h_K0 (t≡1) and h_K1 (t1=1, t2=(−1)^x1, t3=(−1)^{x1+x2}).
for L ∈ {4,8,12}: assert dim ker h_K1 == 8 (constant); dim ker h_K0 ∈ {20,68,140} (strictly increasing).
sympy: assert cos(π/2+t)+cos(π/2−t)+cos(π/2) == 0 for symbol t (K0 zero set non-discrete);
       assert K1 band 2√(Σ sin² p_μ)=0 ⇔ p ∈ {0,π}³ (exactly 8 points).
non-vacuity/geometry-blindness: predicate FINITE_POINTLIKE over {K0, K1, scalar-NN+on-site(−6)}
  must return {FALSE, TRUE, TRUE} (a 2nd-order operator also passes ⇒ predicate ≠ Dirac assumption).
supplier-absence guard: assert no clause in {Record, realized_state, kinetic_isotropy} texts bounds the
  kinetic-kernel zero-set cardinality ⇒ predicate is an unsupplied posit ⇒ conditional_on_new_premise.
```

### RS-3 — Cone isotropy / order (P2 blindness)

```text
Euclidean symbols on Z³×Z_tau: S_E=Σ_μ(1−cos p_μ) (2nd order); |D|²=Σ_μ sin² p_μ (1st order).
(1) assert exact invariance under all 24 axis permutations for BOTH (max dev < 1e−12) ⇒ P2 cannot separate.
(2) fit log|symbol| vs log|p| along ≥20 directions ⇒ scalar order 2, Dirac order 1; direction variance < 1e−6.
(3) for massless KG scalar: assert E²/|p|² → const isotropically at the isolated zero p=0 (var < 1e−6)
    ⇒ a SECOND-order theory passes "isolated + isotropic cone" ⇒ the sharpening does NOT exclude K0.
VERDICT: PASS = PASS (no separation) ⇒ does_not_force; the residual is the ORDER bit, not isotropy.
```

(Routes 4 and 5 carry checkable guards too — F1 commutant nullspace = `C·I₂`;
`CAR(2)` algebra dim = 16; `‖[H_K0,σ_i]‖ = 0` vs `‖[H_K1,σ_i]‖ > 0`; ray
equivalence `[aI+ibσ_μ,σ_i]=0 ⇔ b=0`; HCB/CAR NN hopping equal up to site-local
`U(1)` with frame-invariant flux; F-odd kinetic bilinear breaks `[Q,H]=0` — all
reproduced above.)

---

## WHAT THIS DOES NOT CLAIM / HONEST RESIDUALS

- It does **not** claim `φ = −1` is false, unphysical, or unnatural. It is the
  physically expected Dirac ray; the claim is only that it is **not forced** by
  axioms + accepted primitives non-circularly.
- It does **not** claim `K0` is the physical kinetic term. `K0` is a COUNTERMODEL
  exhibiting that the constraint set is too weak to exclude the scalar ray — it is
  the witness, not a proposal for nature.
- It does **not** set or change any audit status, retire any axiom, register any
  primitive, or perform any closure. The minimal posit named above is a candidate
  for a future owner+audit admission decision, nothing more.
- **Negative-result honesty (Routes 1, 3, 4, 5).** Four routes return DOES NOT
  FORCE. I cannot exclude that a cleverer functional in some route's class could
  be engineered to favor `K1`, but any such functional in Route 1's class would
  have to penalize the bounded-below scalar Laplacian relative to an
  unbounded-below first-order operator — the opposite of what positivity/stability
  does. I judge the four negatives strong; Route 2 is the only genuine non-circular
  exclusion, and it fails on supplier authority.
- **Route 1 caveats.** (a) The single-mode reduction collapses the spatial sector
  to a scalar magnitude; the full `C²` spinor temporal transfer only HURTS `K1`
  further (more strongly non-Hermitian) and leaves `K0` real-symmetric, so the
  verdict is robust. (b) I used the canonical geometric time reflection; I did not
  exhaustively scan all lattice-axiom-licensed reflection planes — but the
  time-direction reflection is the canonical OS comparator and the one the staggered
  authority uses. (c) The Hamiltonian-guard min-eig of `e^{−aH}` depends on the
  chosen `a` and finite-`L` grid; my `L=4`, `a=1` values (`0.0498`, `0.1769`)
  differ numerically from a different `(a, grid)` choice but the load-bearing fact
  (both PSD) is convention-independent.
- **Route 5 precision residual (recorded honestly).** The exact Jordan-Wigner
  telescoping gives `c†_{k+1}c_k = σ⁺_{k+1} σ_z^{(k)} σ⁻_k = −σ⁺_{k+1}σ⁻_k`
  (because `σ_z σ⁻ = −σ⁻`), so the HCB and CAR NN hopping matrices differ by `−1`
  per oriented bond — they coincide **up to a site-local `U(1)` frame**
  (`u_k=(−1)^k`), NOT "entrywise identical" as loosely stated in some upstream
  phrasings. This is a gauge/convention artifact: the spectrum is identical and the
  **gauge-invariant plaquette flux `Φ_P` is unchanged**, which is exactly the
  quantity on which `φ` is defined. The Route 5 verdict (`φ ⟂ ε`; `K0` survives
  graded locality) is therefore fully intact; only the wording "identical matrix"
  should read "identical up to a site-local `U(1)` frame / flux-invariant."
- **Scope of Route 5's factorization.** It is certified on the STATIC finite-block
  baseline. A genuine emergent-spacetime Haag–Kastler graded local net (graded
  modular/derivation tying grading to dynamics) is not excluded by the finite-lattice
  runners — but that frontier requires emergent Lorentz (the linear cone), which is
  circular for THIS claim and is the OS→Wightman migration, not the static surface
  where `d ≤ 3` must be discharged.
- **The "irreducible" verdict is the valuable outcome.** The wall is well-defended:
  every escape route either points the wrong way (Route 1), is unsupplied
  (Route 2), or re-imports the Dirac/linear-cone assumption it was meant to derive
  (Routes 3–5). Naming the single smallest non-circular admission (finite-zero-set
  clause B-Z2) is the honest, actionable result.

---

## CROSS-REFERENCES (by filename)

- [`D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md`](D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md)
  — the dimension-compression companion; its Clause A is this `φ = −1` bit.
- [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the two-flux-class collapse, the `M_μ = aI + i bσ_μ` two-ray surface, and B-BIT.
- [`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md)
  — the representation-level twin; the linear-cone circularity (lines 84–90).
- [`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the `M₂(ℂ)` anticommutant cap that turns `φ = −1` into `d ≤ 3`.
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  — Route 1 level (A): Hamiltonian-level `E1`–`E4` vacuity.
- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — Route 1 level (C): the staggered 2-step `T_odd·T_even` rescue (circular as a selector).
- [`P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md)
  — Route 2 wave-2: B-Z2 has no retained supplier in Record/readout.
- [`P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md)
  — Route 2 wave-3: thermal clause strictly stronger (also forces conical dispersion).
- [`P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`](P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md)
  — Route 2: the within-surface FSB-K selection that bundles the circular linear cone.
- [`STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md`](STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md)
  — Route 2: cone data `(V,C,r)=(2I,2/3,1)` (Z-K1) vs Z-K0 violation.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — Route 3: P2's defining text ("no selector," only the graining ratio).
- [`EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](EMERGENT_POINCARE_FREE_SECTOR_FROM_KINETIC_ISOTROPY_PRIMITIVE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — Route 3: the landed firewall rejecting P2-as-Lorentz (Audit Note).
- [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
  — Route 4: the landed F2→F3 non-sequitur (Clifford-action / Dimension routes).
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  — Routes 2/3: P3's firewall ("the laws do not pick the state; the world does").
- [`GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md`](GL_F_MULTILOOP_GRADED_NET_COCYCLE_NARROW_NO_GO_NOTE_2026-06-10.md)
  — Route 5: the multi-loop graded-net classification SET `{ε≡+1, ε≡−1}`.
- [`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md)
  — Route 5: statistics frame is flux-invariant (`φ ⟂ ε`).
- [`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — Route 5: GL(F) selects CAR (`ε`) only conditionally on GL(F), and on `ε` not `φ`.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  — the three-axiom baseline (Lattice, Quantum, Record); A2 "does not supply a dynamics."

**Independent audit required.** This note asserts no effective-status change.
