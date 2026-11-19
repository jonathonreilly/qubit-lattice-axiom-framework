lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:12Z

# gap-mini-branch-fable (row 1179): the Wilson branch selection

Research-stage working state. Nothing here grants status. Pinned commit 6a3a26b93.
Every statement below carries one label: PROVED (written proof in this file, not yet checked by
another model), ARGUED, GUIDE (numeric or heuristic, never a proof step) or OPEN.

## 0. Plan (written first, 2026-11-19 21:12Z by `date -u`)

Moves: the wall (W) of row 720, in the exact forms of rows 1175 and 1177
(twist cost o(N^2/log N), or the planar tension test), given a one-cube physical neutral upper bound.

Steps, one per response, each appended here before the next:

1. Read `library/gap-council-synthesis.md`, `parts/gap.md` (methods 1-36, route registry), the FINISH
   RESULT lines of rows 1143-1177, and the two latest files (`gap-solve16-astra62.md`,
   `gap-solve17-astra62.md`). Record the exact statement of the branch selection in Section 1.
2. Repo search and duplicate check (`library/open-core.md`, FINISH rows, cross-branch) for each
   candidate attack, recorded in Section 2 before any attack.
3. Attacks on the selective inequality, each ending in a proof, a disproof or a precise obstruction
   theorem. Section 3 onward.
4. Re-read of every PROVED item, then the RESULT line.

## Status log

- 21:12Z file created; reading inputs.
- 21:13Z read: FINISH rule sections, GOAL.md, `gap-council-synthesis.md`, `parts/gap.md` L1-160 (formulation, methods 19-36, lead rules, obligations to row 1072), FINISH RESULT lines of rows 1141-1178 and the sibling rows 1180 (neutral bound) and 1181 (free method). Row 1178 (gpt-6.2-astra, continue chain on (W)) runs in parallel. Next: the exact statements of rows 1175 and 1177.
- 21:18Z read `gap-solve16-astra62.md` L1-135 (statements (1)-(13)). Section 1 below written from it.

## 1. The statement (from row 1175, `gap-solve16-astra62.md` L59-64; unchecked there)

Fixed bare coupling beta = beta_j, symmetric periodic lattice torus N^4 with 4 | N. Z_0 is the periodic Wilson SU(2)
partition function, Z_14 the one with the elementary centre twist in the (1,4) plane (the sign of the coupling is
reversed on one co-closed stack of N^2 plaquettes), and zeta_beta(N) = Z_14(N^4)/Z_0(N^4).

**Branch selection (BS), OPEN.** At each sufficiently fine fixed cutoff beta_j,

    liminf over N to infinity, 4 | N, of (log(2 + N)/N^2) [ - log zeta_beta_j(N) ] = 0.          (6)

Row 1175 proves (unchecked): given the one-cube physical neutral bound (row 1161's premise, the item of row 1180),
(BS) is equivalent to (W). In the competing branch every nonzero twist obeys
Z_B/Z_0 <= 64 exp(- c_q (N/n_0)^2 / log(2 + N/n_0)) (its (4)); in the periodic branch zeta tends to 1.

Facts used below, all elementary:

- (F1) Trivial area bound: - log zeta_beta(N) <= 2 beta N^2 (the stack has N^2 plaquettes). So (BS) asks for a gain
  of a factor o(1/log N) over the trivial bound, at fixed beta, with constants free to depend on beta.
- (F2) (BS) is a statement at fixed bare coupling and growing lattice volume. It contains no physical scale.
- (F3) For compact U(1) the uniform spread of the flux pi over a (1,4) torus gives - log zeta <= beta pi^2/2 for
  every N and every beta (Jensen with the shift theta_p -> theta_p + pi/N^2; the odd term vanishes by charge
  conjugation). So (BS) alone holds for compact U(1): it is not the selective statement. The selective content of
  (W) then sits in the neutral premise (row 1180's item). This agrees with the row's remark that every positive
  result so far is non-selective.
- 21:33Z read `gap-solve17-astra62.md` in full (planar tension test (7), bounds (14), (25), (26), obstruction (33), (35)). Section 2 written.

## 2. Where blind derivations land (no new claim in this section)

Before reading row 1177's spreading sections I derived the following by hand. Each one is on file, so none is
claimed here.

| Blind derivation | On file |
|---|---|
| Jensen with fixed (configuration-independent) insertions at half-links gives, after gauge averaging at each plaquette corner, the cost beta <w_p> sum_p [1 - eta_p prod_corners cos c], and a per-site parity constraint forces order one cost per transverse site: area law | thin-stack and Mack-Petkova stack bound, row 1175 (12), (14); row 1177 L32 |
| A spread vortex with a field-built colour axis pays beta a^2 abs(D n)^2, and abs(D n)^2 is at least c/beta on typical fields: area law with a coefficient independent of beta | row 1141 (2); row 1177 (14), (26), obstruction (33)-(35) |
| The exact sewing identity (1-z)/(1+z) = E_nu prod tanh(J_x) | row 1147 (16)-(19); row 1177 (24) |
| Twist = ratio of the weights of the two SO(3) bundle classes; frozen Q_8 has twist eaters and ratio 96/736 | rows 737, 744, 878, 1130 (counts 736, 96) |
| The 2D reading of the planar test: sigma_beta(w) is about 2 exp(-F_v(w)), F_v the free energy of one vortex spanning the transverse w x w torus | row 1177 (8), (13), the Z_2 plane model at L361 |
| Renormalization-group spreading gives at best an area law with coefficient about xi(beta)^(-2), and the competing branch allows a vortex tension that small | consistent with row 1177 (25), (31); set-aside method 23 |

Reading of the state (ARGUED): at fixed beta every first-moment or quadratic comparison is an area law in the
width (row 1177 (33)). (BS) asks for less than area by more than a logarithm. In a hypothetical competing branch
the vortex tension in physical units is at most of order (seed size)^(-2), far below what ultraviolet control can
exclude. So no argument that reads only scales below the seed size can select the branch.

## 3. Candidate: branch constancy along a path of couplings (to be checked against the lane before any claim)

Idea. Both branches are certified by finite-volume strict inequalities (a seed with margin q at one size, improved
by Theorem S at larger sizes), which are open conditions in the coupling. They exclude each other. Row 1161 says
that the neutral premise forces one of them. So on any connected set of couplings where the neutral premise holds,
the branch is constant; at strong coupling the branch is the periodic one. Then (BS) at beta_j would follow from the
neutral premise at every beta in (0, beta_j], with no flux input at all. Next step: grep the lane for this argument
(continuity method M5, (NOCRIT), carry rows 978, BR-3), then write it as a theorem with exact hypotheses, or name
the match and drop it.

Status of Section 3 (21:41Z): **the candidate is on file. Match: Corollary R6 of row 737 (`gap-means-max.md` 4.7,
"the flux phase cannot change while an even seed exists; argued, the continuity step is not written with
constants"), with the continuity method (M5) of the same file (2.5), Lemma CONT of row 1072
(`gap-bridge-exercise-opus.md` 3.2) and (NOCRIT) of row 709.** Not attacked as new. What R6 gives in the present
notation: (BS) at beta_j follows from the fixed-coupling neutral premise at every beta in (0, beta_j]. The closed
half of the method (the premise on the whole interval) is the lane's "no transition on the path", which is the
target again ((M5): absent, counterexample in the class).

Two paths other than the Wilson axis, checked by hand here (ARGUED, belief-grade inputs on the phase diagram):
- the mixed fundamental-adjoint line of constant beta_F + (8/3) beta_A from the pure adjoint axis (where zeta = 1
  identically) crosses the Z_2 first-order line near beta_F = 0.44 at large beta_A, so the neutral premise fails on it;
- the one-plaquette weight 2 cosh(beta w_p + gamma), gamma from 0 (twists free, zeta = 1) to infinity (Wilson):
  in the monopole-free approximation its twisted partition functions are the convolution over H^2(T^4; Z_2) of
  the Wilson twist sectors with those of the Z_2 gauge theory at coupling gamma, so it carries the Z_2
  transition at gamma near 0.44. Both paths are worse than the Wilson axis.

## 4. Is the branch selection on the path to the Jaffe-Witten gap? (question raised 21:41Z; reading next)

Observation to test against the lane's files: in BOTH branches the selected seed (Z or V) contains the periodic
centre-neutral sector. So the neutral premise alone should give the gap of the centre-blind sector at every larger
size (Corollary R4 of row 737 says this for the even seed (ES)). The Jaffe-Witten gap concerns local gauge-invariant
observables, which are centre-blind. If the consumer (Propositions P, P' of `gap-seed-limit.md`) reads only that
sector, then (BS) is needed for (W) as worded (flux sectors included) and for confinement, but not for the
Jaffe-Witten gap. Row 1052 (Lemma FLUX-W, target T_JW-lat) and its checks 1054, 1055 are the place to compare.

Findings so far on the question of Section 4 (21:44Z; all from the lane's own files, lines grep-verified):

- Row 1161 (`gap-solve9-astra62.md` L101-105, equation (7); checked by row 1162, HOLDS): under the neutral premise
  the Pfaffian sum obeys S_kappa(t) <= 113 eta "in either case, even when the alternative varies with the cutoff",
  and "the lane's Theorem S-w propagates this seed and gives the gap on its centre-blind local observable space
  under the lane's limit hypotheses. This does not yet give the assigned periodic wall in the second alternative."
- Row 731 (`gap-flux-exercise.md` 8.4): Corollary EV, any one of the three seeds (periodic, full, kappa) gives
  (G_ev) at all sizes; Theorem EV-L (d) (L135-145, proof 8.2; cross-provider check row 732, HOLDS): under (G_ev)
  every limit of the periodic symmetric tori clusters at rate m_0 on the centre-blind class in all four directions.
- The same file L18 and L465, `gap-finishline-opus.md` 2.6 (row 837) and `gap-dichotomy.md` (row 1024): the passage
  from Theorem EV-L to the transfer operator of the limit and to the continuum (Theorem L3 (e), Propositions P, P'
  of row 700 with the centre-blind class in place of all local functions) "was not rewritten" ("OPEN, expected
  routine"). No hit for it in `library/open-core.md`, the FINISH rows or `library/open-registry.md`.
- `parts/gap.md` L200 records row 1161 as "Open: the physical neutral upper bound and the flux-branch choice" and
  does not record that the gap clause needs only the first.

So the branch selection of this row is on the path of (W) as worded (flux sectors included, that is confinement on
tori), and by the lane's own theorems it is not on the path of the Jaffe-Witten gap clause, up to the one step
never written. Section 5 writes that step.

## 5. The even-sector consumer, written out (21:47Z)

This section writes the step that rows 731, 837 and 1024 mark "not rewritten": Theorem L3 (e) and Propositions P,
P' of row 700 for the centre-blind class. Every step cites a lane statement. Nothing here is about twists.

### 5.0 Inputs and their standing on file

| Input | Where | Standing on file |
|---|---|---|
| (TM-tw), twisted transfer operators | `gap-transfer-twisted.md` Theorem TW-T (row 1004) | check 1008, same provider, HOLDS |
| (S): Lemmas K, X, E, E', Theorem S | `gap-crux-restate.md` (row 697) | lane checks rows 698, 699 |
| Lemma W, Theorem S-w, Corollary EV | `gap-flux-exercise.md` 8.4 (row 731) | cross-provider check row 732, HOLDS |
| Lemma CB, Lemma MX, Lemma L1-ev, Theorem EV-L (c), (d) | `gap-flux-exercise.md` 8.2 | same check |
| (L): Lemma FE, Lemma RPc, Theorem L3 (a), (c) | `gap-seed-limit.md` 4.2-4.3 (row 700) | checked row 703; cross-provider row 723 |
| Statements (1), (3), (5a)-(5c), Lemma E | `gap-os-equiv.md` (row 668) | "checked, HOLDS for these parts" (`gap-seed-limit.md` Section 7 table) |
| One periodic cube, equation (7), consumer | `gap-solve9-astra62.md` L99-105, L113-148 (row 1161) | check 1162, HOLDS after a credit correction |

Notation as in those files. Direction 1 or 4 is time as each file says; the statements below do not depend on it.

- A is the class of local functions F on Z^4 with F(g.U) = F(U) for every map g from the sites to (+1, -1),
  where (g.U)(x, mu) = g(x) g(x + mu) U(x, mu). This is condition (i) of `gap-flux-exercise.md` 8.2. Functions of
  finitely many plaquette traces, and of traces of contractible closed loops, are in A.
- V_A is the set of F in A with time range in [0, infinity). Theta and tau_t are the time reflection and the time
  translation of `gap-seed-limit.md` Lemma RPc and 4.3.
- (G_ev) for a sequence of integer sides L_i -> infinity: there are n_i <= L_i/2 with S_ev(n_i; L_i^3) -> 0,
  L_i - n_i -> infinity, and m_ev(L_i^3) >= m_0 > 0 for all i (hypothesis of Theorem EV-L (d)).

**Lemma A-cl (closure; PROVED).** A is a complex algebra with unit. It is closed under complex conjugation, under the
translations of Z^4, under the hypercubic group, and under Theta. V_A is a complex vector space with
tau_t V_A in V_A for every integer t >= 0, and conj(Theta F) G is in A for F, G in V_A.

Proof. Sums, products and conjugates of functions invariant under every g are invariant under every g. A lattice
symmetry s (a translation, a signed permutation of the axes, or the reflection theta) maps the set of centre-valued
site functions onto itself: s(g.U) = (g o s^(-1)).(sU), because the rule (g.U)(x, mu) = g(x) g(x + mu) U(x, mu)
multiplies a link by the values of g at its two end points, and reversing a link inverts U and keeps the sign
g(x) g(x + mu). So F o s is invariant under every g when F is. The time range of tau_t F is the time range of F
moved by t. QED

### 5.1 Theorem L3-ev

**Theorem L3-ev (PROVED GIVEN (L), Theorem EV-L (d), and `gap-os-equiv.md` Statement (3), Lemma E).** Assume (G_ev)
along L_i. Let nu be a limit state of the periodic symmetric tori L_i^4 along a subsequence, restricted to A
(it exists by Theorem L3 (a) of (L), whose proof uses only Lemma FE). Then:

(c-ev) nu is linear, positive and normalised on A, with abs(nu(F)) <= norm(F). It is invariant under the
translations of Z^4 and under the hypercubic group. It is reflection positive at every site mirror: for F in V_A,
nu(conj(Theta F) F) >= 0, and the same for the mirrors x_mu = c.

(d-ev) For F, H in A separated by d >= 1 in one of the four directions:
abs(nu(FH) - nu(F) nu(H)) <= norm(F) norm(H) exp(- m_0 d). (This is Theorem EV-L (d).)

(e-ev) D_nu := (V_A, b, tau, 1) with b(F, G) = nu(conj(Theta F) G) is a time-reflection datum with (P1), (P2), (P3)
on the time set Z. Its Hilbert space H_A(nu) has a unique vector invariant under time translation, the vacuum
Omega = [1]. Its transfer operator T satisfies norm(T^t psi) <= exp(- m_0 t) norm(psi) for every psi orthogonal to
Omega and every integer t >= 0. The spectrum of T on the complement of Omega lies in [- exp(-m_0), exp(-m_0)].
The same holds with each of the four directions as time.

Proof. (c-ev) Each periodic torus state is linear, positive, normalised and bounded by the sup norm; these pass to
the limit. Each is invariant under the translations and the signed axis permutations of its torus (proof of
Theorem L3 (c)), and these maps keep A (Lemma A-cl); so nu is invariant. Reflection positivity. Let F be in V_A.
Then X := conj(Theta F) F is in A (Lemma A-cl). By Theorem EV-L (d), the periodic state on L_i^4 and the cylinder
state on L_i^3 x Z differ on X by an amount that tends to 0. So nu(X) is the limit of the cylinder values. By
Lemma RPc of (L) each cylinder value is the squared norm of psi_F, which is >= 0. Other time mirrors: translation
invariance. Other directions: hypercubic invariance.

(d-ev) is Theorem EV-L (d).

(e-ev) (P1) is (c-ev). (P2): nu(conj(Theta F) tau_t G) = nu(tau_(-t)[conj(Theta F) tau_t G]) =
nu(conj(Theta tau_t F) G), by translation invariance on A and Theta tau_t = tau_(-t) Theta. (P3):
abs(b(tau_t F, tau_t F)) <= norm(F)^2. The unit is the constant 1, which is in V_A. Decay. Let F in V_A have time
range [a, b], a >= 0, and let t >= 1. Then conj(Theta F) has time range [-b, -a] and tau_t F has [a + t, b + t].
Both are in A and they are separated by d = t + 2a >= 1. By (d-ev),
abs(nu(conj(Theta F) tau_t F) - nu(conj(Theta F)) nu(tau_t F)) <= norm(F)^2 exp(- m_0 t). The time reflection is
an element of the hypercubic group, and it acts on links as theta; so nu(conj(Theta F)) = conj(nu(F)) by (c-ev),
and nu(tau_t F) = nu(F). Hence u(F, F; t) = nu(conj(Theta F) tau_t F) - abs(nu(F))^2 <= norm(F)^2 exp(- m_0 t)
for every integer t >= 1. This is hypothesis (X_m^C) of Statement (3) with C = V_A, C_F = norm(F)^2, t_F = 2,
m = m_0. The class C is the whole space of the datum, so the vacuum and the vectors [F], F in C, are total in
H_A(nu). Statement (3b) and Lemma E (E1), (E3) give the claim. The other directions follow from hypercubic
invariance. QED

Remark. The proof is the proof of Theorem L3 (e) of row 700 with two changes. Reflection positivity and clustering
are taken from Theorem EV-L (d) in place of Theorem L3 (c), (d). The class is V_A in place of all local functions
at non-negative times. No flux sector, twist ratio or branch enters.

### 5.2 Proposition P-ev

**(SEED-any-phys), the hypothesis.** There are ell_* > 0 and s_* < 1/5041 such that for every cutoff iota (spacing
a_iota, coupling beta_iota) there are one of the three classes w_iota in (per, full, kappa) of
`gap-flux-exercise.md` 8.3 and an integer N_iota >= 3 with N_iota a_iota <= ell_* and
S_(w_iota)(N_iota; (2 N_iota)^3) <= s_* at beta_iota. The class may change with the cutoff.

**Proposition P-ev (PROVED GIVEN (TM-tw), (S), Theorem S-w, Corollary EV, Theorem L3-ev).** Assume
(SEED-any-phys). Put M_* := log(1/(5041 s_*)) / ell_*. Then for every cutoff iota:

(a) every periodic cube of integer side L >= 2 N_iota has m_ev(L^3) >= m_0(iota) := log(1/(5041 s_iota))/N_iota
>= M_* a_iota, where s_iota is the seed value; and (G_ev) holds along every sequence of integer sides L_i -> infinity
with this m_0(iota);

(b) every limit state nu, restricted to A, of periodic symmetric tori L_i^4 with L_i -> infinity at the cutoff
iota satisfies abs(nu(FH) - nu(F) nu(H)) <= norm(F) norm(H) exp(- M_* x) for F, H in A separated in a coordinate
direction by the physical distance x = d a_iota, d >= 1;

(c) the transfer operator of D_nu satisfies norm(T^t psi) <= exp(- M_* (t a_iota)) norm(psi) on the complement of
the vacuum in H_A(nu).

Rate and constant do not depend on the cutoff, on the class w_iota, or on which of the classes holds.

Proof. (a) Theorem S-w with N = N_iota, s = s_iota, q = 5041 s_iota < 1: for every integer L >= 2N, with
D = 2^(k+1) N <= L < 2D, S_w(D/2; L^3) <= q^(2^k)/71, and every eigenvalue of T^w on L^3 other than the simple
lambda_0 is at most lambda_0 exp(- m_0(iota)). The even sector (0; 0) belongs to each of the three sector sets
(Lemma W (c)), so S_ev <= S_w and m_ev(L^3) >= m_0(iota) (proof of Corollary EV). Also
m_0(iota) = log(1/(5041 s_iota))/N_iota >= log(1/(5041 s_*))/N_iota = M_* ell_*/N_iota >= M_* a_iota. For a
sequence L_i -> infinity put n_i = D_i/2 <= L_i/2; then S_ev(n_i; L_i^3) <= q^(2^(k_i))/71 -> 0 and
L_i - n_i >= L_i/2 -> infinity. (b) Theorem EV-L (d) with m_0 = m_0(iota), and m_0(iota) d >= M_* a_iota d.
(c) Theorem L3-ev (e-ev). QED

### 5.3 Proposition P'-ev

**Proposition P'-ev (PROVED GIVEN Proposition P-ev and `gap-os-equiv.md` Statement (5a)-(5c)).** Let iota_j be
cutoffs with a_(iota_j) -> 0 for which (SEED-any-phys) holds. Let nu_j be limit states as in P-ev (b), and
D_j := D_(nu_j), read on the time set a_(iota_j) Z. Let D_inf be a continuum time-reflection datum with (P1)-(P3)
and C a class of its observables with maps iota_j: C -> V_A (centre-blind lattice versions at non-negative
times) such that (H2) holds (for each F in C the diagonal truncated reflected functions of the lattice versions
converge at each time t > 0, in the sense of (H2) there), and (TOT) holds (the vacuum and the vectors of C are
total in the Hilbert space of D_inf). Then D_inf has a unique vacuum and, with time continuity (P4),
spec(H) lies in (0) union [M_*, infinity).

Proof. (H1) of Statement (5) holds for the data D_j with m_j = M_* and S_j the whole complement of the vacuum in
H_A(nu_j): this is P-ev (c) in the time unit a_(iota_j). Apply (5a)-(5c). QED

Remark (the sector form). One may keep the full datum of row 700 on all local functions and take S_j to be the
closed span of the vectors Q_j[F], F in V_A. Statement (5) allows this ("a smaller S_n is the gap on the sector of
the class"), and (3a) with C = V_A gives the bound on S_j. Then no restriction of the lattice state is needed.
