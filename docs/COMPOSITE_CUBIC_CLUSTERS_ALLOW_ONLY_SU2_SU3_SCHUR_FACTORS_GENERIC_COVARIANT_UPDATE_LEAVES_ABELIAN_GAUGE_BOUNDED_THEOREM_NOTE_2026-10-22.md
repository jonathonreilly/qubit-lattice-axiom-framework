---
claim_id: composite_cubic_clusters_allow_only_su2_su3_schur_factors_generic_covariant_update_leaves_abelian_gauge_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "One qubit per site of Z^3 read in site blocks of side b. Exact: the cubic group's irreps have dimension at most 3 (C4v at a bond end: at most 2; the spinor lift adds 4, which no site-permutation representation contains), so Schur-protected multiplets of a composite cluster can carry only SU(2) and SU(3) simple factors; every site orbit carries A1 exactly once; the first block with two or more sites and a C4v doublet per bond end is b = 4. At b = 5 (inner 6-orbit as composite matter A1 + E + T1, 3x3 face ends as link-end registers), the per-cluster gauge algebra (commutant of every cluster-local, cluster-number-conserving piece) is u(1)+u(2)+u(3) for on-cluster pieces alone, but abelian once generic C4v-covariant matter-end pieces are added, and only the cluster number (dim 1) once end-end plaquette pieces are added; also abelian for proper rotations with complex pieces; an internal two-copy label per site restores u(2). Fock registers of Schur multiplets (d_i <= 3), even sector, group prod SU(d_i) x U(1)_X with X = 2N - n: every even n has an invariant mass; n = 3 is anomalous; n = 5 is the smallest anomaly-free, mass-protected, non-abelian-charged register, every split of 5 passes, and the split with the largest one-body commutant is uniquely 3 + 2 (13); with the spinor lift it would be 4 + 1. The cluster, piece supports, Fock reading, even sector, mass-protection criterion and the least-information measure are supplied. No gauge group is forced by the update; SU(3) x SU(2) x U(1) is conditionally selected among Schur-realisable registers, not derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/composite_cubic_clusters_schur_factors_generic_update_abelian_2026_10_22.py
---

# Composite cubic clusters allow only SU(2) and SU(3) Schur factors; the generic covariant update leaves an abelian gauge group

Claim type: bounded_theorem.
Primary runner: `scripts/composite_cubic_clusters_schur_factors_generic_update_abelian_2026_10_22.py`
(campaign copy agents/nonabelian-composite/runner.py; TOTAL: PASS=19 FAIL=0, about 0.5 s, about 130 MB peak).

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
fix one qubit per site of Z^3 and name no gauge group. The [SU(N) link note](DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS_ONE_QUBIT_CARRIES_NO_SU_N_LINK_SU2_NEEDS_TWO_SU3_THREE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
shows that a supplied SU(N) link needs at least 2N states. This note asks whether composite registers (several one-qubit
sites per coarse edge, from rung-2 to rung-5 blocks) carry a non-abelian gauge group that nobody names, and whether
the cubic geometry singles one out.

## Statement

A. Census (exact).
1. The irreps of the rotation group O have dimensions 1, 1, 2, 3, 3; those of C4v (the stabiliser of a bond end in O_h)
   have dimension at most 2; the binary octahedral lift adds 2, 2, 4 (48 = sum d^2). A site-permutation representation
   is single-valued, so it never contains the 4. Schur-protected degeneracies of a composite cluster are therefore at
   most 3-fold at a vertex cluster and 2-fold at a bond end, so the only simple factors such multiplets can carry
   are SU(2) and SU(3).
2. The six half-links of a site carry A1 + E + T1 (reproduces time-complex-structure S1). Every O-orbit of sites carries
   A1 exactly once (a transitive permutation representation), so no cubic cell carries E + T1 without an A1.
3. Sites per bond end (Voronoi) and C4v doublets per end, for block sides b = 2..7: 0/0, 1/0, 4/1, 10/2, 20/5, 35/8.
   The first block with at least two sites per end and a protected doublet at the end is b = 4. At b = 2 and 3 a coarse
   edge carries only abelian (two-state per end) links. The state count never binds (b >= 4 gives 2^8 states per bond,
   against 4 or 6 needed): what binds is a protected degeneracy.

B. The generic covariant rule (exact commutants, b = 5).
The cluster is the inner 6-orbit (composite matter, A1 + E + T1) plus six 3x3 face ends (link-end registers),
60 sites. If each cluster's fermion number is conserved (the abelian Gauss law of the emergent-gauge note), every
inter-cluster term is a product of cluster-local, number-conserving pieces. The per-cluster gauge algebra is then the
commutant of all such pieces.
1. On-cluster O_h-invariant pieces only: commutant u(1)+u(2)+u(3) (dim 14, derived 11). This is the Schur symmetry of
   A1 + E + T1.
2. Adding generic C4v-covariant matter-end pieces: abelian (dim 7, derived 0). The same holds with the matter-matter
   part removed (pairings and end-local terms only). The reason: each end pairs with a different 2-plane of T1 (and
   T1 restricted to C4v is A1 + E). The six pairings together leave only diagonal phases.
3. Adding end-end (plaquette) pieces: only the cluster number survives (dim 1).
4. Proper rotations only, with complex Hermitian pieces: abelian (dim 1). C4 has no 2-dim irrep.
5. Control: an internal two-copy label on every site (atomic; it bends the Qubit axiom) turns each u(1) into u(2).
   A non-abelian group needs a label that no covariant rule can see. One qubit per site supplies none: every
   multiplicity copy of an irrep sits on a geometrically distinct orbit (a different radius), and generic covariant
   terms distinguish orbits.

C. Fock registers of Schur multiplets (exact enumeration, n <= 6).
Register Lambda(sum C^d_i) with d_i in {1, 2, 3}. The even sector is the chiral half picked by the time arrow
(time-complex-structure T1e). The group is prod SU(d_i) x U(1)_X, with X = 2N - n the number-conservation charge
(time-complex-structure T5b). Tested: SU(3)^3, Witten SU(2), SU(d)^2 X, X and X^3 anomalies; invariant symmetric
bilinears (Majorana-type masses) in Sym^2; non-abelian charge.
1. Every even n fails, because the empty and filled states (X = -n, +n) pair into an invariant mass.
2. n = 3 fails: (3) gives 1 + 3bar (SU(3)^3 anomaly), and (2,1) has one doublet (Witten).
3. n = 5 is the smallest passing register. Every split with parts <= 3 passes (3+2, 3+1+1, 2+2+1, 2+1+1+1), because all
   of them sit inside U(5) acting on the 16. Anomalies do not pick the split.
4. Least information, measured as the fewest distinct one-body frequencies (the largest generic one-body commutant,
   sum d_i^2), picks 3+2 uniquely (13, against 11, 9, 7). Its even sector is the one-family content with nu^c, every
   tested anomaly is zero, and it has no invariant mass.
5. If the spinor lift were allowed (d = 4), the same measure would pick 4+1. The selection depends on the multiplets
   being site-permutation (single-valued) representations.

## Answer to the three questions

(1) Composite edge registers can carry SU(2) links from b = 4 (one C4v doublet per end) and SU(3) only at vertex
clusters (T1). The count is never the obstruction. Under any generic cubic-covariant cluster rule, the per-cluster
gauge algebra is abelian (B2-B4).
(2) The cubic geometry restricts the Schur-protected factors to SU(2) and SU(3) (A1). Among Fock registers of such
multiplets, anomaly freedom, mass protection and least information pick 3+2, i.e. SU(3) x SU(2) x U(1)_Y x U(1)_X on
the 16. The 3 axes alone give T1 (an SU(3) triplet), but the register 1 + 3bar is anomalous (C2). E + T1 is the
cheapest passing combination.
(3) Honest status. SU(3) x SU(2) x U(1) is SELECTED only conditionally, by four supplied criteria: Fock reading of one
cluster, even sector, mass protection, and least information = largest commutant. Even then it is a symmetry of the
on-cluster rule, not of the generic covariant update, which breaks it to abelian. It is not forced. The 5-mode
register also needs the A1 removed (A2).

## Gate (anti-smuggling)

Rule SB (Schur blindness), proposed and scored: "every cluster-local piece of the update commutes with the
cluster's Schur group (the commutant of the generic on-cluster tick)".
1. No number chosen: PASS.
2. No structure named: PASS literally, because the group follows from the cubic irreps. FAIL in substance: the clause
   is chosen to keep a degeneracy that generic covariant end pairings break. It is the same tuning found in
   time-complex-structure S5 (11 marginal couplings), now proven at the gauge-piece level (B2).
3. Predictions not built for (UNTESTED): no simple gauge factor beyond SU(3) as an exact cluster symmetry (no exact
   SU(5)/SO(10)); a second neutral U(1)_X boson if X is gauged; nu^c required (n = 5 is odd and anomaly-free only
   with it).
4. Bends no axiom, but it adds a clause.
Verdict: FAILURE as a derivation (gate clause 2 in substance). The census (A), the abelian no-go for generic rules (B)
and the conditional selection (C) stand as exact results. Naming SU(3) x SU(2) x U(1) was not done and is not needed
for (C); the criteria in (C) are supplied.

## Boundary

Supplied: the block side and the choice of matter orbit and end regions; piece supports (on-cluster, matter-end,
end-end) and their real or complex type; cluster-number conservation as the abelian Gauss law; the Fock reading,
the even sector, U(1)_X, the mass-protection criterion, and least information = largest one-body commutant.
Not established: any dynamics that makes the end pairings Schur-blind (emergent restoration under RG is untested),
removal of A1, any gauge coupling, confinement, or a continuum limit. The 2N-state bound, the Witten and new SU(2)
anomalies, and the 16 of Spin(10) are cited. The Witten anomaly is computed here as 2 Tr J3^2 mod 2, valid because the
registers contain only j <= 1/2.

## Notes used

- Main: DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS (2N bound; this note shows the count never binds
  for b >= 4 and that the binding condition is Schur protection); A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS
  (rishon sites carry no records, consistent with link-zoom item 6).
- Campaign: emergent-gauge-composite (Z2/U(1) at rung 2; narrowed here: rung 2 and 3 edges are abelian-only);
  time-complex-structure (S1 reproduced; S5 lock lifted to the gauge-piece level; T1e and T5b used); link-zoom
  (flavour-blind rishons give SU(3) by supplied blindness; B5 is the same mechanism with the label made explicit);
  gauge-registers (no group selected by register size; agrees with A3); nonabelian (Lie-algebra self-coupling from a
  vector response; agrees that the algebra is not fixed).
- Literature: Bethe (cubic double-group irreps); Witten 1982; Wang-Wen-Witten 1810.00844; Georgi-Glashow; Chandrasekharan-Wiese 1997.
