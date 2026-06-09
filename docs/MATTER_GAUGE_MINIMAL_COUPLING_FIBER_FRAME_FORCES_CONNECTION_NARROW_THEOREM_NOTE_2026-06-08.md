# Matter-Gauge Minimal Coupling — The Link Connection Is Forced by Fibre-Frame Independence

**Date:** 2026-06-08
**Type:** narrow theorem (gauge-covariance kinematics) with one named premise
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.py`
**Cache:** `logs/runner-cache/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.txt`
**Status:** source proposal — the gauge-COVARIANCE algebraic core (Parts 1–5, 7 of
the runner) is unconditional; the physical "the connection is forced" reading rests
on one named premise (ADM-1, fibre-frame gauge redundancy). Authority role: source
proposal; the independent audit lane sets downstream status.

## Claim under test

Can the matter–gauge **minimal coupling** — the link connection `U_μ(x)`, the
gauge-covariant hopping `H_cov = Σ a_x† U_μ(x) a_{x+μ} + h.c.`, and the lattice
covariant derivative `(D_μψ)(x) = U_μ(x)ψ(x+μ) − ψ(x)` — be **derived on the
framework surface** rather than imported, using only retained inputs?

The wall-map of the interacting sector records that every prior note using the link
`U_μ = exp(igaA_μᵃTᵃ)` *imports* it: there is no note deriving where the connection
comes from or why a gauge field lives on the `Z³` links. This note fills that gap at
the **kinematic** level (the connection's existence and gauge law), leaving the gauge
**action**/dynamics to the separate Yang–Mills target.

## Verdict

**Yes, at the kinematic level, modulo one named premise.** The link connection and its
parallel-transporter gauge law are **forced** — not chosen — by demanding that the
retained nearest-neighbour hopping be independent of the (unregistered) local choice
of internal fibre frame. The gauge-covariance identity itself is unconditional algebra.

## Retained foundations exercised (statuses verified on the live `origin/main` ledger)

1. **`graph_first_su3_integration_note`** — *retained* (positive_theorem).
   Each site carries an internal **`SU(3)` fibre** = the commutant of the observable
   weak-`su(2)` action on the taste cube; the full retained commutant is
   `gl(3) ⊕ gl(1)`, so the fibre **structure group is `U(3) = SU(3) × U(1)`**, the
   abelian factor "hypercharge-like" (that note's own boundary §"What remains bounded").

2. **`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`**
   — *retained* (positive_theorem). Per-site fermion operators `a_x` with the
   translation law `T_a a_x T_a† = a_{x+a}`. Its decoration
   `hopping_bilinear_hermiticity_theorem_note_2026-05-02` gives the **Hermitian,
   number-conserving nearest-neighbour hopping bilinear** `a_x† a_y + a_y† a_x`.

3. **Axioms LATTICE + QUANTUM.** `Z³` with 6-NN adjacency; **one qubit per site**, so
   distinct sites carry **independent** fibres.

## The named admitted premise (the honest boundary)

**(ADM-1) Gauge redundancy of the fibre frame.** A *local* re-choice of internal fibre
frame `g(x) ∈ U(3)` is a **redundancy of description** — it registers no observable —
and equivalently the framework supplies **no canonical *physical* cross-site fibre
identification** beyond the flat reference `U = I`.

This premise is **strongly supported but not yet a separate theorem:**

- *Frame rotations are unobservable by construction.* The `SU(3)` fibre is, by
  `graph_first_su3_integration_note`, the **commutant** of the observable weak-`su(2)`
  action. Operators in the commutant act *trivially* on the registered (observable)
  content, so a local fibre rotation changes nothing that is recorded. In the record
  ontology, the fibre frame is an **unregistered reconstruction**, not registered
  content — exactly the kind of thing physics must be blind to.

- *Locality forbids a canonical global section.* One-qubit-per-site (QUANTUM) plus
  distinct sites (LATTICE) means each fibre is constructed **intrinsically and
  independently** per site. There is no framework-given isomorphism `V_x ≅ V_{x+μ}`;
  any identification used to write a hopping term is a **choice**, made independently
  at each link. The redundancy is therefore *born local*.

- *Residual to audit.* The retained translation bridge supplies **one** identification,
  `T_a a_x T_a† = a_{x+a}` — the **flat reference** `U = I`. ADM-1 is the statement that
  this reference is a **gauge choice** (physically non-rigid), not a canonical physical
  pinning. Were translation to *rigidly* fix a physical frame, `U = I` would be forced
  and there would be no gauge field. That the commutant frame is unregistered (point 1)
  is precisely why the flat reference is non-rigid — but turning "strongly supported"
  into "derived" is a distinct audit step (cf. the translation bridge's
  `record_invariance_companion`).

**Under ADM-1 the connection is forced. Independently of ADM-1, the gauge-covariance
identities (Parts 1–5, 7) are unconditional algebra** — they hold for any configuration.

## The derivation

### Step 1 — The hopping term silently chooses a cross-site frame

The retained hopping `Σ_x a_x† a_{x+μ} + h.c.` contracts the fibre index of `a_{x+μ}`
(in *some* frame at `x+μ`) with that of `a_x†` (in *some* frame at `x`). Writing it as
`Σ_{x,i} a_{x,i}† a_{x+μ,i}` presupposes that "frame label `i` at `x`" means the same as
"frame label `i` at `x+μ`". By LATTICE+QUANTUM there is no canonical such identification.

### Step 2 — Local frame change breaks the naive hopping

A local frame re-choice acts as `a_x → ρ(g(x)) a_x`, `g(x) ∈ U(3)`. Under a **global**
`g`, the naive hopping is invariant (`g†g = I`). Under a **local** `g(x)` it is **not**:
`a_x† a_{x+μ} → a_x† ρ(g(x))† ρ(g(x+μ)) a_{x+μ} ≠ a_x† a_{x+μ}` unless `g(x)=g(x+μ)`.
*(Runner Part 1: free hopping is global- but not local-invariant.)*

### Step 3 — Frame-independence forces the connection

To make the retained hopping independent of the arbitrary local frame, introduce a
compensating **link variable** `U_μ(x) ∈ ρ(U(3))` and define the **covariant hopping**

```
    H_cov = Σ_{x,μ} a_x† U_μ(x) a_{x+μ} + h.c.
```

`H_cov` is invariant under the local frame change **iff** `U_μ(x)` transforms as

```
    U_μ(x)  →  ρ(g(x)) U_μ(x) ρ(g(x+μ))† .                    (parallel-transporter law)
```

This is precisely the gauge-transformation law of a **lattice connection** on the link
`(x, x+μ)`. The central identity, verified exactly,

```
    G H_cov[U] G†  =  H_cov[U'],     U'_μ(x) = g(x) U_μ(x) g(x+μ)† ,
```

(`G = ⊕_x ρ(g(x))`) holds to `6×10⁻¹⁵` *(Runner Part 2)*. Hence the spectrum of
`H_cov` is a gauge invariant.

### Step 4 — The law is unique; `D_μ` is forced

Every other site-assignment (`g(x)Ug(x)†`, `g(x+μ)Ug(x)†`, one-sided) **breaks**
covariance *(Runner Part 3)*. The associated **lattice covariant derivative**
`(D_μψ)(x) = U_μ(x)ψ(x+μ) − ψ(x)` transforms covariantly, `(D'_μψ')(x) = g(x)(D_μψ)(x)`,
while the naive difference `ψ(x+μ)−ψ(x)` does not *(Runner Part 4)*. The connection is
exactly what repairs the difference operator.

### Step 5 — Gauge-invariant content = closed loops; minimal-coupling form

Closed-loop holonomies (plaquette traces `Tr U_p`) are gauge invariant; open Wilson
lines `Tr U_μ(x)` are not *(Runner Part 5)* — the physical, registered content is the
**closed-loop** data. Writing `U_μ = exp(iε A_μ)` with `A_μ` Hermitian (algebra-valued
connection), the covariant difference reduces at leading order to
`D_μ = ∂_μ^{lat} + i A_μ` — the **minimal-coupling form** `∂_μ + ig A_μ` — with the
residual confirmed `O(ε²)` (log–log slope `2.00`) *(Runner Part 6)*. The same argument
with `g(x) = e^{iθ(x)}I` forces an **abelian (hypercharge-like) connection** for the
`U(1)` factor *(Runner Part 7)*.

## What the runner verifies (`PASS=23 FAIL=0`)

- `U_μ(x)`, `g(x) ∈ SU(3)`; `H_free`, `H_cov` Hermitian; `U=I` ⇒ retained free hopping.
- Free hopping global-invariant, **not** local-invariant (the problem is real).
- **Central:** `G H_cov[U] G† = H_cov[U']` under the transporter law (to `6e-15`);
  spectrum gauge-invariant.
- Transporter law **unique** — four wrong site-assignments all break covariance.
- `D_μ` covariant, naive `∂_μ` not.
- Plaquette holonomy gauge-invariant, open line not; flat connection trivial holonomy.
- Leading-order minimal coupling `D_μ = ∂_μ + iA_μ`, residual `O(ε²)` (slope `2.00`).
- `U(1)` factor forces an abelian connection by the same argument.

## What this closes

- The matter–gauge **minimal-coupling kinematics** are moved from *entirely admitted*
  to *derived on the framework surface* (modulo ADM-1): the link connection, its gauge
  law, the covariant derivative, and gauge invariance of `H_cov` are **forced** by
  frame-independence of the retained hopping on the retained `U(3)` fibre, not imported.
- A reusable on-surface origin for the gauge field: it is the **bookkeeping of the
  framework's absent canonical cross-site fibre identification** — the unregistered
  internal frame — rather than a postulated `U_μ = exp(igaA)`.

## What this does NOT close

- **No gauge action / dynamics for `U_μ`.** This is pure kinematics: `U_μ` here is a
  background connection, not a dynamical field with a Yang–Mills/Wilson/heat-kernel
  action. Deriving that action is the separate sub-target (cf.
  `bridge_gap_action_form_uniqueness_no_go_note_2026-05-06` and the heat-kernel lane).
- **No continuum limit, no coupling value.** Part 6 is a leading-order consistency
  check, not an `a→0` statement; `g` and `g_bare=1` are untouched.
- **No physical `SU(3)_c` identification beyond the algebraic fibre** — deferred exactly
  as in `graph_first_su3_integration_note`; the abelian factor remains "hypercharge-like"
  pending the anomaly-complete identification.
- ADM-1 is **named, not discharged**: that the local fibre frame is physically
  non-rigid (a gauge redundancy) is strongly supported by the commutant/record-ontology
  argument but is its own audit target.

## Scope and non-claims

The covariance theorem (Steps 3–4) is an exact finite-dimensional identity, verified at
`(L=2)³` with `C³` fibres; it is representation-independent (depends only on `g†g=I`).
This note adds **no new axiom or import**: it uses the two cited retained theorems plus
LATTICE+QUANTUM, and cites the standard fibre-bundle/connection correspondence only as
mathematical method. The "connection is forced" reading is conditional on the named
premise ADM-1; the algebraic core is not.

## Cross-references

- Retained fibre: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
- Retained operators/translation: [`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
- Hopping bilinear (decoration): [`HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md`](HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md)
- Downstream (gauge action, separate target): [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
- Standard method (not an import): lattice gauge connection / parallel transport
  (Wilson 1974; Kogut–Susskind 1975); fibre-bundle origin of gauge fields.
