---
claim_id: the_link_registers_cannot_supply_the_cube_ticks_pi_faces_and_the_hop_phases_reduce_to_minus_one_around_every_unit_face_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Spinless half-filled nearest-neighbour cubic sea (hop 1) and the CL-1 two-tiling cube tick (eps = 0.3, 0.8, 1.2; Floquet vacuum = negative quasi-energies filled, proper units = quasi-energy per tick / N), Bloch supercells up to 16x8x1 and 8^3, classical (static) link values, CL-3 magnetic term (1/g^2)(1 - cos Phi) l/S per loop. (A) With CL-1's fixed hop phases removed, registers laid out by the Links clause (B_f-block faces, crossing odd hops dressed) put flux only on the fine faces at block-edge segments (1/B_f^2 per orientation); every even-cube and inter-cube face reads 0 at every register value, so R_even is the bare hop and the pi-flux sector is unreachable at any g^2, B_f. What they can reach (pi on every block-edge loop) lowers the sea by 0.0351 (B_f = 2) and 0.0049 (B_f = 4) per site; an isolated pi flux line binds 0.018 per unit length, so the zero-flux photon vacuum fails at n_m g^2 > ~2/(0.018 B_f^2) (10.7 and 4.8 computed at B_f = 2, 4; 0.15 at B_f = 27). With the fixed phases the same flux costs energy (0.049, 0.016 per site), so the current law keeps a zero-flux register vacuum at every g^2, B_f. (B) A register on every matter edge: R^2 = 1 fixes only the cube faces; among all 128 R^2 = 1 odd-cube fields on the 2^3 cell the energy falls with every inter-cube pi face and is least at pi on every face (static and eps = 0.8). Against the CL-3 term read from 1, zero flux wins until n_m g^2 = 31.4 (static; 32.1, 39.3, 56.7 at eps = 0.3, 0.8, 1.2), then pi on every face; no partial pattern ever wins. (C) The sea's own magnetic response about pi is diamagnetic and log-growing (c = 0.042 to 0.078 per delta^2 for delta = 2 pi/8 to 2 pi/48), paramagnetic about 0 (about -0.005): the matter's magnetic minimum is at pi. CL-3's term read from 1 gives the photon about pi stiffness n_m c - 1/(2g^2); read from the vacuum holonomy it gives 1/(2g^2) + n_m c > 0 at every g. No element of SU(3) x SU(2) x U(1)_Y acts as -1 on every measured multiplet, so pi can sit only in a factor acting alike on all modes (fermion parity). (D) 'Phase -1 around every unit face' is equivalent to {W_i, W_j} = 0 on every cube, hence R^2 = sum w_i^2 for any positive weights; CL-1's spin-3/2 field is gauge-equivalent to it on every face; the tick with mass angle and copy mass, the copy-sign spectrum, the Dirac point, the dressed tick and the rotation covariance (half-turns anticommute: the double cover) are identical. (E) A dynamical face register cannot be passed at pi per face (Stokes); a flipped link costs 0.37. Supplied: hop 1, half filling, eps, classical link values, n_m."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_link_registers_cannot_supply_the_cube_ticks_pi_faces_and_the_hop_phases_reduce_to_minus_one_around_every_unit_face_2026_10_22.py
---

# The link registers cannot supply the cube tick's pi faces, and the hop phases reduce to "minus one around every unit face"

Claim type: bounded_theorem. The candidate-law register has zero premise weight, and the axioms are unchanged.

CL-1 supplies the cube hop R with fixed phases: "the phase of their spin-3/2 overlap along the body diagonals, each site keeping one overlap state shared by its two cubes". The nested-prefold-sea and pi-flux-fold notes found that these phases are the pi-flux (Kogut-Susskind) field, and that the half-filled sea's energy prefers pi on every face (Lieb). This note tests whether the fixed phases can be removed and derived: the hop's phases become the link registers' plaquette phases, and the vacuum selects pi.

The questions are:
1. With the phases replaced by the matter-coupled link registers of the Links clause (odd hops dressed by V_y^dagger V_x), is the half-filled vacuum the pi-flux sector? The sea's kinetic energy favours pi; CL-3's magnetic term favours 0. Which wins as a function of g^2 and B_f?
2. Can a pi background carry ordinary photons as fluctuations about pi?
3. If pi wins, what is the simplified CL-1 text, and does anything else break (Dirac cones, the copy mass, the dressed-cone clause, the species angles, C3v)?
4. If 0 wins, what is the mismatch, and what extra would be needed?

Notation: n_m is the number of matter modes per site that a register dresses with unit charge. With one qubit per site, n_m = 1. Energies are per site, for hop 1 (static) or for the CL-1 tick in proper units.

## Results

### A. The existing Links layout (question 1)

**A1 [T+D]. Reach.** In the Links clause, the only hops dressed are those whose sites lie in different B_f-blocks. Blocks are made of whole even cubes, so only odd-cube hops cross, and those crossing one block face all carry that face's register.

A fine face therefore picks up register flux only if two of its edges cross different block faces, which happens only at a block-edge segment. That is 1/B_f^2 of the faces of each orientation, and all of them are odd-cube faces. Every even-cube face and every inter-cube face reads 0 at every register value. This was checked with random U(1) register values: at B_f = 2, 48 of 192 faces are nonzero, and at B_f = 4, 96 of 1536; in both cases every nonzero face is at a block edge, and the largest even or mixed flux is 0.

So with the fixed phases removed, R_even is the bare hop (spectrum +-sqrt3, +-1/sqrt3) and R^2 = 1 fails on every even cube at every register value. **The pi-flux sector is unreachable in the existing layout, whatever g^2 and B_f are.** No energetics can change this. It is a statement about where the registers sit.

**A2 [D]. What the registers can reach.** Take pi on every block-edge loop (the coarse Kogut-Susskind field) and weigh it against CL-3's magnetic cost. Per site that cost is 3/B_f^3 loops times 2/g^2 times l/S = 1/B_f, which is 6/(g^2 B_f^4).
- At B_f = 2 the sea gains 0.0351, so the threshold is n_m g_c^2 = 10.7. At B_f = 4 the gain is 0.0049 and the threshold is 4.8.
- An isolated pi flux line in the zero-flux sea binds. Its gain per unit length is 0.0142, 0.0191, 0.0182 and 0.0180 at line spacings 2, 4, 6 and 8, converging to lambda ~ 0.018.
- So the threshold falls as n_m g_c^2 ~ 2/(lambda B_f^2): 0.77 at B_f = 12 and 0.15 at B_f = 27.

Without the fixed phases, then, the photon registers' zero-flux vacuum is unstable at large B_f and natural couplings, and the vacuum becomes a crystal of pi flux lines. That would be a charge-dependent, anisotropic background seen by every charged species, against measured isotropy, and it still gives no fine Dirac cone.

**A3 [D]. The current law, for contrast.** On CL-1's pi background the same register flux costs energy: 0.0491 per site at B_f = 2 and 0.0161 at B_f = 4. A flux line costs 0.10 per unit length. So with the fixed phases the registers' vacuum is zero flux at every g^2 and B_f, and the fixed phases are what keep the photon vacuum at zero flux.

**A4 [D]. The CL-1 tick at finite step.** The ordering is the same at finite step. In proper units the full-pi gain is 0.187, 0.153 and 0.106 at eps = 0.3, 0.8 and 1.2, and the B_f = 2 register gain is 0.036, 0.037 and 0.076.

### B. A register on every matter edge (a new carrier; question 1)

**B1 [D]. R^2 = 1 leaves the inter-cube faces to the sea.** R^2 = 1 fixes the cube faces of both tilings to -1. That is 1.5 faces per site, and it leaves the 12 inter-cube faces per 2^3 cell free.

Fix the even cube and run over all 128 odd-cube sign fields with R^2 = 1. They fall into classes with 0, 4, 6, 8 or 12 inter-cube pi faces. The energy within a class is degenerate, and it falls with every inter-cube pi face:

| Inter-cube pi faces | Static | eps = 0.8 |
|---|---|---|
| 0 | -0.99643 | -1.0891 |
| 4 | -1.07969 | -1.1633 |
| 6 | -1.09512 | -1.1745 |
| 8 | -1.14110 | -1.2159 |
| 12 | -1.19381 | -1.2599 |

The least is pi on every face, the Kogut-Susskind class. R^2 = 1 with every inter-cube face at 0 lies above even the zero-flux sea (-1.00243), so R^2 = 1 alone does not give the Dirac sea; the inter-cube faces must also be pi. This sharpens the main notes' global statement (pi on every face is the U(1) minimum) to the R^2 = 1 subfamily.

**B2 [D]. Who wins against CL-3's magnetic term.** Use (1/g^2)(1 - cos) per fine face, so 2/g^2 per pi face. Over the patterns zero, odd faces only, xy layers and the five R^2 = 1 classes, the lower envelope in x = n_m g^2 is:
- zero flux up to x = 6/0.191 = 31.4, the runner's envelope switching at 31.5;
- pi on every face beyond that;
- no partial pattern wins anywhere.

At finite step the threshold is 6/gain: 32.1, 39.3 and 56.7 at eps = 0.3, 0.8 and 1.2. In alpha = g^2/(4 pi) this is alpha_c = 2.5/n_m.

**B3 [E]. Strong coupling.** Two estimates, not run:
- At the threshold the electric term g^2/2 per unit of electric value is not small. With n_m = 1 it is at least about 16, so the selected flux need not be sharp. A deconfined compact U(1) needs g^2 of about 1 or less (Wilson critical beta about 1), which is incompatible with n_m g^2 > 31 at n_m = 1.
- Below threshold, zero flux is not strictly a minimum. The nesting log of pi-flux-fold A4 (E - E0 ~ -0.029 Phi^2 ln(1/Phi) along the nesting path) gives a flux Phi* ~ exp(-1.5/(0.029 n_m g^2)), which is e^-52 at n_m g^2 = 1 and negligible.

### C. The photon about the vacuum (question 2)

**C1 [D]. The sea's own magnetic term has its minimum at pi.** Apply a uniform field delta = 2 pi/q per xy face on top of each background.
- About pi, c = dE/delta^2 = 0.0421, 0.0582, 0.0707 and 0.0775 at q = 8, 16, 32 and 48: positive (diamagnetic) and growing with ln(1/delta). This is the Dirac sea's vacuum polarisation, with a log slope of 0.018 still drifting down. The two-taste continuum value 1/(48 pi^2) = 0.0021 is not reached on these lattices, so the asymptotic coefficient is not established.
- About 0, c = -0.003 to -0.006, which is paramagnetic.

**C2 [T+D]. Two readings of the plaquette law.**
- Read from 1, as CL-3 now writes it (n - Re tr U), the term gives +1/(2g^2) per xy face about 0 but -1/(2g^2) about pi. A pi vacuum with ordinary photons then needs n_m c > 1/(2g^2), which means n_m g^2 > 11.9, 8.6, 7.1 and 6.4 at wavelengths q = 8, 16, 32 and 48. That is strong coupling again. The long-wavelength log helps only slowly.
- Read from the vacuum holonomy, n - Re tr(U_vac^dagger U), which is CL-3's vacuum-standard principle ("respond only to departures from the vacuum") applied to the loop, the term vanishes at whatever vacuum the sea selects. The self-consistent vacuum is then the sea's least-energy sector: pi, by B1 and the main notes. The photon stiffness is 1/(2g^2) + n_m c > 0 at every g, so the photon is an ordinary fluctuation about pi, with the matter's log adding to 1/g^2.

**C3 [T]. Which factor can carry pi.** An element (omega^k, +-1, e^(i theta Y)) acting as -1 on u_R and on d_R needs e^(i theta) = 1, and then it acts as +1 on e_R. So no element of SU(3) x SU(2) x U(1)_Y acts as -1 on every measured multiplet, with or without nu_R. The runner's scan finds min max |g + 1| = 1.618.

The pi face phase therefore cannot be the photon's register, or any measured register. It must sit in a factor that acts alike on every mode: fermion parity (Z2), or fermion number U(1)_F. A long-range U(1)_F photon is excluded by fifth-force bounds, so the factor would be Z2. Its excitations are visons, links flipped against the pi background; one costs 0.37 (E1), a heavy gapped defect.

### D. The simplified hop clause (question 3)

**D1 [T].** "Phase -1 around every face of a cube" is equivalent to {W_i, W_j} = 0 for i != j, which is equivalent to (sum w_i W_i)^2 = sum w_i^2 for any positive weights. So "scaled so that R^2 = 1" holds on every metric automatically. Checked at 2e-16 for random weights in a random gauge; one flipped link breaks it (0.67).

**D2 [T+D].** CL-1's spin-3/2-overlap field carries -1 on EVERY face of Z^3: both tilings' cube faces and the 12 inter-cube faces per cell (to 7e-15). So it is gauge-equivalent to the field "-1 around every unit face". The full tick, with mass angle mu = 0.1 and copy mass MN = 0.3 at eps = 0.3, has identical quasi-energies (9e-16), the same copy-sign spectrum (+-1, four each) and the Dirac point.

**D3 [T].** Every cube rotation maps the all-minus class to itself, so each rotation (90, 120 and 180 degrees checked) is a symmetry of R up to a site gauge. The compensated half-turns about z and x anticommute (commutator -1), which is the projective class of half-integer spin. Rotation covariance, the spin-3/2 character and the double cover become theorems of the clause; they are no longer written into it.

**D4 [T+D].** With the same random register values on the crossing odd hops (B_f = 2), the dressed tick is identical for the two fields (4e-15). Every CL-1 object depends on the hop phases only through face fluxes: R, s = i R_1 R_2 R_3 R, the V^q dressing and the plaquettes are all gauge-covariant. So the dressed-cone clause, each species' eps and mu (read from dressed cones), the copy mass (even cubes, read from undressed hops) and the split's C3v (read from edges and the nesting) are unchanged.

### E. Passing (question 3)

**E1 [T+D].** Children at pi read +1 around a parent face, by Stokes ((-1)^4). So a dynamical face register cannot be passed at pi per face (pi-flux-fold D1). Every split would seed visons costing 0.37 each (0.368 on 4^3 cells, 0.372 on 6^3), and the vacuum would have to re-form at every split.

The kinematic clause has nothing to pass. It fixes each rung's faces directly, and the passing already carries vacuum to vacuum.

## Verdict

**As posed, negative.** The fixed phases cannot be replaced by the existing link registers.
- The Links layout never dresses an even-cube or inter-cube hop (A1), so the pi sector is unreachable at any g^2 and B_f.
- Removing the phases also destabilises the existing photon registers' zero-flux vacuum into a pi flux-line crystal at large B_f (A2).
- With a new register on every matter edge and CL-3's term read from 1, zero flux (the photon vacuum) wins until n_m g^2 = 31.4 (alpha_c = 2.5/n_m; 32 to 57 at finite step). With n_m = 1 that is deep strong coupling, where the flux is not sharp (B3). At measured-scale couplings (g^2 ~ 0.1 to 0.5) the mismatch is a factor of 60 to 300 in n_m g^2.

**What would be needed.** Three extras together:
- (i) a new register on every matter edge, three per site, with a Gauss law per site, which means role-assigned qubits;
- (ii) the factor must be fermion parity Z2, by C3;
- (iii) the loop term read from the vacuum holonomy (C2), or no loop term for that factor at all.

With these, pi wins at every g, photons are ordinary fluctuations about pi, and visons are gapped. But this is more structure than the fixed phases, not less, and it fails at the split (E1).

**The simplification that works is kinematic.** R^2 = 1 forces -1 on every cube face (D1, and the main note's Cauchy-Schwarz theorem), and the sea's energy forces -1 on the inter-cube faces (B1). So the spin-3/2 construction can be replaced by one symmetric condition with a stated reason, and everything else follows (D2-D4).

## Candidate law text (recommended)

> CL-1, hop sentence. "Let W_i pass each site's odds to its edge neighbour along axis i with a phase, the phases multiplying to -1 around every unit face. The cube's hop R is a sum of the W_i with positive weights, sqrt(gamma^ii) when gamma^ij is diagonal, scaled so that R^2 = 1 wherever none of the cube's registers is at an extreme value, and its step is eps0."

What is removed:
- "the phase of their spin-3/2 overlap along the body diagonals";
- "each site keeping one overlap state shared by its two cubes".

What becomes derived:
- the spin-3/2 character and the double cover (D3);
- R^2 = sum w_i^2 for every metric (D1);
- the Dirac sea (D2).

The reason for -1, for the owner's "a choice needs a reason":
- It is the only face phase at which every unit cube's hop is a reflection on every metric (D1).
- It is the half-filled sea's least-energy sector over all U(1) phases (main notes), also within the R^2 = 1 family (B1).
- It treats every unit face alike, including the faces of neither tiling, so it is not lopsided.

Torus Wilson lines remain a finite-volume choice (the main note's eight classes), with no effect in infinite volume.

## Candidate law text (tested, not recommended)

> Links, face-parity factor. "Each matter edge carries a fermion-parity register that every hop along it is dressed by; its loop term is read from the vacuum holonomy, n - Re tr(U_vac^dagger U); the vacuum is the update's least-quasi-energy state over these registers."

It derives pi (Lieb), keeps photons ordinary and gaps visons. It costs three role-assigned registers per matter site and a Gauss law, and it cannot be passed by a split (E1).

## Smuggling review

Supplied:
- hop 1 and half filling;
- eps;
- link values treated classically (static, sharp), with the electric term only estimated (B3);
- n_m;
- the pattern families: Bloch-periodic fields on 2^3 to 16x8x1 cells, and the coarse Kogut-Susskind pattern for A2 (other register patterns not searched);
- the CL-3 normalisation (1/g^2)(1 - cos) l/S.

Forced, given those:
- the A1 reach theorem;
- the A2 and A3 energetics and the flux-line binding;
- the B1 ordering and its least point;
- the B2 thresholds;
- the C1 sign of the magnetic response;
- the C3 group theorem;
- the D1-D4 equivalences;
- the E1 Stokes obstruction.

The recommended clause still supplies the phase, now as -1 per face rather than as a construction. What it removes is the spin-3/2 overlap and the shared overlap state, not the stipulation itself. The phase is not derived from a register, because the cheapest register derivation costs more structure than it removes. The energy argument is a consistency reason (the clause picks the sea's own least-energy sector), not a dynamical selection.

Not computed:
- quantum link dynamics (the electric term, a deconfined pi phase, a Z2 Monte Carlo);
- interactions beyond the main repulsive theorem;
- non-periodic register patterns;
- the asymptotic coefficient of C1.

## Dependencies

On main:
- HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02: Theorem 1 (R^2 = 1 iff all-minus faces, Cauchy-Schwarz), the end-point energies, the Wilson classes. Used.
- CUBIC_REPULSIVE_FLUX_FIXED_HALF_AND_CANONICAL_TWISTS_BOUNDED_THEOREM_NOTE_2026-09-04: pi through every plaquette is the global U(1) minimum at half filling, also with repulsion. Used, and B1 sharpens it to the R^2 = 1 subfamily.

Campaign:
- nested-prefold-sea (#9982): CL-1's spin-3/2 tick equals the KS tick; R^2 = 1 iff pi. Used, and extended to the inter-cube faces (D2).
- pi-flux-fold: the face clause it suggested; the Stokes obstruction (D1); the nesting log (A4). Used. Its suggestion "the face clause derives CL-1's pi phases" is narrowed here: not through registers, but kinematically.
- face-plaquette-law (#9968): loop operators and l/S = 1/B_f. Used.

Literature context, not premises:
- Lieb, PRL 73 (1994) 2158, the flux phase.
- Z2 gauge theories with fermions select pi flux at half filling in their deconfined phase (Assaad and Grover 2016; Gazit, Randeria and Vishwanath 2017, in 2+1D).

## How to run

python3 scripts/the_link_registers_cannot_supply_the_cube_ticks_pi_faces_and_the_hop_phases_reduce_to_minus_one_around_every_unit_face_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120. It takes about 23 s, peaks at about 160 MB, prints 5196 characters and ends with TOTAL: PASS=14 FAIL=0. It was checked through scripts/runner_cache.execute_runner from a temporary origin/main worktree (status ok, exit 0).
