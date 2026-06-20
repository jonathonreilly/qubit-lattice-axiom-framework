# Exercise Three — Literature Proof Search (B-AXIS wall)

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` (Exercise Three)
**Slug:** baxis-wall-break  •  **Date:** 2026-06-20
**Network:** AVAILABLE (WebSearch + WebFetch live; two PDFs extracted locally via pypdf).
**Posture:** extract proof skeletons to translate into A_min. Nothing here is imported
as authority. Literature is precedent / proof template only; any surviving route must be
rebuilt as a native runner/proof and audited like native theory.

## Framework refresher surfaces read (before any conclusion)

- `docs/MINIMAL_AXIOMS_2026-06-05.md` (Lattice/Quantum/Record; explicit OPEN GATES:
  arrow, measurement, decoherence, record-production dynamics, source/action — and the
  explicit statement that Lattice supplies *no boundary condition, no metric scale, no
  dynamics, no causal cone*).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (four approved primitives:
  `scale_reference`, `kinetic_isotropy`, `realized_state`, plus `minimal_axioms`).
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (one dimensionful ruler `a^{-1}=M_Pl`, units
  only, zero dimensionless content — directly relevant to N2b).
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (`c_t=c_s`, OS0 graining isotropy
  — the time-direction analogue of cubic adjacency; **already approved**, highly relevant
  to N4/N2b, see Vector L7 below).
- `docs/audit/data/axiom_premise_nodes.json` + `docs/audit/data/tier_a_admissions.json`
  (READ-ONLY; AC_phi_lambda and theta are the only Tier-A targets; the staggered-Dirac
  realization is itself a Tier-A admitted *gate*, not an axiom — relevant to the
  carrier-choice challenge).
- `docs/ai_methodology/skills/review-loop/SKILL.md` (no new axiom/primitive; no-go
  discipline N1–N8; Record guardrails).
- `docs/repo/CONTROLLED_VOCABULARY.md` (status/claim vocabulary; no-go is a `claim_type`).
- Re-read: the wall `EXERCISE.md`, the unified no-go note, the `NO_GO_LEDGER.md`.

## How this slice avoids re-proposing pruned routes

The `NO_GO_LEDGER` already prunes: OS/GNS-privileges-τ, record-durability-axis,
registration-cone, anomaly/chirality, KMS/APBC, Wilson temporal gauge, APBC-alone,
per-axis-Z₂-BC-as-selector, reality/CPT grading, crossing-link cocycle (all N4);
spectrum/Stone and Lattice-no-scale (N2b); algebraic-commuting-factor-exclusion,
product-Stone, Record-additivity (N5). **None of the vectors below is one of those.**
The KMS angle in the ledger is the *APBC-thermal-circle-as-second-clock* route; the
**Tomita-Takesaki modular/thermal-time** vector (L1) is a *different* use of KMS (an
intrinsic-generator-existence theorem, not an axis supplier), and is explicitly NOT in
the ledger. Where a vector touches a pruned area I say exactly how it differs.

---

## Source table (Source | Problem solved | Premises | Proof skeleton | Maps to repo | Does NOT map | Runner/proof translation | Import risk | Citation)

### L1 — Tomita–Takesaki modular flow + Connes–Rovelli thermal time (the canonical-generator existence theorem) — attacks N5 + the native-on-Z³ reframe

- **Source.** Connes & Rovelli, *Von Neumann Algebra Automorphisms and Time–Thermodynamics
  Relation in General Covariant Quantum Theories*, Class. Quantum Grav. 11 (1994) 2899,
  arXiv:gr-qc/9406019. Tomita–Takesaki background: Takesaki, *Theory of Operator Algebras
  II*; Bratteli–Robinson Vol. 2.
- **Problem solved.** Given an algebra of observables `M` (von Neumann algebra) and a
  single faithful normal state `ω`, produce a **canonical one-parameter automorphism
  group** (a clock) `σ_t^ω` with no external time input.
- **Premises.** `M` a von Neumann algebra; `ω` faithful + normal. KMS condition. The
  *state-independent* upgrade needs the cocycle Radon–Nikodym (Connes) theorem.
- **Proof skeleton.** (i) Tomita operator `S = JΔ^{1/2}` from `Sxξ_ω = x*ξ_ω`; modular
  flow `σ_t^ω(x) = Δ^{it} x Δ^{-it}` (paper eq. 8, sign-convention `α_t A = Δ^{-it}AΔ^{it}`).
  (ii) `ω` satisfies KMS at β=−1 w.r.t. `σ_t^ω`. (iii) **Cocycle Radon–Nikodym:** two
  states give modular flows that differ by an *inner* automorphism, so all states define
  the **same** one-parameter subgroup in `Out(M)=Aut(M)/Inn(M)` — *"a von Neumann algebra
  possesses a canonical 1-parameter group of outer automorphisms"* — independent of `ω`.
  (iv) This canonical flow is **nontrivial exactly for type III** factors; for type I and
  type II it is **inner** (so it collapses to an ordinary Hamiltonian and is "trivial" in
  Out). (v) Thermal time hypothesis: physical time = modular flow of the physical state.
- **What maps to the repo.** This is a *constructive existence theorem for a preferred
  one-parameter generator from state + algebra alone* — exactly the object the unified
  note says A_min "does not supply" (Section 7: "the generator of U(t) is not
  axiom-supplied"). A_min supplies Quantum (`M`) and Record (`ω` = the realized durable
  state / the `realized_state_primitive` supplies the slot). If the relevant operator
  algebra is type III, modular theory hands back a *canonical, state-class-independent*
  clock — which would directly pressure N5 (it would be THE distinguished one-parameter
  orbit) and supply the U(t) the native-on-Z³ reframe needs.
- **What does NOT map / why this is hard, not a free win.** The repo's supplied object
  `T̂² = ⊗_p diag(1, e^{−2E(p)})` lives on a **finite-dimensional** Hilbert space → the
  algebra is **type I_n** (finite matrix algebra). For type I the modular flow is INNER:
  `σ_t^ω(x)=Δ^{it}xΔ^{-it}` with `Δ=ρ⊗ρ^{-1}` built from the density matrix `ρ`, so it is
  literally generated by `log ρ` and is trivial in Out(M). On the finite even-cubic block
  the modular flow gives you back exactly `Ĥ` (up to the state) and does NOT single out a
  *unique* clock beyond what you put in via `ω`. **So the naive import FAILS on the
  retained surface** — and that failure is itself informative: it says the modular-time
  route can only bite in the **thermodynamic / GNS limit** where the local algebra of the
  Z³ system becomes a genuine **type III₁ factor** (the generic situation for a
  relativistic/QFT local algebra — Buchholz–Wichmann; Haag). This is precisely the
  emergent-dynamics open gate, not the finite retained surface.
- **Runner/proof translation.** Two distinct artifacts. **(a) Falsifier-runner (cheap,
  do first):** on the finite even-cubic block, build `Δ` from a Record-realized `ρ`, show
  `σ_t` is inner and recovers `span{Ĥ}` only — i.e. *prove modular time is trivial on the
  retained surface* (this either kills the route honestly or sharpens exactly where it
  could live). **(b) Type-III probe (the real test):** take the GNS representation of the
  infinite Z³ system w.r.t. a translation-invariant KMS/vacuum state and ask whether the
  local algebra is type III₁; if so, the modular flow is a canonical outer one-parameter
  group, and the question becomes whether it coincides with the RP/transfer generator.
  This is a genuine derivation target, not in the ledger.
- **Import risk.** HIGH if imported as authority (it would smuggle a QFT type-III
  classification, a vacuum/KMS state choice, and the thermodynamic limit — all OPEN
  GATES). LOW as a *skeleton*: the construction `state+algebra → canonical generator` is
  exactly the shape A_min would need, and the type I/II/III trichotomy tells you *why*
  the finite surface can't deliver it (so the no-go's "relocates to emergent-dynamics
  gate" gets a precise operator-algebraic *reason*, upgrading prose to theorem).
- **Citation.** arXiv:gr-qc/9406019 (Connes–Rovelli), eq. 8 + cocycle-Radon–Nikodym
  statement ("All states ... determine the same 1-parameter group in Out(R)").

### L2 — Free-fermion / integrable transfer matrix = generating function of a COMMUTING-CHARGE TOWER; integrability breaking COLLAPSES the tower to one charge — attacks N5 head-on

- **Source.** Quantum inverse scattering / Yang–Baxter: transfer matrix as generating
  function of mutually commuting charges (Sklyanin; Faddeev; review e.g.
  ETH lecture notes "Quantum spin chains", edu.itp.phys.ethz.ch/fs13/int/SpinChains.pdf;
  arXiv:2402.08924 "local conserved quantities in 1D ..."). Integrability-breaking:
  arXiv:2302.12804 ("Weak integrability breaking perturbations of integrable models"),
  arXiv:2504.14315 ("Dichotomy theorem separating complete integrability and
  non-integrability of isotropic spin chains"), and the free-fermion classification
  Elman–Chapman "Free fermions behind the disguise".
- **Problem solved.** Characterizes *exactly when* a transfer matrix `T(u)` has an
  extensive tower of independent mutually-commuting conserved charges `Q_k = d^k/du^k log
  T(u)` (the Hamiltonian being `Q_1`) vs when the only conserved local charge is `H`.
- **Premises.** A spectral-parameter family `T(u)` obeying Yang–Baxter (integrable case);
  or a generic non-integrable interaction (the dichotomy theorem's other side).
- **Proof skeleton.** Integrable: `[T(u),T(v)]=0 ∀u,v ⇒` log-derivatives give an
  *infinite/extensive commuting family*. The dichotomy theorem (2504.14315): a translation-
  invariant nearest-neighbor spin chain either has a full integrable tower OR has **no
  nontrivial local conserved charge beyond H and the obvious symmetries** — there is no
  middle ground for local charges. Weak-breaking (2302.12804): a generic perturbation
  destroys the tower, leaving only `H` conserved (quasi-conserved charges decay).
- **What maps to the repo — the decisive reframe of N5.** The repo's N5 wall is built on:
  `T̂² = ⊗_p diag(1, e^{−2E(p)})` is *maximally factorized* into `L_s` commuting per-mode
  clocks `{n_p}`, generator span dim `L_s` ≠ 1, so "no commutant/center forces a single
  one-parameter orbit." **The literature names this object precisely: it is a FREE
  (Gaussian) fermion transfer matrix, the most integrable case, whose commuting tower
  `{n_p}` is the well-known free-fermion charge tower.** The multi-dimensional commuting
  generator span is NOT a generic feature of "A_min + locality" — it is the *signature of
  the free/quadratic staggered surface*. The dichotomy theorem says: turn on a generic
  local interaction (still A_min-admissible: Quantum gives `M_2(C)` per site, nothing
  forbids interacting dynamics) and the tower **collapses to a single conserved `H`** —
  i.e. **N5 would be DERIVED (no second commuting clock) for the generic dynamics, and is
  FALSE only for the measure-zero free surface the repo happens to have retained.**
- **What does NOT map.** A_min does not *supply* any dynamics at all (the dynamics is the
  emergent-dynamics OPEN GATE), so I cannot claim "the generic case holds." But this flips
  the burden: the repo currently treats the `L_s`-fold factorization as the *generic*
  obstruction; the literature shows it is the *special* (free, integrable) case. The honest
  N5 statement should be: *N5 fails on the free staggered surface precisely because that
  surface is integrable; on a generic A_min-admissible interacting dynamics the commuting
  tower collapses and the second clock is excluded.* That is a strictly stronger and more
  honest no-go boundary — possibly a route to deriving N5 *conditional on non-integrability
  of the emergent dynamics*, which is itself a far weaker and more plausible premise than a
  bespoke `(L_s−1)`-parameter physical-clock-admission ray.
- **Runner/proof translation.** (i) **Label the existing object:** add to the N5 runner a
  block proving `T̂²` is the free-fermion transfer matrix and `{n_p}` is the standard
  free-fermion charge tower (cheap, exact). (ii) **Integrability-breaking witness:** build
  a minimal A_min-admissible *interacting* two-step transfer on the same small block
  (e.g. add a nearest-neighbor `n_x n_{x+1}` term), recompute the commuting local-charge
  span, and show it drops to 1 (just `Ĥ`). If it does, you have a runner-backed statement
  "N5 holds for generic dynamics, fails only for the free surface." (iii) Cite the
  dichotomy theorem as the precedent that this collapse is generic, not accidental.
- **Import risk.** LOW. We are not importing a theorem as authority; we are *recognizing
  what the repo's own object is* (a free-fermion transfer matrix) and testing the generic
  case with a native runner. The only risk is over-claiming that the emergent dynamics IS
  non-integrable (it is an open gate) — so the result must ship as *conditional on
  non-integrability*, not as unconditional N5 closure.
- **Citation.** arXiv:2504.14315 (integrability/non-integrability dichotomy);
  arXiv:2302.12804 (weak breaking destroys the tower); arXiv:2402.08924 (local conserved
  charge structure).

### L3 — Pauli's theorem (refined: Galapon) — the absolute-clock-unit / time-operator obstruction is a THEOREM, sharpening N2b (and bounding N5)

- **Source.** Galapon, *Pauli's Theorem and Quantum Canonical Pairs ...*, Proc. R. Soc.
  Lond. A 458 (2002) 451, arXiv:quant-ph/9908033. Background: Pauli (1933/1958);
  Srinivas–Vijayalakshmi 1981 (the imprimitivity restatement); Busch–Grabowski–Lahti
  (covariant POVM clocks); Holevo.
- **Problem solved.** Whether a self-adjoint "time" operator `T` canonically conjugate to
  a Hamiltonian `H` (`[T,H]=i`, equivalently the imprimitivity/covariance
  `e^{iHα}E_T(Δ)e^{-iHα}=E_T(Δ+α)`) can exist.
- **Premises / the sharp content.** Galapon's clean restatement (his eq. 7.7, quoting
  Srinivas–Vijayalakshmi): **if `H` is semibounded, there is NO self-adjoint `T` with
  `e^{iHα}E_T(Δ)e^{-iHα}=E_T(Δ+α)` for all α∈ℝ.** A covariant *sharp clock* (a self-adjoint
  time observable shifting uniformly under `H`) requires the energy spectrum to be the
  **whole real line, absolutely continuous**. With only semiboundedness (`H≥0`, exactly the
  repo's spectrum condition) you get at most a *covariant POVM* clock (non-self-adjoint),
  never a sharp self-adjoint uniform clock. Galapon's twist: a *bounded* self-adjoint `T`
  conjugate to a discrete/semibounded `H` IS consistent if you DROP the
  covariance/imprimitivity demand (it then holds on a proper subspace only).
- **What maps to the repo.** The repo's `Ĥ = Σ_p E(p) n_p ≥ 0` is semibounded with
  discrete spectrum (finite block). Pauli/Galapon then says: **there is provably no
  self-adjoint observable on this Hilbert space that runs at a uniform unit rate against
  `Ĥ`** — i.e. *the framework cannot contain a clock pointer that reads absolute time
  uniformly*, which is exactly N2b's "no A_min observable carries 1/time units," but now as
  a **citable spectral theorem** rather than a rescaling-gauge computation. It explains
  *why* the `a_τ→c·a_τ` gauge is unavoidable: a sharp uniform clock conjugate to a
  semibounded generator is forbidden, so no internal observable can fix the unit.
- **What does NOT map.** Pauli is about a *uniform self-adjoint* clock; it does NOT forbid
  a *covariant POVM* time (which exists for semibounded `H`). So it does not by itself close
  N2b positively — it converts N2b from "we computed a gauge" into "a spectral no-go forbids
  the only object that could break the gauge," which is the same wall with a deeper reason
  and a cleaner falsifier. It also bounds N5: any *second* clock would also need a uniform
  pointer; Pauli forbids the self-adjoint version of that too.
- **Runner/proof translation.** Finite-dimensional Pauli check: on the retained block,
  enumerate self-adjoint `T` and show no `T` satisfies the covariance/ladder relation
  `[T,Ĥ]=i·(unit)` with a *uniform* spectrum-shift (finite discrete spectrum makes the
  ladder relation literally impossible — `[T,H]=i` has no finite-dim solution since
  `tr[T,H]=0≠tr(iI)`). This is a two-line exact certificate that *no internal uniform
  clock exists*, upgrading the N2b prose with a finite-dim Pauli obstruction. Then note the
  only escape (a covariant POVM clock) requires an a.c. real-line spectrum = the continuum/
  thermodynamic limit = OPEN GATE.
- **Import risk.** LOW. The finite-dimensional `tr[T,H]=0` obstruction is elementary and
  native; Pauli is cited as the precedent/name. No state, no continuum is imported for the
  finite certificate.
- **Citation.** arXiv:quant-ph/9908033, §7 eq. (7.7) (Srinivas–Vijayalakshmi restatement);
  §8 (canonical pairs); §"Conclusion" (POVM covariance only for a.c. real-line spectrum).

### L4 — Rovelli "time-oriented coarse graining": the ARROW/orientation is a property of the chosen macroscopic subalgebra, not of dynamics — reframes N4's orientation half + the record-production gate

- **Source.** Rovelli, *Why do we remember the past and not the future? The 'time oriented
  coarse graining' hypothesis*, arXiv:1407.3384.
- **Problem solved.** Where the past→future asymmetry comes from when the microdynamics is
  CPT-symmetric.
- **Premises.** A "sufficiently rich, ergodic" microscopic system; a choice of macroscopic
  observables `A_n` (a coarse-graining / a subalgebra).
- **Proof skeleton (his Conjecture + eq. 1–3).** Micro-entropy
  `S_{s,A_n}=log ∫ ds' Π_n δ(A_n(s')−A_n(s))`. **Conjecture:** for a generic motion and
  *each* direction of `t`, there EXISTS a family of macroscopic observables `A_n` with
  `dS/dt ≥ 0`. So the second law (hence the arrow) is **not** a property of the state or
  the dynamics — it is selected by *which coarse-graining (subalgebra) we couple to*.
- **What maps to the repo.** Directly addresses the unified note's orientation firewall.
  The note currently says orientation is carried by the past hypothesis (`H≥0` ⟺ low-record
  past). Rovelli's result is a *different and weaker* source: the arrow can be carried by
  the **Record readout context** itself (Record = a *coarse-graining* to durable central
  sectors — exactly an `A_n` choice). This is promising because **Record IS in A_min**,
  whereas the past hypothesis is explicitly NOT housed by any primitive
  (`realized_state_primitive` note: "The past hypothesis is explicitly not housed by this
  primitive"). If the *direction* (not the unit, not the axis-label) can be sourced from the
  Record coarse-graining via a Rovelli-type entropy monotone, part of the orientation
  residual moves *inside* A_min rather than to the open gate.
- **What does NOT map.** Rovelli's conjecture is about *orientation* (t vs −t), NOT about
  *which Euclidean axis* is time (N4 proper) nor the absolute unit (N2b). And it is a
  *conjecture* with plausibility arguments, not a theorem; importing it as closure would be
  illegitimate. It also needs "sufficiently rich + ergodic," which is dynamics-dependent
  (open gate). So at most it relocates the *orientation* sub-residual from past-hypothesis
  to Record-coarse-graining — a reframe, not a derivation.
- **Runner/proof translation.** On a small A_min block with a Record coarse-graining map
  (durable central-sector projection), compute the coarse-grained entropy monotone along a
  swept evolution and test whether the Record coarse-graining yields `dS≥0` in exactly one
  direction. If yes for the Record `A_n` but not for a W-conjugate coarse-graining, you have
  a *Record-sourced* orientation that is NOT W-symmetric — a genuinely new datum. (Caveat:
  the unified note's R-N4-REGDIR found the A_min accumulation monotone is a W-invariant
  *ball*; the Rovelli angle differs by using an *entropy/information* monotone of the
  coarse-graining, not a record-count ball — so it is not the same pruned object.)
- **Import risk.** MEDIUM. The conjecture is not proven; must ship as orientation-only,
  conditional, and clearly separated from N4 axis-label and N2b. Do not let "ergodic" smuggle
  in dynamics.
- **Citation.** arXiv:1407.3384, eqs. (1)–(3) and the boxed Conjecture.

### L5 — Lieb–Robinson emergent light cone: an *intrinsic* causal velocity from a local generator — a different N4 angle (and a circularity warning the repo already half-knows)

- **Source.** Lieb–Robinson (1972); Nachtergaele–Sims; Hastings. Reviews:
  arXiv:1503.07538 (equilibration review), researchgate Lieb–Robinson reviews; long-range
  caveat arXiv:2511.22020. Repo-adjacent: the unified note already cites a Lieb–Robinson
  "equal-time tensor locality" note and R-N4-REGDIR.
- **Problem solved.** A local Hamiltonian on a lattice generates an emergent finite
  maximal velocity `v_LR` and an approximate light cone — an *intrinsic* causal/temporal
  structure from the generator.
- **Premises.** A *Hamiltonian generator* with finite-range/decaying interactions on the
  lattice. (Short range required: long-range models need NOT have a light cone.)
- **Proof skeleton.** Commutator bound `‖[A(t),B]‖ ≤ C‖A‖‖B‖ e^{−(d−v_LR|t|)/ξ}` ⇒ a cone.
- **What maps / does NOT map.** This is the most honest place to record a *boundary*: the
  repo's R-N4-REGDIR already found that a real LR cone needs a *supplied generator* whose
  W-conjugate gives an identical cone (circular). The literature CONFIRMS the premise gap:
  LR needs a *Hamiltonian* (a chosen evolution generator) as input — which is downstream of
  B-AXIS. **So L5 mostly RE-CONFIRMS a pruned route — I record it as a guardrail, not a new
  vector**, with one caveat worth a fresh look: LR distinguishes *space* from *time* by the
  fact that the cone opens in time and is bounded in space; on the *Euclidean* lattice
  (before choosing a generator) all four directions are equivalent, but once a *generic
  non-integrable* generator is in hand (see L2) the LR velocity is finite in spatial
  directions and the "time" direction is the parameter — i.e. **L2's non-integrability +
  L5's LR cone together might give an axis distinction that the free surface cannot.** That
  combined L2⊕L5 angle is new; standalone LR is not.
- **Runner/proof translation.** Only attempt *after* L2: if a generic interacting A_min
  generator collapses the commuting tower (L2), test whether its LR cone is direction-
  asymmetric in a way the free `T̂²` is not.
- **Import risk.** MEDIUM (LR needs a generator = open gate; do not re-import the pruned
  cone). Recorded mainly to keep the next agent from re-proposing standalone LR.
- **Citation.** Lieb–Robinson 1972; arXiv:2511.22020 (long-range caveat).

### L6 — Site- vs link- vs diagonal-reflection positivity: the transfer matrix the repo retained is ONE of several inequivalent RP choices — a hidden-premise probe for N4/N2a

- **Source.** Lattice RP literature: Osterwalder–Seiler (1978); Montvay–Münster
  (textbook); Fröhlich–Israel–Lieb–Simon (RP + phase transitions). Search surfaced:
  "three known types of reflection positivity in lattice gauge theory: site-reflection,
  link-reflection, diagonal-reflection" (lattice YM RP reviews); OWR_2017_55 (Oberwolfach
  Reflection Positivity report); arXiv:2506.20526 (RP in Euclidean relativistic QM).
- **Problem solved.** How to build the transfer matrix / Hamiltonian from a Euclidean
  lattice action — and the fact that *the reflection plane and reflection TYPE are choices*.
- **Premises.** A reflection-positive Euclidean action; a chosen reflection plane (which
  bond/site it cuts) AND a chosen reflection type (site vs link vs diagonal).
- **Proof skeleton.** RP at a chosen plane ⇒ positive-definite physical Hilbert space +
  self-adjoint `H≥0` for *that* reflection. Different reflection types give *different but
  related* Hamiltonians of the same theory.
- **What maps to the repo — the new probe.** The repo's W/S₄ transport result tested the
  signed **site**-exchange `W = P_{τ↔1}·diag((−1)^{x_τ x_1})` and concluded all axes are
  equivalent. But the literature says there are **inequivalent RP constructions** (site vs
  link vs diagonal). The repo's whole N4 argument is "every retained anchor is W-transported
  to a spatial axis with resid 0" — **but W is a SITE-reflection symmetry.** Question the
  repo may not have asked: *is the signed exchange `W` also a symmetry of the LINK-reflection
  transfer matrix, or of the diagonal-reflection construction?* If a link/diagonal RP
  transfer matrix exists on the staggered surface whose stabilizer is NOT transitive S₄
  (because link-reflection treats the bond, not the site, breaking the site-exchange), then
  there is an A_min-internal construction selecting an axis that W does NOT transport — a
  potential N4 selector the S₄-transitivity result missed because it only enumerated the
  signed *site/hyperoctahedral* group (`|G_bare|=384`).
- **What does NOT map.** Choosing a reflection *plane* is still a choice (could be itself
  transportable). And link/diagonal RP may simply reproduce the same S₄ orbit. So this is a
  *probe*, not a proof: it tests whether the repo's "transitive S₄" conclusion is an
  artifact of having only enumerated site-reflection symmetries.
- **Runner/proof translation.** Construct the **link-reflection** transfer matrix on the
  even-cubic staggered block (reflect across a bond midpoint rather than a site), compute its
  automorphism group and the axis-image of its stabilizer, and check whether the signed
  site-exchange `W` still preserves it. Decisive outcomes: (a) link-RP stabilizer is still
  transitive S₄ → strengthens the no-go (now robust across RP types); (b) link-RP breaks the
  W-transitivity → a NEW axis-distinguishing A_min construction, reopening N4.
- **Import risk.** LOW. Link/diagonal RP are standard lattice constructions on the *same*
  retained surface; nothing new is axiomatized. The only risk is mislabeling a transportable
  plane-choice as a selector — guard by checking transportability of the plane too.
- **Citation.** Osterwalder–Seiler 1978; Oberwolfach Reflection Positivity report
  OWR_2017_55; lattice YM RP reviews (site/link/diagonal classification).

### L7 — (cross-check, not literature-novel) the approved `kinetic_isotropy_primitive` `c_t=c_s` and the N2b unit

- **Source.** Repo-internal `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (read as
  refresher), cross-read against the OS reconstruction literature (anisotropic lattices,
  arXiv:2606.20090 "Hamiltonian-based dimensional reduction with Wilson-Dirac fermions,"
  which treats `a_τ ≠ a_s`).
- **Why recorded here.** The literature on *anisotropic* lattice reconstruction makes the
  spacing ratio `ξ = a_s/a_τ` an explicit physical input fixed by matching `c_t=c_s`. The
  repo *already* has an approved primitive fixing `c_t=c_s`. This means the N2b residual is
  *narrower than the unified note states*: the note says "no A_min observable carries
  1/time units," but the kinetic-isotropy primitive already ties the *time graining* to the
  *space graining* in FORM. The residual is purely the single overall dimensionful ruler
  `a^{-1}=M_Pl` (`scale_reference_primitive`), which is *also already granted*. **So the
  honest N2b statement is not "a_τ is wholly unfixed" but "a_τ is fixed in FORM by
  `c_t=c_s` and in overall SCALE by `a^{-1}=M_Pl`; what remains is only the (already
  gauge) overall normalization."** This is a *reframe* (it belongs more to REFRAMING.md)
  but the anisotropic-OS literature is the precedent that `c_t=c_s` + one ruler is exactly
  what pins an anisotropic lattice's time spacing — worth a runner that composes the two
  approved primitives and checks what `a_τ` freedom genuinely survives.
- **Import risk.** LOW (uses only already-approved primitives). Risk = double-counting the
  scale; guard by the PRIMITIVE_REGISTRY_CHECK (units only, no dimensionless content).
- **Citation.** arXiv:2606.20090 (anisotropic Hamiltonian reconstruction);
  repo `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`.

---

## What the literature CONFIRMS about the wall (so the next agent does not waste cycles)

- OS reconstruction genuinely "chooses an arbitrary time direction" and the transfer is
  built *after* that choice — the repo's N4 framing is faithful to the literature. The S₄
  transport result is the lattice shadow of Euclidean rotation invariance. (arXiv:2506.00284
  and OS reconstruction reviews.)
- The finite-dimensional modular flow is inner ⇒ the Tomita route is provably trivial on
  the retained finite block; it can only bite in a type-III (continuum/thermodynamic) limit.
  This is a *reason*, not just a relocation.
- Lieb–Robinson needs a generator as input (confirms the R-N4-REGDIR circularity).

## What is GENUINELY NEW here (not in NO_GO_LEDGER), ranked

1. **L2 (free-fermion/integrability):** the repo's `L_s`-fold commuting tower is the
   *free-fermion signature*; integrability-breaking collapses it to one charge. N5 may be
   derivable *conditional on non-integrability* of the emergent dynamics — a far weaker
   premise than the `(L_s−1)`-param admission ray. **Highest value: it reframes N5 from
   "open premise" to "true generically, false only on the retained free surface."**
2. **L6 (link/diagonal RP):** the S₄-transitivity no-go enumerated only signed *site*
   symmetries; a link-reflection transfer matrix is a standard A_min-internal object that
   might not be W-transitive — a concrete N4 selector probe the campaign appears to have
   missed.
3. **L1 (modular/thermal time):** a citable existence theorem for a canonical generator
   from state+algebra, with a precise type-I/II/III reason it fails on the finite surface
   and could live only at the type-III emergent limit — upgrades the N5/native-reframe
   prose to operator-algebra.
4. **L3 (Pauli/Galapon):** finite-dim `tr[T,H]=0` no-go ⇒ no internal uniform clock;
   makes N2b a spectral theorem and bounds N5.
5. **L4 (Rovelli coarse-graining):** orientation (t vs −t) may be sourced from the Record
   coarse-graining (in A_min) rather than the past hypothesis (not in any primitive).

## What NOT to do

- Do not import any of L1/L2/L4 as authority or as closure: each rides on an OPEN GATE
  (thermodynamic limit, choice of emergent dynamics, ergodicity). Translate skeletons into
  native runners and ship as *conditional* boundaries, audited like native theory.
- Do not re-propose standalone Lieb–Robinson cone (L5) — pruned; only the L2⊕L5
  combination is fresh.
- Do not re-run the *site*-exchange S₄ enumeration (done, resid 0); L6 is specifically the
  *link/diagonal* RP construction the prior enumeration did not cover.
- Do not let the kinetic-isotropy reframe (L7) double-count the scale reference.
