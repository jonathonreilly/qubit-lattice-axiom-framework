---
claim_id: link_register_split_transport_and_response_give_a_covariant_level_matched_zoom_map_born_exponential_decay_and_the_maxwell_limit_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For link registers under the three-law register: (split) a block's child Gauss laws sum to the parent's exactly when each parent electric value is the total of the four child bonds crossing its face, and in a 2+1D Z_3 toy (2x1 parent torus, 4x2 children) the passing 'face totals = parent values, the rest in the children's vacuum of the same flux sector' is an isometry; the nearest vacuum-carrying isometry is covariant but heats excited levels, and a level-matched polar map (vacuum to vacuum, each sector's levels onto the children's lowest levels) exists and is gauge-, winding- and translation-covariant. (Transport) In two-configuration blocks a transport cost that charges any change makes the actual configuration's survival equal the Born probability whenever it falls; in a supplied emitter plus link-chain model the actual waiting times are exponential with fitted rate / Wigner-Weisskopf rate = 1.0112 (finite diagnostic), and counting changes of electric values, not occupations only, keeps a stationary register state's actual configuration fixed. (Response) The plaquette phase's quadratic part has exactly two photon polarisations per momentum; the half-tick pair is symplectic with the free photon dispersion, on the edge cone when c_E c_B = 1 (supplied); Gauss's law with static charges gives the lattice Coulomb law; measured from the vacuum on the same edges the zero-point subtracts to zero at every configuration and a one-photon register sources exactly hbar omega with traceless null-dust edge response. Toy sizes, single-quantum truncation and supplied couplings; no continuum limit of the register is computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/link_register_split_transport_and_response_give_a_covariant_level_matched_zoom_map_born_exponential_decay_and_the_maxwell_limit_2026_10_22.py
---

# Link-register split, transport and response give a covariant level-matched zoom map, Born exponential decay and the Maxwell limit

Claim type: bounded_theorem.
Primary runner: `scripts/link_register_split_transport_and_response_give_a_covariant_level_matched_zoom_map_born_exponential_decay_and_the_maxwell_limit_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) gives each bond a link register; its actuality law (CL-2) moves one actual configuration by the fewest-change, Born-preserving transport and keeps records; its response law (CL-3) is the vacuum standard, under which edges and links respond only to departures from the vacuum of the same edges. This note tests three places where link registers meet those laws: how a coarse link register passes to its children when a block splits, what the transport cost must count for link registers, and what the response law gives in the Maxwell limit. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the couplings used here.

## Statement

Split.

1. A block's eight child Gauss laws sum to the parent's Gauss law exactly when each parent bond's electric value is the total of the 4 child bonds crossing its face and the block charge is the children's total (R D_c = D_p S, an integer identity). The 12 bonds internal to each block are unconstrained by it.
2. In a 2+1D Z_3 toy (parent 2x1 torus, children 4x2 torus at half the spacing, with g_c^2 = g_p^2/2), plaquette loops and 2 windings parametrise every Gauss-law configuration once, and the Kogut-Susskind plaquette plus electric Hamiltonian is Hermitian on that space. The passing "face totals = parent values, everything else as in the children's vacuum of the same flux sector" is an isometry into the children's Gauss-law space.
3. The nearest isometry carrying the parent's vacuum onto the children's vacuum is V* = |Om_c><Om_p| + polar(Q_c P Q_p). It is gauge covariant (all states obey Gauss's law), conserves the electric winding sectors and commutes with translations (parent shift 1 against children shift 2): the polar part of a covariant map is covariant. It heats the vacuum by 0, while the bare passing does not.
4. Carrying the vacuum is not enough: V* sends the parent's excited levels mostly outside the children's 6 lowest levels per (flux, momentum) sector. The level-matched polar map, vacuum to vacuum and each sector's parent levels onto the children's lowest levels of the same sector, exists, is covariant, and leaves no weight above the matched window.

Transport.

5. In every two-configuration block, a cost that charges any change makes the transport plan unique: move exactly the shortfall. If the excited-level probability P_e falls at every half-tick, the actual configuration's survival in the excited level then equals the Born P_e(t) exactly.
6. If the cost counts occupation changes only, every move of a link quantum along a chain of link registers is free, and greatest entropy then flips the actual electric values at order one per tick even in a stationary register state. Counting changes of electric values restores the forced, current-sized motion.

Response.

7. On the bond lattice, the plaquette phase's quadratic part curl^T curl has, at each momentum k, eigenvalue 0 on the gauge (gradient) mode and lambda_k = sum_i 4 sin^2(k_i/2) on exactly two modes (two photon polarisations), and curl grad = 0.
8. The half-tick pair (electric plaquettes along the normal, then magnetic plaquettes) is a symplectic map with cos Omega = 1 - eps^2 c_E c_B lambda_k/2, so Omega/eps -> sqrt(c_E c_B) |k|: the free photon with speed sqrt(c_E c_B), with lattice corrections of order eps^2 k^2 and k^2. With the same coupling for both, c_E c_B = 1, the photon lies on the edge cone.
9. Gauss's law with static charges +-1 fixes the longitudinal electric values, E = -grad phi with lap phi = -q, as the least-energy solution; the register energy shifts by exactly -c_E G(R), and 4 pi R G(R) -> 1 isotropically: the Coulomb law with alpha = c_E/(4 pi) in the dressed-coupling unit.
10. Vacuum standard. An energy eigenstate's local energy is the same at every electric configuration, so the vacuum's zero-point (omega/2 per mode, for any edges) subtracts to 0 at every actual configuration, and a one-photon register sources exactly hbar omega. Since omega_k(edges) is homogeneous of degree -1 in the edge lengths, the edge response is traceless, T^ij = omega n^i n^j (null dust).

## Derivation

Item 1: R sums child charges into blocks and S sums the child bonds crossing each block face; R D_c = D_p S holds because divergence contributions of internal bonds cancel inside each block. Items 2-4: configurations are enumerated in the Z_3 Gauss-law space; the passing is a column-normalised map with disjoint face totals, so it is an isometry; V* is the polar factor of the passing restricted to the complement of the vacua, which is the nearest isometry to it with the vacuum constraint; any map built from covariant pieces by a polar decomposition is covariant, since the polar factor of a map that commutes with a unitary also commutes with it. The level-matched map applies the same polar step sector by sector onto the children's lowest levels. Item 5: in a two-configuration block with odds p0 -> p1, the only plan that preserves the distribution and charges any change moves the shortfall |p1 - p0| and nothing else; the survival product then telescopes to P_e(t) when P_e decreases monotonically. Item 6: with occupation-only cost, moving a quantum between link registers changes no occupation, so the entropic plan (product of odds) applies. Items 7-8: Fourier transform of the plaquette curl; the half-tick pair is a product of two shears. Item 9: the least electric energy under Gauss's law is (1/2) q^T (D D^T)^+ q, attained at E = -grad phi. Item 10: in the electric-value basis the local energy (H psi)/psi of an eigenstate is its eigenvalue at every configuration; the vacuum's is omega/2 and a one-photon state's is 3 omega/2; omega_k = |(2/a) sin(k/2)| scales as 1/a.

## Checks

The runner ends with `TOTAL: PASS=14 FAIL=0` in about 1.5 s. Exact or machine-precision checks:

- Block identity on a 3^3 -> 6^3 torus: max |R D_c - D_p S| = 0.0, 4 child bonds per face.
- Z_3 toy: parent Gauss-law space dimension 27, children 19683, unique parametrisation and Hermitian Hamiltonian. Passing: min column weight 3.279e-01, ||P^T P - 1|| ~ 4e-15.
- V*: vacuum heating 0 to machine precision (bare passing 0.9971); all 20 random perturbed vacuum-carrying isometries lie farther from the passing; cross-sector weight ~ 1e-16, ||T_c V* - V* T_p|| ~ 1e-16.
- Level-matched map: weight outside the matched window ~ 1e-15 against 0.48 for V*; translation residual 0.0. Mean |excess energy| of excited levels: passing 3.32, V* 3.36. Parent gap 0.227, children gap 0.002 at parent coupling g_p^2 = 1.5.
- Photon modes on a 4^3 torus (192 links): eigenvalue deviation 1.8e-14, curl grad = 0 exactly. Half-tick map at eps = 0.2, c_E = 1.3, c_B = 1/1.3: symplectic, quasi-energy deviation 1.5e-08.
- Gauss least-energy identity on a 6^3 torus (exact). Coulomb coefficient 4 pi dG/d(1/R) over R .. 2R on a 64^3 torus, with the torus background term r^2/(6 L^3) removed: along an axis 1.013, 1.004, 0.996 at R = 6, 8, 10; along the diagonal 0.989, 0.995 at R = 3 sqrt3, 4 sqrt3.
- Vacuum standard (one mode, 60 levels, k = (0.07, 0.04, 0.02)): one-photon departure / omega - 1 = 2.0e-12; sum_i d omega/d ln a_i + omega = -2.7e-12; max |T^ii/omega - n_i^2| = 6.1e-05 (finite-difference step).

Finite diagnostics (supplied model, finite diagnostic, no physical identification): an excited emitter coupled with g = 0.15 to the end of a chain of 420 link registers with hop J = 1, truncated to one quantum, under block half-ticks with dt = 0.05; Gamma_WW = 2 g^2/J.

- Survival of the actual configuration equals Born P_e: max |S - P_e| = 1.0e-14 over 3111 ticks, to t = 7.0/Gamma_WW, with P_e monotone. The uniqueness of the plan in item 5 is the argument above; the runner implements that plan.
- Fitted decay rate / Gamma_WW = 1.0112 over 1/Gamma < t < 6/Gamma. From 20000 sampled actual trajectories, max |S_emp - e^{-Gamma t}| = 0.004, and the end-time total-variation distance between the actual configurations and |psi|^2 on 20-link bins is 0.005.
- Electric-value jumps per tick on the chain: 0.0851 with the fewest-change cost counting electric values, 0.850 with occupation-only cost plus greatest entropy. For a Floquet eigenstate of a closed 24-link chain (stationary odds): actual jumps per tick 0.000 with the minimal plan against 0.850 with the entropic plan.

## Estimates against measurement

- Exponential decay: the measured hydrogen 2p decay is exponential with lifetime 1.60 ns (quoted, not computed); the diagnostic above gives exponential actual waiting times at the Wigner-Weisskopf rate in the supplied model.
- Zero-point: without the vacuum standard the register zero-point would source about (1/2)<omega_k> per cell, 1.21 per link-cell in lattice units on 4^3, of order one Planck density against the measured rho_Lambda ~ 1e-123 in Planck units. The runner prints the 1.21 and asserts the comparison with check(True); it is stated, not computed. The subtraction also removes the zero-point's edge derivative, so the response law must count the plaquette phase from the links' vacuum on the same edges.

## Boundary

Supplied: the Z_3 truncation, the 2+1D toy torus sizes, the coupling g_p^2 and its child value g_p^2/2, the 6-level matched window, the emitter coupling g, chain hop J, step dt, single-quantum truncation, c_E and c_B (and c_E c_B = 1 for the edge cone), and the edge dispersion omega_k = |(2/a) sin(k/2)|. Forced, given those: the face-total split rule, the isometry and covariance of the passing and polar maps, the need for level matching, Born survival under a change-charging cost, the need to count electric-value changes, two photon polarisations, the photon dispersion, the Coulomb law, zero vacuum departure and a traceless one-photon source. Not claimed: that the level-matched map is unique or is the register's split rule, any statement beyond the toy sizes for the split, exponential decay beyond the supplied single-quantum model, the value of c_E or of the fine-structure constant, interacting photons, or any continuum limit of the register.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): link registers in the update law, the fewest-change Born-preserving transport of the actuality law, and the vacuum standard of the response law. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/link_register_split_transport_and_response_give_a_covariant_level_matched_zoom_map_born_exponential_decay_and_the_maxwell_limit_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 2 s with about 205 MB resident, prints about 5.4 kB and ends with `TOTAL: PASS=14 FAIL=0`. Several machine-zero residuals in the split section (for example the V* vacuum heating, 0.0e+00 or 1.8e-14) vary between runs because the sparse eigensolver's start vector is not seeded; every check is a tolerance bound and passes.
