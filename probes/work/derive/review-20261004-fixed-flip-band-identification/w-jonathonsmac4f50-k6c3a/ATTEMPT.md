# ATTEMPT: identify the certified unfolded Pauli zeros as band touchings

Task `J:derive:review-20261004-fixed-flip-band-identification:a1`. Worker: Claude Sonnet 5.5. Same-family, unrefereed.
Files: `check.py` (run: TOTAL PASS=29 FAIL=0, about 60 s, 80 MB), `RECOVERY_STATUS.json`.

## Plain-language summary

The cubic-flip note counts zeros of the Pauli *vector* of the E=0 Schur complement (1 zero before the flip, 3 after) but says it does not
prove that the *scalar* part also vanishes there, so a vector zero was not yet known to be a band touching. The short route in the brief works.
The comparator's spectrum is symmetric (`+-l1, +-l2`) at every real momentum and every coupling, by an exact identity. A symmetric
spectrum has equal numbers of positive and negative levels. If the complement block C has one positive and one negative level, the Schur
complement S must then have equal numbers too. A 2x2 Hermitian S with a vanishing Pauli vector is a multiple of the identity,
so it can only be balanced if it is zero. Hence the scalar part vanishes too. The route needs only the enforced `det C < 0` on the box,
and it also gives `|N0| <= |N|` everywhere on the box. It does not need family-location bounds. Those are needed only to say *which* touchings
the zeros are (the line node and the plane pair); that step is checked here but not interval-certified.

## What I read (as required)

- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (Lattice, Qubit, Admissibility, Record; the qualification that further structure needs a retained derivation).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full (approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`).
- The three source notes and the cubic-flip, census and region-(b) scripts (hashes in `RECOVERY_STATUS.json`, all six verified at
  `2868a0c453e667d1267f0e1e7403732a11893d78`; they are also unchanged on current main `a77a3449c9`).
- Nothing below uses an axiom or an approved primitive as a premise. The comparator is a supplied model (reading), as the notes say (N3).
- Prior-art search: `ai/probes` view has no attempt under this problem id. The brief's phrasing (candidate route) appears only in the task text.
  In the notes, `|N0|<|N|` is proved by weighted Taylor remainder bounds at `eps = 0` only
  (cubic-flip note, lines 59-60, 121-123 of the landed text), and the same note says scalar vanishing over the eps-range is NOT proved (lines 85-86, 116-120).
  `gh pr list --search` for related open PRs returned nothing (a weak search, not exhaustive).

## Setting and premises

- P1 (ASSUMED, supplied): H(theta, kappa) = i M(z), z_j = exp(i theta_j), the 18 terms of `check.py` (`TERMS`, equal to the census script's literal and to the terms rebuilt by the
  cubic-flip script, CHECKED by `check.py`), amplitudes 2, 2, 2J, 2kappa; real theta, real kappa, `J_x = J_y = 1`.
- P2 (ASSUMED, supplied): the cubic-flip note's two flip points (i) J=1, kappa^2=3/20 and (ii) J=5/2, kappa^2=45/44, both nodes +-x0, theta = (x0+x)(1,-1,0)+y(1,1,0)+z(0,0,1),
  kappa = kappa_node + eps with 0<|eps|<=eps0 (1/62500, 1/2250000), shifted box Q: |z|<=zeta (1/20, 1/500), X^2+Y^2<=zeta^6, `X = x+mz^2+lam eps+a1 eps z`, `Y = y+b1 eps z`.
- P3 (ASSUMED, supplied by the note's enforced inequality; recomputed in S6): on Q x eps-range the block `C = U^+ H U` keeps one positive and one negative eigenvalue (so `det C < 0`).
- P4 (ASSUMED, supplied by the note, NOT re-proved here): the Pauli vector of `Num = detC * S` has exactly 1 zero in Q for eps<0 and exactly 3 for eps>0.
- Notation: T = [W U] is the note's node basis (W, U columns of the kernel projector P and of 1-P at the node). T is invertible but NOT unitary: `|det T|^2 = 1/16` at all four nodes (S5a).
  `T^+ H T = [[A,B],[B^+,C]]`, `S = A - B C^-1 B^+`, `Num = detC*S = N0 + N.sigma` (Pauli components real because S is Hermitian).

## Numbered steps

1. **PROVED (exact, sympy; `check.py` S1a, S1b).** For symbolic `J_x, J_y, J_z, kappa, z1, z2, z3`: `M(z) + M(1/z)^T = 0`, and `det(mu - M) = mu^4 + a2 mu^2 + D` (the `mu^3` and `mu^1` coefficients vanish identically).
   Hence for every real theta and every real kappa, J: H is Hermitian and `det(lambda - H) = lambda^4 - a2 lambda^2 + D`, so the spectrum is `{+-l1, +-l2}`, `l_i` real.
   Consequences: `n_+(H) = n_-(H)`, `det H = D = (l1 l2)^2 >= 0`, and the zero level has even multiplicity (0, 2 or 4). No signed permutation of the four sites realises the pairing (searched in a scratch run), so this is an identity of the characteristic polynomial, not a visible lattice symmetry.
   The census script records the same char-poly identity (its line 884 check); the use below is what is new.
2. **PROVED (textbook).** Block factorization `T^+ H T = L^+ diag(S, C) L` with `L = [[1, C^-1 B^+],[0,1]]` when C is invertible.
   Hence `det(T^+HT) = |det T|^2 det H = det S * det C`, and Sylvester's law: `inertia(H) = inertia(S) + inertia(C)`.
   With `Num = detC*S`: `N0^2 - |N|^2 = det Num = detC * det(T^+HT) = detC * |det T|^2 * det H`.
   (CHECKED, exact: S2a on 12 random Gaussian-rational instances; CHECKED, mp: S7 on 480 box points.)
   **Convention correction to the brief:** the brief's `det H = N0^2/detC` at a vector zero omits the factor `|det T|^2` (here 1/16). The sign argument is unaffected.
3. **PROVED lemma.** Let H be Hermitian 4x4 with `n_+ = n_-`, T invertible, C invertible with `det C < 0` (one + and one - eigenvalue).
   Then `n_+(S) = n_+(H) - 1 = n_-(H) - 1 = n_-(S)`, so S (2x2, Hermitian) is either indefinite (`det S < 0`) or zero (`n_0(S) = n_0(H) = 2`).
   Therefore `det S <= 0` with equality iff `S = 0` iff `det H = 0`. (Odd case `n_0(S) = 1` is impossible because `n_+(S) = n_-(S)`.)
   Equivalent short form (the brief's): `det H >= 0` and `detC < 0` give `N0^2 - |N|^2 = detC |det T|^2 det H <= 0`.
4. **PROVED corollary (the vector-zero statement).** On any set where P1 (so step 1) and `det C < 0` hold:
   (a) `|N0| <= |N|`, with equality only where `N = 0 = N0`; (b) `N = 0` at a point implies `N0 = 0`, `S = 0`, and H has the zero level with multiplicity exactly 2 (C invertible rules out 4) and a symmetric pair `+-l`, `l > 0`;
   (c) conversely `det H = 0` (a band touching) implies `S = 0`, so `N = 0`. Thus {vector zeros of Num} = {zeros of det H} = {band touchings} on that set.
   (b) is the converse the brief asked to check: the even zero multiplicity plus invertible C closes it.
   The brief's route needs the pairing hypothesis literally: S2b (exact) shows that for unpaired `H = diag(1,1,1,-1)` one has `detC<0`, `N = 0`, `N0 = -1`.
5. **PROVED, conditional on P1-P3 (no use of P4).** At J=1 and J=5/2, throughout the shifted box Q and for all `|eps| <= eps0` (including eps=0 and both signs), the exact scalar Schur part vanishes at every
   zero of the Pauli vector, and every band touching in Q is a vector zero. This is step 4 with P3. The convention checks of the brief are done: matrix `H = iM`, Pauli decomposition `Nm = N0 + N.sigma` of `detC*S`, non-unitary T.
6. **PROVED, conditional on P3, P4 and step 8.** The box contains exactly 1 (eps<0) or 3 (eps>0) band touchings, namely the vector zeros of P4. If the landed line node and plane-(ii) pair (exact: `det H = 0` there, from the 2026-09-26 note) lie in Q, each is a band touching in Q
   (`det H = 0`), hence a vector zero by 4(c), hence they are all of them (3 distinct points for eps>0 because their z-values are `0, +-z_e` with `z_e > 0`). This identifies the certified zeros with the families without any bound on the vector map.
7. **CHECKED (mp, 60 digits, not outward-rounded; `check.py` S4-S9).**
   - S4: H Hermitian, spectrum symmetric, `det H >= 0` at 60 random real (theta, J, kappa).
   - S5a: node spectrum `{0,0,+-4J}`, `detC0 = -4` and `-25`.
   - S5b: independent numerical reconstruction of the local form (`m, lam, a1, b1`, orthogonal `n_x, n_y, n_b`, `mu = (J+2)/kappa^3`). `a1`, `b1` are 0 to 1e-24.
   - S6: independent recomputation of the complement-gap inequality: min|lambda(C0)| over the bound on `||dC||` is 3.94 (case i) and 97.4 (case ii).
   - S7: 120 box points per node: `detC<0`, identity of step 2 to 1e-44 or better, `|N0| <= |N|`, largest `|N0|/|N|` about 5e-4 (i) and 3e-7 (ii).
   - S8: Newton finds 1 vector zero (eps<0) and 3 distinct vector zeros (eps>0) at `eps = +-0.6 eps0, +-eps0`, all inside Q, with `N0 = 0` to 1e-30 and a double zero level plus a symmetric pair.
   - S9: for 164 eps values per node in `[-eps0, eps0]` the closed-form line node and (for eps>0) plane pair lie inside Q (largest fill fraction 0.575 (i), 0.695 (ii)). At them `det H`, `N`, `N0` vanish (6e-40). Newton zeros coincide with them to 1e-38.
8. **UNRESOLVED (first open step).** Interval-certified (outward-rounded) enclosure of the family points inside Q for every `eps` in the range. S9 samples a grid and uses 60-digit numerical `m, lam, a1, b1`; the source runner holds these as exact elements of `Q(i, sqrt p, sqrt q)`.
   Sampling a smooth function with margins 1.4x to 1.7x is not a proof. Needed: enclosures of `X(eps) = x_family(eps) - x0 + m z^2 + lam eps + a1 eps z` over the whole interval. For the plane pair `z ~ sqrt(mu eps)`, so a direct
   interval evaluation loses the cancellation between `x_family - x0` and `m z^2 + lam eps` (this matters in case (ii), where `eps0 >> zeta^3`); a Taylor model in `s = sqrt(eps)` is the natural fix.
9. **NOT DONE here.** P3 and P4 are taken from the note (P3 only recomputed in floating high precision, P4 not recomputed at all); no cross-model confirmation; `claim.py` / `run_probe.py` were not run and nothing was committed.

## What is new relative to the sources

- NEW (scoped, proved conditional on P1-P3): steps 3-5. A uniform, short proof that the scalar Schur part vanishes at every vector zero of the shifted box and that `|N0| <= |N|` on the whole box for all `|eps| <= eps0`. The sources prove `|N0|<|N|` only on punctured balls at eps=0 via Taylor remainders and say the eps-range scalar vanishing is not proved.
  The route uses the exact paired-spectrum identity (step 1) already recorded in the census script, but not for this purpose.
- Not new: the node census, the local normal form, the vector-zero count, the complement-gap inequality (all supplied), the family closed forms (landed 09-26 note), and the numerical coincidence of zeros with the families.
- Scope: two flip points of one supplied comparator, `J_x=J_y=1`. The argument itself (steps 1-5) is coupling-independent and applies wherever `det C<0` is established, but I checked only the stated boxes.
- Limits: same-family, unrefereed; "proved" means a complete argument is written above, not that a referee confirmed it.

## Reading (interpretation only)

The pairing identity acts as a global constraint that forbids the "wrong" local sign pattern: a point where the vector part of the Schur complement vanishes but the scalar part does not would be a gapped
point with three levels of one sign, which the symmetric spectrum excludes. So the vector-zero count, the degree computation and the band-touching count are the same count in this region.
