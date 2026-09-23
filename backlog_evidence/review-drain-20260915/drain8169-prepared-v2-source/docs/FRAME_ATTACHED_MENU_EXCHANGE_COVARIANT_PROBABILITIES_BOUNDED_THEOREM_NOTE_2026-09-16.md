---
claim_id: frame_attached_menu_exchange_covariant_probabilities_bounded_theorem_note_2026-09-16
claim_type: bounded_theorem
claim_scope: "Conditional normalized probabilities on a supplied four-point sphere menu, under independent internal rotations and exchangeable cubic slots; exact Gibbs, linear and normalized-overlap identities."
upstream_dependencies: [minimal_axioms, possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14]
runner: scripts/frame_attached_menu_exchange_probabilities_2026_09_16.py
---

# Exchange-covariant probabilities on a frame-attached four-point menu

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Result and supplied premises

For noncollinear unit vectors q,q' and t=q·q', the allowed menu is
S(q,q')={q,q',-q,-q'}. For a fixed two-slot occupancy stratum, independent
internal SO(3) covariance together with exchange of the two occupied cubic
slots gives masses (α(t),α(t),γ(t),γ(t)), where α,γ≥0 and 2α+2γ=1.
The menu has four points; the probability support has four only if both
α and γ are positive. Boundary choices have two nonzero atoms.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the finite
support meaning: nonzero-probability possibilities. It does not select the
sphere, covariance action, menu, weights, formation order or stochastic
product model used here. The [conditional covariance parent](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md)
supplies the direct product of proper cubic slot permutations and independent
internal SO(3), as a mathematical representation. This note works in that
supplied representation, not every interpretation of the full M_2(C) domain.
No registered primitive supplies these probability choices.

## 1. Menu covariance and the one-record boundary

For every rotation R, S(Rq,Rq')=R S(q,q'). The four points are distinct
exactly when |t|<1. If q'=q or q'=-q, the set collapses to {q,-q}; the
four-distinct formulas below are stated only on -1<t<1.

For a single record q, a finite SO(2)-invariant probability support lies
inside {q,-q}. Indeed, rotations fixing q sweep every other sphere point
through an infinite circle. A finite invariant support cannot contain such
an orbit. Conversely a δ_q+(1-a)δ_-q is covariant for every a∈[0,1]. Its
support is a singleton at a=0 or a=1, and the pair only for 0<a<1.
This is a complete finite-support statement; it does not require both
antipodes to have nonzero mass.

## 2. Ordered covariance versus occupied-slot exchange

For an ordered noncollinear pair, the internal SO(3) stabilizer is trivial:
a rotation fixing both vectors fixes their cross product and therefore an
oriented basis. Two ordered pairs with the same t are related by a unique
proper rotation, obtained by matching their oriented orthonormal frames.
Thus internal covariance alone permits any four nonnegative functions
w_1(t),...,w_4(t) summing to one, attached respectively to q,q',-q,-q'.
For example (1/2,1/4,1/8,1/8) defines such an internally covariant law.
It is not symmetric under exchanging the two records.

Now include the two occupied spatial slots in the input. For opposite
slots (+x,-x), rotation by π about y exchanges them. For adjacent slots
(+x,+y), rotation by π about the x+y axis exchanges them. These are proper
cubic rotations; every two-slot pair is cubic-equivalent to one of these
cases. Opposite and adjacent occupancy strata are distinct and may have
different functions α and γ. No equality across these strata is asserted.
There is no external slot label distinguishing the two occupied positions.

The internal bisector rotation B, of angle π about (q+q')/|q+q'|, exchanges
q and q'. It does NOT stabilize the ordered record pair by itself.
Combine it with the independent cubic slot exchange: each original slot
then receives its original record, so the complete input is fixed. The
output transforms by B, forcing the q and q' masses to agree and likewise
the -q and -q' masses. This proves necessity of (α,α,γ,γ).
Conversely, these equalities, dependence only on t within the occupancy
stratum, and normalization give covariance under all the declared actions.
Equivalently this is the internally covariant classification of an unordered
record pair. A π rotation about q at t=0 relates the different inputs
(q,q') and (q,-q'); it does not force α(0)=γ(0).

## 3. Pair-Gibbs and the full valid linear parametrization

For finite real β, the supplied pair-Gibbs formula on S is

    p(s)=exp[β s·(q+q')]/[2exp(β(1+t))+2exp(-β(1+t))],
    α(t)/γ(t)=exp[2β(1+t)].

At t=0 and B=exp(2β)=2, α=1/3 and γ=1/6; B=1 gives α=γ=1/4.
The runner's rational B formula is explicitly restricted to t=0. At finite
β all four masses are positive. At fixed -1<t<1, β→+∞ or -∞ gives the
uniform distribution on the two copy or two flip atoms, respectively.
These are not deterministic single-record choices.

A general member of the exchange family has the equivalent form

    p(s)=[1+λ(t) s·(q+q')]/4,
    α(t)=[1+λ(t)(1+t)]/4, γ(t)=[1-λ(t)(1+t)]/4,
    λ(t)=[4α(t)-1]/(1+t), |λ(t)|(1+t)≤1, -1<t<1.

Antipodal cancellation makes the four weights sum to one. The displayed
inequality is exactly their nonnegativity condition. This is a function
λ(t), potentially different in the two occupancy strata; a fixed constant
λ is only a subfamily on a domain where its bound holds. For a constant
valid on all -1<t<1, |λ|≤1/2 suffices and is necessary. At t=0, λ=0 is
uniform, while λ=±1 gives the two-copy or two-flip boundary law. At t=3/5,
λ=1 would give γ=-3/20 and is excluded. The parameterization retains all
zero-mass boundary cases rather than silently assuming four-point support.

## 4. Raw overlap and normalized menu identities

For any unit reference a, antipodal cancellation gives

    sum_(s in S) (1+s·a)/2=2.

For a=q the raw weights in menu order are

    (1,(1+t)/2,0,(1-t)/2).

They are raw overlap values, not normalized four-menu probabilities. After
dividing by two they define the normalized internally covariant law

    (1/2,(1+t)/4,0,(1-t)/4).

It depends on q' through both its atom locations and t. No violation of the
Admissibility variation sentence follows from the absence of q' as a literal
symbol in the overlap formula. Under the separately imposed occupied-slot
exchange this normalized law generally differs from its swapped-input law;
it is an ordered-reference comparison, not an exchange-family member.
On {q,-q} the original two-outcome law is (1,0).

With a=(q+q')/sqrt(2+2t), the raw four-menu sum is again two. Dividing by
two gives the symmetric linear family with λ(t)=1/sqrt(2+2t), whose bound
is sqrt((1+t)/2)≤1. This is a normalized four-menu comparison, not a
claim that a physical Born rule or a replacement Hamiltonian was selected.

## 5. Scope, preserved process argument and evidence

The complete corrected endpoint-event argument for the supplied three-site
sequential process is preserved readably in
`work_history/repo/review_feedback/pr8169-evidence/DEFERRED_CORRECTED_ENDPOINT_PROOF.md`.
It distinguishes actual joint endpoint laws using |L·R|<1, rather than
conditional menus at an endpoint profile unreachable in chain order. The
valid conditional argument is preserved as deferred scientific source; no universal negative
process conclusion is asserted as part of this live bounded row. Formal
negative certification is not supplied by changing its label. The exact
original erroneous argument is separately retained, never overwritten.

The current supplied-record/common-kernel note is relevant comparison
context, not a parent of the menu theorem:
`SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md`.
Its common-kernel and all-order hypotheses remain conditional. No conclusion
about physical formation or all framework laws is imported.

Primary runner: `scripts/frame_attached_menu_exchange_probabilities_2026_09_16.py`.
Exact rational finite controls cover the reference pair, all 24 proper cubic
rotations, both occupied-slot exchange strata, support boundaries, parameter
bounds, normalized overlaps and a finite endpoint-event analogue. They are
not numerical execution of Haar almost-sure or infinite-system statements.
TOTAL counts actual check calls, including explicitly identified input checks.
The original 120-second timeout is retained; a 256 MiB external process-tree
cap is proposed for small exact rational arrays and standard-library overhead.
JSON diagnostics go to `logs/runner-cache/`. No capture has yet been made.

[Exact eight-path original recovery](work_history/repo/review_feedback/pr8169-evidence/README.md)
preserves original modes, blobs, hashes, the 21-check historical cache, all
original route text and the topology manifest as history only. The original
branch remains a recovery handle for deferred negative certification. Reopen
active promotion only after an honestly complete negative packet and original
reviewer confirmation; the valid supplied-process proof is not thereby
rejected as false or unproved.

## No-Go Discipline Gate

N1: The four actual original routes are preserved with corrected dispositions
in the deferred proof. No fifth route or formal negative PASS is invented.
N2: The supplied covariance, finite-support and product-process assumptions
are not declared independent walls; no nonimplication witnesses were proved.
N3: Slot exchange, nonnegative weights, unordered/ordered inputs, fixed
occupancy stratum and independent Haar roots are explicit where used.
N4: The covariance parent supplies an action, not weights or physical
formation. The common-kernel result is context only; no open sibling is an
authority or a required runner string.
N5: Five stdout lines name finite element/site/mode/block checks and the
unexecuted lattice-wide class. A finite six-axis control is labelled as such.
N6: No primitive, reading, menu, weighting, physical order or Gibbs rule is
selected by these conditional identities.
N7: Ordered unequal weights, singleton support and direction-sensitive
process hypotheses are substantive alternative inputs; the argument must
retain its precise exchange and sequential assumptions.
N8: The read covariance parent distinguishes supplied actions from physical
selection; the current common-kernel theorem distinguishes joint equality
from null-profile cancellation. These scope corrections are retained.
