# The Four-Axiom Foundation Reviewed As A Theory-Of-Everything Base

**Date:** 2026-08-09
**Type:** meta
**Document class:** F — orientation memo. This memo carries
**no premise or interpretive weight**. It is citable for orientation and scope
discipline only, never as a premise, and it sets, predicts, and requests no
audit status. Every status word it quotes belongs to the surface it is quoted
from; the audit ledger remains the sole authority.

**Subject:** Lattice, Qubit, Admissibility, and Record as stated in
[`MINIMAL_AXIOMS_2026-06-29.md`](../MINIMAL_AXIOMS_2026-06-29.md), read as the
foundation of a theory of everything.

---

## 1. Scope and method

This memo reviews only the foundation. It asks one question: taken as the base
of a theory intended to derive all of physics, are these four axioms the right
four, and if not, what would be better suited?

Three method commitments follow from that scope.

**Downstream results are evidence about the foundation, not the subject.** No
claim in this memo turns on whether a Koide target closes or a CKM identity
holds. Downstream work appears only where it diagnoses the base — most often
where the repo has already proven that the axioms cannot supply something.

**Every criticism is paired with the repo's own record where one exists.** The
framework has an unusually complete negative literature. Most of what follows is
not an outside objection the program has failed to consider; it is a structural
reading of obstructions the program has already proven, one at a time, in
separate lanes. The contribution here is to say what they add up to.

**The alternatives are named concretely.** "Better suited" is only meaningful
against a specific replacement with a specific cost. Section 4 names replacements
at the level of individual axioms and at the level of the whole base, and says
what each would unblock in this repo.

## 2. Summary judgement

The four axioms are not so much wrong as **mis-typed for the job**. Read
literally, they specify a static, classical, volume-extensive mosaic on a
crystal with a preferred frame. Physics is quantum, relativistic, chiral,
area-extensive, and dynamical. Every one of those five mismatches is a
structural property of the axiom text, not a gap in the work built on it.

The sharpest way to see this is to look at what the foundation forbids rather
than what it fails to supply. A missing piece can be derived later. A structural
exclusion cannot — it has to be repaired at the axiom.

The three "roots" the program tracks as its remaining walls are not three
independent research problems. Each is the visible end of one axiom defect:

- the readout/Born root is Record's additive-scalar clause;
- the chirality root is Admissibility's strict nearest-neighbor clause;
- the action/bridge gap is the absence of any variational or amplitude
  structure anywhere in the four axioms.

That is the central finding of this review. Below, the defects are ordered by
how much of the program each one blocks.

## 3. Where the foundation is likely wrong

### 3.1 Admissibility is a classical Gibbs specification, so it cannot generate quantum mechanics

Admissibility says: for each site, the probability distribution over the
possibilities is determined by, and varies with, the nearest-neighbor
conditions. That is the definition of a Markov random field. By the
Hammersley-Clifford correspondence, a positive nearest-neighbor conditional
specification is exactly a Gibbs measure with nearest-neighbor potentials.
Admissibility, read as written, is classical lattice statistical mechanics.

Real, non-negative, locally-conditioned weights cannot produce interference.
There is no phase anywhere in the axiom, and no cancellation between
alternatives is possible in a measure. The Qubit axiom supplies a complex
algebra at a site, but Admissibility never uses its complex structure: it
extracts a probability distribution over possibilities and stops. The framework
recovers quantum behavior in practice only by working inside the operator
algebra — the Tsirelson bound note reaches `2√2` by computing with entangled
vectors on `H_x ⊗ H_y` — but that computation is not licensed by Admissibility,
which speaks only of site-local distributions conditioned on neighbors.

There is a second, sharper version of the same problem. The state of the world
is a configuration of records, locked where recorded and open elsewhere; the
policy record shows that assigning one possibility to *every* site was
explicitly rejected as a hidden-variables picture. That rejection is correct,
but the structure it rejected is close to what the axioms re-instantiate: a
site-local distribution conditioned on adjacent sites, with Record locking
exactly one possibility per recorded site. Whether or not that configuration
reproduces Bell-inequality violations is precisely the question a foundation
must answer before it is usable, and Admissibility as written gives no
mechanism by which it could.

**Severity: foundational.** Nothing that is recognizably quantum mechanics
follows from this axiom, and the program's quantum results are being computed on
a surface the axiom does not describe.

**Repair cost: one word.** See §4.1.

### 3.2 Record's additive scalar readout excludes the observables that carry the physics

Record fixes that a readout value is determined by record content alone, and
that for any finite collection of pairwise-disjoint records, scalar readout `I`
is additive with `I(empty) = 0`.

Additivity over disjoint regions is the signature of an *extensive* quantity.
The observables that actually define modern physics are not extensive:

- **Gauge observables are multiplicative, not additive.** The physical content
  of a gauge field is holonomy — Wilson loops, products of link variables around
  a closed path. A Wilson loop is not the sum of anything over disjoint regions.
- **Correlation observables are products, not sums.** A CHSH correlator is
  `A ⊗ B`. Entanglement entropy is not additive over disjoint regions; that
  non-additivity *is* the phenomenon.

So the two observable classes that carry gauge physics and quantum physics
respectively are both outside the readout Record licenses. This is not a
speculative reading — the repo's own record shows both exclusions biting:

- the Wilson action is carried as an **admitted import**, described in the
  program's own planning surface as the deepest one. That is exactly what one
  expects if the foundation structurally cannot generate holonomy observables;
- the observable-principle note, after five successive narrowings, reaches the
  log-det generator family only through a **declared bridge premise**, with a
  companion no-go exhibiting `log det + ε·Tr` as a countermodel that satisfies
  Record additivity and determinant multiplicativity without being a function of
  `det(D+J)` alone;
- a further no-go establishes that Record additivity does not identify a Born
  branch probability, a determinant modulus, or a log-det as the additive
  scalar, since any power family stays multiplicative and the only bridge to
  additivity is `−c log p` — which is the selector under test.

**Severity: foundational.** This single clause is the readout/Born root, the
Wilson-action import, and the gauge-sector blockage simultaneously.

**Repair cost: one clause.** See §4.2.

### 3.3 The substrate has a preferred frame, so Lorentz invariance is bought rather than derived

`Z^3` with proper cubic rotations supplies the octahedral group — 24 elements —
where physics needs `SO(3)`, and ultimately the Lorentz group. Lattice field
theory has a standard answer: continuous rotation invariance emerges at long
wavelength as an accidental symmetry, with violations suppressed by powers of
the lattice spacing. That answer requires two things the axioms do not provide.

**It requires a continuum limit, which requires criticality.** Emergent
continuous symmetry lives at a second-order critical point where the correlation
length diverges in lattice units. Admissibility fixes one rule with no tuning
parameter and no mechanism that would drive the system to a critical surface.
Absent criticality, correlation lengths are of order one spacing and the
anisotropy is order one, not suppressed. The repo's own continuum-limit note was
demoted on audit to a finite-`h` trend table, with the `h → 0` statement
explicitly not claimed for want of a convergence theorem.

**It requires universality of the emergent light cone, which is not generic.**
Distinct species on a lattice generically acquire distinct limiting velocities;
Lorentz invariance is not an accidental symmetry unless something protects it.
The framework's response is the approved `kinetic_isotropy_primitive`, which
supplies `c_t = c_s` outright. That is the assumption being named honestly, and
naming it honestly does not make it derived. The supporting record is explicit
that this was bought rather than proven: spatial cubic symmetry alone leaves two
independent kinetic coefficients, and the attempt to derive `c_t = c_s` from
four-axis equivalence was found circular.

Worse, the interacting version is quantified and negative. The Lorentz
naturalness note evaluates the Collins-Perez-Sudarsky-Urrutia-Vucetich
regeneration problem on supplied inputs and concludes the suppression fails **by
4 to 16 orders of magnitude**. A companion threshold result retires the weaker
"positive anomalous dimension suffices" route.

This matters more than any other single mismatch because Lorentz symmetry is the
most precisely tested symmetry in physics. A foundation with a preferred frame
starts in tension with the tightest experimental bounds available, and its only
escape route is a protection mechanism the axioms do not contain.

**Severity: foundational.** **Repair: not available within a fixed lattice.**
See §4.4.

### 3.4 One permanent record per site gives every region a finite history budget

Record fixes that a site never carries more than one record and that records are
permanent. Combined, these give a monotone, append-only, non-erasable world: the
recorded region only grows, and once a site is recorded it is inert forever.

Consider what persistence then costs. A single stable particle existing for
cosmological time participates in an unbounded number of events. Each event that
registers anything must consume fresh, previously-open sites, permanently. A
bounded spatial region therefore contains a bounded total quantity of history,
after which nothing further can happen inside it. Either the recorded set stays
forever sparse — in which case the open sites, which carry no records and are not
readable, are doing the physical work and are outside the readable ontology — or
the recorded region grows and physics is confined to a moving frontier through an
inert bulk.

This is why "physical persistence dynamics" sits on the open-gate list. It is not
an unfinished derivation; it is a consequence of the axiom. The repo's working
picture already reflects it: the record-occupancy front is treated as a monotone
domain wall, with chirality fixed by the occupancy-gradient sign, and uniform
empty or uniform full occupancy carrying no front and no light mode.

There is a second cost. Permanence hard-codes irreversibility into the
fundamental law. Every successful fundamental theory we have is microscopically
reversible, with irreversibility emerging statistically from initial conditions,
and the framework's own strong-CP and CPT-adjacent work depends on that
reversibility. And the axiom does not even discharge the obligation it appears
to buy: the past-hypothesis low-entropy magnitude is still carried separately, as
a scope condition. An irreversible fundamental law that still needs a past
hypothesis has paid the price and not collected.

**Severity: high.** **Repair: demote permanence.** See §4.3.

### 3.5 One qubit per site is volume-extensive; the world is area-extensive

The axioms assign an independent two-dimensional system to every site of `Z^3`.
The number of independent degrees of freedom in a ball of radius `R` therefore
grows as `R^3`. Black-hole thermodynamics says the maximum entropy of that region
grows as `R^2` — the Bekenstein-Hawking area law. At Planck spacing the axioms
overcount the independent content of a region by a factor of order `R/a`.

Record's additivity clause makes this worse rather than better: additivity of
readout over disjoint regions is a volume law written into the foundation, at
precisely the point where nature supplies an area law.

The symptom is visible in the repo's area-law lane, which is a long sequence of
attempts to reach the coefficient `1/4` from the entanglement side and a
corresponding sequence of no-gos — the simple-fiber Widom class closed
negatively at `c_Widom ≤ 1/6`, with the multipocket-selector, primitive
finite-edge entropy, and algebraic finite-Schmidt-spectrum shortcuts also closed
negatively. A foundation whose degree-of-freedom count has the wrong scaling
should be expected to miss an area-law coefficient.

**Severity: high, and it is the defect most often fatal to lattice ontologies.**
See §4.6.

### 3.6 Nothing in the axioms makes anything happen, and nothing says how two sites compose

Three absences compound.

**No dynamics.** The axioms supply no Hamiltonian, transfer operator, transition
weight, or time metric, and the memo says so. The consequence is stronger than
"dynamics is future work": the dynamics-selection firewall establishes that
record preservation plus locality plus hermiticity yields only *class
membership*, and that `H = 0` remains in the class. The foundation does not
exclude nothing happening.

**No time.** Time is not in the Lattice axiom. In practice the work uses
"record time" as a fourth coordinate, and the framework says so plainly — the
carrier is natively three-dimensional space plus record time, and *the
dimensional interpretation of record-time remains open*. The single-clock lane
then proves the axis cannot be derived at all: every retained candidate
axis-anchoring structure is exactly transported onto a spatial axis with
residuals of zero, so the time axis can only be declared, and the minimal
selecting input is computed to be a single per-axis boundary-condition datum.

**No composition rule.** The Qubit axiom is a one-site statement. That two
distinct sites compose by tensor product — the fact without which no
multi-site quantum statement can even be written — required a separate bridge
note, and the joint-presentation note states that the common joint presentation
and distinct-site commutation are supplied, not derived from the one-site axiom
wording.

A foundation that cannot say how two subsystems combine, or that anything
changes, is a kinematic vocabulary rather than a physical theory. Composition is
not a technical convenience; in every operational reconstruction of quantum
theory it is where the physical content lives.

**Severity: foundational.** See §4.1 and §4.5.

### 3.7 The site algebra is provably too small

`M_2(C)` is four real dimensions per site. The repo has established, in
independent lanes, four separate ways this is insufficient — and in each case the
obstruction is dimensional or parity-based, so it cannot be relieved by cleverer
derivation.

- **No four-dimensional Clifford structure.** The axiom-stack minimality
  result proves that no `A_min`-derivable operator algebra carries four
  Hermitian generators with `{γ_i, γ_j} = 2δ_{ij}I`. Without a `Cl_4`
  action there is no native spacetime spinor and no native Dirac operator.
  The minimal extension that would supply it was formally declined.
- **No color.** A single qubit link natively carries `u(2)`, and `dim 4 < 8 =
  dim su(3)`. `SU(3)` cannot be a link algebra on this substrate. The
  independent `Cl(3)⊗Cl(3) → Spin(6) ≅ SU(4)` route terminates in an `SU(4)`
  admission rather than color.
- **No statistics.** Lattice plus Qubit does not derive Grassmann/fermionic
  statistics: the fermionic Jordan-Wigner frame and a hard-core-boson reading
  sit on equal ungraded footing. The rotation-exchange route to spin-statistics
  fails for a reason that is intrinsic to discreteness — the Finkelstein-Rubinstein
  argument needs `π_1(SO(3)) = Z_2` in a *continuous* configuration space, and a
  bare site set supplies no such homotopy.
- **No generations.** The generation-triplet parity argument is clean and
  final in its scope: faithful `SU(2)` centre action occurs exactly on
  half-integer-spin blocks, all of even dimension, and no sum of even integers
  equals three.

There is a general pattern behind the last point worth stating directly. Lattice
discretizations generate species multiplicities in **powers of two** — staggered
tastes, doublers, Clifford module dimensions. The observed generation count is
three. Asking a two-dimensional algebra on a cubic lattice to produce a three
is asking the wrong kind of structure for the answer.

**Severity: high.** This is the whole chirality/generation root. See §4.5 and §4.7.

### 3.8 Strict nearest-neighbor locality forbids chiral fermions

Admissibility fixes *one nearest-neighbor rule*. Ultralocality of exactly this
kind is a hypothesis of the Nielsen-Ninomiya theorem: a local, translation-
invariant, Hermitian lattice theory with a conserved chiral charge carries equal
numbers of left- and right-handed Weyl modes. The Standard Model is chiral. So
the axiom, as worded, excludes the matter content it is meant to explain.

All three known escapes break one of the four axioms:

| Escape | What it costs |
|---|---|
| Ginsparg-Wilson / overlap | Ultralocality — couplings decay exponentially but are not strictly nearest-neighbor. Breaks **Admissibility** as worded. |
| Domain-wall fermions | Requires an extra dimension. Breaks **Lattice** at `Z^3`. |
| Symmetric mass generation | Requires anomaly-free multiplets far larger than one qubit. Breaks **Qubit**. |

The repo's chirality record is consistent with exactly this. The framework's own
reading is that its chirality no-go is narrow, forbidding only a particular
hybrid identification; that is true of the specific result but does not touch
the general theorem, whose hypotheses the Admissibility axiom satisfies. And the
working construction that does produce a chiral edge is a **domain wall** — that
is, the second row of the table, obtained by treating record-time as an extra
coordinate.

**Severity: high.** **Repair cost: one word — replace "nearest-neighbor" with
"exponentially local."** See §4.5.

### 3.9 The four axioms hide an arbitrary function

Admissibility posits *one fixed* nearest-neighbor rule. It never says which. The
entire physical content of the theory is that unspecified conditional
distribution, drawn from an infinite-dimensional space of cubic-covariant
candidates.

This means the advertised premise count is not the real premise count. Four
axioms plus one unspecified function is not more parsimonious than a
conventional foundation; it is less specified. Minimality of axiom *count* is
being read as minimality of axiom *content*, and those come apart precisely when
one axiom quantifies existentially over a function space.

The framework's own July exercise reached this conclusion independently and
stated it about as plainly as it can be stated: a predictively complete
framework needs one exact law identity or one exactly defined physical-
equivalence class of law representatives, every slogan-level substitute
*"leaves physically different rules alive,"* and no candidate fills the exact
law contract *"without a free kernel, coupling, schedule, branch semantic,
boundary, or other physical fork."*

**Severity: high, and it is a presentation defect as much as a physics one.**
The honest statement of the foundation is "four axioms, three approved
primitives, and one undetermined kernel."

### 3.10 There is no symmetry principle, therefore no route to conservation laws

The axioms contain no action, no variational principle, and no continuous
symmetry group. Noether's theorem is therefore unavailable, and with it every
derivation of energy, momentum, angular momentum, and charge conservation.

This is a large hole to have in a foundation and it is easy to miss because
conservation laws are usually assumed rather than derived in downstream work.
But a theory of everything that cannot derive energy conservation has not
explained one of the most basic facts about the world. Every alternative in §4
that supplies an action or a symmetry group fixes this as a side effect; no
repair internal to the four axioms does.

### 3.11 Background dependence blocks general relativity — including the sign of gravity

A fixed `Z^3` has fixed dimension, fixed topology, and fixed spacing. There is no
diffeomorphism invariance, hence no constraint algebra and no natural route to
the Einstein equations; no topology change; and no straightforward account of
cosmological expansion, since what would expand is the lattice spacing, which the
axioms hold fixed.

The repo's positive background-independence claim is a numerical observation on a
*fixed* `N = 20` cubic lattice — effective propagator geometry responding to a
source. That is emergent effective geometry on a fixed graph, which is a
different and much weaker thing than background independence in the sense
general relativity requires. The lattice never moves.

The severity is best shown by one result rather than by argument. The gravity-sign
sharpening proves that **attraction is not derivable** on the retained surface:
the Green's function route is blind to the sign, the energy-stability route would
select *repulsion* because the attractive case is unbounded below, and the
arrow/entropy route is sign-agnostic because clumping lowers configurational
entropy. The sign then reduces to a shared orientation datum that Record's
conjugation structure cannot select. Separately, the degenerate-supermetric
result finds no normalization making both graviton channels healthy.

A foundation that cannot derive that gravity attracts is not yet a foundation for
gravity.

**Severity: high.** See §4.4 and §4.8.

### 3.12 Three dimensions and cubic adjacency are not derived

The `d = 3` argument is a pinch between an upper leg and a lower leg. The upper
leg — a Dirac-square nearest-neighbor carrier exists on a one-qubit-per-site
lattice iff `d ≤ 3` — is a consequence of the **Qubit** axiom, so it does not
independently support the Lattice axiom; the two legs lean on each other. The
lower leg rests on attractive gravity and stable atoms, which are **empirical
boundary conditions**, not derivations. The repo says as much in its own words:
three spatial dimensions is *"a CHOICE, not derivable,"* and the dimension-selection
note explicitly disclaims deriving `Z^3` from a dimension-free baseline. An
independent `Cl(3)`-minimality route records its own circularity, since its
`2^n = 8` requirement conditions on a `Z^3`-proven orbit structure.

**Nothing anywhere argues for cubic adjacency over any other three-dimensional
lattice.** This is not cosmetic. The leading lattice correction to gravity is a
cubic-harmonic anisotropy, `G(r) = 1/(4πr) + [5/(32π)]K_4(n̂)/r^3 + O(1/r^5)`,
with zero free parameters — so the choice of Bravais lattice is directly
physical, and it was never made on physical grounds.

## 4. Alternatives, ranked by leverage

Each entry states what it replaces, what it buys, what it costs, and what in this
repo it would unblock. The ordering is by leverage per unit of disruption.

### 4.1 Replace the probability in Admissibility with an amplitude

**Replaces:** "the probability distribution over the possibilities is determined
by ... the nearest-neighbor conditions" with a complex-valued local weight.

This is the single highest-leverage change available, and it is one word. A
non-negative local weight is classical statistical mechanics; a complex local
weight is a lattice path integral. The difference between a Markov random field
and a quantum theory is exactly that.

**Buys:** interference and entanglement natively rather than by importing an
operator-algebra surface the axiom does not describe; unitarity via the transfer
matrix; a classical limit by stationary phase; and — through the action that a
path integral requires — Noether's theorem and hence conservation laws (§3.10).

**Costs:** an action must be supplied. This is not a new debt. The Wilson action
is already an admitted import; this change converts a hidden liability into a
named premise, which the program's own accounting discipline should prefer.

**Unblocks in this repo:** the action/bridge gap; the interference structure the
Tsirelson result presumes; and the honest home for the reflection-positivity and
`OS0` machinery already in use.

**The natural destination is Osterwalder-Schrader.** If the substrate is a
Euclidean lattice with complex local weights and reflection positivity, then the
OS axioms are the mature, precise axiomatization of exactly that object, and they
*deliver as theorems* what this program lists as open gates: a Hilbert space, a
self-adjoint Hamiltonian, unitarity, the spectrum condition, and Poincaré
covariance in the continuum limit. The framework is already using OS vocabulary
downstream. Adopting it at the foundation would be a consolidation, not an
importation.

### 4.2 Replace additive scalar readout with a local net of algebras

**Replaces:** Record's clause that scalar readout is additive over finite
disjoint record collections.

**Buys:** the observables the current clause excludes (§3.2) — holonomies,
correlators, entropies — become expressible. In the Haag-Kastler form (a net of
algebras over regions with isotony, locality, and covariance), one also inherits
as *theorems* several things this program currently carries as open or imported:
the spin-statistics theorem, the CPT theorem, and the DHR analysis of
superselection sectors, which classifies which charges can exist and in which
representations.

**Costs:** algebraic quantum field theory is a framework, not a specific theory;
it does not by itself select the Standard Model. It also presumes a spacetime
with a causal structure, which interacts with §4.4.

**Unblocks in this repo:** the readout/Born root; the Wilson-action import; the
gauge-selection question of why `su(3) + su(2) + u(1)` rather than `u(6)`, which
is a superselection question in disguise; and the spin-statistics row, currently
high in the bounded-to-positive restatement ranking while the underlying
statistics result says the axioms do not derive fermionic statistics at all.

**A cheaper partial version exists and should be taken regardless.** The
framework's own result is that normalization on *every finite effect partition*
forces the Born trace form, while product-menu relaxation admits a non-Born
grading, and that no menu grade is selected. That is Busch's theorem doing its
work — and note that Busch's POVM form is essential here, because Gleason's
theorem fails in dimension two, so the `M_2(C)` choice sits at precisely the one
dimension where the projective argument gives nothing. **Making full effect-menu
eligibility part of the Record axiom closes the Born form.** It is one clause,
it is already proven sufficient in-repo, and it directly retires the largest
single item on the readout root.

### 4.3 Replace Record with decoherent histories

**Replaces:** permanence and one-record-per-site as primitives.

**Buys:** records become *derived* — quasi-classical branches selected by a
decoherence condition on histories, permanent for all practical purposes rather
than by fiat. This removes the irreversibility defect (§3.4) at a stroke, keeps
the fundamental law reversible and CPT-respecting, restores a sane account of
persistent matter, and gives measurement and the arrow of time a home that the
current axiom denies them.

**Costs:** the set-selection problem — which family of histories decoheres — is a
genuine open problem in that programme. It is, however, a *better* open problem
than the current one, because it is a question about dynamics rather than a
structural exclusion.

**Unblocks in this repo:** physical persistence dynamics; record-production
dynamics; the arrow; the past-hypothesis scope condition, which becomes the
ordinary statistical-mechanics assumption it already is everywhere else in
physics.

**Retaining the framework's instinct.** The intuition that definite outcomes are
ontologically primitive is shared by serious programmes and need not be
abandoned. What should be abandoned is deriving that primitiveness from
*permanence of a site-local token*, which is what forces the finite history
budget.

### 4.4 Replace the fixed lattice with a Lorentz-invariant discretization

**Replaces:** `Z^3` with cubic adjacency.

If discreteness is the non-negotiable commitment, then **causal sets** are the
one known way to have it without a preferred frame. A Poisson sprinkling into
Minkowski space is provably Lorentz invariant — there is no preferred direction
in the distribution, which is exactly what a lattice cannot achieve. Order gives
causal structure, number gives volume, and dimension and topology emerge rather
than being posited.

**Buys:** the elimination of §3.3 outright, and with it the
`kinetic_isotropy_primitive`, the naturalness gap, and the cubic-anisotropy
fingerprint. Background independence and dimensional flexibility come with it.

**Costs:** dynamics is hard (classical sequential growth models are the state of
the art and are not yet a quantum theory), and matter content is harder still.
This is a trade of a solved-but-wrong-frame problem for an open-but-right-frame
problem.

**Assessment:** if the program's identity is "physics is fundamentally
discrete," this is the alternative that preserves the identity while removing the
defect that is most likely to be fatal. That the repo contains no evaluation of
it — no causal-set, FCC, BCC, or amorphous-substrate note anywhere — is the most
conspicuous gap in an otherwise exhaustive negative literature.

### 4.5 If the lattice stays, move to `Z^4` at criticality and be honest about it

**Replaces:** `Z^3` plus an undeclared record-time coordinate with a
four-dimensional Euclidean lattice.

This is the least disruptive alternative, because it is what the work already
does. Record-time is already used as a fourth coordinate; the chiral edge is
already obtained from a domain wall along it; the theta carrier is already
computed on a Euclidean four-torus. Promoting record-time to a genuine lattice
direction changes the axioms to match the practice.

**Buys:** domain-wall fermions become available and legitimate, which is a real
route to chirality (§3.8) rather than a diagnostic; the dimensional
interpretation of record-time stops being open; a continuum limit becomes
statable; and the entire apparatus of lattice field theory — the only version of
"the universe is a lattice" that has ever reproduced measured hadron physics to
percent accuracy — becomes available without apology.

**Costs:** criticality must be assumed or explained; strict nearest-neighbor
locality must be relaxed to exponential locality for Ginsparg-Wilson chirality;
and the program must stop describing itself as a four-axiom theory of everything
and start describing itself as a specific lattice model, which is a different and
more defensible claim.

**Recommended companion change, independent of everything else:** relax
"nearest-neighbor" to "exponentially local" in Admissibility. It is one word, it
costs nothing anyone would miss, and it removes the hypothesis that makes
Nielsen-Ninomiya bite.

### 4.6 Replace the site-local Hilbert space with an entanglement-first substrate

**Replaces:** the assignment of an independent qubit to every site.

Tensor-network substrates — MERA and holographic codes in particular — build
geometry out of the entanglement pattern rather than assigning independent
degrees of freedom to points. Area-law entanglement is a structural property of
the construction rather than a coefficient to be chased.

**Buys:** the correct scaling of degrees of freedom (§3.5); emergent curved
geometry from a discrete network; and a principled account of why the
holographic bound holds rather than a conflict with it.

**Costs:** the best-developed versions live in anti-de Sitter boundary
conditions, and our universe is de Sitter. This is a real and unresolved
mismatch.

**Unblocks in this repo:** the entire area-law lane, including the `1/4`
coefficient the current substrate has repeatedly failed to reach.

### 4.7 Replace `M_2(C)` with an algebra chosen for the job

Three options, in increasing order of specificity.

**Operational reconstruction (Hardy; Chiribella-D'Ariano-Perinotti;
Masanes-Müller).** These derive the complex Hilbert-space formalism — including
composition and the Born rule — from operational postulates such as causality,
purification, local tomography, and ideal compression. **Buys:** "why a complex
matrix algebra" stops being an unexplained explainer and becomes a theorem, and
the composition rule (§3.6) comes with it rather than needing a bridge note.
**Costs:** it still does not say which system sits where. **Assessment:** this is
strictly better than positing `M_2(C)`, and it is the change most aligned with
the program's own minimality discipline, since it *reduces* supplied content.

**Connes' spectral triple.** If the commitment is specifically "a finite algebra
at each point," then the mature version of that idea is noncommutative geometry,
where the finite algebra `C ⊕ H ⊕ M_3(C)` together with the spectral action
yields the Standard Model gauge group, the fermion representations, the Higgs
sector, and the Einstein-Hilbert term. **Buys:** exactly the questions this
program currently has stuck or owner-pending — hypercharge, why
`su(3) + su(2) + u(1)`, the Higgs. **Costs:** the finite algebra is itself chosen
to fit, and the framework's cosmological predictions have had a mixed record.
**Assessment:** the repo already admits Chamseddine-Connes machinery as an import
in several places. Adopting it at the foundation rather than borrowing it
downstream would consolidate rather than complicate. `M_2(C)` is, in effect, an
amateur version of the same idea with an algebra that is too small.

**The exceptional Jordan algebra `J_3(O)`.** If the target is three generations
from an algebraic structure, then use an algebra with a three in it. The `3 × 3`
octonionic Hermitian matrices carry the generation index as the matrix size, and
the associated automorphism and structure groups have been argued to yield the
Standard Model symmetry. **Buys:** a candidate answer to the program's declared
prize. **Costs:** speculative and not yet a dynamical theory. **Assessment:**
worth an evaluation note. `M_2(C)` contains no three anywhere; the parity
obstruction in §3.7 is the framework discovering this the hard way.

### 4.8 For gravity: derive geometry rather than embed it

The gravity-sign no-go (§3.11) is decisive about the current base and points at
what a replacement needs. Loop quantum gravity is the relevant contrast: it does
not *assume* discreteness, it *derives* discrete spectra for area and volume
operators by quantizing general relativity, and diffeomorphism invariance is
built in rather than absent. **Buys:** background independence, a derived rather
than posited discreteness, and the constraint algebra that makes the Einstein
equations reachable. **Costs:** the classical limit and matter coupling are open.
**Assessment:** for the specific question "why is spacetime discrete," deriving
the discreteness is a strictly stronger position than positing a lattice, and it
is the position that makes the sign of gravity a dynamical consequence rather
than an orientation datum that must be admitted.

## 5. Two coherent paths

The alternatives above do not all compose. Two do.

### Path A — minimal repair, keeping the program's identity

Six clause-level edits, in dependency order:

1. Admissibility: local weight becomes **complex** (§4.1).
2. Admissibility: **"nearest-neighbor" becomes "exponentially local"** (§4.5).
3. Lattice: **record-time becomes a fourth lattice direction** (§4.5).
4. Record: **full effect-menu eligibility** replaces bare scalar additivity
   (§4.2, cheap version) — this alone closes the Born form.
5. Record: **permanence demoted** to a derived, past-hypothesis-conditioned
   statement (§4.3).
6. Admissibility: the kernel is **named as a premise** or derived from a
   variational principle (§3.9).

Edits 1, 2, and 3 taken together have a name: this is Euclidean lattice field
theory on `Z^4` at a critical point. That is a well-posed and genuinely
successful research program. What it is not is a four-axiom derivation of
everything — it is a specific model with a specific action, and its parameters
are inputs. Path A therefore buys enormous technical capability at the cost of
the program's headline claim.

Path A does **not** repair §3.3 (preferred frame), §3.5 (volume law), or §3.11
(background dependence). Those are properties of *having a lattice at all*.

### Path B — rebuild on a base typed for the job

Foundation: operational reconstruction for the state space (§4.7), a local net
for observables (§4.2), a Lorentz-invariant discrete or emergent substrate
(§4.4), and decoherent histories for records (§4.3). This addresses every defect
in §3, at the cost of discarding most of the current derivational apparatus.

### Recommendation

**Take edits 2, 4, and 6 of Path A immediately, regardless of anything else.**
They are individually cheap, each removes a named blocker, and none of them
commits the program to a direction:

- edit 2 removes the Nielsen-Ninomiya hypothesis for one word;
- edit 4 closes the Born form using a result the repo has already proven;
- edit 6 makes the premise accounting honest, which the program's own audit
  discipline should already require.

**Then decide the identity question before doing more downstream work.** The
program is currently paying the full cost of being a lattice theory — preferred
frame, volume law, background dependence, cubic anisotropy, powers-of-two species
counting — while declining the one benefit lattices actually deliver, which is
being a *calculational* scheme for a continuum theory defined elsewhere. That is
the worst square of the matrix. Either commit to the lattice as a regulator
(Path A) or commit to discreteness done in a Lorentz-invariant way (§4.4). The
current position is unstable in a way no amount of downstream derivation will
fix.

## 6. What the foundation gets right

Three things, stated plainly because they are real and because a review that
only subtracts is not useful.

**The premise discipline is exemplary and should survive any rebuild.** The
refusal to let downstream content become premises, the premise-hash guard that
invalidates dependent audits when axiom text changes, the requirement that a
proposal never becomes a premise by itself, and the ban on citing policy as
physics are all better than standard practice in theoretical physics. The
negative literature — a large, systematic, honestly-maintained record of what has
been *proven impossible* from the base — is the most valuable asset in this
repository and is rarer than any positive result in it.

**The self-correction is real.** A conformal-class result was withdrawn by its
own authors for having consumed a no-go as a positive input. A continuum-limit
claim was demoted on audit. An axiom-text error was corrected by a downstream
note. A `Cl(3)`-module theorem records its own load-bearing algebra error. This
is what a healthy program looks like from the inside.

**Two of the four instincts are sound.** That definite outcomes are
ontologically primitive is a defensible position with serious company. That the
right notion of an observable is a local, region-indexed quantity is precisely
the algebraic-quantum-field-theory instinct — the defect in §3.2 is that it was
formalized as *additivity* rather than as a *net*, which is a fixable error in
formalization rather than a wrong idea.

## 7. What this review does not claim

It does not claim that any specific downstream result is wrong; downstream
content was read only as evidence about the base. It does not claim that any
alternative in §4 is a working theory of everything — none of them is, and each
carries the costs recorded against it. It does not claim the four axioms are
inconsistent; no contradiction is exhibited here, and the existence question is
raised in §3.9 rather than answered. It does not claim that the Lorentz,
holography, or Bell tensions are formal contradictions rather than severe
tensions requiring a mechanism. It sets, predicts, and requests no audit status,
and it is not a proposal for an axiom edit: any such edit runs through the
owner-approval channel in the axiom-minimality policy, not through an orientation
memo.

## 8. Sources

Axiom text and policy: [`MINIMAL_AXIOMS_2026-06-29.md`](../MINIMAL_AXIOMS_2026-06-29.md),
[`AXIOM_MINIMALITY_POLICY.md`](../audit/AXIOM_MINIMALITY_POLICY.md),
[`axiom_premise_nodes.json`](../audit/data/axiom_premise_nodes.json).

Load-bearing negative results cited above, by section:

- §3.2 — [`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](../OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md),
  [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](../OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
- §3.3 — [`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](../LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md),
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](../SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md),
  [`KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md`](../KINETIC_ISOTROPY_B4_TRANSITIVITY_ROUTE_NO_GO_2026-06-20.md),
  [`CONTINUUM_LIMIT_NOTE.md`](../CONTINUUM_LIMIT_NOTE.md)
- §3.4 — [`RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md`](../RECORD_FORMATION_FRONT_IS_THE_DOMAIN_WALL_FREE_FIELD_BOUNDED_THEOREM_NOTE_2026-07-05.md)
- §3.5 — [`AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md`](../AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25.md)
- §3.6 — [`DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md`](../DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md),
  [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](../SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md),
  [`TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](../TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md),
  [`QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md`](../QUBIT_LATTICE_JOINT_PRESENTATION_TENSOR_SUBSTRATE_BRIDGE_NOTE_2026-07-09.md),
  [`THETA_NATIVE_RECORD_TIME_SPATIAL_SPLIT_ORIENTATION_IMPORT_LOCALIZATION_CONJUGATION_PARITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-07-03.md`](../THETA_NATIVE_RECORD_TIME_SPATIAL_SPLIT_ORIENTATION_IMPORT_LOCALIZATION_CONJUGATION_PARITY_BRIDGE_BOUNDED_THEOREM_NOTE_2026-07-03.md)
- §3.7 — [`AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md`](../AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md),
  [`EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_RECORD_TEXT_NARROW_NO_GO_NOTE_2026-06-08.md`](../EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_RECORD_TEXT_NARROW_NO_GO_NOTE_2026-06-08.md),
  [`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`](../STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md),
  [`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`](../FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md),
  [`GENERATION_TRIPLET_DIMENSION_PARITY_NO_FAITHFUL_Z_NARROW_NO_GO_NOTE.md`](../GENERATION_TRIPLET_DIMENSION_PARITY_NO_FAITHFUL_Z_NARROW_NO_GO_NOTE.md)
- §3.11 — [`GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md`](../GRAVITY_SIGN_NOT_FORCED_BY_ARROW_STABILITY_OR_SPECTRAL_ROUTES_NO_GO_SHARPENING_NOTE_2026-06-08.md),
  [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](../UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md),
  [`BACKGROUND_INDEPENDENCE_NOTE.md`](../BACKGROUND_INDEPENDENCE_NOTE.md)
- §3.12 — [`D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md`](../D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md),
  [`DIMENSION_SELECTION_NOTE.md`](../DIMENSION_SELECTION_NOTE.md),
  [`AXIOM_REDUCTION_NOTE.md`](../AXIOM_REDUCTION_NOTE.md),
  [`GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md`](../GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md)
- §4.2 — [`BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md`](../BORN_FORM_EFFECT_MENU_SITEWISE_FORCING_AND_PRODUCT_MENU_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-17.md),
  [`COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](../COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
