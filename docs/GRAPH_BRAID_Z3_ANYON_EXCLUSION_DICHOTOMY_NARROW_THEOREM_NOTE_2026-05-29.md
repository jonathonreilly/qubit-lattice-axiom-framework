# Graph-Braid Anyon-Exclusion Computed Witness Packet on Z^3 Cubes

**Date:** 2026-05-29
**Scope repair:** 2026-06-06
**Claim type:** bounded_support
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:**
[`scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py`](../scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py)
**Cached runner output:**
[`logs/runner-cache/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.txt`](../logs/runner-cache/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.txt)
(`SCORECARD: PASS=25 FAIL=0`)

## Scope Repair

The original source wording was too broad: it suggested that the packet had
closed the theorem that the two-particle exchange class is the order-2 torsion
generator in `H_1(UD_2)` for every `L >= 3` cubic box and for infinite `Z^3`.
The runner does not prove that quantified bridge. This repaired note is scoped
only to the directly computed graph witnesses and the elementary `Hom(Z_2,U(1))`
phase consequence.

## Repaired Claim

The packet verifies the following bounded witness facts.

1. **Abrams unordered two-particle complexes are built and checked exactly** for
   the finite reference graphs `C_3`, `C_4`, `C_5`, `K_4`, `K_5`, and
   `K_{3,3}`. The runner constructs the cell boundary maps for `UD_2(Gamma)`
   and verifies `d1*d2 = 0`.

2. **Smith normal form gives the displayed witness homology groups**:
   `C_3`, `C_4`, and `C_5` have `H_1 = Z`; planar `K_4` has
   `H_1 = Z^4`; non-planar `K_5` has `H_1 = Z^6 (+) Z_2`; and non-planar
   `K_{3,3}` has `H_1 = Z^4 (+) Z_2`.

3. **Finite `Z^3` cube witnesses are non-planar and 3-connected in the tested
   cases.** Direct graph counts verify that cubic boxes of side `L=3` and
   `L=4` violate the bipartite planar bound `E <= 2V - 4`. Brute-force cut
   checks verify that no one- or two-vertex cut disconnects those boxes, while
   the three neighbors of a corner form an explicit cut. The `2x2x2` cube is
   checked as a finite boundary case that does not trigger this Euler
   obstruction.

4. **Order-2 torsion admits only sign phases.** For any already-established
   order-2 exchange class `t`, any abelian statistics homomorphism
   `phi: H_1 -> U(1)` satisfies `phi(t)^2=1`, so the phase is `+1` or `-1`.
   The runner checks this elementary root-of-unity fact.

These are useful support witnesses for the graph-braid anyon-exclusion route.
They are not a packet-contained proof of the full `Z^3` graph-braid statistics
theorem.

## What This Does Not Claim

- It does not prove that the two-particle exchange class is the `Z_2` torsion
  generator for every `L >= 3` cubic box.
- It does not prove the infinite-lattice `Z^3` statement.
- It does not import Ko-Park or HKRS as retained-grade load-bearing theorem
  authorities inside this packet.
- It does not select boson versus fermion.
- It does not bridge first-quantized graph-braid statistics to the framework's
  second-quantized gauge-coupled matter sector.
- It does not introduce a new axiom, admission, audit result, or status tag.

## Runner Construction

For a finite graph `Gamma`, the runner builds the Abrams discretized unordered
two-particle space `UD_2(Gamma)`:

| dim | cell | condition |
|---|---|---|
| 0 | unordered pair `{u, v}` of vertices | `u != v` |
| 1 | unordered `{w, e}`, `w` a vertex, `e` an edge | `w` not an endpoint of `e` |
| 2 | unordered `{e, f}` of edges | `e` and `f` vertex-disjoint |

With oriented edges `e=(a,b)` and `f=(c,d)`, the boundary maps are

```text
d1 {w, e=(a,b)} = {w,b} - {w,a}
d2 {e=(a,b), f=(c,d)} = {b,f} - {a,f} - {d,e} + {c,e}
```

The runner computes the Smith normal form of `d2` and the rank data from
`d1`, giving the displayed `H_1` witness groups.

## Verification

Run:

```bash
python3 scripts/graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py
```

Expected:

```text
SCORECARD: PASS=25 FAIL=0
VERDICT: bounded witness packet only. Exact UD_2 homology checks show Z_2
torsion for K_5 and K_{3,3}; L=3,4 cubic boxes violate the bipartite
planar bound and are 3-connected graph witnesses; Hom(Z_2,U(1)) gives
sign phases for an
already-established order-2 class. This runner does not prove the quantified
all-L or infinite-Z^3 exchange-generator theorem.
```

## External Context

- J. H. Kim, K. H. Ko, H. W. Park, "Graph braid groups and right-angled
  Artin groups," Trans. Amer. Math. Soc. **364** (2012) 309-360.
- D. Farley, L. Sabalka, "Discrete Morse theory and graph braid groups,"
  Algebr. Geom. Topol. **5** (2005) 1075-1109.
- A. Abrams, "Configuration spaces and braid groups of graphs," PhD thesis,
  UC Berkeley (2000).
- J. M. Harrison, J. P. Keating, J. M. Robbins, A. Sawicki, "n-Particle
  quantum statistics on graphs," Commun. Math. Phys. **330** (2014) 1293-1326.

These references are cited as external mathematical context. They are not used
here as retained-grade proof authorities for the quantified `Z^3` theorem.

## Audit-Lane Handoff

The repaired row should be audited only as a bounded witness packet. The
remaining graph-braid route to a full `Z^3` anyon-exclusion theorem needs a
packet-contained proof or a retained standard-math authority establishing the
exchange-generator bridge for all relevant finite boxes and the infinite
lattice limit.
