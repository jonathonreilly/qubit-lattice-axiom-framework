lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:50Z

# gap-vacsub-max (row 934): the vacuum-subtraction lemma of the transport route

Author: Claude Fable 5.2 (max), Mac mini worker, pinned at commit 0865f2344. Not yet checked by the other model
(check row 935). Research-stage working state. Nothing here grants status.

Moves: the crux of the gap lane (transport of the thermal trace along the Wilson coupling, ranked first by row 913).
Row 913 stopped at the vacuum subtraction. This item states that stop as one lemma (VAC-SUB), runs its fact tests,
and attacks it for SU(2) Wilson.

Labels used below: PROVED, CONDITIONAL (on named inputs), GUIDE (a run or a heuristic, no weight), OPEN.

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. Read row 913 (`library/gap-target-max.md`) and check 914 (`library/gap-target-check-astra.md`) in full; row 708
   (`library/gap-mid-max.md`) only where 913 cites it. Duplicate check: grep `library/open-core.md` and the FINISH
   rows for the vacuum-subtraction lemma.
2. STEP 1 of the row: state (VAC-SUB) exactly, with check 914's corrections.
3. STEP 2a: fact test on the free photon / U(1).
4. STEP 2b: fact tests at the K7 first-order line and at the frozen Q_8 / 2T transitions.
5. STEP 3a: attack (VAC-SUB) for SU(2) Wilson: Lemma F, Hellmann-Feynman, the Laplacian eigenfunction identity.
6. STEP 3b: second approach (reflection positivity / the account), or a solvable-model test (2D or Gaussian).
7. If it does not close: the smallest unproved inequality, and one solvable-model test that could refute it.
8. Summary table and the RESULT line.

## Log

- 2026-11-14T04:50Z: file created. No earlier run of this item exists at the pinned commit.
- 2026-11-14T05:20Z: sources read in full: `library/gap-target-max.md` (row 913), `library/gap-target-check-astra.md`
  (check 914). Read in part, where 913 cites them: `library/gap-mid-max.md` L98-197 (row 708: Lemma 4.1, Lemma 4.2,
  Theorem TR, Remarks CH and LEV, Corollary TR1, (DEF_K), (VIR-log)); `library/gap-vir-sc.md` L67-80 (row 710, Theorem U).
- Duplicate check (rule 0a). `grep -i -E "VAC-SUB|vacuum.subtract|SUPER-D|DEF_K|VIR-log|LEV_K|KF-LEV" library/open-core.md`:
  no hit. FINISH rows that name the vacuum subtraction: 363 (`mu-uses`, another lane), 710 (`gap-vir-sc`, closed with
  (BAND-sc) not queued), 913, 914, and this row with its check 935. Row 915 (`library/prior/gap-lit-transport.md`) is
  the reading row; its RESULT: no source read supplies the bound. No other row attacks (VAC-SUB). I continue.

## 1. STEP 1: the lemma (VAC-SUB), stated exactly

### 1.1 Setting (row 913 Section 6, with the corrections of check 914)

B is a periodic box b^3 with b >= 3. H is the space of gauge-invariant functions in L^2(SU(2)^E, Haar), E the links of B.
x_p is the normalized trace of the plaquette p. W = sum over the 3|B| plaquettes of B of (1 - x_p), so 0 <= W <= 6|B|.
M_u = multiplication by exp(-u W). For n >= 1 put eps_n(b) = log(I_1(b)/I_n(b)) >= 0 and nu_n(b) = -eps_n'(b) >= 0
(positive for n >= 2 by the Bessel lemma, row 843 Lemma 3.1, check 854; nu_1 = 0). On the Peter-Weyl sector with spins
(j_l) on the links, n_l = 2 j_l + 1, the normalized kinetic operator is Khat_b = exp(-EE(b)), EE(b) = sum over l of
eps_(n_l)(b). The link projections do not depend on b. Put N(b) = -EE'(b) = sum over l of nu_(n_l)(b) >= 0, the
electric rate operator. (Sussman and Alpoge, with Claude and Codex as authors of their text, prove the convolution
spectrum and the gauge-projected transfer trace: outline GL3-GL4, GL8; CA-II 141025-141120; read by check 914.)

That(b_t, b_s) = M_(b_s)^(1/2) Khat_(b_t) M_(b_s)^(1/2), and R(b_t, b_s) = Khat_(b_t)^(1/2) M_(b_s) Khat_(b_t)^(1/2).
They have the same non-zero spectrum. The isotropic line is b_t = b_s = s. Eigenvalues lam_0 > lam_1 >= lam_2 >= ...
of That(s, s) on ALL of H: the levels of all electric-flux sectors are ordered together and measured from the one
global vacuum (check 914, Section 3). Ehat_i = -log lam_i, D_i = Ehat_i - Ehat_0 for i >= 1, H_m = D_1 + ... + D_m.
psi_i are orthonormal eigenvectors of That(s, s), and chi_i = lam_i^(-1/2) Khat^(1/2) M^(1/2) psi_i are the matching
orthonormal eigenvectors of R(s, s). S(t) = sum over i >= 1 of exp(-t D_i), G = log(1 + S).

### 1.2 Lemma HF (first-order formula on the isotropic line). PROVED (by hand; the magnetic half is check 914 Section 4)

For every s > 0 outside a set of measure zero, and for a suitable orthonormal choice of the psi_i in each eigenspace,
   dEhat_i/ds = w_i - n_i,   w_i = <psi_i, W psi_i> (magnetic action),   n_i = <chi_i, N(s) chi_i> (electric number).
Hence   -D_i'(s) = rho_i(s) := (n_i - n_0) - (w_i - w_0).
I call rho_i the response excess of level i: electric-number excess minus magnetic-action excess.

Proof. dR/ds = (1/2){N, R} - Khat^(1/2) W M Khat^(1/2) on the isotropic line (N Khat^(1/2) is bounded, because
nu_n exp(-eps_n/2) is bounded in n and there are finitely many links). With R chi_i = lam_i chi_i the first term has
mean lam_i n_i. For the second, M^(1/2) Khat^(1/2) chi_i = lam_i^(-1/2) That psi_i = lam_i^(1/2) psi_i, so its mean is
lam_i w_i. So <chi_i, R' chi_i> = lam_i (n_i - w_i). The ordered eigenvalues are locally Lipschitz (min-max), the
positive ones stay away from 0 locally, and at a multiple eigenvalue the first-order equation is the compression of
R' to the eigenspace; diagonalize it (the argument of check 914, Section 4). QED

Agreement with row 710: Theorem U (ii) is the same formula for the unnormalized operator and one state.
Absolute levels: 0 <= w_i, and n_i >= 0, so -dEhat_i/ds <= n_i. Theorem ABS of row 913 is the Ky Fan form of this.

### 1.3 The statement

Data: an even b >= 256, B = b^3, beta_0 <= 1/25600 < beta_1, and a continuous K >= 0 on [beta_0, beta_1].

**(VAC-SUB)_K, prefix form.** For almost every s in [beta_0, beta_1] and every m >= 1:
   rho_1(s) + ... + rho_m(s) <= K(s) (D_1(s) + ... + D_m(s)).
In words: the electric-number excess minus the magnetic-action excess of the lowest m excited levels of the box, each
measured against the global vacuum, is at most K times their excitation energy.

**Budget (B).** The integral of K over [beta_0, beta_1] is at most log(b/(2 ceil(log_2 b))).

**(VAC-SUB)** is: for each beta_1 there are b, beta_0 and K with (VAC-SUB)_K and (B).

**One-signed form** (what row 913, 6.5 and 8.4, asks a proof to produce): an exact relation
   rho_1 + ... + rho_m = K H_m - Rem_m   with Rem_m >= 0 for every m.

Three remarks fix the reading.
(a) Equivalent integrated form. H_m is positive and locally Lipschitz, and H_m' = -(rho_1 + ... + rho_m) almost
everywhere. So (VAC-SUB)_K holds if and only if H_m(s') >= H_m(s) exp(-integral of K over [s, s']) for all s < s' and
all m. This is (KF-LEV) of row 913, 6.2, for every pair of couplings with theta' = exp(-integral of K). By Identity 6.4
of row 913 it is (SUPER-D) for every pair. The restriction theta' <= theta(s, s') of 6.4 is not part of (VAC-SUB): it
is needed only to write the statement through the defects of Theorem ABS (check 914, Section 5).
(b) Place among the earlier statements (check 914, Section 5; none of the arrows reverses):
   (DEF_K) [rho_i <= K D_i for each i]  =>  (LEV_K)  =>  (VAC-SUB)_K  =>  S(t; B; s') <= S(t exp(-integral K); B; s)
   for all t > 0 and s < s' (Lemma KF)  =>  the conclusion of Theorem TR.
   (VIR-log) of row 708 is weaker than (VAC-SUB): it asks the thermal mean, sum of rho_i exp(-t D_i) <= K sum of
   D_i exp(-t D_i), only at the times t = ceil(log_2 b) exp(integral of K over [beta_0, s]).
   So (VAC-SUB) is not "(DEF_K) in exact form" and is not equivalent to (VIR-log). It lies between them.
(c) Finite K is not the budget (check 914). At fixed b every K_b(s) = sup over m of (rho_1 + ... + rho_m)/H_m is
finite on compact sets of couplings where the gap of the box is positive. The content is (B).

Consequence. PROVED GIVEN Theorem SH (row 705) and `gap-seed-sc.md` Theorem 1 (iii) (checked in row 704), by the
proof of Corollary TR1 of row 708 with Lemma KF in place of Theorem TR: (VAC-SUB) at beta_1 gives
S(b/2; b^3; beta_1) < 1/1650 and a gap on every periodic cube at beta_1.

### 1.4 The same statement in two other exact forms

(i) Euclidean form of the thermal mean (Lemma 4.2 of row 708 and Lemma F of row 913 with the factors of check 914).
For integer t >= 3 and s outside a countable set,
   t (sum over i of rho_i exp(-t D_i)) / (1 + S(t)) = dG/ds = 6 t |B| (abar_inf - abar_t) = (s/12) (omega_t(Q_t) - t q_inf),
where abar is the mean plaquette action on the torus t x B, Q_t = |grad A|^2 there, and q_inf is the squared force
per unit time on the infinite cylinder. So the thermal form of (VAC-SUB) bounds the time-matched shift of the total
action (equally: of the total squared force) between the torus and the cylinder by K t times the thermal energy.
(ii) Continuous-time shadow (row 913, 3c.3; exact for h = lam K_E + x W; not the Wilson operator). There
D_i = lam DK_i + x DW_i with DK_i, DW_i the electric and magnetic excesses, and on the path lam = 1/s, x = s:
   -s D_i' = D_i - 2 x DW_i.
So there (DEF_K) reads: -2 x DW_i <= (s K - 1) D_i. The magnetic action of a level may lie below the vacuum's by at
most (sK - 1)/2 times its excitation energy. This is the sentence of the row. For the Wilson operator the electric
number cannot be eliminated exactly, and (VAC-SUB) keeps both terms.

Correction to a GUIDE number of row 913, 3a.3 (i). The two-loop formula for SU(2) with beta = 4/g^2 is
a Lambda = (6 pi^2 beta/11)^(51/121) exp(-3 pi^2 beta/11) (RECALLED). So asymptotic freedom predicts the rate
3 pi^2/11 = 2.69 minus 0.42/beta, not 5.38. The published rates near beta 2.3 to 2.6 quoted in row 708 are about 3.3.
The number enters no proof. It halves the box size exp(integral of K) that row 913 quotes.

Stop of STEP 1. Statement fixed. Next: the fact tests.

## 2. STEP 2a: the U(1) fact test

Verdict first. The free photon PASSES the inequality (VAC-SUB)_K at every coupling, with K = 0 and equality.
Compact U(1) FAILS (VAC-SUB), and it fails through the budget (B) on the window of couplings around its transition,
not through any property of the photon. So the test "it must fail for the free photon" is the wrong test for a
transport statement; the transport form itself is not refuted by U(1).

### 2.1 Proposition G (the Gaussian family does not move with the coupling). PROVED

Let Om be a real symmetric d x d matrix, Om >= 0. On L^2(R^d) let M_s = multiplication by exp(-(s/2) <q, Om q>), let
Ghat_s be convolution with the probability density (s/2 pi)^(d/2) exp(-(s/2)|q|^2), and
That_s = M_s^(1/2) Ghat_s M_s^(1/2). Let (U_s f)(q) = s^(d/4) f(s^(1/2) q), a unitary. Then That_s = U_s That_1 U_s^(-1).
So the spectrum of That_s, with multiplicity and type, is the same for every s > 0. Every level has
dEhat_i/ds = 0: its magnetic action equals its electric number, w_i = n_i, and rho_i = 0 for every i.
Proof. (M_s U_s g)(q) = exp(-(s/2)<q, Om q>) s^(d/4) g(s^(1/2) q) = (U_s M_1 g)(q). The substitution y = s^(1/2) q'
gives (Ghat_s U_s g)(q) = s^(d/4) (Ghat_1 g)(s^(1/2) q) = (U_s Ghat_1 g)(q). Powers and products follow. QED

This is the transfer operator of the lattice action (s/2) sum over tau of (|q_(tau+1) - q_tau|^2 + <q_tau, Om q_tau>):
the rescaling q -> s^(-1/2) q removes s. The free photon on B is the case q in R^E, <q, Om q> = |curl q|^2, on
gauge-invariant functions (U_s commutes with the gauge shifts up to rescaling them). The identity w_i = n_i is the
virial theorem of the oscillator, level by level. So for the free photon (VAC-SUB)_K holds with K = 0, for every
box, with Rem_m = 0.

Why it passes. The Gaussian weight is covariant under a dilation of the field. The coupling is then not a parameter
of the spectrum at all. Any model with an exact scale covariance of this kind passes every transport inequality.

### 2.2 Where compact U(1) fails. PROVED GIVEN the inputs named; the location is GUIDE

(a) PROVED GIVEN [the strong-coupling seed for U(1) (the expansion is group-blind; `library/gap-skeleton-final.md`
L537: "Theorem DOB and the cluster expansion hold for U(1)"), Theorem SH and Theorem S of the lane (group-blind,
row 913 2.3), and the RECALLED theorem that compact U(1) with the Wilson action has no area law at large beta
(Guth 1980; Frohlich and Spencer 1982; `library/gap-crux-fp.md` L287 records that the U(1) test rests on a theorem
only at large beta)]. If (VAC-SUB) held for U(1) at such a beta_1, Corollary TR1 would give the seed there, hence a
gap on all cubes and an area law. So for every b and every beta_0 below the strong-coupling threshold, every K with
(VAC-SUB)_K on [beta_0, beta_1] has integral above log(b/(2 ceil(log_2 b))).
(b) GUIDE (the standard picture; nothing here is proved). In the Coulomb phase the low levels of the box are photons,
D = |k| with k in (2 pi/b) Z^3, which do not move with s at leading order (Proposition G), and electric-flux levels
D = e^2/(2 s_R b), which fall at the rate 1/s. For the Villain form the kinetic rate is exactly 1/s (eps_n = n^2/(2s)).
So K_b(s) stays bounded in b at each coupling of the Coulomb phase, and of the confined phase. The excess over the
budget is collected on the window around the transition (near beta 1.01), where the levels fall from a mass of
order one to order 1/b, and at a first-order point to a tunnel splitting.
(c) The margin is a logarithm. In the Coulomb phase the levels are of order 1/b, so a fall from a mass m_0 costs an
integral of K of about log(b m_0). The budget is log b - log(2 ceil(log_2 b)). The seed asks D_1 b/2 to be large,
which is exactly what 1/b-levels deny. So (B) excludes the Coulomb phase by the factor 2 ceil(log_2 b) and constants,
not by a power of b. The budget cannot be relaxed to C log b with C > 1 without admitting a massless phase.

### 2.3 What the test says about a proof

- An inequality at one coupling that "the free photon violates" does not exist in this form: at one coupling the free
  photon satisfies (VAC-SUB)_K with the best constant. The selectivity of (VAC-SUB) is not local in the coupling.
- (VAC-SUB) at one coupling with K bounded in b does not give a gap at that coupling (the Coulomb phase has it,
  GUIDE). The gap comes only from the seed carried from strong coupling. So a proof must hold on the whole interval
  from strong coupling, with one box.
- The step that compact U(1) must break is therefore a step that fails only where monopoles condense, near beta 1.01,
  and nowhere in the Coulomb phase. A proof whose SU(2)-specific step is "the group is non-abelian, so there is no
  photon" proves too much or too little: the photon is not the obstruction.
- This agrees with Proposition T1 of the lane (`library/gap-skeleton-final.md` L537): a tool is refuted only by a
  model in its class where its hypothesis holds and the seed fails.

Stop of STEP 2a. Next: K7 and the frozen finite groups.
