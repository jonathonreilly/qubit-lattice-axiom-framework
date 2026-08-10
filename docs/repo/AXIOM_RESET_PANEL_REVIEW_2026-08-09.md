# Six-Reviewer Panel On The Proposed Axiom Reset, And The Decision To Withdraw It

**Date:** 2026-08-09
**Type:** meta
**Document class:** F — orientation memo. This memo carries
**no premise or interpretive weight**. It is citable for orientation and scope
discipline only, never as a premise, and it sets, predicts, and requests no
audit status.

**Subject:** independent adversarial review of the drafted axiom set in
[`AXIOM_RESET_PROPOSAL_2026-08-09.md`](../AXIOM_RESET_PROPOSAL_2026-08-09.md).

---

## 1. Verdict

Six reviewers were given the drafted axiom text verbatim and nothing else — no
access to the proposal's rationale, the probe results, or any earlier
conclusion, so that none could anchor on them. Each was given a distinct lens
and instructed that a review finding nothing wrong is a failed review.

| Lens | Verdict |
|---|---|
| Quantum foundations / reconstruction | **FATAL** |
| Algebraic QFT / operator algebras | **FATAL** |
| Quantum gravity / causal sets | **FATAL** |
| Lattice QFT / phenomenology | **FATAL** |
| Mathematical rigour / logic | **FATAL** |
| Journal referee | **Reject** |

**Unanimous. The proposed axiom set is withdrawn.** Not revised — withdrawn.
Four independent fatal defects were found, each sufficient on its own, and the
one claim that would have made the draft novel is false as stated.

## 2. What the panel found that I did not

Objections reached independently by three or more reviewers, with my own
verification where the claim was checkable.

### 2.1 The axioms have a classical model, so nothing quantum is entailed

Take any locally finite order, assign each region an **abelian** algebra of
functions, and take a classical Gaussian random field. Every clause is
satisfied: isotony, commutation at order-unrelatedness (trivially — everything
commutes), generation of unions, automorphism invariance, decay, two-point
positivity, and "the antisymmetric part is the commutator supplied by the
order" — because the only commutator the axioms supply is the *vanishing* one.

That model is a local hidden-variable theory. CHSH ≤ 2 in it. Bell violation is
not derivable, Kochen–Specker contextuality is not derivable, and the complex
Hilbert space is not forced. **A foundation for quantum theory that is satisfied
by classical statistical field theory has not stated what makes the theory
quantum.**

I verified the degenerate limiting case directly: the one-event model with
`A(R) = C`, `f = 1` satisfies every clause, with the two-point function
positive-semidefinite and antisymmetric part `= commutator = 0`. **Confirmed.**

### 2.2 "The commutator supplied by the order" is a dangling reference

Five reviewers independently flagged this as the largest smuggle in the text. A
partial order supplies only the *vanishing* of commutators at unrelated pairs —
microcausality. It never supplies a non-zero commutator. The object I meant is
the Pauli–Jordan function `Δ = G_R − G_A`, whose value is the Peierls bracket,
constructed from a **Lagrangian's** retarded-minus-advanced Green functions. On
a causal set it requires Johnston's propagator, which is explicitly
dimension-specific — the causal matrix in 2d, the *link* matrix with
normalisation `1/(2π√6)` in 4d — plus a mass and a sprinkling density.

So the clause imports an action, a spacetime dimension, a mass and a discreteness
scale, through a phrase advertised as supplying none of them. **The draft's
central claim — that it smuggles no imports — is false, and this is where it
fails.**

### 2.3 ACTUALITY is inconsistent, and it is the clause I added to fix Born

All six reviewers hit this. "Every finite partition of the region's unit into
positive observables is such a menu" plus "an outcome is exactly one of the
mutually exclusive alternatives" asserts a non-contextual `{0,1}` valuation
across all POVMs — forbidden by Kochen–Specker for dimension ≥ 3 and by
Busch/Caves–Fuchs–Manne–Renes even at dimension 2. Separately, POVM elements are
in general non-orthogonal, so "mutually exclusive" is simply false of them.

I verified it with a two-line counterexample: `{I/2, I/2}` is a legitimate menu
under the drafted clause — both elements positive, summing to the unit — so
"exactly one occurs" demands `v(I/2) + v(I/2) = 1` with `v` two-valued, i.e.
`v(I/2) = 1/2`. No such function exists, and the two elements are literally the
same operator. **Confirmed.**

This is the clause I added *specifically* to secure the Born result. It secures
probabilities and destroys actuality.

### 2.4 The locality clause contradicts the reason for the substrate change

The deepest finding, and it is theorem-backed. **Bombelli–Henson–Sorkin**
proves there is no way to associate a finite-valency graph to a sprinkling
consistently with Lorentz invariance: the shell of nearest neighbours is a
non-compact hyperboloid, so every element has infinitely many links. This forces
a choice — finite valency and a preferred frame, or Lorentz invariance and
infinite valency, in which case "decays with order separation" has no finite
neighbourhood to decay over.

Worse, "order separation" is undefined exactly where locality must bite: between
*unrelated* events, which is the spacelike case. I measured both: in a 120-event
sprinkling **45.8%** of ordered pairs are incomparable, and mean link valency
grows `1.80 → 2.82 → 3.58 → 4.21` as the sprinkling densifies from 30 to 240
events, with no sign of saturating. **Confirmed.**

The causal-set literature's resolution is the opposite of mine: discreteness plus
Lorentz invariance *forces* non-locality, and the Benincasa–Dowker operators use
infinite alternating sums plus a separate mesoscale. **My locality clause forbids
the only known cure for my own substrate's problem.**

### 2.5 I claimed a theorem's conclusion while omitting its hypothesis

Lorentz invariance in causal set theory is a property of the **sprinkling
measure**, not of any individual order. An individual sprinkled causal set has no
spacetime symmetry at all. My Law axiom asks for invariance under
`Aut(order)` — the wrong group entirely — while the frame-freedom I claimed
comes from Poisson equivariance, which my axioms never supply.

My own check was inconclusive here and I report it as such: using colour
refinement (a *sufficient* condition for rigidity, so a lower bound) I found only
9–14 of 30 sprinklings provably rigid at N = 20–160, and small causal sets are
frequently *not* rigid (13/40 at N=5). So I did not reproduce the reviewers'
"almost surely trivial" claim at testable sizes. It rests on asymptotic
combinatorics I did not verify. **Not confirmed by me; the wrong-group objection
stands regardless, and is the more serious half.**

### 2.6 My chirality claim is mis-attributed — my own data disproved it

The referee's sharpest hit. Nielsen–Ninomiya's locality hypothesis is **not**
nearest-neighbour coupling; it is exponential boundedness. Exponentially decaying
couplings sit *inside* the NN hypothesis. So relaxing "nearest-neighbour" to
"local" removes no NN hypothesis whatsoever.

I re-ran the audit and it is unambiguous. The naive operator is strictly local
*and* exactly chiral, and doubles — fully consistent with NN, no hypothesis
violated. The overlap operator has `max |{γ5,D}| = 4.0`, i.e. it has **given up
exact chiral symmetry**, and satisfies Ginsparg–Wilson instead to `1.3e-15`. The
hypothesis it violates is exact chiral symmetry, not locality. **My earlier probe
measured exactly these numbers and I drew the opposite inference from them.**

One qualification survives, and I checked it rather than assuming it: scanning
40 000 strictly nearest-neighbour γ5-hermitian operators, the best
Ginsparg–Wilson defect is `1.1e-01` — ultralocality blocks the GW route
(Horváth). So relaxing nearest-neighbour is **necessary to permit** the real
mechanism, but it is not the mechanism, and "one word unlocks chirality" was
wrong.

### 2.7 The reduction claim is an accounting artifact

I counted clauses. Clause count is not supplied structure. `Z^3` designates
**one** structure; "a poset with finite intervals" designates a class whose size
grows as `2^(n²/4)`. Weakening an axiom *enlarges* the model class, which is a
reduction in assumptions only if something later cuts it down — and nothing does,
because I withheld the dynamics.

By Kleitman–Rothschild the class is asymptotically **100% non-manifoldlike**
three-layer orders. The only known suppression is a path-sum with an action —
which "one fixed assignment ... invariant under every automorphism of the
supplied order" structurally forbids, since it fixes the order and sums over
nothing. **The substrate is a fixed background, so the draft contains no
gravity**, which for a TOE foundation is disqualifying on its own.

### 2.8 Roughly 90–95% prior art, uncited

The referee mapped it clause by clause: Substrate is Bombelli–Lee–Meyer–Sorkin
(1987); Observables is Haag–Kastler (1964), already transplanted to causal sets
by Markopoulou (2000) and Dable-Heath–Fewster–Rejzner–Woods (2020); the Law's
amplitude-plus-invariance is Sorkin's quantum measure theory (1994) with
Rideout–Sorkin discrete general covariance; the effect-menu clause is Busch
(1999). And the positivity clause is not merely similar to the Sorkin–Johnston
state — **it is its definition**, `W = Pos(iΔ)`.

Which means my round-three "rescue" was circular: I verified that SJ satisfies
the SJ condition. The probe confirmed my code implements the prescription, not
that the axiom has content. Three further defects I had not recorded: SJ is
quasi-free, so two-point positivity is state positivity only for **free fields**;
SJ is **not Hadamard** in general (Fewster–Verch), so there is no renormalised
stress tensor and nothing to couple to gravity; and SJ **fails local
covariance** — the SJ state of a subregion is not the restriction of the larger
one — which directly contradicts my own isotony axiom.

## 3. What survived

The panel was asked to be fair, and several things were credited by more than one
reviewer.

- **The critique of the existing four axioms.** The referee singled out the
  additivity result — that `I(C) = Σ I({r})` has no two-record term, so distance,
  adjacency, Wilson loops and Bell correlators are all unreadable — as "correct
  and genuinely damaging." The Hammersley–Clifford argument (a non-negative
  nearest-neighbour conditional specification is a Gibbs measure, hence cannot
  interfere) was called "the best reasoning in the document."
- **The `M_2(C)`/Gleason observation.** That the existing foundation sits at the
  one dimension where Gleason gives nothing, and that the Busch effect-menu
  repair fixes it *independently of any substrate change*, was credited as
  correct and separable. The referee would accept it as a short technical note.
- **Amplitude rather than probability** as a substrate primitive: credited as a
  genuine withdrawal of an assumption, not an addition.
- **The direction of the substrate change** — causal order over cubic lattice —
  credited by all six as the right move for the right reason, and mainstream
  rather than idiosyncratic. What is broken is my axiomatisation of it, not the
  instinct.

## 4. Decision

**1. Withdraw the proposed axiom set.** Six independent FATAL verdicts, at least
four independently sufficient defects, and the no-imports claim — its entire
design principle — refuted by §2.2. It should not be repaired clause by clause;
the panel's objections are structural, and three of them (classical model,
fixed background, BHS locality) go to the shape of the thing rather than its
wording.

**2. Do not propose a substrate change.** If this programme wants a causal
substrate, the correct move is to adopt causal set theory *as it exists* — with
number–volume correspondence, the sprinkling measure, an action, and a path-sum —
and cite it. Not to re-derive a broken subset of it under new labels. The draft
kept causal set theory's difficulties and discarded its two falsifiable
commitments.

**3. Keep exactly one actionable item.** The effect-menu/Born finding is correct,
separable, and independent of everything withdrawn here. But it must be restated
in **menu-relative (contextual)** form: the universally quantified version is
inconsistent (§2.3). Stated contextually, it says that if the outcome menu is an
effect partition rather than a projection partition, the Born trace form is
forced at dimension two where Gleason gives nothing. That is a real result about
the *existing* Record axiom's readout clause and needs no new substrate.

**4. The deliverable of this line of work is the critique, not the replacement.**
The axioms-only critical review survived adversarial attack and is credited by
the panel. The replacement did not survive first contact with independent review.

**5. Correct the record.** The chirality claim (§2.6) is withdrawn as
mis-attributed; the "net reduction" claim (§2.7) is withdrawn as an accounting
artifact; the round-three positivity rescue (§2.8) is downgraded from a result to
a verification that the code implements a known prescription.

## 5. Method note

The panel was run blind to my conclusions, with six distinct lenses, and each
reviewer was told that finding nothing wrong would be a failed review. That
framing biases toward finding fault, so unanimity is weaker evidence than it
looks — but the objections are specific, theorem-backed, and mutually
independent, and five of six checkable ones were confirmed by my own runners
rather than accepted on authority. The sixth (rigidity) I could not reproduce and
have reported as unconfirmed.

The reviewers also found things my own adversarial pass had missed entirely,
including the objection that kills the design principle (§2.2) and the one that
inverts my flagship result (§2.6). Self-review caught real errors in this line of
work, but it did not catch these; independent review did.

**Runners for the verification pass:**
`scripts/probe_axiom_reset_panel_objections_2026_08_09.py` and
`scripts/probe_axiom_reset_chirality_reattribution_2026_08_09.py`.
