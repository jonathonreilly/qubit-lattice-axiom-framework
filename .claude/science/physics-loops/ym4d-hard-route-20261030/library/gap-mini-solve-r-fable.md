lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T17:29Z

# gap-mini-solve-r-fable: four-dimensional SU(2) Yang-Mills mass gap (queue row 1225)

Worker: Claude Opus 5.5 at max effort, Mac mini worker 3, started 2026-11-20T05:29Z on branch
`claude/ym4d-hard-route` pinned at bf998a992. The row was queued for Fable 5.2; per the lead note of
2026-11-20 04:12Z it runs on Opus 5.5 max. No Fable text existed in this file at the pinned commit, so
this file starts fresh.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument
with a named gap), GUIDE (heuristic or numeric orientation, never a proof step), OPEN.

## 0. Status of this file

Step 0 (orientation): done 05:46Z, Section 1. Plan: Section 2. Step A: Section 3. Step B: Section 4. Section 5: what is left. Finished 05:58Z; RESULT line at the end.

## 1. Orientation (read, not re-derived; 05:29Z-05:46Z)

Sources read: `GOAL.md`; `FINISH.md` sections 1-84, 299-360 and the RESULT lines of rows 916-917, 924-925,
1179-1222; `parts/gap.md` L1-104, L311-330; `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-mini-branch-fable.md` L290-330 (row 1179, (N-phys) and Theorem BP);
`library/gap-solve9-astra62.md` L130-160 (row 1161, the finite-aspect statement and its consumer);
`library/gap-mini-solve-q-fable.md` L31-135 (row 1224, running beside this row on worker 1).

What the record says the gap needs (each item cited, none re-proved here):

- The Jaffe-Witten gap clause follows from ONE open lattice estimate, (N-phys), plus a matched continuum datum
  (row 1179 Theorem BP; check row 1183 "main chain HOLDS AFTER CORRECTION"). (N-phys): there are a physical side L
  and j_0 such that for every cutoff j >= j_0 some integer u_j with 3 <= u_j <= n_j/K has
  s_{+,j}(u_j; n_j^3) = Tr_{H_+} U_j^{u_j} - 1 <= 1/2, with K = 512 explicit (check row 1187, item (3): "row 1161
  already gives K = 512"; check row 1183 link (1): the premise is K = 512, 4 | n, n >= 2^70).
- (N-phys) holds iff every fine coupling beta_j has a finite one-cube seed size nu(beta_j) and
  limsup_j a_j nu(beta_j) < infinity (row 1180, checked HOLDS in row 1187). So (N-phys) is a uniform lattice gap
  for centre-neutral states at arbitrarily weak coupling plus a lower bound of asymptotic-scaling type.
- The continuum datum: rows 916-917 prove and check, given the account's premises, the passage from the seed
  (SEED-FP) to the gap on the tr F^2 sector (Lemma C, Theorem E, Proposition P'). Row 1219 reads this as covering
  (N-phys); the lead note there asks for that reading to be confirmed before it is relied on.
- The alternative (ONE-K) (row 916, checked 917): a seed at one cutoff's window suffices, given the
  cutoff-universality hypothesis (UNIV-K), which stays OPEN (rows 924-925).
- Published work of the same group (row 1218): A's (A-B*) is stronger than (N-phys); B's BP is different in kind;
  B's weak-coupling Corollary 166 is not selective (row 1220 Proposition U); C's rate is row 1204's Q. Row 1224
  (worker 1, now running) checks A's slab route (A-M) and runs a kill test of A's hypothesis in 4D. I do not repeat it.
- About seventeen plain-brief rows (row 1224's count, rows 1188-1223) screened candidate mechanisms against the
  record; by their RESULT lines every candidate was on file with a first failing step. Row 998 9.5 lists "another fresh-framing exercise by this model family" under
  "What not to do next". So this row does not screen again.

## 2. How to attack it (judgement, ARGUED)

The crux is (N-phys): a one-scale, cutoff-uniform estimate deep in the infrared (row 1181 GUIDE: at K = 512 the
premise sits near 1.1e4 correlation lengths). Every method on file is blind (it also holds for a massless comparison
model) or is not uniform in the cutoff. I see no route to a proof of (N-phys) in this session, and I say so now.

So I choose bounded work with a named consumer, in this order:

- Step A (consumer side, short): settle the lead's open note on row 1219. Does the checked chain of rows 916-917 take
  (N-phys) as its input, or does it need (SEED-FP) in a form that (N-phys) does not give? Moves: the exact statement
  of what is open for the gap clause. If it fails, the lead learns that the crux is (N-phys) plus a named bridge.
- Step B (producer side, the crux): one attack on (N-phys), not a screening. Chosen in Step B's own section after
  Step A, with its kind ((K-one) or (K-flow), lane rule W2) and the 4D or gauge-specific input it uses named first.
  (Outcome: Section 4 found no structure off the record to attack, so no attack was started; see the Status line.)

Status: Step A done 05:48Z (Section 3). Step B done 05:55Z (Section 4): no attack started, reasons given. Section 5 (what is left, and a process note) written 05:56Z. RESULT line at the end.

## 3. Step A: the checked chain of rows 916-917 takes (N-phys) as its input (05:48Z)

Question (lead note on row 1219): Theorem E of row 916 (`gap-chain-ce-opus.md` L240-251, checked by row 917) is
proved from (SEED-FP), the periodic seed at the first-passage data. Theorem BP of row 1179 gives from (N-phys) only
the even-sector seed (SEED-any-phys) and the even-sector consumers L3-ev, P-ev, P'-ev (`gap-mini-branch-fable.md`
L167-301). Does the composition still close?

Where (SEED-FP) enters Theorem E (read in row 916, Step 5, L172-251):

| Item of Proposition P' | Use of the seed in row 916 | Without the periodic seed |
|---|---|---|
| (H2), E1-E3 | none: lattice identities (CA L1726, L99150-99156) and the account's convergence (CA L1690, L1709, L1785) | unchanged |
| (P1) | members' reflection positivity on all local functions (row 700 Theorem L3 (c) under (G-all)); alternative READ: CA L1759 | members restricted to V_A: L3-ev (c-ev) gives it on V_A; or the account's own statement CA L1759 |
| (P2), (P4) | none (CA L1757-1758, L1761, L1769-1770) | unchanged |
| (P3) | the member's transfer is a contraction (gap-os-equiv (1b)), from its (P1)-(P3) | the same on V_A, by L3-ev (e-ev) |
| (TOT) | none (CA L115178-115181, L115205) | unchanged |
| (H1) of the members, m_n = M_* | Lemma C (iv) = row 700 Proposition P (c) under (SEED-FP) | P-ev (c) under (SEED-any-phys), on H_A(nu_j) |

**Lemma A0 (the account's lattice observables are centre-blind). PROVED.** Let A be the class of row 1179 5.0
(local F on Z^4 with F(g.U) = F(U) for every map g from the sites to {+1, -1}, where
(g.U)(x, mu) = g(x) g(x + mu) U(x, mu)). Every gauge-invariant local function on Z^4 is in A. In particular every
lattice version iota_j X of row 916 E1 is in V_A.

Proof. The map U -> g.U is the gauge transformation by the site function g, whose values lie in the centre
{+1, -1} of SU(2) (central values commute with U, so g(x) U g(x + mu)^(-1) = g(x) g(x + mu) U, as g(y)^(-1) = g(y)).
A gauge-invariant function is invariant under every gauge transformation, so under these. The account's observables
are sums of plaquette traces: O(f) = sum_p f(x(p)) a_p(U) with a_p = 1 - (1/2) Re tr U_p (CA L1640-1658, L1651) and
O_j(f) = sum_p f(x_p) A_p (CA L99284-99294), both as READ in row 916 Step 3, items (O1) and (O5); I did not re-read
the account. A plaquette trace is gauge invariant, and centring by a constant and taking products keep gauge
invariance. E1 gives the time range in (0, infinity). QED

**Theorem E-N (Theorem E with (N-phys) in place of (SEED-FP)). PROVED GIVEN (N-phys) on the account's trajectory
and the inputs of row 1179 5.0 ((TM-tw), (S), Theorem S-w, Corollary EV, (L), `gap-os-equiv.md` Statements (3), (5a)-(5c),
Lemma E), and the account's statements READ in row 916 Step 5.** Let S be a volume-first limit at g with defining
sequence (K_j, beta_j, nu_j) (CA L1690, L1893), and assume (N-phys) along (K_j, beta_j): one physical side L with
4 | L/a_j for all large j (for example L a multiple of 4 in units with a_0 = 1, since a_j = L_b^(-K_j) with an odd
blocking factor L_b). Then ker H = C Omega in H(S) and spec(H) lies in {0} union [M_*, infinity), with a cutoff-free rate: in the form
checked by check 1183 (its N-JW (c, d) after correction; premise K = 512, 4 | n_j, n_j >= 2^70),
M_* = (2/L) log(2^18/5041) > 7.9/L; row 1179 Theorem BP (ii) writes M_* = (2/L) log(1/(40328 eps)).

Uniformity. To cover every volume-first limit at g, read (N-phys) in the uniformity of (SEED-FP) (row 916 Step 1):
one side L and K_0 such that the bound holds at every first-passage datum (K, beta) with K >= K_0. For one given S,
(N-phys) along its own defining sequence suffices.

Proof. Step 1. Each nu_j is a limit state of periodic symmetric tori (N_i, N_i) at the cutoff j, with no seed
(row 916 Lemma C (i)-(iii), checked in row 917). Step 2. By Theorem BP (i), (N-phys) gives (SEED-any-phys) at every
large cutoff with the class kappa, N_j = n_j/2, ell_* = L/2, s_* = 8 eps. By Proposition P-ev (c), the datum D_(nu_j)
on V_A (L3-ev (e-ev)) has transfer norm at most exp(-M_* t a_j) on the complement of its vacuum. This is (H1) of
Statement (5) with S_j the whole complement. Step 3. Take D_inf, C and iota_j exactly as in row 916 Step 5. By Lemma A0,
iota_j maps C into V_A. The six items of the table hold: (H2), (P2), (P4), (TOT) by row 916's proofs, which never
read the seed; (P1) and (P3) by row 916's proofs with the members' (P1)-(P3) taken on V_A from L3-ev (c-ev), (e-ev),
or directly from CA L1759, L1761. Step 4. Proposition P'-ev (row 1179 5.3) applies to D_inf with this C. Its
conclusion is the claim. QED

Remarks. (1) This is the even-sector form of Theorem E; the only change is to restrict the member data to V_A, which
row 1179 5.3 already does for the abstract datum. No branch, flux alternative or twist ratio is read (check 1183's
wording correction for "no flux sector": the proof uses both alternatives of row 1161 but chooses neither).
(2) The canonical-component corollary of Theorem E (CA L1895) follows as there.
(3) Scope. The conclusion is on H(S), the account's tr F^2 sector; whether that sector is the whole theory is a T0
question, not a gap question. All account statements carry the account's hypotheses (CA L1748-1751).
(4) Standing. A composition of checked statements, written by Claude Opus 5.5 (same provider as row 916 and as the
Fable author of row 1179); not checked by the other provider. It answers the lead note on row 1219: the reading
there is right, given the restriction to V_A.

**Consequence for the lane (PROVED GIVEN the same inputs).** For SU(2) along the account's trajectory, the
Jaffe-Witten gap clause on the tr F^2 sector is implied by (N-phys) alone, beside the account's premises. Nothing
else on the gap side is open.

## 4. Step B: what any proof of (N-phys) must contain (ARGUED from checked statements; 05:54Z)

**Self-similarity of the band (ARGUED; each link is a checked statement).**

1. (N-phys) along the trajectory implies, at every large cutoff j, a centre-neutral lattice gap of the bare Wilson
   theory at the FIXED coupling beta_j on every periodic cube of side at least n_j (row 1179 P-ev (a)).
2. Conversely, a seed at one cutoff's window implies (N-phys) given (UNIV-K) (row 916 (ONE-K), checked row 917).
   (UNIV-K) is a statement about the ultraviolet (the account's finite-horizon universality at n = 0); it is OPEN
   (rows 924-925 reduce it to (MAPCONV), (VAC-ID), (DENS-K) B1-B2, (CLASS)); ARGUED: it needs no estimate in the band,
   since it compares two cutoffs on one fixed torus through the account's ultraviolet steps.
3. The seed at a fixed coupling beta_0 cannot sit at a side where the running coupling is small (first passage;
   row 1180 seed-size form; row 1215 (5), levels coalesce at fixed spatial size; A's Theorem 7.59, row 1218).
   So its cube has side of order exp(c beta_0) lattice units at least, and the estimate is an infinite-volume
   statement about one lattice theory with no small parameter.

So, modulo an ultraviolet statement, the crux is the lattice mass gap of SU(2) Wilson at ONE fixed coupling in the
account's window. Balaban's renormalisation group, and the account's, map weak coupling to weak coupling: they
stop at a threshold g_0 and hand on SU(2) at coupling g_0 on a coarser lattice, which is the same problem at the
fixed coupling 4/g_0^2. GOAL.md forbids a computed certificate, so the estimate at that coupling must come from a
structure valid at all couplings (a positivity, a monotonicity or convexity in the coupling, an exact identity or
duality), not from a finite check.

**The structural families, each on file with its failure (cited, not re-derived):**

| Family valid at every coupling | Selective for SU(2)? | Where it stops on file |
|---|---|---|
| Correlation inequalities, association, FKG, Ginibre | would be | FKG fails for plaquette traces (row 1213 Lemma FKG-NO); Hopf frustration (row 1188 Lemma HF); gauge port of the 2D positivity step fails three ways (row 1084) |
| Positive dual or random-surface representation | would be | adjoint moments positive only when each link lies in at most three plaquettes (row 1213 Lemma PAR); 4D links lie in six; dual-gas positivity FAILS (check 1209, E193) |
| Monotonicity or convexity in the coupling (coupling integral, Feynman-Hellmann, thermal flow) | no by itself | reads the gap at every smaller coupling, (ANOM) of row 931; rows 1190, 1198 |
| Exact identities: loop equations, sector Fourier analysis, Pfaffian transfer | partly (splitting term) | volume blind (rows 754-767, Proposition VB); sector identities give the reduction, not the bound (rows 697, 731, 1161) |
| Curvature, Bakry-Emery, orbit-space geometry, Gribov region | partly | magnetic energy not convex (row 1032 B8); horizon condition has no consumer (B9); method 31 |
| Stiffness iteration with a bracket gain (the 2D O(N) step) | yes | dimension count on a 3D slice (row 1188 Lemma PC; row 1193 Lemma PC-c); colour coherence lost under pin suprema (rows 1011, 1016) |

I found no structure outside this table that holds at every coupling, is selective, and gives a bound. I did not
start an attack that would end at a row of this table; by row 998 9.5 and FINISH "Is it worth doing?" such an attack
is waste.

Correction (05:55Z) to a plan written at 05:54Z. I had marked the splitting term of the SU(2) loop equations as the
one entry not closed on file. It is closed: row 754 (`gap-loop-eq-opus.md` Lemma 1.2, 5.3) shows the splitting
terms make the winding difference equation non-contracting (theta_m >= 1 for m >= 4 at every beta), Proposition VB
gives volume blindness of every local constraint set, and rows 755-767 (`gap-loop-pos-astra.md`,
`gap-loop-grow-astra.md`, Theorem O) show positive width for every fixed-radius and sublogarithmic certificate, while
full finite-volume Ward data determine the Wilson measure. So no part 2 is run on loop equations.

## 5. What is left, and a process note (05:56Z)

**State of the gap side after Section 3 (PROVED GIVEN checked statements, same provider; needs a cross-provider
check).** The Jaffe-Witten gap clause on the account's tr F^2 sector is implied by (N-phys) beside the account's
premises (Theorem E-N). Lemma A0 removes the one point that row 1219 left to confirm: the account's observables are
gauge invariant, hence centre-blind, so the even-sector consumer of row 1179 reads them. A short cross-provider check
of Section 3 (Lemma A0, Theorem E-N, its six-item table) would close it. Nothing else on the gap side is open.

**What stays open.** (N-phys) (the infrared crux); the account's premises (the T0 chain, CA L1748-1751); (UNIV-K)
only if the lane wants the one-cutoff form (ONE-K).

**Process note for the lead (not a proof claim).**

1. Section 4 gives a structural reason, from checked statements, why plain-brief crux rows keep landing on the map:
   modulo (UNIV-K) the crux is the lattice gap of SU(2) Wilson at one fixed coupling with a seed side of order
   exp(c beta_0), and with no computed certificate allowed (GOAL.md) it must come from a structure valid at every
   coupling. A filter in place of row 1002's plausibility test (withdrawn as a price, `parts/gap.md` lead rules) would
   ask each new crux row to name such a structure that is not in the table of Section 4, before any work.
2. Open items on the gap path that need no infrared input: (UNIV-K) through the sub-hypotheses named by row 924
   ((MAPCONV), (VAC-ID), (DENS-K) B1-B2, (CLASS)); it is in neither `library/open-registry.md` nor
   `library/t0-tree.md` at this pin (grep, 05:56Z), and no row has worked on it since row 925 (2026-11-14). It would
   turn the crux into one statement at one coupling window; it would not supply that statement.
3. This row spent no tokens on a screening. It ran 05:29Z-05:58Z (date -u).

RESULT: Row 1225 (Claude Opus 5.5 max, Mac mini worker 3, 05:29Z-05:58Z; the Fable 5.2 row ran on Opus by the lead note; author only, checked by no one; no numeric run). The mass gap is NOT proved and nothing is disproved. PROVED GIVEN checked statements (a composition, same provider as rows 916 and 1179, needs a cross-provider check): Lemma A0 (every gauge-invariant local function, so every account observable built from plaquette traces, is centre-blind) and Theorem E-N (Theorem E of row 916, checked in row 917, holds with (N-phys) in place of (SEED-FP) once the member data are restricted to V_A, using row 1179's L3-ev, P-ev, P'-ev): for SU(2) along the account's trajectory the Jaffe-Witten gap on the account's tr F^2 sector follows from (N-phys) alone beside the account's premises, with rate M_* = (2/L) log(2^18/5041) > 7.9/L in check 1183's form; this confirms the reading the lead asked to check in row 1219. ARGUED: modulo the ultraviolet hypothesis (UNIV-K), the crux is the lattice gap of SU(2) Wilson at one fixed coupling with a seed side of order exp(c beta_0); with no computed certificate allowed it must come from a structure valid at every coupling, and every such structure on file (positivity and association, positive duals, coupling integrals, loop and sector identities, curvature and Gribov geometry, the bracket stiffness step) stops at a cited failure, so no attack was started and no screening was run. OPEN: (N-phys), the account's premises (T0 chain), (UNIV-K) (unowned since row 925). Output library/gap-mini-solve-r-fable.md.
