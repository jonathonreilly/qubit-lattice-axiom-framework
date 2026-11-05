---
claim_id: label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's parallel-carriage circuit at zoom b, whose b^3 label copies of each block fermion are rotated by an exact U(b^3): gauge generators act as T x 1 and commute with all of U(b^3), so every label copy carries one whole linked family (checked at b = 2); on one chiral family the only link-free Weyl state is nu^c and the only gauge-invariant bilinear is the Majorana nu^c nu^c (hand-entered charge table), so a chiral label copy takes no label mass and heavy labels are vector-like; any quadratic label term keeps one exact U(1) per label-mass eigenspace (commutator 2e-15), which the links make a long-range force on matter; terms even in each label break label number but keep label parity (-1)^N_k, and one mixing bilinear breaks it (Fock toy, 2 labels x 3 modes), so label parity is a supplied choice. For the links: the spin-3/2 register's charge conjugation maps E to -E and U to U^dag (checked), the extra mode is stated C-odd with no selection rule against three-photon decay; the register raiser conserves each bond's rishon number (other link-spin sectors are superselected); on compact cubic links every cube's magnetic charge is an integer, the total is zero and 312 continuous-evolution events changed charges in +- pairs (monopole number locally conserved); on the six-edge block triangulation 48 registers per 8 block sites give two light roots at |K| = 0.05 and every other real root at least 1.49 per block tick, and the one-register hop conserves no edge number or parity. Estimates of label relics and monopoles against measurement use supplied inputs. Supplied model, finite diagnostic: label terms and label parity, effective couplings, the gravitational production yield, splittings, the cell unit, a cubic link lattice for the monopole count, the sync slab; many decay times and the conserved-number census are stated, not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.py
---

# Label copies carry linked families, and only a supplied label parity or magnetic charge stabilises a massive relic

Claim type: bounded_theorem.
Primary runner: `scripts/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its three laws (update CL-1, actuality CL-2, response CL-3) bring new structure that could carry dark matter: label copies of the block fermion at zoom b, site-bond link registers with an extra mode and rishon sectors, compact link angles with monopoles, and six-edge block registers. This note tests each against the measured dark matter (Omega_dm h^2 = 0.120, cold, sigma/m below about 1 cm^2/g, no direct-detection signal, stable for 13.8 Gyr) by asking which numbers the laws conserve. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Label copies at zoom b (label terms supplied).

1. The links read per coarse cube alike for every label: gauge generators act as T x 1 and commute with all of U(b^3). Every label copy carries one whole linked family.
2. In one chiral family the only link-free Weyl state is nu^c, and the only gauge-invariant bilinear is nu^c nu^c, a Majorana term that the Z4 of B - L forbids (stated from the register). A chiral label copy takes no label mass; heavy labels are vector-like.
3. Any quadratic label term keeps one exact U(1) per label-mass eigenspace. The update law links these numbers to the gauge fields, so the light label's number would be a massless long-range force on matter. The runner states the MICROSCOPE bound (below about 1e-25) against which this is excluded; it does not compute the force.
4. Terms even in each label break label number (no dark link) but keep label parity (-1)^N_k; one mixing bilinear breaks it. The fine tick has trivial cell commutant (cited from an earlier hidden-sector computation), so label parity is not in the fine tick: it is a supplied choice. With parity supplied, the lightest odd state N' (label nu^c) is exactly stable and link-free; the runner states, without computing, a lifetime of about 1e-39 s if parity is broken by mixing.

B. Link registers.

5. For the spin-3/2 register, charge conjugation C (m -> -m) maps E -> -E and U -> U^dag and keeps ring exchange, so n photons have C = (-1)^n. The extra d1 d2 d3 mode is stated to be C-odd and trivial under the kept turns, so three-photon decay is allowed and no selection rule protects it. Its lifetime at the cell scale, about 1e-41 s, is stated, not computed: not dark matter.
6. The register raiser (the rishon hop between a bond's two ends, 2S = 2) conserves the bond's total rishon number while changing each end's. Other link-spin sectors are superselected and never occur; they are not a relic.
7. On compact link angles (a cubic lattice, supplied) every cube's magnetic charge, the reduced plaquette flux divided by 2 pi, is an integer and the total is zero. Continuous evolution changes charges only in +- pairs: monopole number is locally conserved and a lone monopole is stable. Monopoles are magnetically charged, so they are not dark.

C. Edge registers on the six-edge block triangulation (sync slab, fixed lapse, zero shift).

8. There are 48 registers per 8 block sites, 6 per site, the metric count, so no non-metric light strain exists. At |K| = 0.05 the light roots are the two tensor polarisations on the edge cone, and every other real root is at the cell scale.
9. The one-register hop V_e + V_e^dag changes every edge value by +-1 and anticommutes with (-1)^n: no edge-register number or parity is conserved. With crystal momentum alone, and threshold zero at K = 0 (back-to-back massless pairs), massive edge quanta near K = 0 are open to decay. Near-zero transfer roots at generic K are ill-conditioned (Jordan blocks of the gauge zeros), so a kinematically closed band minimum near the zone edge is not excluded here.

D. Conserved numbers as stabilisers (a census stated, not computed).

10. Exact U(b^3) must be broken (LEP), and quadratic terms leave linked U(1)s. Label parity is not in the fine tick. The Z4 of B - L makes the light neutrino the lightest carrier, which is hot and below 1% of dark matter (sum m_nu below 0.07 eV). Rishon number is superselected. Only zero static charge occurs in the Gauss sectors. Magnetic charge is exact but not dark. Edge value, copy sign and turn charges are not conserved; crystal momentum and pattern are not particle charges. The dark constant has zero mean in every cube under the response law, so it has no carrier. Only label parity (supplied) and magnetic charge (not dark) stabilise a massive relic.

## Derivation

Item 1 checks [T x 1, 1 x U] = 0 for a random 3 x 3 Hermitian T and a random U(8) at b = 2. Item 2 scans a hand-entered table of one family's SU(3), SU(2) and hypercharge assignments for neutral states and singlet bilinears. Item 3 checks that the projectors onto each eigenvector of a random 8 x 8 label mass commute with H = H_c x 1 + 1 x M. Item 4 builds six Jordan-Wigner modes, adds intra-label hops, intra-label pair terms and a cross-label term even in each label, and tests commutation with label parity and label number, then adds a mixing bilinear. Item 5 checks C Sz C = -Sz and C S+ C = S+^T for S = 3/2. Item 6 checks commutation of the rishon hop with total and one-end rishon number. Item 7 draws random compact angles on a 5^3 lattice, computes the cube charges, and follows 400 random small steps (width 0.02), counting charge-changing events. Items 8-9 build the sync slab's quadratic form on the six-edge triangulation (inlined from an earlier edge-register computation) and find its roots at |K| = 0.05 by a polynomial eigenproblem; the edge hop is checked on a four-level register.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- [T x 1, 1 x U] below 1e-12 (b = 2, 8 labels).
- Link-free state ['nu^c']; singlet bilinear [('nu^c', 'nu^c')].
- Label-mass eigenspace commutator 2e-15 (8 eigenspaces).
- Fock toy: label parity conserved below 1e-12 by even terms; label number broken (above 0.1); mixing at 1e-3 breaks parity (above 1e-4).
- Spin-3/2 C relations below 1e-12; rishon hop conserves the total, changes one end's (above 0.5).
- Compact links: integer charges to 1e-9, total 0, 312 events all in +- pairs; G(0) = 0.2498 on a 48^3 midpoint grid against Watson's 0.2527 (asserted within 3%).
- Edge hop anticommutes with (-1)^n below 1e-12.

Finite diagnostics (supplied model, finite diagnostic):
- Six-edge slab: 48 registers; light roots [0.05 0.05] at |K| = 0.05; every other real root at least 1.49 per block tick.

## Estimates against measurement

Estimates with supplied inputs (M_P = 1.221e19 GeV, reduced 2.435e18 GeV, the cell scale Lambda = M_P/sqrt(8 pi) for a = sqrt(8 pi) l_P, a cell-contact decay width with splittings dm = (1.4-5)e-3 m, alpha_eff = 0.03-0.3 with a coannihilation factor 0.1-10, a gravitational production yield Y = 1e-3 (T/M_P)^3 e^(-2m/T), r < 0.036, MACRO's 1.4e-16 /cm^2/s/sr at beta 1e-3):
- Coloured or charged label states reach N' only through cell-scale contacts: lifetime 4e+44 s at m = 10 TeV, far beyond the age; decay before BBN (1 s) needs m above 8.5e+12 to 3.0e+13 GeV.
- A thermal coannihilating label family gives Omega h^2 = 0.12 at m about 0.4 to 39 TeV; its stable coloured relics would then exceed heavy-isotope bounds by more than 1e16 (the abundances n/n_B above about 1e-12 against bounds below about 1e-28 are stated, not computed): excluded.
- Non-thermal window: the reheating temperature needed is T_reh/m = 0.42, 0.18, 0.11 at m = 1e13, 1e14, 1e15 GeV; T_reh < 5.8e+15 GeV (from r < 0.036) caps m below 1.0e+17 GeV; dlnY/dlnT = 8, 14, 22, so the abundance is tuned.
- N' couples by contact only: sigma_SI about m_n^2/(pi Lambda^4) = 3e-102 cm^2, no direct-detection signal; label masses at the cell scale give e^(-2 Lambda/T_max) = e^-842, so none are made after the start.
- Monopoles: M = (pi/2 alpha) G(0) Lambda = 1.3e+19 GeV at alpha = 0.071 (the S = 3/2 natural coupling), allowed dark-matter fraction below 3.6e-03; 1.9e+21 GeV at alpha = 5.0e-4 (a hypercharge-unit target), fraction below 5.1e-01. MACRO excludes monopoles as all of the dark matter at the natural coupling.
- Edge quanta: b_e = 6 gives m about 6.1e+17 GeV and lifetime about 2e-41 to 2e-39 s; b_e = 38 gives 9.6e+16 GeV and 4e-39 to 4e-37 s (universal coupling, N = 1 to 100 channels). Any closed band minimum would be cell-scale and made only at T about m/20 > T_max = 6e+15 GeV, or by splits, which carry vacuum to vacuum: no abundance from the rules.
- Conditional survivor: N' with a supplied label parity, m about 3e+13 to 1e+17 GeV, produced non-thermally; Omega is not set by the rules.

## Boundary

Not claimed: a derivation of label parity from the register (it is supplied); the dark-matter abundance; the extra link mode's lifetime, the mixing lifetime and the census of section D (stated, not computed); a closed band minimum of the edge registers near the zone edge (not excluded); monopole production; the hidden-sector commutant result (cited). The monopole count uses a cubic compact-link lattice, not the register's bcc link geometry.

## Supplied vs forced

Supplied: the label terms and label parity, alpha_eff, the production yield, the splittings, the cell unit a = sqrt(8 pi) l_P, the cubic link lattice, the sync slab with fixed lapse and zero shift, and the measured inputs. Forced, given those: the linked family per label; no label mass for a chiral copy; the linked U(1) per label-mass eigenspace; label parity under even terms and its breaking by mixing; the C action on the spin-3/2 register; rishon-number superselection; integer, locally conserved magnetic charge; six registers per site and the two light roots; no conserved edge number or parity.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's parallel-carriage circuit and label copies, the site-bond link registers and their raiser, the edge registers on block edges, the response law's zero-mean dark constant. Zero premise weight; results using it are conditional on it.
- Companion computation: EDGE_REGISTER_SET_CENSUS_CUBE_EDGES_ALONE_GIVE_NO_HINGE_SUM_AND_SIX_EDGES_PER_SITE_GIVE_TWO_TENSOR_POLARISATIONS_ON_THE_EDGE_CONE_BOUNDED_THEOREM_NOTE_2026-10-22 (the slab construction is inlined from its runner).

## How to run

```
python3 scripts/label_copies_carry_linked_families_and_only_a_supplied_label_parity_or_magnetic_charge_stabilises_a_massive_relic_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 70 MB resident, prints about 5.9 kB and ends with `TOTAL: PASS=14 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output.
