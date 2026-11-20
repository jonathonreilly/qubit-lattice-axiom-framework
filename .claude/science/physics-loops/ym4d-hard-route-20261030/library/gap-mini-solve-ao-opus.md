lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:45Z

# gap-mini-solve-ao-opus: the SU(2) mass gap in four dimensions

Queue row 1278 of `FINISH.md`. Started 2026-11-20T13:45Z on the Mac mini, Claude worker 3, pinned at commit 45997b1e3.
The problem as briefed: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation only), OPEN.

## File status

Written section by section. Sections below are appended as each step finishes.

## Step 0. Reading record (13:45Z-14:00Z by date -u)

Read: `GOAL.md`; `FINISH.md` opening sections, rules, efficiency section and queue rows 1143-1286 (titles); `parts/gap.md`
State of attack (lines 1-104); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; the RESULT lines of every
`library/gap-mini-solve-*`, `gap-owner-*` and `gap-laptop-solve*` file at this commit.

What the record says, in short (each item is a citation, not evidence of its own):
- The only open lattice input of the gap clause is the infrared seed (N-phys) (row 1179 Theorem BP with check 1183;
  the continuum datum is proved given the account's premises, rows 916-917; row 1219's RESULT line).
- About forty plain-brief rows (1188-1275) screened route families against (N-phys); each ends "NOT proved, nothing
  disproved". The literature names I tested by grep (Tomboulis, Migdal-Kadanoff, Ito-Seiler, Chatterjee, Adhikari-Cao,
  Shen-Zhu-Zhu, instantons, Gopfert-Mack, Brydges, Federbush, Magnen-Rivasseau, Durhuus, Osterwalder-Seiler,
  Mack-Petkova, Yaffe, Borgs, Kovacs) each have 20 to 180 hits in `library/`, `parts/` and `FINISH.md`.
- The later Opus rows (1255-1275) worked the one-cutoff carry: (EDGE), (FI), (FC), (FC-T)/(FC-1), (V9). Open there per
  rows 1268 and 1275: (U) at the jumps of R_k; the readings (E0)-(E6) against Balaban CMP 116; row 1267's (H2)-(H3);
  Theorem 9.1's hypothesis (e) `9.1:prop-blind-site-expansions` (outstanding in the account; row 1264 was blocked by a
  bot check on CMP 116); (DET)'s inputs.
- Siblings in flight at this commit: row 1277 (an) reads the question left UNDECIDED by check 1239 (does the slab
  hypothesis (M) of Bhattacharjee et al. fail along the 4D Wilson tuning?); row 1280 (ap) was at its Step 0.

Decision rule for Step 1: no forty-first screen of route families (lead's "what not to do next", row 998 9.5, and
the forty RESULT lines above). Choose one precise statement on the gap chain that no row owns, and take it to a proof,
a counterexample, or one precise failing step.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T14:02Z by date -u)

**The crux, as I read the record and as I re-derive it.** Modulo the ultraviolet carry, the gap clause reads one
lattice input: a seed of Wilson SU(2) at one coupling of the account's window (rows 1179, 1225, 1233, 1234; check 1183).
At beta between 2.3 and 2.6 (standard normalisation) the glueball correlation length is of order one to four lattice
spacings (GUIDE, recalled Monte Carlo lore, not used as a step). So the seed is a statement about a lattice of a few
tens of spacings per side at a coupling where:
- every published rigorous method stops far below: cluster and character expansions, Dobrushin and Bakry-Emery bounds
  reach beta of order 0.1 to 0.2 in this normalisation (row 1218: A's single-link and star ranges, B's Corollary 74,
  the curvature range of A and B Theorem 5; the conversion beta_W = N_c^2 beta = 2 beta_std is mine and assumes A's
  action is beta times the sum of Re tr U_p, which I did not read in A);
- the uniform-boundary finite-size criteria are false (Proposition CA-FAIL, row 1072/1073, holds after correction in
  check 1074: two pinned adjacent slices make the temporal links a 3D O(4) magnet that orders above about beta 1.01);
- a finite computation would be a computer-assisted step, which GOAL.md forbids.
So the seed is the lattice mass gap at one intermediate coupling. I know of no rigorous result of that kind for any
four-dimensional lattice gauge theory with a continuous non-abelian group, and the forty plain-brief rows found none
on file. My own re-derivations (center-vortex and electric-flux free energies, Singer's positive curvature of the orbit
space with the Faddeev-Popov density, the Kogut-Susskind electric gap, finite-subgroup approximants, Migdal-Kadanoff
flows, a change of bare action) each meet a recorded first failing step: the curvature gain is O(1) against a Hessian
of order beta; finite subgroups and Migdal-Kadanoff are group-blind or meet the same band; a change of bare action
changes only irrelevant terms, and the effective theory at the physical scale is the same strongly coupled one.
Verdict (ARGUED): no attack on the seed fits one session; a further screen is waste.

**What I do instead.** One open input of the chain that no row owns and that can be closed with sources on hand.
Owned at this commit or at the branch tip (read by `git fetch` at about 14:00Z): (U) by row 1280; the slab hypothesis (M) by
row 1277; the CMP 116 readings (E0)-(E6) and `9.1:prop-blind-site-expansions` are blocked (CMP 116 is not in the
papers folder; row 1264 met a Project Euclid bot check). Unowned: (H2) cross-admission and (H3) the total-form list
comparison of row 1267's Proposition FC-chain. Row 1267 labels (H3) ARGUED from EM input (4) with an open condition
("This needs f'' to be admitted") and (H2) assumed.

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1260, 1267, 1268). Success: (H2) and (H3)
leave the input list of Theorem FCT' (row 1268). Failure: an admission condition of EM that the shifted list f'' or the
other frame's list violates; then the frame comparison needs a different splitting.

Rule 0a: grep of FINISH.md and `library/open-core.md` for "(H2)", "(H3)", "cross-admission": hits only in rows 1267,
1268, 1275 (as OPEN inputs); no queued row names them.

## Step 2. (H3) and (H2) of row 1267 (written 2026-11-20T14:09Z by date -u)

Source: Sussman and Alpoge, `YM4/EM/YM4_EM.tex` at c7fef8b21b58 (2001 lines; with Claude and Codex as authors of their
text; after Balaban), fetched by raw URL into a scratch folder outside the repository. "EM:n" is a line of that file.
Row 1267 = `library/gap-mini-solve-ak-opus.md` (its 3.1-3.2, Proposition FC-chain).

**2.1 What EM supplies (READ, with lines).**
- (R1) The step reads a list only through the totals of its subtracted members. EM:532-561: S_f is "the sum of its
  vacuum-subtracted regular families, their own Wilson counterterms and its vacuum-subtracted remainders", and the
  physical output is (em:eq-actual-step), log of the integral of K_(k,theta_k)(W, dV) exp[-x_k A(U_k(V)) + S_f(U_k(V))]
  plus x_k A(U_(k+1)(W)) - S_f(U_(k+1)(W)). Adding a constant to S_f changes nothing.
- (R2) The coefficient readout b_j is linear, real on real data, and "unchanged ... by changing coherent localizations
  of the same physical total" (EM:1202-1204; proof EM:1218-1219: "two coherent localizations of the same total give the
  same kernel"). A constant total has zero Hessian, so b_j vanishes on it.
- (R3) One-step input (3) (EM:667-706): for a list of regular entries of norm at most E_0 with s(1 + N_k) <=
  eps_step, the step forms E_(k+1) = N_(k+1) + G_(k+1,tau_k) + F_(k+1)[f]; N_k is the age-weighted sum of the ORIGINAL
  regular-family norms "before vacuum and quadratic subtraction", and "the fixed subtraction-operator bounds are
  included in K". One-step input (4) (EM:707-716): for two admitted lists on the common smaller cores, ||F_(k+1)[f] -
  F_(k+1)[f']|| <= K s times the weighted load of the differences of their inputs, same age weights, through "the
  prescribed interpolation and contour domains" of the marked slot. N and G do not depend on the list.
- (R4) Formation (EM:855-870): above the floor every creation has norm at most B_N + (E_0 - B_N)/4 + (E_0 - B_N)/2 =
  (3 E_0 + B_N)/4, a margin (E_0 - B_N)/4 below the cap, and every list with entries of norm at most E_0 meets
  s(1 + N_k) <= eps_step (D_* = Omega E_0).
- (R5) Regular families: covariance under the partition isometries, a companion, the scalar coefficient (EM:251-273);
  the pointed norm (em:eq-pointed-norm, EM:225-238) takes the supremum over the admissible tori and the companion; the
  absolute cores a_* are fixed for the whole chain (EM:504-508). Row 1267 READ that regular families form a linear space
  (EM:215-218) and defined |||T|||_j as the infimum of ||H||_(j,kappa;a_*) over regular pointed families H whose total
  is T + const (row 1267 3.1).

**2.2 Proposition H3' (PROVED GIVEN (R1)-(R5); author only, unchecked).** Fix a frame phi, a weight x_k and a step k.
Let f, f' be two unmarked lists admitted at that step, with original regular families O_i, O'_i (i = 1..k) and
subtracted members f_i = Sub_i(O_i), f'_i = Sub_i(O'_i), where Sub_i(H) := H - vac(H) - b_i(H) (tent-pointed A_i)
(EM:266-283). Put d_i := |||T(O_i) - T(O'_i)|||_i (original totals). Let mu_slot > 0 be the radius of the admitted
marked slot of input (4) in member norm (the size of list differences for which the interpolation of (R3) stays
admitted). If max_i d_i < min(mu_slot, (E_0 - B_N)/4), then
    |||T(E^phi_(k+1)[f]) - T(E^phi_(k+1)[f'])|||_(k+1) <= K s_k sum_(i<=k) omega_(k+1-i) d_i.          (H3')

Proof. Here, as in row 1267 3.1, the total of a family is its sum over domains on each admissible torus, up to an additive
constant; the companion enters only through regularity (R5) and through b_j, which by (R2) depends on these totals
alone. Let eta > 0 be small. For each i choose a regular pointed family h_i with total T(O_i) - T(O'_i) + c_i and
||h_i|| <= d_i + eta (definition of |||.|||_i). Put O''_i := O_i - h_i (regular, by linearity) and f''_i := Sub_i(O''_i).
(a) Totals. T(O''_i) = T(O'_i) - c_i. By (R2), b_i(h_i) = b_i(O_i - O'_i) = b_i(O_i) - b_i(O'_i) (h_i and O_i - O'_i are
coherent localizations of totals that differ by a constant; linearity), so b_i(O''_i) = b_i(O'_i), and T(f''_i) =
T(f'_i) + const. By (R1) the integrands of the step on f'' and on f' are equal on every admissible torus, so the
physical totals of E^phi_(k+1)[f''] and E^phi_(k+1)[f'] agree on every torus up to a constant; since N, G do not depend
on the list (R3), T(E[f]) - T(E[f']) = T(F[f] - F[f'']) + const on every torus.
(b) Admission of f''. ||O''_i|| <= (3 E_0 + B_N)/4 + d_i + eta <= E_0 for eta small (R4); so f'' is a list of regular
entries of norm at most E_0 on the same absolute core, and s(1 + N_k(f'')) <= eps_step (R4). The list difference
f - f'' has members of original norm ||h_i|| <= d_i + eta < mu_slot, inside the marked slot.
(c) Bound. F[f] - F[f''] is a regular pointed family at level k+1 (both outputs are regular; linearity) whose total is
T(E[f]) - T(E[f']) + const by (a). So the left side of (H3') is at most ||F[f] - F[f'']|| <= K s_k sum_i
omega_(k+1-i) ||h_i|| <= K s_k sum_i omega_(k+1-i) (d_i + eta) by input (4) in original-family norms (R3). Let eta -> 0. QED

Differences from row 1267's (H3). (i) The right side reads the ORIGINAL totals, so the factor (1 + C_x C_A) of row
1267's (3.2) is not needed: with O^theta_i = E^theta_i, d_i is exactly row 1267's u_i. (ii) The open condition of row
1267 ("This needs f'' to be admitted") is met in the regime max d_i < min(mu_slot, (E_0 - B_N)/4); it is not met for
large differences, so (H3') is a small-difference statement and the chain needs a bootstrap (2.4).

**2.3 Lemma H2' (cross-admission; ARGUED: PROVED GIVEN (R3)-(R5), row 1267's READ list of where the frame enters, and
connectedness of the core).** Row 1267
2.4 READ that the unmarked chain reads the frame only inside the actual kernel K_(k,theta_k) (cut, gauge weight, real
fluctuation coordinates); localisation cubes have the fixed side M (EM:176-178), the absolute radii a_* are fixed
(EM:506-510), backgrounds come from the frame-free block map (EM:240-249), and the unmarked list has no aged remainders
(EM:535-536). Given that, a member formed on the frame psi is a regular family on the same absolute core with norm at
most (3 E_0 + B_N)/4 (R4); the step on the frame phi reads it only through its total, its own coefficient and its own
companion (R1, R2, R5). The one frame-dependent number attached to a member, its creation covariance radius c_e
eps(theta_j) (EM:653-656), does not restrict its use on phi: covariance, P_(rz)(G; rW) = P_z(G; W) (EM:258-262), is an identity between
holomorphic functions of W on the absolute core, so it continues from any open real set on which it holds to the
connected domain of both sides (identity theorem; EM uses the same device for parameters at EM:812-816). This needs the
core to be connected and isometry-invariant, which I did not find stated (ARGUED).
So f^psi_k satisfies the conditions of (R3) on the frame phi: (H2) holds.

What is not shown: that EM's "admitted" in input (4) contains nothing beyond (R3)'s conditions and the marked slot
(EM states admission in prose across EM:500-716; I found no further condition on lists there); and the reading of
row 1267 2.4 itself. Both are readings, so Lemma H2' is PROVED GIVEN readings.

**2.4 Corollary FC-chain' (PROVED GIVEN Proposition H3', Lemma H2', (H1), (H4) = (FC-1) with loads nu_k, and
(H5') K s_* Omega <= 1/2).** Let mu := min(mu_slot, (E_0 - B_N)/4)/2 and suppose nu_k <= mu/2 for every k < n (true
above a high floor by Theorem FCT' of row 1268, whose nu_k tends to 0). Then for 0 <= k < n
    u_(k+1) <= nu_k + K s_k sum_(i=1)^k omega_(k+1-i) u_i,   u_(k+1) <= mu,                                  (2.1)
and sum_(i<=n) u_i <= 2 sum_(k<n) nu_k, eta_k <= C_x u_(k+1), sum_k eta_k <= 2 C_x sum_k nu_k.
Proof. Induction on k. u_1 <= nu_0 <= mu (empty lists, EM:536). If u_i <= mu < min(mu_slot, (E_0 - B_N)/4) for i <= k,
split as in row 1267: T(E^phi[f^phi]) - T(E^psi[f^psi]) = [T(E^phi[f^phi]) - T(E^phi[f^psi])] + [T(E^phi[f^psi]) -
T(E^psi[f^psi])]. The second bracket is at most nu_k by (H4) on the list f^psi_k, admitted on phi by Lemma H2'. The
first is at most K s_k sum omega u_i by (H3') with d_i = u_i. This is (2.1)'s first inequality; then u_(k+1) <= mu/2 +
K s_* Omega mu <= mu by (H5'). Summation as in row 1267 (3.3), with Omega and (H5'). The coefficient bound is row 1267's
(3.4) unchanged. QED

**2.5 Effect on the input list of Theorem FCT' (row 1268).** (H2) and (H3) leave the list, replaced by the readings
(R1)-(R5) and row 1267's READ list of 2.4; (H5) is weakened to (H5'). Still open on the pin route: (U) (row 1280 is on
it), (E0)-(E6) against Balaban CMP 116 (not on this machine), (TH), and everything outside the carry (the seed, the 9.1
hypothesis (e), (DET)'s inputs, the account's premises). The mass gap is not touched by this step.

Check request (cross-provider, one reading): Proposition H3' (a)-(c), in particular the use of (R2) for h_i and the
claim that input (4) is a bound in original-family norms; Lemma H2', in particular the covariance-continuation sentence
against EM:812-816 and the creation radius at EM:653-656.

## Step 3. (TH) of row 1268, read at the source (written 2026-11-20T14:14Z by date -u)

(TH) is row 1268's threshold identification: in the common chart every small-field threshold is at least
a (log theta_k)^(p_0) with a > 0 fixed. Row 1268 marked it ARGUED ("the unit conversion between the two frames'
normalized fields is my reading"). Read in CA-I at 31a47c543775 (Sussman and Alpoge, with Claude and Codex as authors
of their text; after Balaban CMP 119):
- the degree function is p_0(g) := A_0 (log g^(-2))^(p_0) (I:1012-1014; glossary I:345-347), with p_0 a natural number,
  p_0 >= 5r, r >= 2 (I:1346-1349);
- the cutoff radius of the one-step theorem is (A_1/A_0) p_0(g) = A_1 (log g^(-2))^(p_0), and "When g = g_k, this radius
  is the quantity delta_k/g_k of [B-CMP119]" (I:4172-4175);
- the raw threshold is delta_m = (A_1/A_0) g_m p_0(g_m) = A_1 (log g_m^(-2))^(p_0) g_m, "the threshold of [B-CMP119,
  (3.16)]" (I:29104-29110);
- EM's frame entry is the Wilson weight x = g^(-2) (the bare density is exp[-g_0^(-2) A(U)], CA-I def-wilson-action;
  EM:500-503 writes x_k for the weight and tau_k = x_k/theta_k); EM leaves delta(theta) supplied and gives
  delta(theta) = c_delta theta^(-1/2) (log theta)^(p_0) as its example (EM:872-875); CA-I's delta_m is that function
  of theta = g^(-2) with c_delta = A_1.

**Lemma TH (PROVED from the lines above; elementary).** Let theta, theta' be the entries of two frames at one step, with
|x_k/theta - 1| < 1/4 and |x_k/theta' - 1| < 1/4. In the field normalised by theta'^(1/2) (frame theta''s chart), frame
theta's cut radius is A_1 (log theta)^(p_0) (theta'/theta)^(1/2) >= 3^(-1/2) A_1 (log theta)^(p_0), and if theta >= 9
it is also >= 3^(-1/2) 2^(-p_0) A_1 (log theta')^(p_0).
Proof. The raw cut of frame theta is |V| < delta(theta) = A_1 (log theta)^(p_0) theta^(-1/2). Multiplying by
theta'^(1/2) gives the first expression. Both entries lie in (4 x_k/5, 4 x_k/3), so theta'/theta > (4/5)/(4/3) = 3/5 > 1/3.
For the second form, theta' < (5/3) theta < 3 theta, so log theta' < log theta + log 3 <= 2 log theta when theta >= 3,
and (log theta)^(p_0) >= 2^(-p_0) (log theta')^(p_0). QED

So (TH) holds with a = 3^(-1/2) A_1, as row 1268 wrote, when each frame's threshold is measured against its own log
theta; against the other frame's log theta' the constant is a = 3^(-1/2) 2^(-p_0) A_1. Either is a fixed positive
number. (TH) leaves the input list of Theorem FCT' as READ plus Lemma TH. The identification of EM's frame entry with
g^(-2) is the one reading left; EM's delta(theta) and CA-I's delta_m are the same function of it.
