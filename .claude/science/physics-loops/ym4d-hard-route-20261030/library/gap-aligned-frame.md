lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-16T11:55Z

# gap-aligned-frame (row 1026): decide the aligned frame left open by check 1022

Pinned at commit fe79776a6, branch `claude/ym4d-hard-route`. Started 2026-11-15T23:55Z (from `date -u`).
Research-stage working state. Nothing here is a public claim.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read the sources the row names: `parts/gap.md`, `library/gap-short-step-max.md` 4.1-4.5,
   `library/gap-short-step-check-opus.md` L220-290 (D2), Lemma FR of
   `library/gap-pinned-cell-gauge-max.md` 7.3. Fix the exact definitions: frame n, heads, N_l, projected
   current, cost, curl form, "order-one response". Grep `library/open-core.md` and FINISH rows for overlap.
2. State the open statement precisely (AF) in the notation of the sources.
3. Hand test: one plaquette.
4. Hand test: one cube.
5. Hand test: 3^4 torus (structure, counting of equations against unknowns).
6. Decide: obstruction on an open set of positive Wilson measure, or a construction with cost form and consumer.
7. Optional numeric guide or refutation, under the numeric lock, only if memory is 50 percent free or more.
8. Verdict table with marks PROVED, ARGUED, OPEN, FAILS, credits, and the RESULT line.

## Step log

(steps are appended below as they finish)

### Step 1 (done 2026-11-16, first response): sources read, overlap check

Read in full: `library/gap-short-step-max.md` Section 4 (L213-277: Lemmas FLOW, PROJ, FR+, SPLIT, sizes 4.5);
`library/gap-short-step-check-opus.md` L215-292 (D2 at L224 and L273); `library/gap-pinned-cell-gauge-max.md`
3.1-3.2 (conventions, Proposition A) and 7.3-7.4 (Lemma FR, (N1)-(N3)); `parts/gap.md` L1-60 and L137.
Overlap grep (`aligned`, `orthogonal to the forces`, `conserved pathwise`, `projected current` in
`library/open-core.md`, `FINISH.md`, `parts/gap.md`): the only matches are row 1022 (the check that opened this
item), this row, and `parts/gap.md` L137 (which records the item as open). No other row covers it. Row 1016 plan
step 7 (reopen condition (ii) of row 1013 in general) is the neighbour named by row 1018; it is not this statement.

### Step 2: the statement, in exact form

Notation of row 1011 3.1-3.2 and row 1018 4.2. Lattice Lambda (a finite 4D torus with V sites, or a cell). Links are
oriented x -> x + mu. X(b) = (d/d eps) A(e^(eps b) U) = - sum_l b_l . N_l, so N_l in su(2) = R^3 sits in the frame of
the tail of l. Gauss law (PROJ (ii)): M_z := sum_(tail z) N_l = sum_(head z) Ad(U_l)^(-1) N_l.
A frame is a unit-vector field n_x(U), gauge covariant: n_x(U^g) = Ad(g_x) n_x(U). j_l = n_tail(l) . N_l.
(div j)(z) = sum_(tail z) j_l - sum_(head z) j_l = - sum_(head z) (D_l n) . N_l (PROJ (iii)).

**(AF-1), pathwise alignment.** At the configuration U: div j = 0 at every free site.
**(AF-2), the cost.** The cost form of the moves theta n is zero on gradients theta = d lambda, and is bounded by a
constant times beta sum_p (d theta)_p^2 at order-one response.

Three exact remarks that fix what has to be decided (each PROVED, one line).

**Remark LIN.** At fixed U the current is linear in n. Put P_x(lambda) = sum over l with tail x of
(lambda_x - lambda_head(l)) N_l in R^3. Then sum_l (d lambda)_l j_l = sum_x n_x . P_x(lambda). So (AF-1) says:
n is orthogonal in (R^3)^V to the subspace PP(U) = {P(lambda)}, of dimension at most V - 1 on a torus. Without the
unit-length condition the solutions form a linear space K(U) of dimension at least 2V + 1. (AF-1) asks for a point
of K(U) on the product of spheres (S^2)^V: V - 1 linear equations for 2V angles. No count excludes it; no count
gives it (K = {v_1 = 2 v_2} has codimension 3 and no unit point, and missing (S^2)^V is an open condition on K).

**Remark JAC (the further point of D2, made exact).** For a field-dependent frame the move V = theta n has
div V = sum_l theta_l d_l with d_l(U) = sum_a (derivative of n^a_tail(l) in direction a of link l). So in Lemma FLOW

  Psi_(theta n) = - sum_l theta_l (j_l - d_l).

The cost is zero on gradients if and only if the current jt = j - d is conserved almost surely. Then the fields
V_lambda = (d lambda) n are infinitesimal symmetries of the measure e^A dU, and for lambda zero on the pinned sites
E[V_lambda f] = - E[f Psi_lambda] = 0; so Q(theta) = - E[V_theta Psi_theta] satisfies Q(theta + d lambda) = Q(theta):
it is a quadratic form in d theta. That is the meaning of "curl form" in PROJ (iv). It is NOT yet a bound by
beta sum_p (d theta)_p^2: a form C(d theta, d theta) with a long-range kernel C (for instance the transverse
projector, a mass term for the transverse part of theta) is also zero on gradients.

**Remark BACK (a cleaner divergence-free class than tree transport).** If n_x does not depend on the four links with
tail x, then d = 0 and theta n is divergence free for every theta. Gauge-covariant examples: the axis of a
plaquette (x; -mu, -nu), whose loop x -> x - mu -> x - mu - nu -> x - nu -> x uses no link with tail x.
The forces N_(x,mu) do depend on the links with tail x, so a frame solving (AF-1) is in general not of this class.

### Step 3: one plaquette, by hand (PROVED)

Sites x, x + mu, x + nu, w = x + mu + nu, all free; gauge U_1 = U_2 = U_3 = 1, U_4 = g^(-1), g = U_p = cos phi + s,
|s| = sin phi. Then N_1 = N_2 = beta s, N_3 = N_4 = - beta s (transported). (AF-1): n_(x+mu) . s = n_x . s = n_(x+nu) . s
(n_w is free: w has no outgoing link). A gauge-covariant vector at x is a function of g that is fixed by the
stabiliser of g, so n_x = + or - s/|s|: the only covariant frame is the axis, D n = 0. A plaquette is reducible; this
is the trivial case. Cost, with the Jacobian: d_l = 2 cot phi (1, 1, -1, -1) (the divergence of the field d/d phi for
the Haar density sin^2 phi), so jt = (beta sin phi - 2 cot phi)(1, 1, -1, -1) is conserved and

  Psi = - (d theta)_p (beta sin phi - 2 cot phi),      Q(theta) = E[Psi^2] = (d theta)_p^2 E[beta cos phi + 2/sin^2 phi].

Checks: beta = 0 gives 2 E[1/sin^2 phi] = 4; large beta gives about beta + 2 beta = 3 beta (in the Gaussian limit
E[1/r^2] = 1/sigma^2 in three dimensions). So the frame's singularity at s = 0 is integrable, and the Jacobian term
is of the same order beta as the action term: on one plaquette the form is a curl form with constant about 3 beta
against beta for U(1).

### Step 4: one cube (open, 8 free sites), by hand (PROVED)

Each site has at most 3 outgoing links. At the corner 000 there is no incoming link, so the Gauss law gives
N_1 + N_2 + N_3 = 0: the three outgoing forces are coplanar. At a site with two outgoing links they span a plane; with
one, a line. So at every site with an outgoing link there is a unit n_x orthogonal to all outgoing forces at x
(unique up to sign when the span is a plane), for instance n_000 = N_1 x N_2 / |N_1 x N_2|. With it **j = 0 on every
link**, so (AF-1) holds. It is gauge covariant because the forces are. The three plaquette holonomies at 000 do not
commute for almost every U, so the cube is non-reducible almost surely, and D n is not 0 (Lemma FR).
So: **on one cube an aligned frame exists on almost every configuration, and almost every configuration is
non-reducible.** Sentence L275 of row 1018 ("exists exactly on reducible configurations only") is false there.
What the cube does not show: its frame is of the kind "j = 0", which needs outgoing forces in a plane at each site.
In the bulk of a 4D lattice a site has 4 outgoing links with the single relation M_x = (incoming sum), and the four
forces span R^3 for almost every U, so j = 0 is not available. (In two dimensions it is: n = N_1 x N_2 normalised.)
With j = 0 the move theta n keeps the action to first order for every theta, and Psi = sum_l theta_l d_l is all Jacobian.
