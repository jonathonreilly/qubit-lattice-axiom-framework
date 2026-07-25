# Wave 1 — Selection principles: inventory and intersection

**Campaign:** matter-action-measure-campaign-20260725
**Wave:** 1 (selection-principle inventory + decisive intersection)
**Worked against:** `origin/main` @ `e192e332f2` (fetched 2026-07-25)
**Author role:** campaign worker. This file sets no audit verdict, predicts
none, adds no axiom, adds no primitive, adds no repo vocabulary, and edits no
repo surface. Nothing here is a gate.

---

## 0. Headline

**The intersection of every framework-native constraint currently identifiable
on the matter action is NOT a singleton.** Two physically inequivalent
matter actions — `K0` (uniform plaquette flux `+1`, scalar tight-binding) and
`K1` (uniform plaquette flux `−1`, Kawamoto-Smit / staggered) — satisfy every
one of the nine candidate constraints, including the three the campaign brief
flagged as most likely to cut (reflection positivity, microcausality /
Lieb-Robinson, `kinetic_isotropy_primitive`). A third, `Φ = I − SWAP`, survives
if the licensed-bilinear surface declaration is also dropped.

The nine constraints partition sharply:

- **Two of them cut hard, together, and then stop.** Hermiticity + finite-range
  + translation + proper-cubic covariance (up to site-local frame) cut the sign
  systems on a unit cube from `2^12 = 4096` to exactly **2** classes. That is
  the entire cut. Every subsequent constraint cuts **zero further**.
- **Seven of them cut nothing at all on the surviving pair.** Reflection
  positivity, Lieb-Robinson microcausality, `c_t = c_s`, Record readout,
  Admissibility, gauge covariance, and the doubling/QCA constraints are each
  satisfied by both `K0` and `K1`, and I show why each is *structurally* unable
  to separate them, not merely untested.

The residual is therefore exactly **one gauge-invariant, frame-invariant bit**
(the plaquette flux `φ = ±1`), plus the surface declaration that licenses the
bilinear form in the first place, plus the statistics/measure frame. This bit
is the repo's already-named `B-BIT`; **1450 ledger rows sit downstream of it**
(`docs/STAGGERED_DIRAC_PKIN_SUBTREE_CURRENT_SURFACE_RESTATEMENT_NOTE_2026-07-03.md:31-36`).

This is a **strengthening**, not a rediscovery: the two-class collapse and the
non-forcing of the bit are landed prior art (§5). What is new in this wave is
(a) the *complete* intersection — the six constraints the prior notes explicitly
declined to impose or left open as future selectors are now shown neutral, with
the structural reason in each case; and (b) the closure of the specific escape
route the prior note names at
`docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:386-392`.

---

## 1. Mandatory framework refresher — surfaces read

Read in full this wave (not from memory):

1. `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 194 lines).
2. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all 47 lines).
3. `docs/audit/data/axiom_premise_nodes.json` — `canonical_ids` =
   `['minimal_axioms', 'scale_reference_primitive', 'kinetic_isotropy_primitive',
   'realized_state_primitive']`.
4. Source note of the one approved primitive this wave invokes:
   `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (all 100 lines). I did
   **not** invoke `scale_reference_primitive` or `realized_state_primitive` as a
   premise anywhere below; both are named only as rescue routes that fail.
5. `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`
   (the obligation whose first conjunct this campaign targets, lines 19-24).

All status claims below are read from `docs/audit/data/ledger/` shards
directly. Prose status labels are used **only** as objects of correction (§6).

### 1.1 Well-posedness kill-check (campaign hard rule 1)

`MINIMAL_AXIOMS_2026-06-29.md:103-111` states verbatim:

> Admissibility is not a dynamics axiom. [...] It does not choose a Hamiltonian
> or transfer operator, supply transition probabilities or weights, select a
> scalar or nonzero kinetic branch, assert a Dirac-square carrier, define a time
> metric, or provide a record-production process or physical persistence
> dynamics.

and `:170` lists "source/action and physical-observable identification" among
the gates that "remain outside axiom content".

**Kill-check verdict: the obligation is well-posed only in the "axioms + approved
primitives + selection principles" reading, and this wave adopts that reading.**
The "from the four axioms alone" reading is dead on the axiom memo's own text, and
is already independently killed by an explicit countermodel
(`docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:239-244`).
So the only live question is the one this wave answers: **does the set of
framework-native constraints, taken together, cut the menu to a point?**

---

## 2. The two objects that the whole inventory is scored against

Both are existing repo objects, not new constructions. On the adjacency-licensed,
`Q`-conserving nearest-neighbor bilinear surface over the one-qubit-per-site
carrier, the kinetic family is

```text
H_t = sum_{x, mu} ( t_mu(x) a^dag_{x+mu} a_x + conj ),      t_mu(x) in C
```

with frame redundancy `t_mu(x) -> conj(u(x+mu)) t_mu(x) u(x)` and
frame-invariant plaquette flux
`Phi_P = t_mu(x) t_nu(x+mu) conj(t_mu(x+nu)) conj(t_nu(x))`
(`docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md:247-257`).

```text
K0 :  phi = +1,  representative t == 1            (scalar tight-binding)
K1 :  phi = -1,  representative eta^0             (Kawamoto-Smit)
      eta^0_1 = 1, eta^0_2 = (-1)^{x_1}, eta^0_3 = (-1)^{x_1+x_2}
```

They are separated by three frame-invariant, gauge-invariant data
(worker probe §7, checks B2/B3/B4):

| datum | `K0` | `K1` |
|---|---|---|
| uniform plaquette flux | `+1` | `−1` |
| zero modes on the `4^3` torus | **20** | **8** |
| infinite-volume zero set | extensive surface `sum_mu cos k_mu = 0` | 8 isolated Dirac points |

The zero-set difference is a difference in **kinetic order** — quadratic vs
linear low-energy dispersion. These are not two presentations of one theory.

A third object is needed only for the axiom-level row: `Φ_{x,y} = I − SWAP_{x,y}`
(`docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:190-235`),
whose one-particle generator is the cubic graph Laplacian with symbol
`2 sum_mu (1 − cos k_mu)`, zero only at the origin.

---

## 3. THE INVENTORY

For each constraint: **(i)** native or import, with source; **(ii)** what it
excludes; **(iii)** what survives; **(iv)** first artifact that would test it.

Column "cut" = how much of the menu it removes *given the constraints above it*.

| # | Constraint | Native? | Cut |
|---|---|---|---|
| C1 | Hermiticity / self-adjointness | **native** (structural) | large, but does not touch `φ` |
| C2 | Locality / finite range (NN adjacency) | **native**, Lattice axiom | large, but does not touch `φ` |
| C3 | Proper-cubic + translation covariance | **native**, Lattice axiom | **`4096 → 2`; the entire cut** |
| C4 | Reflection positivity | native surface, **but structurally neutral** | **zero** |
| C5 | Microcausality / Lieb-Robinson | native, **but implied not imposed** | **zero** |
| C6 | `kinetic_isotropy_primitive` (`c_t = c_s`) | **native primitive**, boundary forbids use | **zero** |
| C7 | Record-compatibility (fixed content-determined readout) | **native**, but readout is kinetic-blind | **zero** |
| C8 | Admissibility as a local constraint | **native**, but availability ≠ kinetic coefficients | **zero** |
| C9 | Gauge covariance | not axiom-native; and neutral either way | **zero** |
| C10 | Doubling / no-doubling; QCA triviality | **not native** (species count is nowhere in the axioms) | **zero** |

### C1 — Hermiticity / self-adjointness

**(i) Native, structurally.** Not an axiom clause. It is forced once one asks for
a self-adjoint generator on the Qubit axiom's `M_2(C)` carrier; the kinetic
family above is Hermitian by construction
(`...KINETIC_CLASS_FORCING...2026-06-10.md:264-267`, constraint K1). No import.

**(ii) Excludes** non-Hermitian hopping systems, and — via the interaction with
C3 — is what forces `φ = conj(φ)`, hence `φ ∈ {+1, −1}` rather than a
`U(1)`-valued uniform flux. Probe check A7 rebuilds this: on the unimodular
circle, `φ = conj(φ)` has solution set exactly `{θ = 0, π}`; the uniform-flux-`i`
Landau-type class is rejected.

**(iii) Survives:** the entire two-parameter-per-edge complex family, modulo
frame. Hermiticity alone removes no class.

**(iv) First artifact:** none needed — already certified inside the two-class
theorem's own runner.

### C2 — Locality / finite range

**(i) Native.** `MINIMAL_AXIOMS_2026-06-29.md:37-38`: "Physical sites are the
points of the cubic lattice `Z^3`, with nearest-neighbor adjacency". The
nearest-neighbor **support** is read off the adjacency license; the repo flags
this explicitly as license-not-derivation
(`...KINETIC_CLASS_FORCING...2026-06-10.md:113-114`, boundary B-S2).

**(ii) Excludes** next-nearest-neighbor and longer-range kinetic terms. This is
a genuinely large cut: the note's falsification leg D3 shows an NNN **continuum**
of classes reappears the moment the license is dropped
(`...2026-06-10.md:377-380`).

**(iii) Survives:** all NN systems. Does not touch `φ`.

**(iv) First artifact:** a derivation (not a license) that the physical
matter action's support is exactly the Lattice adjacency. Absent this, the NNN
continuum is a live second axis of underdetermination, strictly larger than the
one bit reported here.

### C3 — Proper-cubic + translation covariance — **the only constraint that cuts**

**(i) Native.** `MINIMAL_AXIOMS_2026-06-29.md:37-38` supplies "standard
translations, and proper cubic rotations about each site"; `:40-41` supplies "No
site is privileged." The covariance rubric used is the equivariance/no-selector
licensing lemma L-EQ (`...2026-06-10.md:229-240`).

**(ii) Excludes:** everything anisotropic, everything position-dependent beyond
frame, and every non-real uniform flux. Worker probe §7 section A rebuilds the
cut natively and exactly on the unit cube:

```text
sign systems on the 12 cube edges            4096
  -> uniform flux +1                          128     <- one Z2 gauge orbit
  -> uniform flux -1                          128     <- one Z2 gauge orbit
  -> non-uniform flux                        3840     <- excluded
survivors modulo site-local gauge:              2
```

That is a `2048:1` compression, and it is **the whole of the framework's
selective power on this surface**. Probe check F3 additionally verifies that all
24 proper cubic rotations preserve the flux class of **both** `K0` and `K1` — so
C3 is exactly balanced between them, by construction.

**(iii) Survives:** exactly `{K0, K1}`.

**(iv) First artifact:** already exists —
`scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py`. The
first *new* artifact worth building is the same census on a **2-mode-per-site**
carrier, where the note itself records that a one-parameter Wilson continuum
`M_μ(r) = γ_μ + r I` survives all symmetry constraints
(`...2026-06-10.md:349-357`). That continuum is killed here only by the
single-mode qubit-reframe closure — i.e. by the Qubit axiom's one-site
`M_2(C)`. The sharpness of the whole result rides on that.

### C4 — Reflection positivity — **structurally neutral; the named escape route closes**

**(i) Native surface, and the repo has a lot of it.** But note two live-ledger
facts that the campaign brief's framing does not carry:

- `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28` is
  **`audited_failed`** (terminal, 2026-07-21, `gpt-5.6-sol`). The two-step
  blocked transfer positivity named in the brief is *not* standing landed
  content. Its re-audit note asks for "an explicit two-slice Berezin integration
  establishing the residue, CAR metric, reflected inner product, and coherent-state
  normalization before identifying the physical transfer kernel with the decaying
  recurrence eigenchannel."
- The standing on-main RP-surface note,
  `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md`,
  is `unaudited`. This session's own d-dim landing (`fd883a3de1`) records in its
  commit body that `C = 1` is pinned *relative to* a supplied kernel form, and
  that the form "is a conditional input at every `d` incl. the landed `d = 1`".
  The RP lane **consumes** a matter action; it does not produce one.

  *Hygiene note.* A file
  `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_EXTENSION_BOUNDARIES_..._2026-07-24.md`
  exists **untracked** in this worktree and is **not on `origin/main`**
  (`git cat-file -e origin/main:<path>` fails; no ledger shard exists). I read it
  during recon and have excluded it from every load-bearing use below. Wave 2
  should not cite it as landed.

**(ii) What RP excludes — and why it cannot reach `φ`.** Three readings, all
neutral:

1. **Hamiltonian / continuous-Euclidean-time reading.** For any self-adjoint `H`,
   `T = exp(−a_τ H) = (exp(−a_τ H/2))^dag (exp(−a_τ H/2))` is a positive
   operator. Positivity of the transfer operator is therefore *implied by*
   hermiticity (C1), so it can add nothing beyond C1. Probe checks C1/C2 verify
   the spectra of both `K0` and `K1` are exactly real at `L = 2`
   (`K0`: `{−6, −2, 2, 6}`; `K1`: `{−2√3, 2√3}`).
2. **Lagrangian / staggered-action reading — the on-main RP theorem's own
   quantifier already admits both branches.** The standing on-main 3+1 RP surface
   note states its theorem for an *arbitrary* hop of the right algebraic type, not
   for the staggered phases specifically:
   `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:388`
   — "succeeds for **arbitrary finite-dimensional real anti-Hermitian `H`**" — and
   `:466` lists "arbitrary finite real anti-Hermitian spatial hop" as an in-scope
   carrier. So the load-bearing hypothesis of the repo's own RP theorem is
   *anti-Hermiticity of the spatial hop*, nothing more.

   Natively (probe checks C3/C4/C5): for a first-order hop
   `h = sum_mu eta_mu(x) (delta_{y,x+mu} − delta_{y,x−mu})`, anti-Hermiticity
   holds exactly when `eta_mu(x)` does not depend on `x_mu`. Both `eta ≡ 1` (the
   `K0` phase system) and `eta^0` (Kawamoto-Smit) satisfy this and both give
   anti-Hermitian hops — so both sit inside the on-main theorem's stated
   hypothesis class. Probe check C5 is the construction-mutation probe:
   `eta_mu(x) = (−1)^{x_mu}` (made to depend on its own coordinate) breaks
   anti-Hermiticity and the rejector fires. The hypothesis is therefore a *real*
   constraint — it is just a constraint whose admissible class **contains both
   branches**.
3. **The prior-art reading.** The repo already records
   "the staggered-grounded RP surface does not separate `K0` from `K1`"
   (`docs/STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md:149`),
   and the two-class note declines to impose RP as circular
   (`...2026-06-10.md:213-219`).

**What is new here:** `...2026-06-10.md:386-392` leaves open, as a candidate
future selector, "an RP/transfer-positivity theorem grounded **off**-staggered-
surface". Reading (1) is exactly that — it is grounded on nothing but
self-adjointness — and it is neutral. Reading (2) shows the actual landed
off-surface hypothesis is neutral too. **That route is not merely untried; it
cannot work**, because transfer positivity is a consequence of hermiticity and
hermiticity is symmetric between the branches.

**(iii) Survives:** `{K0, K1}`, unchanged.

**(iv) First artifact:** a two-slice reflected Berezin Gram computed for the
`K0` phase system on the *same* carrier and conventions as the on-main 3+1 note
(`..._CAR_FOCK_REPRESENTATION_..._2026-07-12.md`), exhibited as positive
semidefinite. That converts the structural argument into a same-surface
constructive exhibit and closes reading (2) constructively.

**Measure corollary.** The same neutrality holds on the measure half:
"On the periodic ring, RP/T-positivity certifies BOTH the HCB and the CAR ring
[...] the ring does not select CAR"
(`docs/RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md:40`, `unaudited`,
`no_go`), and "transfer positivity therefore has no frame difference to detect"
(`docs/CAR_FROM_POSITIVITY_NEUTRALITY_NOTE_2026-06-02.md`, `unaudited`).

### C5 — Microcausality / Lieb-Robinson — **implied, not imposed; cut = 0**

**(i) Native**, and this session landed a large family of it (twelve
`MICROCAUSALITY_*_2026-07-18/20` notes). But it is the wrong shape to be a
selector: the derived velocity is

```text
v_LR := 2 * e * q * W * R
```

(`docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md:23`),
a function of support size `q`, support diameter `R`, and per-site overlap
weight `W` **only**. Applied to the NN hopping bilinear it gives the
unconditional `v_LR <= 4·e·(|m| + 2d)`, i.e. `≈ 65.24` on `Z^3` at `m → 0`
(`ibid.:29`). Probe check D2 rebuilds `24e = 65.23876...` natively.

**(ii) Excludes** non-quasilocal actions — actions with unbounded per-site
weight or non-decaying tails. That is a real exclusion, but it is *entailed by
C2*: every finite-range bounded interaction obeys an LR bound. Microcausality is
therefore a **theorem about** the licensed surface, not a **cut on** it.

**(iii) Survives:** `{K0, K1}` with **identical** LR budgets. Probe checks
D1/D3: the per-edge two-site block has singular values `{1, 1}` for `t = +1`
and for `t = −1` alike, and `|t_mu(x)| = 1` throughout both systems, so
`q`, `R`, `W` — and therefore `v_LR` — coincide exactly. The phases enter the
LR bound only through `|t|`, and the flux bit lives entirely in the *phases*.
No LR-type bound can ever see it.

**(iv) First artifact:** none can help. To make microcausality selective one
would need a bound sensitive to phase holonomy rather than to `|t|`; that is a
different theorem than any in the landed family, and I know of no such object.

### C6 — `kinetic_isotropy_primitive` (`c_t = c_s`) — **boundary forbids the use; cut = 0**

**(i) Native approved primitive**, registered in
`docs/audit/data/axiom_premise_nodes.json` as `kinetic_isotropy_primitive`,
source `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`.

**(ii) What it grants and what it forbids.** It grants exactly "the matter
kinetic normalization is space-time isotropic, `c_t = c_s`" — "a structural
statement about the regulator geometry" (`:17-29`). Its own boundary section
(`:62-75`) says it "does not supply any dimensionless dynamical quantity",
"does not re-axiomatize time", and supplies no "selector". The registry check
repeats the boundary: "Do not grant more than the primitive source note
declares" (`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md:14-16`).

The tempting move is: `K1` has a relativistic linear cone, `K0` has a quadratic
dispersion, so `c_t = c_s` (a light-cone statement) picks `K1`. **That move is
already ruled out by prior art**, in exactly those words:
`docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md:291`
lists "approved kinetic isotropy" with honesty marker **`RULED OUT BY PRIOR`**,
positive attack "use `c_t=c_s` to force first-order staggered dynamics", result
"the linked primitive explicitly supplies no dynamics, selector, or
Lorentz-closure theorem". The primitive fixes the *regulator's* graining ratio,
not the *matter law's* dispersion.

**(iii) Survives:** `{K0, K1}`. Both are formulable on a hypercubic
`Z^3 × Z_τ` regulator with `a_t = a_s`.

**(iv) First artifact:** a derivation (not the primitive) that the emergent
low-energy cone of the *physical matter law* is linear and isotropic. That
would be a Lorentz-closure theorem, which the primitive explicitly disclaims
housing. Building it is the honest route to closing `B-BIT` — and it is
precisely the "dynamical/spectral principle requiring point-like zero sets
(relativistic cones)" that `...2026-06-10.md:390-391` names as an open selector.

### C7 — Record-compatibility — **readout is kinetic-blind; cut = 0**

**(i) Native.** `MINIMAL_AXIOMS_2026-06-29.md:69-72`: "Only records are
readable. A readout value is determined by record content alone. For any finite
collection of pairwise-disjoint records, scalar readout `I` is additive, with
`I(empty)=0`."

**(ii) Excludes** readouts that depend on non-record data or fail additivity. It
excludes **nothing about the kinetic law**, because the readout is a functional
of the record configuration and the kinetic law is a functional of the
coefficients. The July-10 countermodel makes this concrete: it exhibits a
nonempty record history with `I(R) = |dom R|`, and states that "Both the
qubit-exchange kinetic completion below and the staggered comparator can be
added to this identical axiom reduct without changing any availability or record
statement"
(`...NONFORCING_NO_GO_NOTE_2026-07-10.md:186-188`).

**(iii) Survives:** `{K0, K1}` and `Φ = I − SWAP`.

**A near-miss worth flagging.** There *is* a live route where Record bites, and
it is honest about its own status:
`docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:4`
claims "a conditional scalar-branch exclusion **when nontrivial rank-one spectral
record-faithfulness is separately supplied**", and `:202` restates: "'excludes'
is conditional on supplied spectral faithfulness." Ledger: **`unaudited`**. So a
*strengthened* Record reading (faithfulness) would exclude the scalar branch —
i.e. would kill `K0` — but faithfulness is a supplied premise, not the Record
axiom's text. Likewise
`docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md:6-18`
concludes explicitly: "the branch is **registered by the realized record stack,
not forced by the axioms**" (`unaudited`).

**(iv) First artifact:** the record-forming-instrument classification named at
`...RECORD_FAITHFUL...2026-07-11.md:203-204` ("a record-forming instrument
classification or a faithful scalar countermodel can still settle the bridge in
either direction"). **A faithful scalar countermodel is the single
highest-value artifact this campaign could build**: it would convert the
conditional Record exclusion into a fourth neutral row and make the
underdetermination airtight. A successful faithfulness derivation would instead
close `B-BIT` — the one route I found where a framework-native strengthening
could still win.

### C8 — Admissibility as a local constraint — **contested; countermodel stands**

**(i) Native.** `MINIMAL_AXIOMS_2026-06-29.md:57-61`, in particular the
variation clause "the available possibilities are determined by, and vary with,
the nearest-neighbor conditions" — the clause the whole realized-kinetic-branch
chain consumes.

**(ii) The live dispute.**
`docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md:6-20`
argues that the variation clause selects `K1`, via the per-direction
algebra-dimension dichotomy `[1,1,1]` (`K0`, `C·I`, vacuous) versus `[2,2,2]`
(`K1`, direction-tagged maximal abelian). Its own scope adds: "does not claim
selection from the four axioms alone outside the licensed surface". Ledger:
**`unaudited`**.

The July-10 no-go refutes its **exhaustiveness** with an explicit construction:
a covariant top-eigenspace availability rule `A_x(R) = P_x(R) M_2(C) P_x(R)`
that satisfies the variation clause verbatim while remaining *independent of the
kinetic coefficients*
(`...NONFORCING_NO_GO_NOTE_2026-07-10.md:132-161`, N1 row at `:289`, and the
residual-matching verdict at `:336`: "context dropped as authority because its
licensed-surface semantic premise is stronger than current `A_min`").

**(iii) Survives:** `{K0, K1}`. The selection holds only if one additionally
supplies the identification of availability projectors with kinetic coefficient
algebras — which is precisely the bridge the axiom text does not make.

**(iv) First artifact:** an **exhaustive** Admissibility-to-kinetic-carrier
bridge, i.e. a theorem that every covariant availability rule satisfying the
variation clause induces kinetic coefficients. The July-10 top-eigenspace rule
is the standing counterexample it must exclude; any such artifact must dispose
of it first.

### C9 — Gauge covariance — not axiom-native, and neutral regardless

**(i) Not axiom-native.** No axiom names a gauge group or link variable. The
gauge sector enters through separate retained/bounded authorities. I therefore
score it as an **import** for the purposes of "framework-native constraint",
while still testing it because the brief asked.

**(ii) Excludes** kinetic terms with no covariant minimal substitution. Neither
branch is touched: probe checks E1/E2 verify exactly that
`Phi_P(t·U) = Phi_P(t)·Phi_P(U)` for both branches and that a site-local `U(1)`
frame leaves `Phi_P` invariant. **Gauging preserves the discriminating bit
rather than removing it.**

**(iii) Survives:** `{K0, K1}`. Confirmed independently by prior art at
the link-integrated level:
`docs/STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md:4`
— "at `beta = 0` every gauge-invariant polynomial observable of the hopping
kernel takes identical values on `K0` and `K1`", and "no selection of K1 over
K0 is claimed". Ledger: `unaudited`.

**(iv) First artifact:** none needed. Gauge covariance is settled neutral by an
existing landed computation.

### C10 — Doubling / no-doubling; QCA triviality — **not a framework-native constraint at all**

**(i) Not native.** The Nielsen-Ninomiya doubling obstruction relates two
desiderata — exact chiral symmetry and a prescribed species count — *neither of
which appears anywhere in the four axioms*. The axioms name no species count and
no chiral charge. The species count is a landed *consequence* of a chosen action
(`naive_lattice_fermion_two_power_d_species_count_narrow_theorem_note_2026-05-10`,
ledger **`retained` / `audited_clean`**: `2^d` species), never a constraint on it.

**(ii) What it does exclude.** Nothing, framework-natively. It is worth stating
plainly because it is the classic reason a lattice theorist would expect the
menu to be pinned: *in standard lattice QCD the action is chosen so as to hit a
target species count.* This framework has no target species count to hit.

There is one adjacent native cut worth recording, and it is not on this surface:
`docs/SCALAR_CUBIC_CAR_QCA_TRIVIALITY_AND_SIX_DIRECTION_ESCAPE_BOUNDED_THEOREM_NOTE_2026-07-11.md:4`
(`unaudited`) shows that with one fermionic mode per site, scalar unitarity plus
full proper-cubic covariance forces the QCA symbol's winding to vanish, "leaving
only an onsite phase", with a six-direction internal-mode escape. That is a
strong constraint on *unitary discrete-time* matter dynamics, and it cuts the
one-mode scalar QCA to triviality — but it is a statement about QCAs, not about
the Hermitian kinetic bilinear, and it separates neither `K0` nor `K1`
(both are Hamiltonians, not QCAs).

**(iii) Survives:** everything.

**(iv) First artifact:** an argument that the physical matter law must be a
strictly-local unitary (QCA) rather than a Hamiltonian flow. If that were
derived, the QCA triviality theorem would bite hard, and the six-direction
carrier escape would become the live menu — a *different* and possibly much
smaller menu. This is the most interesting unexplored lever I found.

---

## 4. THE DECISIVE SYNTHESIS — the intersection is not a singleton

### 4.1 Statement

Let `N` = the conjunction of C1–C10 as scored above, restricted to the
adjacency-licensed `Q`-conserving nearest-neighbor bilinear surface over the
one-qubit-per-site carrier.

**Both `K0` and `K1` satisfy `N`.** They are physically inequivalent: they differ
in a frame-invariant, gauge-invariant `Z_2` datum (plaquette flux), and in
kinetic order (20 vs 8 zero modes at `L = 4`; extensive zero surface vs 8
isolated Dirac points). Therefore `N` does not determine the matter action.

If the licensed-surface declaration is *also* dropped — i.e. if only the four
axioms plus the approved primitives are imposed — a third inequivalent law
survives, `Φ = I − SWAP` with graph-Laplacian symbol `2 sum_mu (1 − cos k_mu)`
(`...NONFORCING_NO_GO_NOTE_2026-07-10.md:190-235`).

### 4.2 Why this answers the campaign question, and what it costs

The supervisor's dispatch asked for either a decisive underdetermination no-go
(two inequivalent survivors) or a singleton with a named residual. **The answer
is the former, and the honest size of the residual is exactly one bit.** That is
a much sharper — and much more useful — negative than "the menu is a
finite/low-dimensional family": the framework's selective machinery is
*enormously* strong (a `2048:1` cut on the unit cube) and then falls exactly one
bit short.

Two caveats I will not paper over:

1. **The one-bit sharpness is bought by the Qubit axiom's single mode.** On a
   two-mode carrier the Wilson family `M_μ(r) = γ_μ + r I` is `O`-equivariant for
   every real `r` — a genuine one-parameter continuum
   (`...2026-06-10.md:349-357`). The single-mode absorption kills it. So the
   result is "one bit" only conditional on the one-qubit-per-site reading being
   the physical matter carrier, which is a reading of Qubit, not a theorem about
   the matter sector.
2. **`N` is scored on a licensed surface, not on the axioms.** The NN support
   (C2), the `Q`-conservation, and the exclusion of pairing terms and on-site
   sectors are surface declarations (`...2026-06-10.md:112-119`, B-S1–B-S3).
   Dropping any of them reopens a continuum. The one-bit figure is therefore a
   **lower bound** on the residual supply, not the whole of it.

### 4.3 The full accounting of what the matter sector actually rides on

| residual | what it is | status |
|---|---|---|
| `B-BIT`: `φ = −1` vs `+1` | one gauge-invariant `Z_2` selector | not forced; `1450` ledger rows downstream |
| surface license | NN support, `Q`-conservation, no pairing, no NNN | declared, not derived |
| carrier reading | one fermionic mode per site (vs 2-mode Wilson continuum) | a reading of Qubit |
| statistics / measure frame | CAR vs hard-core-boson (the "and its measure" half) | not forced; RP-neutral |

Every matter-sector value in the framework inherits all four.

### 4.4 Every attempted selector of `B-BIT`, and why each fails to be native

I found four, and checked each against the live ledger:

| attempt | selector used | native? | live ledger |
|---|---|---|---|
| `p_flux_selection_via_fsb_k_and_z_certificate_conditional_theorem_note_2026-06-11` | finite-species-density requirement (CL) | **no** — its own boundary B-R says "(REQ)'s normative force [...] is consumed at the chain's grade, **not claimed axiom-forced**" (`:225`) | `unaudited` |
| `realized_kinetic_branch_selected_by_admissibility_variation_..._2026-07-02` | Admissibility variation clause | **contested** — July-10 exhibits a countermodel availability rule | `unaudited` |
| `realized_kinetic_branch_conditional_record_registration_..._2026-07-02` | realized record stack | **no** — self-describes as "registered [...], not forced by the axioms" | `unaudited` |
| `record_faithful_cubic_neighbor_response_..._2026-07-11` | supplied spectral record-faithfulness | **no** — "conditional on supplied spectral faithfulness" (`:202`) | `unaudited` |

Note additionally that the P-FLUX composer is explicitly conditional on its
premise `C1` (`FSB-K` at retained grade). On the live ledger
`axiom_first_fermionic_stefan_boltzmann_narrow_theorem_note_2026-05-26` is
**`unaudited`**, and `staggered_kernel_satisfies_z_point_cone_certificate_..._2026-06-11`
is **`unaudited`**. By that note's own stated collapse condition, the composition
is not standing at current grades. (Status is the audit lane's to set; I am
reporting the shard values, nothing more.)

---

## 5. MANDATORY PRIOR-ART SWEEP ON MY OWN HEADLINE

Headline swept: *"the framework-native constraint set does not pin the matter
action; ≥ 2 physically inequivalent matter actions survive."*

**Found, and it substantially pre-empts the core claim:**

1. `docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`
   (`unaudited`, `bounded_theorem`). **Already contains** the two-class collapse,
   the `K0` countermodel, the flux-invariant separation, the `20/8` spectral
   witness, and the statement at `:118` that "The selector `φ = −1` (K1 vs K0) is
   NOT forced by the specified constraint set". *My contribution is not the
   two-class result.* It is the intersection with the six constraints that note
   explicitly did **not** impose (`:213-219` for RP; C5–C7, C9, C10 untested there).
2. `docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`
   (`unaudited`, `no_go`). Already contains the axiom-level non-forcing with the
   `I − SWAP` countermodel, **and** already rules out the kinetic-isotropy rescue
   (`:291`), the Record/realized-state rescue (`:292`), and the Admissibility
   rescue (`:289`). I am reporting those as its results, not mine.
3. `docs/STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md:149`
   already records "the staggered-grounded RP surface does not separate `K0` from
   `K1`", and `:4` already records gauge-invariant observable identity at `β = 0`.
4. `docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md:201-215`
   (`unaudited`, `no_go`) is the **gauge-sector twin** of this result: Wilson,
   heat-kernel and Manton are jointly compatible with a stack that explicitly
   includes reflection positivity and Lieb-Robinson, and differ at finite `β`.
   The matter-sector result reported here has the same shape; the two together
   say the framework's *action* underdetermination is sectoral, not local to
   matter.
5. `docs/CAR_FROM_POSITIVITY_NEUTRALITY_NOTE_2026-06-02.md` and
   `docs/RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md:40` already
   establish the **measure-half** neutrality of RP/positivity.
6. `docs/STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md:213-231`
   (`retained_bounded` / `audited_clean`) — the only *retained* row in this lane
   I found — carries an explicit import firewall denying that its operator is
   "a staggered fermion or Kogut-Susskind action" or any "physical matter
   carrier". The repo's one retained staggered-blocking result is deliberately
   **not** about a physical matter action.

**What survives the sweep as genuinely new in this wave:**

- The **RP escape route named at `...2026-06-10.md:386-392` is closed**, not by
  testing yet another RP variant but structurally: transfer positivity is
  entailed by hermiticity (C1), so no RP theorem — on or off the staggered
  surface — can separate two Hermitian branches. Plus: the on-main 3+1 RP
  theorem is quantified over "arbitrary finite real anti-Hermitian spatial hop"
  (`...CAR_FOCK_REPRESENTATION..._2026-07-12.md:388, :466`), a class that
  natively contains the `K0` phase system — verified here with a mutation
  rejector.
- The **microcausality lane is shown structurally non-selective**: `v_LR`
  depends on `(q, W, R)` and the phases enter only via `|t| = 1`. This is the
  first statement I found that the session's own twelve-note LR family cannot
  contribute to action selection.
- The **complete intersection** — nine constraints scored, seven at cut zero,
  with the reason in each case — rather than one-constraint-at-a-time no-gos.
- The **corrected live-ledger picture** of the RP lane (§6), including the
  `audited_failed` status of the row the campaign brief cited as landed.

---

## 6. LEDGER-VS-PROSE CORRECTIONS (campaign hard rule 6)

Read directly from `docs/audit/data/ledger/` shards. Reported as data, not as
verdicts.

1. **The campaign brief's own premise is stale.** The brief says the repo has
   "substantial landed RP content, including two-step blocked transfer
   positivity". `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`
   is **`audited_failed`** on the live ledger (terminal, 2026-07-21).
2. **The July-10 no-go's own status table is contradicted by the live ledger**,
   in four places at once. `...NONFORCING_NO_GO_NOTE_2026-07-10.md:358-359` and
   `:397-399` label:
   - `staggered_dirac_kinetic_class_forcing_..._2026-06-10` — prose
     `audited_clean / retained_bounded`; **live: `unaudited` / `awaiting_audit`**
   - `staggered_dirac_realization_gate_note_2026-05-03` — prose
     `audited_clean / retained_bounded`; **live: `unaudited`**
   - `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` —
     prose `audited_clean / retained_no_go`; **live: `unaudited`**
   - `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` — prose
     `audited_clean / retained_no_go`; **live: `unaudited`**
3. **The P-FLUX selection composer's premise `C1` does not hold at live grade.**
   `...2026-06-11.md:6-11` asserts "both the (Z) geometry leg and FSB-K stand at
   retained grade (`retained` / `retained_bounded`)"; **live: both `unaudited`**.
4. `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` is quoted as
   `retained_bounded` at `...RESTATEMENT_NOTE_2026-07-03.md:220`; **live:
   `unaudited`**. (That note flags its statuses as drafting-time snapshots, so
   this one is disclosed rather than misleading.)
5. **A worktree-local file is easy to mistake for landed content.**
   `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_EXTENSION_BOUNDARIES_..._2026-07-24.md`
   (plus its runner and cache) is untracked here and absent from `origin/main`
   and from the ledger. I cited it in a first draft of this report and caught it
   only on an explicit `git cat-file -e origin/main:<path>` sweep of every
   citation. **Wave 2 should run that sweep on its own citation list before
   reporting.** All ten load-bearing `docs/` citations in this report were
   verified present on `origin/main`.

Practical consequence for the campaign: **no row in the `K0`/`K1` selection lane
is at retained grade on the live ledger.** The one retained neighbour is
`staggered_os0_supplied_action_ks_blocking_..._2026-07-11`, whose firewall
disclaims physical-action content. Wave 2 must not build on any of the prose
labels above.

---

## 7. WORKER PROBE (not a gate)

`/private/tmp/.../scratchpad/wave1_probe.py` — session-local worker probe.
Exact integer / sympy arithmetic only; **no floats consumed as inputs**; the one
decimal printed (`65.23876`) is an output display of the exact `24e`.
Deterministic. **This is a worker probe, not a repo runner and not a gate.**
No repo file was created or modified by this wave except this report.

```text
TOTAL: PASS=28 FAIL=0
```

| § | checks | what was rebuilt natively |
|---|---|---|
| A | A1–A7 | unit-cube census `(128, 128, 3840)` out of `4096`; each uniform-flux bucket is exactly one site-local-`Z_2` gauge orbit of size `128`; `eta^0` lies in the `−1` bucket; `phi = conj(phi)` ⟹ `theta ∈ {0, π}` (Landau-`i` class rejected) |
| B | B1–B5 | both hopping matrices real symmetric; zero-mode counts `(20, 8)` at `L = 4` by exact fraction-free rank; uniform flux `{+1}` vs `{−1}` on the `4^3` torus; `K0` symbol has 20 exact zeros; both have identical `Tr(H^2) = 2dN = 384` |
| C | C1–C5 | `exp(−aλ) > 0` for real `λ`; exact real spectra at `L = 2` (`K0`: `{−6,−2,2,6}`, `K1`: `{−2√3, 2√3}`); the on-main RP theorem's anti-Hermiticity hypothesis holds for `eta ≡ 1` **and** `eta^0`; **mutation probe**: `eta_mu(x) = (−1)^{x_mu}` breaks anti-Hermiticity and the rejector fires |
| D | D1–D3 | edge-block singular values `{1,1}` for `t = ±1`; `v_LR = 2e·q·W·R = 4e(|m|+2d) = 24e = 65.23876…` matching the landed note's `≈ 65.24`; `|t| = 1` in both branches |
| E | E1–E2 | `Phi_P(tU) = Phi_P(t)·Phi_P(U)` for both branches; site-local `U(1)` frame leaves `Phi_P` invariant (symbolic, exact) |
| F | F1–F3 | proper cubic group generated from `C4z`, `C3[111]`: `|O| = 24`, all `det = +1`, direction orbit `6`; all 24 rotations preserve the flux class of **both** `K0` and `K1` |

Construction-mutation probes (campaign hard rule 4), not assertion probes:
C5 mutates the *construction* of the phase system (`eta_mu` made to depend on
`x_mu`) and confirms the landed RP hypothesis genuinely rejects it — establishing
that the hypothesis is a real constraint whose admissible class nonetheless
contains both branches. A7 mutates the flux target off the real axis and confirms
rejection.

---

## 8. What this wave does NOT establish

- **No audit verdict** is set, predicted, or implied for any row.
- It does **not** claim `K0` is the physical law, or that `K1` is wrong. It
  claims neither is *selected*.
- It does **not** claim the menu is exactly `{K0, K1}` in any absolute sense —
  only on the licensed surface. Off that surface the menu is larger (NNN
  continuum; pairing sector; two-mode Wilson continuum; `I − SWAP`).
- It does **not** address the `det_C` vs `|det_C|^2` grain (the obligation's
  already-discharged second conjunct).
- It does **not** claim the underdetermination is permanent. Two named routes
  could still close `B-BIT` framework-natively, and both are recorded above as
  first artifacts: an exhaustive Admissibility-to-carrier bridge (C8), and a
  derived record-faithfulness premise (C7).
- The `I − SWAP` third survivor and the `2^d` species-count row are cited from
  landed notes, not rebuilt here.

## 9. Recommended Wave-2 targets, ranked

1. **Build the faithful scalar countermodel** named at
   `...RECORD_FAITHFUL...2026-07-11.md:203-204`. It is the one place a
   framework-native strengthening could still close `B-BIT`; settling it in
   either direction is decisive. Highest value in the campaign.
2. **Compute the `K0` two-slice reflected Berezin Gram** on the landed 3+1
   carrier and conventions. Converts §C4 reading (2) from structural to
   constructive on the repo's own RP surface.
3. **Test whether the physical matter law must be a QCA.** If it must, the
   `unaudited` scalar-cubic-QCA triviality result bites and the menu changes
   shape entirely (C10 (iv)). Highest upside, lowest probability.
4. **Re-run the census on the two-mode carrier** to state the Wilson continuum
   `M_μ(r)` explicitly as the residual under a weakened Qubit reading — this
   quantifies caveat §4.2(1), which is currently the weakest joint in the
   one-bit claim.
