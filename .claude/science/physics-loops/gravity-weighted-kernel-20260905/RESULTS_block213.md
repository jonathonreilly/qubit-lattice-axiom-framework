# RESULTS — block 213, the weighted-kernel dispersion (Fable primary, resumed seat)

Runner: `scripts/admissibility_dirac_kahler_weighted_kernel_dispersion_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy rationals, symbols, exact roots of unity, QQ(sqrt 6) at the two
locus witnesses); the runner's gate I measures zero `sp.nsimplify`, zero float literals and
zero float call sites in its own source.

## Headline

The weighted kernel `K_H = H d - d^T H` reproduces R5's flat symbol exactly at the flat cell in
all four constructions. Under the graded (onsite) assembly its characteristic cone is exactly
the union of the two Hodge readings' cones `k^T (D1/D0) k = 0` and `k^T (D3 E D2^-1 E) k = 0`;
those two readings coincide on the Block 211 family exactly on the codimension-one locus
`S1 = -E S0 E`, `g0 = g1/(1 + pi0 g1)` (eight of the sixty-four sign cells, positive-definite-
solvable along its whole length) and nowhere else off flat; on the locus the cone IS one
metric's cone, `(k^T G1 k)^2`, and the symbol is STILL not a quadratic form times the identity
(branch constants `1, mu, 1/(1-g1^2), 1/(1-g1^2)` with `mu - 1 != 0`). Under the overlap
assembly the cone is a non-Hodge pair of quadrics at every point measured. The symbol is scalar
only in two directions on `v^2 = 1 - c^2`. The shears `g0, g1` enter the cone in both
assemblies; the diagonal moduli do not move the graded cone (formal four-parameter statement) —
a named tension with PR #7970's matter-side result, recorded and not resolved.

The dead seat's draft headline "never one metric's cone off flat" is REFUTED (correction 113 of
this block's own draft; nothing landed is touched).

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| diagnostic 1 (draft runner as found, e91bd87342) | baseline | never completed: killed after 35 CPU-minutes against the 600 s cache timeout | killed |
| phase timing 1 (rewritten measurement code) | scratch | `measure_principal` raised `PolynomialError` in `primitive_factors` on a symbolic denominator (defect 5) | exception |
| phase timing 2 | scratch | construction 0.8 s, control 0.0 s, spectra 0.9 s, principal 50.8 s, registration 6.6 s; three facts disagreed with declared literals (defects 6, 7 and my own sp.solve root drop) | — |
| pre-note baseline (9aa266d5f0 minus the E-3 correction) | baseline | `TOTAL: PASS=34 FAIL=2` (E-3: boundary H regular on (4,4), defect 8; I-1: note absent by design) | 2 |
| certified baseline | baseline | `TOTAL: PASS=36 FAIL=0`, `GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS`, elapsed 75 s | 0 |
| mutations | `--mutation <name>` x 36 | see the table below | nonzero each |

## Defects found in the inherited runner (audited as a refutation) and fixed

1. The first-order expansion `K_H,B(z) = i eps M + O(eps^2)`, `M = H0 D + D^T H0`, was assumed; now measured from the composed rules at the symbolic cell form under both assemblies (06004253df).
2. The overlap cone was accepted as `det B = +-Q+ Q-`; the sign is `+`, now pinned (06004253df).
3. The coincidence test used only Block 211's four class representatives, and filtered `sp.solve` output in a way that silently drops parametric solutions. The weighted kernel is not corner-sign-gauge invariant; the sixty-four-cell census finds sixteen curve cells, eight positive. Fail-closed Groebner reduction + census + closed form + QQ(sqrt 6) witnesses + symbolic curve (9aa266d5f0).
4. Baseline runtime > 35 CPU-minutes vs the 600 s cache timeout: generic symbolic 3x3 inverses, `cancel()` and a rational-function determinant in the lemma. Fraction-free rewrite; baseline 75 s (9aa266d5f0).
5. `primitive_factors` raised on rational functions with symbolic denominators (9aa266d5f0).
6. The declared 3D onsite cone lemma had sign `-D3`; measured `+D3` (9aa266d5f0).
7. "Transverse branches are quadratic forms nowhere" was false at the draft's own `honest_face` witness (`g1 = 0`), where the pair splits into `5 k^2` and `(25/13) k^T M1 k` (9aa266d5f0).
8. "Onsite H singular on both benches at the PD boundary" was false on (4,4) (the face at `c = 1/2` is regular, 2x2 block determinant `v0^2/(1-c^2)`) (9aa266d5f0).

One defect in this seat's own rewrite, found in testing before certification: `sp.solve` under the symbols' positivity assumptions dropped rule B's negative root; replaced by a degree-one check with exact substitution.

## What could NOT be established (honest list)

- Which assembly (onsite/graded vs overlap) the framework selects: not decided; both reported.
- Which Hodge reading (`G1 = D1/D0` vs `G2 = D3 E D2^-1 E`) is "the" metric: not decided; both are exact branches. The blind F2 comparator (sealed, unread by this seat) is the supervisor's to compare.
- Whether anything in the framework prefers or forbids the coincidence locus: not decided.
- A rational point with rational volumes on either positive coincidence curve: none below height 120; the witnesses live in QQ(sqrt 6).
- The meaning of the transverse 2-form branches (irreducible quadratic generically; split at `honest_face` and on the locus): exhibited, not interpreted.
- The transverse-product identity at fully symbolic D: derived from det-multiplicativity and gated on the symbolic Block 211 family and at the witnesses, not expanded as a seventeen-symbol polynomial identity (cost).
- Bench spectra at the locus witnesses over QQ(sqrt 6): the E-family spectra are taken at the eight rational witnesses only (the DomainMatrix charpoly path is over QQ / QQ(i)); the locus witnesses carry the cone/branch analysis (F-8) and the cell reconciliation (C-4).
- The (4,2,2) bench probes only the t-direction antisymmetric links (R5's structure); the three-direction content is carried by the Bloch principal part, not by that bench's spectra.
- Resolution of the #7970 tension: recorded only.
- No dynamics, no spacetime, no gravity, no continuum: not attempted (fence).

## Modelling choices not forced by the landed chain

`m = 0` (Block 201 ran at FORK_MASS = 9/20); periodic closure (Block 201 used the fork seam);
running both assemblies and both readings rather than choosing; reading "the cone" as
polynomial proportionality (over the reals a PD form's null cone is the origin); `G1`, `G2` as
the declared metric candidates with `E = diag(1,-1,1)` from Block 209's honest-lift pattern;
the formal four-parameter block family for the volume/shear separation; the `(t, x, y)`
direction order; the two QQ(sqrt 6) locus points; the eight rational witnesses (GOAL's four
required plus `mixed`, `near_boundary`, `boundary`, `honest_face`).

## Full baseline stdout (certified run, exit 0)

```text
MEASURED
  elapsed: 75s
  origin/main e249016f759f224d9b429932cd0d1db4d452dc1a
  authority AuthorityCertificate(fixed_authority=True, parent_pin_is_commit=True, parent_ref_and_ancestry=True, parent_artifact_blobs=True, stale_parent_artifact_blobs=False, stale_is_real_ancestor=True, stale_carries_neither_artifact=True, machinery_import_landed=True, inputs_readable=10, inputs_missing=())
  imposed 6, registered 0, adopted 0, gravity structures NOT SUPPLIED 9, readings 7, scoped headline words 4
  check verdict carried: DEGRADED-WORKER-MODE-FABLE-PRIMARY-REFUTING-CHECKER-PENDING
  THE CONSTRUCTION
    2D lane kernel = Block 201's True, nnz 64, spin-nonscalar 0, site-sign-equivalent True, raising part = Block 201's on (8,4) True, K = d - d^T True, d^2 = 0 True
    3D lane kernel: 48 links scanned, 0 bad, shadow = eta/2 True, nnz 32, x/y links absent on extent 2 True, K = d - d^T True, d^2 = 0 True
    assemblers: fork_hodge True, onsite_hodge True, overlap_hodge True, rules = bench assembly True
    flat: H = I True, K_H = K True
    witness flat: moduli (v0, g0, v1, g1) = (1, 0, 1, 0), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(0, 1) True
      leading minors (1, 1, 1, 1, 1, 1, 1, 1), PD True
      G1 = D1/D0 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
      G2 = D3 E D2^-1 E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
      G1 ~ G2 True; Hodge-consistency defects: D0 D3 - 1 = 0, nnz(D1 E D2 E - D0 D3 I) = 0
    witness W1: moduli (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(1/4, 15/16) True
      leading minors (15/16, 15/16, 225/256, 15/16, 25/32, 25/32, 25/36, 25/36), PD True
      G1 = D1/D0 = ((16/15, -4/15, -4/15), (-4/15, 16/15, -4/15), (-4/15, -4/15, 16/15))
      G2 = D3 E D2^-1 E = ((9/8, -3/8, 3/8), (-3/8, 9/8, -3/8), (3/8, -3/8, 9/8))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -1/16, nnz(D1 E D2 E - D0 D3 I) = 9
    witness W2: moduli (v0, g0, v1, g1) = (7/16, 3/4, 1, 3/4), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(3/4, 7/16) True
      leading minors (7/16, 7/16, 49/256, 7/16, 5/32, 5/32, 25/196, 25/196), PD True
      G1 = D1/D0 = ((16/7, -12/7, -12/7), (-12/7, 16/7, 12/7), (-12/7, 12/7, 16/7))
      G2 = D3 E D2^-1 E = ((49/40, -21/40, 21/40), (-21/40, 49/40, 21/40), (21/40, 21/40, 49/40))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -9/16, nnz(D1 E D2 E - D0 D3 I) = 9
    witness W3: moduli (v0, g0, v1, g1) = (12/25, 3/5, 3/4, 4/5), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(3/5, 12/25) True
      leading minors (12/25, 9/25, 108/625, 9/25, 297/2000, 891/8000, 429/6400, 143/1600), PD True
      G1 = D1/D0 = ((25/16, -15/16, -15/16), (-15/16, 25/16, 15/16), (-15/16, 15/16, 25/16))
      G2 = D3 E D2^-1 E = ((144/65, -64/65, 64/65), (-64/65, 144/65, 64/65), (64/65, 64/65, 144/65))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -9/25, nnz(D1 E D2 E - D0 D3 I) = 9
    witness mixed: moduli (v0, g0, v1, g1) = (15/16, 1/4, 1, 1/4), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(1/4, 15/16) True
      leading minors (15/16, 15/16, 225/256, 15/16, 25/32, 25/32, 3/4, 3/4), PD True
      G1 = D1/D0 = ((16/15, -4/15, -4/15), (-4/15, 16/15, -4/15), (-4/15, -4/15, 16/15))
      G2 = D3 E D2^-1 E = ((25/24, -5/24, 5/24), (-5/24, 25/24, 5/24), (5/24, 5/24, 25/24))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -1/16, nnz(D1 E D2 E - D0 D3 I) = 9
    witness near_boundary: moduli (v0, g0, v1, g1) = (7599/10000, 49/100, 1, 49/100), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(49/100, 7599/10000) True
      leading minors (7599/10000, 7599/10000, 57744801/100000000, 7599/10000, 22201/500000, 22201/500000, 22201/6502500, 22201/6502500), PD True
      G1 = D1/D0 = ((10000/7599, -4900/7599, -4900/7599), (-4900/7599, 10000/7599, -4900/7599), (-4900/7599, -4900/7599, 10000/7599))
      G2 = D3 E D2^-1 E = ((2601/200, -2499/200, 2499/200), (-2499/200, 2601/200, -2499/200), (2499/200, -2499/200, 2601/200))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -2401/10000, nnz(D1 E D2 E - D0 D3 I) = 9
    witness boundary: moduli (v0, g0, v1, g1) = (3/4, 1/2, 1, 1/2), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(1/2, 3/4) True
      leading minors (3/4, 3/4, 9/16, 3/4, 0, 0, 0, 0), PD False
      G1 = D1/D0 = ((4/3, -2/3, -2/3), (-2/3, 4/3, -2/3), (-2/3, -2/3, 4/3))
      G2 = D3 E D2^-1 E = ('UNDEFINED: det D2 = 0',)
      G1 ~ G2 None; Hodge-consistency defects: D0 D3 - 1 = -1/4, nnz(D1 E D2 E - D0 D3 I) = 9
    witness honest_face: moduli (v0, g0, v1, g1) = (3/5, 4/5, 5/3, 0), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(4/5, 3/5) True
      leading minors (3/5, 1, 3/5, 1, 13/27, 65/81, 325/243, 65/81), PD True
      G1 = D1/D0 = ((25/9, -20/9, -20/9), (-20/9, 25/9, 20/9), (-20/9, 20/9, 25/9))
      G2 = D3 E D2^-1 E = ((9/25, 0, 0), (0, 9/25, 0), (0, 0, 9/25))
      G1 ~ G2 False; Hodge-consistency defects: D0 D3 - 1 = -16/25, nnz(D1 E D2 E - D0 D3 I) = 9
    witness L+-: moduli (v0, g0, v1, g1) = (sqrt(6)/3, 1/3, 3*sqrt(6)/8, 1/2), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(1/3, sqrt(6)/3) True
      leading minors (sqrt(6)/3, 3/4, sqrt(6)/4, 3/4, 3*sqrt(6)/16, 27/64, 9*sqrt(6)/64, 3/8), PD True
      G1 = D1/D0 = ((9/8, -3/8, -3/8), (-3/8, 9/8, -3/8), (-3/8, -3/8, 9/8))
      G2 = D3 E D2^-1 E = ((4/3, -4/9, -4/9), (-4/9, 4/3, -4/9), (-4/9, -4/9, 4/3))
      G1 ~ G2 True; Hodge-consistency defects: D0 D3 - 1 = -1/9, nnz(D1 E D2 E - D0 D3 I) = 3
    witness L-+: moduli (v0, g0, v1, g1) = (sqrt(6)/3, 1/2, 4*sqrt(6)/9, 1/3), ranks (32, 32), free ('D07', 'D16', 'D25', 'D34'), blocks = formulas True, cross-degree zero True, origin tx face = shear_hodge(1/2, sqrt(6)/3) True
      leading minors (sqrt(6)/3, 8/9, 8*sqrt(6)/27, 8/9, 64*sqrt(6)/243, 512/729, 512*sqrt(6)/2187, 128/243), PD True
      G1 = D1/D0 = ((4/3, -2/3, 2/3), (-2/3, 4/3, -2/3), (2/3, -2/3, 4/3))
      G2 = D3 E D2^-1 E = ((9/8, -9/16, 9/16), (-9/16, 9/8, -9/16), (9/16, -9/16, 9/8))
      G1 ~ G2 True; Hodge-consistency defects: D0 D3 - 1 = -1/4, nnz(D1 E D2 E - D0 D3 I) = 3
  THE R5 CONTROL
    flat symbol identity 2D True, 3D True; (4,4) multiset ((0, 4), (1, 8), (2, 4)) expected ((0, 4), (1, 8), (2, 4)); (4,2,2) multiset ((0, 8), (1, 8)) expected ((0, 8), (1, 8)); Bloch = direct True
  THE EXACT SPECTRA (factored charpoly of the 16 x 16 bench -K^2; 'agree' = Bloch union equals direct bench)
    [flat (4, 4) onsite form] agree True multiset ((0, 4), (1, 8), (2, 4))
      lam**4*(lam - 2)**4*(lam - 1)**8
    [flat (4, 4) onsite pencil] agree True multiset ((0, 4), (1, 8), (2, 4))
      lam**4*(lam - 2)**4*(lam - 1)**8
    [flat (4, 4) overlap form] agree True multiset ((0, 4), (1, 8), (2, 4))
      lam**4*(lam - 2)**4*(lam - 1)**8
    [flat (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (2, 4))
      lam**4*(lam - 2)**4*(lam - 1)**8
    [flat (4, 2, 2) onsite form] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [flat (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [flat (4, 2, 2) overlap form] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [flat (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [W1 (4, 4) onsite form] agree True
      lam**4*(8*lam - 9)**2*(225*lam - 512)**2*(3600*lam**2 - 7921*lam + 4096)**4/544195584000000000000
    [W1 (4, 4) onsite pencil] agree True multiset ((0, 4), (16/15, 4), (256/225, 4), (8/5, 2), (128/75, 2))
      lam**4*(5*lam - 8)**2*(15*lam - 16)**4*(75*lam - 128)**2*(225*lam - 256)**4/18245578765869140625
    [W1 (4, 4) overlap form] agree True
      lam**4*(921600*lam - 923521)**8*(212336640000*lam**2 - 758109081600*lam + 653188856401)**2/23463327920443900734737608470952059032165154816000000000000000000000000
    [W1 (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (1922/1081, 4))
      lam**4*(lam - 1)**8*(1081*lam - 1922)**4/1365534810721
    [W1 (4, 2, 2) onsite form] agree True
      lam**8*(lam - 1)**2*(9*lam - 16)**2*(1800*lam**2 - 3433*lam + 1152)**2/262440000
    [W1 (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (16/15, 4), (9/8, 2), (32/25, 2))
      lam**8*(8*lam - 9)**2*(15*lam - 16)**4*(25*lam - 32)**2/2025000000
    [W1 (4, 2, 2) overlap form] agree True multiset ((0, 8), (116281/147456, 4), (4844401/3686400, 4))
      lam**8*(147456*lam - 116281)**4*(3686400*lam - 4844401)**4/87309122741611403792360904482602195353600000000
    [W1 (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [W2 (4, 4) onsite form] agree True
      lam**4*(8*lam - 1)**2*(49*lam - 512)**2*(784*lam**2 - 5321*lam + 4096)**4/58054566272303104
    [W2 (4, 4) onsite pencil] agree True multiset ((0, 4), (8/7, 2), (16/7, 4), (128/49, 2), (256/49, 4))
      lam**4*(7*lam - 16)**4*(7*lam - 8)**2*(49*lam - 256)**4*(49*lam - 128)**2/1628413597910449
    [W2 (4, 4) overlap form] agree True
      lam**4*(200704*lam - 279841)**8*(10070523904*lam**2 - 43992911872*lam + 36469158961)**2/267025264114921925707976017494600585196289137988168464702898176
    [W2 (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (1058/697, 4))
      lam**4*(lam - 1)**8*(697*lam - 1058)**4/236010384481
    [W2 (4, 2, 2) onsite form] agree True
      lam**8*(lam - 1)**2*(49*lam - 16)**2*(392*lam**2 - 9409*lam + 6272)**2/368947264
    [W2 (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (49/40, 2), (16/7, 4), (32/5, 2))
      lam**8*(5*lam - 32)**2*(7*lam - 16)**4*(40*lam - 49)**2/96040000
    [W2 (4, 2, 2) overlap form] agree True multiset ((0, 8), (508369/802816, 4), (3301489/802816, 4))
      lam**8*(802816*lam - 3301489)**4*(802816*lam - 508369)**4/172555240996445312059316339412827644581375901696
    [W2 (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [W3 (4, 4) onsite form] agree True
      lam**4*(50*lam - 9)**2*(72*lam - 625)**2*(57600*lam**2 - 294064*lam + 140625)**4/142657607172096000000000000
    [W3 (4, 4) onsite pencil] agree True multiset ((0, 4), (5/4, 2), (25/16, 4), (125/36, 2), (625/144, 4))
      lam**4*(4*lam - 5)**2*(16*lam - 25)**4*(36*lam - 125)**2*(144*lam - 625)**4/584325558976905216
    [W3 (4, 4) overlap form] agree True
      lam**4*(1440000*lam - 1485961)**8*(518400000000*lam**2 - 1770812640000*lam + 1338257962561)**2/4968552950211927758340096000000000000000000000000000000000000000000000000
    [W3 (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (2438/1489, 4))
      lam**4*(lam - 1)**8*(1489*lam - 2438)**4/4915625528641
    [W3 (4, 2, 2) onsite form] agree True
      lam**8*(144*lam - 25)**2*(19200*lam**3 - 429376*lam**2 + 724899*lam - 270000)**2/7644119040000
    [W3 (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (25/18, 2), (25/16, 2), (144/65, 2), (125/22, 2))
      lam**8*(16*lam - 25)**2*(18*lam - 25)**2*(22*lam - 125)**2*(65*lam - 144)**2/169612185600
    [W3 (4, 2, 2) overlap form] agree True multiset ((0, 8), (361/625, 4), (1190281/360000, 4))
      lam**8*(625*lam - 361)**4*(360000*lam - 1190281)**4/2562890625000000000000000000000000
    [W3 (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [mixed (4, 4) onsite form] agree True
      lam**4*(8*lam - 9)**2*(225*lam - 512)**2*(3600*lam**2 - 7921*lam + 4096)**4/544195584000000000000
    [mixed (4, 4) onsite pencil] agree True multiset ((0, 4), (16/15, 4), (256/225, 4), (8/5, 2), (128/75, 2))
      lam**4*(5*lam - 8)**2*(15*lam - 16)**4*(75*lam - 128)**2*(225*lam - 256)**4/18245578765869140625
    [mixed (4, 4) overlap form] agree True
      lam**4*(921600*lam - 923521)**8*(212336640000*lam**2 - 758109081600*lam + 653188856401)**2/23463327920443900734737608470952059032165154816000000000000000000000000
    [mixed (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (1922/1081, 4))
      lam**4*(lam - 1)**8*(1081*lam - 1922)**4/1365534810721
    [mixed (4, 2, 2) onsite form] agree True
      lam**8*(lam - 1)**2*(25*lam - 16)**2*(1800*lam**2 - 5481*lam + 3200)**2/2025000000
    [mixed (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (16/25, 2), (25/24, 2), (16/15, 2), (32/15, 2))
      lam**8*(15*lam - 32)**2*(15*lam - 16)**2*(24*lam - 25)**2*(25*lam - 16)**2/18225000000
    [mixed (4, 2, 2) overlap form] agree True multiset ((0, 8), (151321/147456, 4), (3845521/3686400, 4))
      lam**8*(147456*lam - 151321)**4*(3686400*lam - 3845521)**4/87309122741611403792360904482602195353600000000
    [mixed (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [near_boundary (4, 4) onsite form] agree True
      lam**4*(5000*lam - 2601)**2*(57744801*lam - 200000000)**2*(577448010000*lam**2 - 1716093277201*lam + 1000000000000)**4/9268668354548770320567322395208844305273017200250000000000000000000000
    [near_boundary (4, 4) onsite pencil] agree True multiset ((0, 4), (10000/7599, 4), (200/149, 2), (100000000/57744801, 4), (2000000/1132251, 2))
      lam**4*(149*lam - 200)**2*(7599*lam - 10000)**4*(1132251*lam - 2000000)**2*(57744801*lam - 100000000)**4/1055201249476755683705784578216196429114343364572774499488778001
    [near_boundary (4, 4) overlap form] agree True
      lam**4*(92391681600000000*lam - 95929452354489601)**8*(2134055707218944640000000000000000*lam**2 - 7244431307736186652742721600000000*lam + 5309189379798400912285477686478801)**2/24181012272179195502108113002012317321322411948429408497270860324375170855429943484246788271829144112726016000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    [near_boundary (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (619449602/384195001, 4))
      lam**4*(lam - 1)**8*(384195001*lam - 619449602)**4/21787471837434733075119289686780001
    [near_boundary (4, 2, 2) onsite form] agree True
      lam**8*(lam - 1)**2*(2601*lam - 10000)**2*(288724005000*lam**2 - 797519272201*lam + 130050000000)**2/563957648614582480370025000000
    [near_boundary (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (10000/7599, 4), (2601/200, 2), (500000/22201, 2))
      lam**8*(200*lam - 2601)**2*(7599*lam - 10000)**4*(22201*lam - 500000)**2/65740173059577556546160040000
    [near_boundary (4, 2, 2) overlap form] agree True multiset ((0, 8), (239350494815629201/369566726400000000, 4), (695847932293350001/369566726400000000, 4))
      lam**8*(369566726400000000*lam - 695847932293350001)**4*(369566726400000000*lam - 239350494815629201)**4/347970882060756862816199199479876376123532952137738532177284345722944681410560000000000000000000000000000000000000000000000000000000000000000
    [near_boundary (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [boundary (4, 4) onsite form] agree True
      lam**4*(2*lam - 1)**2*(9*lam - 32)**2*(36*lam**2 - 109*lam + 64)**4/544195584
    [boundary (4, 4) onsite pencil] agree True multiset ((0, 4), (4/3, 6), (16/9, 6))
      lam**4*(3*lam - 4)**6*(9*lam - 16)**6/387420489
    [boundary (4, 4) overlap form] agree True
      lam**4*(2304*lam - 2401)**8*(1327104*lam**2 - 4508928*lam + 3286969)**2/1398523325946563526078320054468635262976
    [boundary (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (98/61, 4))
      lam**4*(lam - 1)**8*(61*lam - 98)**4/13845841
    [boundary (4, 2, 2) onsite form] agree True multiset ((0, 8), (1/6, 2), (1, 2), (8/3, 2), (4, 2))
      lam**8*(lam - 4)**2*(lam - 1)**2*(3*lam - 8)**2*(6*lam - 1)**2/324
    [boundary (4, 2, 2) onsite pencil] agree True
      UNDEFINED: det H = 0
    [boundary (4, 2, 2) overlap form] agree True multiset ((0, 8), (5929/9216, 4), (17689/9216, 4))
      lam**8*(9216*lam - 17689)**4*(9216*lam - 5929)**4/52040292466647269602037015248896
    [boundary (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    [honest_face (4, 4) onsite form] agree True
      lam**4*(9*lam - 50)**2*(9*lam - 2)**2*(81*lam**2 - 594*lam + 625)**4/282429536481
    [honest_face (4, 4) onsite pencil] agree True multiset ((0, 4), (10/9, 4), (25/9, 8))
      lam**4*(9*lam - 25)**8*(9*lam - 10)**4/282429536481
    [honest_face (4, 4) overlap form] agree True
      lam**4*(25*lam - 49)**8*(5625*lam**2 - 33100*lam + 23716)**2/4827976226806640625
    [honest_face (4, 4) overlap pencil] agree True multiset ((0, 4), (1, 8), (42/31, 4))
      lam**4*(lam - 1)**8*(31*lam - 42)**4/923521
    [honest_face (4, 2, 2) onsite form] agree True
      lam**8*(9*lam - 25)**2*(25*lam - 9)**2*(81*lam**2 - 738*lam + 625)**2/332150625
    [honest_face (4, 2, 2) onsite pencil] agree True multiset ((0, 8), (9/25, 2), (25/13, 2), (25/9, 2), (5, 2))
      lam**8*(lam - 5)**2*(9*lam - 25)**2*(13*lam - 25)**2*(25*lam - 9)**2/8555625
    [honest_face (4, 2, 2) overlap form] agree True multiset ((0, 8), (256/225, 4), (676/225, 4))
      lam**8*(225*lam - 676)**4*(225*lam - 256)**4/6568408355712890625
    [honest_face (4, 2, 2) overlap pencil] agree True multiset ((0, 8), (1, 8))
      lam**8*(lam - 1)**8
    translation covariance at W1, nnz([-K_H^2, T_mu]): (((4, 4), 'onsite', (128, 128)), ((4, 4), 'overlap', (64, 0)), ((4, 2, 2), 'onsite', (128, 128, 128)), ((4, 2, 2), 'overlap', (0, 0, 0)))
    boundary: onsite H singular on (4,4) False, on (4,2,2) True; overlap H regular True
  THE PRINCIPAL PART AND THE CONE
    onsite lemma 3D True, 2D True, D0 absent True, block-diagonal True, 0-form branch True, top-form branch True, transverse product True, expansion K_H,B = i eps (H0 D + D^T H0) + O(eps^2) measured True
    overlap H0 form True, overlap cone 3D True, 2D True
    2D (c, v): onsite branches True, onsite pencil scalar generically False, on the locus v^2 = 1 - c^2 True, onsite form scalar False; overlap pencil scalar True, matches True, cone matches True, form scalar False, effective shear True, discrepancy True
    2D onsite exact 0-form H-pencil symbol: (-c*zt**4*zx**2 + c*zt**4 - c*zt**2*zx**4 + 2*c*zt**2*zx**2 - c*zt**2 + c*zx**4 - c*zx**2 + zt**4*zx**2 + zt**2*zx**4 - 4*zt**2*zx**2 + zt**2 + zx**2)/(4*c**2*zt**2*zx**2 - 4*zt**2*zx**2)
    2D onsite exact 2-form H-pencil symbol: (c*zt**4*zx**2 - c*zt**4 + c*zt**2*zx**4 - 2*c*zt**2*zx**2 + c*zt**2 - c*zx**4 + c*zx**2 - zt**4*zx**2 - zt**2*zx**4 + 4*zt**2*zx**2 - zt**2 - zx**2)/(4*v**2*zt**2*zx**2)
    2D overlap exact H-pencil scalar symbol: 961*(841*zt**4*zx**2 + 120*zt**4 + 841*zt**2*zx**4 - 3604*zt**2*zx**2 + 841*zt**2 + 120*zx**4 + 841*zx**2)/(4*(60*zt**2 - 961*zt*zx + 60*zx**2)*(60*zt**2 + 961*zt*zx + 60*zx**2))
    [flat onsite] parity-preserving H0 True; det B factors ('(kt**2 + kx**2 + ky**2)^2 [hessian rank 3]',)
      pencil branches (quadratic-form eigenvalues, multiplicity) (('kt**2 + kx**2 + ky**2', 4),); remaining factor degrees (); scalar True
      form branches (('kt**2 + kx**2 + ky**2', 4),); remaining (); scalar True
      k^T G1 k = kt**2 + kx**2 + ky**2; k^T G2 k = kt**2 + kx**2 + ky**2; cones are G1, G2 None; branches include G1, G2 None
    [flat overlap] parity-preserving H0 True; det B factors ('(kt**2 + kx**2 + ky**2)^2 [hessian rank 3]',)
      pencil branches (quadratic-form eigenvalues, multiplicity) (('kt**2 + kx**2 + ky**2', 4),); remaining factor degrees (); scalar True
      form branches (('kt**2 + kx**2 + ky**2', 4),); remaining (); scalar True
      k^T G1 k = kt**2 + kx**2 + ky**2; k^T G2 k = kt**2 + kx**2 + ky**2; cones are G1, G2 None; branches include G1, G2 None
    [W1 onsite] parity-preserving H0 True; det B factors ('(2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2)^1 [hessian rank 3]', '(3*kt**2 - 2*kt*kx + 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('9*kt**2/8 - 3*kt*kx/4 + 3*kt*ky/4 + 9*kx**2/8 - 3*kx*ky/4 + 9*ky**2/8', 1), ('16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15', 1)); remaining factor degrees ((2, 1),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15; k^T G2 k = 9*kt**2/8 - 3*kt*kx/4 + 3*kt*ky/4 + 9*kx**2/8 - 3*kx*ky/4 + 9*ky**2/8; cones are G1, G2 True; branches include G1, G2 True
    [W1 overlap] parity-preserving H0 True; det B factors ('(55*kt**2 - 16*kt*kx - 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2)^1 [hessian rank 3]', '(55*kt**2 - 16*kt*kx + 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15; k^T G2 k = 9*kt**2/8 - 3*kt*kx/4 + 3*kt*ky/4 + 9*kx**2/8 - 3*kx*ky/4 + 9*ky**2/8; cones are G1, G2 False; branches include G1, G2 False
    [W2 onsite] parity-preserving H0 True; det B factors ('(2*kt**2 - 3*kt*kx - 3*kt*ky + 2*kx**2 + 3*kx*ky + 2*ky**2)^1 [hessian rank 3]', '(7*kt**2 - 6*kt*kx + 6*kt*ky + 7*kx**2 + 6*kx*ky + 7*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('16*kt**2/7 - 24*kt*kx/7 - 24*kt*ky/7 + 16*kx**2/7 + 24*kx*ky/7 + 16*ky**2/7', 1), ('49*kt**2/40 - 21*kt*kx/20 + 21*kt*ky/20 + 49*kx**2/40 + 21*kx*ky/20 + 49*ky**2/40', 1)); remaining factor degrees ((2, 1),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/7 - 24*kt*kx/7 - 24*kt*ky/7 + 16*kx**2/7 + 24*kx*ky/7 + 16*ky**2/7; k^T G2 k = 49*kt**2/40 - 21*kt*kx/20 + 21*kt*ky/20 + 49*kx**2/40 + 21*kx*ky/20 + 49*ky**2/40; cones are G1, G2 True; branches include G1, G2 True
    [W2 overlap] parity-preserving H0 True; det B factors ('(79*kt**2 - 48*kt*kx - 48*kt*ky + 79*kx**2 + 48*kx*ky + 79*ky**2)^1 [hessian rank 3]', '(79*kt**2 - 48*kt*kx + 48*kt*ky + 79*kx**2 + 48*kx*ky + 79*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/7 - 24*kt*kx/7 - 24*kt*ky/7 + 16*kx**2/7 + 24*kx*ky/7 + 16*ky**2/7; k^T G2 k = 49*kt**2/40 - 21*kt*kx/20 + 21*kt*ky/20 + 49*kx**2/40 + 21*kx*ky/20 + 49*ky**2/40; cones are G1, G2 False; branches include G1, G2 False
    [W3 onsite] parity-preserving H0 True; det B factors ('(5*kt**2 - 6*kt*kx - 6*kt*ky + 5*kx**2 + 6*kx*ky + 5*ky**2)^1 [hessian rank 3]', '(9*kt**2 - 8*kt*kx + 8*kt*ky + 9*kx**2 + 8*kx*ky + 9*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('25*kt**2/16 - 15*kt*kx/8 - 15*kt*ky/8 + 25*kx**2/16 + 15*kx*ky/8 + 25*ky**2/16', 1), ('144*kt**2/65 - 128*kt*kx/65 + 128*kt*ky/65 + 144*kx**2/65 + 128*kx*ky/65 + 144*ky**2/65', 1)); remaining factor degrees ((2, 1),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 25*kt**2/16 - 15*kt*kx/8 - 15*kt*ky/8 + 25*kx**2/16 + 15*kx*ky/8 + 25*ky**2/16; k^T G2 k = 144*kt**2/65 - 128*kt*kx/65 + 128*kt*ky/65 + 144*kx**2/65 + 128*kx*ky/65 + 144*ky**2/65; cones are G1, G2 True; branches include G1, G2 True
    [W3 overlap] parity-preserving H0 True; det B factors ('(1091*kt**2 - 635*kt*kx - 635*kt*ky + 1091*kx**2 + 635*kx*ky + 1091*ky**2)^1 [hessian rank 3]', '(1091*kt**2 - 635*kt*kx + 635*kt*ky + 1091*kx**2 + 635*kx*ky + 1091*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 25*kt**2/16 - 15*kt*kx/8 - 15*kt*ky/8 + 25*kx**2/16 + 15*kx*ky/8 + 25*ky**2/16; k^T G2 k = 144*kt**2/65 - 128*kt*kx/65 + 128*kt*ky/65 + 144*kx**2/65 + 128*kx*ky/65 + 144*ky**2/65; cones are G1, G2 False; branches include G1, G2 False
    [mixed onsite] parity-preserving H0 True; det B factors ('(2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2)^1 [hessian rank 3]', '(5*kt**2 - 2*kt*kx + 2*kt*ky + 5*kx**2 + 2*kx*ky + 5*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15', 1), ('25*kt**2/24 - 5*kt*kx/12 + 5*kt*ky/12 + 25*kx**2/24 + 5*kx*ky/12 + 25*ky**2/24', 1)); remaining factor degrees ((2, 1),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15; k^T G2 k = 25*kt**2/24 - 5*kt*kx/12 + 5*kt*ky/12 + 25*kx**2/24 + 5*kx*ky/12 + 25*ky**2/24; cones are G1, G2 True; branches include G1, G2 True
    [mixed overlap] parity-preserving H0 True; det B factors ('(762829*kt**2 - 192944*kt*kx - 192944*kt*ky + 750541*kx**2 - 18352*kx*ky + 750541*ky**2)^1 [hessian rank 3]', '(762829*kt**2 - 192944*kt*kx + 192944*kt*ky + 750541*kx**2 - 18352*kx*ky + 750541*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 16*kt**2/15 - 8*kt*kx/15 - 8*kt*ky/15 + 16*kx**2/15 - 8*kx*ky/15 + 16*ky**2/15; k^T G2 k = 25*kt**2/24 - 5*kt*kx/12 + 5*kt*ky/12 + 25*kx**2/24 + 5*kx*ky/12 + 25*ky**2/24; cones are G1, G2 False; branches include G1, G2 False
    [near_boundary onsite] parity-preserving H0 True; det B factors ('(50*kt**2 - 49*kt*kx - 49*kt*ky + 50*kx**2 - 49*kx*ky + 50*ky**2)^1 [hessian rank 3]', '(51*kt**2 - 98*kt*kx + 98*kt*ky + 51*kx**2 - 98*kx*ky + 51*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('2601*kt**2/200 - 2499*kt*kx/100 + 2499*kt*ky/100 + 2601*kx**2/200 - 2499*kx*ky/100 + 2601*ky**2/200', 1), ('10000*kt**2/7599 - 9800*kt*kx/7599 - 9800*kt*ky/7599 + 10000*kx**2/7599 - 9800*kx*ky/7599 + 10000*ky**2/7599', 1)); remaining factor degrees ((2, 1),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 10000*kt**2/7599 - 9800*kt*kx/7599 - 9800*kt*ky/7599 + 10000*kx**2/7599 - 9800*kx*ky/7599 + 10000*ky**2/7599; k^T G2 k = 2601*kt**2/200 - 2499*kt*kx/100 + 2499*kt*ky/100 + 2601*kx**2/200 - 2499*kx*ky/100 + 2601*ky**2/200; cones are G1, G2 True; branches include G1, G2 True
    [near_boundary overlap] parity-preserving H0 True; det B factors ('(27799*kt**2 - 19600*kt*kx - 19600*kt*ky + 27799*kx**2 - 19600*kx*ky + 27799*ky**2)^1 [hessian rank 3]', '(27799*kt**2 - 19600*kt*kx + 19600*kt*ky + 27799*kx**2 - 19600*kx*ky + 27799*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 10000*kt**2/7599 - 9800*kt*kx/7599 - 9800*kt*ky/7599 + 10000*kx**2/7599 - 9800*kx*ky/7599 + 10000*ky**2/7599; k^T G2 k = 2601*kt**2/200 - 2499*kt*kx/100 + 2499*kt*ky/100 + 2601*kx**2/200 - 2499*kx*ky/100 + 2601*ky**2/200; cones are G1, G2 False; branches include G1, G2 False
    [boundary onsite] parity-preserving H0 True; det B factors ('(kt - kx + ky)^2 [hessian rank 0]', '(kt**2 - kt*kx - kt*ky + kx**2 - kx*ky + ky**2)^1 [hessian rank 2]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees (); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 4*kt**2/3 - 4*kt*kx/3 - 4*kt*ky/3 + 4*kx**2/3 - 4*kx*ky/3 + 4*ky**2/3; k^T G2 k = None; cones are G1, G2 None; branches include G1, G2 None
    [boundary overlap] parity-preserving H0 True; det B factors ('(11*kt**2 - 8*kt*kx - 8*kt*ky + 11*kx**2 - 8*kx*ky + 11*ky**2)^1 [hessian rank 3]', '(11*kt**2 - 8*kt*kx + 8*kt*ky + 11*kx**2 - 8*kx*ky + 11*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 4*kt**2/3 - 4*kt*kx/3 - 4*kt*ky/3 + 4*kx**2/3 - 4*kx*ky/3 + 4*ky**2/3; k^T G2 k = None; cones are G1, G2 None; branches include G1, G2 None
    [honest_face onsite] parity-preserving H0 True; det B factors ('(kt**2 + kx**2 + ky**2)^1 [hessian rank 3]', '(5*kt**2 - 8*kt*kx - 8*kt*ky + 5*kx**2 + 8*kx*ky + 5*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (('5*kt**2 + 5*kx**2 + 5*ky**2', 1), ('25*kt**2/9 - 40*kt*kx/9 - 40*kt*ky/9 + 25*kx**2/9 + 40*kx*ky/9 + 25*ky**2/9', 1), ('25*kt**2/13 - 40*kt*kx/13 - 40*kt*ky/13 + 25*kx**2/13 + 40*kx*ky/13 + 25*ky**2/13', 1), ('9*kt**2/25 + 9*kx**2/25 + 9*ky**2/25', 1)); remaining factor degrees (); scalar False
      form branches (('25*kt**2/9 + 25*kx**2/9 + 25*ky**2/9', 1), ('9*kt**2/25 + 9*kx**2/25 + 9*ky**2/25', 1)); remaining ((2, 1),); scalar False
      k^T G1 k = 25*kt**2/9 - 40*kt*kx/9 - 40*kt*ky/9 + 25*kx**2/9 + 40*kx*ky/9 + 25*ky**2/9; k^T G2 k = 9*kt**2/25 + 9*kx**2/25 + 9*ky**2/25; cones are G1, G2 True; branches include G1, G2 True
    [honest_face overlap] parity-preserving H0 True; det B factors ('(13*kt**2 - 5*kt*kx - 5*kt*ky + 13*kx**2 + 5*kx*ky + 13*ky**2)^1 [hessian rank 3]', '(13*kt**2 - 5*kt*kx + 5*kt*ky + 13*kx**2 + 5*kx*ky + 13*ky**2)^1 [hessian rank 3]')
      pencil branches (quadratic-form eigenvalues, multiplicity) (); remaining factor degrees ((2, 2),); scalar False
      form branches (); remaining ((4, 1),); scalar False
      k^T G1 k = 25*kt**2/9 - 40*kt*kx/9 - 40*kt*ky/9 + 25*kx**2/9 + 40*kx*ky/9 + 25*ky**2/9; k^T G2 k = 9*kt**2/25 + 9*kx**2/25 + 9*ky**2/25; cones are G1, G2 False; branches include G1, G2 False
    W1 graded exact 0-form H-pencil symbol: -(2*zt**4*zx**2*zy**2 + zt**4*zx**2 + zt**4*zy**2 + 2*zt**2*zx**4*zy**2 + zt**2*zx**4 + 2*zt**2*zx**2*zy**4 - 18*zt**2*zx**2*zy**2 + 2*zt**2*zx**2 + zt**2*zy**4 + 2*zt**2*zy**2 + zx**4*zy**2 + zx**2*zy**4 + 2*zx**2*zy**2)/(15*zt**2*zx**2*zy**2)
    W1 cones onsite True, overlap True; onsite cones = G1, G2 everywhere True; branches everywhere True; overlap cones never G1, G2 True; scalar anywhere curved 3D False; transverse pair splits at ('honest_face',)
    G1 ~ G2 on the chart: Groebner bases (('t*(u**2 + 1)', 'u*(u**2 + 1)'), ('t*(u**2 + 1)', 'u*(u**2 + 1)'), ('t*(u**2 + 1)', 'u*(u**2 + 1)'), ('t*(u**2 + 1)', 'u*(u**2 + 1)')) (all equal True), real solutions ((0, 0),) over 4 classes
    THE SIXTY-FOUR-CELL CENSUS (64 cells): (('(g0*g1 + g0 + g1,)', 4, ((-1, -1),)), ('(g0*g1 + g0 - g1,)', 4, ((1, -1),)), ('(g0*g1 - g0 + g1,)', 4, ((-1, 1),)), ('(g0*g1 - g0 - g1,)', 4, ((1, 1),)), ('(g0, g1)', 48, ((-1, -1), (-1, 1), (1, -1), (1, 1))))
      rule-A cells (S1 = -E S0 E) 8, rule-B cells (S1 = +E S0 E) 8, rules cover the curve cells True, closed form of M1 E M2 E verified True, curves solved True
    THE LOCUS WITNESSES ('L+-', 'L-+'): PD True, G2 = mu G1 True with mu (32/27, 27/32), graded det B = (k^T G1 k)^2 True, branch constants ((1, 32/27, 4/3, 4/3), (27/32, 1, 9/8, 9/8)), transverse split True, overlap factor counts (2, 2), overlap never G1 True
    THE LOCUS SYMBOLICALLY: one quadric squared True, branches k-free True, tied constants (('1', '-(2*g1 + 1)/((g1 - 1)*(g1 + 1)**3)', '-1/((g1 - 1)*(g1 + 1))', '-1/((g1 - 1)*(g1 + 1))'), ('1', '(2*g1 - 1)/((g1 - 1)**3*(g1 + 1))', '-1/((g1 - 1)*(g1 + 1))', '-1/((g1 - 1)*(g1 + 1))')) match True, mu - 1 = ('-g1**3*(g1 + 2)/((g1 - 1)*(g1 + 1)**3)', '-g1**3*(g1 - 2)/((g1 - 1)**3*(g1 + 1))') matches True
  SHEAR REGISTRATION
    onsite: shear moves the cone True, volumes do not True, branch scales ('v1/v0', 'v0/v1')
    overlap: Bloch H at zero shear = h0 I True, zero-shear pencil = R5 True, zero-shear form = h0^2 times R5, shear moves the cone True, sign class moves the cone True
    KERNEL-SIDE SHEAR REGISTRATION: YES in both assemblies (the cone moves with g0, g1 exactly); DIAGONAL-METRIC REGISTRATION: branch scales only (graded) or through h0 and the h_f sums (overlap), and invisible to the overlap pencil symbol at zero shear.  MATTER SIDE (PR #7970, conditional): responds to the diagonal metric and to NO shear.  NAMED TENSION -- recorded, not resolved here.
  READINGS, AND EACH IS A READING
    R1: that the characteristic cone is a light cone or a causal structure.  Measured: the zero set of det B(kappa), a homogeneous polynomial in three formal variables attached to a finite antisymmetric matrix.  No time, no signal, no causality.  Reading.
    R2: that the H-pencil reading is the physical propagator.  Measured: one of two declared squared-symbol readings of the same antisymmetric form; the chain's action-form convention is the Euclidean reading and neither is selected by any premise.  Reading.
    R3: that the assembly is decided.  Measured: Block 105 lands BOTH the onsite and the overlap assembly, Block 201's completion uses the overlap one, and no premise here chooses; the two give different cones and both are reported.  Reading.
    R4: that kernel-side shear registration is a gravitational shear response.  Measured: exact nonzero derivatives of a polynomial with respect to two rational parameters of one cell form.  The matter-side result it stands in tension with is itself conditional (PR #7970).  Reading.
    R5: that Block 201's completion is corrected.  Measured: Block 201's fork Hodge is reproduced digit for digit and its overlap assembly is one of the two landed assemblies run here; nothing landed is touched.  Reading.
    R6: that any of it generalises past this instance.  Measured: two periodic benches, one cell family, ten witnesses, two assemblies, two readings, one rule.  Reading.
    R7: that the coincidence locus is selected, preferred or physical.  Measured: a codimension-one algebraic locus in eight of sixty-four sign cells on which two DECLARED readings of one cell form agree; no premise here prefers it, the overlap assembly does not see it, and the symbol is not scalar on it.  Reading.
  nsimplify calls in this source: 0; float literals: 0; float call sites: 0
  NOT CLAIMED: NO GRAVITY. NO DYNAMICS. NO SPACETIME CONE. NO PROPAGATOR. NO ASSEMBLY DECIDED. NO HODGE READING SELECTED. NO CONTINUUM. THE READINGS ARE READINGS.

[PASS] A-1: origin/main is e249016f759f224d9b429932cd0d1db4d452dc1a, the axiom and registry blobs match on origin/main AND in the worktree, and the audit timeout is 600s
[PASS] A-2: PARENT_COMMIT 4e9931a970de is a real ancestor of HEAD resolving PARENT_REF, both Block 212 artifacts are content-identical at it and in the worktree, the stale pin 7a98db1dfea5 -- the Block 211 tip -- is a real ancestor carrying NEITHER, the three machinery imports are landed (Blocks 201, 211 with 209, and 105), and 10 of 10 audit inputs are readable
[PASS] B-1: 6 imposed objects, 0 registered, 0 adopted
[PASS] B-2: NO GRAVITY IS SUPPLIED: gravity_supplied = False and 9 gravity structures are enumerated as NOT SUPPLIED
[PASS] B-3: THE WORD *SYMBOL* IS SCOPED BEFORE THE FIRST NUMERAL: it names the exact 2^d x 2^d Bloch matrix of a finite antisymmetric kernel on a periodic bench and its eigenvalue branches; symbol_is_dynamics = False, propagator = False
[PASS] B-4: THE WORD *CONE* IS SCOPED: it names the zero set of det B(kappa), a homogeneous polynomial in three formal variables, and NO light cone, NO causal structure and NO spacetime; cone_is_spacetime_cone = False, and 4 headline words ('SYMBOL', 'CONE', 'METRIC', 'DISPERSION') are scoped before any number, the words ('SPACETIME', 'LIGHT CONE', 'PROPAGATOR', 'EINSTEIN') naming NOTHING established here
[PASS] B-5: THE ASSEMBLY IS NOT SELECTED BY THIS BLOCK: Block 105 lands BOTH the onsite and the overlap assembly and Block 201's completion uses the overlap one; both are run and both are reported; assembly_selected = False
[PASS] B-6: NO GENERIC-PARAMETER THEOREM AND NO CONTINUUM LIMIT, AND THE READINGS ARE READINGS: 7 of them are enumerated, readings_licensed = False, and EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the cycle-913 caution, carried verbatim, with nothing registered and nothing adopted
[PASS] C-1: THE 2D LANE KERNEL IS BLOCK 201's: on (4,4) the eta-staggered rules give Block 201's lane_kernel exactly (True) with 64 nonzero entries, it is site-sign-equivalent to Block 201's spin-diagonalised covariant kernel (True) which has 0 non-scalar blocks, the graded raising part equals Block 201's raising_part on its (8,4) fork extent (True), and K = d - d^T with d^2 = 0 (True, True)
[PASS] C-2: THE 3D LANE KERNEL IS BLOCK 209's SHADOW, LINK BY LINK: on (4,2,2) all 48 directed links scalarise under Omega = G1^t G2^x G3^y with 0 bad links and every scalar equal to the rule's eta_d / 2 (True); the bench kernel has 32 nonzero entries because the extent-2 directions carry NO antisymmetric link (True) -- R5's (4,2,2) structure -- and K = d - d^T, d^2 = 0 (True, True)
[PASS] C-3: THE ASSEMBLERS REPRODUCE THE LANDED HODGES DIGIT FOR DIGIT: Block 201's fork_hodge on (8,4) at c = 5/13 (True), Block 105's onsite_hodge (True) and overlap_hodge (True), and the rule-based onsite and overlap assemblies equal the bench assemblies of a uniform cell (True)
[PASS] C-4: THE CELL FORMS ARE BLOCK 211's, RECONCILED: all 10 witnesses solve at ranks (32, 32) with free names D07, D16, D25, D34, the degree blocks equal Block 211's formulas [v0], v1 M1, M2/v0, [1/v1] with zero cross-degree entries, the origin tx face equals Block 105's shear_hodge(s_tx0 g0, v0), and PD holds exactly at ('flat', 'W1', 'W2', 'W3', 'mixed', 'near_boundary', 'honest_face', 'L+-', 'L-+') -- the two QQ(sqrt 6) locus witnesses included -- and fails at the boundary
[PASS] C-5: THE FLAT CELL IS THE CONTROL'S CELL: at (c, v) = (0, 1) and at Block 211's flat point both assemblies give H = I on both benches (True) and K_H = K exactly (True)
[PASS] D-1: R5's FLAT SYMBOL IS AN EXACT POLYNOMIAL IDENTITY: -K_B(z)^2 = (sum_d sin^2 k_d = sum_d -(z_d - 1/z_d)^2 / 4) times the identity in two (True) and three (True) directions
[PASS] D-2: AND THE BENCH MULTISETS ARE R5's, WITH MULTIPLICITIES: on (4,4) ((0, 4), (1, 8), (2, 4)) and on (4,2,2) ((0, 8), (1, 8)), equal to {sum_d sin^2(2 pi m_d / N_d)} computed exactly, from the direct bench charpoly and from the Bloch union alike (True)
[PASS] E-1: BLOCH UNION = DIRECT BENCH, EVERY TIME: 63 (witness, bench, assembly, reading) charpolys of degree 16 agree exactly between the product of 2^d x 2^d Bloch charpolys at exact roots of unity and the direct 16 x 16 bench matrix (True); translation covariance of -K_H^2 at W1, as nnz([-K_H^2, T_mu]) per direction: (((4, 4), 'onsite', (128, 128)), ((4, 4), 'overlap', (64, 0)), ((4, 2, 2), 'onsite', (128, 128, 128)), ((4, 2, 2), 'overlap', (0, 0, 0)))
[PASS] E-2: W1's OWN (4,4) SPECTRUM, DECLARED: the overlap H-pencil reading has the exact multiset ((0, 4), (1, 8), (1922/1081, 4)) against R5's ((0, 4), (1, 8), (2, 4)) -- only the (pi/2, pi/2)-type momenta move; every other witness spectrum is printed as its factored charpoly above
[PASS] E-3: THE PD BOUNDARY IS A THREE-DIRECTION EDGE CASE, MEASURED: at gamma0 = gamma1 = 1/2 all-plus the onsite H is SINGULAR on (4,2,2) (True; the triangle determinant (1 + g)^2 (1 - 2g) vanishes) so the H-pencil reading is undefined there while the form reading stays defined, and REGULAR on (4,4) (False singular; the origin tx face is Block 105's shear_hodge at c = 1/2 with 2 x 2 block determinant v0^2/(1 - c^2), the two-direction PD condition being |c| < 1); the overlap H stays regular on both (True)
[PASS] F-1: THE ONSITE CONE LEMMA, AT FULLY SYMBOLIC D: det B = +D3 * (k^T D1 k) * (k^T E adj(D2) E k) (True) and in two directions det B = -D2 * (k^T D1 k) (True); D0 is absent from det B (True); B = [[k^T D1, 0], [D2 W, D3 E k]] with W k = 0 and (E k)^T W = 0 so the pencil principal block is block-diagonal by form degree (True) with the 0-form branch k^T D1 k / D0 (True) and the eigenvector adj(D2) E k at eigenvalue D3 k^T E D2^-1 E k (True), all as fraction-free polynomial identities in the seventeen symbols; and on the symbolic Block 211 family the transverse product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k) (True); and the expansion K_H,B(z) = i eps M + O(eps^2), M = H0 D + D^T H0 symmetric, is MEASURED from the composed rules at the symbolic cell under both assemblies (True)
[PASS] F-2: THE OVERLAP CONE, AT SYMBOLIC h: the folded overlap H0 is h0 I + 2 h_f on the two-flip pairs, h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8, h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8 (True); det B = +Q+ Q- exactly, sign pinned, with Q+ = h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx + 4*h0*hty*kt*ky + 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky - 8*htx*hxy*kt*ky - 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2 and Q- = h0**2*kt**2 + h0**2*kx**2 + h0**2*ky**2 + 4*h0*htx*kt*kx - 4*h0*hty*kt*ky + 4*h0*hxy*kx*ky - 4*htx**2*ky**2 - 8*htx*hty*kx*ky + 8*htx*hxy*kt*ky - 4*hty**2*kx**2 - 8*hty*hxy*kt*kx - 4*hxy**2*kt**2 (True), and in two directions det B = -h0 (h0*(kt**2 + kx**2) + 4*htx*kt*kx) (True)
[PASS] F-3: TWO DIRECTIONS AT SYMBOLIC (c, v), BLOCK 105's OWN CELL FORM: the graded H-pencil principal symbol has EXACTLY the branches ('(kt**2 - 2*c*kt*kx + kx**2)/(1 - c**2)', '(kt**2 - 2*c*kt*kx + kx**2)/v**2') (True) -- the Hodge reading's cone k^T (D1/D0) k and det(g)/v^2 times it -- so the cone IS the cell metric's cone there; the overlap H-pencil principal symbol is the scalar (c**2*(v**2 + 1) - 3*v**2 - 1)*((c**2*(v**2 + 1) - 3*v**2 - 1)*(kt**2 + kx**2) + 4*c*v**2*kt*kx)/((c**2 - 1)*(c**2*(v**2 + 1)**2 - (3*v**2 + 1)**2)) times the identity (True, True) with cone h0(kt^2+kx^2)+4 htx kt kx
[PASS] F-4: AND THE OVERLAP CONE IS NOT THE METRIC'S: its effective shear is 2*c*v**2/(3*v**2 + 1 - c**2*(v**2 + 1)) (True), the same sign as the Hodge reading's c but never its magnitude, with the exact discrepancy c_K - c = -c*(1 - c**2)*(v**2 + 1)/(3*v**2 + 1 - c**2*(v**2 + 1)) (True), nonzero for every c != 0
[PASS] F-5: THREE DIRECTIONS AT EVERY CURVED WITNESS: under the graded assembly det B factors EXACTLY into the two Hodge readings' cones k^T G1 k and k^T G2 k (True) and both are exact H-pencil branches (True); at W1 the cones are ('2*kt**2 - kt*kx - kt*ky + 2*kx**2 - kx*ky + 2*ky**2', '3*kt**2 - 2*kt*kx + 2*kt*ky + 3*kx**2 - 2*kx*ky + 3*ky**2') (True) and under the overlap assembly ('55*kt**2 - 16*kt*kx - 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2', '55*kt**2 - 16*kt*kx + 16*kt*ky + 55*kx**2 - 16*kx*ky + 55*ky**2') (True); the overlap cones are proportional to NEITHER reading at any curved rational witness (True)
[PASS] F-6: THE SYMBOL IS NOT A QUADRATIC FORM TIMES THE IDENTITY: at no curved three-direction witness, under either assembly or reading, is the principal symbol scalar (principal_scalar_curved_3d = False); the transverse 2-form pair splits into two quadratic-form branches at exactly the curved rational witnesses ('honest_face',) -- honest_face, offset-1 shear zero, D2 isotropic -- and is an irreducible quadratic at the other five (measured ('honest_face',)); ON the coincidence locus the cone is one quadric but the symbol is STILL not scalar, because mu - 1 = pi0 g1^3 (2 + pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3) is a nonzero rational function of g1 (True; measured ('-g1**3*(g1 + 2)/((g1 - 1)*(g1 + 1)**3)', '-g1**3*(g1 - 2)/((g1 - 1)**3*(g1 + 1))')), locus_symbol_scalar = False; in two directions the graded symbol is scalar exactly on v**2 = 1 - c**2 (True) and not generically (False); the form readings are scalar nowhere (False, False)
[PASS] F-7: THE COINCIDENCE THEOREM: on the four class representatives' (t, u) chart the proportionality ideal of (G1, G2) has the lex Groebner basis ('t*(u**2 + 1)', 'u*(u**2 + 1)') in every class (True) with real zeros EXACTLY ((0, 0),) -- the flat point -- taken fail-closed over 4 classes; BUT the weighted kernel is not corner-sign-gauge invariant, and the census over all 64 sign cells at symbolic moduli is (('(g0, g1)', 48, ((-1, -1), (-1, 1), (1, -1), (1, 1))), ('(g0*g1 + g0 - g1,)', 4, ((1, -1),)), ('(g0*g1 - g0 + g1,)', 4, ((-1, 1),)), ('(g0*g1 - g0 - g1,)', 4, ((1, 1),)), ('(g0*g1 + g0 + g1,)', 4, ((-1, -1),))): 48 cells coincide only at flat and 16 carry a curve, exactly the 8 rule-A cells [S1 = -E S0 E (so pi1 = -pi0): g0 (1 + pi0 g1) = g1, i.e. g0 = g1/(1 + pi0 g1), positive on the magnitude domain] and the 8 rule-B cells [S1 = +E S0 E (so pi1 = pi0): g0 + g1 = pi0 g0 g1, i.e. g0 = -g1/(1 - pi0 g1) < 0: no positive point] (True), with the closed form of M1 E M2 E verified in each (True) and both curves solved exactly (True); 8 cells carry a positive-definite-solvable coincidence curve; coincidence_only_at_flat_everywhere = False, cone_is_one_metric_cone_everywhere = False
[PASS] F-8: THE LOCUS, WITNESSED AND THEN PROVED ALONG THE CURVE: the two QQ(sqrt 6) witnesses ('L+-', 'L-+') are on the family and positive definite (True); G2 = mu G1 EXACTLY with mu = (32/27, 27/32) (True); the graded det B is ONE quadric squared, (k^T G1 k)^2 (True) -- the cone IS one metric's cone there -- with all four H-pencil branches constant multiples ((1, 32/27, 4/3, 4/3), (1, 27/32, 9/8, 9/8)) of k^T G1 k and the transverse pair SPLIT (True), while the overlap cone stays a non-Hodge pair with factor counts (2, 2) (True); symbolically along g0 = g1/(1 + pi0 g1) with free volumes det B is one quadric squared (True), every branch is k-free times k^T G1 k (True), and with the ties the constants are ('1', '(1 + 2 pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3)', '1/(1 - g1^2)', '1/(1 - g1^2)') (True); cone_is_one_metric_cone_on_locus = True
[PASS] G-1: THE SHEAR ENTERS THE CONE, EXACTLY: under the graded assembly d(k^T G1 k)/dg0 and d(k^T G2 k)/dg1 are nonzero and det B is not proportional to its zero-shear value (True); under the overlap assembly likewise (True) and the sign class moves the cone at fixed magnitudes (True)
[PASS] G-2: THE DIAGONAL METRIC DOES NOT: under the graded assembly det B is proportional to its unit-volume value (True) and the volumes enter only the branch scales ('v1/v0', 'v0/v1'); under the overlap assembly the Bloch H at zero shear is h0 times the identity (True), the zero-shear H-pencil symbol is R5's for EVERY volume pair (True) and the zero-shear form symbol is h0^2 times R5; volume_enters_onsite_cone = False
[PASS] G-3: THE #7970 TENSION IS RECORDED AND NOT RESOLVED: KERNEL-SIDE SHEAR REGISTRATION: YES in both assemblies (the cone moves with g0, g1 exactly); DIAGONAL-METRIC REGISTRATION: branch scales only (graded) or through h0 and the h_f sums (overlap), and invisible to the overlap pencil symbol at zero shear.  MATTER SIDE (PR #7970, conditional): responds to the diagonal metric and to NO shear.  NAMED TENSION -- recorded, not resolved here. (tension_recorded = True)
[PASS] H-1: FENCE ONE -- 'scout-grade finite exact linear algebra on one cell form, not a spacetime and not a dynamics', BLOCK 211's FENCE INHERITED VERBATIM: scout_grade_only = True, physical_content = False
[PASS] H-2: FENCE TWO -- THE ASSEMBLY IS A SUPPLIED FORK, NOT A RESULT: Block 105's onsite and overlap assemblies give DIFFERENT cones and this block decides between them nowhere; assembly_decided = False
[PASS] H-3: FENCE THREE -- NO HODGE READING IS SELECTED: G1 = D1/D0 and G2 = D3 E D2^-1 E are both realised as exact branches and neither is named 'the' metric; hodge_reading_selected = False
[PASS] H-4: FENCE FOUR -- THE INSTANCE SCOPE, ENUMERATED: 6 restrictions (("two periodic benches, (4,4) with Block 105's 2D face form and (4,2,2) with Block 211's 3D cell form, and no other extent", "one cell family, Block 211's per-offset-isotropic variety at the degree-diagonal representative, eight rational witnesses and two QQ(sqrt 6) locus witnesses, with the sixty-four-cell census taken on the degree-block formulas at symbolic moduli", "two assemblies, Block 105's onsite and overlap, and two squared-symbol readings, the Euclidean form and the H-pencil", "one rule, Block 201's A = sx, B = -sz shadow and its Block 209 three-direction shadow, at the periodic closure and m = 0", 'the principal part at k = 0 of the eight-fold degenerate zero; no continuum limit, no lattice-spacing statement', "the two Hodge readings G1 and G2 as declared candidates; which, if either, is 'the' metric is not decided here"))
[PASS] I-1: the note is present at ADMISSIBILITY_DIRAC_KAHLER_WEIGHTED_KERNEL_DISPERSION_BOUNDED_THEOREM_NOTE_2026-09-05.md and the N5 fence appears in it VERBATIM as a single line
[PASS] I-2: sp.nsimplify appears 0 times in this runner's own source -- MEASURED, not promised -- so no rational tolerance can turn the nonzero discrepancy polynomial into a zero and manufacture the identity this block refutes
[PASS] I-3: and 0 float literals appear in that same source with EXACTLY 0 float call sites, both MEASURED by an AST walk -- Block 211's strict form
GATES A=PASS B=PASS C=PASS D=PASS E=PASS F=PASS G=PASS H=PASS I=PASS
N5: per_element: THE IMPOSED-OBJECT BANNER, FIRST AND WITH TEETH, AND THE WORDS SYMBOL, CONE, METRIC AND DISPERSION ARE EACH SCOPED BEFORE THE FIRST NUMERAL. NOTHING HERE IS REGISTERED OR ADOPTED -- THE WEIGHTED KERNEL K_H = H d - d^T H (Block 107's / Block 201's completion at m = 0 and periodic closure, with d Block 201's graded raising part of the eta-staggered lane kernel and Block 209's three-direction shadow), THE TWO LANDED ASSEMBLIES (Block 105's onsite_hodge at even anchors and its overlap_hodge at every anchor with weight 2^-d, Block 191's rule as used by Block 201's fork_hodge), THE TWO SQUARED-SYMBOL READINGS (the Euclidean form -K_H^2 and the H-pencil -(H^-1 K_H)^2), THE PERIOD-2 BLOCH REDUCTION with its bipartite block B(kappa), THE TWO CANDIDATE CELL METRICS G1 = D1/D0 and G2 = D3 E D2^-1 E read off the degree blocks by Block 209's honest-lift pattern, and BLOCK 211's FAMILY, ITS SIXTY-FOUR SIGN CELLS AND ITS WITNESSES with BLOCK 105's shear_hodge READ THROUGH THEIR OWN RUNNERS, are IMPOSED MEASURED OBJECTS OF THIS BLOCK, built from the landed primary bodies and from NOTHING in any scratchpad. NO GRAVITY IS SUPPLIED: this block supplies NO lapse variable in an ADM phase space, NO shift vector, NO Hamiltonian constraint, NO momentum constraint, NO first-class constraint algebra, NO Dirac closure, NO Dirac observable, NO gauge orbit and NO diffeomorphism quotient. 'SYMBOL' NAMES THE EXACT 2^d x 2^d BLOCH MATRIX OF A FINITE ANTISYMMETRIC KERNEL ON A PERIODIC BENCH AND NAMES NO DYNAMICS AND NO PROPAGATOR. 'CONE' NAMES THE ZERO SET OF det B(kappa), A HOMOGENEOUS POLYNOMIAL, READ AS A POLYNOMIAL IDENTITY (proportionality of quadratic forms) BECAUSE OVER THE REALS A POSITIVE DEFINITE FORM'S NULL CONE IS THE ORIGIN, AND NAMES NO LIGHT CONE, NO CAUSAL STRUCTURE AND NO SPACETIME. 'METRIC' NAMES ONE OF TWO DECLARED RATIONAL READINGS OF THE CELL FORM'S DEGREE BLOCKS. 'DISPERSION' NAMES THE EIGENVALUE BRANCHES OF AN EXACT 4 x 4 OR 8 x 8 MATRIX. THE WORDS SPACETIME, LIGHT CONE, PROPAGATOR AND EINSTEIN NAME NOTHING ESTABLISHED HERE. NOTHING IS REGISTERED, NOTHING IS ADOPTED, AND NO AXIOM AMENDMENT IS JUSTIFIED.\nper_site: THE CONSTRUCTION IS THE CHAIN'S AND THE CONTROL IS R5's. The 2D lane kernel equals Block 201's lane_kernel exactly and is site-sign-equivalent to its spin-diagonalised covariant kernel with zero non-scalar blocks; the 3D lane kernel is Block 209's shadow link by link (48 links, 0 bad, every scalar eta_d / 2), and on (4,2,2) the extent-2 directions carry NO antisymmetric link; K = d - d^T with d^2 = 0 in Block 201's grading in both dimensions; the assemblers reproduce Block 201's fork_hodge and Block 105's onsite_hodge and overlap_hodge digit for digit; the ten cell forms -- eight rational witnesses and two QQ(sqrt 6) locus witnesses -- are Block 211's solved D at ranks (32, 32) with its degree-block formulas and its origin tx face equal to Block 105's shear_hodge; at the flat cell both assemblies give H = I and K_H = K on both benches; and -K_B(z)^2 = sum_d -(z_d - 1/z_d)^2 / 4 times the identity is an exact polynomial identity in two and three directions, whose bench multisets are {0 x4, 1 x8, 2 x4} on (4,4) and {0 x8, 1 x8} on (4,2,2), exactly R5's.\nper_mode: THE EXACT SPECTRA AND THE PRINCIPAL PART. Every (witness, bench, assembly, reading) charpoly of degree 16 at the eight rational witnesses agrees exactly between the Bloch union over exact roots of unity and the direct bench matrix; at W1 on (4,4) the overlap H-pencil multiset is {0 x4, 1 x8, 1922/1081 x4} against R5's {0 x4, 1 x8, 2 x4}; at the PD boundary g0 = g1 = 1/2 the onsite H is singular on (4,2,2), where the triangle determinant (1 + g)^2 (1 - 2g) vanishes and the H-pencil reading is undefined while the form reading remains defined, and REGULAR on (4,4), whose origin tx face is Block 105's shear_hodge at c = 1/2 with two-direction PD condition |c| < 1; the overlap assembly remains regular on both. The expansion K_H,B(exp(i eps kappa)) = i eps M(kappa) + O(eps^2) with M = H0 D(kappa) + D(kappa)^T H0 symmetric is MEASURED from the composed rules at the fully symbolic cell form under both assemblies; both assemblies preserve grade parity, M = [[0, B], [B^T, 0]] with B = H_e D_eo + D_oe^T H_o, the characteristic cone {det B = 0} is reading-independent, and the principal symbols are B B^T (form) and H_e^-1 B H_o^-1 B^T (pencil) on the even sector with the same spectra on the odd sector.\nper_block: THE TWO LEMMAS, AT SYMBOLIC ARGUMENTS. Graded assembly, any block-diagonal cell form, as fraction-free polynomial identities in seventeen symbols: B = [[k^T D1, 0], [D2 W, D3 E k]] with W k = 0 and (E k)^T W = 0 from d^2 = 0; det B = +D3 (k^T D1 k)(k^T E adj(D2) E k) in three directions and -D2 (k^T D1 k) in two; D0 is absent; the pencil principal symbol is block-diagonal by form degree with the EXACT branches k^T (D1/D0) k on 0-forms and D3 k^T E D2^-1 E k on top forms (eigenvector adj(D2) E k), the transverse 2-form pair being the roots of a quadratic whose product is det(D2)/det(D1) (k^T D1 k)(k^T E D2^-1 E k), the product taken on the symbolic Block 211 family. Overlap assembly: the folded H0 is h0 I + two-flip couplings 2 h_f with h0 = (v0 + 3 v1 + 3/v0 + 1/v1)/8 and h_f = -(s_f0 v1 g0 + s_f1 g1 / v0)/8, and det B = Q+ Q- exactly, sign pinned, with the two displayed quadratic cones differing by the sign of the t-y plane terms; in two directions the single cone h0 (kt^2 + kx^2) + 4 h_tx kt kx.\nlattice_wide: THE HYPOTHESIS, ANSWERED EXACTLY, AND THE FIRST DRAFT's ANSWER CORRECTED. In two directions at symbolic (c, v) the graded H-pencil branches are k^T g^-1 k and (det g / v^2) k^T g^-1 k with g = [[1, c], [c, 1]] = (D1/D0)^-1, so the cone IS the cell metric's cone and the symbol is a quadratic form times the identity exactly on the honest-volume locus v^2 = 1 - c^2; the overlap cone has the effective shear c_K = 2 c v^2 / (3 v^2 + 1 - c^2 (v^2 + 1)) with the exact discrepancy c_K - c = -c (1 - c^2)(v^2 + 1) / (3 v^2 + 1 - c^2 (v^2 + 1)). In three directions the graded cone is EXACTLY the union of the two Hodge readings' cones k^T (D1/D0) k = 0 and k^T (D3 E D2^-1 E) k = 0, both exact H-pencil branches. THE COINCIDENCE THEOREM: on the four class representatives' (t, u) chart the proportionality ideal has lex Groebner basis {t (u^2 + 1), u (u^2 + 1)} with the flat point its only real zero, taken fail-closed; BUT the weighted kernel is not invariant under Block 211's corner-sign gauge, and the census over all sixty-four sign cells at symbolic moduli finds forty-eight cells coinciding only at flat and sixteen carrying a coincidence CURVE, in closed form: with M1 = I - g0 S0, M2 = I - g1 S1, G1 ~ G2 iff P = M1 E M2 E ~ I, and P = (1 - 2 g0 g1) I + (g1 - g0 - pi0 g0 g1) S0 when S1 = -E S0 E (rule A, curve g0 = g1/(1 + pi0 g1), positive and PD-solvable in all eight rule-A cells: four of class (+1, -1), four of class (-1, +1)), P = (1 + 2 g0 g1) I - (g0 + g1 - pi0 g0 g1) S0 when S1 = +E S0 E (rule B, no positive point). ON THE LOCUS THE GRADED CONE IS ONE METRIC'S CONE, (k^T G1 k)^2, every H-pencil branch is a constant multiple of k^T G1 k with constants {1, mu, 1/(1 - g1^2), 1/(1 - g1^2)}, mu = (1 + 2 pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3), and mu - 1 = pi0 g1^3 (2 + pi0 g1)/((1 - pi0 g1)(1 + pi0 g1)^3) is nonzero off flat, so the symbol is STILL NOT SCALAR there; the two QQ(sqrt 6) witnesses L+- (g1 = 1/2, g0 = 1/3, mu = 32/27, constants 1, 32/27, 4/3, 4/3) and L-+ (g1 = 1/3, g0 = 1/2, mu = 27/32, constants 1, 27/32, 9/8, 9/8) realise it on the family with every cone, reading and constant rational, and the transverse pair SPLITS there. OFF THE LOCUS the graded cone is the union of two DISTINCT quadrics, the overlap cones are proportional to neither reading at every curved witness including the locus, no curved three-direction principal symbol is scalar under either assembly or reading, and the transverse pair splits into two quadratic-form branches at exactly one curved rational witness, honest_face (offset-1 shear zero, D2 isotropic), staying an irreducible quadratic at the other five. THE CONE IS ONE METRIC'S CONE EXACTLY ON THE LOCUS AND NOWHERE ELSE OFF FLAT, AND THE EXACT DISCREPANCY IS THE CLOSED FORM ABOVE.\nper_scope: SHEAR REGISTRATION, SEPARATELY. The shears g0 and g1 move the cone under both assemblies (exact nonzero derivatives, exact non-proportionality to the zero-shear cone, and the sign class moves the overlap cone at fixed magnitudes); the diagonal moduli do not move the graded cone (det B is proportional to its unit-volume value, a statement on the formal four-parameter block family in which volumes and shears are independent) and enter only the branch scales v1/v0 and v0/v1; under the overlap assembly the Bloch H at zero shear is h0 times the identity, the zero-shear H-pencil symbol is R5's for EVERY volume pair and the zero-shear form symbol is h0^2 times R5's. THIS IS A NAMED TENSION WITH THE MATTER-SIDE NO-SHEAR-RESPONSE RESULT OF PR #7970 (itself conditional): kernel side registers the shear and not the diagonal, matter side the diagonal and not the shear -- RECORDED, NOT RESOLVED HERE. WHAT REMAINS OPEN: which assembly, if either, the framework selects; which Hodge reading, if either, is 'the' metric; whether anything in the framework prefers the coincidence locus; the transverse branches' meaning; every extent, witness and convention not run; and no energy, no mass, no measurement postulate, no Born rule, no dynamics, no continuum and no gravity is supplied by any line of this block.\nRESULT: THE WEIGHTED KERNEL K_H = H d - d^T H REPRODUCES R5's FLAT SYMBOL EXACTLY AT THE FLAT CELL IN ALL FOUR CONSTRUCTIONS; ITS CHARACTERISTIC CONE IS, UNDER THE GRADED ASSEMBLY, THE UNION OF THE TWO HODGE READINGS' CONES k^T (D1/D0) k = 0 AND k^T (D3 E D2^-1 E) k = 0, WHICH COINCIDE EXACTLY ON THE CODIMENSION-ONE LOCUS g0 = g1/(1 + pi0 g1) OF THE EIGHT SIGN CELLS WITH S1 = -E S0 E -- ONE METRIC'S CONE THERE, WITH A NON-SCALAR SYMBOL -- AND NOWHERE ELSE OFF FLAT; UNDER THE OVERLAP ASSEMBLY IT IS A NON-HODGE PAIR OF CONES AT EVERY POINT MEASURED; THE PRINCIPAL SYMBOL IS A QUADRATIC FORM TIMES THE IDENTITY ONLY IN TWO DIRECTIONS ON v^2 = 1 - c^2; AND THE SHEAR, NOT THE DIAGONAL METRIC, IS WHAT THE KERNEL REGISTERS. THESE ARE SCOUT-GRADE FINITE EXACT LINEAR-ALGEBRA FACTS ON ONE CELL FORM, NOT A SPACETIME AND NOT A DYNAMICS. EVERY NEGATIVE HERE IS NON-SUPPLY WITHIN THIS FORMALISM AND NEVER METAPHYSICAL NECESSITY -- the CYCLE913 CAUTION, CARRIED VERBATIM -- and EVERY POSITIVE HERE IS CANDIDACY WITHIN THIS FORMALISM AND NEVER A CLAIM ABOUT NATURE.\nDECISION_CUT: NOTHING IS REGISTERED AND NOTHING IS ADOPTED. No premise-class change is registered; no landed note is EDITED; no landed number is touched; Blocks 105, 107, 128, 171, 190, 191, 201, 209, 210, 211 and 212 STAND EXACTLY AS LANDED. BLOCK 201 IS NOT CORRECTED: its fork_hodge is reproduced digit for digit and its overlap assembly is one of the two landed assemblies run here. BLOCK 211 IS NOT CORRECTED: its witnesses, ranks, block formulas and minors are reproduced through its own runner; its corner-sign gauge is a symmetry of the cell form's positivity and NOT of the weighted kernel, which is why its four class representatives do not speak for its sixty-four sign cells here. THIS BLOCK's OWN FIRST DRAFT IS CORRECTED, AS CORRECTION 113: the dead seat's headline 'never one metric's cone off flat' was true on the four representatives it tested and false on the family, refuted by the census and by two explicit witnesses; nothing landed is touched by that correction. THIS BLOCK's OWN DEFECTS ARE DISCLOSED: two benches, one cell family, ten witnesses, two assemblies and two readings, one rule, the principal part at one degenerate zero -- not a parameter space and not a limit; the assembly fork is supplied and not decided; the two Hodge readings are declared candidates and neither is selected; the coincidence locus is exhibited and not preferred; the transverse 2-form branches are exhibited and not interpreted; m = 0 and the periodic closure are this block's choices, not the chain's. DEGRADED WORKER MODE IS DISCLOSED: drafted on Fable worker seats after the gpt-5.6-sol seats died at the account limit, resumed by a second Fable seat after the first died mid-block, with the refuting checker pending. PROVENANCE: the R5 weighted-kernel design task of this lane, at TOTAL PASS=36 FAIL=0 across nine families.\nTOE: zero axiom retirement; zero obligation retirement; zero TOE movement; no TOE percentage moves; retained-positive end-to-end theory count remains zero.
TOTAL: PASS=36 FAIL=0
python3   77.80s user 0.32s system 99% cpu 1:18.40 total
```

## Mutation results (36 declared; each must fail exactly its own family and exit nonzero)

| # | mutation | declared family | failing family (GATES line) | TOTAL | exit |
| ---: | --- | :---: | :---: | --- | :---: |
| 1 | `stale_main_authority` | `A` | `A` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 2 | `stale_parent_authority` | `A` | `A` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 3 | `claim_objects_registered` | `B` | `B` | `TOTAL: PASS=34 FAIL=2` | 2 |
| 4 | `claim_gravity_supplied` | `B` | `B` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 5 | `claim_symbol_is_dynamics` | `B` | `B` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 6 | `claim_cone_is_spacetime_cone` | `B` | `B` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 7 | `claim_assembly_selected` | `B` | `B` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 8 | `claim_readings_licensed` | `B` | `B` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 9 | `break_lane_kernel_fidelity` | `C` | `C` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 10 | `break_three_direction_shadow` | `C` | `C` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 11 | `break_assembler_fidelity` | `C` | `C` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 12 | `break_cell_form_reconciliation` | `C` | `C` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 13 | `break_flat_cell_identity` | `C` | `C` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 14 | `break_flat_symbol_identity` | `D` | `D` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 15 | `break_flat_bench_multiset` | `D` | `D` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 16 | `break_bloch_bench_agreement` | `E` | `E` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 17 | `break_witness_spectra` | `E` | `E` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 18 | `break_boundary_edge_case` | `E` | `E` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 19 | `break_onsite_cone_lemma` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 20 | `break_overlap_cone_formula` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 21 | `break_two_dim_branches` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 22 | `break_three_dim_branch_identification` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 23 | `claim_principal_part_scalar` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 24 | `claim_cone_is_metric_cone` | `F` | `F` | `TOTAL: PASS=34 FAIL=2` | 2 |
| 25 | `break_coincidence_census` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 26 | `break_coincidence_locus` | `F` | `F` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 27 | `break_shear_registration` | `G` | `G` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 28 | `claim_volume_registration` | `G` | `G` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 29 | `drop_tension_record` | `G` | `G` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 30 | `break_scout_grade_fence` | `H` | `H` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 31 | `claim_assembly_decided` | `H` | `H` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 32 | `claim_hodge_reading_selected` | `H` | `H` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 33 | `break_instance_scope` | `H` | `H` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 34 | `drop_n5_fence` | `I` | `I` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 35 | `break_nsimplify_absence` | `I` | `I` | `TOTAL: PASS=35 FAIL=1` | 1 |
| 36 | `break_float_absence` | `I` | `I` | `TOTAL: PASS=35 FAIL=1` | 1 |

Per-family mutation census: `A 2, B 6, C 5, D 2, E 3, F 8, G 3, H 4, I 3` (matches the check census). Every mutation exits nonzero and fails exactly its own family, with no assertion error (`every one exits nonzero, fails exactly one family, no assertion: True`). Two mutations fail two checks inside one family (`claim_cone_is_metric_cone`: F-5 and F-7; `claim_objects_registered`: B-1 and B-6), which is the intended single-family flip.

