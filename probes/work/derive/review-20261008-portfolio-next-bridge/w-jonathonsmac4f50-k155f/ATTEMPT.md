# J:derive:review-20261008-portfolio-next-bridge:a1 -- family 265 (dimer entropy / coefficient selection), symmetric version

Worker: Claude Sonnet 5.5, same-family, unrefereed. Output directory only; repository not edited.

## Plain-language summary

The portfolio says an area-law upper bound (for gapped, local, unique-ground-state systems) cannot by itself pick the number 1/4, because a lattice of disjoint dimers has all those properties while its entropy per cut edge can be dialled continuously. A fair objection: a dimer tiling is not the same in every direction and at every site, and the framework's Lattice axiom says no site is privileged and rules are covariant under translations and proper cubic rotations. I replaced the dimers by a family that has those lattice symmetries exactly: qubits on a box of Z^d, with a controlled-phase of angle phi on every nearest-neighbour edge. Its Hamiltonian is a sum of commuting norm-one projectors with a unique ground state and gap exactly 1, for every size. The entropy across a flat cut is exactly (number of cut edges) times h((1+cos(phi/2))/2), which runs over all values from 0 to ln 2 as phi runs from 0 to pi. So the non-selection survives the symmetry restriction. This is a scoped comparison, not a statement that no covariant carrier can fix the coefficient, and I could not read the external theorem, so whether this family meets its exact hypotheses (step 11) is the first unresolved step.

## Read before concluding (stated as required)

- Axioms: I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full on current main (a77a3449c9...), main_wt path `docs/MINIMAL_AXIOMS_2026-06-29.md`:35-90 (four axioms and qualification), 108-112 (axioms plus approved primitives are the whole supplied foundation), 114-130 (admissibility is not a dynamics axiom; no Hamiltonian is supplied).
- Primitives: I read `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full (approved: scale_reference_primitive, kinetic_isotropy_primitive, realized_state_primitive). None is used below. I did not open `docs/audit/data/axiom_premise_nodes.json` itself; the check file's generated block is what I relied on.
- Sources: the five pinned objects at commit 845c625265a4bba3caba176f4155c4f513eb04f5; all five sha256 digests re-computed from `git show` and equal TASK.md (RECOVERY_STATUS.json). I read PORTFOLIO_INDEX.md and REPORT.txt, root/RESULTS.txt and continuum/RESULTS.txt in full, and kinetic/RESULTS.txt in the parts naming 145/154.
- Prior-art search: main docs (`AREA_LAW_*` notes, grep for graph/cluster/controlled-phase states), probes view (`work/`, `tasks/`; no earlier attempt on this task id), and open PRs mentioning area law (gh, titles only: #10036, #10011, #10032 and similar candidate-law notes). I found no note computing a covariant weighted-graph-state area-law family. I did not read those open PRs' bodies, so overlap is not excluded.

## What the axioms say, what lanes supplied, what is shown

- Axioms (docs/MINIMAL_AXIOMS_2026-06-29.md:35-41, 55-61): sites of Z^3, no privileged site; one admissibility rule covariant under translations and proper cubic rotations. Qubit axiom (43-53): each site carries M_2(C), no possibility privileged. Nothing supplies a Hamiltonian, a ground state or a gap (114-130).
- Lane-supplied (portfolio, not axiom): the disjoint-dimer model and the claim that the generic area-law bound cannot select 1/4 (portfolio/root/RESULTS.txt:15-17; PORTFOLIO_INDEX.md:25). The external area-law theorem's hypotheses are known to me only through that paraphrase.
- Supplied by me: the model H_phi below. It is a comparator, not a framework object.
- Shown: steps 5-10.

## Steps

1. [READING] Candidate choice. Of the seven pinned items I picked 265 because its inference ("bound plus gap cannot select the coefficient") has a single concrete weak point, symmetry, that an exact finite construction can test. Others: 215 (needs the multi-link operator and state, not supplied), 261/290/204 (hypothesis mismatches already exact; no new obligation I could discharge in the budget), 113/120 (fibre constancy already makes any event of the f-factor pull back, so no new obligation there), 145/154 (for a finite mixing chain the tuple-dependent null set can be made uniform over all tuples by multilinearity on a finite state space, a remark not a bridge; the growing process has no stationary law). These dispositions are readings, not proofs.

2. [ASSUMED] Premise from the lane: the external theorem needs local norm-one terms, a unique ground state and a uniform gap, and its conclusion is only an upper bound on the entropy across boundaries (root/RESULTS.txt:16). I do not know its interaction-range or dimension wording.

3. [PROVED] The dimer family is not translation invariant. If a dimer tiling (a perfect matching of Z^d edges) contains {0,e_i} and is invariant under all translations, it contains {-e_i,0} too, so site 0 lies in two tiles, contradiction. It is also not invariant under proper rotations about any site (the tile through that site is moved). CHECKED on tori Z_4^2 and Z_3^3 (check.py, "no translation-invariant dimer tiling"). This does not invalidate the lane's counterexample in its own scope; it shows the scope.

4. [PROVED] Setting. Let G be a finite graph (an open box or a torus of Z^d), one qubit per vertex, n vertices, E(z) = sum over edges uv of z_u z_v for z in {0,1}^V. Let U = prod CPhase_{uv}(phi) be diagonal with entries exp(i phi E(z)). Put P_v = 1 - |+><+|_v, h_v = U P_v U^dagger, H_phi = sum_v h_v, psi_phi = U |+>^{n}. Here CPhase = diag(1,1,1,exp(i phi)).

5. [PROVED] Local form. Edges not touching v act on other qubits and commute with P_v, so h_v acts only on v and its neighbours: h_v = 1 - |+_k><+_k|_v with |+_k> = (|0> + exp(i phi k)|1>)/sqrt2 and k = number of occupied neighbours of v. Each h_v is a rank 2^(n-1) projector, norm one, support the star of v (7 qubits in the interior of Z^3).
   [CHECKED] check.py builds h_v from this local formula and, independently, as U P_v U^dagger, and finds them equal entrywise (exact, phi = 2pi/m for m = 2, 3, 4, 6) on chain n=4, 2x2, 2x3 and 2x2x2 boxes; also h_v^2 = h_v, [h_u,h_v] = 0 for all pairs, Tr h_v = 2^(n-1), H psi = 0.

6. [PROVED] Spectrum. Since [P_u,P_v] = 0, H_phi = U (sum_v P_v) U^dagger has spectrum {0,...,n}, multiplicity C(n,k), unique ground state psi_phi, gap exactly 1, for every finite graph, every phi, every size. [CHECKED] prod_{k=0}^{n}(H-k) = 0 and Tr H^p = sum_k C(n,k) k^p (p = 1..n) exactly, which fix the multiplicities (check.py, chain n=4, 2x2, 2x3).
   Infinite volume, frustration-free sense only: a state omega on the quasi-local algebra with omega(h_v) = 0 for all v corresponds, via the automorphism Ad U, to a state giving expectation 1 to every projection |+><+|_v, which is the product state; so it is unique. That this set equals the set of ground states in the Bratteli-Robinson sense is standard for commuting projector sums and is not re-proved here [ASSUMED].

7. [PROVED] Lattice symmetry. The edge set of Z^d (and of an open box, up to the box's own symmetries) is invariant under translations and under the proper cubic rotations, and CPhase is symmetric in its two qubits, so U, hence every h_v and H_phi, is invariant (permutation of sites). [CHECKED] graph automorphism check for all 24 proper rotations on 3x3x3 and 2x2x2 boxes, all 27 translations on the 3x3x3 torus (81 edges, 6 neighbours each), and operator-level P_pi h_v P_pi^-1 = h_pi(v) for all 8 symmetries of the 2x2 box. Not covered: on-site unitary covariance (the Qubit axiom's "no possibility is privileged"). H_phi singles out the Z basis and the |+> direction, exactly as the dimer terms single out |00>,|11>. Whether that axiom requires such covariance of a Hamiltonian is not decided here [READING].

8. [PROVED] Entropy across a matching cut. Let V = A union B and suppose the cut edges (a_i,b_i), i = 1..L, have 2L distinct endpoints. Then psi_phi(z) = 2^(-n/2) alpha(z_A) beta(z_B) prod_i c(z_{a_i}, z_{b_i}) with |alpha| = |beta| = 1, c(x,y) = exp(i phi x y). Tracing out B gives rho_A = 2^(-|A|-L) D K D^dagger, with D = diag(alpha) and K(z,z') = prod_i g(x_i,x_i'), g(x,x') = 1 + exp(i phi (x - x')), x_i = z_{a_i}. Writing K = 2^(|A|-L) R G R^T with G = g^{(x)L} and R the isometry spreading each boundary pattern uniformly over its preimages, the non-zero spectrum of rho_A equals that of (g/4)^{(x)L}. g has eigenvalues 2 +- 2|cos(phi/2)|, so rho_A has non-zero eigenvalues prod over i of (1 +- |cos(phi/2)|)/2, and
   S(A) = L h((1+|cos(phi/2)|)/2),  h the binary entropy.
   Nothing about the bulk of A or B enters. Flat half-space cuts of a box of Z^d are matching cuts (each boundary site has exactly one cut edge).
   [CHECKED] check.py: exact equality Tr rho_A^p = (lam+^p + lam-^p)^L for p = 1..dim rho_A (which fixes the full spectrum) on chain 1|1, 2x2, 3x3 (column cut), 4x2 (middle cut, A with 4 sites), 2x2x2 cube (layer cut, L = 4), for phi = pi, 2pi/3, pi/2, pi/3; and high-precision entropies equal L h. Scope control: for a single interior site of the 3x3 grid (four cut edges sharing one site) the exact purity (1 + cos^8(phi/2))/2 differs from the matching formula, so the additive law is specific to matching cuts.

9. [PROVED] Range of the coefficient. s(phi) = h((1+cos(phi/2))/2) is continuous, s(0) = 0, s(pi) = ln 2, and strictly increasing on [0,pi] (cos(phi/2) falls, h falls in its argument above 1/2). So every coefficient in [0, ln 2] is the entropy per cut edge of some H_phi. [CHECKED] sympy derivative positive on 399 grid points, endpoints exact; the value 1/4 nat is attained at phi = 1.06002058793 and 1/4 bit at phi = 0.82253614802 (floating root, mpmath). Whether the framework's 1/4 is per edge, per face, in nats or bits is not asserted.

10. [READING] Consequence. Inside the class "qubits on Z^d, translation- and cubic-rotation-invariant, finite-range norm-one commuting terms, unique frustration-free ground state, gap 1 at all sizes", the area-law upper bound constrains the coefficient only to [0, ln 2]; the parameter phi, a Hamiltonian input, fixes it. This preserves the lane's statement as a local comparison and removes the symmetry objection to it. It selects nothing about the framework's 1/4.

11. [UNRESOLVED -- first failing/unresolved step] Hypothesis match with the external theorem. The five fixed sources only paraphrase it. H_phi has star terms of radius 1 (7 qubits on Z^3, 5 on Z^2, 3 on Z^1), not two-body nearest-neighbour terms. If the theorem requires two-body terms, or a specific dimension or gap notion, this family may fall outside it and step 10 would be weakened to "within the class of finite-range commuting-projector Hamiltonians". I did not download or read the theorem. Two further open sub-obligations: (a) a nearest-neighbour two-body symmetric family with tunable coefficient; (b) any family with global on-site unitary covariance.

## What is new relative to the sources

New (scoped, same-family, unrefereed): the translation- and cubic-rotation-invariant replacement for the dimer counterexample, steps 4-9, with the closed-form flat-cut entropy and an exact finite check. Not new: weighted graph states, commuting-projector parent Hamiltonians and the fact that cluster-state-type states obey an area law (standard quantum-information background, recalled from memory, not retrieved); the dimer non-selection itself (root/RESULTS.txt:16); the observation that the dimer example is not symmetric is mine but elementary.

## Claim boundary

No status words are claimed. Not shown: that H_phi satisfies the external theorem's exact hypotheses; any thermodynamic-limit gap statement beyond the frustration-free uniqueness in step 6; any link between H_phi and the framework's Admissibility rule (the neighbour-count dependence of |+_k> is an analogy only, since the Z-basis distribution of psi_phi is uniform and neighbour-independent); any value of the framework's coefficient.

## Files

check.py (148 checks, about 7 s, about 64 MB peak), RECOVERY_STATUS.json, this file.
