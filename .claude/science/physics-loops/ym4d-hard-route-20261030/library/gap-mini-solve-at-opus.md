lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:42Z

# gap-mini-solve-at-opus: the SU(2) mass gap, one more attack (FINISH row 1294)

Started 2026-11-20T15:42Z (date -u). Claude Opus 5.5 max, Mac mini worker 2. Research-stage working state; nothing here is a public claim. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Status (updated in place)

- Step 7 (kappa_0 > 6 removed: Corollary U') written 2026-11-20T16:26Z.
- Step 6 ((H-an'), (H-tail) from the account's apparatus: Proposition HAN) written 2026-11-20T16:23Z.
- Step 5 (state of the carry after this row) written 2026-11-20T16:18Z.
- Step 4 (H2' covariance clause: margin (M), no connectedness) written 2026-11-20T16:15Z.
- Step 3 (Lemma SYM: (H-flip) removed) written 2026-11-20T16:09Z.
- Step 2 ((S-chart)) written 2026-11-20T16:06Z.
- Step 0 (record read) and Step 1 (judgement and plan) written 2026-11-20T16:01Z (date -u). Work steps follow.

## Repo search (rule "Repo first")

Searched this folder only (the open YM4D branches were searched by rows 1218 and 1264 for the same objects; not
repeated). Greps of `FINISH.md`, `library/*.md`, `library/prior/*.md` for the candidate mechanisms named in Step 1
(O'Neill, orbit space, Luscher/admissibility, instanton, Mack-Petkova, Z_2 monopole, Feynman, Zwanziger/Gribov, Singer,
Goepfert-Mack, Tomboulis, Yaffe, Bakry-Emery, spin foam/6j, loop equations/bootstrap): every one has hits, between 2
and 539 files. Row hits for loop equations with positivity: rows 688-770, 934, 1031, 1133.

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T16:01Z by date -u)

Read at pin 59f4e99fc: `GOAL.md` in full; `FINISH.md` L1-90 and L299-357, this row (L1375), and the RESULT segments of
rows 1255-1298 and 985-995; `parts/gap.md` L1-104 and the obligation headers; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; Steps 0-3 of `library/gap-mini-solve-aq-opus.md` (row 1284, running on another worker); Step 6 of
`library/gap-mini-solve-as-opus.md` (row 1293); `library/gap-mini-solve-ao-opus.md` L75-151 (row 1278). Sources fetched
by URL into a scratch folder outside the repository: Sussman and Alpoge's CA-III at 31a47c543775
(`theorem_0_complete_account_raw_III.tex`) and `YM4/EM/YM4_EM.tex` at c7fef8b21b58 (with Claude and Codex as authors
of their text; after Balaban).

What the record fixes (pointers only):
1. Modulo the ultraviolet carry, the gap clause reads one lattice input at one physical size: (N-phys) (row 1161), or
   (SL)/(RR) at one coupling (row 1258), or a seed at the base datum of the pin route (rows 1233, 1256). Every engine
   on file is blind; the one selective proved fact (asymptotic freedom at small coupling) has no carrier through the
   band (`parts/gap.md`, "Hardest open obligation"; row 998 6b).
2. Row 1218's sources: A's ascent is conditional on its own seed; B's Corollary 166 is a non-selective weak-coupling
   statement about straight-path variables (perimeter self-energy randomises them for U(1) as well); Zeng's routes are
   conditional.
3. The one-cutoff carry (rows 1255-1293, mostly this worker's thread) is reduced to named inputs. Open at this pin
   (row 1293 6.3, check 1288): (H-an)/(H-an') and (H-flip) against Balaban's CMP 116; (S-chart) and kappa_0 > 6 in the
   account; the cut part of (FC-1) ((E0)-(E6), (TH)); (H2)-(H3) (row 1278; row 1284 item B left the core-path clause
   OPEN); `9.1:prop-blind-site-expansions` (Proof outstanding in the account, CA-III L16558-16560); (V9) (reading N2
   FAILS in check 1288); (DET)'s remaining normalisation (rows 993-994); the account's premises.
4. Balaban's CMP 116 is not in the paper folder and Project Euclid answers with a bot check (rows 1264, 1060-era notes);
   so every input that must be read against CMP 116 is blocked on this machine, not refuted.
5. Row 1284 (another worker, running) attacks the parity envelope (PE) without the localised expansion (log-concavity
   and Helffer-Sjostrand on the global step integral, its Step 3). Rule 0a: I do not attack (PE), (H-an), (H-flip).

Record-keeping observation for the lead (evidence only): `library/gap-mini-solve-aq-opus.md` labels its Step 0-3 times
15:55Z, 16:10Z, 16:55Z and 17:20Z "by date -u", but the relay commit 7e38abf41 that contains Step 3 is dated
2026-11-20 15:39Z; those labels cannot be date -u readings.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T16:01Z by date -u)

**The seed.** The problem, modulo the carry, is a lattice statement at order-one coupling with no small parameter, on
a box of several hundred correlation lengths. Every proved gap result read by the lane (row 735) verifies its criterion
at the correlation length by one of four means: a small number at that scale, a second small number after an exact
change of variables, exact closure, or a correlation-inequality dichotomy. None of the four is available for 4D SU(2)
at the band, and the candidate fifth means I could name (Step 0, Repo search) are all on file with a first failing step.
Row 998 9.5 rules a further screen by this model family a waste. Verdict (ARGUED): no route to the seed off the record;
I do not attack it. This is said plainly so that nothing below is counted as progress on the crux.

**What I do instead.** Only closures count, so I take carry inputs that (a) are unowned at this pin, (b) can be decided
from sources on hand (EM, CA-III, Balaban's papers in the owner's folder), and (c) are not (PE)'s inputs (row 1284).
Plan, one item per step, each appended before the next:
- Step 2: (S-chart), the chart scale of the account's step (row 1293 6.1: "a reading for the account").
- Step 3: the core clause of Lemma H2' (row 1278 2.3; row 1284 item B left it OPEN): whether covariance of a
  psi-formed member needs connectedness of the data domain at all, read against EM's own covariance argument.
- Step 4: chosen after Step 3 from (V9), (DET)'s normalisation, kappa_0, by what the sources decide.
(Plan as executed: Step 3 became Lemma SYM on (H-flip), found while reading row 1293's Theorem PE; the H2' clause
moved to Step 4; Step 5 records the carry's state; Step 6 attempts the cut half of (FC-1).)
Moves: the one-cutoff carry on the pin route (rows 1233, 1256-1293). Success removes named inputs from row 1293's list;
failure names the first step that does not close. Neither changes the seed.

## Step 2. (S-chart), the chart scale of the account's step (written 2026-11-20T16:06Z by date -u)

**What row 1293 needs.** Theorem PE's structure hypothesis (S)(c) and Corollary FC-s read the step as one analytic
family in the chart scale h: the frame-theta step equals the h-family at h = theta^(-1/2), with a Gaussian reference
in the free variables that does not depend on theta (row 1293 3.1-3.2, 4.1 last paragraph, 5.3). Row 1293 READ this
in Balaban (A'_k = g_k A_k) and left it "a reading for the account".

**2.1 READ (sources fetched at the pins named in Step 0).**
- CA-I L149155-149171 (the account's step, transcribing CMP 119 p. 267): the fluctuation field is defined by
  A'_k = (1/i) log V'_k, "and A'_k = g_k A_k", and the cut is read as |g_k A_k| < a_# eps_k. So in the account's own
  step the integration variable A_k enters the configuration only through g_k A_k.
- EM L502-505: "The frame fixes the lattice partitions, Gaussian references, real fluctuation coordinates and tests.
  The variable x_k does not change those choices."
- EM L333-345: every frame threshold is a function of the frame entry of the form y^(-1/2) times a power of log y
  (alpha_iota(y) = C_iota y^(-1/2) (log y)^q, delta(y) = A_1 y^(-1/2) (log y)^(p_0)), so theta plays the role of g^(-2).
- EM L563-578 (em:eq-frozen-gaussian-rewrite): the Wilson weight enters the Gaussian only through tau_k = x_k/theta_k,
  and "the scaled Gaussian is normalized" at tau_k = 1.

**2.2 Lemma SC (the integrand in the frame's scaled chart; PROVED, elementary).** Let Phi(W, A) be any frame-free
parametrisation of the fibre (the set of V with M(V) = W) by physical fluctuation coordinates A, with Phi(W, 0) the
background. Write the frame-theta step integrand in A:
    exp[-x A(U_k(Phi(W,A))) - theta Gs(W, Phi(W,A)) + S_f(U_k(Phi(W,A))) - S_f(U_(k+1)(W))] J(W, A) chi(|A| <= delta(theta))
(chi a product of tests over the tested bonds or cubes). Put h = theta^(-1/2), B = A/h, tau = x/theta. Then, as a
function of B, the integrand equals
    exp[-tau h^(-2) A(U_k(Phi(W, hB))) - h^(-2) Gs(W, Phi(W, hB)) + S_f(U_k(Phi(W, hB))) - S_f(U_(k+1)(W))]
    J(W, hB) chi(|B| <= rho),        rho := theta^(1/2) delta(theta) = A_1 (log theta)^(p_0),
and dA = h^N dB (N the fibre dimension), a field-independent scalar. If the background is critical along the fibre and
meets the gauge condition ((S)(d) of row 1293), the second-order parts of the first two terms are -(tau/2) <B, H_A B>
and -(1/2) <B, H_G B>, where H_A and H_G are the Hessians at A = 0 of A(U_k(Phi(W, .))) and Gs(W, Phi(W, .)); they do
not depend on theta.
*Proof.* Substitution: x = tau theta = tau h^(-2), theta = h^(-2), and |hB| <= delta(theta) iff |B| <= rho. A quadratic
form q in A gives h^(-2) q(hB) = q(B). QED

So, whatever coordinates the account calls "real fluctuation coordinates", the frame-theta step integral is exactly
(up to the scalar h^N) the h-family of row 1293 3.1 at h = theta^(-1/2), with the theta-free reference (H_A, H_G), the
weight entering only through tau, and the cut entering only through rho (an even test in B). This is (S-chart) for the
integrand, with no reading. By 2.1 the account's coordinates are moreover Balaban's, B = A'_k/g_k with
g_k = theta_k^(-1/2) at tau = 1 (CA-I L149163-149171 with EM L502-505). That the account's g_k in the two-weight
setting is the frame's theta_k^(-1/2), and not x_k^(-1/2), is what EM L504-505 says (the weight does not change the
coordinates); so it is READ, not inferred.

**2.3 What is left of (S-chart).** Only the localisation: that the account's prescribed localisation of the frame-theta
step, written in B, is the member at h = theta^(-1/2) of one localisation family F(h) that is holomorphic in h. That is
(H-an) of row 1293 (row 1284 attacks (PE) by the global integral instead, Step 0 item 5), not a separate input. The
substitution of 2.2 is linear in the free variables, so a localisation defined from the Gaussian measure and the
integrand as functions on the fibre is carried along by it; this last sentence is ARGUED, not read in CMP 116.

**Verdict.** (S-chart) leaves row 1293's input list: PROVED for the integrand (Lemma SC) and READ for the account's
coordinates (2.1). Its localisation part is (H-an). Rows that use (S-chart) (row 1293 5.3, Corollary FC-s) now rest on
(S), (H-flip) and (H-an') only.

## Step 3. (H-flip) leaves the input list: symmetrise the localisation (written 2026-11-20T16:09Z by date -u)

Rule 0a: grep of `FINISH.md`, `library/open-core.md` and `library/*.md` for "symmetris", "symmetriz", "even part",
"F(h) + F(-h)", "(H-flip)": "(H-flip)" occurs in FINISH.md once (row 1293's RESULT) and in the files of rows 1280,
1284 (as P4) and 1293; "even part" occurs in row 1293 4.3, where it is formed WITH (H-flip). The ten library files that
mention symmetrisation and localisation together treat propagators, averages and trace norms (a2-curved, carrier-adopt,
conditional-normalization, fc-r2, gap-conv-in-law-check-opus; b98p5*, b99, cr-prem only by spelling). No match for
symmetrising a localisation in the fluctuation scale. `library/open-core.md` has no (H-flip) entry.

**3.0 Why this matters.** (H-flip) is one of the three inputs of Theorem PE (row 1293) that must be read against
Balaban's CMP 116, which is not on this machine. Row 1293 4.2 ARGUED it from the account's transcription. Here it is
removed: every consumer reads only physical totals, and the total is exactly even in h, so the even part of ANY
localisation family can be used.

**3.1 Two facts on file.**
- (T) Consumers read totals only. The coefficient readout b_j is linear and "unchanged ... by changing coherent
  localizations of the same physical total" (EM L1202-1204, proof L1218-1219: "two coherent localizations of the same
  total give the same kernel"). The comparison norm |||T|||_j of row 1267 3.1 is the infimum of ||H||_(j,kappa;a_*)
  over regular pointed families H whose total is T + const. Regular families form complex linear spaces (EM L215-218),
  and covariance, companions and the readout are linear (EM L251-273). Row 1293 uses Theorem PE only through f_(k+1)
  (5.1, 5.2) and through |||.||| (5.3).
- (E) The total is even in h. With (S)(a)-(c) of row 1293 (centred Gaussian, cut Omega, integrand P with
  P(-h, -B; W) = P(h, B; W) by its Lemma 3.3; for the account's integrand this is Lemma SC of Step 2), put
  I_Omega(h; W) := int mu_W(dB) 1_Omega(B) exp P(h, B; W). The change of variables B -> -B (measure preserving for mu_W)
  gives, for real h, I_Omega(-h; W) = I_(-Omega)(h; W). In particular I_Omega(-h) = I_Omega(h) when Omega = -Omega.

**3.2 Lemma SYM (PROVED, elementary).** Let F(h), |h| < r, be any family of regular pointed families on the absolute
core, holomorphic in h, real for real h, with ||F(h)|| <= K_a, meeting the hypotheses of em:prop-companion-coefficient
uniformly in h, and with total log I_Omega(h; W) - (scalar) - N - G at every real h and real datum W (that is, (H-an)
for some localisation, not necessarily the prescribed one). Put F_s(h) := (F(h) + F(-h))/2. Then:
(a) F_s is holomorphic and even in h, real for real h, ||F_s(h)|| <= K_a, and meets the same hypotheses (linearity).
(b) If Omega = -Omega, the total of F_s(h) equals the total of F(h) for every |h| < r.
(c) In general, total F_s(h) = total F(h) - D(h)/2, where D(h) := log I_Omega(h) - log I_(-Omega)(h) is the one-scale
    cut comparison between Omega and -Omega at the same h.
*Proof.* (a) Each property is linear or convex in the family; the disc is symmetric under h -> -h. (b), (c): for real
h the total of F(-h) is log I_Omega(-h) - c = log I_(-Omega)(h) - c by (E), with the same h-free c (the separated
scalar, N and G: N and G are h-free families by row 1293 3.1, and the h-family is written with the normalized
Gaussian mu_W in B, so no power of h enters it; the h^N of Lemma SC relates only the value at h = g to the actual
integral). The identity total F_s(h) = total F(h) - D(h)/2 with D(h) := total F(h) - total F(-h) is algebra; the content
is that for real h, D(h) = log I_Omega(h) - log I_(-Omega)(h). If Omega = -Omega, D vanishes for real h, hence on the
disc (identity theorem for the holomorphic function D of one variable). The branch of each logarithm is fixed at
h = 0, where P(0, B) = 0 and I_Omega(0) > 0. QED

**3.3 Corollary PE' (Theorem PE without (H-flip); PROVED GIVEN (S), (H-an) for some localisation family, (H-tail)).**
With F as in 3.2 and Omega = -Omega (Balaban's cut, row 1293 4.1): the coefficient f_(k+1) = b(F_s(g)) by (T), and by
the even Cauchy estimate (row 1293 Lemma 3.4) applied to F_s,
    |||T(F^u_(k+1)) - T(F_s(0))||| <= ||F_s(g) - F_s(0)|| <= K_a (g/r)^2/(1 - (g/r)^2),
with T(F_s(0)) the h = 0 total, a Gaussian tail by (H-tail). For a cut that is even only up to a thin shell (row 1293
4.3, Lemma AS), the same bound holds with the extra term |||D(g)|||/2 + |||D(0)|||/2, and D is a cut comparison at one
scale: exactly the input that row 1293 4.3 calls eta (Lemma SW with (E+) of row 1280), now needed WITHOUT (H-flip).
So Theorem PE and its consequences 5.1-5.2 of row 1293 hold with (H-flip) deleted from their inputs; Corollary FC-s
(5.3) holds with (H-flip) deleted, applying 3.2 to the two-variable family F(h, tau) (the symmetrisation is in h only;
tau is untouched).

**3.4 What (H-an) now asks.** By (T), (H-an) and (H-an') need not be statements about the supplier's prescribed
localisation: ANY holomorphic family of regular localisations of the h-family's totals with the stated bounds will do,
provided at h = g its total is the actual step total on every compatible torus (then f_(k+1) = b(F(g)) by (T)). So
(H-an) is a statement that can be met by a localisation we build ourselves (for example from the ultralocal cluster
expansion already in `library/ultralocal_cluster_expansion.md`, after a decoupling of the Gaussian), with no reading of
CMP 116. It is still OPEN here. Row 1284 attacks the coefficient part of (PE) by a global route; the family part (for
Corollary FC-s) is not covered by that route.

**Verdict.** (H-flip) is removed from the carry's input list (Lemma SYM, PROVED); for an exactly even cut nothing
replaces it, and for a shell-even cut it is replaced by the one-scale cut comparison D, which row 1293 4.3 already
needed. (H-an)/(H-an') stay OPEN but are now open as existence statements for some localisation, not as readings of
CMP 116.

## Step 4. The core clause of Lemma H2' (cross-admission): what it really needs (written 2026-11-20T16:15Z by date -u)

**4.0 The clause.** Row 1278 2.3 argued cross-admission (H2) by continuing a psi-formed member's covariance identity
P_(rz)(G; rW) = P_z(G; W) from its creation class to the whole absolute core "by the identity theorem", and asked for
connectedness of the core (not found stated). Row 1284 2.1 weakened this to real paths from each datum to the creation
class and left the path on large tori OPEN.

**4.1 How EM proves covariance (READ).** EM does not continue covariance over the data. At each real datum W of "the
admitted real common covariance class" it changes variables B -> O_(r,W) B (EM L742-748; the orthogonal map with
V'(rW, O_(r,W) B) = r V'(W, B), EM L643-647), which transports the cut, the response, the measure factors and the point.
This is pointwise in W. What it needs from the INHERITED members is stated at EM L647-653: "There is an open real
fluctuation ball on which all inherited backgrounds have their required covariance ... The earlier backgrounds used by
the actual step also have to lie in their own covariance classes throughout the retained real cut." The identity
theorem is used only for PARAMETERS ("On a connected complex parameter domain a covariance identity of holomorphic
terms continues from an open full-dimensional real slice", EM L748-751), and parameter domains are products of discs.

**4.2 Proposition H2-cov (the covariance clause of cross-admission; PROVED GIVEN (M) below).** Let (M) be the
statement: the supplier's requirement of EM L652-653 holds with a fixed relative margin mu_m > 0, that is, for every
frame and step, the earlier backgrounds produced by the real cut enlarged by the factor 1 + mu_m still lie in the
inherited members' covariance classes. Let phi, psi be two frames at one step k with |theta^phi_j - theta^psi_j| <=
Z_j for j <= k (the drift of row 1293 5.1 or the account's), and let the floor be so high that
delta(theta - Z)/delta(theta) <= 1 + mu_m for all theta above it. Then every psi-formed member read by the phi-step has
its covariance at every background the phi-step uses, so EM's change of variables gives the covariance of the phi-step's
output with psi-formed inputs, with no connectedness of any data domain.
*Proof.* delta(y) = A_1 y^(-1/2) (log y)^(p_0) is decreasing for y > e^(2 p_0) (EM L333-345), so the phi-cut is at most
the psi-cut times delta(theta^psi - Z)/delta(theta^psi) <= 1 + mu_m, at every level read; the created covariance radii
c_e eps(theta) have the same form (EM L653-656), so the same ratio bounds them. By (M) applied to the psi-frame, the
backgrounds of the enlarged psi-cut, which contain those of the phi-cut, lie in the psi-members' covariance classes.
Then EM L742-748 applies verbatim. QED
With Z = C theta^(1/2) (log theta)^(p_0) (the account's drift) the ratio is 1 + O(theta^(-1/2) polylog), so any fixed
mu_m > 0 is enough above a floor. (M) is a margin statement of the same kind as EM's other margins (its target radii
enlarged by 1 + beta_s, EM L507-509; "c_e is fixed by the domain margin", EM L656); it is ARGUED as a reading, not
found stated with that wording.

**4.3 Remark (the continuation route is the wrong tool; ARGUED, the topological input recalled, not read).** For SU(2),
Luscher's charge (CMP 85 (1982), recalled) is an integer, constant on connected sets of lattice fields whose plaquettes
are all within a small fixed distance of 1. A smooth charge-one connection of scale R, transported onto a lattice of
spacing 1, has plaquette defects of order R^(-2); on tori of side large against R it lies in any core that bounds
plaquette defects by a fixed multiple of R^(-2), while the trivial field has charge zero. So "the core is connected"
fails on large tori whenever the core's defect bound is below Luscher's constant, and a continuation over the data could
at most work sector by sector, which needs connectedness of curvature sublevel sets inside a sector (OPEN, and not
needed after 4.2).

**4.4 Effect.** Lemma H2' of row 1278 loses its geometric clause: (H2) is PROVED GIVEN the readings (R3)-(R5) of row
1278, row 1267's READ list of where the frame enters, and the margin reading (M). Row 1284's open path clause (its 2.1)
is not needed.

**4.5 A note on (H-an), from the same reading.** EM states the principle that row 1293 3.7 needed: "The fixed-domain
step and its normally convergent expansion give joint holomorphy with the new parameters" (EM L882-885). With Lemma SC
(Step 2) the chart scale h is a parameter that enters the integrand holomorphically, and on the cut the per-piece size
of the non-Gaussian part is at most C |h| rho^3, while the field size in physical units is |h| rho, so EM's smallness
condition s(1 + D_*) <= eps_step (EM L863-868) holds on |h| <= c_* rho^(-3) above a floor (s = |h| rho/a_(*,0) <=
c_* rho^(-2)/a_(*,0)). So (H-an) and (H-an') are the one-step theorem on the h-extended parameter domain: a supplier
premise of exactly EM's kind (EM inputs 1-3 on "the requested field, coupling and remainder parameter domains"), with
the h-disc added. ARGUED, as in row 1293 3.7; no upgrade to PROVED is claimed.

## Step 5. The one-cutoff carry after Steps 2-4 (superseded in part by Steps 6-7; written 2026-11-20T16:18Z by date -u)

Chain (unchanged): row 1256 (pins) -> row 1260 (Lemma GR) -> row 1267 (Proposition FC-chain) -> row 1268 (Theorem
FCT') -> row 1280 (Theorem U) -> row 1293 (Theorem PE, Corollary FC-s) -> this row. Status of each input of row 1293 6.3:

| Input | Before this row | After this row |
|---|---|---|
| (S-chart) | "a reading for the account" | leaves the list: Lemma SC (PROVED, integrand) + CA-I L149163-149171 and EM L502-505 (READ); its localisation part is (H-an) (Step 2) |
| (H-flip) | ARGUED from the account's transcription; CMP 116 not on this machine | leaves the list: Lemma SYM (PROVED); for a shell-even cut, replaced by the one-scale cut comparison D that row 1293 4.3 already needed (Step 3) |
| (H-an), (H-an') | ARGUED (row 1293 3.7) | OPEN, unchanged in label; now a supplier premise of EM's own kind on the h-extended parameter domain (EM L882-885 and L863-868, Step 4.5), and it may be met by ANY regular localisation family of the totals (Step 3.4) |
| (S) | READ for Balaban's step (row 1293 4.1) | READ; for the account's integrand also by Lemma SC (Step 2) |
| (H-tail) | READ (row 1293 4.5, EM L682-683) | unchanged; note that EM's formation bound carries the term K delta(theta) beside the tail, so reading the h = 0 value as the tail alone is a reading of where that term comes from |
| kappa_0 > 6 | "the account's value is not read" | OPEN: EM states kappa_0 > 4 as a hypothesis on the creation norms of inherited remainders (EM L383-385, L1351-1366) and leaves those norms to the supplier (EM L119-121, L166-169); not decidable from EM |
| (H2) cross-admission | ARGUED, clause "connectedness of the core" OPEN (rows 1278, 1284) | PROVED GIVEN row 1278's readings (R3)-(R5), row 1267's READ list and the margin reading (M) (Proposition H2-cov, Step 4); no connectedness needed |
| (H3) | PROVED GIVEN (R1)-(R5) (row 1278) | unchanged |
| cut part of (FC-1): (E0)-(E6), (TH) | (E1)-(E3) READ for the account's large-field stages only; (TH) READ (row 1278) | unchanged. The account prints its expansion machine with one-term bounds and holomorphy for the large-field stages (CA-I 4.22, L80618-80700; 4.24, L108354-108610); for the regular step it cites CMP 116 (CA-I L58700-58760). Applying the printed machine to the regular step is possible in principle (the regular step has no arrested components) but was not checked here |
| 9.1:prop-blind-site-expansions | "Proof outstanding" in the account (CA-III L16558-16560) | unchanged; its route needs CMP 116 Section 2 (CA-III L16663-16700) |
| (V9) | OPEN (check 1288: reading N2 FAILS) | unchanged, not worked |
| (DET)'s normalisation | exact torus independence of the whole E_0 OPEN (rows 993-994) | unchanged, not worked |
| the account's premises; the infrared seed | OPEN | unchanged; the seed was not attacked |

So the smooth half of the carry (Theorem PE, its drift consequences 5.1-5.2 and Corollary FC-s) now rests on (S) and
(H-tail) (read), (H-an)/(H-an') (a supplier premise of EM's kind) and, for 5.1-5.2, kappa_0 > 6 (a supplier premise).
No input of the smooth half needs a reading of CMP 116 any more. The cut half still does, through (E0)-(E6).

## Step 6. (H-an), (H-an') and (H-tail) from the account's own cluster-expansion apparatus (written 2026-11-20T16:23Z by date -u)

**6.0 Aim.** Row 1293 3.7 ARGUED (H-an) as "a statement about the supplier". Step 4.5 left it a supplier premise of
EM's kind. Here it is derived from what the account already uses for its regular step, so the smooth half of the carry
needs no new supplier input. The key fact is the account's own parameter lemma. The idea (estimates that use only
per-piece smallness give holomorphy in h) is row 1293's 3.7; what is added is the account's statement of that
principle, a re-split integrand on which it applies, the element bounds, and the use of (T).

**6.1 READ (CA-I at 31a47c543775, with Claude and Codex as authors of its text; after Balaban).**
- CA-I L80178-80239, Lemma 4.22:lem-cluster-manifold ("The cluster expansion with a complex-manifold parameter";
  status PROVED in `library/sa-index/ca-full/index.tsv` row 300). It assumes "the lemma on the cluster expansion with
  parameters" and "the proposition on the parameter-free majorants of the cluster expansion, clauses (ii) and (iii)".
  If each element v_e is continuous on its range, holomorphic in the polydisc and manifold coordinates, with
  |v_e| <= nu(e) there, and "all the other objects entering that lemma do not depend on the parameter: the pieces of
  the expansion ..., the large-field bonds, the decoupled cubes, the Gaussian measure with its decoupling parameters s,
  the products chi^(j) chi'^(j) of cut-off functions ..., the partitions and the contours", then each term of the
  expansion is continuous, holomorphic in those coordinates, and the majorant clauses hold with the supremum over the
  parameter inside the norm. Its proof: the identities hold at each parameter value; the majorant is built from the
  nu(e) alone; each term is a finite sum of products of integrals over parameter-free contours; Weierstrass.
  The two assumed statements are cited there by description; I did not find them under those names in CA-I, II or III
  at the pin (grep for "parameter-free majorant", "cluster expansion with param": hits only inside this lemma).
- CA-I L4073-4196 (the regular small-field step, Theorem 4.3:thm-small-field-step): the bounds of CMP 116 and CMP 109
  are "quoted, not" re-proved; the localized part obeys CMP 116 (2.41) on Balaban's analyticity domain
  U^c_l(X, alpha_0, alpha_1) (L4085-4089); the expansion statements are read with "the small parameter epsilon of these
  statements replaced by C_P epsilon-hat" (L8778-8781).
- CA-I L58700-58760: the ingredients of a localized term of the regular step are the decoupling parameters s(Delta),
  the small solutions of CMP 116 (1.3)-(1.4), the minimisers, block-local algebra, fixed profiles, "the factors
  chi^(k), the signs of [CMP 116 (2.3)], and d mu_0", and "the Mayer, polymer and cluster sums".

**6.2 Lemma PH (parameter holomorphy of an expansion; PROVED, elementary; the account's Lemma 4.22:lem-cluster-manifold
in the form used here).** Let a localization be produced by an expansion each of whose terms is a finite sum of products
of integrals, against a fixed measure and over fixed contours, of finitely many elements v_e(zeta, .), and suppose the
series of terms is dominated, uniformly in zeta, by a convergent majorant series that depends on the numbers nu(e)
only. If each v_e is continuous, holomorphic in zeta in a polydisc Z, and |v_e| <= nu(e) on its domain for all zeta in
Z, then every localized term is holomorphic in zeta on Z and obeys the majorant bound with sup over Z inside the norm.
*Proof.* A finite product of integrals over a fixed compact contour of continuous functions holomorphic in zeta is
holomorphic in zeta (differentiation under the integral, dominated convergence). The series converges uniformly on Z
by the zeta-free majorant. A uniform limit of holomorphic functions is holomorphic (Weierstrass). QED

**6.3 The re-split integrand.** Fix a real tau_0 (the step's own x/theta for Theorem PE; one of the two compared
values for Corollary FC-s). In the frame's scaled chart (Lemma SC, Step 2) keep the reference Gaussian at tau_0,
mu_W^(tau_0) with precision tau_0 H_A + H_G (theta-free, h-free; it is the actual step's Gaussian at that weight, EM
L563-578), and the cut |B| <= rho (h-free, tau-free). Put every remaining factor into elements, localized by the account's localization of the action and of the inherited list (the same pieces as in
the actual step):
 (i)   -tau h^(-2) [A_e(hB) - A_e^(2)(hB)]   (non-quadratic part of an action piece A_e of the physical field hB);
 (ii)  -(tau - tau_0) A_e^(2)(B)             (the weight shift, h-free since h^(-2) A_e^(2)(hB) = A_e^(2)(B));
 (iii) -h^(-2) [Gs_e(hB) - Gs_e^(2)(hB)]     (non-quadratic part of the gauge weight);
 (iv)  log J_e(hB) - log J_e(0)              (fibre density and pivot pieces);
 (v)   S_(f,e)(U_k(Phi(W, hB))) - S_(f,e)(U_(k+1)(W))   (inherited list).
At h = g and tau = x/theta this is the actual integrand (EM em:eq-actual-step) written with the tau_0 Gaussian, so the
expansion of 6.1 applied to it is a localization of the actual total; it is not the prescribed localization, but by
(T) of Step 3 any regular localization of the same total serves every consumer.

**6.4 Lemma EB (element bounds at complex scale and weight; PROVED given the analyticity domain of 6.1).** Suppose each
piece of the integrand is holomorphic in the physical field phi on the polydisc |phi| <= a (a fixed, from Balaban's
analyticity domain) with |A_e|, |A_e^(2)|, |Gs_e|, |log J_e|, |S_(f,e)| <= M e^(-kappa d(e)) there, and let the
expansion read B on a complex collar polydisc |B| <= c_B rho. Let |h| <= c_* rho^(-3) and |tau - tau_0| <= c_tau rho^(-2),
and let theta be above a floor such that c_B c_* rho^(-2) <= a/2. Then on that domain
    |v_e| <= C_M (c_* + c_tau) e^(-kappa d(e)),   C_M := 8 M (c_B/a)^3 + M c_B^2/a^2.
*Proof.* |hB| <= c_B c_* rho^(-2) <= a/2. For (i) and (iii) the Cauchy remainder of order three of a function bounded
by M e^(-kappa d) on |phi| <= a gives |A_e(phi) - A_e^(2)(phi)| <= 2 M e^(-kappa d) (|phi|/a)^3 for |phi| <= a/2, so
|h^(-2) [...]| <= 2 M e^(-kappa d) |h| (c_B rho/a)^3 <= 2 M (c_B/a)^3 c_* e^(-kappa d); |tau| <= 2. For (ii),
|A_e^(2)(B)| = |h|^(-2) |A_e^(2)(hB)| is a quadratic form bounded by M e^(-kappa d) (|B|/a)^2 (Cauchy) on the collar
polydisc, so |(tau - tau_0) A_e^(2)(B)| <= c_tau rho^(-2) M (c_B rho/a)^2 e^(-kappa d). For (iv), (v) the first-order
Cauchy bound gives at most 2 M e^(-kappa d) |hB|/a <= M c_B c_* rho^(-2) a^(-1) e^(-kappa d), which is smaller. QED
(The linear term of (v) is not zero, but it carries |hB|; the linear terms of (i), (iii) vanish because the background
is critical and meets the gauge condition, (S)(d) of row 1293.)

**6.5 Proposition HAN ((H-an') and (H-tail) with no new supplier input; PROVED GIVEN (CE) below, (S), Lemma SC).**
(CE): the account's regular-step expansion (6.1) has the form of Lemma PH, with the reference Gaussian, its decoupling,
the cut, the partitions and the contours fixed, and it converges with its majorant bounds K when every element obeys
|v_e| <= eps_0 e^(-kappa d(e)) for a fixed eps_0 (the "small parameter epsilon of these statements", CA-I L8778-8781).
Choose c_*, c_tau with C_M (c_* + c_tau) <= eps_0. Then, on |h| < r := c_* rho^(-3), |tau - tau_0| < sigma := c_tau rho^(-2):
(a) the localization F(h, tau) of the re-split integrand minus N and G_tau exists, is holomorphic in (h, tau), real for
    real (h, tau), with ||F(h, tau) - F(0, tau)|| <= 2K and ||F|| bounded by K plus the norms of N and G_tau;
(b) (H-tail) in total form: |||T(F(0, tau))||| <= K_t e^(-c rho^2) for each such tau;
(c) its symmetrisation in h (Lemma SYM, Step 3) is even in h with the same bounds and, for an even cut, the same total.
*Proof.* (a) Lemma EB and the choice of c_*, c_tau put every element under the threshold of (CE) for all (h, tau) in the
bidisc, with nothing else depending on (h, tau) (6.3). Lemma PH with the two polydisc parameters h, tau gives
holomorphy and the majorant bound K uniformly. (b) At h = 0 keep instead the tau-Gaussian as the measure (no parameter
holomorphy is needed at one tau): the elements of (i), (iii)-(v) vanish, and the expansion of log mu_tau(Omega) has
only the complement terms of the decomposition chi = chi_(Y_0) sum_P (-1)^|P| chi^c_P with P non-empty, each carrying
e^(-(1/2) gamma_2 T^2 |P|) by the account's one-term bound (CA-I L108584-108600, the same mechanism); its total is
log mu_tau(Omega) = T(F(0, tau)) + const, so this localization is a competitor in |||.|||. (c) Step 3. QED

*Robustness.* If (CE) holds only with a threshold eps_0(theta) that shrinks with the floor, but not faster than
(log theta)^(-C), take c_* and c_tau of that size: r and sigma lose a factor (log theta)^(-C), and every conclusion of
6.6 holds with further polylog factors. If the threshold had to shrink like a power of theta, 6.6 would fail as stated;
a checker should look for that first.

**6.6 Consequences (PROVED GIVEN (CE), (S), Lemma SC).**
- Theorem PE of row 1293 (via Corollary PE' of Step 3) holds with r = c_* rho^(-3): f_(k+1) - b(F(0)) is at most
  C a^(-2) K (g/r)^2/(1 - (g/r)^2) = O(theta^(-1) rho^6); with (b) the h = 0 value is a tail. No input of Theorem PE is
  open beyond (S), (H-tail)'s reading (now (b)) and (CE).
- Corollary FC-s of row 1293 holds with sigma = c_tau rho^(-2) in place of sigma_*, centred at tau_0 := tau (above a
  floor |tau - tau'| <= 2|zeta|/theta <= sigma/2, since |zeta| <= C theta^(1/2) polylog): with |zeta| = |theta - theta'|,
      |||T(h, tau) - T(h', tau')||| <= 2 K_t e^(-c rho^2)
          + K [ rho^6 |zeta|/(c_*^2 theta theta') + 2 rho^8 |zeta|/(c_*^2 c_tau theta^2) + 2 rho^12/(c_*^4 theta^2) ](1 + o(1)),
  using |h^2 - h'^2| = |zeta|/(theta theta'), |tau - tau'| <= 2|zeta|/theta (x/theta' <= 2), the even Cauchy estimate
  in h and the Cauchy estimate in tau on the disc of radius sigma. With the account's drift |zeta| <= C theta^(1/2)
  (log theta)^(p_0) this is O(theta^(-3/2) polylog), summable along a pin run (theta_k growing linearly). The smaller
  tau-disc costs one factor rho^2, a polylog; nothing else changes.
- So the smooth half of the one-cutoff carry (Theorem PE, 5.1-5.2 given kappa_0 > 6, Corollary FC-s) rests on the
  account's own regular-step apparatus (CE), the readings (S), Lemma SC, and for 5.1-5.2 the supplier premise kappa_0 > 6.
  (H-flip), (S-chart), (H-an), (H-an') and (H-tail) are no longer separate inputs.

**6.7 What a checker should redo first.** (1) That the account's regular-step expansion is of the form of Lemma PH with a
fixed Gaussian (at tau_0), decoupling, cut, partitions and contours, when the weight shift (ii) is moved into
elements (the account keeps the tau-scaled Gaussian at every tau instead, EM L563-578); in particular that the expansion tolerates elements with
nu(e) of order eps_0 and not only of order the step's own small parameter. (2) Lemma EB's Cauchy constants, and that the
expansion reads B only on a collar polydisc of radius c_B rho (the account's 6.6 b'_j, CA-I L108555-108567). (3) 6.5(b):
that the P = empty terms at h = 0 with no elements are exactly the uncut Gaussian's terms (no element, so D is empty and
Y_0 is empty). (4) The FC-s arithmetic of 6.6.

## Step 7. kappa_0 > 6 leaves the list: (U) needs only (PE) and the account's own drift (written 2026-11-20T16:26Z by date -u)

**7.1 Where kappa_0 > 6 entered.** Row 1293 5.1 bounds the drift of a run from its scaffold by a polylog, given (PE),
the drift recursion and kappa_0 > 6 (so that the marked terms |q_(k+1)| <= C theta_k^(-(kappa_0 - 4)/2) (log theta_k)^(-2q),
EM L1366, are summable along a run). Row 1293 5.2 then closes (U) with that polylog drift, following row 1280 4.5 (b).
EM's sharper marked envelope (EM L1373-1375, the factor s_k = delta(theta_k)/abar_(k,0) of order (log theta_k)^(p_0 - q),
EM L345-353) gains only a logarithm, so it would lower the requirement to kappa_0 >= 6 at most.

**7.2 Corollary U' ((U) given (PE) alone; PROVED, arithmetic, from row 1280's Lemma W and Proposition W2).** Let D(y) be
the account's own drift bound, D(y) = C_D y^(1/2) (log y)^(p_0) (row 1260 2.1, CA-III III:69015-69017), and let (PE) give
the one-frame coefficient bound e_PE(y) = C y^(-1) (log y)^(c) + C exp(-c' (log y)^(2 p_0)) for some fixed c (Step 6,
or row 1293 with c = 6 p_0). Then the window total of row 1280 is finite, uniform in n, and tends to 0 as X grows:
    sum over jump points Y_b >= X/2 of (2 D(2 Y_b)/c_0 + 1) * 2 e_PE(Y_b/2) < infinity.
*Proof.* Lemma W of row 1280 is stated for this D: its condition D(2 Y_b) < min(Y_b - Y_(b-1), Y_(b+1) - Y_b) holds for X
large since Y_(b+1) - Y_b grows faster than any power of Y_b (row 1280 3.1, last paragraph). By Lemma W (b) the
windows at Y_b have at most 2 D(2 Y_b)/c_0 + 1 levels, and at each the defect is at most 2 e_PE(Y_b/2) (row 1280 4.5
(b)). With Y_b = exp(L^(b/r)) the b-th summand is at most C'' exp(-L^(b/r)/2) L^((p_0 + c) b/r) plus
C'' exp(L^(b/r)/2 - c' L^(2 p_0 b/r)) L^(p_0 b/r); both sum over b, the second because 2 p_0 > 1 (EM's standing
choice for the cut tail to beat every power of theta, EM L873-876), so that L^(2 p_0 b/r) dominates L^(b/r). This is Proposition W2's criterion (row 1280 3.2) with
kappa(y) = y^(-1) polylog, which only needs sum_b D(2 Y_b) kappa(Y_b/2) finite: with D of order y^(1/2) polylog the
summand is of order Y_b^(-1/2) polylog. QED

**7.3 Effect.** (U) leaves the carry's input list given (PE), with no improved drift: row 1293 5.1 (polylog drift) is
an improvement that no consumer needs. Corollary FC-s already works with the account's drift (row 1293 5.3, and 6.6
here). So kappa_0 > 6 leaves the input list. EM's own standing hypothesis kappa_0 > 4 (EM L383) remains a premise of
EM's full chain, as before.

(Rows (H-an), (H-an'), (H-tail) and kappa_0 > 6 of the Step 5 table are superseded by Steps 6 and 7.)
