---
claim_id: edge_register_sites_are_bound_by_exact_pair_totals_when_each_pair_is_two_bond_partners_and_free_when_the_ends_sit_apart_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's edge registers built like rishons (N = (4 + Delta)s fermion-mode sites per end, one site per flavour at each end, raising operator S+ f(n1) with S+ = sum_a c+_1a c_2a, normalised on its domain) and the actuality law's bound-site rule (a site is bound when some set A containing it and A's mirror across one of A's bonds hold a definite total that A alone does not). Theorems: every pair total n_1a + n_2a and the end total commute with every register term (normalised hop, any function of the values, the positive-volume projector, two-register products), at every S (exact, S = 1, 2, 3); a flavour-mixing hop keeps only the end total; the full length window needs exactly one unit in every pair; so in any odds the edge dynamics reaches, each pair holds exactly one unit while each site is occupied with probability <n>/N, indefinite unless the register is surely at an extreme value. Finite diagnostics: the site-level vacuum equals the value-level one (dE <= 1e-15); in a corner tetrahedron of six registers with the positive-volume projector and one- and two-register hops (S = 1, 2, 3), no register is surely extreme in the vacuum or an evolved random state (min site variance 0.18 to 0.24); on a 16-site chain with a 12-site matter ring whose hop is controlled by the register value, partners placed as bond partners give 4/4 register sites bound and 0/12 matter sites, with |A| <= 2 and with every set, while ends placed apart give 0/4 bound; a set pair covering the whole finite matter ring binds every site (finite-size artefact); the variant 'mirror across any lattice plane' binds the far-apart register and no matter site. Estimates: the register's BMV numbers (0.79 rad inner phase, concurrence 0.156) are reproduced and do not depend on records, since records never condition the odds; quadrupole graviton emission per run ~5e-60. Verdict: CL-1 as written does not place the ends, so the rule does not decide; read as ends at the edge's two vertices, edge sites are free and their locks fix a distant partner; the fix is a layout clause (each site a bond partner of one site at the other end, the hop moving units within pairs), which Admissibility already favours. Toy sizes, hop weights, stiffness and layouts supplied; no 3D lattice, no split, no CL-3 phase."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/edge_register_sites_are_bound_by_exact_pair_totals_when_each_pair_is_two_bond_partners_and_free_when_the_ends_sit_apart_2026_10_22.py
---

# Edge-register sites are bound by exact pair totals when each pair is two bond partners, and free when the ends sit apart

Claim type: bounded_theorem.

The candidate-law register has zero premise weight. Its actuality law (CL-2) now excludes bound sites from records: "A site is bound when some set containing it and that set's mirror across one of its bonds hold a definite total that the set alone does not; a bound site's occupation is part of the actual configuration but gets no record." The neighbourhood-roles probe (PR #9970) verified this for rishons in a U(1) quantum-link toy, where Gauss's law makes pair totals definite, with sets of at most two sites. Edge registers have no Gauss law. This note asks whether edge-register sites are bound under the rule as written, and if not, what the smallest fix is. Axiom text is quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` and is not edited. Admissibility: "There is one fixed nearest-neighbor admissibility rule". Record: "When present, a record locks exactly one admissible local possibility."

## The register

CL-1 Edges: "A register is (4 + Delta)s fermion-mode sites at each end, role-assigned in a coarser block; its length is its flat length ... times 2^(n/s - 3), with n the occupation at its first end". The CL-3 edge tick raises it with "V_e + V_e^dagger ... each V normalised on its domain". Its site-level form is the rishon construction (edge-source, PR #9929, item 6): one site per flavour a at each end, S+ = sum_a c+_1a c_2a, and V = S+ f(n1) with f fixed so that V|n> = |n+1> on the top multiplet. Write N = (4 + Delta)s.

## Statement

A. Exact algebra (every S).

1. Each pair total n_1a + n_2a commutes with c+_1b c_2b for every a and b, and with every function of the end occupations. So it commutes with V, with V^dagger, with the phase terms, with the positive-volume projector (a function of the values), and with the two-register hops V_e V_f and V_e V_f^dagger. The end total n_1 + n_2 is conserved too. The runner checks the commutators at site level for S = 1, 2, 3: all exactly zero (A1).
2. Control. A flavour-mixing hop c+_1 Q c_2, with Q a random orthogonal matrix, breaks the pair totals (commutator 0.34 to 0.65) but keeps the end total (A1b). So the pairs come from the sum-over-pairs form of the hop. Without it, only the whole-end set pair could bind, and only if the two ends are mirror layers.
3. Window. With e empty pairs and d doubly filled pairs, the value n1 runs over [d, N - e] only. CL-1's full window, from an eighth of the flat length up to 2^(1+Delta) times it, needs n = 0..N, so every pair holds exactly one unit (A2, enumerated).
4. Hence, in every odds the edge dynamics reaches, each pair total is exactly 1. In the top multiplet each register site is occupied with probability p = <n>/N, with variance p(1 - p), which is indefinite unless the register is surely at n = 0 or n = N. The vacuum value n = 3s gives p = 3/(4 + Delta), so the variance is 0.24 at Delta = 1, independent of s. This is the large-S pattern: nothing in items 1 to 4 depends on S.

B. Finite diagnostics.

5. The site-level vacuum is the value-level vacuum: the same energy and the same length law, to 1e-15, for S = 1, 2, 3 (A3, A4). With each pair's two sites placed as bond partners, the rule with |A| <= 2 binds every register site (4/4, 8/8, 12/12).
6. Tetrahedron (B1, B2). A corner tetrahedron of the five-tetrahedron cube has three axis edges and three diagonals, giving six registers at value level with lengths flat x 2^(5n/N - 3) (Delta = 1). The model uses:
   - a Cayley-Menger positive-volume projector, plus positive face areas;
   - one-register hops and two-register hops between edges that share a vertex;
   - a harmonic phase about the flat value.
   In the vacuum and in a random allowed start evolved by the projected tick, no register is surely extreme (max P(extreme) 0.45, 0.39, 0.20 for S = 1, 2, 3). The minimum site variance is 0.18 to 0.24. The projected tick never leaks out of the allowed set and is unitary there. So every edge site in the tetrahedron is bound once its partner is a bond partner.
7. Matter is not bound by the register (C1). The toy is a 16-site chain: one S = 1 register (4 sites) and a 12-site matter ring at half filling with a staggered mass. The hop of one matter bond is controlled by the register value (amplitude 1 + 0.4(n - 1)), and a density-value coupling entangles the two. With partners adjacent ([1a, 2a, 1b, 2b, matter]), the rule binds 4/4 register sites and 0/12 matter sites, in the coupled vacuum and in an evolved random state. This holds with |A| <= 2 and with every set, leaving out only set pairs that cover the whole matter ring (item 9). A set that mixes register pairs with matter sites has total (pairs) + (matter part), which is definite only if the matter part is, so register pairs never lend definiteness to matter.
8. Ends apart (C2). The ends are placed as the edge's two vertices would place them ([1a, 1b, matter, 2b, 2a, matter], with partners mirror images about a plane far from both). No set pair is definite, so every register site is free, although each pair total is still exactly 1.
9. Finite-size artefact (C3). In a finite toy, a set pair covering a whole number-conserving component holds its conserved number. With partners adjacent, the matter ring alone is such a component, and every matter site is then bound. On Z^3 the sea is infinite: no finite set pair covers it, and its region counts fluctuate. So the rule is not affected on the CL-1 lattice, but toy tests must leave covering pairs out, and a closed (compact) universe would bind all matter.
10. Variant reading (C4). "Mirror across any lattice plane" (A need not touch the plane) binds the far-apart register as well, and still binds no matter site. It makes a site's role depend on correlations over the edge's length (b_e >~ 40 cells).

C. Gravity-mediated entanglement (estimates).

11. The register's numbers are G m^2 T/(hbar d) = 0.79 rad for the inner branches and concurrence |sin(dphi/2)| = 0.156 with dphi = 0.314, for the linear two-arm geometry (1e-14 kg, d = 200 um, splitting 250 um, 2.5 s) (D1).
12. Theorem (CL-2): "Records never condition the odds". Readable distributions are Born marginals of the odds, so they do not depend on which sites are recorded. The witness is safe whether edge sites are bound or free. The masses' own matter sites are already recorded every half-tick, and the prediction never relied on their exclusion. The concern that recorded edges decohere the geometry has no basis in the laws. The decoherence that does act is in the odds and is the same either way: quadrupole graviton emission gives about 5e-60 gravitons per run (D2).
13. If edge sites were free, edge registers would add 12(4 + Delta)s/b_e^3 = 0.13 records per cell per half-tick (s = 135, Delta = 1, b_e = 40) (D3).

## Verdict

- CL-1 places the register's sites only by "role-assigned in a coarser block". Whether they are bound turns on geometry the text does not fix, so the rule as written does not decide.
- Read as "ends at the edge's two vertices" (the natural reading of "at each end"), edge sites are free. Their locks then fix a distant partner, because the pair total is exact. That breaks the reading the rule was adopted to enforce (owner decision 1: a lock fixes no other site's possibility).
- The defect is the Record reading, not the gravity prediction.

## Fix (proposal, CL-1 Edges)

Replace "A register is (4 + Delta)s fermion-mode sites at each end, role-assigned in a coarser block;" with:

> "A register is (4 + Delta)s fermion-mode sites at each end, role-assigned in a coarser block, each site a bond partner of one site at the other end; its raising operator is the sum over partner pairs of the hop from the second end to the first, normalised on its domain;"

Under this layout CL-2's rule binds every edge site (items 1 to 7), with single-site mirror pairs, at every S. No matter site is bound, and the bound-site rule needs no change. Sites of a register held at an extreme value (a held floor during a split) are definite, so they are free. Their records lock values that are already fixed, which is harmless.

Optional unification: CL-1 Links already makes rishon ends straddle B_f faces, so one sentence, "each register site is a bond partner of one site at its register's other end", could serve both kinds of register.

Alternative, not preferred: read CL-2's mirror across any lattice plane (item 10). It binds the far register too, but it makes roles non-local and leaves the register hop non-local.

## Smuggling review

**Supplied:**
- the placement (supplied before too, now stated);
- the toy hop weights (t = 1, two-register 0.25), the stiffness 0.5, the coupling 0.4 and 0.5, the staggered mass 0.3;
- the corner tetrahedron and the vertex-sharing two-register set;
- sizes, seeds and TOL 1e-10.

**Forced, given the register construction:**
- exact pair totals (algebra);
- one unit per pair (window);
- site indefiniteness away from the extremes;
- binding of every edge site once partners are bond partners;
- no binding of matter;
- independence of readable distributions from record assignment.

**Reason for the placement, not an import:** Admissibility is nearest-neighbour, and with partners adjacent the register hop is a sum of nearest-neighbour bilinears. With ends at the vertices it spans b_e cells. The fix adds no parameter.

**Lopsided:** the "first end" orientation remains. The window is asymmetric (1/8 to 2^(1+Delta)), so a register needs an orientation; n1 = (N + n1 - n2)/2 exactly, so either end's reading is the same up to that orientation.

## Boundary

Not claimed:
- a 3D layout of the (4 + Delta)s pairs in a block (the budget fit is block-hierarchy's);
- the split's passing at site level;
- CL-3's phase;
- registers outside the top multiplet beyond item 1's algebra (which holds there too);
- a closed-universe version of the rule (item 9).

The tetrahedron is value-level, and A4 is what justifies the reduction.

## Dependencies

Used:
- PR #9970 (neighbourhood-roles: the bound-site rule, its |A| <= 2 runner form, C3 multi-site ends);
- PR #9929 (edge-source item 6: the rishon-built register);
- PR #9977 (register-size-s: s >= 135, b_e >~ 40);
- PR #9926 (link-zoom: rishon ends across faces).

Narrowed: PR #9970's C3 statement that the condition "covers edge-type registers". It does so only when the ends are mirror images across a bond.

## How to run

```
python3 scripts/edge_register_sites_are_bound_by_exact_pair_totals_when_each_pair_is_two_bond_partners_and_free_when_the_ends_sit_apart_2026_10_22.py
```

Needs numpy and scipy, and declares `AUDIT_TIMEOUT_SEC = 120`. It runs in about 11 s at about 170 MB resident, prints about 4.7 kB and ends with `TOTAL: PASS=14 FAIL=0`. It was run through `scripts/runner_cache.execute_runner` from a temp origin/main worktree (status ok), and two runs gave identical output.
