lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:42Z

# gap-mini-solve-at-opus: the SU(2) mass gap, one more attack (FINISH row 1294)

Started 2026-11-20T15:42Z (date -u). Claude Opus 5.5 max, Mac mini worker 2. Research-stage working state; nothing here is a public claim. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Status (updated in place)

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
