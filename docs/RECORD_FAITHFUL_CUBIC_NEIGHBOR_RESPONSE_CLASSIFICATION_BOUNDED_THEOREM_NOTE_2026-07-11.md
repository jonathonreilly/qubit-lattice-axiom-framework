---
claim_id: record_faithful_cubic_neighbor_response_classification_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exact proper-cubic intertwiner classification for real-linear maps from six directed neighbor sensitivities to the scalar-plus-vector decomposition of Herm(2), plus a conditional scalar-branch exclusion when nontrivial rank-one spectral record-faithfulness is separately supplied."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_faithful_cubic_neighbor_response_2026_07_11.py
---

# Cubic Neighbor-Response Classification And The Record-Faithfulness Residual

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source note sets no audit
status and proposes no axiom or primitive.

Primary runner:
[`scripts/record_faithful_cubic_neighbor_response_2026_07_11.py`](../scripts/record_faithful_cubic_neighbor_response_2026_07_11.py)

Cached output:
[`logs/runner-cache/record_faithful_cubic_neighbor_response_2026_07_11.txt`](../logs/runner-cache/record_faithful_cubic_neighbor_response_2026_07_11.txt)

## Result

Let the six real input coordinates `c_d`, with
`d in {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}`, transform by the directed-neighbor
permutation representation of the 24-element proper cubic group. Let the
output be

```text
Herm(2) = R I direct-sum span_R{Gamma_1,Gamma_2,Gamma_3},
```

where the scalar is invariant and the three traceless coordinates transform
by the ordinary vector representation.

The vector space of site-independent real-linear equivariant maps from the six
neighbor coordinates to `Herm(2)` has dimension exactly two. Every such map is

```text
F(c) = a [sum_d c_d] I
     + b sum_mu (c_(+mu) - c_(-mu)) Gamma_mu.                 (1)
```

The runner constructs all 24 proper rotations, forms the complete exact
integer equivariance system, and obtains rank `22` on `24` map coefficients,
hence nullity `2`. The displayed scalar-sum and directed-vector-difference maps
are independent null vectors and therefore span the full intertwiner space.
The two even axis-anisotropy modes are annihilated.

## Conditional spectral-faithfulness corollary

Supply this additional bridge:

> For at least one nontrivially varying neighbor condition, the available
> rank-one record possibilities are the nontrivial spectral projectors of the
> realized response `F(c)`; no independent response sector is appended that
> has no effect on formation support or weights.

Then `b != 0`. If `b=0`, equation (1) is proportional to `I` for every input
and has only the full two-dimensional eigenspace, never a nontrivial rank-one
spectral projector. A nonzero vector response on `M_2(C)` has two simple
rank-one spectral projectors. Within the separately supplied standard
spatial-vector action on traceless `Herm(2)`, the trace metric is invariant;
after one common normalization its coefficients may be chosen to obey

```text
{Gamma_mu, Gamma_nu} = 2 delta_(mu nu) I.                    (2)
```

Turning this response into a Hermitian kinetic symbol requires a second,
independent bridge. Supply the oriented-link realization

```text
A_(+mu) = a I - i b Gamma_mu,
A_(-mu) = A_(+mu)^dagger = a I + i b Gamma_mu.               (3)
```

The runner checks the adjoint relation and reconstructs the corresponding
nearest-neighbor Hermitian symbol

```text
H(k) = [m + 2 a sum_mu cos(k_mu)] I
     + 2 b sum_mu Gamma_mu sin(k_mu).                        (4)
```

The odd part therefore satisfies

```text
H_D(k)^2 = 4 b^2 [sum_mu sin^2(k_mu)] I.                     (5)
```

Thus spectral faithfulness forces a nonzero odd Clifford response component
on this separately supplied oriented-link Hermitian symbol surface. Only with
that response-to-symbol realization does it have a first-order Dirac infrared
reading. The cubic graph Laplacian is exactly the scalar-even point
`(m,a,b)=(6,-1,0)` in (4), so it cannot be the complete response under both
supplied bridges. It may still occur as an `O(k^2)` scalar correction alongside
a nonzero vector term; this theorem does not forbid Wilson-like corrections.

## Why this moves the open lane

The July-10 countermodel demonstrates that locality, proper-cubic symmetry,
common qubit-frame invariance, Hermiticity, and nontriviality do not select a
first-order carrier. This classification identifies the exact missing
discriminator on the linear directed-neighbor surface:

```text
scalar even response  versus  spatial-vector odd response.
```

It also shows why adding more undirected symmetry is not promising. The scalar
channel is a genuine cubic intertwiner. A selector has to earn a nontrivial
direction-resolving relationship between record formation and the qubit Bloch
vector; symmetry alone cannot supply it.

## Current-surface boundary

The spectral-faithfulness sentence is not a theorem of the four axioms.
Current Admissibility specifies which possibilities are available and says
that they vary with neighbor conditions. It explicitly does not choose a
Hamiltonian, transfer operator, formation rule, probability weight, or kinetic
branch. The July-10 availability rule

```text
S_x(R) = sum_(y~x) rho_y
```

is covariant and variable but uses the spatial-scalar neighbor sum with an
internal `M_2` value; it does not implement the directed spatial-vector
locking of (1). Identifying its availability projectors with coefficients in
a kinetic symbol would add the missing bridge.

The next campaign block must therefore derive or falsify a basis-free
record-formation influence functor. A weak requirement that "the law varies
when Admissibility varies" is insufficient: a covariant scalar function of
the availability projectors multiplying `I-SWAP` remains record-sensitive and
second order. The bridge must exclude every such scalar natural functional,
not only the record-independent July witness.

## Object-separation warning

The theorem classifies a neighbor response. It does not decide whether the
fundamental physical object is a continuous-time Hamiltonian, a strict causal
unitary tick, or a record-forming CP instrument.

Directly requiring one Hamiltonian to preserve every possible rank-one locked
record freezes all nontrivial same-site kinetics: commuting with every
rank-one projector means acting as the identity on that site. In a finite
`blank direct-sum record` space, a unitary that leaves the record subspace
invariant makes it reducing and cannot form a record from the blank subspace.
Thus permanence does not select Dirac; it requires a separate record register,
an instrument/channel, an enlarged dilation, or equivalent extra structure.

## Refutation legs

- **Drop spectral faithfulness:** `b=0` survives and includes the exact cubic
  graph Laplacian.
- **Keep only record dependence:** a scalar state-dependent multiple of
  `I-SWAP` survives.
- **Drop cubic covariance:** independent axis coefficients and anisotropic
  scalar/vector response channels survive.
- **Omit the oriented-link realization:** the real response classifier alone
  does not produce equation (4); directly substituting Fourier characters in
  `c_+-c_-` gives `2 i sin(k)`, so the explicit `-i` in (3) is load-bearing.
- **Treat the response as a strict tick:** equation (4) is a Hermitian symbol,
  not automatically a finite-radius unitary. Exponentiating either its Dirac
  or Laplacian part generally spreads beyond one lattice edge.
- **Demand common `SU(2)` naturality on an undirected two-qubit edge:** the
  commutant is spanned by `I` and `SWAP`; this favors the scalar exchange class
  rather than deriving spatial-to-Bloch locking.

## Negative-claim discipline

The negative content is restricted to the displayed linear response class and
the stated premise-removal legs.

- **N1 alternatives:** undirected symmetry, weak record dependence, direct
  permanence, strict tick, and spectral faithfulness are separated above.
- **N2 wall independence:** cubic covariance classifies the response but does
  not provide faithfulness; faithfulness excludes scalar response only inside
  the supplied scalar-plus-vector representation; the oriented-link map is a
  separate bridge and still does not define a tick, rate, probability rule, or
  continuum limit.
- **N3 hidden walls:** real linearity, directed-neighbor inputs, the vector
  action on traceless `Herm(2)`, and the spectral reading are explicit.
- **N4 residual matching:** the target is the missing
  Admissibility-to-carrier interface exposed by the July-10 countermodel, not
  minus-flux or boundary-holonomy selection.
- **N5 rhetoric:** "exactly two" refers only to the stated intertwiner space;
  "excludes" is conditional on supplied spectral faithfulness.
- **N6 partial closure:** a record-forming instrument classification or a
  faithful scalar countermodel can still settle the bridge in either direction.
- **N7 steelman:** a scalar natural response can affect record rates while a
  separate vector-free exchange block propagates excitations. This would evade
  weak faithfulness and is the required hostile construction for the next
  block.
- **N8 cross-cycle echo:** prior tick and kinetic classifications narrowed
  licensed surfaces but left their realization inputs open. This theorem does
  not re-label those inputs as derived.

## Reproduction

```bash
python3 scripts/record_faithful_cubic_neighbor_response_2026_07_11.py
```

Expected deterministic result:

```text
TOTAL: PASS=23 FAIL=0
```

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  static premise wording and the explicit dynamics boundary.
- [`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`](STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)
  supplies the countermodel target and graph-Laplacian comparison.

Context only: the existing strict-tick, kinetic-isotropy, two-flux-class, and
graded-constraint program notes. None supplies the spectral-faithfulness
bridge used in the conditional corollary.
