lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T07:39Z

# Check of row 1013 (`gap-invent-selective-max`): work items W1 and W2

Row 1015 (`gap-invent-selective-check-opus`), queued 2026-11-15 19:39Z on Mac mini worker 3.
Checker: Claude Opus 5.5, max effort. Author of the checked file: Claude Fable 5.2 (row 1013).
Same provider, so this is a second reading, not an independent check in the sense of the working
rules; where a step below uses a different derivation from the author's, it says so.
Source pinned: branch `claude/ym4d-hard-route` at commit b9125417f.
Checked file: `library/gap-invent-selective-max.md` (row 1013), section 7.3, work items W1 and W2.
W2 is read against `library/gap-pinned-cell-gauge-max.md` (row 1011).
No new attack (row text). Marks: PROVED, ARGUED, OPEN, FAILS; for a checked claim:
CONFIRMED, CONFIRMED WITH CORRECTION, NOT CONFIRMED, FALSE.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read FINISH.md rules for this row, row 1013 section 7.3 (W1, W2, stop rule) and the statements
   and proofs of Lemma WN, Corollaries WN1-WN3, Lemmas TWIST, JEN, SLAB. Record the exact
   checklist here.
2. W1 tests (a)-(e), as written in 7.3, before any proof reading.
3. Lemma WN (i)-(iii) and Corollaries WN1-WN3: line-by-line check, own derivation where possible.
4. Lemma TWIST: line-by-line check.
5. Lemmas JEN and SLAB: line-by-line check.
6. The two ARGUED remarks of W1; apply the stop rule.
7. W2 against row 1011: its three answers.
8. Verdict table, what stays open, RESULT line.

## Progress log

- 2026-11-15 19:41Z: file created, plan written. Step 1 next.

## 1. Step 1 result: inputs, repo search, checklist

**Read in full.** `GOAL.md`; `FINISH.md` L1-84, L299-351, rows 1013, 1015, 1016 (L1094-1097);
`library/gap-invent-selective-max.md` L1-112 and L128-299 (plan, Sections 1-2, candidates C1-C3 and
C8, Sections 4-8). The rest of Section 3 (C4-C7, C9) is not read; W1 does not ask for it.

**Repo search** (grep over this folder for `Lemma WN`, `Lemma JEN`, `Lemma SLAB`,
`gap-invent-selective`, `corner graph`). No earlier check of row 1013 exists. One name clash:
`library/gap-direction2-max.md` L162 (row 970) has a different "Lemma SLAB" (transfer matrix,
infinite time extent). In this file "Lemma SLAB" always means row 1013 Section 5.2.

**Duplicate check (rule 0a).** This row checks proofs; it attacks no open lemma, so there is
nothing to match against `library/open-core.md`. W1's stop rule: no new attack.

**Checklist (W1 exactly as written in row 1013 7.3).**

- Tests first: (a) the sign rule of WN (i) for a link traversed backward; (b) one plaquette,
  density exp(beta x) on SU(2): (beta/3) E(1 - x^2) = E x by one integration by parts with weight
  (2/pi) sqrt(1 - x^2), so rho = 0; (c) in WN (iii), the gauge average at one free site kills each
  cross term, and the closed word passes that site once (sides at least 3); (d) the count "three"
  in WN1; (e) in JEN (ii), the averages at the four corner sites may be taken one after the other.
- Then line by line: Lemma WN (i)-(iii), Corollaries WN1-WN3, Lemma TWIST, Lemma JEN (i)-(ii),
  Lemma SLAB (identity).
- Then judge two ARGUED remarks: "the best lab-frame bound is of order beta eta^2 R" (5.1) and
  Proposition LOC (4.3).
- Report the first failing step, or none.

**W2** (row 1013 7.3): read row 1013 5.1-5.2, then answer for row 1011's construction
(`library/gap-pinned-cell-gauge-max.md`): (1) its blind bound on the stiffness of a cell of side R,
beta or beta R, and if beta, what supplies it; (2) does its class contain two pinned parallel
hyperplanes at distance below beta, or non-cubic cells; (3) does its iteration run at one fixed bare
coupling without the account's effective actions. Row 1015 puts the three answers in this file.

**Conventions fixed for the check** (from row 1013 4.1). SU(2) as unit quaternions,
U = x + i y.sigma, x = (1/2) tr U, c = i sigma_3, c^2 = -1. Then (1/2) tr(c U) = -y_3 and
(1/2) tr(c^2 U) = -x (checked: (1/2) tr(i sigma_3 (x + i y.sigma)) = (1/2) tr(i x sigma_3 - y_3) = -y_3).
The weight is exp(H), H = sum_p beta_p x_p, x_p = (1/2) tr U_p.

- 2026-11-15 19:52Z: step 1 done. Step 2 (tests (a)-(e)) next.

## 2. Step 2 result: W1 tests (a)-(e), each redone by hand

Notation. A plaquette p is a closed path x_1 -> x_2 -> x_3 -> x_4 -> x_1 with four distinct sites;
V_i is the factor of the link between x_i and x_(i+1): V_i = U_l if l runs from x_i to x_(i+1),
V_i = U_l^(-1) if l runs from x_(i+1) to x_i; U_p = V_1 V_2 V_3 V_4. tau_t sends
U_l -> e^(t F(l,s) c) U_l e^(-t F(l,e) c), s and e the start and end of l.

**(a) Sign rule for a backward link: PASSES.** If p runs along l from e to s (backward), its factor
is U_l^(-1), and tau_t sends it to e^(t F(l,e) c) U_l^(-1) e^(-t F(l,s) c). The left exponential
carries F at e, the site where p leaves along l; the right one carries F at s, where p arrives. For
a forward link the same holds with s and e exchanged. So at a corner x_i, arriving by l and leaving
by l', the two adjacent exponentials are e^(-t F(l,x_i) c) e^(+t F(l',x_i) c) = e^(t theta_i c),
theta_i = F(l',x_i) - F(l,x_i), since both lie on the axis c. The pair at x_1 is split between
the two ends of the word and joins by cyclicity of the trace. Reversing the orientation of p sends
every theta_i to -theta_i and the word to its inverse; since tr U = tr U^(-1) on SU(2), the value
is unchanged, so the choice of orientation is immaterial.

**(b) One plaquette: PASSES.** Under Haar measure on SU(2) = S^3 the law of x = (1/2) tr U has
density (2/pi) sqrt(1 - x^2) on [-1, 1] (the slice at fixed x is a 2-sphere of area
4 pi (1 - x^2), and the arc element is dx/sqrt(1 - x^2); the integral of sqrt(1 - x^2) is pi/2).
With the weight e^(beta x):
 0 = integral over [-1,1] of d/dx [ e^(beta x) (1 - x^2)^(3/2) ] dx
   = beta * int e^(beta x) (1 - x^2) sqrt(1 - x^2) dx - 3 * int x e^(beta x) sqrt(1 - x^2) dx,
the boundary terms being 0. Divide by int e^(beta x) sqrt(1 - x^2) dx: beta E(1 - x^2) = 3 E x.
So rho = E x - (beta/3) E(1 - x^2) = 0 for a single plaquette of free links. Second derivation (a
different route, used as a cross-check): for one plaquette, W(t) = E exp(beta [x(e^(t theta c) U) - x(U)])
= 1 for all t by left invariance of the Haar law of U_p, so -W''(0) = 0, which is WN2's formula
theta^2 beta [E x - (beta/3) E(1 - x^2)] = 0. Both agree.

**(c) Cross terms in WN (iii): PASSES.** The cross term of corners i < j is
(1/2) tr(c P_ij c P_ji), P_ij = V_i ... V_(j-1), P_ji = V_j ... V_(i-1), P_ij P_ji the holonomy
based at x_i. Let x_i be free (the case x_j free is the mirror image). The gauge map at the one
site x_i, V_(i-1) -> V_(i-1) h^(-1), V_i -> h V_i (true for forward and backward links by (a)),
touches only integrated links (x_i is free), keeps Haar measure and every x_q. Because the four
sites of p are distinct, the word passes x_i once, so P_ij -> h P_ij and P_ji -> P_ji h^(-1), and
the term becomes (1/2) tr(h^(-1) c h P_ij c P_ji). Average over h (Fubini; the trace is linear in
the inserted matrix): int h^(-1) c h dh is an Ad-invariant element of su(2), hence 0 (Schur). So
each cross term has mean 0. Distinct sites need only sides at least 2; the file's "at least 3" is
sufficient, not a defect.

**(d) The count "three" in WN1: PASSES.** For p = (x; mu, nu), mu < nu, traversed x, x+mu,
x+mu+nu, x+nu: links l_1 = (x,mu) forward, l_2 = (x+mu,nu) forward, l_3 = (x+nu,mu) backward,
l_4 = (x,nu) backward. With F = f at starts and 0 at ends the corners are:
x: f(x,mu) - f(x,nu); x+mu: f(x+mu,nu) - 0; x+mu+nu: 0 - 0 (end of l_2, end of l_3);
x+nu: 0 - f(x+nu,mu) (leave by l_4 at its end, arrive by l_3 at its start). This matches the file.
A link of direction d is the second link of the d - 1 plaquettes with mu < d = nu, and the third
link of the 4 - d plaquettes with d = mu < nu: d - 1 + 4 - d = 3. So the form is at least
3 |f|_2^2. The same count for first and fourth positions gives the upper bound: the form is at
most 2*3 + 3 = 9 times |f|_2^2. In dimension D the two counts are D - 1 each.

**(e) JEN (ii), corner averages one after the other: PASSES.** The sites of p are distinct, so
the gauge maps at the free corner sites with theta not zero act on disjoint sets of factors:
the map at x_i conjugates only the insertion at x_i, e^(eta theta_i c) -> h_i^(-1) e^(eta theta_i c) h_i.
Each map keeps the measure E_u (the site is free; no pinned link moves). Average at the first
site: by linearity of the trace in that insertion and int h^(-1) (cos + sin c) h dh = cos, the
insertion becomes the scalar cos(eta theta_i). A scalar commutes with all factors, so the next
site's average sees the same form. After all sites, E_u[x_p o tau_eta] = prod cos(eta theta_i) E_u[x_p];
corners with theta = 0 contribute cos 0 = 1. (One may also average over independent h_i at once.)

**Summary of step 2.** Tests (a)-(e) pass. One imprecision found on the way, recorded for step 3:
WN1 writes one number xbar = E x_p for all plaquettes; on a torus with unequal sides E x_p can
depend on the plane (mu, nu). With equal sides (hypercubic symmetry) it is one number.

- 2026-11-15 20:05Z: step 2 done. Step 3 (WN (i)-(iii), WN1-WN3 line by line) next.
