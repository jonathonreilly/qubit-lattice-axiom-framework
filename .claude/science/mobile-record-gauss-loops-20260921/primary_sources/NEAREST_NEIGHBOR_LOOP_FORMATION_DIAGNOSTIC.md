# The constant-rate loop birth has a formation-locality gap

2026-09-21. Primary exact diagnostic. This examines the new thirteen-state
construction against the current Admissibility wording; it does not alter
the loop, transport or equilibrium identities already checked.

The loop construction preserves permanent labels, single-site capacity and
both exact Gauss constraints. Those facts do not establish the full set of
framework axioms. In particular, identifying its Poisson birth generator
with the complete forming-record probability law exposes a nearest-neighbor
odds problem. The following pair of source-free backgrounds proves it.

## 1. Compute the actual conditional birth law

Write v(y)=1 when y is vacant. Each allowed four-record template forms at
the same microscopic rate beta/N. Conditional on a birth at vacant x,
the rate for either sign of axis i, in either species, is

    h_i(x)=(beta/N) sum_(j!=i) sum_(sigma=+/-1)
       v(x+2sigma e_j) v(x+sigma e_j+e_i) v(x+sigma e_j-e_i).   (1)

These are precisely the four templates placing that signed label at x.
The two circulations give the same vacancy conditions. Species changes
also leave those conditions unchanged. Therefore, when a birth at x is
possible, its conditional probability for any particular label of axis i is

    p_(species,+/-i)(x)=h_i(x)/[4 sum_j h_j(x)].               (2)

The formula probes record sites at distance two from x. Such dependence
could still cancel after normalization, so the two backgrounds below test
the normalized law, not just an unnormalized rate.

## 2. Equal nearest-neighbor conditions, different forming-label odds

Take x=0 on a torus N>=7. Background A is empty. Background B contains
one A-species loop in the yz plane centered at (2,0,1), namely

    (2,0,0): +e_y,    (2,1,1): +e_z,
    (2,0,2): -e_y,    (2,-1,1): -e_z.

Background B is exactly Gauss-free and is reachable by one permitted birth
from empty. At x and all its six nearest neighbors
both backgrounds are vacant. Only the first listed record intersects any
candidate loop birth through x: it is the blocker at 2e_x. Consequently

    A: (h_x,h_y,h_z)=(4,4,4) beta/N,
    B: (h_x,h_y,h_z)=(4,3,3) beta/N.                         (3)

In A all twelve label probabilities equal 1/12. In B a particular signed
x label in either species has probability 1/10, while a signed y or z
label has probability 3/40. The nearest-neighbor record conditions are
identical, but the actual conditional formation law differs.

The Admissibility axiom says that the distribution at a site is determined
by its nearest-neighbor conditions. Its current reading concerns which
possibility a forming record locks, conditional on formation there. Under
that identification, the constant-rate loop birth is not a realization of
that requirement. Calling the remote factor only a formation-site rate
does not fix it: a common positive scalar multiplies every h_i and cancels
from (2), leaving the unequal probabilities.

## 3. Scope and constructive next obligations

This is a counterexample to one fully specified formation kernel. It is
not a proof that exact Gauss constraints and nearest-neighbor formation are
incompatible in general. Its conservative moves and constrained invariant
ensembles are unaffected. The successful departure/reformation history is
still a legal history of that supplied process, but the process must not
be advertised as satisfying all the minimal axioms.

A repair must specify a joint collective birth law whose single-site
conditional probabilities obey the same nearest-neighbor rule at every
background where formation occurs. Possible directions include compensated
template rates, more event types, a different microscopic Gauss encoding,
or a model with explicit charge sources rather than D E=D B=0 everywhere.
None has been supplied or ruled out by this diagnostic. A change in the
Admissibility axiom is not assumed or requested.

There is a useful geometric restriction on one tempting repair. A finite
nonzero divergence-free axis field on Z^3 supported in a fixed finite set S
cannot assign every axis at every occupied site with positive probability:
at a site with maximal first coordinate, a nonzero first component would
produce a charge one step beyond that maximal plane with no compensating
record. Hence that component is zero at every such boundary site. A fixed
finite birth footprint with a full isotropic marginal at each of its sites
is impossible under this particular source-free encoding. Randomizing the
footprint may avoid this restriction; the constant-rate version shows why
vacancy conditioning then needs a separate calculation.

`loop_birth_locality_check.py` independently enumerates every template
containing x, checks both backgrounds' exact divergence and nearest-neighbor
identity, and compares the conditional rational probabilities. Its finite
checks supplement the explicit calculation (1)-(3). The current four-axiom
source is `docs/MINIMAL_AXIOMS_2026-06-29.md`, SHA-256
93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.
