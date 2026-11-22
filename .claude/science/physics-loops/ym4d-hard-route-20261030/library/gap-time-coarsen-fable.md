lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T03:43Z

# gap-time-coarsen-fable (queue row 1396): the neutral Wilson quotient under geometric time coarsening

Status: DONE 2026-11-22T15:55Z (date -u). Author only, checked by no one. Reading order: Section 4 (verdict), 3.3 (Proposition USE), 2 (lemmas), 5 (rows).
No commit, claim or push from this machine; a relay copies this file.

## 0. Plan (written before any reading beyond the queue row)

1. Read check 1393 (`library/gap-dim-carry-check-astra62.md`) in full; row 1390; Theorem S (row 697) and
   check 699; rows 863, 1145; the filter (t1)-(t5) of row 1386 section 4.5 and Remark PAIR; (M-neutral) of
   row 1367; (A3) of row 1332.
2. FIRST GATE (Section 1-2): restate inequality (1), s_B(2q; beta, beta) <= s_B(q; 2 beta, beta/2), exactly;
   apply (t1)-(t5) and Remark PAIR at band couplings beta in [2.3, 2.6]; say what a positive answer would
   and would not give for (M-neutral). If the statement cannot be selective, prove that and stop.
3. Only if the gate passes: attack the inequality (interpolation H_z between F^2 and D, centered insertion),
   or build a counterfamily.
4. End with the next two rows and their decisive outcomes.

Each step is appended below as it is finished.

## 1. Repo search, the statement, the notation (15:53Z, date -u)

**Repo search.** The cross-branch search for this object is check 1393's (five refs; no neutral grid
comparison on any). Inside this folder I ran one `grep -l -i` loop over `library/gap-*.md`,
`library/open-core.md`, `parts/gap.md` and `FINISH.md`. Hits: "Karsch" 14 files (the one that matters:
row 1066, `gap-aniso-trajectory.md` L62, L128, the one-loop anisotropy coefficients, RECALLED there);
"time coarsen" only check 1393; "Trotter" 1 file; "uniform in b_s" none. `library/open-core.md` has no
entry for the gap lane. Lemma A2 of row 863 (`gap-crux-skeleton-max.md` 3.2, Claude Fable) is the
electric-only seed; Lemma END below extends its proof. Rows 1215 (5) and 1227 (11) (gpt-6.2-astra, checked)
give neutral near-vacuum levels at a fixed lattice as beta grows.

**The statement (check 1393, gpt-6.2-astra, inequality (1)).** B = n^3 periodic, 4 | n, q = floor(n/1024)
>= 1, neutral untwisted sector. s_B(t; b_s, b_t) = sum over a >= 1 of (lambda_a/lambda_0)^t for the Wilson
transfer with space-like coupling b_s and time-like coupling b_t. Decide at beta in [2.3, 2.6]:

  (1)  s_B(2q; beta, beta) <= s_B(q; 2 beta, beta/2) for all large n.

**Notation.** K_b is the one-step electric operator: on each link the convolution with
k_b = e^(b x)/c_0(b), x = tr/2, c_0(b) = integral of e^(b x), times the gauge projection Pi. So K_b 1 = 1
and K_b >= 0. Its link multipliers are u_j(b) = I_(2j+1)(b)/I_1(b), j = 1/2, 1, ... P_b = e^(b X) is the
multiplication by the space-like weight, X = sum of x_p over the plaquettes of B. The transfer at
(b_s, b_t) is T = P^(1/2) K P^(1/2) with P = P_(b_s), K = K_(b_t). Fine side: F = T(beta, beta), 2q steps.
Coarse side: D = T(2 beta, beta/2), q steps. F^2 and D differ in two ways, which I keep apart:

- (i) the splitting: K P K against K^2 P (the object of REF, rows 1390 and 1393);
- (ii) the kernel: K_beta^2 against K_(beta/2), multipliers u_j(beta)^2 against u_j(beta/2).

## 2. Four elementary facts (each PROVED here unless marked; unchecked)

### 2.1 Lemma KER (the kernel difference (ii) changes sign at a coupling of order one)

(a) As b tends to 0, u_(1/2)(b)^2 = b^2/16 + O(b^4) and u_(1/2)(b/2) = b/8 + O(b^3). So the coarse multiplier
is the larger one. (b) As b tends to infinity, u_(1/2)(b) = 1 - 3/(2b) + 3/(8 b^2) + O(b^(-3)), so
u_(1/2)(b)^2 = 1 - 3/b + 3/b^2 and u_(1/2)(b/2) = 1 - 3/b + 3/(2 b^2). So the coarse multiplier is the
smaller one, by 3/(2 b^2). In logarithms: -log u_(1/2)(b) = (3/2)(1/b + 1/(2 b^2)) + O(b^(-3)). The Wilson
kernel at b/2 is wider than the square of the kernel at b, by the relative amount 1/(2b). For compact U(1),
I_1/I_0 gives the same form: -log = (1/2)(1/b + 1/(2 b^2)).
Proof. (a) is the power series of I_1, I_2. (b) is Hankel's expansion, I_nu(x) = e^x (2 pi x)^(-1/2)
(1 - (4 nu^2 - 1)/(8x) + (4 nu^2 - 1)(4 nu^2 - 9)/(128 x^2) + ...), at nu = 1, 2: the ratio is
1 - (12/8)/x + (120/128 - (3/8)(3/2))/x^2. QED.
GUIDE (mpmath table under the numeric lock, script /tmp/gtc-fable/bessel.py, criterion written first; not a
proof step): u_j(b/2) - u_j(b)^2 at j = 1/2 is +0.043 at b = 2.3, +0.034 at b = 2.6, crosses zero at
b = 4.0 and is -1.43/b^2 at b = 50. At j = 1 it crosses near 6.2, at j = 3/2 near 10. For U(1), m = 1, it
is already negative at b = 2. So in the band the kernel difference favours (1) for SU(2) at j = 1/2.
A heat-kernel time-like weight has no difference (ii) at all (semigroup).

### 2.2 Proposition FREE ((1) holds mode by mode in the free noncompact theory, in every dimension)

Take the Gaussian model: real link variables, action (b_t/2) sum (time differences)^2 + (b_s/2) sum
(lattice curl)^2, constant modes removed. A transverse mode with lattice momentum square phat^2 has the
one-step kernel exp(-(b_t/2)(x - y)^2 - (b_s phat^2/4)(x^2 + y^2)). Its level ratio is e^(-omega) with
cosh omega = 1 + (b_s/b_t) phat^2/2. Fine: cosh omega = 1 + phat^2/2. Coarse: cosh Omega = 1 + 2 phat^2.
Then cosh 2 omega = 2 (1 + phat^2/2)^2 - 1 = 1 + 2 phat^2 + phat^4/2 > cosh Omega. So Omega < 2 omega for
every mode, and every coarse excitation factor e^(-q Omega) exceeds the fine one e^(-2 q omega). The same
holds at every later halving ((b_s/b_t) to 4 (b_s/b_t)). QED.
Reading. The Gaussian time-like kernel is a semigroup, so this is difference (i) alone. It is the known
lattice artefact of a coarser time step, omega = (1/a_t) arccosh(1 + a_t^2 omega_0^2/2). It is blind to the
group and to the dimension, and the theory has no gap. Its size on the modes that matter at time q (phat
of order 1/n) is relative phat^2/8, which tends to 0.

### 2.3 Lemma END (one coarse step is seeded for every space-like weight)

Let P >= 0 be any bounded gauge-invariant weight, not identically 0, T = P^(1/2) K_b P^(1/2) on the
gauge-invariant space, eps(b) = sum over j >= 1/2 of (2j+1)^2 u_j(b). If 10 e eps(b) <= 1/2, then on a
periodic box B with sides at least 4

  sum over a >= 1 of lambda_a/lambda_0 <= exp(6 (10e)^3 eps(b)^4 |B|) - 1,

and the same bound holds in the neutral sector. For b <= 1/(40e), eps(b) <= 2b.
Proof. (Vacuum.) K_b >= 0 and K_b 1 = 1, so K_b >= |1><1|. With psi = P^(1/2)/|P^(1/2)|,
lambda_0 >= <psi, T psi> = <P, K_b P>/Z_P >= Z_P, Z_P = integral of P. (Trace.) Tr T = integral of
P(U) K_b(U, U) dU, and K_b(U, U) = integral over site variables g of the product over links <xy> of
k_b(U_l g_y U_l^(-1) g_x^(-1)). Write k_b = 1 + f, integral of f = 0, |f| <= eps(b). Expand the product over
link sets Gamma. A site of degree 1 in Gamma integrates to 0 (Haar invariance in g_x), for every U. From
here the count is that of Lemma A2 of row 863 (Claude Fable): components have at least 4 links, at most
(10e)^(n-1) connected sets of n links through a link. So K_b(U, U) <= exp(6 (10e)^3 eps^4 |B|) for every U,
and Tr T <= Z_P times that. Divide by lambda_0 >= Z_P. The neutral projection commutes with T, keeps the
vacuum and drops nonnegative terms. The bound on eps: u_j(b) <= (b/2)^(2j) e^(b^2/4)/(2j+1)! from the power
series and I_1(b) >= b/2. QED.
New over A2: A2 is P = 1. Here the bound is uniform in the space-like coupling. It holds for every compact
group with the same proof (U(1): link currents), in every dimension with its own count.

### 2.4 Proposition CHAIN (the only self-contained use of time coarsening, and its strength)

Let n = 1024 x 2^m, so 2q = 2^(m+1) =: 2^K. Call (CH) the K inequalities
  s_B(2^(K-k); 2^k beta, 2^(-k) beta) <= s_B(2^(K-k-1); 2^(k+1) beta, 2^(-k-1) beta), k = 0, ..., K-1.
The case k = 0 is (1). If (CH) holds and beta <= 2q/(40e), then by Lemma END at b = beta/(2q)

  s_B(2q; beta, beta) <= exp(96 (10e)^3 beta^4 n^3/(2q)^4) - 1 <= exp(1.4 x 10^17 beta^4/n) - 1.

Proof. Chain the K inequalities. The last term is one step at (2^K beta, beta/2^K), and Lemma END applies
with eps <= 2 beta/(2q). Here 2q = n/512, so n^3/(2q)^4 = 512^4/n, and 96 (10e)^3 512^4 < 1.4 x 10^17. QED.
So (CH) gives the neutral seed (4/21) at the coupling beta on every such box with n >= 10^18 beta^4, for
every beta.
No transport back to an isotropic grid, no entry and no rate question remain: in Theorem T's terms
(row 1332, Claude Fable) it is (A2) with a size polynomial in beta, that is c = 0.
- (CH) is therefore stronger than the target of the lane, not a step toward it.
- (CH) is believed false at large beta (ARGUED, belief grade): a box of n = 10^18 beta^4 sites at large beta
  is far below the physical scale (n << exp(2.69 beta)), the neutral levels there are of order g^(2/3)/n
  and the neutral sum at time n/512 is large. Rows 1215 (5) and 1227 (11) prove the fixed-lattice form; their
  constants depend on n, so they do not cover n = 10^18 beta^4. I did not prove the failure.
- Proposition FREE shows where a failure cannot sit: the Gaussian part obeys every link of (CH). Lemma END
  uses compactness. I did not locate a failing link.

## 3. The first gate (15:54Z, date -u)

### 3.1 What (1) says in the scaling region (GUIDE: one-loop matching; coefficients RECALLED, not read)

Source: F. Karsch, Nucl. Phys. B 205 (1982) 285, as quoted in row 1066 (`gap-aniso-trajectory.md` L62,
recalled there, not read): on a lattice with xi = a_s/a_t the couplings that keep the isotropic physics are
g_sigma^(-2) = g^(-2) + c_sigma(xi), g_tau^(-2) = g^(-2) + c_tau(xi), with the sum rule
c_sigma' + c_tau' = b_0 = 11 N/(48 pi^2) at xi = 1 (SU(2): 0.11403 - 0.06759 = 0.04644).
The coarse side of (1) has xi_0 = 1/2 and equal bare couplings. Matching the two products gives, to first
order, an equivalent isotropic coupling and a true anisotropy

  beta_eq = beta - 2 (c_sigma + c_tau)(1/2),   a_t/a_s = 2 (1 + (c_tau - c_sigma)(1/2) g^2/2).

With c linear in log xi from xi = 1: c_sigma + c_tau = -b_0 log 2, so beta_eq = beta + 2 b_0 log 2
= beta + 0.064. This is one quarter of the one-loop step delta = (11/(3 pi^2)) log 2 = 0.2575 of row 1386
(STEP). The reading: the bare coupling sits at the geometric-mean cutoff (a_s^3 a_t)^(1/4). Doubling a_t
at the same bare coupling lowers that cutoff by 2^(1/4). So the coarse grid is the same continuum theory
on a box that is smaller by about 2^(-1/4) in physical units, at nearly the same shape
(a_t/a_s = 2 (1 + 0.18/beta) with the recalled numbers, linear in xi).

Consequences (all GUIDE; none is a proof step):
- (S1) SU(2), d = 4, gapped infinite-volume regime (n far above the correlation length). With gaps m_F
  (fine, per fine step) and m_D (coarse, per coarse step), log s is -2 q m_F and -q m_D up to powers of n.
  So (1) for large n follows from m_D < 2 m_F and implies m_D <= 2 m_F. The matching gives
  m_D/(2 m_F) = exp(-2.69 x 0.064)(1 + 0.18/beta): 0.84 as beta grows, about 0.90 at beta = 2.45
  (0.95 with c linear in xi). So (1) is expected to hold, with a margin of 5 to 16 percent in the exponent.
  At beta in [2.3, 2.6] this is an extrapolation of a one-loop formula with recalled constants. It decides
  nothing.
- (S2) SU(2), d = 4, small physical box (n << exp(2.69 beta)). The same matching: the coarse box is smaller,
  its coupling at the box scale is weaker, its neutral levels are lower, its sum is larger. (1) is expected
  to hold there too.
- (S3) Compact U(1), d = 4, large beta. b_0 = 0, so the leading term vanishes. The sign then rests on the
  anisotropy constant. For the Wilson U(1) action the one-loop effect is exactly the Hartree factor
  <cos theta_p> on each plane. The time-like plaquettes of the coarse grid fluctuate more (rough mode
  average: <1 - cos> is 0.38/beta time-like against 0.155/beta space-like). So the effective ratio
  b_s/b_t exceeds 4, and the low modes have Omega > 2 omega by a relative 0.1/beta. This beats the artefact
  of Proposition FREE (relative phat^2/8) on all modes with phat^2 < 1/beta, which are the modes that matter
  at time q. So (1) is expected to FAIL for compact U(1) in the Coulomb phase at large n. (On a fixed box
  near Haar it holds for U(1), check 1393.)
- (S4) d = 5, weak coupling: no logarithm, the same tie; the sign rests on the anisotropy constant.

### 3.2 The filter (t1) to (t5) of row 1386 and Remark PAIR, applied to (1) at band couplings

| Test | Verdict for (1) | Named line |
|---|---|---|
| (t1) compact U(1), d = 4 | PASSES at GUIDE grade. The leading term of (1) is zero for U(1), and the next term has the opposite sign (S3). Not proved. | Karsch's sum rule c_sigma' + c_tau' = b_0, with b_0 = 0 |
| (t2) SU(2), d = 5, on the step (PAIR) | PASSES at GUIDE grade as a statement: no logarithm in d = 5 (S4). But see PAIR below: the map of couplings (beta, beta) to (2 beta, beta/2) is the same in every dimension. | the same sum rule; check 1393 L77 |
| (t3) SU(3) | PASSES: the statement and the sum rule exist for SU(N). | b_0 = 11 N/(48 pi^2) |
| (t4) beta grows at a fixed lattice | (1) SURVIVES (S2). By the wording of (t4) a hypothesis that survives is dead as a trigger. (1) is not a trigger: it has no hypothesis that a seed could follow from. (CH) is a trigger, and it is dead by (t4) at belief grade (2.4). | rows 1215 (5), 1227 (11) |
| (t5) equivalence | FAILS. See 3.3: the zero-gain form gives nothing, and the gain form is a quarter of (STEP), which is the target above the first-passage coupling. No method is named beside the sign of the centered insertion, and that sign is the statement. | row 1386 4.1, 4.5 |

Remark PAIR applied. PAIR splits a mechanism into a gain (reads the group) and a carry (reads the
dimension). One time coarsening is one direction of a carry at zero gain. In d = 4 the four coarsenings
return the same weight beta (CW, check 1393), so the composite is the statement "the quotient of the grid
2n at beta is at most the quotient of the grid n at beta". In PAIR's variable this is x(2L) <= x(L). It is
true exactly when the gains are nonnegative. It holds no gain. PAIR's missing object is an inequality that
passes a proved local gain through the carry. (1) passes none: both sides of (1) have the bare coupling
beta.

### 3.3 Proposition USE (what a positive answer gives; PROVED as logic, given the statements named)

Put Sigma_iso(n, beta) = s_(n^3)(2 floor(n/1024); beta, beta), the quantity of (M-neutral) (row 1367,
gpt-6.2-astra; rows 1356, 1359), and Sigma_an(n, beta) = s_(n^3)(floor(n/1024); 2 beta, beta/2). Then (1) is
Sigma_iso <= Sigma_an at the same n and the same beta.

(a) Alone, (1) bounds the target by Sigma_an. Nothing on file bounds Sigma_an at a band coupling. Row 1145's
strip seed keeps the time-like coupling and moves the space-like one (check 1393 L77), and Lemma END needs
b_t <= 1/(40e) and n^3 b_t^4 small. So (1) alone gives (M-neutral) nothing.

(b) The transport. Suppose the three space-like coarsenings are also granted in the form
(R): Sigma_an(n, beta) <= Sigma_iso(n/2, beta), for n = 1024 x 2^m, m >= 1 (both sides then have q steps). Then Sigma_iso(n, beta) <= Sigma_iso(n/2, beta), and by
iteration Sigma_iso(2^k n_0, beta) <= Sigma_iso(n_0, beta). Every inequality in this family has one coupling
on both sides. (R) is open: the space-like coarsenings change the Hilbert space, and the vacuum
normalisation has no sign there (Theorem S of row 697, Claude Fable, check 699, handles it only below
the seed level).

(c) The rate. (A2) of Theorem T (row 1332) asks: from a seed at beta_w, a seed at every larger beta at a
size N(beta) <= C_1 exp(c (beta - beta_w)), with c inside (A3). The family of (b) never raises beta. In
(STEP)'s terms it has delta = 0, and (A3) needs delta > 0.173 (GUIDE of row 1386). So (1) with (R) gives
no rate at all, not a poor one.

(d) The entry. For (M-neutral) at a late cutoff (n_j, beta_j), (b) gives
Sigma_iso(n_j, beta_j) <= Sigma_iso(n_j/2^k, beta_j): a smaller box at the same late coupling. There the sum is
believed large; rows 1215 (5) and 1227 (11) prove this at a fixed lattice as beta grows. So the family has no entry. Below the seed level the
doubling at one coupling is already Theorem S, with a strict contraction, for the full trace.

(e) The gain form. Write (1_d): s_B(2q; beta + d, beta + d) <= s_B(q; 2 beta, beta/2), d > 0, and (R_d')
likewise. Then (R_d') and (1_d) give: a seed on the grid n/2 at beta gives a seed on the grid n at
beta + d + d'. This is (STEP) with delta = d + d'. The one-loop guide of 3.1 puts d near 0.064. By row 1386
4.1, (STEP) above the first-passage coupling is equivalent to the target. So the gain form is the open
infrared carry cut into four directions. It is not a smaller statement.

QED (a) to (e) are implications between the named statements; nothing in them is an estimate.

### 3.4 The sufficient test of check 1393 (the centered insertion along H_z)

I did not attack it, by the gate. Two remarks. First, in the band both differences of Section 1 point the
way of (1): (i) by Proposition FREE, (ii) by Lemma KER at j = 1/2 (GUIDE table). Second, the centered
insertion is the difference between the thermal mean and the vacuum mean of the extensive observable
E = D - F^2 in units of H_z. It is of the same kind as Delta(b) in the path identity of row 863 (3.3
there), which that row found to be a restatement of the seed question. A pointwise sign would prove (1),
and by Proposition USE (1) is not worth a proof.

## 4. Verdict

- **(1) at beta in [2.3, 2.6], all large n: NOT DECIDED.** No proof and no counterfamily. GUIDE: expected
  true for SU(2) in d = 4 (3.1 (S1)), because one time coarsening at equal bare coupling is a quarter of an
  asymptotic-freedom step toward the smaller box.
- **Gate: (1) is selective as a statement and useless as a step.** I could not prove "cannot be selective",
  and at GUIDE grade the opposite holds: its sign reads b_0 through Karsch's sum rule ((t1) to (t3) pass,
  unproved). The statement fails (t5) and Remark PAIR: a positive answer gives no transport, no rate
  (delta = 0 against the 0.173 that (A3) needs) and no entry (Proposition USE, PROVED as logic). Its gain
  form is a quarter of (STEP), that is, the open infrared carry itself.
- **Proved on the way (unchecked):** Lemma KER (the Wilson kernel difference changes sign near beta = 4 at
  j = 1/2; expansions proved, crossing value GUIDE). Proposition FREE (the free theory obeys (1) mode by
  mode in every dimension: the sign of the splitting is a lattice artefact). Lemma END (one step is seeded
  for every space-like weight when n^3 b_t^4 is small; extends A2 of row 863). Proposition CHAIN (the
  full dyadic chain of time coarsenings would give the neutral seed at every beta on boxes of polynomial
  size; so the chain is stronger than the target and, at belief grade, false at large beta).
- **Recommendation: queue no proof row on (1) or on its gain form.**

What is not established: every line marked GUIDE or ARGUED; the failure of (CH); the U(1) reversal (S3);
Karsch's coefficients at xi = 1/2 (I used a linear continuation of recalled values at xi = 1).
No Monte Carlo was run. One mpmath table (Bessel ratios) ran under the numeric lock as a guide.

## 5. The next two rows and their decisive outcomes

1. **Check of this file by the other provider** (short). Order: Proposition USE (b) to (e); Lemma END (the
   vacuum bound lambda_0 >= Z_P and the degree-one cancellation for every U); Proposition CHAIN's constant;
   Proposition FREE; Lemma KER (b). Decisive outcomes: if USE holds, the time-coarsening line of check 1393
   closes with no proof row. If USE (c) or (d) fails, the check names the consumer that reads a zero-gain
   carry, and that consumer is the next row.
2. **Only if the lead wants (1) itself settled in the scaling region: one hand computation row.** Read
   Karsch 1982 and compute c_sigma, c_tau at xi = 1/2 for SU(2), and the Hartree anisotropy constant for
   compact U(1) at (2 beta, beta/2) with exact lattice sums. Decisive outcomes: (S3) confirmed makes (1) an
   example on file of a statement that passes (t1) to (t3) and still gives nothing, which sharpens the
   filter (pass (t5) and PAIR first). (S3) refuted makes (1) non-selective outright. Neither outcome moves
   (M-neutral). I judge this row low value and do not ask for it.

Credit. Inequality (1), the interpolation test and the row are check 1393's (gpt-6.2-astra). REF and the
grid class are row 1390's (Claude Fable). Lemma A2 and the path identity are row 863's (Claude Fable).
Theorem S is row 697's. Theorem T and (A3) are row 1332's. The filter, (STEP) and Remark PAIR are row
1386's, with the reading of row 1128. The anisotropy coefficients are Karsch's, as recalled in row 1066.
From the Sussman-Alpoge repository (with Claude and Codex as authors of their text) this note uses only
what check 1393 already read there: the positive gauge-projected Wilson transfer and its trace (outline
2315-2335) and the change of units (CA-III 9.13). I opened no further source.

RESULT: Row 1396 (Claude Fable 5.2 medium, Mac mini worker 1; author only, checked by no one; no Monte Carlo, one Bessel table under the numeric lock as a guide, no subagents). Inequality (1) at beta in [2.3, 2.6] for all large n is NOT DECIDED: no proof, no counterfamily. The first gate stops the row. PROVED as logic (Proposition USE): a positive answer gives (M-neutral) no transport, no rate (delta = 0 against (A3)) and no entry, and its gain form is a quarter of (STEP), the open infrared carry. PROVED, unchecked: Lemma KER (kernel sign change), Proposition FREE (the free theory obeys (1) mode by mode in every dimension), Lemma END (one step is seeded uniformly in the space-like weight), Proposition CHAIN (the full dyadic chain would give the seed at polynomial box size, so it is stronger than the target). GUIDE only: (1) reads b_0 through Karsch's sum rule, so it is expected true for SU(2) in d = 4 and false for compact U(1) at weak coupling. Open: (1) itself, the failure of the chain, the U(1) reversal, (M-neutral).
