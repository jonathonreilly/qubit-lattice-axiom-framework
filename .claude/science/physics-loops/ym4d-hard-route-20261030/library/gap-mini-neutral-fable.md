lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T09:58Z

# gap-mini-neutral-fable: the one-cube physical neutral upper bound

FINISH row 1180 (`gap-mini-neutral-fable`). Status marks: PROVED, ARGUED, GUIDE, OPEN. No subagents.

**Provenance of this file.** An earlier run of this item (Claude Opus 5.5 at max effort, started
2026-11-19T21:48Z by its own `date -u`, pinned at commit 0d6295dd9) wrote only a header and the plan
below; its header lines were `lead: anthropic/claude-opus-5-5/max mac-mini-worker` and
`lease_until: 2026-11-20T09:48Z`. This session (Claude Fable 5.2 at max effort, started
2026-11-19T21:58Z by `date -u`, pinned at commit 3b1d5e14f on branch `claude/ym4d-hard-route`)
keeps that plan and continues from it. All mathematical content below is from this session.

## Plan (earlier run, kept; written before reading the chain)

1. Read the row's required sources: `library/gap-council-synthesis.md`, `parts/gap.md` (methods 1-36,
   route registry), RESULT lines of FINISH rows 1143-1177, and the defining texts of the "one-cube
   physical neutral upper bound" in rows 1161, 1175, 1177 (`gap-solve9-astra62.md`,
   `gap-solve16-astra62.md`, `gap-solve17-astra62.md`).
2. Write down the exact statement of the bound (call it N1) with every quantifier, and record what is
   already on file about it (grep open-core.md and FINISH rows; stop if another row covers it).
3. Attack: try to prove N1, or disprove it, or prove the strongest true statement toward it; for
   every route tried, record the precise obstruction.
4. One RESULT line at the end.

Each step below is appended as it finishes.

## Step log (this session)

### Step 1. The exact statement, and what is on file (reading only; no new claim)

Written 2026-11-19T22:04Z (`date -u`).

**Setting (row 1161, `gap-solve9-astra62.md` L13-63; credit: the positive transfer and trace identity GL8 of
Sussman and Alpoge, with Claude and Codex as authors of their text; Balaban for the ultraviolet trajectory).**
Wilson SU(2) at coupling beta on the periodic spatial cube n^3, 4 | n. F is the symmetric magnetic sandwich
(the positive transfer operator on gauge-invariant functions of the spatial links), lambda_0 = ||F||, G = (Z/2)^3
the centre flips. X_{m,q}(u) = Tr_q (F_m/lambda_0)^u for static magnetic twist m and electric character q, in
units of the periodic vacuum. The periodic neutral excited sum is

    s(u; n) = X_{0,0}(u) - 1 = sum over excited neutral levels of (lambda_i/lambda_0)^u.

**(N-phys), the one-cube physical neutral upper bound** (row 1161 L146-148 and L215; in the wording of row 1179,
`gap-mini-branch-fable.md` Section 6): there is one admissible physical side L and an index j_0 such that for
every j >= j_0, with n_j = L/a_j and 4 | n_j, there is an integer u_j with 3 <= u_j <= n_j/K and

    s_j(u_j; n_j) <= 1/2.

K is the aspect of row 1161's finite-aspect statement; the explicit version is K = 512 with n_j >= 2^70
(row 1161 L215). Rows 1175 and 1177 read the same premise (row 1175 L59 "row 1161's short-period periodic
neutral premise at one permitted physical side"; row 1177 RESULT "given the one-cube physical neutral bound").
So the three rows need one statement, (N-phys).

**In plain words.** With H_n = -log(F/lambda_0) on the cube n^3, (N-phys) says Tr_neutral exp(-u H_n) <= 3/2 at
u = n/512: the centre-neutral thermal partition function at temperature 512/L on the box L^3 is at most 3/2 in
vacuum units, uniformly in the cutoff. GUIDE: for a free massless field the same trace is exp(c 512^3); for a
theory with lightest neutral mass m it is about 512^3 (x/2 pi)^(3/2) exp(-x) with x = m L/512, so the bound asks
for m L of order 10^4. It is a statement at one large physical size, not a small-volume statement.

**What is on file about (N-phys)** (each line read at this pin):

1. Consumer, PROVED in row 1161 (checked by Opus 5.5 max in row 1162): (N-phys) gives a cutoff-uniform
   Pfaffian seed S_kappa < 2^(-18) at time n/2, and one of two flux alternatives (9).
2. Row 1179 (`gap-mini-branch-fable.md` Theorem BP, PROVED GIVEN rows 697, 700, 731, 1161; checked by no one):
   (N-phys) alone gives a cutoff-uniform gap on the centre-blind sector and, with the continuum datum, the
   Jaffe-Witten gap clause in both flux alternatives. So (N-phys) is the whole gap clause in this lane.
3. Necessity, PROVED in row 1161 L150: (W) implies (N-phys) on all large dyadic sizes.
4. Equivalent forms over physical sizes, PROVED in row 1161 (26) and L389-400: a cutoff-uniform Pfaffian seed
   iff S^+_ev(L) -> 0 on dyadic sizes iff (S^+_ev bounded and the neutral dimensionless gap z^-_+ unbounded),
   where S^+_ev(L) = limsup_j s_j(n/2; n) is the neutral excited sum at aspect two.
5. Lower bounds, PROVED in row 1161 (17), (19): s(u) >= c n^3 exp(-C u) at every beta >= 1, so u = o(log n)
   is excluded. Row 1153: the short-period trace is a free gluon gas.
6. Abstract obstructions, PROVED: the sign-product comparison (row 1161 L375), the finite-moment construction
   (row 1161 L404), the local neutral spectator (row 1175 (29)), the centre-spectator principle of the council
   (rows 1128-1134), Lemma PT and Proposition NP (rows 998, 1003).
7. The glue-half engine: rows 1124-1125 ((GLUE-STEP), found-again, no first leaf), row 731 ((G_ev), (EV-STEP)),
   route RE. No published theorem gives an order-one four-dimensional non-abelian glue-half seed (row 1124).

**Rule 0a.** `grep -i neutral library/open-core.md` returns nothing. FINISH rows that name the neutral bound:
1161-1177 (the chain that states it as OPEN), 1178 (`gap-solve18-astra62`, the chain's general continuation on
(W), running now), 1179 (branch selection, not this bound), 1181 (free method). No other row is assigned the
neutral bound; row 1180 (this row) is. I proceed.

**Kind of statement (lead rule W2).** (N-phys) is selective: it is false for the free photon and for compact
U(1) in its Coulomb phase (massless neutral states at every size), and it is violated by a product with a
massless or slowly cooling neutral spectator (item 6). A proof must read the non-abelian group at a scale of
order one in the coupling. It is (K-flow) in the lane's terms if proved along the trajectory, (K-one) if proved
at one bare coupling with a carry to finer cutoffs.

### Step 2. What (N-phys) says at each fixed coupling (corollaries of statements on file)

Written 2026-11-19T22:38Z (`date -u`). Nothing in this step closes (N-phys).

**2.1 Fixed-coupling form (PROVED GIVEN row 1161 L215 and L335; a corollary, no new input).** Let nu(beta)
be the least n with 4 | n, n >= 2^70 and s(floor(n/512); n) <= 1/2 at the bare coupling beta, and nu = infinity
if there is none. Row 1161 L335 proves this chain at a fixed coupling: the test at (beta, n) gives a Pfaffian
seed at n (L215); Theorem S-w propagates it to the sides 2^k n; Proposition B3 enlarges the cube 512-fold at a
fixed multiplier on the log excess; so the test holds again at the sides 512 * 2^k * n for every k >= k_0. The
integer k_0 depends only on the seed margin 2^(-18) and on the multiplier (1024)^3, so it is absolute. I did
not compute it. Hence, on the lane's dyadic grid (row 1161 L150, L389):

    (N-phys) at some admissible L   iff   limsup_j a_j nu'(beta_j) < infinity,

where nu' is nu restricted to grid sizes. The "only if" part is the definition. The "if" part is the chain.

In words, (N-phys) is two statements.
- (a) Every fine coupling beta_j has a finite seed size. This is a lattice gap for centre-neutral states at
  arbitrarily weak coupling.
- (b) The seed size grows no faster than 1/a_j. This is a lower bound of asymptotic-scaling type on that gap.

**2.2 Subsequences (ARGUED).** Row 1161 L148 and row 1179 Theorem BP apply the premise one cutoff at a time. If
the continuum datum is a limit along a subsequence of cutoffs, the premise is needed along that subsequence
only. Then the gap clause for that limit point needs liminf_j a_j nu'(beta_j) < infinity only. I did not check
the continuum hypotheses of row 1179 ((H2), (TOT), (P4)) for this reading. So it stays ARGUED.

**2.3 Size of the task (reading).** By row 1179 Theorem BP (ii), (N-phys) gives at every fine coupling beta_j a
centre-even gap of at least M_* a_j on every large periodic cube. Row 1124 found no published theorem that gives
a gap or a thermal seed for four-dimensional Wilson SU(2) at a coupling of order one. So a proof of (N-phys)
contains a new theorem at each beta_j. This measures the task. It is not an obstruction.

**2.4 Where the bound can first hold (GUIDE; no proof reads this).** For a dilute gas of one scalar of mass m on
the box L^3 at temperature K/L, log(1 + s) is about K^3 (x/2 pi)^(3/2) exp(-x) with x = m L/K. With K = 512 this
is below log(3/2) from x of about 21, so from m L of about 1.1 x 10^4. With the lane's guide value m = 3.78
sqrt(sigma) (row 1063) this is L sqrt(sigma) of about 2900, and the temperature 512/L is about a quarter of the
deconfinement temperature. Below that size the short direction is hot, and log(1 + s) is of the order of
512^3. So (N-phys) is a statement about one very large cube. No small-volume expansion reaches it.

### Step 3. Routes tried, with the first failing step of each

Written 2026-11-19T22:38Z (`date -u`). Each route below was worked by hand in this session until it reached a
precise failing step. For each, the obstruction is stated, and the place where the lane already has it is
named. I found no route whose first failing step is not on file. No line below is a new result.

**R1. Count by reflection positivity, then decay by one gap.** Chain: s(u; n) <= (count at an earlier time v)
x exp(-m_+ (u - v)). The ultraviolet bounds give an extensive count, log(1 + s(v; n)) <= c_0 (L/l)^3, with l
the first-passage scale and v a_j = tau_0 fixed. Arithmetic (PROVED, elementary): with a cutoff-uniform gap M,
the chain gives s <= 1/2 at u = n/K only if M L/K >= c_0 (L/l)^3 + log 2 + M tau_0 for some L >= l. The left
side minus the first term on the right is concave in L, with slope M/K - 3 c_0/l at L = l. So a solution with
L >= l needs M l >= K min(c_0 + log 2, 3 c_0), which is at least K c_0. The count must therefore have a density
scale of at least K c_0 correlation lengths. At the first-passage scale M l is small. So the count has to be
an infrared input.
On file: row 1153 L393-397 (the exact first gap applied to the whole short-period multiplicity diverges); row
1161 L185-190 (the same chain with (BDD-Delta) as the count); row 1135 (a gap does not bound the torus excess
in general: the line-spin model; `parts/gap.md` L188).

**R2. The thermodynamic form.** Reading the torus n^3 x u in the other three frames gives
1 + S_per(u; n^3) <= exp(n^3 u [e(n^3) - e(u^3)]) (1 + S_per(n; u^3)), with e(B) the vacuum energy per site of
the box B, and e(n^3) >= e(n, n, u) >= e(n, u, u) >= e(u^3) when u divides n. I derived this by hand and then
found it in the lane: it is Lemma Z and Lemma Z' of row 720 (`gap-phys-seed.md` L253-279) with Proposition B3
(`gap-seed-shape.md` L72-77), in the variable F(n)/abs(n). First failing step: the excess of the periodic torus
of side u must be below log(3/2)/K^3 uniformly in the cutoff. That is a periodic seed at side u. It is stronger
than (N-phys).

**R3. Integration in the coupling at a fixed lattice shape.** d/d beta of log(1 + S_per(u; n)) is the sum over
the plaquettes of n^3 x u of the plaquette mean at period u minus its mean in the vacuum. The bound is true at
small beta. First failing step: a signed bound on this response at couplings of order one. On file: row 1145,
inequality (24) ("the real form of (W)", on the path in the spatial coupling), with its proved obstructions to
continuation, and rows 1147-1151; for the path in the isotropic coupling, row 1161 L325-339 (the sets P, M, N
and the fixed-coupling obstruction to a change of branch).

**R4. Operator inequalities (Golden-Thompson, min-max against the electric operator).** First failing step
(ARGUED): each compares Tr F^u with a trace that does not carry the vacuum energy of F, so the bound exceeds
lambda_0^u by a factor exp(c u n^3). I did not prove the extensive loss for all beta: a Holder bound over 24
classes of link-disjoint plaquettes is too weak at large beta. On file in kind, not in this form: method 35
(`parts/gap.md` L69); row 1145 (absolute summation).

**R5. Crossing at the symmetric torus without the premise.** A scale-invariant spectrum satisfies crossing and
positivity in all four frames at every size. So crossing gives no upper bound on s without a seed. On file: the
massless floor (row 988, Lemma FLOOR; method 26); the test table rows "free photon" and "product with a massless
factor" (`parts/gap.md` L296-297).

**R6. A selective seed at weak coupling on thin or twisted boxes.** With a twist through two short sides the
gluon modes have no zero momentum, so the box has a gap of order 1/(short side) at weak coupling, and compact
U(1) has none. First failing step: no engine carries a seed from a box with short sides to a cube, and doubling a
twisted side removes the twist. On file: Route T and (AC'-lat), rows 678-687 (`gap-ac-lat.md`); the council,
2c (`gap-council-synthesis.md` L54-59).

**R7. Curvature of the group at the lattice scale.** A Bakry-Emery bound with the Ricci curvature of SU(2)
would give a gap of order 1/beta in lattice units. That contradicts asymptotic scaling, so the Hessian of the
log of the vacuum must cancel the curvature term at low momentum (ARGUED). On file: method 31 (rows 957, 968);
row 1128, Proposition G1.

**R8. One coupling, then a carry to finer cutoffs.** In the form of 2.1: a seed at one beta_J and
nu(beta_(j+1)) <= 2 nu(beta_j) from J on. First failing step: the carry needs the thermal trace at a fixed
physical shape to converge as the cutoff is removed, with an error o(1) in the total. The ultraviolet bounds
give errors per unit physical volume. On file: row 978 (no carrier; the carry is (NOCRIT) of row 709 plus a
climb), with the correction of its check.

**R9. The count from the gap.** First failing step: a uniform gap does not give a bounded count in the class.
On file: row 1135 (line-spin model; sufficient extra input liminf D^+(L)/L below m_0/64); the hypothesis (DS-W)
of row 691 (`parts/gap.md`, route registry).

