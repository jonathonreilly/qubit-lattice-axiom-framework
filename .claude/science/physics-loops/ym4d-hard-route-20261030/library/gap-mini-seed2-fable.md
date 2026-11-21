lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T23:35Z

# The neutral seed for the SU(2) Wilson trajectory at late cutoffs: attempt 2 (row 1364)

Queue row 1364, `gap-mini-seed2-fable`. Claude Fable 5.2 max, Mac mini worker 2, pinned at commit 767a6b4e5. Started 2026-11-21T11:35Z (date -u). Author only; checked by no one. Research-stage working state; grants no status. Independent of row 1363, which this file does not read.

## 0. The problem, and the plan of this file

**Problem (row 1364).** In the coupling range of `library/gap-phys-seed.md` (beta_0 <= beta_j <= B_0 log(L/a_j)), uniformly in the cutoff and the volume, show that the neutral transfer kernel over some fixed physical time w satisfies s(2w) <= 4/21 (the rank-one test (M-neutral) at tolerance 2/5; row 1356 Lemma M1 and Corollary M2, checked by row 1359). Or disprove (M-neutral) for the Wilson trajectory, or a step of the chain that consumes it.

**Labels.** PROVED, ARGUED, GUIDE, OPEN, as the row asks.

**Plan.** Step 1: read the exact statements the row names (gap-phys-seed, rows 1342, 1349, 1353, 1356 and their checks) and write the precise target. Step 2: prior-identity and route screening (memory of this lane: 32 route families on file; rows 1351-1362). Step 3: choose one attack and carry it. Each step is appended below before the next begins.

(Sections follow as the work proceeds.)

## 1. The target, exactly (written 11:44Z, date -u)

Read for this section: GOAL.md; FINISH.md L1-84, L299-356 and the rows 754, 755, 760, 842, 862, 1007, 1009, 1010, 1342, 1349, 1353, 1355, 1356, 1359-1364; `parts/gap.md` L8-104 and L223-320; `library/gap-phys-seed.md` L280-330 (Lemma Z3, Theorems ZD and ZD-c, the two lead notes); `library/gap-mini-mneutral-fable.md` L1-130 (Lemma M1, Corollary M2); `library/gap-mini-neutral-step-fable.md` L52-72 and L380-412 ((N-phys), Corollary BT2).

Notation (row 1353, 2.1 and 6.1; row 1356, Section 2). The spatial box is the periodic lattice n^3. T is the Wilson transfer operator on the gauge-invariant functions of the slice configurations. P_0 is the mean of the eight centre translations. lambda_0 is the vacuum eigenvalue. x_a = lambda_a/lambda_0, a >= 1, are the relative eigenvalues of the neutral sector (electric flux zero, magnetic twist zero). s(u) = sum over a >= 1 of x_a^u.

- (N-phys): there is an admissible physical side L such that for all late j: 4 divides n_j, n_j >= 2^70, and there is an integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j; n_j^3) <= 1/2.
- (M-neutral) at tolerance 2/5 is s(2w) <= 4/21 at some w <= n/1024 (row 1356, Corollary M2 (i); check row 1359). It gives (N-phys) with no loss in the time, and (N-phys) gives it at w >= 3u/2.
- With Z_+(t) = Tr(P_0 T^t) = lambda_0^t (1 + s(t)): 1 + s(u) <= Z_+(u)^2/Z_+(2u) (Lemma TP of row 1342).

Reading in thermal terms (on file: Lemma Z, Lemma Z', Proposition Delta, rows 1180 and 1184; not new). The number log(1 + s(u)) is the volume n^3 times the thermal pressure of the neutral sector at the temperature 1/u, in units of that temperature. A free gas of three massless vector particles has pressure (pi^2/15) T^4, so it gives log(1 + s) about 0.66 (n/u)^3, at least 0.66 x 512^3. (N-phys) asks for log(3/2) = 0.405. For a massive particle of mass m the one-particle term is n^3 (m/(2 pi u))^(3/2) e^(-m u); at n = 512 u it is below 1/2 once m u is at least about 22, so the physical side is L at least about 1.1 x 10^4/m (my arithmetic, GUIDE). So the seed is a low-temperature statement far above the correlation length. It is not a statement at the scale where the running coupling is small.

## 2. Screening against the file (written 11:53Z, date -u; ARGUED, no proof)

I listed the routes I would take from first principles and looked each one up before any derivation. Every one has a match, so none is attacked again here.

| Route (my words) | Match on file | State there |
|---|---|---|
| Stiffness iteration with a commutator gain (the posted 2D O(4) mechanism of OpenAI), ported to 4D | rows 1009-1016, 1228; `library/prior/gap-o4-pinned-cell-read-opus.md` | closed: the gauge field has no non-gauge symmetric twist; the class of all pins is not closed in 4D (Theorem D2, Lemma SHEET) |
| Loop equations with positivity (bootstrap of Anderson and Kruczenski, Kazakov and Zheng) as a certified order-one input | rows 754-762, 1326, 1331 | a fixed-radius certificate cannot see the finite-size shift (Theorem O of row 760; Remark OS) |
| Thin twisted torus, fractional instantons (Tanizaki and Unsal; 't Hooft; van Baal) | Route T, rows 678-687, 842, 862 | a gap proved in a window of base sizes at weak coupling; no carry to the cube |
| Thermal form, rotated frames, Casimir energy | Lemma Z, Z', Proposition Delta; rows 1180, 1184 | equivalent forms of the target |
| Ground-state representation, Lipschitz transport, coding, Poincare inequality of the 4D measure | row 1356; rows 941, 957, 968; Proposition UNI of row 1237 | each needs a regularity statement at order-one coupling |
| Centre decomposition SU(2) = Z_2 x SO(3) (Mack and Petkova), thick vortices | rows 1345, 1351, 1354, 1358, 1360 | thin signs are locked on the tail; the step is (BS-thick) or (BS-BL) |
| Twist ratios and the zero-mode count (margin 2^(11/3)), theta sectors | rows 731, 1200 | an engine for the flux half only |
| Verified computation of the seed | rows 1326, 1331, 1332 | no finite sufficient statement on file |

What the screening leaves. The band has no small parameter, and every class-wide tool is bound by a comparison model. The registry of `parts/gap.md` (L223-256) lists reopen conditions. Section 3 takes the flow statement in its rate form, (LEV_K) of row 708.

Further matches found after the table above was written (same section, added 12:23Z, date -u). Each was derived here first and then found on file; none is called new.

| Derived here | Match on file | State there |
|---|---|---|
| The Wilson one-link kernel is a mixture of heat kernels (Hartman and Watson; Kent), so K is a mean of electric semigroups with random times | prior B8, `library/gap-sepinput-max.md` L146-148; `library/gap-mini-mneutral-fable.md` L456-457 (row 1356, 6.3) | used there; gives the jump form from above only |
| K_(beta') <= K_beta^theta with Araki's log-majorization relates the isotropic operator to a shorter time step | row 1356, 6.3 (Golden-Thompson, Araki); Lemma R4 of row 1180 | bounds products of top eigenvalues, no ratio x_k |
| A seed at one coupling climbs to late cutoffs if no neutral level falls faster than at a logarithmic rate K in the coupling | (LEV_K), (VIR_K), (DEF_K): Theorem TR and Corollary TR1 of row 708, `library/gap-mid-max.md` L52-58, L120-176; Theorem U of row 710 | OPEN; three failed ways on file (L160-170) |
| In the vacuum representation the rate is a covariance: -d mu_a/dt = Cov(f_a^2, Y), and a bound needs the gradient of the solution of L psi = Y - <Y> | Lemma 4.1 and (HS-sup) of row 677 (`library/gap-zf-box-x.md`); Way 2 of row 708 | OPEN; constants from stability theorems depend on the gap (Proposition B of row 677) |
| Re log(lambda_0/lambda_1) is a positive harmonic function of the complex coupling where the two levels stay apart; Harnack then gives the rate from the width of a tube | Route Z: Theorems LP, Z, ZB of row 670 (`library/gap-zero-transport.md` L48-96), Harnack chain of check 681, `library/gap-zf-box-s.md` L108-117 | the crux is the zero-free tube (ZF_B); proved for Re beta at most 1/10 only (Theorem A of row 677) |
| The tube in the coupling is analyticity under a complex dilation of all lengths; its half-width is pi/(2 c_a) for masses and pi/(4 c_a) on periodic tori | `library/gap-skeleton-max-b.md` L313, L325 ((BD-ir)), L497 ((ZF_B-s)); `library/gap-zero-transport.md` L82 | OPEN, "no data" |
| The 2D stiffness mechanism, in temporal gauge, sees only the sectors that violate the Gauss law (static charges); the neutral sector is what is left | rows 1011-1016, 1115, 1241 ((SING); "the neutral half is the real content") | (SING) is OPEN in two dimensions too |
| A family with the same group, centre symmetry, reflection positivity and asymptotic freedom, and with no gap: adjoint matter in the conformal window | test table of `parts/gap.md` L293 | BELIEF; binds every tool that does not use the locality of the pure gauge weight |
| Thin twisted torus: a gap of order 1/n on the flip-even sector holds at weak coupling in a window of base sizes, but the thin directions are hot channels, and a doubling of a thin side loses the twist | rows 842, 862 (Theorems BAD, CH-D, A, B); row 1200 (index engines) | no carry to the cube |

## 3. How best to attack it, and the one route carried to its first failing step (written 12:26Z, date -u)

### 3.1 Decision (ARGUED)

1. A proof cannot be structural. The classes on file bind every tool that reads only reflection positivity, the centre, the group, the dimension and positive plaquette weights (compact U(1), frozen groups, the weights w_p of Proposition V, products; test table of `parts/gap.md` L279-293). With matter the same structure allows a theory with no gap (the conformal-window row of that table, BELIEF). So a proof must contain a quantitative statement about the pure gauge measure at a coupling of order one, or about the flow through that range.
2. There are two places to put that statement. (K-one): a number at one coupling, which needs a consumer and, since 2026-11-20, could come from a formal computation. Rows 1326, 1331, 1332 size it and find no finite sufficient statement of computable size. (K-flow): a rate. In the coupling variable the weakest form on file is (LEV_K) of row 708: no neutral level falls faster in the coupling than at a logarithmic rate K. With a strong-coupling base it gives the seed at every coupling (Theorem TR, Corollary TR1), and the rest is the carry to late cutoffs.
3. I took the rate. Reason: it is one inequality, it is false for compact U(1) at its transition (row 708 (ii)), and the vacuum representation gives it a form that reads only the vacuum. Section 3.2 is that form. It did not close.

### 3.2 The rate in the vacuum representation (Setting H: the lattice theory with continuous time)

Setting. H_t = X - t Y on the gauge-invariant functions on the slice configurations, with X = -2 times the sum of the link Laplacians and Y a bounded real function (for the Kogut-Susskind form, Y is the sum of (1/2) tr U_p over the plaquettes of the slice and t is beta^2 up to the normalisation). Omega_t > 0 is the ground state, phi_t = log Omega_t, mu_t = Omega_t^2 dU. In L^2(mu_t) the operator H_t - E_0(t) becomes L_t = -2 (Laplacian + 2 grad phi_t . grad), with <f, L_t f> = 2 integral of |grad f|^2 d mu_t. A level a has the eigenfunction f_a of L_t, with eigenvalue m_a(t) = E_a(t) - E_0(t) and integral of f_a^2 d mu_t = 1. Put Y^ = Y - integral of Y d mu_t and psi = d phi_t/dt.

**Lemma OSC (PROVED, elementary; unchecked).** (i) L_t psi = Y^. (ii) d m_a/dt = - integral of f_a^2 Y^ d mu_t = integral of (4 |grad f_a|^2 - 2 m_a f_a^2) psi d mu_t. (iii) For every analytic branch of every level, |d log m_a/dt| <= 2 osc(psi), with osc = sup - inf.

Proof. (i) Differentiate (H_t - E_0) Omega_t = 0: (H_t - E_0)(psi Omega_t) = (Y + E_0') Omega_t, and E_0' = - integral of Y d mu_t (first-order perturbation; Y is bounded, so the family is analytic and Omega_t is analytic in t). (ii) The first equality is first-order perturbation for E_a and for E_0. For the second, L(f^2) = 2 f L f - 4 |grad f|^2, so the integral of f_a^2 L_t psi equals the integral of (2 m_a f_a^2 - 4 |grad f_a|^2) psi. (iii) The weight 4 |grad f_a|^2 - 2 m_a f_a^2 has integral 2 m_a - 2 m_a = 0. So psi may be replaced by psi - c, and the integral of 4 |grad f_a|^2 + 2 m_a f_a^2 is 4 m_a. Take c at the middle of the range of psi. QED

Reading. (iii) is (LEV_K) for all levels at once, with K read from one function of the vacuum. The first equality of (ii) is first-order perturbation, on file for the Wilson operator as Theorem U of row 710 (`library/gap-vir-sc.md` Section 3). The statements (i), (ii) second equality and (iii) were not found by grep in `library/gap-*.md` ("d log Omega", "osc(psi)", "2 osc": no match in this form); `library/open-core.md` has no line on them. I do not count them as progress: they are the counterpart, for the vacuum generator, of Lemma 4.1 and (HS-sup) of row 677 (`library/gap-zf-box-x.md` L177-184, stated there for the generator of the four-dimensional measure). Part (iii) is not a route: psi is a sum over the volume of terms of bounded oscillation, so osc(psi) grows with the box. It restates the bound of Way 2 of row 708 (`library/gap-mid-max.md` L166) as a relative one.

First failing step. A bound free of the box needs the local form of (ii): d m_a/dt = -4 times the sum over links of the integral of f_a (grad_l f_a) . (grad_l psi). With a bound on sup |grad_l psi| (the counterpart of (HS-sup) of row 677, OPEN there) the sum is still not bounded by the Dirichlet form of f_a, because the sum over links of the integral of |f_a| |grad_l f_a| grows like the square root of the volume for a level that is spread over the box. The true value is small by a cancellation: the weight in (ii) has conditional mean near zero given the fields near any one place. That is a locality statement for the excited level with a constant free of the gap. By a scaling argument the constant is the inverse of the lattice beta function read from that level (row 708, L176), so it is finite exactly when the flow has no fixed point. I found no input that gives it. Three ways tried here, each ends on a statement on file: the oscillation bound above (extensive); Harnack's inequality for Re log(lambda_0/lambda_a) in a complex disc of the coupling (needs the zero-free tube (ZF_B) of Route Z); the thermal mean with the diagonal heat kernel q_t(x) = p_t(x, x) - 1 >= 0 (gives the bound sup |Y^|/m_1, the trivial rate of row 708, L57).

### 3.3 Notes for the lead (ARGUED; none is a proof step)

- A tool not named on file (grep "Siciak", "separately analytic", "cross theorem": 0 files in `library/gap-*.md`; "Hartogs" and "complex dilation" appear in `gap-skeleton-max.md` L118 and `gap-skeleton-max-b.md` L325 for the two-point function and for (BD-ir)). The torus partition function is analytic in each period in a half-plane when the other periods are real, by the transfer operator in that direction, and log Z is analytic there where that direction is cold (the excited trace at the real part of the period is below 1). Siciak's theorem on separately analytic functions then gives joint analyticity in the hull where the sum of the four relative extremal functions is below 1; for half-planes over a long interval of the positive axis the extremal function at the angle theta tends to 2 theta/pi, so this allows a common complex dilation by an angle up to nearly pi/8 (less for short intervals). So, given a seed and scaling, (BD-ir) holds in a tube of half-width up to nearly (pi/8)/c_a. This is a consequence of a seed, not a way to one, and it needs continuous periods, which the lattice has in one direction only.
- Why the 2D mechanism does not reach the neutral half, in one line: in temporal gauge the only non-gauge symmetric twist is a time-dependent gauge rotation, its cost is the energy of static charges, and that is of order 1/beta per step for every compact group. The posted 2D proofs reach singlets by association only (row 1241).

## 4. Verdict (written 12:29Z, date -u)

(N-phys), equivalently (M-neutral) at tolerance 2/5, is NOT proved in this row. No counterexample is built. No step of the chain (rows 1161, 1179, 1342, 1349, 1353, 1356 with their checks) is disproved; I re-derived only the elementary ones (Lemma TP, Corollary M2 (i)) and they hold.

What this row adds.

- An independent pass over the problem, without reading row 1363. Every route I derived from first principles is on file with its first failing step (Section 2, two tables, 17 routes). This agrees with rows 1188-1259: a plain brief returns the map.
- Lemma OSC (Section 3.2; PROVED by hand, elementary, unchecked): in the lattice theory with continuous time, d m_a/dt is the integral of a weight of total mass zero and absolute mass 4 m_a against the coupling derivative psi of the log-vacuum, and L psi = Y - <Y>. So every level obeys (LEV_K) with K = 2 osc(psi). The bound grows with the box, so it is not a route. It states the first failing step in one line: a rate free of the box needs the weight to have conditional mean near zero near every place, a locality statement for excited levels with a constant free of the gap.
- Two notes (Section 3.3, ARGUED): Siciak's theorem as a supplier of (BD-ir) from a seed, with an angle up to nearly pi/8; the temporal-gauge reading of why the 2D stiffness mechanism covers only the charged half.

The one statement where every route of this row stops. A quantitative bound in the law of the pure gauge model at a coupling of order one. In the coupling variable it is (LEV_K) of row 708 with K free of the box; as a number at one coupling it is the seed at a window coupling with a carry; as an analytic statement it is the zero-free tube (ZF_B) of Route Z; as a block statement it is (BS-thick) or (REG-vac). I found no implication among these that is not on file, and no supplier for any of them.

Labels. PROVED: Lemma OSC. ARGUED: Sections 2, 3.1, 3.3 and the scaling remark of 3.2. GUIDE: the arithmetic of Section 1. OPEN: (N-phys), (M-neutral), (LEV_K), (ZF_B), the carry to late cutoffs, the mass gap.

Limits of this row. (1) The files of rows 1161, 1179, 1342 were not re-read line by line; their RESULT lines and checks were used. (2) The cross-branch search (main and the open pull requests) cannot be run from this checkout, where origin/main is not a ref; it was not done. (3) No numeric run was made; the numeric lock was not taken. (4) Credits: K. Wilson; K. Osterwalder and E. Seiler; M. Luscher; T. Balaban; E. Sussman and L. Alpoge with Claude and Codex as authors of their text (the account and its trajectory); G. 't Hooft; G. Mack and V. Petkova; P. Hartman and G. Watson, J. Kent (the heat-kernel mixture); J. Siciak (separately analytic functions); OpenAI, and J. Ding, F. Huang and P. Yang (the posted 2D proofs, as read in rows 1007-1010); in this lane gpt-6.2-astra (rows 1161, 1165, 1345, 1351), Claude Opus 5.5 (checks), Claude Fable 5.2 (rows 670, 677, 708, 710, 1332, 1342, 1353, 1354, 1356, 1358, 1360).

RESULT: Row 1364 (Claude Fable 5.2 max, Mac mini worker 2; author only, checked by no one; no numeric run; independent of row 1363, not read). NOT solved: the neutral seed (N-phys), equivalently (M-neutral) at tolerance 2/5, is not proved for the Wilson trajectory; no counterexample is built and no step of the chain is disproved. Seventeen routes derived from first principles were each found on file with their first failing steps (two tables in Section 2), so this is an independent confirmation of the wall, not a new route. PROVED here (by hand, elementary, unchecked): Lemma OSC, for the lattice theory with continuous time: the coupling derivative psi of the log-vacuum solves L psi = Y - <Y>, d m_a/dt is the integral of (4 |grad f_a|^2 - 2 m_a f_a^2) psi, and so every level obeys (LEV_K) of row 708 with K = 2 osc(psi); the bound grows with the box and is not a route. ARGUED: a proof needs a quantitative statement in the law of the pure gauge model at a coupling of order one (a number with a carry, or a rate (LEV_K) free of the box, or the zero-free tube (ZF_B), or a block step); Siciak's theorem would give (BD-ir) from a seed in a tube of half-width up to nearly (pi/8)/c_a. First failing step: a locality bound for excited levels with a constant free of the gap, which by scaling is the statement that the flow has no fixed point. OPEN: (N-phys), (M-neutral), (LEV_K), (ZF_B), the carry to late cutoffs, the mass gap. Output library/gap-mini-seed2-fable.md.
