---
claim_id: a_frozen_fold_needs_a_frustrated_preference_the_laws_lack_and_a_handed_texture_feeds_the_families_only_once_it_keeps_no_screw_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For handed neighbourhood configurations (folds, helices, screws) of edge or link registers as candidate sources of the family term that the mass no-gos ask for: exactly, if the up and down family terms share a unitary whose eigenspaces on the light family space have sizes d_i, |V| has at least n^2 - sum d_i^2 zeros, and an eigenspace of size 1 gives an entry 1 (50 seeded pairs per size set). CL-3's hinge sum is stationary at zero deficit, which flat edges meet, so CL-1..CL-3 contain no frustrated local preference (law text). With a supplied frustrated preference (all-regular tetrahedra; 2 pi / arccos(1/3) = 5.104), the range-3 rule 'each new site bonds to the newest three' holds for exactly one of 3^9 face-sharing chains: the Boerdijk-Coxeter helix, a screw turning arccos(-2/3) = 131.81 deg (irrational) and rising 1/sqrt10 per site. Its sense is the seed's orientation, and a mirrored seed gives the other sense. A longer contact rule has 24 best chains of 9252 (no single funnel). A Z_6 register chain with a mirror-even frustrated preference has helical classical minima of both senses and a mirror-even quantum vacuum with equal odds of each sense; the tunnelling splitting falls from 0.0278 to 0.0031 over 4-6 sites. On the copy-massed two-tiling tick (6^3 sites), I U(h) I^-1 = U(-h) and sigma_d maps h to -h, so the two senses have equal vacuum quasi-energy with or without the polar term. The bare sea's energy rises for helix and unhanded strain alike, equal at order a^2, and CL-3's vacuum standard removes the sea's share anyway; the helical strain has TT fraction 1/3. The commensurate helix keeps the screw T(2 e_x) C3 (light-space multiplicities 3, 2, 1: unit |V| entry, 22 zeros), so does helix + polar split; the triple helix keeps C3 (unit entry); the unhanded wave keeps I (16 zeros); only a distorted helix gives no zero, no unit entry (max |V| 0.99985) and J = 3.2e-6 at a = 0.3. Family quasi-energy ratios are 0.35 and 0.57, set by the band. A time-even handed background enters Dirac fields as b0 gamma5, which shifts the helicities without removing one. Supplied model, finite diagnostic: the frustrated preferences and contact rules, the clock register and its couplings, the texture forms and amplitudes, the polar stand-in, eps = 0.5, mu = 0.20 / 0.35, M = 0.6, the light-state selection and the measured values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_frozen_fold_needs_a_frustrated_preference_the_laws_lack_and_a_handed_texture_feeds_the_families_only_once_it_keeps_no_screw_2026_10_22.py
---

# A frozen fold needs a frustrated preference the laws lack, and a handed texture feeds the families only once it keeps no screw

Claim type: bounded_theorem.
Primary runner: `scripts/a_frozen_fold_needs_a_frustrated_preference_the_laws_lack_and_a_handed_texture_feeds_the_families_only_once_it_keeps_no_screw_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Today's family no-gos (`record-arrow-family-phase`, `mass-tower-law`, `family-charge-search`) ask for a bulk family structure that is polar and odd under A = sigma_d K, with at least two hop ranges. Candidates are a time-odd family current, or a mirror-odd, time-even chiral texture together with the polar split term. This note tests whether a handed neighbourhood configuration that the laws can form on their own supplies one. The main test case is a protein-like fold: a frustrated local preference that forces a twist. The note asks what picks the twist sense, and what a handed texture does to the mixing matrix. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs. Every check passes. Several PASS lines record that a candidate fails.

## Statement

A. The mixing lemma (exact).

1. Suppose the up and down family terms commute with one unitary G whose eigenspaces on the light family space have sizes d_i. Then V is block diagonal, with at least n^2 - sum d_i^2 zero entries. An eigenspace of size 1 is a common eigenvector, so |V| has an entry 1 (50 seeded pairs for each of the size sets (1,2), (3,2,1) and (4,2)). Translations, inversion I, the turn C3 about the family axis and any screw built from them are all such unitaries. The measured |V| has no zero entry and no entry equal to 1. So a structure that both sectors share must leave no unitary acting on the light family space with two distinct eigenvalues. This generalises the inversion item of `record-arrow-family-phase` and the translation item of `mass-tower-law`.

B. The protein-fold test.

2. The laws hold no frustrated preference. CL-3's hinge sum is stationary at zero deficit, and flat edges meet zero deficit in every cell. Matter's vacuum share is subtracted (item 9), and links respond only to departures from the vacuum. So nothing in CL-1..CL-3 is a local rule that the flat arrangement fails, as a protein's preferred bond angle is. This is stated from the law text.
3. A supplied frustrated preference. Suppose edge registers preferred regular tetrahedra. The block cube's central tetrahedron is regular, but its four corner tetrahedra are not. The regular dihedral angle arccos(1/3) goes 5.104 times into 2 pi, so regular tetrahedra cannot close around an edge (exact). This is the frustration of polytetrahedral order in flat space.
4. The fold (exact enumeration). Among the 3^9 face-sharing chains of 10 regular tetrahedra, exactly one satisfies the range-3 rule "each new site bonds to the newest three". That chain is the Boerdijk-Coxeter helix, with one sense throughout. A mirrored seed folds the other sense with the same score. So the sense is the orientation of the seed, as an amino acid's handedness fixes the alpha helix's sense. Without that rule there is no single funnel. The preference alone leaves 9252 non-overlapping folds, and a longer contact rule (most i -> i+5 contacts) has 24 best chains, all helical for four steps and then branching.
5. The fold is a screw. Each site turns by arccos(-2/3) = 131.81 degrees and rises by 1/sqrt10 edge. Since cos is rational and not 0, +-1/2 or +-1, the turn is an irrational part of a circle (Niven), so the fold has no lattice period.
6. A register version. Take a chain of Z_6 clock registers with the mirror-even frustrated preference -cos(d1) + 0.5 cos(d2) and value hops t = 0.1. Its classical minima are helices of both senses (no minimum has chirality 0 at 6 sites). The quantum vacuum commutes with the mirror, has chirality expectation 0 and gives each sense the same odds (0.4541, 0.4889, 0.4983 at 4, 5, 6 sites). The mirror-even/odd splitting, which is the tunnelling between senses, falls 0.0278 -> 0.0136 -> 0.0031. So the sense is chosen spontaneously in the long-chain limit. The only local term that picks a sense is sum sin(d1), the Dzyaloshinskii-Moriya form. It is odd under the mirror, so a mirror-keeping law cannot contain it.

C. The matter sea (exact on the model, 6^3 sites, copy-massed two-tiling tick).

7. Textures are hop-weight (edge) strains with the cube hop's normalisation kept: w_i^2 = (1 + a sin(phi - 2 pi i h / 3))/3, with phi = (pi/3) times the sum of the cube-centre coordinates. This is a traceless strain whose stretched axis turns about (1,1,1) with sense h and pitch 3 cubes. I U(h) I^-1 = U(-h) exactly (3e-16). The diagonal mirror maps the h helix to the -h helix shifted by one cube, so A, the texture being real, does the same.
8. The two senses have equal vacuum quasi-energy, both without and with the C3v polar term. The polar term breaks I but keeps A.
9. Driving. At equal rms strain, the helix and an unhanded linear wave cost the same at order a^2. Their cross term is the mirror-odd Lifshitz term, and the energies first differ at higher order (relative 0.7% at a = 0.1, 2.1% at a = 0.2; finite diagnostic). The bare sea's energy rises for both (6.4e-4 per tick at a = 0.1), so there is no instability. CL-3 subtracts the vacuum phase of the same edges anyway, so the sea adds nothing at any texture. The helical strain has no linear scalar curvature (q_i q_j h_ij = 0), but its TT fraction is 1/3, which the hinge sum's static energy charges positively. The flat vacuum is the minimum.

D. The family term (exact symmetry, finite values). Up has mu = 0.20 and down has mu = 0.35, with eps = 0.5, M = 0.6 and a = 0.3. Six light family states (two per family, at the lowest positive band at each family momentum) come from the untextured tick at mu = 0.275 and are shared by both sectors.

10. The commensurate helix is a screw. T(2 e_x) C3, with a gauge sign (-1)^(xy + xz), commutes with its tick exactly. On the light space its eigenvalues have multiplicities 3, 2 and 1. By item 1 this gives a unit entry and 22 zeros, which the runner confirms. Adding the polar split keeps the screw, with the same result. The triple helix (pitch 3 along x, y and z) keeps the pure turn C3 and gives a unit entry. The unhanded wave keeps I and has 16 zeros. So a perfect helix fails even though it is odd under I and A.
11. A distorted helix (the helix plus a 0.15 linear wave) keeps no screw, turn, I or A. It gives no zero and no unit entry (max |V| 0.99985) and max |J| = 3.2e-6. The needed structure is therefore a low-symmetry handed texture, which no law selects.

E. Weak chirality (exact, continuum).

12. A time-even handed background reaches a Dirac field as b0 gamma5 (P-odd, T-even). Then E = +-sqrt(m^2 + (|p| +- b0)^2), and both helicities are present at every momentum (20 seeded momenta). This is a helicity shift, not a missing partner. CL-1's finite-range tick stays vector-like with any static texture (register, chirality theorems). So a fold's handedness is not weak chirality, and the two walls do not unify this way.

## Estimates against measurement

- The family quasi-energies at a = 0.3 are up (0.545, 0.525, 0.515, 0.493, 0.195, 0.193) and down (0.604, ..., 0.342) rad per tick. Smallest/largest is 0.35 (up) and 0.57 (down). They are set by the band at the three family momenta, not by the texture. Measured values are m_u/m_t = 1.3e-5 and m_d/m_b = 1.1e-3, so the model gives no hierarchy.
- The distorted helix's J = 3.2e-6 and the entries of 1 - |V| (about 1e-4) scale with the supplied amplitude and with mu_d - mu_u. The model has no measured size; matching J = 3.1e-5 would be a fit.
- If the sense were chosen spontaneously per domain, neighbouring domains would disagree. The family phase would flip sign between domains: J would average to zero over many domains, and wherever the texture's symmetry is restored there would be unit entries. Measured CKM CP violation is one sign everywhere tested. So a spontaneous sense needs one domain at least the size of the observable universe, or an inherited bias.
- An inherited bias: the polar split keeps A and the tick order is a frame (`record-arrow-family-phase`), so neither picks a sense (item 8). Weak chirality is not in CL-1..CL-3. If it were added, a sense bias would be the analogue of the molecular parity-violating energy difference, a loop effect of the weak interaction. Its size at the edge rung is not estimated here.

## Speculation (no check)

- The fold's turn is 0.36614 of a circle. Its multiples come within 0.0053 (n = 10) and 0.0105 (n = 20) of a family character (1/3 or 2/3). An incommensurate fold has no exact family hop on the lattice. A near-commensurate one would hop only at the orders where n times the turn nears a character, and that would give a staged ladder of scales. That ladder would be set by the turn's continued fraction under a supplied preference. It is not derived here.
- Zoom ladder. A fold of folds (a coiled coil) would need a frustrated preference at every rung. CL-1..CL-3 supply none, so a staged secondary structure along the ladder is not available from the laws.

## What measured reality asks for instead

Three requirements follow from items 1, 10 and 11. The family structure must be odd under I and A. It must also leave no shared unitary with two distinct eigenvalues on the light family space, so it must keep no screw, no turn and no translation that acts on families. And it must have a definite sense over the observed universe. A perfect fold fails the second requirement, and a spontaneously chosen sense fails the third unless one domain covers the observed universe. So the replacement rule needs a law-level frustrated preference with a sense-selecting (mirror-odd) local term, or a sense inherited from a chiral ingredient that is not yet in the laws. The law also needs a mechanism that leaves the fold low-symmetric (for example incommensurate packing) rather than a perfect screw.

## Candidate law text (not adopted) and smuggling check

> "Fold. Edge registers prefer the regular tetrahedron of their block's triangulation, and each newly split block's edges bond to those of the three blocks split just before it along its split front."

Smuggling check. The text uses no measured number, but it smuggles in three things. The first is the preference itself, which is not in CL-3; CL-3 prefers zero deficit, and the two conflict. The second is an ordering ("split just before"), which the register's simultaneous splits lack. The third is the sense, which the text still does not fix, so the sense comes from the seed. The candidate is mirror-blind, so by item 6 it gives both senses equal odds. By item 10, wherever it is commensurate it forms a screw that blocks mixing. It is recorded as the protein analogue, not as a working rule.

## Boundary

Not claimed:
- link registers as quantum dynamics in 3D (the register chain is a 1D clock model);
- a Regge computation of the helical strain (the TT positivity is the continuum linearised statement);
- the BC fold placed on the cubic lattice;
- a proof that the higher-order helix-linear difference has a fixed sign;
- weak-chirality bias sizes;
- any physical family masses or mixings;
- spin-doubled light states beyond the six used.

## Supplied vs forced

Forced: the mixing lemma; that CL-3 holds no frustrated preference; the regular-tetrahedron frustration; the unique newest-three fold and its seed-set sense; the irrational turn; the mirror-even register vacuum with equal odds and the mirror-odd DM term; I and the mirror flipping the sense; equal quasi-energies of the two senses; the vanishing order-a^2 cross term; CL-3's subtraction; the screw and turn symmetries and their multiplicities; the b0 gamma5 helicity shift.

Supplied: the regular-tetrahedron preference, the contact rules, the clock register (Z_6, J2 = 0.5, t = 0.1), the texture forms and amplitudes, the polar stand-in, eps, mu_u, mu_d and M, the light-state choice, b0 and m, and the measured values.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1 tick, copy mass, edge registers, polar split; CL-2 actuality; CL-3 vacuum standard and hinge sum.
- Context: today's `record-arrow-family-phase`, `mass-tower-law` and `family-charge-search` drafts. The main note `DYNAMICS_CLAUSE_MORIYA_HANDEDNESS_IS_A_TWIST_WITH_CURVATURE_GAUGED_ALONG_A_LINE_NOT_IN_THREE_DIMENSIONS_AND_SEEN_IN_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-24.md` (a supplied DM coupling) is consistent with this note: the DM form is the one sense-picking term, and a mirror-keeping law excludes it. The main note `ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md` (handed rule terms are admissible, and the lowest soldered one is a lattice curl) shows that a handed law term would be allowed but not forced.

## How to run

```
python3 scripts/a_frozen_fold_needs_a_frustrated_preference_the_laws_lack_and_a_handed_texture_feeds_the_families_only_once_it_keeps_no_screw_2026_10_22.py
```

Seeded (20261022), runtime about 5 s, peak memory about 135 MB, AUDIT_TIMEOUT_SEC = 120, output 5.6 kB. Expected: TOTAL: PASS=15 FAIL=0.
