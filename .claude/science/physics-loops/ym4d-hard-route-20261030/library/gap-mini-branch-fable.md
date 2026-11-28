lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:12Z

# gap-mini-branch-fable (row 1179): the Wilson branch selection

Research-stage working state. Nothing here grants status. Pinned commit 6a3a26b93.
Every statement below carries one label: PROVED (written proof in this file, not yet checked by
another model), ARGUED, GUIDE (numeric or heuristic, never a proof step) or OPEN.

## Result in short (written last; details and labels in Sections 5-8)

- The branch selection (BS) is not proved. The competing branch is not proved. Both stay OPEN.
- (BS) is not on the path of the Jaffe-Witten gap clause. Row 1161 (7) gives a flux-independent seed in both
  alternatives. Section 5 writes the even-sector consumer that rows 731, 837 and 1024 left unwritten. Theorem BP
  (Section 6): the one-cube physical neutral bound alone gives a cutoff-uniform gap on the centre-blind sector and,
  with the continuum datum, the gap clause. (BS) is needed only for (W) as worded, that is for confinement on tori.
- Corollary FB (7.5): at the cube of the premise, (BS) is an order-one bound on one flux energy.
- Proposition J (7.1): no first-moment comparison with fixed multipliers beats the area law.
- Routes already on file are named, not attacked again (7.2, 7.3).

## Repo search (run 22:00Z, after the lane-folder search; rule "Repo first")

- Lane folder (this branch at 6a3a26b93): `library/open-core.md`, `library/open-registry.md`, the FINISH rows and
  the `gap-*` files were searched with `grep -n` for each candidate before it was written (matches in Sections 2, 3,
  4, 7). The even-sector consumer of Section 5 has no owner there: the only hits are the three "not rewritten" notes
  (`gap-flux-exercise.md` L18 and L465, `gap-finishline-opus.md` 2.6, `gap-dichotomy.md` L298).
- Other branches: bare, blob-less, depth-1 fetch into a scratch folder of origin/main (8b11ae2) and the heads of pull
  requests 10114 (f76f6c6), 10133 (89faef2), 10134 (1e70c72), 10141 (a2f6a43), 10144 (1f20846), 10149 (7fc6b1a).
  Scope: the 248 files whose path holds "mass-gap", "MASS_GAP" or a name `gap-*.md`. Pattern: "EV-L", "centre-blind",
  "center-blind", "even-sector consumer", "T_JW-lat", "flux-independent seed", "Pfaffian seed". Hits: six files, all
  under `research/mass-gap/` on main (README.md L17, ROWS.md rows 731, 732, 735, and the landed copies of
  `gap-flux-exercise.md`, its check, `gap-form-exercise.md`, `gap-skeleton-final.md`). They are the lane's own rows
  731-735; none writes the consumer for the centre-blind class. No hit on any pull-request head.
- What the search does not show: files outside those 248 paths were not searched. The repository of Sussman and
  Alpoge was not searched in this row.

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
- 21:13Z read: FINISH rule sections, GOAL.md, `gap-council-synthesis.md`, `parts/gap.md` L1-160 (formulation, methods 19-36, lead rules, obligations to row 1072; the obligations of rows 1076-1115 were read next, those of rows 1116-1140 only through their FINISH lines; L223-322, the route registry, test table and price, were read at 21:58Z, after the RESULT line was first written; they changed no statement and added item 5 of Section 6), FINISH RESULT lines of rows 1141-1178 and the sibling rows 1180 (neutral bound) and 1181 (free method). Row 1178 (gpt-6.2-astra, continue chain on (W)) runs in parallel. Next: the exact statements of rows 1175 and 1177.
- 21:18Z read `gap-solve16-astra62.md` L1-135 (statements (1)-(13)). Section 1 below written from it.
- 21:33Z read `gap-solve17-astra62.md` in full (planar tension test (7), bounds (14), (25), (26), obstruction (33), (35)). Section 2 written.
- (entries between 21:13Z and 21:52Z are the dated notes inside Sections 1-7.) 21:52Z: Sections 5-7 written and
  corrected once (frozen Z_2 wording, positivity of the plaquette mean, the mixture sentence). Next: re-read of every
  PROVED item, then the RESULT line.
- 21:57Z: re-read done; Corollary FB added; every cited line anchor re-taken with `grep -n -F` (two corrected: the
  finite-aspect statement of row 1161 is L146, Corollary F1 of row 1158 is L212). Section 8 and the RESULT line written.
- 22:00Z: cross-branch search done (main and six pull-request heads; no earlier text of the even-sector consumer);
  "Repo search" section added at the top. Check 1162's verdict table read: (7) is S6, the one-cube statement S8, the
  finite-aspect statement S9, the consumer with the bound 8 eps S10, all HOLD.

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

Remark (the sector form; not used). Statement (5) also allows a full datum with a smaller invariant subspace S_j
("a smaller S_n is the gap on the sector of the class"). That form needs reflection positivity of the limit state
on all local functions. In the second alternative of row 1161 this file does not show it (Theorem L3 (c) of row 700
gets it from (G1), which is the periodic seed). So the proof above restricts the state to A first.

## 6. Theorem BP: the gap clause does not read the branch (21:47Z)

**(N-phys), the neutral premise in the form of row 1161 (`gap-solve9-astra62.md` L146-148).** Fix s_0 = 1/2, the
interval J = [1/2, 1] and a tolerance eps < 1/(8 x 5041). Let K = K(s_0, eps, J) be the integer of row 1161's
finite-aspect statement (L146; an existence statement, independent of the cube, the coupling and the cutoff).
(N-phys) says: at one admissible physical side L, for every cutoff index j >= j_0, with n_j = L/a_j and 4 | n_j,
there is an integer u_j with 3 <= u_j <= n_j/K and s_+(u_j; n_j^3) <= 1/2. Here s_+ is the periodic centre-neutral
excited trace of the cube n_j^3 in units of its vacuum.

**Theorem BP (PROVED GIVEN the inputs of 5.0).** Assume (TM-tw), (S) and (N-phys). Then for every j >= j_0:

(i) S_kappa(n_j/2; n_j^3) <= 8 eps < 1/5041. So (SEED-any-phys) holds with the class kappa, N = n_j/2,
ell_* = L/2 and s_* = 8 eps.

(ii) Proposition P-ev holds at the cutoff j with M_* = (2/L) log(1/(40328 eps)): the centre-even gap of every
periodic cube of integer side at least n_j is at least M_* a_j, every limit state of the periodic symmetric tori
clusters on A at the physical rate M_*, and its transfer operator has the gap M_* on H_A.

(iii) Proposition P'-ev holds: every continuum datum D_inf with a class C of centre-blind observables, (H2) and
(TOT) has a unique vacuum and, with (P4), spec(H) in (0) union [M_*, infinity).

No hypothesis on a twist ratio, on a flux sector or on the branch is used. The conclusion is the same if
alternative I holds at some cutoffs and alternative II at others.

Proof. (i) Row 1161's finite-aspect statement, applied to the cube n_j^3 at the coupling beta_j with u = u_j:
one of the two alternatives (9) approximates all 64 sector weights within eps at every integer v with v/n_j in J,
and the omitted higher-level weights are at most eps. Take v = n_j/2. In alternative I the sectors of limiting
weight one are (m, 0), and in alternative II they are (0, q); in both, the sectors (m, m) with m != 0 have limiting
weight zero and the sector (0, 0) has limiting weight one, carried by one level. So the periodic neutral excited sum
s(v) is at most eps and each of the seven weights X_(m,m)(v), m != 0, is at most eps. By definition
S_kappa(v) = s(v) + sum over m != 0 of X_(m,m)(v) <= 8 eps (this is row 1161 L148 and its equation (7)). The time
is v = n_j/2 and the cube side is n_j = 2v, which is the seed shape S_w(N; (2N)^3) of Theorem S-w with N = v >= 3.
Also N a_j = L/2. (ii) Proposition P-ev with these data: log(1/(5041 x 8 eps)) / (L/2). (iii) Proposition P'-ev. QED

**What Theorem BP says about this row's item (ARGUED from Theorem BP and the lane's definitions).**

1. The gap clause of the Jaffe-Witten target concerns the Hamiltonian on the space generated from the vacuum by
   local gauge-invariant observables. Every gauge-invariant local function is in A, because a centre-valued gauge
   transformation is a gauge transformation. So the lattice input of the gap clause is (N-phys) alone, with the
   continuum datum of the T0 chain ((H2), (TOT)). The branch selection (BS) is not an input.
2. (BS) is an input of (W) as worded in row 720, because z^-(L) counts the flux sectors of the periodic cube. Lemma
   FLUX-W of row 1052 said this in one direction ((W) forces heavy electric flux); row 1161 (7) and Theorem BP say
   that the gap clause survives when the flux clause fails.
3. What (BS) decides is the phase of the centre symmetry on tori. In alternative I the seven electric flux sectors
   of the periodic cube are heavy and every twist ratio tends to 1 (confinement on tori). In alternative II they
   are light and every non-zero twist ratio tends to 0 (row 1161 (9)). In both, the periodic torus state and the
   centre-even state have the same limits on A (Theorem EV-L (d)), and the gap on A is at least M_*.
4. Consequence for the queue (evidence for the lead; the lead decides): a row on (BS) moves (W) and the
   confinement statement, and it does not move the gap clause. The open lattice input of the gap clause is the
   item of row 1180, (N-phys). `parts/gap.md` L200 lists both as open without this distinction.

5. In the route registry of `parts/gap.md` (L223-267, read 21:58Z) this is route RE, the sector engines: "blocked-local,
   reopen on an even step". Rows 737 (Theorem R: the even seed (ES)) and 1161 (the short-time neutral trace) each
   supply an even step, and Theorem BP carries the route to the gap clause. In the words of the test table (L268),
   (N-phys) gives T_ev uniformly in the cutoff, and T_per is what (BS) adds.

Scope. Theorem BP is an implication. (N-phys) is open. The continuum datum, (H2) and (TOT) are open (the T0 chain).
The constant K of (N-phys) is not explicit in the form used here; row 1161 also has an explicit test with K = 512
on two shapes (its check: 4 | n, n >= 2^70), which this file did not re-read line by line. Non-triviality (NT1,
NT2 of GOAL.md) is not addressed. Nothing here is a mass-gap claim.

## 7. The branch selection itself: routes tried, first failing step, obstruction (21:51Z)

(BS) is not proved here and the competing branch is not proved here. For each route this section names the first
failing step and a precise obstruction, with the lane's match where the obstruction is already on file.

### 7.1 Route J: first-moment comparison with fixed multipliers. FAILS, obstruction PROVED here.

Setting. Torus with even sides, twist sign eta_p = -1 on one stack of (1,4)-plaquettes and +1 elsewhere, so each
(1,4)-plane (fixed x_2, x_3) holds exactly one plaquette with eta_p = -1. S_0 and S_tw are the periodic and twisted
Wilson actions, w_p = (1/2) tr U_p. A fixed multiplier field gives each link l two elements a_l, b_l of SU(2) that
do not depend on the configuration; phi(U)_l = a_l U_l b_l. phi preserves the product Haar measure, so
zeta = < exp(-(S_tw o phi - S_0)) >_0 >= exp(-J(phi)), J(phi) := < S_tw o phi - S_0 >_0 (Jensen).

At a site x, give each of the eight half-links h at x the multiplier m_h next to x: m_h = a_l if l leaves x, and
m_h = b_l^(-1) if l arrives at x. For a plaquette p with a corner at x between the half-links h' and h, put
d_(x,p) = m_(h')^(-1) m_h and t_(x,p) = (1/2) tr d_(x,p) (the trace does not change if d is inverted).

**Proposition J (PROVED).**
(a) J(phi) = beta sum over p of < w_p >_0 (1 - eta_p prod over the four corners x of p of t_(x,p)).
(b) For every site x and coordinate plane, the corner elements of the four plaquettes of that plane at x, taken in
cyclic order as d_i = m_(h_i)^(-1) m_(h_(i+1)), satisfy d_1 d_2 d_3 d_4 = 1.
(c) For every (1,4)-plane, the sum over its plaquettes of (1 - eta_p prod_x t_(x,p)) is at least 1 - 2^(-1/2).
(d) So J(phi) >= (1 - 2^(-1/2)) beta < w_14 > N_2 N_3 for every fixed multiplier field, where N_2 N_3 is the
number of (1,4)-planes and < w_14 > >= 0 is the periodic expectation of one (1,4)-plaquette; the identity map
(the thin stack) has J = 2 beta < w_14 > N_2 N_3. No choice of fixed multipliers gives less than an area law.

Proof. (a) In the word of the plaquette p after phi, the two multipliers that meet at a corner x multiply to
d_(x,p) or its inverse, so (phi U)_p is the plaquette word of U with one insertion at each corner. The measure <.>_0
is invariant under gauge transformations, so the expectation does not change if each insertion d is replaced by
k^(-1) d k and k is integrated over SU(2) with Haar measure, independently at the four corners (they are four
different sites). The Haar average of k^(-1) d k is (1/2) tr(d) times the identity. So
< (1/2) tr (phi U)_p >_0 = (prod_x t_(x,p)) < w_p >_0. Insert this in J(phi) = - beta sum_p (eta_p < (1/2) tr
(phi U)_p >_0 - < w_p >_0). (b) The product telescopes. (c) All terms are >= 0 because abs(t) <= 1. Suppose every
plaquette of the plane has eta_p prod_x t_(x,p) > 2^(-1/2). Then every corner has abs(t_(x,p)) > 2^(-1/2), and the
sign of prod_x t_(x,p) is eta_p. The product over the plaquettes of the plane of these signs is -1 (one stack
plaquette). Each corner of the plane occurs once, so some site x has an odd number of negative corners among its
four in the plane. Write d_i = sigma_i r_i with sigma_i the sign of t_i and (1/2) tr r_i = abs(t_i), so that the
angle theta_i = arccos abs(t_i) between r_i and the identity is below pi/4. By (b),
1 = (prod sigma_i) r_1 r_2 r_3 r_4 = - r_1 r_2 r_3 r_4. The angle metric on SU(2) is invariant under left
multiplication, so the angle between 1 and r_1 r_2 r_3 r_4 is at most theta_1 + ... + theta_4 < pi. But the angle
between 1 and -1 is pi. Contradiction. So some plaquette of the plane has eta_p prod t <= 2^(-1/2). (d) < w_p >_0
is the same for all plaquettes of one orientation (translations), and it is >= 0 for every orientation: as a
function of the coupling b of the plaquettes of one orientation alone, say (1,4), log Z is convex, and it is even,
because the change of variables U_(x,4) -> (-1)^(x_1) U_(x,4) (N_1 even) reverses the sign of every (1,4)-plaquette
and of no other; so its derivative at b = beta >= 0, which is the sum of the < w_p >_0 over the (1,4)-plaquettes,
is >= 0. Drop the plaquettes of the other planes (their terms are >= 0 by (a) and abs(t) <= 1) and use (c) in each
(1,4)-plane. QED

Match. In spirit this is the thin-stack and stack-parity bound of row 1175 (12), (14) and the quadratic obstruction
of row 1177 (33). Proposition J is exact for the first moment and covers multipliers on all links, including the
transverse ones; it is weaker in that the multipliers do not read the field. Small.

### 7.2 Route F: multipliers that read the field (colour axes transported by the links). On file.

First failing step: the frame defect. A rotation by an angle alpha about an axis v_x built from the field changes a
mixed plaquette by sin^2(alpha) times the squared covariant difference of v, and on a typical field every axis
field has squared covariant difference at least c/(1 + 6 beta) per site (row 1141 (2)-(6)). Obstruction on file:
row 1177 (33)-(35), every quadratic comparison that fixes the transverse links costs at least c w^2 with
probability tending to one, on the same tori where the true twist free energy tends to zero. Best bounds on file:
row 1177 (26), sigma_beta(w) >= c beta^(-1/2) exp(-C beta^(1/2) log(2 + beta) w^2); row 1171 (33),
- log zeta <= C n^2 L_beta^3 J_beta^2. All are area laws. Not attacked again.

### 7.3 Route C: constancy of the branch along a path of couplings. On file.

Match: row 1161 (`gap-solve9-astra62.md` L335-339: the sets N, P, M; P and M are open and disjoint, N lies in their
union, so "there is a single fixed bare coupling with neither seed" below any coupling of M); Corollary R6 of row 737;
(M5) of the same row; Lemma CONT of row 1072; (NOCRIT) of row 709. First failing step: closedness, the neutral
premise at every coupling of the path. Obstruction on file: the two-dimensional Ising model has G open and not
closed ((M5)). Added here (ARGUED, Section 3): the two natural paths from a corner with free twists both cross a
first-order line.

### 7.4 Route R: bounds that read only scales below the seed size. FAILS by arithmetic, GIVEN row 1177 (3).

Statement. Let a method give, at each fine cutoff, - log zeta_beta(N) <= A (N/l)^2 for all large N, with A and the
length l fixed in lattice units (this is the form of 7.1, 7.2, and of a twist inserted in an effective action at a
block scale l). In the competing branch row 1175 (4) reads - log zeta_beta(N) >= c_q (N/n_0)^2 / log(2 + N/n_0) -
log 64. The two are compatible for all large N whenever A/l^2 is at least the competing constant, and nothing known bounds that
constant below. So a bound of the form A (N/l)^2 does not by itself contradict the competing branch. (Frozen Z_2 at
large coupling shows an area-law twist cost inside the lane's class: its periodic seed fails by the lane's Peierls
theorem, `gap-crux-exercise2-max.md` test table; the lane expects, and has not proved, the full seed there.) The
same holds in the planar form: row 1177 (3) allows sigma_beta(w) as large as
C n_0^(-2) x^(-4) exp(- c x^2/log(2 + x)), x = w/n_0, in the competing branch. (BS) needs a bound below every area law
by more than a logarithm, and such a bound must read the measure at scales of the seed size and above.

### 7.5 The forbidden band: a finite form of the selection at the cube of the premise (PROVED GIVEN row 1161's finite-aspect statement; rewritten 21:55Z)

Notation. On the periodic cube n^3: lambda_0 is the vacuum eigenvalue; for an electric character q != 0,
lambda_q is the top eigenvalue of the periodic transfer operator on the sector (0, q), and E_q := log(lambda_0/lambda_q);
for a static magnetic twist m != 0, lambda_m is the top eigenvalue of the transfer operator of the twisted cube,
and D_m := log(lambda_0/lambda_m) >= 0. Its eigenvector is even, so it lies in the sector (m, 0) ((S3) of
`gap-flux-exercise.md` 3.1). Put b_- := - log(1 - 2 eps) and b_+ := 2 log(1/eps). For eps just below 1/40328,
b_- is about 5.0 x 10^(-5) and b_+ is about 21.2.

**Corollary FB (PROVED GIVEN row 1161 L146, with the constants of Section 6).** Under (N-phys), at every cutoff
j >= j_0 and with n = n_j, exactly one of the following holds.

- Alternative I: n E_q >= b_+ for all seven q != 0, and n D_m <= b_- for all seven m != 0.
- Alternative II: n D_m >= b_+ for all seven m != 0, and n E_q <= b_- for all seven q != 0.

So each of the fourteen numbers n E_q, n D_m lies outside the open band (b_-, b_+). **One number in the band on the
right side selects the branch: if n D_m < b_+ for one m != 0, or n E_q > b_- for one q != 0, then alternative I
holds at that cutoff.** In physical units: the energy of one unit of magnetic flux on the cube of side L is below
21.2/L, or the energy of one unit of electric flux is above 5.0 x 10^(-5)/L.

Proof. By the finite-aspect statement one of the alternatives (9) of row 1161 approximates all 64 sector weights
within eps at every integer v with v/n in [1/2, 1], and in each sector of limiting weight one the levels after
the first carry at most eps. A sector of limiting weight zero has weight at most eps at v = n/2, and its top
level is at most its weight; so (top eigenvalue/lambda_0)^(n/2) <= eps and n log(lambda_0/top) >= 2 log(1/eps).
A sector of limiting weight one has weight at least 1 - eps at v = n, of which the first level carries at least
1 - 2 eps; so n log(lambda_0/top) <= - log(1 - 2 eps). In alternative I the weight-one sectors are the (m, 0) and
the sectors (0, q), q != 0, have limiting weight zero. In alternative II the roles are exchanged. The two lists
exclude each other because b_- < b_+. QED

Reading (ARGUED). (BS) is an order-one statement at one physical cube: a bound of one flux energy by a fixed
multiple of 1/L, with a margin of five orders of magnitude between the two alternatives. Lower bounds on electric
flux energies of this kind are on file as targets: row 1158 Lemma F with (TUN), and row 1161 (1)-(2) (linear in
the overlap). (N-phys) gives exp(- m_+ u) <= s_+(u) <= 1/2 with u <= n/K, so n m_+ >= K log 2. Corollary F1 of row 1158
(`gap-paths-fable.md` L212-215: z^- >= (tau_*^2/13) z_+, for m_+ <= 1) would then put n E_q above b_- as soon as
tau_*^2 > 13 b_-/(K log 2): an overlap above about 1.4 x 10^(-3) for K = 512, and above 0.031 for every K >= 1
(arithmetic from the stated constants; the lemma was not re-derived here). The upper bound n D_m < 21.2 is of the kind of row 1161 L107 (a transverse
class probability above 1/10). Neither is proved for Wilson SU(2). OPEN.

### 7.6 Why no soft argument selects the branch (ARGUED)

(a) At one cutoff, the periodic state and the centre-even state have the same limits on A (Theorem EV-L (d)), and
both alternatives have the same clustering rate on A (Theorem BP). So the gap, and every bound on correlations of
centre-blind observables of bounded size that holds in both, does not select. This file does not claim that the two
alternatives agree on all of A: the decay law of large fundamental Wilson loops is a centre-blind quantity that is
expected to differ (area law against perimeter law); that equivalence is not shown here. (b) Inside the lane's class the periodic seed can fail
(frozen Z_2 at large coupling, lane Peierls theorem; the lane expects the second alternative there), so reflection
positivity, the transfer structure and the crossing symmetry of the sector weights do not select; this is the
scope of Theorem R of row 737 and of row 1161 (9).
(c) A selection must therefore read the group and the scales at and above the seed size, through a quantity that
is not centre-blind: a twist ratio, a flux energy, or a winding observable. Row 1177 ends at the same sentence.

## 8. Re-read of the PROVED items, and what is left (21:56Z)

Re-read done on Lemma A-cl, Theorem L3-ev, Propositions P-ev and P'-ev, Theorem BP, Proposition J and Corollary FB.
Corrections made during the re-read (all in place above):

- 5.3: the remark on the sector form claimed more than is shown in the second alternative; it now says so.
- 6, item 3: a sentence said that eight flux sectors agree on A; only "periodic state and centre-even state have
  the same limits on A" is proved (Theorem EV-L (d)).
- 7.1 (d): positivity of the plaquette mean is now derived for one orientation; "thin stack" is the identity map.
- 7.4 and 7.6: frozen Z_2 at large coupling has a lane theorem only for the failure of the periodic seed; the
  second alternative there is expected, not proved in the lane. 7.6 (a) no longer claims that the two alternatives
  agree on all centre-blind observables (large Wilson loops are expected to differ).
- 7.5: rewritten as Corollary FB; the neutral gap bound is n m_+ >= K log 2, not a fixed 512 log 2.

Statements of this file and their labels:

| Statement | Label | Kind (FINISH rule 9) |
|---|---|---|
| Lemma A-cl | PROVED | proof of a step the lane left unwritten |
| Theorem L3-ev, Propositions P-ev, P'-ev | PROVED GIVEN the lane statements of 5.0 | same (rows 731, 837, 1024: "not rewritten") |
| Theorem BP | PROVED GIVEN 5.0 (composition; row 1161 (7) states its first half) | same |
| Reading 1-4 under Theorem BP | ARGUED | evidence for the lead |
| Proposition J | PROVED | obstruction for one route; small |
| Corollary FB | PROVED GIVEN row 1161 L146 | finite restatement of (BS) |
| 7.2, 7.3 | on file (rows 1177, 1171, 1141; rows 1161, 737, 1072, 709) | named matches, not attacked |
| 7.4, 7.6, the two paths of Section 3 | ARGUED | obstruction readings |
| (BS), the competing branch, (N-phys), (W) | OPEN | - |

Not done, and why. No numeric run (none was needed; no lock taken). The cross-branch search was run only at the
end (see "Repo search" at the top); it found no earlier text of the consumer. Row 1161's explicit two-shape test with K = 512
and row 1175's (1)-(9) were used as stated and not re-derived. Row 1176 (check of row 1175) had no RESULT at this
pin. The complete account of Sussman and Alpoge was not opened in this row: nothing here reads a statement of
theirs beyond what the cited lane files already cite.

Credits. Balaban (the renormalization group behind the ultraviolet premise of the trajectory). Sussman and Alpoge,
with Claude and Codex as authors of their text (the account that supplies the trajectory and the continuum datum of
Proposition P'). Chatterjee (the weak-coupling free-energy method credited in row 1143, an input of the chain this
row builds on). 't Hooft (twisted boundary conditions and the flux sectors). Mack and Petkova (the stack-parity
comparison). In the lane: rows 697, 700, 731, 737 (Theorem S, the limit consumer, Theorem EV-L and Corollary EV,
Theorem R and Corollary R6), row 1052 (Lemma FLUX-W), row 1158 (Lemma F), rows 1161, 1175, 1177 (gpt-6.2-astra:
the one-cube alternative with its flux-independent seed (7), the twist-cost form, the planar tension test and the
quadratic obstruction).

What stays open, in order of what it blocks:

1. (N-phys), the one-cube physical neutral bound (row 1180's item). By Theorem BP it is the only open lattice input
   of the gap clause, given the continuum datum.
2. The continuum datum with (H2) and (TOT) (the T0 chain).
3. (BS), in any of its forms (row 1175 (6), row 1177 (7), Corollary FB). It blocks (W) as worded and the
   confinement statement on tori. It does not block the gap clause.

Suggested edits for the lead (the lead decides; this file edits nothing else):

- `parts/gap.md` L200 and the Formulation section: record that the gap clause needs (N-phys) and not the
  flux-branch choice (row 1161 (7); Theorem BP here), and that the even-sector consumer is now written (Section 5),
  pending a check by a model that did not write it.
- A check row for Section 5 and Theorem BP: line by line against `gap-seed-limit.md` 4.3, 5,
  `gap-flux-exercise.md` 8.2, 8.4, `gap-os-equiv.md` (3), (5), and `gap-solve9-astra62.md` L113-148.
- If the target is the Jaffe-Witten gap clause, no further row on (BS) is needed for it.

RESULT: Row 1179 (Claude Fable 5.2 max, Mac mini worker; author, checked by no one; no numeric run; no mass gap
claimed). The branch selection (BS) is NOT proved and the competing branch is NOT proved; both stay OPEN. PROVED
GIVEN the lane's checked statements (rows 668, 697, 700, 731, 1004, 1161): the even-sector consumer that rows 731, 837 and 1024
left unwritten (Theorem L3-ev, Propositions P-ev, P'-ev), and Theorem BP: the one-cube physical neutral bound alone
gives a cutoff-uniform gap M_* = (2/L) log(1/(40328 eps)) on the centre-blind sector and, with the continuum datum,
the Jaffe-Witten gap clause, in BOTH flux alternatives; so (BS) is on the path of (W) as worded (confinement on
tori) and not on the path of the gap clause. PROVED GIVEN row 1161: Corollary FB, (BS) at the cube of the premise
is the statement that one flux energy lies on the right side of a forbidden band (magnetic below 21.2/L, or electric
above 5.0 x 10^(-5)/L). PROVED: Proposition J, no first-moment comparison with fixed multipliers beats the area law
(at least (1 - 2^(-1/2)) beta <w> per plane). Named matches, not attacked: field-built frames (row 1177 (33)),
constancy of the branch along a coupling path (row 1161 L335-339, Corollary R6 of row 737). OPEN: (N-phys), the
continuum datum, (BS), (W).
