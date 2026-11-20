lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:16Z

# gap-mini-solve-ah-opus (FINISH row 1259): plain brief "prove the SU(2) mass gap", run by Opus 5.5 max

Branch claude/ym4d-hard-route, pinned commit c23b8c360. Writer: Claude Opus 5.5 (max), Mac mini worker. Not committed
by the writer; a relay copies the file. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Status log

- 2026-11-20T11:16Z (date -u) file created; reading the row, `parts/gap.md`, row 1218's reading `library/prior/gap-onebound-read-sol.md`
  and the newest chain rows next.
- 2026-11-20T11:51Z (date -u) Step 1 written (reading, screen, choice).
- 2026-11-20T11:59Z (date -u) Step 2 written: the (S2) port was dropped (check row 989 L156: the flat-package route is "possible
  but not needed"); worked instead on the count half (NS-gap), Lemma CD and its corollaries.
- 2026-11-20T12:00Z (date -u) Step 2 self-check: two claims corrected in place (only sigma_3 is monotone in t; the density
  bounds are 12 beta t^(3-k)). Step 3 (status, RESULT) written; row finished.

## Step 1. How best to attack it (judgement; ARGUED where not cited)

**Read for this choice.** GOAL.md; FINISH.md L1-90 and L299-350 (rules); queue row 1259 in full; the RESULT parts of rows
1216-1258; `parts/gap.md` L1-104 (state, methods 19-36, lead rules); `library/prior/gap-onebound-read-sol.md` L25-125,
L255-272 (row 1218); `library/gap-mini-solve-ag-opus.md` L11-60, L228-300, L342-381 (row 1258, (SL), (RR)); the plan of
the running sibling row 1256 (`gap-mini-solve-af-opus.md` L11-66: it works on (EDGE)); `library/gap-seed-limit.md`
L196-245 (row 700: Propositions N1, N2, Corollary N3, (NS-gap)); `library/gap-phys-seed.md` L253-330 (row 720: Lemma Z,
Z', Z3, Theorem ZD, Corollaries Z1-Z4, Theorem ZD-c); `library/gap-crux-restate.md` L50-90 (C1-C5);
`library/gap-mini-solve-q-fable.md` L125-200, L252-272 (row 1224: A's hypothesis (M) and A's checked Section 11);
`library/gap-univk-opus.md` L341-398 (row 924: (DENS-K), B1-B3); the open-input lists of rows 1241 (L148-166) and 1255.
Branch tip at 8af5d34eb (scratch bare fetch, read-only): sibling files af and ag only; ai, aj not started.

**What the record fixes (cited, not re-derived; pointers, not evidence).**
- Beside the account's premises, the Jaffe-Witten gap on the account's tr F^2 sector reads one lattice estimate, (N-phys)
  (row 1161 L146-148; row 1179; row 1225 Theorem E-N, check 1232 HOLDS AFTER CORRECTION).
- At one coupling the seed is EXACTLY a gap inequality with a count term: Theorem ZD (C) of row 720
  (`gap-phys-seed.md` L296-310): there is b with b m(b^3) >= 256 D(b/4) + 29.64, D the Casimir free energy of the
  symmetric torus. Corollary Z2 (L312-317): a uniform gap plus liminf D(a)/a < m_0/64 gives the seed. So "seed =
  lattice gap" (rows 1225, 1233, 1238; FAILED as a deduction in check 1242) is true exactly modulo the count, and the
  count is (NS-gap) of row 700 (L234), open since rows 697/720 and never attacked.
- Every one-scale form on file asks for the same thing at the band (an order-one effective coupling): C1 seed, C3 (W),
  (SL)/(RR) (row 1258), A's (M) (row 1224, A's Definition 11.3), B's cube Poincare (row 1254 (1)). Hopf/Birkhoff
  contraction of the slab kernel is on file with its extensive diameter (`gap-crux-skeleton-max.md` L202, L373;
  `gap-fr-opus.md` L99; `gap-short-step-max.md` L482).

**My own screen this run (each grepped in `library/`, `library/prior/`, `parts/gap.md` before any work; counts are
files naming the tool).** Every idea is on file or dies at a stated step.

| Idea | Registry | Where it stops |
|---|---|---|
| Count from the gap: bound D(a) by the thermal sum at a shorter time (Proposition Delta, RP doubling f(2T) <= f(T)) | Prop. Delta row 708, Lemma Z row 720 | it IS Lemma Z / Corollary Z2; the sublinear bound on D is the open (NS-gap) |
| Count by recursion into prisms and slabs (D = sum of thermal densities with 1-4 short sides) | new as a form; ARGUED here | each density is a count per unit volume; a gap on prisms adds only an additive -t m, not a factor |
| Counterexample to (NS-gap) in the class (uniform gap, linear D) | row 720 L319 "I do not know a model" | subsystem and fracton models give linear D but their gap closes (degenerate sectors); none found |
| Birkhoff self-improvement of (RR): tanh(eta_*/4) submultiplicative, constant threshold | Birkhoff 19 files, Hopf L202 | a corollary of Hopf's theorem; the diameter stays extensive (`gap-mini-free-fable.md` L379) |
| Dobrushin contraction through slices: tau(s1+s2) <= tau(s1) tau(s2) | standard | true, but a whole-slice TV is near 1 until s ~ xi log abs(B): the same log |
| A's (M) at one coupling gives the seed | A Prop. 7.19 (product of rings) | false in general; maximal correlation misses the count (A's own example) |
| Seed gives B's/A's cube Poincare (static to dynamic) | row 1218 item 2 | needs worst-case mixing; B leaves the converse open |
| Higgs complementarity path kappa: infinity -> 0 at fixed beta | Fradkin 26, Osterwalder-Seiler 41 | the crossover W mass ~ Lambda is the band in the kappa direction |
| Lieb-Mattis ordering of sector ground levels | 0 files | no sign rule: the SU(2) character expansion has negative terms (crosscap, rows 737, 744) |
| Weinberg-Witten | 0 files | forbids only massless helicity > 1 with a covariant stress tensor; spin 0, 1 glueballs allowed |

Verdict (ARGUED): no engine for the band off the record, as in rows 1219-1258.

**Choice for this row.** Rule 0: the item must move a named open input. The infrared crux has no engine, and the
rules (FINISH L301) give Opus the ports and routine steps. Three inputs of the one-cutoff carry (row 1233 Proposition
3.7, as corrected by check 1242 and rows 1241, 1255) are unattacked and look like ports, not new mathematics: (DET)'s
structural inputs (S1)-(S3) (`gap-det-fable.md` L71-77, L290-316), the existence of the inverses at U = 1 ("pr-lay W",
`pr-lay.md` W, used at U = 1 by `gap-det-fable.md` L403), and 8.22's standing hypotheses. The running sibling row 1256
works on (EDGE); check row 1263 reads row 1255's (R). Next step: decide which of these the repository's CHECKED hard-core
work already supplies (FINISH L14: the flat package from Balaban CMP 89, 95, 96 was checked line by line, row 95), and
port it. If none is a port, I return to the count (NS-gap) and record its exact first failing step.

## Step 2. The count half of the one-coupling crux: an exact decomposition of D (Lemma CD)

**Why this and not the port (decision recorded).** (S2) of (DET) is already ported conditionally on pr-lay R and W,
and both checks of row 987 accept that (`gap-det-check-opus.md` L133, L156: the route through the flat package of row
95 is "possible but not needed"; `gap-det-check-astra.md` L314, L395). A port through row 95 would change no verdict.
I return to the count: at one coupling the seed is the gap plus a bound on the Casimir free energy D (Theorem ZD (C),
Corollary Z2 of row 720), and the count half (NS-gap) of row 700 has never been attacked. Question: is the count an
easier half, provable by tools that do not see the band?

**Setting.** SU(2) Wilson action S(U) = (beta/2) sum_p tr U_p, weight e^S, Haar measure on links; Z(t_1, t_2, t_3, t_4)
the periodic torus with these sides (each >= 1), F = log Z. Z is symmetric in its four sides (the action is invariant
under permutations of the lattice directions). For a spatial torus X = (x_2, x_3, x_4), Z(t, X) = Tr R_X^t with R_X the
positive trace-class transfer operator on the gauge-invariant space of X (rows 697-699: (TM), Lemma A), eigenvalues
lambda_0(X) >= lambda_1(X) >= ... >= 0, and g(t; X) := F(t, X) - t log lambda_0(X) = log sum_j (lambda_j/lambda_0)^t
>= 0 is the lane's thermal sum (row 700 notation). D(t) := F(t^4) - f_infinity t^4 (row 720, Proposition Delta;
equivalently D(t) = sum_(k>=0) 16^(-(k+1)) Phi(2^k t), row 697 Proposition R).

**Lemma CD (PROVED; Claude Opus 5.5, checked by no one).**
(a) Almost additivity. For every spatial torus X and t, t' >= 1:
    abs( F(t + t', X) - F(t, X) - F(t', X) ) <= 12 beta abs(X).
(b) Limits. Lambda_1(X) := lim_t F(t, X)/t exists, equals log lambda_0(X), and abs(F(t, X) - t Lambda_1(X)) <= 12 beta abs(X),
so 0 <= g(t; X) <= 12 beta abs(X) for every t. Likewise Lambda_2(x_3, x_4) := lim_T Lambda_1(T, x_3, x_4)/T,
Lambda_3(x_4) := lim_T Lambda_2(T, x_4)/T and f_infinity := lim_T Lambda_3(T)/T exist, with
abs(Lambda_1(T, x_3, x_4) - T Lambda_2(x_3, x_4)) <= 12 beta x_3 x_4, abs(Lambda_2(T, x_4) - T Lambda_3(x_4)) <= 12 beta x_4,
abs(Lambda_3(T) - T f_infinity) <= 12 beta, and f_infinity = lim F(T)/abs(T) as all sides grow.
(c) The identity. For every t >= 1,
    D(t) = g(t; (t,t,t)) + t sigma_1(t) + t^2 sigma_2(t) + t^3 sigma_3(t),                                    (CD)
    sigma_1(t) := Lambda_1(t,t,t) - t Lambda_2(t,t),  sigma_2(t) := Lambda_2(t,t) - t Lambda_3(t),  sigma_3(t) := Lambda_3(t) - t f_infinity,
and every term is >= 0.
(d) Meaning of the terms. sigma_1(t) = lim_T g(t; (T, t, t))/T, sigma_2(t) = lim g(t; (T, T', t))/(T T'),
sigma_3(t) = lim g(t; (T, T', T''))/(T T' T''): the thermal sums at the SAME time extent t per unit volume of a prism
(one long side), of a slab (two long sides) and of space (three long sides). sigma_3 is row 978's thermal pressure over
temperature pi(t) (`gap-ladder-max.md` L188). sigma_3 is non-increasing in t (sigma_1, sigma_2 change their cross-section
with t, so no monotonicity is claimed for them), and sigma_k(t) <= 12 beta t^(3-k).

Proof. (a) Label the time slices 0, ..., t + t' - 1 of the torus (t + t') x X. Rewire the 3 abs(X) time-like plaquettes
between slices t - 1 and t so that they close on slice 0, and those between slices t + t' - 1 and 0 so that they close
on slice t. The rewired weight is the product of the weights of the tori t x X and t' x X on the same link variables,
so its integral is Z(t, X) Z(t', X). Only 6 abs(X) plaquette terms changed, each by at most 2 beta in absolute value
(abs((beta/2) tr U) <= beta); the Haar measure is the same. So the two integrals differ by a factor in
[e^(-12 beta abs(X)), e^(12 beta abs(X))]. (b) By (a), F(t, X) + 12 beta abs(X) is subadditive and F(t, X) - 12 beta abs(X)
is superadditive in t; Fekete's lemma gives the limit and the two-sided bound. Since F(t, X) = t log lambda_0(X) + g(t; X)
and g(t; X) decreases to log(multiplicity of lambda_0) in t, the limit is log lambda_0(X) and g >= 0. For Lambda_2: cut
the torus (t, T + T', x_3, x_4) in direction 2; the cut hyperplanes have t x_3 x_4 sites, so (a) in that direction gives
abs(F(t, T + T', x_3, x_4) - F(t, T, x_3, x_4) - F(t, T', x_3, x_4)) <= 12 beta t x_3 x_4; divide by t and let t -> infinity:
Lambda_1(., x_3, x_4) is almost additive with error 12 beta x_3 x_4, and Fekete again. Lambda_3 and f_infinity the same way.
That f_infinity is the limit of F/abs(T) follows from the four two-sided bounds. (c) The identity is the telescoping sum
F(t^4) = [F(t^4) - t Lambda_1(t^3)] + t [Lambda_1(t^3) - t Lambda_2(t^2)] + t^2 [Lambda_2(t^2) - t Lambda_3(t)] + t^3 [Lambda_3(t) - t f_infinity] + t^4 f_infinity,
whose first bracket is g(t; (t,t,t)) by (b). Positivity: reflection positivity gives Z(2s, Y) = sum lambda^(2s) <=
(sum lambda^s)^2 = Z(s, Y)^2 in every direction, so F/abs(T) does not increase when one side is doubled. Hence
Lambda_1(2^k t, t, t)/(2^k t) <= Lambda_1(t, t, t)/t (take the first side to infinity first), and k -> infinity gives
sigma_1 >= 0; sigma_2, sigma_3 >= 0 the same way. (d) By the symmetry of Z, g(t; (T, t, t)) = F(t, T, t, t) -
t Lambda_1(T, t, t) = F(T, t, t, t) - t Lambda_1(T, t, t); divide by T and use (b). The same for sigma_2, sigma_3. g(t; Y)
is non-increasing in t for every fixed Y; sigma_3 has no other dependence on t, so it is non-increasing. g <= 12 beta abs(Y)
with abs(Y) = T t^2, T T' t, T T' T'' gives sigma_1 <= 12 beta t^2, sigma_2 <= 12 beta t, sigma_3 <= 12 beta. QED

**Corollary CD1 (the one-coupling seed in thermal form; PROVED GIVEN Corollary Z2 of row 720,
`gap-phys-seed.md` L312-317).** At one coupling, let the periodic cubes have a uniform gap m(b^3) >= m_0 > 0 for
b >= b_0. If
    (TR)   liminf over a of  [ g(a; a^3)/a + sigma_1(a) + a sigma_2(a) + a^2 sigma_3(a) ]  <  m_0/64,
the model has a seed. Proof: by (CD) the bracket is D(a)/a; apply Corollary Z2. QED
So the count half (NS-gap) of row 700 is exactly a low-temperature thermal statement: the thermal sum of the cube grows
sublinearly, and the thermal free-energy densities of prism, slab and space at time extent a are o(1), o(1/a), o(1/a^2).

**Corollary CD2 (what a seed forces; PROVED GIVEN Lemma Z3 of row 720, L278-294).** If S(N; (2N)^3) = s < 1/5041,
q = 5041 s, then for L = 2^(k+1) N: g(L; L^3) + L sigma_1(L) + L^2 sigma_2(L) + L^3 sigma_3(L) = D(L) <= 128 q^(2^k)/5041.
In particular the thermal pressure density obeys sigma_3(L) <= 128 q^(2^k)/(5041 L^3): a seed forces the thermal
free energy of space at temperature 1/L to vanish doubly exponentially along the dyadic sizes. Proof: (CD), each term
>= 0, and Lemma Z3 at L = D_k. QED

**What the decomposition says about the count (ARGUED from the PROVED items; GUIDE values RECALLED).**
1. Lemma CD (b) is the lane's trace bound in four places: g(t; X) <= 12 beta abs(X) is row 700's
   Tr R/lambda_0 <= e^(12 beta L^3) (`gap-seed-limit.md` L236, as corrected by row 703), and sigma_k(t) <= 12 beta t^(3-k) is
   its density form (together D(t) <= 48 beta t^3, surface order). Reflection positivity adds only the signs and the
   monotonicity of sigma_3 in t. So the tools that do not see the band (RP, locality, compactness, the gap of single cubes)
   give these bounds and nothing that decays in t.
2. A gap on cubes does not bound the densities. In (CD) the gap enters only through g(t; (t,t,t)) (Lemma Z of row 720).
   For the extensive terms, the gap of a prism or slab gives g(t; Y) <= g(s; Y) - (t - s) m(Y) when g(s; Y) is large,
   an additive gain that vanishes per unit volume. A product of K copies of one gapped model has the same gap and K times
   every sigma_k; its seed size grows like (log K)/m_0. This is the count point that Bhattacharjee et al. make with a
   product of rings (their Proposition 7.19, as read by row 1218 L118-123) and that row 1234's Proposition LS makes for the
   ultraviolet count (check 1250); I do not claim it as new.
3. (TR) is blind, unlike the gap: a free massless field has sigma_3(t) of order t^(-3) (the Stefan-Boltzmann law,
   RECALLED), sigma_2 of order t^(-2), sigma_1 of order t^(-1), and D(t) of order log t from its zero modes, so (TR) holds
   for the free photon and for compact U(1) at weak coupling. It fails where the number of light states grows
   exponentially in the side, for example in models with planar subsystem symmetries in their broken phase (the
   four-dimensional plaquette Ising model at low temperature: D(t) of order t log 2, RECALLED physics, not proved here),
   which also have no gap. So (TR) is a "no exponential multiplicity of light states" condition. It is not a property of
   reflection-positive local models as such, and no blind tool in the lane gives decay of sigma_3 below 12 beta.
4. Verdict on the count half (ARGUED). (TR) at a coupling in the band reads the density of low-lying states per unit
   volume at an order-one coupling; it is as band-hard as the gap. So the count is NOT an easier half: Theorem ZD (C) at
   one coupling needs two band-level inputs, the cube gap and (TR), and (TR) cannot be supplied by class-wide tools. This
   answers the open question of row 700 (L232-234) and row 720 (L318-319) only in this negative, structural sense; the
   implication "uniform gap implies a seed" itself stays OPEN, with no counterexample in the class (a counterexample needs
   a gapped model with exponentially many light states, and the subsystem-symmetric candidates lose their gap).

**Repo search for Lemma CD.** Greps of `library/gap-*.md`, `library/prior/gap-*.md` and `parts/gap.md` for "prism",
"per unit length", "thermal densit", "Lambda_3": no decomposition of D into compactified thermal densities on file. Row
720 Lemma Z3 Step 1 (L278-284) has the finite doubling version Phi(n) = 8 d_1 + 4 d_2 + 2 d_3 + d_4, and row 978 (b)
(`gap-ladder-max.md` L188) the thermal pressure pi(t) = sigma_3(t). Lemma CD is the limit form of the first and
contains the second as its top term. The almost-additivity and Fekete steps are classical (Ruelle; Fisher), recalled.

## Step 3. Status, credits, check request

**3.1 Physical-units reading (ARGUED; the cutoff limits of the four terms are not proved).** Along a trajectory, (CD)
at t = L/a_j splits the lane's (BDD-Delta) (row 720 Theorem ZD-c) into four bounds at temperature 1/L: the thermal sum of
the physical cube, and the thermal free energies of prism, slab and space in units of L^(-4) per physical volume. So
(BDD-Delta) is a low-temperature Stefan-Boltzmann bound in all compactified geometries; it holds for a free massless
field up to zero-mode logarithms, and for a gapped theory every term tends to 0. The selective content of the crux sits
in (Z-UNB), as row 720 already says ("What Attempt 1 gives", L330-337); (CD) adds that the count half has no
selective content but needs the density of light states at the band.

**3.2 Statements of this file.**

| Statement | Label | Depends on |
|---|---|---|
| Step 1 screen (ten ideas, each on file or stopped at a stated step) | ARGUED, with file anchors | registry greps of this run |
| Lemma CD (a) almost additivity, 12 beta abs(X) | PROVED | bounded plaquette terms only |
| Lemma CD (b) limits Lambda_1-3, f_infinity, two-sided bounds; 0 <= g(t; X) <= 12 beta abs(X) | PROVED | (a), Fekete; (TM) of rows 697-699 for Lambda_1 = log lambda_0 |
| Lemma CD (c) identity (CD), all four terms >= 0 | PROVED | (b); reflection positivity (doubling a side does not raise F/abs(T)) |
| Lemma CD (d) sigma_k = thermal sums per unit volume of prism, slab, space; sigma_3 non-increasing; sigma_k <= 12 beta t^(3-k) | PROVED | (b), (c), symmetry of Z under permutations of directions |
| Corollary CD1: uniform cube gap m_0 plus (TR) gives the seed | PROVED GIVEN | Corollary Z2, row 720 (checked in row 727 as a duplicate in substance of row 700 Corollary N3) |
| Corollary CD2: a seed forces D(L) <= 128 q^(2^k)/5041, hence sigma_3(L) <= 128 q^(2^k)/(5041 L^3) | PROVED GIVEN | Lemma Z3, row 720 |
| Products: for the group SU(2)^K (product Wilson action) the cube gap is that of SU(2) and g, sigma_k, D are K times SU(2)'s, so no bound of (TR) by (m_0, beta, t) holds uniformly over compact groups | PROVED (F is additive over independent factors; the transfer operator is a tensor product) | none; same point as Bhattacharjee et al. Proposition 7.19 (rings) and row 1234 Proposition LS |
| (TR) is blind (true for the free photon and weak-coupling U(1)); fails in subsystem-symmetric models, which also lose the gap | ARGUED; the two model facts RECALLED | Stefan-Boltzmann law; plaquette Ising model |
| The count half of Theorem ZD (C) is as band-hard as the gap; "uniform gap implies a seed" stays OPEN with no counterexample | ARGUED | points 1-4 of Step 2 |
| (S2) of (DET) through the flat package of row 95 | not done: would change no verdict (checks 988, 989) | `gap-det-check-opus.md` L156 |

**3.3 What stays OPEN.** (N-phys); at one coupling in the band, the cube gap (Z-UNB) and the count (TR) (equivalently
(BDD-Delta), (NS-gap)); the one-cutoff carry's inputs (the account's outstanding 9.1:prop-blind-site-expansions, (EDGE)
on which row 1256 is working, 8.22's standing hypotheses, (DET)'s (S1)-(S3) and pr-lay W as ported conditionally, the
reading (R) or (V9) under check in row 1263); the account's premises (T0 chain). No engine for the band is offered.

**3.4 Credits.** The seed, Theorem S, Proposition Delta, Lemma Z, Lemma Z3, Theorem ZD and Corollary Z2 are the lane's
(rows 697, 700, 708, 720 and their checks). Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and Singha Roy
("The Yang-Mills Mass Gap from One Bound at One Scale", Preprints.org 202611.1282, read through row 1218) for the
product-of-rings point on counts. Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) for the
complete account whose carry inputs are listed in 3.3; Tadeusz Balaban for the renormalisation group behind them. The
almost-additivity and Fekete steps are classical (Ruelle, Fisher), recalled, not read here.

**3.5 Check request.** One line-by-line check of Lemma CD (a)-(d) and Corollaries CD1-CD2 by the other provider; the
ARGUED verdict of Step 2 point 4 needs no check unless a row relies on it.

**3.6 Process note.** I spent most of the run reading and screening (11:16Z-11:53Z by `date -u`) before the first
proof; every infrared candidate I named was on file. No numeric run was made (no statement here rests on one), and no
subagent was used.

RESULT: Row 1259 (Claude Opus 5.5 max, Mac mini worker 1, 11:16Z-12:05Z by date -u; author only, checked by no one; no numeric run, no subagent): the Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; no engine for the band is offered (Step 1: ten ideas screened, each on file or stopped at a stated step). Worked item: the count half of the one-coupling crux, (NS-gap) of row 700. PROVED (Lemma CD): for SU(2) Wilson at every coupling the Casimir free energy of the symmetric torus splits exactly as D(t) = g(t; t^3) + t sigma_1(t) + t^2 sigma_2(t) + t^3 sigma_3(t), the thermal sum of the cube plus the thermal free-energy densities of prism, slab and space at the same time extent t, each term non-negative by reflection positivity and at most the trace bound 12 beta t^3; PROVED GIVEN Corollary Z2 and Lemma Z3 of row 720: a uniform cube gap m_0 plus the low-temperature thermal bound (TR) (liminf of D(a)/a below m_0/64, i.e. the four terms) gives the seed, and a seed forces sigma_3(L) <= 128 q^(2^k)/(5041 L^3); PROVED: products SU(2)^K keep the gap and multiply every term by K. ARGUED: (TR) is blind (true for the free photon and weak-coupling U(1)) but reads the density of light states at the band, so the count is not an easier half; "uniform gap implies a seed" stays OPEN with no counterexample. OPEN: (N-phys), the cube gap and (TR) at one coupling in the band, the one-cutoff carry's inputs, the account's premises. Output library/gap-mini-solve-ah-opus.md.
