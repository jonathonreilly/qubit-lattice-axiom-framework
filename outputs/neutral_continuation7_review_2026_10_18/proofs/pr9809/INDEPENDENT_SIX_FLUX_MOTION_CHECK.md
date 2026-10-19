<!-- Original PR9809 source SHA256 9b96512407d152f886e7cb94ad594dc6eff2faed8a2c03cc556911d344095a6d. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent Q6 configuration and motion check

Disposition: PASS for the finite-order, plane-neutral coefficient block and the stated leading hopping signs. This is not independently a microscopic spectral-transfer theorem. The lower orientation combination is antisymmetric, so plane-neutral must not be silently identified with a cubic/point-group scalar.

## 1. Exact minimal configurations

A finite bad-plaquette syndrome has even cardinality in every row and column. Regard its occupied sites as edges of the bipartite row/column incidence graph. With six edges and all positive degrees even, the graph must be a simple six-cycle (two cycles require at least eight edges). It therefore uses three distinct rows and three distinct columns, and is a 3 by 3 array with a permutation matrix removed.

Its perimeter is 24 minus twice its number of neighboring occupied pairs. At most two horizontal and two vertical pairs can be adjacent: among the three rows, one lacks the middle column, and the other two can each contribute at most one horizontal adjacency. Equality requires all three column coordinates consecutive, and similarly all three rows consecutive. Thus minimum perimeter is exactly 16. The six permutation choices invert to two diagonal two-column pairs and four L-shaped three-column configurations. In the even-column-parity branch the minima are precisely the two diagonal-pair orientations, modulo translations and flat-code transformations. This assertion assumes the nonwrapping local regime; finite torus identifications should be treated separately. For even sufficiently large transverse periods, the flat transformations preserve column parity.

## 2. Independent two-edge enumeration

I wrote `/tmp/q6_independent.py` independently of the root script: it toggles the four plaquettes incident to each column, counts shared plaquette edges, enumerates two physical logical-edge flips, and evaluates rational denominators and detour signs. Starting pair is {(0,0),(1,1)}.

A Q6 intermediate above the perimeter minimum can return to a minimum only at the original pair. Thus the order lambda^14 two-hop term is an onsite selfenergy, not transport. The root selfenergy coefficient is consistent with its two units in -gamma^2/(2b).

At order lambda^16, every displaced pair has one Q4 and one Q8 path, with denominators +Delta/2 and -Delta/2, which cancel. The orientation flip to {(0,1),(1,0)} has four Q4 intermediate paths, each with POSITIVE denominator +Delta/2. Therefore the offdiagonal coefficient is +8 gamma^2/Delta. The sign comes from E_initial-E_intermediate, despite the microscopic hopping itself being negative. Describing these as negative Q4 denominators without also changing the perturbation formula is misleading.

## 3. Order lambda^18 offsite coefficients

For a two-hop path through syndrome (q,p),

    d4=(6-q) Delta/4,
    d6=2a(6-q)+2b(16-p).

The contribution through order lambda^18 is

    gamma^2/d4  [order 16],
    -gamma^2 d6/d4^2 + gamma*d*(m1+m2)/d4  [order 18],

where each m is the sum of the two adjacent plaquette signs for that logical edge. These signs are evaluated before that edge flip; the edge commutes with their product/operator because both flipped columns belong to each adjacent plaquette.

For L=10, Delta=5/8, a=250/18432, b=30/8192, independent rational enumeration gives:

* Same-orientation translations by one x or y unit: intermediate types (Q8,perimeter14) and (Q4,perimeter12), energy part -(9/20) gamma^2 and detour part +(64/5) gamma*d.
* Opposite-orientation pair with center translated by one x or y unit: intermediate types (Q8,perimeter16) and (Q4,perimeter12), energy part -(3/10) gamma^2 and zero detour part.
* Opposite orientation at the same center: leading +(64/5) gamma^2 lambda^16; displayed denominator correction -(154/45) gamma^2 lambda^18 and zero detour part. This last order-18 onsite orientation coefficient is NOT complete unless the scalar order-12 winding renormalization is included. That scalar correction affects the orientation constant, but cancels from the displaced paths exactly as the leading hopping cancels.

Using the supplied exact gamma and d, the displaced coefficients are the root's

    a_move = +4.13308411037e-7,
    b_move = -3.936691639339074e-8.

With equal-center orientation Bloch conventions, the lower eigenvalue contains

    2(a_move-b_move) lambda^18 (cos qx + cos qy).

It is minimized at (pi,pi), with positive quadratic coefficient a_move-b_move about that point. The order-16 orientation splitting remains positive in the offdiagonal, so the lower branch is antisymmetric. An unknown order-18 momentum-independent splitting correction does not change this leading curvature conclusion.

## 4. Why an earlier native orientation-changing term is absent

Changing one diagonal pair to the other changes four entire height-10 columns: forty physical spin bits. A transverse V insertion flips two bits. Consequently a direct canonical N0 matrix element between these configurations needs at least twenty V factors. Diagonal H0 resolvents and folded pieces do not evade this count. The order-16 process is possible only after integrating out the flux intermediate with its lambda^4 denominator.

Every nontrivial N0 change below order 20 changes two columns. Up to the orders relevant here these must be adjacent: moving a complete column to transverse distance two already requires twenty edge insertions. Orders 10 and 12 are therefore nearest-pair winding and its scalar/detour dressings. Two-hop routes through nonminimal Q6 configurations retain the same geometric support and remain onsite, including corrections to their denominators. Three nearest-edge hops cannot connect two diagonal-pair minima: each edge toggles checkerboard sublattice parity, while every diagonal-pair minimum has even parity on each sublattice. Thus the superficially possible order lambda^18 three-hop process with two lambda^6 denominators is zero. Four such hops start no earlier than lambda^22. These observations exclude the proposed overlooked lower-order offsite mechanisms within this fixed-order hierarchy.

## Scope

D8 and higher diagonal terms can change common energies and intermediate denominators; they cannot directly rotate a diagonal pair. Their first effect on the Q4/Q8 two-hop translation denominators is later than order 18. Scalar winding dressing must be retained for an absolute orientation energy, but not for the reported leading displaced hopping. This check supplies neither the original measured-source weight nor an actual-H isolated mode, and does not make the antisymmetric orientation branch a scalar particle.
