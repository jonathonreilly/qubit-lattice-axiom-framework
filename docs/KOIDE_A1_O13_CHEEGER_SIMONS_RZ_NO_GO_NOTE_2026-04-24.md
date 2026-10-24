# Koide A1 — corrected R/Z character and phase checks

**Type:** bounded_theorem
**Date:** 2026-04-24; correction 2026-10-21
**Status:** finite algebraic correction; former general O13 no-go withdrawn
**Primary runner:** `scripts/frontier_koide_a1_cheeger_simons_rz_probe.py`

The legacy filename preserves existing links. This note establishes the
specific group and phase statements below. It neither constructs a physical
Koide phase nor excludes other differential-character constructions.
The earlier source is recoverable at commit
`f24d17d97d372df977476e4a69674577f31af575` under this same path.

## Torsion and degree

If a flat additive character h on homology is evaluated on a class g with
3g=0, then 3h(g)=h(3g)=0 in R/Z. Consequently h(g) is one of
0, 1/3, 2/3 modulo 1. The proposed h(g)=2/9 fails this necessary condition:
3(2/9)=2/3, not 0 modulo 1. Enlarging the coefficient group to R/Z does
not remove the domain relation. This rejects the particular flat order-three
construction; it says nothing comparable about a free cycle or a character
with nonzero curvature.

In the degree convention used by Simons–Sullivan, a degree-k differential
character acts on (k−1)-cycles; its flat subgroup is H^(k−1)(M;R/Z).
A character on one-cycles has degree two in this convention. The former
argument mixed degree conventions and supplied no construction from its
finite eta-like sum to the claimed holonomy. See their definition (1.2)
and character diagram in [Axiomatic Characterization of Ordinary Differential
Cohomology](https://arxiv.org/abs/math/0701077).

The finite sum with omega=(-1+i sqrt(3))/2,

    (1/3) sum[k=1,2] 1/((omega^k−1)(omega^(2k)−1)) = 2/9,

remains an exact algebraic identity. Calling that number a holonomy of the
claimed flat order-three character would require a separate, impossible
identification under the hypotheses above. No spectral eta formula or
physical normalization is established by evaluating this finite sum.

## Quotient phase maps

The map [c] -> exp(2 pi i c) is well-defined on R/Z, since shifting c
by an integer leaves the value unchanged. For the supplied c=2/9 it gives
exp(4 pi i/9). It differs from exp(i 2/9).

Neither exp(i c) nor exp(pi i c) defines a function on the same quotient
R/Z: representatives 0 and 1 have different images. These are not merely
alternative isomorphisms or choices of a radian unit. A real lift or a
different domain would be additional data and would change the problem.

R/Z contains arbitrary real classes, not just rational ones. On a supplied
smooth circle, the flat connection with real coefficient a in A=a dx
(x of period one) has holonomy exp(2 pi i a), with the conventional
normalization of the covariant derivative. In particular the supplied
choice a=1/(9 pi) yields exp(i 2/9). This is a mathematical counterexample
to a universal rational-angle restriction from the character formalism
alone; it is not a framework-derived selection of a or a Koide prediction.

## Withdrawn geometry and execution claims

The old assertion that cyclic coordinate permutation kills all invariant
one-classes of T^3 is false: dx+dy+dz is invariant. The analogous cyclic
sum of two-forms is invariant too. The runner checks the permutation's
fixed space, not the integral cohomology of a singular quotient or an
orbifold. The earlier cohomology table and its claimed lattice
specialization are withdrawn; no replacement quotient table is asserted.

No cellular cocycle, lattice simulation, physical eta-to-holonomy bridge,
or exhaustive search of retained phase sources is performed. The runner
checks exact finite expressions, quotient consistency, and counterexamples.
Its PASS means those predicates hold; FAIL means a check failed, not that
Koide closure was achieved. Previous 49/49 prose assertions and the
O13=TRUE fingerprint are superseded. Downstream uses must preserve this
restricted scope and cannot count this as an additional independent 2/9
source or a general phase no-go.
