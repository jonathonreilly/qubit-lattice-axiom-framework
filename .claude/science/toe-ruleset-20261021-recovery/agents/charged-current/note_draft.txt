---
claim_id: masses_read_from_a_response_set_field_force_a_hypercharge_half_doublet_and_universal_v_minus_a_decays_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Conditional on one supplied chiral family (Q, u, d, L, e, n) and on fermion masses read from a field that the response law sets: with the supplied term list the exact abelian charge is unique, with hypercharge ratios Q:u:d:L:e:n:H = 1:-4:2:-3:6:0:3, so the mass field has hypercharge 1/2; any nonzero vacuum value of it leaves exactly one unbroken abelian generator, Q = T3 + Y, gives the link spectrum {0, mW^2, mW^2, mZ^2} with rho = 1, and the contact coupling G_F = 1/(sqrt2 v^2) for every doublet; if the mass field is instead a fixed coefficient, only colour and Q are linked and there is no charged current. In a supplied lattice-cone model the three-body V - A rate tends to G^2 m^5/(192 pi^3) (finite diagnostic, Monte Carlo). Lifetimes against measurement are estimates with supplied v, couplings, V_ud, g_A and f_pi. No chiral content, mass field origin or value of v is derived."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/masses_read_from_a_response_set_field_force_a_hypercharge_half_doublet_and_universal_v_minus_a_decays_2026_10_22.py
---

# Masses read from a response-set field force a hypercharge-1/2 doublet and universal V - A decays

Claim type: bounded_theorem.
Primary runner: `scripts/masses_read_from_a_response_set_field_force_a_hypercharge_half_doublet_and_universal_v_minus_a_decays_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3 in the three-law numbering) links a symmetry of the update, meaning one the update commutes with when every field the response law sets (edges, links and any vacuum field) is transformed too; coefficients the response law does not set stay fixed. This note asks which generators are linked when the fermion masses are fixed coefficients and when they are read from a field the response law sets, and what charged-current decays then look like. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the chiral content nor the mass field. Every result here is conditional on both.

## Statement

1. With one supplied chiral family of Weyl fields Q, u, d, L, e, n and a mass field H, and with the supplied terms Q u H, Q d H*, L e H*, L n H, n^4 and u d d n, the exact abelian charges form a one-dimensional space. Normalised to Y_H = 1/2 it is 6Y = (1, -4, 2, -3, 6, 0, 3) for (Q, u, d, L, e, n, H). Every mass bilinear carries hypercharge +-1/2 and pairs a weak doublet with a singlet, so the mass field is forced to be a doublet of hypercharge 1/2.
2. If H is a fixed coefficient (frozen at any vacuum value v != 0), the update commutes only with the stabiliser of v. Of the 8 + 3 + 1 = 12 generators of colour x su(2) x u(1)_Y, 9 remain (colour and one abelian generator), so no charged-current link exists. If H is transformed with the fermions, all 12 are symmetries; the stabiliser of the vacuum value is one-dimensional, Q = T3 + Y, giving charges 0, -1, 2/3, -1/3 for the neutrino, electron, u and d.
3. From |D H|^2 at the vacuum value the link mass matrix has spectrum {0, mW^2, mW^2, mZ^2} with mW = g v/2 and mZ = sqrt(g^2 + g'^2) v/2 for every vacuum direction, so rho = mW^2/(mZ^2 cos^2 theta_W) = 1 exactly. In the contact limit G_F = sqrt2 g^2/(8 mW^2) = 1/(sqrt2 v^2): g cancels and the coupling is the same for every doublet.
4. Supplied model, finite diagnostic: for a V - A contact decay of a massive doublet member into three massless modes on lattice cones E = |2 sin(k/2)|, the rate tends to G^2 m^5/(192 pi^3) at small m a, with exponent 5, and the lattice correction stays below 1% at m a = 0.6.

## Derivation

Abelian charges. Each supplied term is invariant exactly when its charge sum vanishes, so the abelian charges are the null space of the 6 x 7 integer matrix of term contents. The runner finds it one-dimensional with sympy. The four mass terms alone leave a three-dimensional space of abelian charges on seven fields; the two terms without H (the four-mode term on n and u d d n) remove the two beyond hypercharge. They are part of the supplied term list, and without them baryon- and lepton-type charges would also be exact.

Stabiliser. The broken generators at v are those with G v != 0. Writing the four generators of su(2) x u(1)_Y acting on v as real 4-vectors, the unbroken dimension is 4 minus the rank of that set; it is 1 for 20 random complex v. At v = (0, 1) the unbroken generator is T3 + Y.

Link masses. The quadratic form M2_ab = g_a g_b Re(v^+ {G_a, G_b} v) on the four electroweak generators has eigenvalues 0, g^2 v^2/4 (twice) and (g^2 + g'^2) v^2/4, for any normalised direction of v; rho = 1 follows. The lattice link propagator g^2/(qhat^2 + m^2) with qhat^2 = 4 sin^2(q/2) tends to g^2/m^2 at q = 0, with correction of order qhat^2/m^2, giving the contact coupling.

Lattice rate. The runner integrates the three-body phase space with the lattice dispersion E(k) = 2 |sin(k/2)| (vector norm) by Monte Carlo over the first momentum and one direction of the second, solving energy conservation for the second momentum's magnitude by bisection, with the V - A matrix element m E2 (E1 E3 - khat1 . khat3).

## Checks

The runner ends with `TOTAL: PASS=17 FAIL=0` in about 3 s. Exact checks:

- The abelian null space is one-dimensional, 6Y = [1, -4, 2, -3, 6, 0, 3]; every mass bilinear carries |Y| = 1/2.
- Frozen H at 20 random vacuum values: unbroken electroweak dimension 1 in every case (12 linked generators reduce to 9, 3 massive).
- Q = T3 + Y annihilates v = (0, 1); charges 0, -1, 2/3, -1/3.
- Link spectrum {0, mW^2, mW^2, mZ^2} at 20 random (g, g', v, direction); max |rho - 1| = 2.2e-16.
- G_F - 1/(sqrt2 v^2) simplifies to 0 (sympy).

Finite diagnostic (supplied lattice-cone model, 200000 Monte Carlo samples, common random numbers): Gamma/(G^2 m^5/(192 pi^3)) = 0.9995 +- 0.0067, 0.9995 +- 0.0067, 1.0000 +- 0.0066, 1.0026 +- 0.0065, 1.0095 +- 0.0063 at m a = 0.01, 0.02, 0.1, 0.3, 0.6. The exponent d ln Gamma/d ln m between m a = 0.01 and 0.02 is 5.00002. Relative to m a = 0.01 on the same samples, the lattice correction is +0.0005, +0.0031, +0.0099 at m a = 0.1, 0.3, 0.6. The statistical error of each absolute coefficient is about 0.7%, so the 1% agreement of the central values is at the level of the sampling.

## Estimates against measurement

All of these are estimates with supplied inputs (alpha(MZ) = 1/127.951, sin^2 theta_W = 0.23122, G_F, PDG masses and lifetimes):

- v = 246.22 GeV, set by G_F. Tree-level mW = 80.23 GeV against 80.369 and mZ = 91.51 GeV against 91.188, both within 0.5%.
- The tau lifetime from the muon lifetime by the fifth power of the mass and one coupling, with the supplied electronic branching 0.1782: 291.1 fs against 290.3 fs.
- The neutron lifetime with supplied V_ud = 0.97373, g_A = 1.2754, phase-space factor 1.6887 and radiative factor 1.0390: 880 s against 878.4 s.
- The charged pion lifetime with supplied f_pi = 0.1302 GeV and no radiative correction: 26.64 ns against 26.03 ns.
- The V - A helicity suppression of the pion's electron channel: Gamma(e)/Gamma(mu) = 1.2834e-4 at tree level against the measured 1.2327e-4 (within 5%).

If the masses were fixed coefficients, item 2 says no charged current is linked, and the muon, tau, charged pion and neutron would be exactly stable, against measured lifetimes of 2.2 us, 290 fs, 26 ns and 878 s. That is the measured reason to prefer the mass-field reading; it is a comparison, not a derivation.

## Boundary

Supplied: the chiral content of one family, the term list (including the four-mode term on n and u d d n), the mass field H as a field the response law sets, its vacuum value v, the couplings g and g', colour as the 8 extra generators, V_ud, g_A, f_pi, the radiative and phase-space factors, the lattice-cone dispersion and the contact limit. Forced, given those: the hypercharges, the doublet representation of H, one unbroken abelian link Q = T3 + Y, rho = 1 at tree level, a universal G_F = 1/(sqrt2 v^2), V - A structure and the m^5 rate law. Not claimed: that the register's update contains the mass field (it does not yet appear in the update or response law), the chiral content, the size of v, any scalar mode or its mass, radiative corrections, or an absence of a right-handed W beyond the statement that none is linked with this content. The lattice-rate result is a sampled finite diagnostic of a supplied model, not a theorem about the register's tick.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records; they fix none of the inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the response law's rule that links follow symmetries of the update with response-set fields transformed. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/masses_read_from_a_response_set_field_force_a_hypercharge_half_doublet_and_universal_v_minus_a_decays_2026_10_22.py
```

Needs numpy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 3 s, prints about 2.4 kB and ends with `TOTAL: PASS=17 FAIL=0`.
