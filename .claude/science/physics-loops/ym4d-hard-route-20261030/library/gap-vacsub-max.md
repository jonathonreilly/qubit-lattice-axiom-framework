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
- Steps done in this order: plan steps 1 to 8, all in one session. Sections 1 to 7 below are complete; the RESULT
  line is the last line of the file.
- 2026-11-14T05:00Z: sources read in full: `library/gap-target-max.md` (row 913), `library/gap-target-check-astra.md`
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
The number enters no proof. It halves the exponent of the box size exp(integral of K) that row 913 quotes.

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
the rescaling q -> s^(-1/2) q removes s. The free photon on B is the case <q, Om q> = |curl q|^2 on the quotient
of R^E by the gauge shifts (U_s maps gauge-invariant functions to gauge-invariant functions). The constant modes have
Om = 0 and give continuous spectrum; the statement covers them, because it is a unitary equivalence. The identity
w_i = n_i is the virial theorem of the oscillator, level by level. So for the free photon (VAC-SUB)_K holds with K = 0, for every
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

## 3. STEP 2b: the K7 line and the frozen finite groups

### 3.1 Lemma BLOW (the constant pays for every fall of a prefix sum). PROVED

If (VAC-SUB)_K holds on [s_0, s_1] for a box, then for every m
   integral of K over [s_0, s_1]  >=  log(H_m(s_0)/H_m(s_1)).
In particular it is at least log(D_1(s_0)/D_1(s_1)).
Proof. Remark (a) of 1.3. QED
The proof uses only that That(s, s) is a positive compact family with a simple top eigenvalue. It holds for every
group and weight of the class (TM-gen).

### 3.2 A first-order point: the weights of Proposition V (theorem-backed) and K7 (numerics)

(a) PROVED GIVEN [Lemma REG of `library/gap-crux-fp.md` L342 (a seed that is uniform on an open interval of couplings
makes the free energy C^(1,1) there; it rests on Theorem S, Corollary S3', Lemma COV); Lemma KF; and a strong-coupling
bound of the form of `gap-seed-sc.md` Theorem 1 (iii) for the weight in question, which I did not check for these
weights]. Let a model of the class have a coupling beta_t where the free energy is not differentiable. Then for
every even b >= 256 and every K with (VAC-SUB)_K on [beta_0, beta_1], beta_1 > beta_t:
   integral of K over [beta_0, beta_1]  >  log(b/(4 ceil(log_2 b))).
Proof. Suppose not. Put t_1 = 2 ceil(log_2 b). For every s in [beta_0, beta_1], Lemma KF gives
S(b/2; b^3; s) <= S(t_1; b^3; beta_0), because (b/2) exp(-integral of K) >= t_1 and S falls in t. The strong-coupling
bound gives g(t_1; b^3; beta_0) <= 0.0101 b^3 t_1 theta^(4 t_1) with theta <= 1/2, and theta^(4 t_1) <= b^(-8). So
S(b/2; b^3; s) < 1/(2 x 5041) on the whole interval, which contains a neighbourhood of beta_t. Lemma REG with n = b/2
makes the free energy differentiable at beta_t. Contradiction. QED
Where it applies. The weights exp(beta ((1+x)/2)^p) for the p covered by the theorem of van Enter and Shlosman
(Proposition V of `library/gap-crux-fp.md` L356; the theorem is cited there, not rebuilt). The mixed weight K7
on a path across its first-order line, GIVEN that line (RECALLED numerics of Bhanot and Creutz; no theorem).
(b) How the constant blows up. GUIDE (the two-level picture; nothing proved). Near a first-order point of the box
the two lowest levels are the two phases: D_1(s) = ((l |B| (s - s_c))^2 + dl^2)^(1/2), with l the jump of the action
density and dl of the order exp(-sigma |B|) the tunnel splitting. Then rho_1 = -D_1' is l |B| times a factor that
rises from 0 to 1, and rho_1/D_1 = 1/(s_c - s) for s_c - s much larger than dl/(l |B|). Its maximum is l |B|/(2 dl),
and its integral over the approach is log(l |B| eta/dl), of the order sigma |B|. In the words of (VAC-SUB): the level
above the vacuum is the other phase; its magnetic and electric excess is the latent heat of the whole box, and its
excitation energy is the tunnel splitting. At the K7 end point the mass vanishes and the constant grows like a
power of b.
(c) What a Wilson proof must therefore contain. Lemma HF, Lemma KF, Theorem ABS and Lemma BLOW hold verbatim for
K7 and for the weights of Proposition V. Of the inputs the row lists, only the Laplacian identity changes with the
weight: Delta x_p = -12 x_p makes the Wilson action an eigenfunction plus a constant; the K7 action has two
eigenvalues (-12 and -32) and the weights of Proposition V have p of them. So a proof of (VAC-SUB) must use the
one-eigenvalue property (or another property special to the exponent linear in x) in the step that produces the
constant K. Section 4 tests whether it can.

### 3.3 The frozen finite groups Q_8 and 2T

Let G be a finite subgroup of SU(2) that contains -1 (Q_8 and 2T do), with the Wilson weight on G. H is finite
dimensional. All of Section 1 holds with sums over G in place of Haar integrals and the kinetic eigenvalues of G.

(a) Proposition FR (at a fixed box the lowest levels fall to the vacuum). PROVED.
Let c_3(G) be the number of orbits of G, acting by simultaneous conjugation, on the commuting triples in G^3. For
every box B: as beta tends to infinity, D_i(B; beta) tends to 0 for 1 <= i <= c_3(G) - 1, and S(t; B; beta) tends to
c_3(G) - 1 for every t > 0. Always c_3(G) >= 8. For Q_8, c_3 = 92.
Proof. The normalized link kernel exp(b (x(g) - 1))/sum over g' of exp(b (x(g') - 1)) tends to the unit mass at 1,
because x(g) < 1 for g not 1. So Khat_b tends to the identity. M_b tends to the indicator of W = 0, the flat
configurations of B. H is finite dimensional, so That(beta, beta) tends in norm to the projection onto the
gauge-invariant functions supported on flat configurations. Its rank is the number of gauge classes of flat
configurations on the 3-torus, which are the classes of commuting triples (the three holonomies). Eigenvalues
converge. The eight triples in {1, -1}^3 are central, so they are eight different classes. For Q_8: by the orbit
counting lemma c_3 is the number of commuting 4-tuples divided by 8. A commuting tuple lies in one of the three
cyclic subgroups of order 4, which meet pairwise and all together in {1, -1}. So the number of commuting 4-tuples is
3 x 256 - 3 x 16 + 16 = 736, and c_3 = 92. QED
(b) Consequence. PROVED from (a) and Lemma BLOW. For G = Q_8 or 2T and each box, the integral of every K with
(VAC-SUB)_K on [beta_0, beta] tends to infinity with beta. So for each b the budget (B) fails from some coupling
beta_fr(b; G) on.
(c) Uniformity in b. GUIDE and ARGUED, not proved here. The lane records the freezing couplings 1.15 (Q_8) and 2.15
(2T) as GUIDE (`library/gap-q8test-opus.md` L78, L334, from Hartung et al.). In the frozen phase the flat classes
are separated by a sheet of b^2 links, so the splittings are of the order exp(-c beta b^2), and beta_fr(b; G) is
bounded in b. A proof needs a Peierls expansion of the twist ratios; I did not write one. One number that is exact:
at beta = infinity the ratio of the twisted to the untwisted partition function on a 4-torus with one twisted plane
is, for Q_8, the number of 4-tuples with one anticommuting pair and all other pairs commuting, over the number of
commuting 4-tuples: 24 x 4/736 = 96/736, about 0.13 (an anticommuting pair is a pair of elements of order 4 in
different cyclic subgroups, 6 x 4 = 24 pairs; the other two entries must be central). It is far below the 9/10 that
the flux half (CORE) needs.
(d) The difference from SU(2), stated so that it is not over-read. For SU(2) the levels of a FIXED box also fall as
beta grows: in a small box the electric-flux levels are tunnel splittings between the two central holonomies
(RECALLED, Luscher's small-volume expansion; GUIDE). (VAC-SUB) allows this, because it lets b depend on beta_1. For
the finite groups no b works above the freezing coupling. So the test binds only through the uniformity in b,
exactly as for U(1) in 2.2.
(e) What a Wilson proof must contain. The loop equation and the Laplacian have no meaning on a finite group. So any
proof that uses Lemma F or the eigenfunction identity is not refuted by Q_8 or 2T. This is the weakest of the three
tests: it only forbids a proof from Lemma HF, Lemma KF, Theorem ABS and positivity alone.

### 3.4 Summary of the fact tests

| Model | (VAC-SUB)_K at one coupling | Budget (B) on an interval from strong coupling | Standing |
|---|---|---|---|
| Free photon (Gaussian) | holds, K = 0, equality (Proposition G) | no seed at any coupling to carry | PROVED |
| Compact U(1), Wilson | K bounded in b away from the transition (GUIDE) | fails for every b once beta_1 is in the Coulomb phase | PROVED GIVEN the inputs of 2.2 (a) |
| Weights of Proposition V | K is at least of order log b near beta_t | fails for every b across beta_t | PROVED GIVEN the inputs of 3.2 (a) |
| K7 across its line | the same; two-level picture: sup K of order l abs(B)/(2 dl) | fails, GIVEN the line (numerics) | GIVEN RECALLED numerics |
| Q_8, 2T | all levels of the flat classes fall to 0 at each box | fails for each b beyond beta_fr(b; G) (PROVED); beta_fr bounded in b (GUIDE) | PROVED in the stated part |

One conclusion covers all rows. (VAC-SUB) fails in a model exactly on intervals that cross a point where the seed
fails at every size. No inequality at one coupling separates the models. The constant K is the object, and its
selectivity is the uniformity of its integral in the box.

Stop of STEP 2. Next: STEP 3, the attack for SU(2) Wilson.

## 4. STEP 3a: the attack with the inputs the row names

Inputs: Lemma F, Lemma HF, the Laplacian identity of the Wilson weight, reflection positivity, Theorem ABS.
Outcome first. The attack does not close, and I can say why in one sentence: every one of these inputs holds
verbatim for compact U(1) with the Wilson action, so by 2.2 (a) no chain of them proves (VAC-SUB) (Proposition
NOGO, 4.3). Two exact statements come out on the way (Lemma SLICE, Lemma VIR). Both are identities that are linear
in the state. Neither has a sign after the vacuum is subtracted.

Notation. Delta is the Laplacian of the product of unit round metrics on SU(2)^E, grad its gradient.
Wt = W - 3|B| = - sum of x_p. Row 913 (F1): Delta Wt = -12 Wt. For a smooth f put d f = <grad W, grad f>.

### 4.1 Lemma SLICE (on one time slice Lemma F has no dynamical content). PROVED

(i) The operator g := d - 6 Wt equals (1/2)[Delta, Wt]. It is real and antisymmetric on L^2(Haar). It generates
the flow of the vector field grad W (the spatial Wilson flow, run backwards), implemented unitarily.
(ii) For every real smooth psi with norm 1: <psi, g psi> = 0. In other words
   <psi, W psi> = 3|B| + (1/6) <psi, d psi>.                                                    (A)
(iii) Let omega_i be the functional of level i on the cylinder, omega_i(F) = lim Tr(P_i T^n F T^n)/lam_i^(2n), P_i
the projection on psi_i. It satisfies the hypothesis of Lemma F (F3) at the links of the slice 0. Lemma F, summed
over the plaquettes of the slice 0, is exactly (A) for psi = psi_i.
Proof. (i) [Delta, Wt] f = (Delta Wt) f + 2 <grad Wt, grad f> = -12 Wt f + 2 d f. A commutator of two symmetric real
operators is antisymmetric. (ii) <psi, g psi> = -<g psi, psi> = -<psi, g psi> for real psi. Then use
W = Wt + 3|B|. (iii) Lemma F summed over the slice: 12 (3|B| - w_i) = s omega_i(<grad_0 W, grad_0 A>), where grad_0 is
the gradient in the links of the slice and A is the action of the cylinder. A = W + A_+ + A_- + (terms without those
links), A_+ and A_- the time-like plaquettes above and below. The W part gives s <psi_i, |grad W|^2 psi_i>. For A_+:
the kernel of the kinetic operator is the integral over the time-like links of exp(-s A_+), so
s omega_i(<grad_0 W, grad_0 A_+>) = -(1/lam_i) <M^(1/2) psi_i, d K M^(1/2) psi_i> = -<psi_i, M^(1/2) d M^(-1/2) psi_i>
by the eigenvalue equation, and M^(1/2) d M^(-1/2) = d + (s/2)|grad W|^2. The part A_- gives the same. The sum is
s <|grad W|^2>_i - 2 <psi_i, d psi_i> - s <|grad W|^2>_i = -2 <psi_i, d psi_i>. So Lemma F reads
12 (3|B| - w_i) = -2 <psi_i, d psi_i>, which is (A). QED

Reading. (A) holds for every wave function, eigenvector or not. So the plaquette loop equation, restricted to a
slice, says only that the generator of the Wilson flow is antisymmetric. It cannot bound w_i - w_0. Its dynamical
content is in the next lemma.

### 4.2 Lemma VIR (the virial identity of the Wilson flow). PROVED

For every eigenvector psi_i of That(s, s), and every real antisymmetric first-order operator X with smooth
coefficients: <psi_i, [X, That] psi_i> = 0. For X = g:
   s lam_i <psi_i, |grad W|^2 psi_i> = <M^(1/2) psi_i, [g, Khat] M^(1/2) psi_i>.                       (V)
Proof. psi_i = lam_i^(-1) That psi_i is smooth, and That is symmetric, so the mean of the commutator is 0.
[g, M^(1/2)] = (d exp(-sW/2)) = -(s/2)|grad W|^2 M^(1/2), a multiplication operator. Expand
[g, M^(1/2) Khat M^(1/2)] in three terms; the two outer ones give -(s/2) lam_i <|grad W|^2>_i each. QED

Three facts about (V).
(a) The Gaussian case closes. For That_s of Proposition G and X = D = <q, grad> + d/2, the dilation:
[D, M_s] = 2 s dM_s/ds and [D, Ghat_s] = 2 s dGhat_s/ds (the two factors are covariant under U_s = exp((1/2) log(s) D);
check: [D, M_s] = (<q, grad> M_s) = -s <q, Om q> M_s). So [D, That_s] = 2 s dThat_s/ds, and (V) becomes dlam_i/ds = 0. The virial identity IS the transport statement, with
K = 0. The reason is that D does not depend on the potential.
(b) The Wilson case does not close. g depends on W. [g, Khat] is a commutator of a function of the link Laplacians
with (1/2)[Delta, Wt]. To first order in the generator it is the operator [Delta, [Delta, Wt]], which contains the
Hessian of Wt. On a link l the diagonal block of that Hessian is (sum over p through l of x_p) times the metric: a
multiple of the metric, as for a dilation, but with a coefficient that is a field. The blocks between two links of a
plaquette are not multiples of anything. So (V) relates the squared force of a level to a new quantity, a kinetic
energy weighted by the Hessian of W. The next commutator brings the third derivative. The relations do not close.
(c) Every relation of this family is linear in the functional <psi_i, . psi_i>. It holds for the vacuum and for
each level. Subtracting gives a relation between vacuum-subtracted quantities of no known sign: for (A),
w_i - w_0 = (1/6)(<d>_i - <d>_0); for (V), the same with the squared force. Row 913, 6.5, found this for (F4). It is
general: a commutator identity cannot produce the sign.

### 4.3 Proposition NOGO (the inputs of the row are shared with compact U(1))

Standing: that each input holds for U(1) is PROVED (item by item below). The conclusion is a transfer argument,
GIVEN the inputs of 2.2 (a).

Each of the following holds for compact U(1) with the Wilson weight exp(s cos), with the constant shown:
- Lemma HF (the same proof; eps_n = log(I_0/I_n), n the absolute charge).
- Lemma KF, Lemma BLOW, Theorem ABS (group-blind; check 914 asks for the kinetic positivity and monotone ratios, which
  U(1) has).
- Lemma F with 4 in place of 12 (row 913, 6.1 (iii); check 914, Section 1), and the eigenfunction identity
  Delta Wt = -4 Wt.
- Lemma SLICE with g = d - 2 Wt, and Lemma VIR (the proofs use only the eigenfunction identity).
- Reflection positivity, the convexity of the free energy, the positivity of the transfer operator.
So a proof of (VAC-SUB) from these inputs alone would prove (VAC-SUB) for compact U(1) at large beta, which is false
by 2.2 (a). In the same way, by 3.2 (a), a proof must use a property that the weights of Proposition V lack; of the
inputs above only the one-eigenvalue identity qualifies, and U(1) has it.
Consequence for the row's demand ("a property that U(1) and K7 lack, named at the exact step"): with the inputs the
row names, the attack never reaches a step where SU(2) and U(1) differ. The first quantity in which the group
appears is the value of x_(p v q) - x_p x_q in Lemma F: for SU(2) it is the scalar product of the two vector parts
of the plaquette matrices, for U(1) it is sin(theta_p) sin(theta_q). Both obey the same bounds, and every identity
above treats them alike. A proof needs an input that is not on the list.

### 4.4 What the missing input has to be (ARGUED)

By 2.3 and 3.4 it is a property that (i) compact U(1) loses only where its monopoles condense, (ii) the weights of
Proposition V and K7 lose at their first-order points, (iii) holds for SU(2) Wilson at every coupling, and (iv) is
uniform in the box. Any such property implies that Wilson SU(2) has no phase transition at any finite coupling. No
identity of the commutator kind can be that property (4.2 (c)). Two kinds remain in the lane: a positivity that is
not linear in the state (the bootstrap certificate (BOOT_eps) of row 708), and a monotone quantity along a lattice
dilation (row 708, 4.5: one block step with relative errors of order one). I found no third kind in this step.

Stop of STEP 3a. Outcome: not closed; two identities PROVED; the no-go PROVED GIVEN 2.2 (a). Next: STEP 3b, the
single-level form and a solvable model in which the lemma is true, to see what its mechanism looks like.

## 5. STEP 3b: the single-level form, and a solvable model in which the lemma is true

### 5.1 The single-level form (VS-1) and Proposition ODE

**(VS-1).** There are beta_0, b_0 and, for each beta_1 > beta_0, a constant c such that for every cube B = b^3 with
b >= b_0 and almost every s in [beta_0, beta_1]:
   rho_1(B; s) <= c (1 + log^+(1/D_1(B; s))) D_1(B; s),
where rho_1 = (n_1 - n_0) - (w_1 - w_0) = -D_1' belongs to the lowest excited level of the box (Lemma HF), and
log^+ = max(log, 0). The constant c does not depend on the box.

**Proposition ODE.** PROVED GIVEN a strong-coupling gap that is uniform in the cube: D_1(b^3; beta_0) >= m_0 > 0 for
all b >= b_0 (row 836 with check 841 gives it for beta_0 below 0.3609; not re-read here). Under (VS-1), for every
b >= b_0 and s in [beta_0, beta_1]:
   D_1(b^3; s) >= exp(-(1 + log^+(1/m_0)) exp(c (s - beta_0))).
So every periodic cube has a gap at every coupling of the interval, with one lower bound for all cubes.
Proof. y(s) = log^+(1/D_1(s)) is locally Lipschitz. Where y > 0, y' = rho_1/D_1 <= c (1 + y) almost everywhere.
On the set y = 0 the derivative of a Lipschitz function is 0 almost everywhere. So (1 + y)' <= c (1 + y) almost
everywhere, and 1 + y(s) <= (1 + y(beta_0)) exp(c (s - beta_0)). QED

Where it stands among the forms. (VS-1) is the case m = 1 of (VAC-SUB)_K with K = c (1 + log^+(1/D_1)). It is row
913's remark 3c.3 (iii) made into a statement. It is not implied by (VAC-SUB) with (B), which lets K grow like log b,
and it does not imply the thermal seed, which also needs a count of the levels. It is the smallest statement I can
write that still contains the whole difficulty: one level, one box, one inequality, a constant uniform in the box.
Fact tests: it must fail for compact U(1) in the Coulomb phase, where the cubes have no uniform gap (GUIDE for the
size 1/b of D_1; the theorem behind it is the one recalled in 2.2 (a)); it fails for the weights of Proposition V if
their cubes lose the uniform gap at beta_t (the two-phase picture of 3.2 (b), GUIDE); and for Q_8 and 2T if beta_fr is
bounded in b (3.3 (c), GUIDE). For each fixed cube it fails for Q_8 and 2T as beta grows (Proposition FR, PROVED).

### 5.2 Proposition N (the O(N) model at N = infinity on a ring: the lemma holds, with a one-signed remainder)

Model. RECALLED (the standard saddle point; not rebuilt): the O(N) lattice model with action
(beta N/2) sum over bonds of |sigma_x - sigma_y|^2 on the cylinder Z_b x Z, at N = infinity. The transfer operator in
the infinite direction has free particles of mass parameter mu: a particle of momentum k in (2 pi/b) Z_b has energy
om_k, cosh om_k = 1 + M_k^2/2, M_k^2 = mu^2 + 4 sin^2(k/2). mu = mu_b(beta) solves the gap equation
   beta = Phi_b(mu^2) := G_b(0),   G_b = the Green function of (-Laplacian + mu^2) on the cylinder.
The lowest excited level is one particle at rest, D_1 = om_0. The model is asymptotically free: on the infinite
line mu is positive at every beta and falls like exp(-2 pi beta).

Statement. PROVED (by hand, for the recalled gap equation). With G the Green function on Z^2 and (G * G) its
convolution square:
(i) Phi_b(mu^2) = (1/b) sum over k of 1/(M_k (M_k^2 + 4)^(1/2)) = sum over n in Z of G(nb, 0).
(ii) The inverse rate of the gap is a sum of positive terms:
   1/K_b := -(d log D_1/d beta)^(-1) = om_0 mu (mu^2 + 4)^(1/2) sum over n in Z of (G * G)(nb, 0)
          = om_0 mu (mu^2 + 4)^(1/2) sum over x in Z_b x Z of G_b(x)^2.
   The term n = 0 is the value on the infinite line at the same mu. The terms n not 0, the windings around the ring,
   are positive. So K_b(beta) <= kappa(mu_b(beta)), kappa the rate of the infinite line: the one-signed remainder.
(iii) For mu <= 2: K_b <= 16 pi/1.76 < 29, for every b. For mu >= 2 (small beta) K_b is bounded by a function of
   beta alone, of the order 1/(beta log(1/beta)).
(iv) Every other level is a sum of om_k, and -(d log om_k/d beta) <= K_b. So (DEF_K), hence (VAC-SUB)_K and (VS-1),
   hold with a constant independent of the ring.
Proof. (i) The integral over the momentum p of the infinite direction of 1/(a - 2 cos p)/(2 pi) is (a^2 - 4)^(-1/2);
with a = M^2 + 2 this is 1/(M (M^2+4)^(1/2)). The second form is the method of images. (ii) d om_0/d mu^2 =
1/(2 sinh om_0) = 1/(mu (mu^2+4)^(1/2)), and d beta/d mu^2 = Phi_b' = -sum over n of (G * G)(nb, 0) by the resolvent
identity dG/d mu^2 = -G * G. G > 0, so every term is positive. The sum over n of (G * G)(nb, 0) is (G_b * G_b)(0) on
the cylinder, the sum of G_b(x)^2. (iii) (G * G)(0) is the integral over the Brillouin zone of
(mu^2 + phat^2)^(-2) d^2p/(4 pi^2), at least the integral over |p| <= mu of (2 mu^2)^(-2), which is 1/(16 pi mu^2).
om_0 = 2 arcsinh(mu/2) >= 0.88 mu for mu <= 2 (concavity), and (mu^2+4)^(1/2) >= 2. So
1/K_b >= 0.88 mu x mu x 2/(16 pi mu^2). For mu >= 2 all M_k^2 lie in [mu^2, mu^2 + 4], and the same formula gives a
bound in mu alone. (iv) (1/om_k) d om_k/d mu^2 = 1/(om_k M_k (M_k^2+4)^(1/2)) falls with M_k. QED

GUIDE (a run; script in the appendix; it checks the formulas and gives the true size; it proves nothing).
- Ring, sup over mu <= 2 of K_b: 5.13 (b = 4), 5.78 (16), 6.19 (64), 6.27 (256), 6.282 (1024), 6.2832 (16384 and
  65536). The supremum is 2 pi = 6.2832, the asymptotic-freedom rate, reached in large volume.
- Ring at beta = 1: K_b = 1.22, 1.67, 2.59, 4.92, 6.28 for b = 4, 16, 64, 256, 1024. It rises monotonically from the
  small-volume value to the bulk value. There is no spike at the crossover b mu of order 1.
- The same model on a b x b torus (three dimensions, which has a critical point at beta_c = 0.2527):
  sup of K_b = 12.4, 25.4, 51.7, 104.8, 211.3, 423.9 for b = 4, 8, 16, 32, 64, 128. It grows like 3.3 b, at
  b mu about 2.5. (VS-1) and the budget (B) both fail, as they must.

### 5.3 What the solvable model shows (ARGUED; a guide for the next attempt, not a step of a proof)

(a) The lemma is true there, and its proof is not an identity for the response of a level. It is an identity for
the COUPLING: the constraint equation beta = Phi_b(mu^2) writes the coupling as a monotone function of the mass
parameter, and the rate is the derivative of the inverse function. The vacuum subtraction never appears, because
mu is defined by the vacuum and the levels are functions of mu.
(b) The one-signed quantity is the inverse rate, a sum of squares of the two-point function over the cylinder. An
upper bound on K is a LOWER bound on correlations at distances up to the correlation length. Positivity of the
winding terms is the remainder with a sign: the finite box only helps.
(c) The dimension decides. mu^2 times the sum of G(x)^2 stays bounded below exactly when the sum diverges like
mu^(-2), which is the marginal dimension (two for this model). In three dimensions it tends to 0 with mu, the rate
blows up, and that is the critical point. So the property a proof must use is the infrared divergence that goes
with asymptotic freedom, not a property of the group alone.
(d) The gauge analogue of the constraint equation exists and is Lemma F: in every Gibbs state and every level
functional, s = 12 omega(x_p)/omega(Phi_p). At N = infinity the O(N) constraint closes because expectations
factorize. For SU(2) Lemma F does not close (4.2 (b)). So the solvable mechanism points at the loop equations with
a positivity input (the bootstrap family of row 708), which is where the lane already stood. I add only this: the
quantity to bound from below is the derivative of the right side of the constraint with respect to the mass scale,
at fixed box, and the box enters with a sign.

Stop of STEP 3b. The lemma is not proved for SU(2). The solvable test did not refute it.

### 5.4 A second approach: convexity of the Ky Fan sums in the magnetic coupling (Lemma CONC). PROVED; wrong side

Row 708 (Way 3) says that sums of the k largest log-eigenvalues are not convex in general. For this family they are.
**Lemma CONC.** Fix b_t. For every k >= 1 the Ky Fan sum EE_k(b_t, u) = Ehat_0 + ... + Ehat_(k-1) of That(b_t, u) is a
concave, non-decreasing function of the magnetic coupling u >= 0. The same holds in the exponent th of the kinetic
operator Khat^th, at fixed u.
Proof. The product of the k largest eigenvalues of a positive compact operator is the norm of its k-th antisymmetric
power. That power of M_u^(1/2) Khat M_u^(1/2) is exp(-u W_k/2) Q_k exp(-u W_k/2), with W_k the sum of W over the k
factors and Q_k the antisymmetric power of Khat, a positive operator. Its norm is the norm of
Q_k^(1/2) exp(-u W_k) Q_k^(1/2), the supremum over unit vectors phi of the integral of exp(-u v) against the spectral
measure of W_k in the vector Q_k^(1/2) phi. Each such integral is log-convex in u (Holder). A supremum of log-convex
functions is log-convex. So -EE_k is convex. It is non-decreasing because each ordered level is (check 914, step 5).
For the exponent th use the isospectral form exp(-th EE/2) M exp(-th EE/2) and the same argument. QED
Corollary (with Lemma HF and Theorem ABS; almost every s). On the isotropic line
   -K_el(s) EE_k(s)  <=  dEE_k/ds  <=  (EE_k(s) - EE_k^el(s))/s,
where EE_k^el is the Ky Fan sum of the kinetic operator alone. The right inequality is
s (w_0 + ... + w_(k-1)) <= EE_k - EE_k^el, from concavity between u = 0 and u = s, and n_i >= 0. So the absolute Ky Fan
sums neither fall faster than the electric rate nor rise faster than 1/s.
Where it fails for (VAC-SUB). H_(k-1) = EE_k - k EE_1 is a difference of concave functions. Concavity bounds the
magnetic EXCESS of the excited levels from above, with the vacuum's concavity defect counted k times:
   (w_1 - w_0) + ... + (w_(k-1) - w_0)  <=  (H_(k-1) - EE_k^el)/s + k (Ehat_0 - s w_0)/s.
(VAC-SUB) needs a bound from below, and the term k (Ehat_0 - s w_0) is of the order of the volume. The lemma is
group-blind, so by 4.3 it could not have been the missing input. In second-order perturbation theory the same
fact reads: the curvature of H_(k-1) in u is the vacuum's (positive, of the order of the volume) minus that of the
lowest k levels; the difference has no sign.

### 5.5 The relation behind the lemma in a scaling theory: the remainder is the pressure (ARGUED; no step of a proof)

Row 913 (6.5, 8.4) asks for "an exact relation ... with a remainder of one sign". In a theory with one length
xi(s) it exists, and the remainder has a name.
(a) Scaling form. Suppose G(t; b^3; s) = Gamma(t/xi(s), b/xi(s)) and put kappa = xi'/xi. Then
   dG/ds = -kappa (t dG/dt + b dG/db).
G = log Tr exp(-t (H - E_0)) is the pressure times volume over temperature. It is non-negative, and for a box much
larger than xi it is proportional to the volume, so b dG/db = 3 G. Then
   dG/ds + kappa t dG/dt = -3 kappa G <= 0.
This is (VIR_K) of row 708 with K = kappa and the remainder 3 kappa G: the thermal form of (VAC-SUB), with a sign.
By 1.4 (i) the left term is the plaquette shift, 6 t |B| (abar_inf - abar_t). So the relation is the
interaction-measure identity of lattice thermodynamics: (energy density - 3 pressure) = (6/kappa) x (plaquette
shift), and (VIR_K) says "the interaction measure is at most the energy density", which holds because the pressure
is non-negative. In Proposition N the same sign appears as the positivity of the winding terms.
(b) What is exact and what is not. The lattice gives dG/ds = 6 t |B| (abar_inf - abar_t) exactly, and G >= 0 exactly.
It does not give the scaling form: that the coupling moves ONLY the unit of length is the statement that the
spectrum of the box at (s, b) is the spectrum at (s', b') up to a factor, which is one block step with relative
errors of order one (row 708, 4.5). So the missing object of row 913 is not a new identity. It is this one, and
what is missing is the inequality dG/ds <= -K t dG/dt in place of the scaling form.
(c) The level form, by scale. For a zero-momentum level the response excess is spread over the box:
rho_1 = 3 |B| (dl_link - dl_plaq), with dl the shift of the local electric number and of the plaquette action
between the level and the vacuum. (VS-1) asks dl_link - dl_plaq <= c D_1/(3 |B|) up to the logarithm. Two
statements together would give it: (LOC) the level differs from the vacuum by a wave packet of size C/D_1 in local
expectations; (AMP) inside the packet the shift of the local action is of the order D_1^4, the size of a
dimension-four operator, not of order one. (LOC) alone gives |rho_1| <= C D_1^(-3), which is row 708's Way 2: the
bound ends at a finite coupling. (AMP) is an ultraviolet statement: the short-distance part of the action density
is the same in the vacuum and in a low level. That is the same kind of statement as (UNIV-K) of rows 913 and 924
(the ultraviolet increments of the free energy are the same on two tori), there for two tori, here for two states.
Row 924 leaves (UNIV-K) OPEN on (VAC-ID), (MAPCONV), (CLASS), (DENS-K). I did not work in the account's variables;
this paragraph is a pointer, not a reduction.
(d) The account. Sussman and Alpoge's dilation identity (SA 6863-6869; `library/sa-index/chunk-06.md` L64-66,
"proved in detail") is a change of units of one bare lattice. It relates no two couplings. A grep of
`library/sa-index/*.md` for "Hellmann", "action sum rule", "monoton... in beta", "derivative in beta" returns
nothing. So the account supplies the spectrum of the kinetic operator and the transfer trace (GL3-GL4, GL8, used
in Section 1) and no statement on how the transfer spectrum moves with the coupling.

## 6. The smallest unproved inequality, and the tests that can refute an attempt on it

**Smallest unproved inequality: (VS-1) of 5.1.** In full: for the Wilson SU(2) transfer operator That(s, s) on the
periodic cube b^3, with psi_0, psi_1 the two lowest eigenvectors on the whole gauge-invariant space, chi_0, chi_1
their partners for Khat^(1/2) M Khat^(1/2), W the spatial action and N(s) = sum over links of
(d/ds) log(I_(n_l)(s)/I_1(s)):
   (<chi_1, N chi_1> - <chi_0, N chi_0>) - (<psi_1, W psi_1> - <psi_0, W psi_0>)
        <=  c (1 + log^+(1/D_1)) D_1,     D_1 = log(lam_0/lam_1),
for almost every s in [beta_0, beta_1], with c independent of b. By Proposition ODE it gives a gap on all periodic
cubes at every coupling up to beta_1. OPEN. Nothing in this note bounds its left side at a coupling of order one.
The thermal seed needs in addition the prefix form (VAC-SUB) or a count of levels.

**Tests in solvable models.**
- Test DIM (run here, by hand, 5.2). The O(N) model at N = infinity. Any argument for (VS-1) or (VAC-SUB) can be
  written for this model, where every quantity is explicit. It must give a box-uniform constant on the ring (two
  dimensions) and must fail on the b x b torus (three dimensions), where sup K_b grows like 3.3 b. An argument
  that does not see the dimension is refuted by the torus. Outcome for the statement itself: (VS-1) holds on the
  ring with c = 29 (hand) and true supremum 2 pi (GUIDE); it is not refuted.
- Test GAUSS (run here, 2.1). The Gaussian family has K = 0. So it cannot refute (VS-1); it refutes only the idea
  that the lemma is a statement against the photon. An argument whose constant K does not vanish on the Gaussian
  family is not sharp but is not wrong.
- Test 2D-YM (by inspection; row 710, Proposition EL). Without spatial plaquettes W = 0, the levels are
  b eps_n(s), and rho_1/D_1 = nu_2/eps_2, the electric rate, for every ring. (VS-1) holds. This test cannot refute
  it either; it fixes the constant from below: c is at least the electric rate.
- The one test that could refute (VS-1) for SU(2) itself is not a solvable model: a measurement of rho_1/D_1 on
  small cubes through the crossover (the GUIDE row that row 913, 5.6, proposes). A value that grows with b at fixed
  coupling in the band would refute the box-uniform form and leave only the budget form (B).

**Calibration: what kind of statement (VS-1) is (ARGUED, with RECALLED theorems; no step of a proof).**
The same inequality can be written for the O(N) model on the ring Z_b x Z at finite N, with D_1 the gap of the
transfer operator in the infinite direction. Proposition ODE applies as it stands (the strong-coupling gap is
uniform in the ring). Three cases:
- N = infinity: (VS-1) holds (Proposition N).
- N = 2, the plane rotator: (VS-1) fails. RECALLED: Frohlich and Spencer (1981) prove power-law decay at large
  beta. A gap uniform in the ring would give exponential decay along the infinite direction for the limit state.
  This is the analogue of the U(1) test, and it fails in the same way: only on the window around the transition.
- N = 3: (VS-1) for all beta is the statement that the two-dimensional O(3) model has no transition, which is a
  classical open problem.
So (VS-1) for Wilson SU(2) in four dimensions is the gauge form of that open problem, not a technical lemma next to
it. The row asked for the smallest unproved inequality; this is it, and its size should be read from this list.
The transport route does not make the problem smaller. It makes it one inequality with a clean statement and
clean tests.

## 7. Summary

### 7.1 Statements and their standing (author's marks; none is checked by another model)

| # | Statement | Where | Standing |
|---|---|---|---|
| 1 | Lemma HF: dEhat_i/ds = w_i - n_i on the isotropic line; rho_i = -D_i' | 1.2 | PROVED (magnetic half is check 914, Section 4) |
| 2 | (VAC-SUB), prefix form with the budget (B); its place: (DEF_K) => (LEV_K) => (VAC-SUB)_K => transport; (VIR-log) weaker | 1.3 | statement; the implications PROVED (they are row 913 6.2 and check 914 Section 5) |
| 3 | (VAC-SUB) at beta_1 gives the seed at beta_1 | 1.3 | PROVED GIVEN Theorem SH (row 705), `gap-seed-sc.md` Theorem 1 (iii), Lemma KF |
| 4 | Proposition G: the Gaussian family is unitarily the same at every coupling; rho_i = 0 | 2.1 | PROVED |
| 5 | Compact U(1) fails the budget for every box once beta_1 is in the Coulomb phase | 2.2 (a) | PROVED GIVEN the lane's Theorem S chain, the U(1) strong-coupling seed, and the RECALLED theorem (Guth; Frohlich and Spencer) |
| 6 | In the Coulomb phase K_b is bounded in b; the failure sits at the transition | 2.2 (b) | GUIDE |
| 7 | Lemma BLOW | 3.1 | PROVED |
| 8 | A model with a kink of the free energy at beta_t fails the budget log(b/(4 ceil(log_2 b))) across beta_t | 3.2 (a) | PROVED GIVEN Lemma REG, Lemma KF, a strong-coupling bound for the weight (not checked for those weights) |
| 9 | It applies to the weights of Proposition V (theorem of van Enter and Shlosman) and to K7 (numerics) | 3.2 (a) | GIVEN the cited theorem; GIVEN RECALLED numerics |
| 10 | Two-level picture of the blow-up, sup K of order l abs(B)/(2 dl) | 3.2 (b) | GUIDE |
| 11 | Proposition FR: for a finite G containing -1, at each box the lowest c_3(G) - 1 >= 7 levels fall to 0 as beta grows; c_3(Q_8) = 92 | 3.3 (a) | PROVED |
| 12 | The budget fails for Q_8, 2T at each box beyond beta_fr(b; G) | 3.3 (b) | PROVED |
| 13 | beta_fr bounded in b; twist ratio 96/736 at beta = infinity | 3.3 (c) | GUIDE and ARGUED; the count is by hand |
| 14 | Lemma SLICE: g = (1/2)[Delta, Wt] = d - 6 Wt; identity (A); Lemma F on a slice is (A) | 4.1 | PROVED |
| 15 | Lemma VIR: the virial identity (V); it closes for the Gaussian family and is then the transport statement | 4.2 | PROVED |
| 16 | Proposition NOGO: every input named by the row holds for compact U(1) | 4.3 | PROVED item by item; conclusion GIVEN 2.2 (a) |
| 17 | (VS-1) and Proposition ODE (uniform gap of all periodic cubes from (VS-1)) | 5.1 | (VS-1) OPEN; Proposition ODE PROVED GIVEN the uniform strong-coupling gap (row 836, check 841) |
| 18 | Proposition N: O(N) at N = infinity on a ring; inverse rate = sum of squares; K_b <= 29 for all rings | 5.2 | PROVED for the RECALLED gap equation |
| 19 | The run: sup K_b = 2 pi on the ring; 3.3 b on the b x b torus | 5.2 | GUIDE |
| 20 | Lemma CONC and its corollary (two-sided bound on dEE_k/ds) | 5.4 | PROVED GIVEN Theorem ABS for the left side |
| 20b | In a scaling theory dG/ds + kappa t dG/dt = -3 kappa G: the remainder of one sign is the pressure; (LOC) and (AMP); link to (UNIV-K) | 5.5 | ARGUED |
| 21 | Calibration: (VS-1) holds at N = infinity, fails for N = 2, is the classical open problem for N = 3 on the ring | 6 | ARGUED, with RECALLED theorems |
| 22 | (VAC-SUB) for SU(2) Wilson at any coupling of order one | all | OPEN |

### 7.2 Answers to the three steps of the row

- STEP 1. (VAC-SUB) is stated in 1.3: the prefix sums of the response excess rho_i = (n_i - n_0) - (w_i - w_0) are at
  most K times the prefix sums of the excitation energies, almost everywhere on [beta_0, beta_1], with the integral
  of K at most log(b/(2 ceil(log_2 b))). It is (KF-LEV) for all pairs of couplings, and (SUPER-D) for all pairs.
  With check 914: it is weaker than (DEF_K) and stronger than (VIR-log); the vacuum is the global one.
- STEP 2. The free photon passes with K = 0 (Proposition G). So the first alternative of the row ("fails for the free
  photon") is false. The second alternative ("then it is the wrong form") does not follow: compact U(1) fails
  through the budget across its transition (2.2), K7 and the weights of Proposition V fail across their first-order
  points (3.2), the frozen groups fail at each box (3.3). The form is right as an implication. Its selectivity is the
  box-uniformity of the integral of K across a window, never an inequality at one coupling.
- STEP 3. Not closed. With the inputs the row names no proof exists, because compact U(1) has all of them (4.3).
  The loop equation on a slice is kinematic (4.1); its dynamical form is a virial identity that closes only for
  Gaussian weights (4.2); convexity gives the wrong side (5.4). The exact step where a property that U(1) and K7
  lack would have to enter is the step that turns a relation which is linear in the state into an inequality after
  the vacuum is subtracted. No listed input does that.

### 7.3 What was not done

- No proof of (VAC-SUB), (VS-1), or any bound on rho_1 at a coupling of order one.
- No Peierls expansion for the frozen groups (uniformity in b of 3.3 is GUIDE).
- The strong-coupling bound of 3.2 (a) was not checked for the weights of Proposition V.
- Reflection positivity was used only through the lane's lemmas (Lemma REG, Theorem S). I found no way to make it
  act on a vacuum-subtracted quantity.
- The account's variables: I did not look for a two-state form of (UNIV-K) there (5.5 (c) is a pointer only).
- Sources not re-read: rows 705, 704, 836, 841, 843, 854 (cited as given), Proposition V's proof, the papers of
  Guth and of Frohlich and Spencer.
- Time: 2026-11-14 04:50Z to 05:30Z, below the 60 to 90 minutes the row allows for STEP 3. I stopped because the
  approaches of Sections 4 and 5 (named inputs, single level with a solvable model, convexity, scaling) each ended at a named step and 4.3 shows that the row's inputs cannot go
  further; more time on the same inputs would repeat them. One numeric job, under the lock, memory 68 percent free.

### 7.4 Advice (ARGUED)

The transport route stands where row 913 left it, with three things settled. (i) Its lemma has an exact statement
and correct fact tests; "it must fail for the photon" is retired. (ii) The row's toolbox cannot prove it; a
further Fable hour on the same inputs would repeat 4.1 to 4.3. (iii) The solvable model says where a proof would
live: in a constraint equation for the coupling (the loop equations) with a positivity that is not linear in the
state, and with the box entering by a sign. That is the bootstrap family (BOOT_eps) of row 708, which the owner's
rule admits only with hand-size certificates. Any new attempt should first be run on the O(N) model at
N = infinity in two and three dimensions (Test DIM): it must give a box-uniform constant in two and fail in three.

## Appendix: the GUIDE script of 5.2 (run with `python3 -I`, numpy 2.x, a few seconds; under the numeric lock)

```python
import numpy as np
def parts(b, mu, dim=2):
    k = 2*np.pi*np.arange(b)/b
    s2 = 4*np.sin(k/2)**2
    M2 = mu**2 + s2 if dim == 2 else (mu**2 + s2[:, None] + s2[None, :]).ravel()
    w = 1.0/b if dim == 2 else 1.0/b**2
    Phi = w*np.sum(1/np.sqrt(M2*(M2+4)))            # gap equation: beta = Phi
    dPhi = w*np.sum((M2+2)/(M2*(M2+4))**1.5)        # = -dPhi/d(mu^2) > 0
    return Phi, dPhi
def K(b, mu, dim=2):                                # K_b = -(d log D_1/d beta)
    Phi, dPhi = parts(b, mu, dim)
    om = np.arccosh(1+mu**2/2)
    return 1/(om*mu*np.sqrt(mu**2+4)*dPhi), Phi
mus = np.logspace(-6, np.log10(2.0), 600)
for b in [4, 16, 64, 256, 1024, 4096, 16384, 65536]:
    print(2, b, max(K(b, m)[0] for m in mus))       # 5.13 5.78 6.19 6.27 6.282 6.2830 6.2832 6.2832
for b in [4, 8, 16, 32, 64, 128]:
    print(3, b, max(K(b, m, 3)[0] for m in mus[::3]))   # 12.4 25.4 51.7 104.8 211.3 423.9
```
Finite-difference check of dPhi at b = 64, mu = 0.05: formula 38.72416, difference quotient 38.72319.
At beta = 1 on the ring the run gave mu b = 0.61, 0.84, 1.33, 2.93, 10.8 and K_b = 1.22, 1.67, 2.59, 4.92, 6.28
for b = 4, 16, 64, 256, 1024.

RESULT: (VAC-SUB) is stated exactly (prefix sums of the response excess rho_i = electric-number excess minus magnetic-action excess, against the global vacuum, at most K times the prefix sums of the excitation energies, with the integral of K at most log(b/(2 ceil(log_2 b)))); PROVED: Lemma HF, Proposition G (the free photon passes with K = 0, so the photon is not the test), Lemma BLOW, Proposition FR (Q_8, 2T: the lowest 7 or more levels of each box fall to 0), Lemma SLICE (the loop equation on a time slice is kinematic), Lemma VIR (virial identity; closes only for Gaussian weights), Lemma CONC (Ky Fan sums concave in the magnetic coupling), Proposition ODE, Proposition N (the lemma holds for O(N) at N = infinity on every ring with K at most 29, true supremum 2 pi by a GUIDE run, and fails in three dimensions like 3.3 b); PROVED GIVEN named inputs: compact U(1), the weights of Proposition V and K7 fail the budget across their transitions, and no proof exists from the inputs the row names because compact U(1) has all of them; OPEN: (VAC-SUB) itself and its smallest form (VS-1), rho_1 <= c (1 + log^+(1/D_1)) D_1 with c uniform in the cube, for SU(2) Wilson at any coupling of order one. Nothing on the crux is proved.
