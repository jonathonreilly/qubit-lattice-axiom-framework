---
claim_id: a_shared_coarse_face_register_keeps_the_coarse_gauss_law_and_nested_role_blocks_hold_supplied_register_sizes_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For link registers placed on coarser blocks than the matter (nested role blocks): one spin-S register shared by every fine bond crossing a coarse face, with hops inside a block undressed, keeps the coarse Gauss law exactly ([H, G_X] = [H, G_Y] = 0 at S = 3, fine-site generator not conserved); with the domain-normalised raiser V (a partial isometry) the dressed crossing hops satisfy [A1, A2] = 0 and [A1, A2^+] = 0 away from the register extremes, so fine gates sharing a register are order-free on |E| <= S - 2, while the plain raiser S^+/S is not (0.44, 0.13); charges 1 and 4 (units of 1/6) cross by V^q of one register; an SU(2) colour-rishon register (F = 1, 12 modes) shared by both crossing bonds keeps every colour Gauss generator and the cluster number. The static potential of coarse-block links against fine links at the same g, on a 96^3 torus, deviates by +0.062, +0.019, +0.005 (B = 2) and +0.080, +0.024, +0.008 (B = 3) at R = nB, n = 2, 4, 8, so the Coulomb coefficient is unchanged at long wavelength (finite); the cell form factor has r^2 = (B^2 - b0^2)/4 fine units per axis; exact orbit counts give per-end capacities K = (b^3 - 10b + 9)/6 (odd b) and (b^3 - 4b)/6 (even b), nested layouts invariant under the 24 rotations, and maximal fill of finer levels starving coarser ones (240 against 3129 sites at level 27 of the 3 x 3 ladder). Estimates with a supplied register-coupling relation, one-loop running and the cell scale: the measured couplings need about 28, 28 and 680 flavours per end, which nested layouts hold at 40% site fill, while none of 2046 fixed nested size rules comes within 15% on all three couplings, so the sizes stay supplied. Supplied model, finite diagnostic: the register spins, mode counts and couplings, the torus size, the nesting ladders and fill rules, the register-coupling relation alpha(F), the one-loop betas, the cell scale, the hypercharge unit and the measured couplings."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_shared_coarse_face_register_keeps_the_coarse_gauss_law_and_nested_role_blocks_hold_supplied_register_sizes_2026_10_22.py
---

# A shared coarse face register keeps the coarse Gauss law, and nested role blocks hold supplied register sizes

Claim type: bounded_theorem.
Primary runner: `scripts/a_shared_coarse_face_register_keeps_the_coarse_gauss_law_and_nested_role_blocks_hold_supplied_register_sizes_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its gauge content lives on quantum link registers, and its couplings are set by register size: a larger register gives a weaker coupling. On a single block size, the hypercharge, SU(2) and SU(3) registers the measured couplings need do not fit the covariant site layout. This note asks whether each factor's register can sit on its own coarser block (nested role blocks) without losing gauge invariance or the long-wavelength photon, and whether any fixed rule for the nesting then gives the measured couplings. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Exact (one coarse face, fine modes x1, x2 on one side and y1, y2 on the other).

1. Coarse Gauss law. Hops inside a coarse block are undressed, and every fine hop crossing the face is dressed by one shared spin-S register (S = 3, with an electric term 0.7 E^2). Then [H, G_X] = [H, G_Y] = 0 for the coarse generators G_X = N_X + E and G_Y = N_Y - E. A fine-site generator is not conserved, so the gauge group is the coarse one.
2. Order-free sharing. Take the domain-normalised raiser V, with V|m> = |m+1> on its domain (a partial isometry). Then the dressed crossing hops satisfy [A1, A2] = 0, and [A1, A2^+] = b1 b2^+ (P_-S - P_S) vanishes away from the register extremes. So fine cube gates sharing one register commute on |E| <= S - 2. The plain raiser S^+/S does not have this property (stated in the derivation, printed values below).
3. Multi-unit charges. A charge of 4 units (1/6 each) crosses by V^4 of the same register as a charge of 1 unit, and the coarse Gauss law holds with the weighted charge.
4. SU(2). One colour-rishon register (F = 1) per coarse face is shared by both crossing bonds (12 fermion modes). The colour Gauss generators G^a_X and G^a_Y (a = 1, 2, 3) and the cluster number commute with H.

B. Long wavelength and form factor.

5. Coarse-block links (charges summed per cell) and links on every fine bond, at the same g, give static potentials whose ratio approaches 1 as R = nB grows. The Coulomb coefficient is unchanged at long wavelength (finite torus).
6. The vertex form factor of a cell is F(q) = mean_u e^{i q.u} over the cell's matter labels, with r^2 = (B^2 - b0^2)/4 fine units per axis for a block of m = B/b0 matter cells of side b0. The runner states, and does not compute, that umklapp enters only at the coarse reciprocal vector.

C. Register vacuum spread. In the harmonic register vacuum <E^2> = c_E / g^2, with g^2 = 4/sqrt(F(F+2)) set by the register (F = 2S), so sigma_E / S ~ sqrt(c_E / 2S) -> 0 and the weight beyond the extremes falls fast with S.

D. Exact nested capacities.

7. Per-end capacity. A block of side b keeps the sites outside the centre, the face-diagonal 12-orbits and the body-diagonal 8-orbits under the 24 rotations about its centre. This gives K = (b^3 - 10b + 9)/6 for odd b and (b^3 - 4b)/6 for even b. After matter and a finer level's fill are removed, the remaining set is invariant under the 24 rotations about the coarser centre, so nested covariant layouts exist.
8. Starvation. Maximal fill of the finer levels leaves a coarser level only the finer blocks' 8- and 12-orbit sites, a capacity of order (B/B_f)^3 B_f rather than B^3.

E. Couplings (estimates). These use the supplied register-coupling relation 1/alpha = pi sqrt(F(F + 2N))/2 for SU(N) and pi sqrt(F(F + 2))/36 for hypercharge, one-loop Standard-Model running, and the cell scale 1/a = 2.435e18 GeV.

9. At b = 3, F = 1 colour registers become strong far above M_Z. SU(2) and SU(3) need F ~ 27-29, so every factor sits on a coarser block.
10. Fixed rules. Take four ladders (b0, k) = (3, 3), (3, 2), (4, 2), (4, 3), every assignment of Y, SU(2) and SU(3) to a level, three fill rules (maximal fill split by equal F, maximal fill split by equal modes, face pooling S ~ B^2) and two cell-scale choices (1/(Ba) or 1/a). That is 2046 trials. None comes within 6% on all three couplings, and none within 15%.
11. With F fitted to the measured couplings (supplied), nested layouts hold the needed sizes with sites to spare. The size conflict is an artefact of a single block size.

## Derivation

Items 1-4 build the fermion modes by Jordan-Wigner (4 modes with a spin-3 register; 12 sparse modes for SU(2)) and compute commutators directly. The gate-order check of item 2 uses exp(-0.9 i h) for each dressed crossing hop. Item 5 computes the lattice Green's function on a 96^3 torus and on the (96/B)^3 coarse torus by FFT and compares V(R) - V(far corner), with the coarse one divided by B. Item 6 evaluates the 1D cell form factor at q = 1e-3 for (b0, m) = (3, 3), (3, 5), (4, 4). Section C averages the harmonic lattice transverse electric spread over a 48^3 momentum grid. Items 7 and 8 classify sites by their sorted absolute doubled coordinates about each block centre, count them, and check rotation invariance by applying all 24 rotation matrices. Section E inverts the coupling relation after one-loop running from M_Z, enumerates the fixed rules, and draws 400 seeded random target rescalings for the look-elsewhere count.

## Finite checks

Exact checks (the runner asserts each):
- Coarse Gauss law: [H, G_X] and [H, G_Y] are 0e+00 at S = 3; the fine-site generator commutator is 1.00.
- Shared register with V: [A1, A2] = 0e+00; [A1, A2^+] P_int = 0e+00 (full commutator 1.0); gate order on |E| <= S - 2 is 0e+00.
- Charges 1 and 4: commutator 0e+00.
- SU(2) shared register: maximum colour-generator commutator 0e+00, cluster number 0e+00.
- Form factor: maximum relative deviation of r^2 from (B^2 - b0^2)/4 is 2.7e-06.
- Capacities: the K formulas are reproduced for b = 3, 5, 9, 17 and b = 4, 8, with 0 violations of rotation invariance under the 24 rotations in three nested configurations.
- Starvation: at level 27 of the (3, 3) ladder, 240 sites per end remain against 3129 alone (asserted below 10%).

Finite diagnostics (supplied model, finite diagnostic):
- Plain raiser S^+/S on the register interior: commutator 0.44, gate order 0.13. These are printed, not asserted.
- Static potential ratio - 1 at R = nB, n = 2, 4, 8: B = 2: +0.062, +0.019, +0.005; B = 3: +0.080, +0.024, +0.008. The runner asserts that the deviation falls from n = 2 to n = 8 and is below 0.01 at B = 3, n = 8.
- Register vacuum: c_E = 0.796. The runner asserts only 0.5 < c_E < 1; the spread table is printed:

| S | sigma_E | sigma_E / S | weight beyond extremes |
|---|---|---|---|
| 1.5 | 0.88 | 0.585 | 2.3e-02 |
| 14.5 | 2.44 | 0.168 | 8.2e-10 |
| 29.0 | 3.43 | 0.118 | 7.3e-18 |
| 327.5 | 11.42 | 0.035 | 2.9e-181 |

- Per-end capacities, alone and after the finer levels' fills:

| ladder (b0, k) | sides | alone | after finer fills |
|---|---|---|---|
| (3, 3) | 3, 9, 27, 81 | 1, 107, 3129, 85203 | 1, 80, 240, 720 |
| (3, 2) | 3, 6, 12, 24, 48 | 1, 32, 272, 2208, 17728 | 1, 24, 16, 32, 64 |
| (4, 2) | 4, 8, 16, 32, 64 | 8, 64, 512, 4096, 32768 | 8, 0, 0, 0, 0 |
| (4, 3) | 4, 12, 36 | 8, 216, 5832 | 8, 0, 0 |

## Estimates against measurement

Supplied inputs: M_Z = 91.1876 GeV; 1/alpha_em = 127.95, sin^2 theta_W = 0.23122 and alpha_s = 0.1180 at M_Z; one-loop betas 41/6, -19/6 and -7; 1/a = 2.435e18 GeV, with a = sqrt(8 pi) l_P.
- Flavours per colour per end needed at 1/(1a): F_Y 655, F_2 29.0, F_3 29.4 (801 modes per end). At 1/(9a): 682, 28.3, 27.8 (822). At 1/(27a): 696, 28.0, 27.0 (833).
- With F = 1 at 1/(3a): SU(2) has 1/alpha = 3.51 and becomes strong at 8e+14 GeV; SU(3) has 1/alpha = 4.16 and becomes strong at 2e+16 GeV. The runner records this as a stated check (it prints the values; the pass is unconditional).
- Fixed rules: 2046 trials, 0 within 6% (asserted) and 0 within 15% (printed). The nearest is off by 55%: ladder (3, 2) with levels {Y: 1, SU(2): 3, SU(3): 3}, equal F, cell scale 1/a, giving 1/alpha_Y 44.0, 1/alpha_2 34.3, 1/alpha_3 12.6 against 98.4, 29.6, 8.47. 2 of 2046 trials fall within a factor 2 of all three. For a random target rescaled log-uniformly by a factor between 1/2 and 2, the rule family hits within 6% with probability 0.00 (400 seeded draws).
- Fitted sizes (F supplied): ladder (3, 2) with 24-blocks for all three factors holds them at fill 0.40; other assignments give 0.57 and 0.65. S_Y is about 340.
- Edge registers, with the supplied bound s >= 26.3 b_e and Delta = 0, fit a free fraction of 0.8 only for b_e >= 40, so edges are the coarsest role.
- Ratio pattern. Equal F per colour for SU(2) and SU(3) on one level matches F_2/F_3 = 1.019 at 1/(9a). This is the Standard-Model near-crossing of alpha_2 and alpha_3 near the cell scale, not new. F_Y/F needed is 24.8. Of the ladder-step laws k^p (k = 2, 3, 5; p = 2, 3), (3, 3) = 27 and (5, 2) = 25 are within 15%, with a look-elsewhere probability of about 0.49, which is chance level. No fixed fill gives the absolute F ~ 28. This ratio check is stated; its pass is unconditional.
- Form factor at B = 27: r_rms = 1.1e-33 m against the electron's measured point-likeness of about 1e-18 m, a margin of 9e+14. The block energy hbar c/(B a) = 9.0e+16 GeV, against a quoted quadratic photon Lorentz-violation bound E_QG2 > ~1e11 GeV.

## Boundary

Not claimed: a derivation of any register size or of the nesting from the rules (the sizes stay supplied, about three numbers); the register-coupling relation alpha(F), which is supplied from earlier link-register probes and not rederived here; running beyond one loop or thresholds; the long-wavelength statement beyond the 96^3 torus and n <= 8; the umklapp statement (stated); dynamics of the shared register beyond the commutators checked (no spectra or real-time evolution of the fine gates); an SU(3) shared register (only U(1) and SU(2) are built); the edge-register bound s >= 26.3 b_e (supplied); any experimental exclusion.

## Supplied vs forced

Supplied: the register spin S = 3 and the electric weight 0.7; the fermion mode layout of one coarse face; the gate angle 0.9; the 96^3 torus and block sizes B = 2, 3; the cell sizes for the form factor; the four nesting ladders, the fill rules and the cell-scale choices; the register-coupling relation; the one-loop betas; the cell scale; the measured couplings; the hypercharge unit 1/6; the edge-register bound; the seeded look-elsewhere draws. Forced, given those: the coarse Gauss law with a shared register; order-free sharing with the domain-normalised raiser away from the extremes; V^q crossing for multi-unit charges; the SU(2) colour Gauss law with a shared colour-rishon register; the r^2 of the cell form factor; the orbit-count capacities, the rotation-invariant nested layouts and the starvation of coarser levels under maximal fill; the absence, within the 2046 enumerated rules, of any rule reaching all three couplings within 15%.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): quantum link registers with Gauss's law, register size setting the coupling, the covariant site layout about block centres, and the reading of each gauge factor's register at its own rung. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/a_shared_coarse_face_register_keeps_the_coarse_gauss_law_and_nested_role_blocks_hold_supplied_register_sizes_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 2 s with about 125-140 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=14 FAIL=0`. Its random draws use a fixed seed; two runs gave identical output apart from the elapsed-time line.
