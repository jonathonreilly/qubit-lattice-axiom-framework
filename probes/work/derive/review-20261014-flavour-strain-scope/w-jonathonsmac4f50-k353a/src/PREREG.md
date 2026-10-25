# X2 pre-registration (written 2026-10-14 ~14:25Z, before any X2 script was run)

Combination X2: the walker's hw1 corners as three generations, T_d as chirality, the mirror
{hw0, hw2, hw3} (or hw2 after F6's bilinear) gapped by a filtered, cube-spread, Spin(10)-symmetric
interaction. The decisive many-body question (does the mirror gap with no massless composite) does not
fit this budget in any dimension where it decides anything (F1 sec. 5, F4 dimension remark). What fits is
an exhaustive finite certificate for the X2-specific structural claims. Each item has a fixed reading.

Script: `scripts/x2_cert.py` (one process, OMP_NUM_THREADS=2, < 0.25 GB). Output `scripts/x2_cert.out`.

## T1. Corner-label selection rules (exhaustive over Z2^3)

With exact single translations, low-energy modes carry a conserved corner label in Z2^3; an operator is
allowed iff its labels sum to 0. Light set Lt, mirror set M.
- Splits: A (Lt = hw1, M = hw0+hw2+hw3); G (Lt = hw1+hw3, M = hw0+hw2, the T_d grading);
  plus an exhaustive scan over every assignment of the 5 non-hw1 corners to M or "extra light".
- Classes counted: light*mirror^3, light^3*mirror, A^c B B landing on a mirror label, A A B B.
- **Prediction (my claim):** (a) for A, light*mirror^3 and light^3*mirror are allowed (F1's stated rule
  fails for the walker 3-generation split); (b) for G both are forbidden; (c) no assignment with exactly
  three light corners (hw1) forbids both odd-leg classes; (d) A A B B is allowed in every split.
- **FAIL of my claim:** any assignment with light = hw1 only that forbids both odd-leg classes, or A
  forbidding them.

## T2. Filter covariance and exact corner decoupling

- Build the walker H_W = sum_a sigma_a sin p_a and two filters on an L = 4 torus: f_NN = (1 - s)/2 with
  s = sum cos p_a, and F1's f = 1 - sum_mu sin^2(p_mu/2) prod_{nu != mu} cos^2(p_nu/2). Build all 24
  proper cubic rotations about a site, with the SU(2) spin lift, and the three unit translations.
- **PASS:** every commutator of a rotation or translation with H_W and with F is <= 1e-12; f vanishes
  at the three hw1 corners and at no other corner; F1's f has an isotropic positive Hessian at hw1.
- Fock check, L = 2 torus (16 modes, 2^16 states): random Hermitian, number-conserving quartic built only
  from psi_S = F psi. **PASS:** ||[H, psi(e_i)]|| <= 1e-10 for the three hw1 corner modes, and the
  control (the same quartic built from unfiltered psi) gives a commutator >= 1e-2.

## T3. Is F6's 3L + 3R reduction protected?

- Free walker + M_f = i eps F (f = s(s^2 - 1)) + delta * i eps F_1 (f_1 = s, also cubic-invariant,
  Hermitian, Spin(10)-blind). Scan delta.
- **Prediction:** the hw1 nodes gap with gap = |delta| * |s(hw1)| = |delta| (linear), so F6's reduction
  needs one real tuning; the light/mirror pair then shares an FCC momentum.
- **FAIL of my claim:** hw1 stays gapless for delta != 0.

## T4. Generation splitting, CKM and strain (exhaustive over subgroups)

Group: proper cubic rotations O (24) times corner translation signs Z2^3, acting on the three hw1 corner
modes as signed permutations, and on traceless symmetric strain through the rotation part only. Enumerate
every subgroup H (closure of all generator pairs). For each H: the commutant of its generation action
(invariant mass matrices), whether generic invariant M has 3 distinct eigenvalues, whether the commutant
is commutative (then any two invariant mass matrices share eigenvectors: CKM is a permutation), and the
dimension of H-invariant traceless symmetric strain.
- **Prediction:** (1) 3 distinct masses <=> the image of H is not S3-type; (2) nontrivial CKM
  (non-commutative commutant) with 3 distinct masses occurs only for H with no element of order 3;
  (3) every such H has >= 1 invariant traceless strain component; (4) H = T (tetrahedral rotations):
  3 distinct masses, commutative commutant (CKM trivial), 0 invariant traceless strain.
- **Reading if all hold:** strain-safe splitting (no first-order traceless strain) is possible for masses
  but not with nontrivial mixing: realistic CKM forces an axis and a first-order strain channel in the
  flavour sector. **FAIL:** any H with nontrivial CKM, 3 distinct masses and 0 invariant strain.

## T5 (locator only, NN-forced; not evidence for or against Golterman-Shamir)

Reduced free model: psi (walker) + composite chi (two components) coupled by Delta f(k) (F1's f), chi
either flat or with mirror-chirality walker dispersion. Record where the unpaired zero modes sit.
**Expected:** psi's hw1 nodes plus chi's nodes at hw1 (vector-like), i.e. the GS signature sits at the
light corners. Any other location is recorded as found.
