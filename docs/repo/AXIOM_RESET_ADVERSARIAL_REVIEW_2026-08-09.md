# Adversarial Review Of The Axiom Reset Work, And Decided Next Steps

**Date:** 2026-08-09
**Type:** meta
**Document class:** F — orientation memo. This memo carries
**no premise or interpretive weight**. It is citable for orientation and scope
discipline only, never as a premise, and it sets, predicts, and requests no
audit status.

**Subject:** an adversarial pass over
[`AXIOM_FOUNDATION_CRITICAL_REVIEW_2026-08-09.md`](AXIOM_FOUNDATION_CRITICAL_REVIEW_2026-08-09.md),
[`AXIOM_RESET_PROPOSAL_2026-08-09.md`](../AXIOM_RESET_PROPOSAL_2026-08-09.md),
and [`AXIOM_RESET_PROBE_RESULTS_2026-08-09.md`](AXIOM_RESET_PROBE_RESULTS_2026-08-09.md),
followed by the resulting decision.

---

## 1. Method and headline

Every substantive claim made in this line of work was treated as a target: for
each, what would have to be true for it to be wrong, and can that be
constructed? Seven claims were attacked. **Four survive intact, two were
overstated and are corrected below, and one is refuted — and the refuted one is
the headline negative from round two.**

> **The main correction: the positivity failure was my error, not the
> substrate's.** The drafted Law axiom asked for "positive under order
> reversal." Reflection positivity is a *Euclidean* construction whose purpose
> is to Wick-rotate a Euclidean measure into a Lorentzian Hilbert space. A
> causal set is intrinsically Lorentzian, with no Euclidean section and no Wick
> rotation, so the clause imported a category error. The Lorentzian condition
> for obtaining a Hilbert space is **Wightman positivity**, and the
> Sorkin-Johnston construction delivers it from the causal order alone.
> It succeeds on exactly the sprinkled causal sets where reflection positivity
> failed.

Consequently **the "Lorentz invariance or a Hilbert space, not both" tension
reported in the previous results note does not exist.** It was an artifact of
testing a clause that should never have been drafted that way.

## 2. Claims attacked, and what happened

### 2.1 SURVIVES — additivity forbids cross-record dependence

The review's §3.1 argued that no readout can see geometry, via additivity plus
content-determination plus the transitivity of lattice translations.

**Attack.** The transitivity step is the weak link. It requires reading
"no site is privileged" as a constraint on *readouts*, but that sentence is
about sites, and readouts are not obviously laws in the Qualification's sense.
If a readout may depend on the absolute site, `I({r}) = f(x, p)`, then readouts
*can* vary with position and the permutation-invariance conclusion fails.

**Outcome: the conclusion survives, but the argument must be restated in a form
that does not need the disputed step.** Additivity alone gives

```text
I(C) = Σ_{r ∈ C} I({r}),
```

so a readout has **no two-record term at all**. Distance, adjacency, angle, and
correlation are irreducibly two-body quantities. Therefore no readout can depend
on any relation between two records, whether or not `f` depends on the site. The
robust statement is:

> Additivity forbids cross-record dependence, so relational geometry is
> unreadable. Whether *absolute* position is also unreadable depends on the
> disputed reading; relational structure is unreadable either way.

This is weaker than what the review asserted and stronger than what the review
needed. The Wilson-loop, Bell-correlator and correlation-function consequences
all follow from the robust form.

### 2.2 CORRECTED — the scope of the additivity clause is genuinely ambiguous

**Attack.** The review treats "scalar readout `I` is additive" as constraining
*every* observable. It can equally be read as naming *one particular* additive
functional — a total charge, say — and saying nothing about other observables.
Under that reading §3.1 and §3.2 constrain only `I`, not the theory.

**Outcome: the attack lands, and the review should present a dilemma rather than
assert one reading.** Both horns are bad for the foundation, but differently:

- if additivity constrains all readouts, the observable class is crippled
  (the review's original charge);
- if it names one functional, then the axiom set specifies almost nothing about
  observables at all, and the observable structure is simply absent.

The review's §3.2 conclusion — that the theory's own targets, being ratios, are
not readouts — holds only under the first horn. **This is a real weakening of a
claim the review stated flatly**, and it is corrected in the review text.

### 2.3 CORRECTED — probabilities are idle, but not for the reason given

**Attack.** The review's §3.3 says the distribution's values "appear in no
readout." But an additive readout over many records is sensitive to the
empirical frequency of locked possibilities: `I(C) = Σ f(p_r) ≈ N·E[f]`. So the
values *could* show up statistically.

**Outcome: the conclusion survives with a corrected mechanism.** The gap is not
that readouts are blind to frequencies. It is that **nothing in the axioms
connects the distribution's values to locking frequency at all** — Record
requires only that a locked possibility be *admissible*, which the memo's own
reading note defines as lying in the distribution's *support*. Support does
work; values do not. A frequency principle would be needed and is absent.

### 2.4 SURVIVES — "Records form" is not a law by the memo's own test

**Attack.** Perhaps "Records form" is intended as an existence assertion rather
than a law, so measuring it against the Qualification's definition of a law is
unfair.

**Outcome: survives, and the attack sharpens it.** If it is not a law, then the
axiom set's only clause about anything *happening* is ungoverned, and the
Qualification's no-privileging discipline binds only the static furniture. That
is the same finding stated more precisely, not a rebuttal.

### 2.5 SURVIVES, SCOPE NARROWED — the chirality probe

**Attack.** The probe demonstrates that the overlap operator escapes doubling
and is exponentially local rather than compactly supported. But that shows the
axiom change *removes an obstruction*; it does not show the change *delivers*
chiral fermions. It is also free-field and two-dimensional, and overlap locality
degrades in strong gauge backgrounds.

**Outcome: the attack lands on the wording, not the result.** The correct claim
is "relaxing nearest-neighbour to local removes the Nielsen-Ninomiya
hypothesis," which the measurements establish cleanly. "Buys chirality"
overstates it. Corrected wording throughout.

### 2.6 REFUTED IN PART — the Born payoff is not secured by the drafted text

**Attack.** The Born probe confirms that additivity over a full *effect* menu
forces the trace form at dimension two. But the drafted Actuality axiom says an
outcome is "one of the mutually exclusive alternatives admitted by the
observable algebra of its region" — which reads as a *projection* menu, exactly
the case the probe shows is insufficient. The proposal therefore recommends a
repair that its own axiom text does not implement.

**Outcome: the attack fully lands. This is a defect in the drafted axioms, not
in the probe.** Fixed in §3 below by an explicit effect-menu eligibility
sentence.

### 2.7 REFUTED — the positivity negative, and with it the headline tension

**Attack.** Two lines of objection, and both hold.

*First, the drafted clause is a category error.* Reflection positivity is the
Osterwalder-Schrader device for turning a Euclidean measure into a Lorentzian
Hilbert space. A causal set is Lorentzian to begin with. Asking for reflection
positivity on it is asking a Lorentzian object to satisfy a Euclidean
requirement that has no motivation there.

*Second, the Benincasa-Dowker test attacked a strawman.* The BD operator is
**retarded**. Symmetrising it — which round two did, to build a Gaussian — is
not how causal-set field theory is done. The community's construction is
Sorkin-Johnston, built from the Pauli-Jordan function, and it was never tested.

**Outcome: refuted, decisively.** The Sorkin-Johnston construction was
implemented from the causal order alone and every property verified rather than
assumed: the Pauli-Jordan operator is antisymmetric to `0.0e+00`; `iΔ` is
Hermitian with spectrum symmetric about zero to `1.1e-14`; the SJ two-point
function is positive-semidefinite (`min eig = -2.5e-15`, machine zero); and it
reproduces the commutator, `W - conj(W) = iΔ`, to `3.3e-15`.

On sprinkled causal sets — the exact substrates where reflection positivity
failed — it succeeds at every size tested:

| N | min eig(W) | commutator defect | GNS rank |
|---|---|---|---|
| 20 | `-3.3e-16` | `2.6e-15` | 9 |
| 40 | `-1.6e-15` | `2.1e-15` | 16 |
| 80 | `-2.9e-15` | `1.8e-15` | 38 |
| 140 | `-1.4e-14` | `1.3e-14` | 67 |

The resulting state is order-invariant (spectrum unchanged under relabelling, to
`1.4e-14`) and substrate-sensitive (two independent sprinklings differ by
`0.63`), so it is neither degenerate nor a constant.

**A Hilbert space is therefore constructible on a frame-free substrate.** The
round-two conclusion that the reset must choose between Lorentz invariance and a
reconstruction theorem is **withdrawn.**

## 3. The revised axiom text

Two clauses change. Both changes are corrections to drafting errors that the
probes exposed.

### Law — positivity clause replaced

Was: *"The assignment is positive under order reversal."*

Now:

> The assignment induces a state of positive type on the observable algebra: the
> two-point function is positive-semidefinite, and its antisymmetric part is the
> commutator supplied by the order.

This is a **re-typing, not an addition** — one positivity condition replaces
another. It is strictly better on three counts. It is intrinsic to the
Lorentzian substrate rather than imported from a Euclidean formulation it does
not have. It is stated on the observable algebra, so it composes with the
Observables axiom instead of standing apart from it. And it is now demonstrated
constructible, which the clause it replaces was not.

### Actuality — effect-menu eligibility made explicit

Was: *"An outcome is exactly one of the mutually exclusive alternatives admitted
by the observable algebra of its region."*

Now:

> An outcome is exactly one of the mutually exclusive alternatives admitted by
> the observable algebra of its region. Every finite partition of the region's
> unit into positive observables is such a menu.

The added sentence is what secures the Born form. It names no operator, basis or
value, and it is what the deleted Record additivity clause was reaching for and
failing to reach. Counting honestly: the reset deletes three readout clauses and
adds this one, so the supplied-structure arithmetic moves from 12 clauses to 13,
against 15 clauses plus 3 primitives plus 1 unstated on the current surface.
**Still a reduction, and the earlier figure is corrected from 13 to 14 including
the retained scale primitive.**

## 4. What the adversarial pass did not shake

- **Model existence.** Obligations 1–3 remain discharged; the kinematic caveat
  was already recorded.
- **The Nielsen-Ninomiya removal.** Measurements stand; only the wording of the
  claim was overstated.
- **The Gleason/Busch results.** Solution-space dimensions were computed from
  null spaces and are exact; the only caveat is that the dimension-two search
  ran over polynomials to degree 3 rather than all functions.
- **The critical review's core diagnosis.** Additivity cripples the observable
  class, the substrate carries a preferred frame, `M_2(C)` is too small by
  direct algebra, and the kernel is undetermined. None of these was touched.

## 5. Decided next steps

Ordered, with the reason each is placed where it is.

**1. Adopt the three cheap repairs into the proposal as the recommended action,
unchanged.** Exponential locality, effect-menu eligibility, and naming the
kernel. All three are confirmed by probe, none needs the substrate change, and
each removes a named blocker. *This is the only item that is ready for an owner
decision.*

**2. Re-probe the substrate change against the corrected clause.** Everything
that was concluded about the substrate rested on the wrong positivity condition.
The specific questions now open: does the SJ state on a sprinkled causal set
support a *non-trivial algebra of local observables* satisfying the drafted
Observables axiom, and does its GNS representation carry a dynamics? GNS rank
scaling as roughly `N/2` is a promising sign and is not a substitute for the
check.

**3. Test Lorentz invariance directly rather than asserting it.** The claim that
a sprinkling is frame-free has been used throughout and never measured. The
sharp test is that the link-velocity distribution of a sprinkled causal set is
boost-covariant while a regular one takes finitely many values. Until this is
run, the central argument for the substrate change is unverified.

**4. Retire the reflection-positivity line of work.** Rounds two and three of the
positivity probes tested a clause that no longer exists. The runners stay for
provenance; their conclusions do not carry forward.

**5. Leave the numerical lanes alone.** Generation count, gauge group, and every
mass and mixing angle remain downstream of the undetermined amplitude
assignment. No axiom reset reaches them, and the probes changed nothing here.

**Not recommended:** proposing the substrate change for owner decision. Step 2
and step 3 must land first. The reset's cheap repairs are ready; its expensive
one is not, and the reason it is not has changed — it is no longer a demonstrated
obstruction, it is an unfinished demonstration.

## 6. Standing limits

The Sorkin-Johnston result is a construction on finite causal sets in two
dimensions with the massless retarded propagator `G_R = C/2`. It has not been
checked in higher dimensions, with mass, or against the continuum limit, and the
SJ prescription itself is known in the literature to have subtleties in
particular spacetimes. Positive-semidefiniteness and the commutator identity
hold by construction once the prescription is adopted; what the probe verifies
is that the construction is well posed and non-degenerate on these substrates,
not that it is the physically correct state.
