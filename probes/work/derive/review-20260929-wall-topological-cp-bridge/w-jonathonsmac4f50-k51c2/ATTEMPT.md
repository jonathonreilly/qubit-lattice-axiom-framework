# ATTEMPT: gauge/matter CP bridge on the staggered taste-singlet surface

Task id `J:derive:review-20260929-wall-topological-cp-bridge:a1`. Worker: Claude Sonnet 5.5. Same-family, unrefereed.
Labels: PROVED (full argument here), CHECKED (executed by `check.py`), ASSUMED (premise), READING (interpretation).

## 0. What was read, and the plain-language result

I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines) on current main (a77a3449c9). The registry lists three approved primitives (`scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive`). None supplies a mass matrix, an index, a phase, a gauge weight or a flux sector (PRIMITIVE_REGISTRY_CHECK.md:31-129). The source branch `claude/toe-walls-20260929` at 4bd42747e5 was fetched; all 8 listed objects match their SOURCE_MAP sha256 (see `RECOVERY_STATUS.json`). I read T41, T42, T43 attacks and kills in full, the 2026-07-02 paired-shift note (`docs/THETA_ASSEMBLY_PAIRED_SHIFT_...2026-07-02.md`) and the 2026-07-02 supplier note (`docs/THETA_SUPPLIER_FLAVORED_GRADING_...2026-07-02.md`), and the 2026-06-11 epsilon-Hermiticity note.

Plain language. The wall (T43, with T41/T42) asks for a bridge between the gauge angle and the quark-mass phase. The honest object is one operator: the 2D even-L staggered Dirac operator `D` with the taste-singlet pseudoscalar mass `i m5 Gamma_f`. I did three things. (1) I classified exactly when the determinant of `D + m + i m5 Gamma` is real or positive (it depends on whether the mass operator flips the site parity, not on "being a mass"). (2) I proved an exact finite identity splitting the first-order phase into an index-like kernel trace plus a defect proportional to the anticommutator `{Gamma_f, D}`; the kernel trace is NOT an integer on a finite lattice. (3) I proved, with explicit hypotheses, that the integer `-2Q` found numerically in the 07-02 supplier note is the signature of `Gamma_f` compressed to the kernel of `D`. That integer count and the physical phase slope (the kernel trace) are two different finite-lattice quantities; they agree only as `L -> infinity`. The route does not derive the combined phase from the axioms: every ingredient is lane-supplied.

## 1. Setting and premises

- ASSUMED P1 (lane model, not axiom content): `D = (1/2) sum_mu eta_mu [U_mu delta_{x+mu} - h.c.]`, `eta_1 = 1`, `eta_2 = (-1)^{x1}`, `eps = (-1)^{x1+x2}`, `Gamma_f = i eta_2 (C1 C2 + C2 C1)/2`, `C_mu = (T_mu + T_mu^dag)/2`, on the periodic `L x L` torus, L even, unitary links (2026-07-02 supplier note:57-98, 67). Mass operator `M = D + m + i m5 Gamma_f`, `m > 0`, `m5` real. Axioms contain no dynamics, no mass matrix, no index (MINIMAL_AXIOMS:114-130, 141-146, 175-181); `Qualification` (:85-90) says such structure needs a retained derivation or an approved primitive. None is provided here.
- ASSUMED P2: the flux sector `Q` is supplied (uniform flux with `phi = 2 pi Q/L^2`, or exact Z_4 links). `realized_state_primitive` gives state data, not a derivation of `Q` (PRIMITIVE_REGISTRY_CHECK.md:98-129).
- ASSUMED P3 (source/readout convention): `Q = (1/2pi) sum_x Arg[U1(x)U2(x+1)U1*(x+2)U2*(x)]` (principal angle in `(-pi, pi]`), mass term enters as `+ i m5 Gamma_f`, the physical phase is `arg det M`, and the gauge-side phase is `e^{+i theta_g Q}`. Section 7 shows the sign of the combined phase depends on these choices.
- All of Z_4 (Part E of `check.py`) is exact arithmetic over `Q(i)`; the uniform-flux family (Part F) is double precision.

## 2. Structure lemmas

**S1 (PROVED).** For L >= 4 even: `D^dag = -D` (links unitary, forward/backward entries conjugate with opposite sign); `{eps, D} = 0` (every hop flips `eps`); `Gamma_f^dag = Gamma_f` and `[eps, Gamma_f] = 0` (07-02 supplier L1, restated; `Gamma_f` is a two-hop operator); `||Gamma_f|| <= 1` (`||C_mu|| <= 1`, hence `||S|| <= 1`); `tr Gamma_f = 0` (two-hop terms have zero diagonal on L >= 4). CHECKED exactly on 7 Z_4 configs (E1, E1b).

## 3. Hermiticity classification (answers "exact Hermiticity conditions")

**S2a (PROVED).** If `Gamma` is Hermitian and `eps Gamma eps = + Gamma`, then `det M(m5)^* = det M(-m5)`; the phase is odd in `m5`. Proof: `M^dag = -D + m - i m5 Gamma`; `eps M^dag eps = D + m - i m5 Gamma = M(-m5)`; `det M^* = det M^dag = det(eps M^dag eps)`. Phase zero is therefore not automatic; for `Gamma = eps` it holds by the 06-11 identity `eps M eps = M^dag` (06-11 note:22, 54), a different case. CHECKED exactly (E2, 5 configs, includes configs with Im det != 0).

**S2b (PROVED).** If `Gamma` is Hermitian and `eps Gamma eps = - Gamma` (an odd number of hops, e.g. `i(T1 - T1^dag)`), then `D' = D + i m5 Gamma` is anti-Hermitian and `eps`-odd, so its spectrum is symmetric `{+-i mu}` (the same eigenvector argument as 07-02 L1), and `det M = prod (m^2 + mu_j^2) > 0` (zero modes contribute `m` each, paired). So positivity of the fermion weight holds for parity-flipping masses and fails for `Gamma_f`. CHECKED exactly (E4).

**S2c (PROVED, 2D only).** `D(U*) = conj(D(U))` entrywise, `Gamma_f(U*) = - conj(Gamma_f(U))` (the factor `i`), hence `M(U*) = conj(M(U))` and `det M(U*) = conj det M(U)`: the phase is odd under `U -> U*`. For real links (U = U*) `det M` is real. CHECKED exactly (E3). Caveat (exact, E3b): `Q(U*) = -Q(U)` holds iff no plaquette angle equals `pi`; the principal-angle `Q` is not C-odd on the branch cut (a real-link Z_2 config has `Q = 4`, real determinant). So "phase proportional to Q" can only be a statement on the admissible set (all plaquette angles `< pi`). 4D is not treated here; the T43 kill says the 4D phase is C-even (not rechecked here).

## 4. Exact first-order phase identity (Theorem B)

**S3 (PROVED).** Let `P` be the orthogonal projector on `ker D`, `R = (m^2 - D^2)^{-1}`, `D^+` the pseudoinverse, `A = {Gamma, D}`. For `m > 0`:

1. `d arg det M / d m5 |_{m5=0} = sigma(m) := m Tr[Gamma R]` (real).
2. `sigma(m) = Tr(Gamma P)/m + (m/2) Tr[ A R D^+ ]`.

Proof. (1) `d log det M = i Tr[(D+m)^{-1} Gamma] dm5`; `(D+m)^{-1} = (m - D) R`. `Tr[Gamma R]` is real (Hermitian `Gamma R`). `Tr[D R Gamma]` is purely imaginary (its conjugate is its negative, using `D^dag = -D`, `[D, R] = 0` and cyclicity). So `Re Tr[(D+m)^{-1}Gamma] = m Tr[Gamma R]` and the arg derivative is that real part. (2) Write `1 = P + D D^+`. `Tr[Gamma R P] = Tr[Gamma P]/m^2`. On the complement, `D^+ D = 1 - P` and `D, D^+, R` commute, so `Tr[Gamma R (1-P)] = Tr[Gamma R D^+ D] = Tr[D Gamma R D^+]`; adding the cyclic copy `Tr[Gamma D R D^+]` gives `2 Tr[Gamma R (1-P)] = Tr[A R D^+]`. Multiply by `m`. QED. CHECKED exactly over `Q(i)` (E5a: `p'(0) = i det(D+m) Tr[(D+m)^{-1}Gamma]` from 17-point exact interpolation; E5b; E5c the split, on free, real-link, admissible and rough Z_4 configs), and in floating point against a finite-difference of `arg det` (F5, error 1e-8).

Corollary (PROVED). If `{Gamma, D} = 0` the defect vanishes and `sigma = Tr(Gamma P)/m` for all `m`; if moreover `Gamma^2 = 1` the 07-02 L2 identity gives `arg det = 2 alpha tr(Gamma)` to all orders (prior art, `THETA_ASSEMBLY_PAIRED_SHIFT...:63-76`). `Gamma_f` meets neither condition once gauged: `Gamma_f^2 != 1` (free-field spectrum `cos q1 cos q2`), `||{Gamma_f, D}||_F` = 0.480, 0.956, 0.321, 0.640 at (L,Q) = (8,1), (8,2), (12,1), (12,2) (reproduces 07-02 supplier note:115 and the L=12 values; CHECKED F0), and `tr Gamma_f = 0` so the paired-shift value `2 alpha tr(Gamma)` would give zero while the exact Z_4 phases are nonzero (E6). Free field (`U = 1`): `{Gamma_f, D} = 0` exactly, `Tr(Gamma P) = 0`, phase exactly zero (E5d).

## 5. Spectral-flow theorem (Theorem A)

Definition (07-02 note:138-151): `H(m) = eps D - m Gamma`, `flow(m) = N_neg(H(m)) - N_neg(H(-m))`. The note says the value `-2Q` was machine-verified, not derived (note:247).

**S4 (PROVED, conditional).** Let `K = eps D` (Hermitian, spectrum symmetric under `eps`). Let `V = ker D`, `W = V^perp`, `Delta = min{|lambda| : lambda != 0}`, `Gamma_VV = P Gamma P|_V`. If `Gamma_VV` is invertible with `gamma0 = min |eig Gamma_VV|` and

`m / (Delta - m) < gamma0`,   (i.e. `0 < m < gamma0 Delta/(1+gamma0)`)

then `flow(m) = sig(Gamma_VV) := N_pos(Gamma_VV) - N_neg(Gamma_VV)`.

Proof. Haynsworth: for Hermitian `H` with invertible block `A`, `In(H) = In(A) + In(H/A)`. Take `A = K_W - (+-m) Gamma_WW`. `K` is block-diagonal in `V (+) W` (it is a function of the spectral decomposition of `D`). `K_W` has `|spec| >= Delta`, `||m Gamma_WW|| <= m < Delta`, so Weyl's inequalities keep each eigenvalue's sign: `In(A) = In(K_W) = (w/2, w/2)` for both signs (`eps` maps eigenvalue `lambda` to `-lambda`, so the spectrum of `K_W` is symmetric). Schur complement: `S(+-m) = -+m [ Gamma_VV +- m Gamma_VW A_{+-m}^{-1} Gamma_WV ]` (here `K_VV = 0`), a Hermitian perturbation of `-+m Gamma_VV` of norm `<= m * m/(Delta - m)`, using `||Gamma_VW||, ||Gamma_WW|| <= 1`. Since this is `< m gamma0`, Weyl again gives `In(S(m)) = In(-Gamma_VV)` and `In(S(-m)) = In(Gamma_VV)`. Hence `N_neg(H(m)) = w/2 + N_pos(Gamma_VV)`, `N_neg(H(-m)) = w/2 + N_neg(Gamma_VV)`. QED.

Near-kernel version (PROVED, same proof). Let `V` be the span of eigenmodes with `|lambda| <= delta`, `W` those with `|lambda| >= Delta > delta`. If `delta/m + m/(Delta - m) < gamma0` (and `m < Delta`) then `flow(m) = sig(Gamma_VV)`.

CHECKED: the Haynsworth lemma on 200 random Hermitian matrices (F1); hypotheses verified and `flow = sig` on 28 (L,Q) cases (L = 6, 8, 10, 12; Q = -3..3) at three `m` each (84 values), no failures (F2); the 07-02 tested family (L = 8, 12; Q = +-1, +-2) has `dim ker D = 2|Q|` and `sig = -2Q`, so its plateau value is the theorem's value (F3); near-kernel version at (8,3) with a 6-mode `V` on 40 admissible `m` (F9).

## 6. Finite lattice versus continuum index normalization (CHECKED / not proved)

- The integer `sig(Gamma_VV)` and the physical phase slope are different. In the small-`m` regime the slope times `m` is `Tr(Gamma_VV)`, a sum of real numbers in `[-1, 1]` (S3). Uniform flux, CHECKED (F6): `Tr(Gamma_VV) = -1.90174, -3.60579` at (L = 8, Q = 1, 2); `-1.95636, -3.82535` at L = 12; and `(1 - |Tr|/2|Q|) L^2/(pi |Q|) = 1.0009, 1.0038, 1.0002, 1.0007, 1.0001, ...` for L = 8..20. So `Tr = -2Q (1 - pi|Q|/L^2 + ...)` as a numerical fit, never the integer. (The zero-mode chirality deficit `pi/L^2` is already in the T43 kill; I only confirm it for Q = 1, 2 and L up to 20.)
- Consequence for the combined phase (CHECKED, F7): at first order `Phi_Q = theta_g Q + alpha Tr(Gamma_VV)`. Choosing `theta_g` to cancel `Q = 1` on L = 12 leaves `8.74e-2` in `Q = 2`, equal to `4 pi/L^2` within 5e-3. No single `theta_g` cancels all sectors at finite L; the mismatch is `O(Q(Q-1)/L^2)` and vanishes only for fixed Q as `L -> infinity`.
- Kernel dimension is not a function of `Q` (CHECKED): uniform flux (L = 8, Q = 3) has `dim ker D = 2`, not 6, with four near-zero modes at `|lambda| = 9.2e-4, 1.8e-3` (F4). `flow(m)` is `-2` for `m` inside the theorem's window (`m = 1.3e-4`) and `-6` for `m >= 3e-3`. The coefficient `m dPhi/dm5` is `-1.70256` at `m = 1e-6` (exactly `Tr(Gamma_ker)`) and `-5.0888` at `m = 0.05` (F10): the orders of limits `m -> 0` and `a -> 0` differ. This is outside the 07-02 note's tested family (Q <= 2); it is a scope boundary, not a refutation of the note.
- Exact Z_4 counterexamples (E6, E6c): admissible configs (no `pi` plaquette) with `Q = +-1` and no exact zero mode, `Tr(Gamma P) = 0` and `Im det M != 0`; and rough configs with `dim ker = 2 != 2|Q|` (Q = 2, 3). So "kernel dimension = 2|Q|" and "phase = 2 alpha Q" are not identities of this operator.
- The 07-02 note's description of `2|Q|` "would-be zero modes taste-split into +-lambda pairs" (note:237) does not match what I find at (8,1), (8,2), (12,1), (12,2): the `2|Q|` eigenvalues are zero to 1e-15 (CHECKED, F11). It matches the (8,3) case.

## 7. Source/readout convention (READING + CHECKED)

With P3, admissible Z_4 configs satisfy `sign(Im det M) = -sign(Q)` in all 4 cases (E6b), uniform flux has `Tr(Gamma_VV) < 0` for `Q > 0` and flips sign with `Q` (F8; exact by S2c), and the sign flips with `m5`. Hence cancellation `theta_g = -alpha Tr/Q ~ 2 alpha` needs gauge phase `e^{+i theta_g Q}` with this plaquette orientation and this sign of the mass term. Reversing either convention makes the two phases add. The combined `theta-bar` is therefore not a convention-free number: the source orientation and the sign of the mass term are inputs.

## 8. What is and is not derived

- Not derived: the operator `D`, the grading `eps`, the mass operator `Gamma_f` (a multi-link taste-singlet, absent from the site-diagonal mass class), the flux sector, the gauge weight, `theta_g`. All are lane-supplied (P1-P3).
- Nonnegative weight and mass chart. S2b/S2a show that positivity of the fermion determinant is a property of the mass chart (parity-flipping masses give `det > 0`, `Gamma_f` does not), so a nonnegative fermion weight does not select or derive the `Gamma_f` phase; with `Gamma_f` the matter weight is complex (E2, E6). This sharpens the T42 "POS" premise: it must be stated for the pair (gauge weight, mass chart), not for the gauge weight alone. No primitive is registered or implied.

## 9. NEW versus sources

Not new: staggered index and flow of `Gamma_f` (Adams; 07-02 supplier note), the `eps`-pairing/real-determinant identity (06-11 note), fixed-grading L1-L3 (07-02 paired-shift note), the coefficient `< 1` at finite L and `pi/L^2` zero-mode deficit (T43 kill), the `-2Q` numerics, the non-convergence in `m`.

New (scoped, same-family, unrefereed; no overlap found in the 231 open PR titles, title-level only, nor in docs/ or scripts/ by keyword):
1. Theorem A (S4): a proved conditional derivation, with explicit window, that the supplier's integer is `sig(Gamma_f` compressed to `ker D)`; near-kernel version; the (8,3) window as a checked boundary.
2. Theorem B (S3): the exact index-plus-defect split of the first-order phase, with the defect equal to `(m/2) Tr[{Gamma,D} R D^+]`.
3. S2a/S2b classification by `eps Gamma eps = +-Gamma`, and the exact branch-cut caveat for C-oddness of `Q` (E3b).
4. Exact Z_4 counterexamples (E6, E6c) to kernel dimension `2|Q|` on admissible configurations.

## 10. First unresolved step and remaining obligations

First unresolved step: **S4's hypothesis, step 5 -> 6: prove, for the uniform-flux family, that `dim ker D = 2|Q|` and `Gamma_VV` is negative definite with `gamma0` bounded below.** Checked only on the families above; fails to hold in the regime `Q` large against `L` (F12: (8,3), (8,5), (10,3), (12,5), (4,3) all have `dim ker D = 2`). A closed form for the spectrum of `Gamma_VV` (fit: `-1 + pi|Q|/L^2`) is not proved.

Remaining: (a) a bound on `|Tr(Gamma_VV) - sig|` and on the defect term; (b) 4D (`Gamma_f` there has no factor `i`, so the C-parity flips; unchecked here) and SU(3); (c) the continuum/index-normalization statement with a stated scaling (`a -> 0` at fixed physical volume); (d) the gauge-side supplier, positivity of the combined weight and reflection positivity (T42); (e) why the mass operator is `Gamma_f` at all (axiom-level supplier). Negative claims here are scoped to this operator and these finite families; none meets N1-N8 and none is a no-go.

Files: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-poison-ivy-oak-treatment-90452e/a67d71b1-0c50-4041-92e4-07c78ad7ebea/scratchpad/attempts/review-20260929-wall-topological-cp-bridge/{ATTEMPT.md, check.py, RECOVERY_STATUS.json}`.
