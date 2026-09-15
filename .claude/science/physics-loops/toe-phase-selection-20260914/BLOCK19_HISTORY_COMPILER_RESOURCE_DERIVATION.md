# History compilation: a quantitative resource obligation, not an axiom wall

Personal follow-on derivation, 2026-09-15. Private proof candidate and research
checkpoint; no proposed retained status or independent review. The purpose is
to test one possible leap from the campaign's fixed-period spatial compiler
to an indefinitely extended local spacetime history. It is not evidence that
all native realizations must take that form.

## 1. Foundation checked again at the current main revision

At main5deabeb698a27c2c3f68c5df685af2521ef15307, the canonical four-axiom source
is docs/MINIMAL_AXIOMS_2026-06-29.md. Lattice gives Z^3 and NN adjacency.
Qubit gives M_2(C), with eight real coordinates, not a finite classical bit
alphabet. Record gives one permanent Record per site, readable through content.
Admissibility gives a fixed covariant NN conditional probability rule, not a
formation schedule, finite precision bound, or a spacetime event embedding.

The complete registered premise map was reread, as were all three current
primitive declarations. Scale reference supplies units. Kinetic isotropy
supplies c_t=c_s for the emergent regulator's kinetic form, and explicitly
supplies no fourth spatial dimension, dynamics or reachability theorem.
Realized state supplies pointwise evaluation, not a history selection rule.
These are approved premises, not missing inputs or sources of boundedness.
None is enlarged into the extra compiler hypotheses below.

The current Record-first Haar-jump note's Theorem4 is only a finite-graph
capacity statement: at most|V| writes, then termination. Its lines170–255
were reread; the whole note is not claimed reviewed here. The older strict-NN
Gaussian compiler note was searched at its scope and open-gate sections: it
expressly stops before a fixed-density all-cover construction. The present
campaign's periodic compiler concerns a supplied three-dimensional periodic
factor family; its motivating DK fixture has a fixed temporal cover. It does
not supply a uniform compiler for growing four-dimensional histories.

## 2. A precise graph-layout bound

Let B_d(R) be the integer l1 ball of radius R in Z^d. Consider a map f from
a four-dimensional event grid to native sites in Z^3, with two DECLARED
compiler conditions:

 (L) Images of every pair of neighboring event vertices have native
     l1 distance at most C, uniformly in the size of the event grid.
 (K) At most kappa event vertices are represented at the same native site.

The map need not be injective, covariant, linear, or preserve graph distance
from below. Logical edge paths may overlap; only their endpoint distance is
used. Thus any stronger bounded-length NN routing satisfies(L).

Every shortest path from0 to v in B_4(R) stays inside that ball. The triangle
inequality gives f(B_4(R)) subset B_3(f(0),C R). Counting fibers gives

 |B_4(R)| <= kappa |B_3(floor(C R))|.                    (1)

For nonnegative integer R,

 |B_d(R)|=sum_{j=0}^d 2^j binom(d,j) binom(R,j).          (2)

Proof: choose the j nonzero coordinates and signs, then count positive
integer magnitudes whose sum is at most R. After subtracting one in each
coordinate, stars-and-bars gives binom(R,j). This proves(2), including j=0.
Explicitly

 |B_3(R)|=(4R^3+6R^2+8R+3)/3,
 |B_4(R)|=(2R^4+4R^3+10R^2+8R+3)/3.

Thus no fixed finite C,kappa can satisfy(1) at every radius. For a family
of finite maps the necessary resource tradeoff is asymptotically

 kappa_R C_R^3 >= (1/2+o(1)) R,                        (3)

when C_R>=1; the ratio form(1) is the exact finite bound. In particular,
fixed congestion requires C_R growing at least on the order R^(1/3), and
fixed edge dilation requires congestion growing at least linearly in R.
These are necessary bounds, not claimed optimal attainable constructions.

Only future time does not remove the issue. For t>=0, the one-sided event
ball has (|B_4(R)|+|B_3(R)|)/2 points, equivalently sum_(s=0)^R|B_3(s)|.
Its leading term is R^4/3; the corresponding necessary asymptotic bound is
kappa_R C_R^3>=(1/4+o(1))R. The growth-degree mismatch persists.

This simple volume-growth argument is not a claim of new graph mathematics.
Its point is that fixed temporal cover and arbitrary temporal cover are
quantitatively different compiler contracts.

## 3. A finite escape with a cost explicitly exposed

For (x,y,z,t) in {0,...,L-1}^4, the map

 f_L(x,y,z,t)=(x,y,z+L t)

is injective. Spatial-neighbor distances are1; temporal-neighbor distance
is L. It has exactly L^4 image sites and obeys(L) with C=L, not a constant.
This is only an integer layout; it is not a complete NN Gaussian routing,
a full-map covariance construction, or a native formation law. It proves
that the counting bound does not prohibit finite history layouts. It names
the edge-length cost that a fixed-C inference would have concealed.

Another escape is fixed temporal period T. The graph Z^3 times a finite
T-cycle has growth degree3 at large radius. Its internal payload/route budget
may depend on T, consistently with the fixed-period compiler already built.
No bound uniform in unbounded T follows merely by repeating its finite-cell
formula. Readout of just a sparse subset of events changes the source growth
again, and can also avoid(1)'s four-dimensional numerator.

## 4. What regular Record readout could add

Condition(K) is NOT automatic from the algebra M_2(C): a continuum-valued
Record does not have a supplied finite-bit capacity. There is a different,
explicitly regular readout hypothesis under which a similar bound follows.
Suppose one jointly recorded real outcome is read for every v in B_4(R),
from native Records within radius r of f(v). Suppose the combined decoder is
locally Lipschitz in the real matrix entries, on a finite or countable union
of strata, and the joint target outcome law is absolutely continuous with
respect to Lebesgue measure in n=|B_4(R)| dimensions. A nondegenerate finite
Gaussian law is an example of that target condition, not an axiom consequence.

All native sites used lie inside B_3(f(0),CR+r), of size K_R. Record presence
and finite discrete metadata yield a finite/countable union of coordinate
strata of dimension at most8K_R. A locally Lipschitz map from R^m to R^n with
m<n has Lebesgue-null image: partition a bounded source cube intoO(delta^-m)
small cubes; each image has diameterO(delta) and can be covered with total
n-volumeO(delta^(n-m)), tending to zero. Use countably many bounded cubes and
local Lipschitz charts. This proof does not require the input law to have a
density. Its pushforward is still supported on that null image.

Therefore an exactly absolutely continuous n-dimensional output requires

 |B_4(R)| <= 8 |B_3(floor(CR+r))|.                       (4)

If only n_R independent coordinates of the target law have a joint density,
replace the left side by n_R. Thus n_R asymptotic to c R^4 with c>0 still
cannot coexist with uniform C,r and these regularity assumptions. Constant
native tensor/payload overhead changes the factor8, not the growth power.

This does NOT equate a Euclidean path integral with actual jointly readable
Records. In quantum theory not every field value at every time is jointly
measured, and initial data plus a law can specify an evolution with much less
than a separately stored history. An OS Gaussian field is not automatically
the Record map in(4). Before using(4) against a proposed native construction,
the construction's actual simultaneously readable variables and their joint
law have to be identified. No such full native identification is proved here.

## 5. The continuous-alphabet escape must remain visible

A uniform real U in(0,1) has independent fair binary digits away from the null
set of double expansions. Partition those digits into n infinite subsequences.
They define n independent uniform variables. Applying the inverse normal CDF
gives any desired finite vector of independent standard normals, followed by
an invertible linear map for a nonsingular Gaussian covariance. One scalar
Record U I can therefore carry such a Borel-measurable codec at the level of
alphabet and measure theory. Its digit decoder fails the locally Lipschitz
hypothesis. This is a codec, not a covariant NN formation construction or a
claim that its selected probability law is native.

A finite interleaving test verifies bijection of all8-bit seeds with two4-bit
outputs; extending the number of target components consumes more seed bits.
The example prevents a finite-bit capacity assumption from being smuggled
into the M_2(C) possibility domain. Ordinary continuity alone is also not a
sufficient dimension bound: the covering proof explicitly uses Lipschitz
control, and no replacement by unproved regularity is allowed.

## 6. Route accounting and next decisive test

| Attempted route | What the calculation actually establishes |
|---|---|
| Fixed-site permanent-event layout with bounded routing and congestion | Exact bound(1); impossible for arbitrarily large four-dimensional balls |
| Longer paths on finite histories | The explicit injective stacked layout survives with C=L |
| Fixed temporal period | Source growth remains three-dimensional; resource constants may depend on the period |
| Regular finite-radius content decoder for a full-dimensional recorded law | Conditional dimension bound(4), with the readout and joint-law premises explicit |
| Arbitrary measurable encoding in one continuum Record | Binary-digit interleaving evades the regularity hypothesis at codec level |
| Sparse records or state-plus-law evolution | The four-dimensional independently recorded-event target is not established; the counting premise may fail |

These routes are related through their compiler assumptions, not independent
physical walls. The main steelman is that an actual world need not store all
of an auxiliary Euclidean field as one permanent event per regulator vertex.
That objection is correct. The current results do not force an axiom update. Analogous finite-memory
recording models have ordinary storage constraints too; this bound is not
by itself a pathology distinguishing the framework from other local models.
They expose a precise test for a next native compiler: either give uniform
history-to-native resource and readout estimates for its ACTUAL observable
class, or declare which of dilation, spatial footprint, payload resolution,
readout regularity, or event density grows. A codec or an allowed escape is
not a completed native stochastic law.

No public science PR or retained-status request is made for this private
checkpoint. Finite arithmetic checks support the identities and examples;
the arbitrary-radius and measure-dimension statements rely on the proofs.
A wider literature/proof review and an actual native-observable match remain
before treating this as an active model obstruction. No source axiom, approved
primitive or editable prompt has been changed.
