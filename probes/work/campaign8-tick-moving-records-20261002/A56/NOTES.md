# A56 notes: are cube-interface gains additive? (decision 22 exploration; nothing adopted)

Setup (10:30): rules51_6.npz keys B4_inner, B4_r4, loaded via a53lib.load_rule(6, key) exactly as A53. Blocks are unions
of 2x2x2 cubes; restricted rule = a53lib.bilinear_pairs / four_sets with an open index (pairs inside, four-sets with all
four sites inside), as A53's t2_blocks. New: a56lib.py (table kernel for four-sets, random-singlet and cube-product
start vectors), chk56.py (term checks, kernel cross-check, 8/16-site exact energies, 24-site timing).
Rule reach: B4_inner J nonzero for classes 001,011,111,002,012,112,022,122,222 (no class with a component 3);
B4_r4 J nonzero for 001,011,111,002 only. Hence two cubes one cube apart (far2) share no term: the line's A-C coupling
is zero, so delta_line is a pure three-cube effect. In the L the two arm cubes share an edge (011-type bonds).

## chk56 B4_inner (10:40) — all checks pass
- Term sets: line3 180 pairs (96 inter-cube), 88 four-sets (24 in one cube, 64 across two, 0 across three); L3 216 pairs
  (132 inter-cube), 100 four-sets (24/64/12). Pairs match an independent class enumeration exactly; four-sets match the
  restriction of the 10^3-torus operator exactly. Table kernel = A53 _matvec_gen to 1e-12 (16 and 24 sites).
- EXACT: E_cube = -13.2367493930 (-1.654594/site, = A53); 2x2x4 = -26.6530796406 (-1.665817/site, = A53).
  Delta_face = -0.179581. Edge pair (cubes (0,0,0),(1,1,0)): -27.1400168618, Delta_edge = -0.666518 (!).
  Corner pair: Delta_corner = -0.000621. Gapped pair (0,0,0),(0,0,2): Delta = 0 exactly (no shared term).
- Anatomy (lz56 on 16 sites): face pair inter-cube bonds 001 -0.80 [4], 002 +0.17 [8], 011 +0.38 [8] -> frustrated
  interface, net -0.43; edge pair 011 bonds -1.12 [2] -> unfrustrated, net -1.65. Product overlaps 0.88 / 0.84.
- 24-site table matvec ~1.0 s (A53 generic kernel 2.1 s). Product start energy = 3 E_cube to 4e-14 (no 2+2 sets).
- The L contains an EDGE pair (arm cubes B, C), which the face-only additive estimate never credits.

## line3 B4_inner (10:45) — EXACT
E_line = -40.085114384396 (E/N -1.67021310), m = 100, true residual 5.6e-8, sum<s.s> -2e-12 (S = 0), product overlap 0.752.
E_add = 3 E_cube + 2 Delta = -40.069409888; delta_line = -0.015704 (line gains MORE than additive). Middle cube's
two-place energy -11.606 vs end cubes -12.136; each face interface -0.552 (vs -0.432 in the 2-cube block).

## L3 B4_inner (10:41) — EXACT
E_L = -40.196882660665 (E/N -1.67487011), m = 115, true residual 4.3e-8, sum<s.s> -2e-12, product overlap 0.800.
delta_L = E_L - E_add = -0.127473 (L gains MORE than face-additive). Split: Delta_edge (arm cubes B,C share an edge)
= -0.666518 alone, so the genuine three-cube increment delta3_L = delta_L - Delta_edge = +0.539045 (monogamy cuts the
edge gain by 81%). Anatomy: B-C 011 bonds <s.s> -0.507 (isolated edge pair -1.118); A-B NN bonds -0.567 (pair -0.80).

## B4_r4 (10:47) — EXACT
chk56 B4_r4: all term/kernel checks pass. E_cube = -13.2693202416 (= A53 -1.658665/site); 2x2x4 = -26.7106452242
(= A53 -1.669415/site); Delta_face = -0.172005; Delta_edge = -0.749491; Delta_corner = -0.000010; gapped pair 0.
line3: E_line = -40.168353473344 (E/N -1.67368139), residual 8.3e-8, S = 0, overlap 0.763. E_add = -40.151970207;
delta_line = -0.016383.
L3 B4_r4: E_L = -40.314396818243 (E/N -1.67976653), residual 6.5e-8, S = 0, overlap 0.794. delta_L = -0.162427;
delta3_L = delta_L - Delta_edge = +0.587064. B-C 011 bonds -0.563 [2]; A-B NN bonds -0.539 [4].
Next: two extra B4_inner shapes (pass 1 only): tri_eee (three pairwise edge-sharing cubes), bent_fe (face + edge chain).

## Extra B4_inner shapes (10:55) — EXACT energies (pass 1, residual est < 1e-7; S = 0 by construction)
tri_eee (cubes 000,110,101, pairwise edge-sharing): E = -41.245637283568 (-1.71857/site, lowest open block so far);
delta3_EEE = E - 3E_c - 3 Delta_edge = +0.464165 (keeps 77% of three isolated edge gains).
bent_fe (000,100,210: face + edge, ends uncoupled): E = -40.582196164736; delta3 = -0.025849 (slightly super-additive).

## Crystal implication (ARGUED)
- Face-only, plus 3 lines/cube: -1.72783 (inner), -1.72931 (r4): about 0.001 below the parton (-1.72681, -1.72841).
- Face-connected expansion to 3 cubes (3 lines + 12 L per cube): -1.919 / -1.973, but each edge pair sits in two L's
  (double count; the 2x2-square weight, 32 sites, corrects it). Edges credited once at in-L value: -1.823 / -1.851.
- All-contact increments (inner): pair level -2.222/site (6 Delta_edge = -4.00/cube); computed 3-cube terms
  +9.51/cube (L +6.47, EEE +3.71, bent -0.62, line -0.05) -> partial -1.033/site. Not converging at the 0.04/cube
  needed. Missing shapes: FEK (24/cube), EE0 (42/cube), 4-cube clusters.
- Monogamy exists but acts on the edge channel: the edge 011 bonds close frustrated triangles with the corner cube's
  NN bonds (L: B-C <s.s> -0.51 vs -1.12 isolated). No face monogamy (delta_line < 0, delta_bent < 0).

## Full three-cube increments, B4_inner (11:01; pass-1 energies, EXACT; corner-only shapes omitted, Delta_k = -6e-4)
- line: E -40.085114 (-1.67021/site); delta3 -0.015704; per cube x3 = -0.0471
- L: E -40.196883 (-1.67487/site); delta3 +0.539045; per cube x12 = +6.4685
- eee: E -41.245637 (-1.71857/site); delta3 +0.464165; per cube x8 = +3.7133
- bent: E -40.582196 (-1.69092/site); delta3 -0.025849; per cube x24 = -0.6204
- fek: E -40.547791 (-1.68949/site); delta3 +0.009176; per cube x24 = +0.2202
- ee90: E -41.124011 (-1.71350/site); delta3 -0.080727; per cube x12 = -0.9687
- ee120: E -41.034664 (-1.70978/site); delta3 +0.008620; per cube x24 = +0.2069
- ee180: E -41.100157 (-1.71251/site); delta3 -0.056873; per cube x6 = -0.3412
- pair level -17.7771/cube (-2.2221/site); three-cube sum +8.6315/cube; truncated estimate -1.1432/site (above the bare cube product -1.6546): the cube-increment expansion does not converge at three cubes.
