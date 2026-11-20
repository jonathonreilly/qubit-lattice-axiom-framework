lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T20:41Z

# gap-mini-solve-y-opus: mass gap for four-dimensional SU(2) Yang-Mills

Queue row 1241 of FINISH.md. Started 2026-11-20T08:41Z (date -u). Worker: Claude Opus 5.5, max effort, Mac mini worker 2. Branch claude/ym4d-hard-route at c941f01ed.

Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Step 0. Reading log (reading only; no new claim; written 08:47Z by date -u)

Read at this pin (c941f01ed): GOAL.md in full; FINISH.md L1-90 and L296-356 (state, how we work, queue rules,
joining, working efficiently, rules), row 1241 (this row) in full, the full texts of rows 1218-1227 and the RESULT
cells of rows 1228-1246; `parts/gap.md` L1-104 (state of attack, methods 1-36, lead rules); `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `library/gap-solve9-astra62.md` L130-160 (row 1161: (N-phys) and its proof frame);
`library/gap-mini-branch-fable.md` L295-315 (row 1179: (N-phys) restated, Theorem BP); `library/gap-mini-solve-j-fable.md`
Step 8 (row 1200); the sibling files of rows 1234 (v-opus) and 1243 (z-opus) as they stood at 08:42Z.

Where the problem stands on file (cited, not re-derived):

1. Consumer side. Beside the premises of Sussman and Alpoge's complete account (the T0 chain), the Jaffe-Witten gap
   on the account's tr F^2 sector follows from one lattice estimate, (N-phys) (row 1179 Theorem BP, check 1183; row
   1225 Theorem E-N, check 1232 HOLDS AFTER CORRECTION).
2. (N-phys) (row 1161 L146-148; row 1179 L304-310): at one physical side L, for every cutoff j >= j_0, some u_j with
   3 <= u_j <= n_j/K has s_+(u_j; n_j^3) <= 1/2, where s_+ is the centre-neutral excited trace of the vacuum-normalised
   periodic transfer matrix on the spatial cube n_j^3 and K is an existence constant fixed first.
3. Ultraviolet carry. Rows 1233, 1237, 1238 reduce the all-cutoff form to a one-cutoff seed plus named statements of
   the account ((UNIV-K) sub-items; checks 1240 and 1242). Modulo these, the crux is a finite seed for Wilson SU(2) at
   one fixed coupling inside the account's window (row 1225, ARGUED; row 1229).
4. Engines. About 45 route families are screened with named failing steps (rows 1189, 1194, 1199, 1200, 1229, 1237;
   methods 1-36 of `parts/gap.md`). The 2D pinned-cell engine has no 4D gauge form (rows 1011-1016, 1228). Uniform
   curvature or Poincare bounds force a trivial limit (row 1237 Proposition UNI, check 1240).
5. Published work (row 1218): A (Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford, Singha Roy) gives a
   stronger full-thermal one-scale seed with a proved ascent; B (the first four authors) gives cube-dynamics criteria
   and a weak-coupling Poincare bound for coarse straight-path variables (Corollary 166), not selective by row 1220;
   C (Zeng Chunping) gives common-rate criteria and a conditional tunnelling route. None proves the Wilson estimate.

Rows running now on the same plain brief: 1234 (v-opus), 1243 (z-opus), 1244 (aa-opus), 1246 (solve28-astra62).
This row will name its item in Step 1 and keep it distinct from theirs as they stood when read.

## Step 1. How best to attack it (judgement, ARGUED; written 09:15Z by date -u)

**1.1 What a proof has to supply (cited).** For SU(2) along the account's trajectory, the gap clause needs exactly
one lattice input beside the T0 chain: (N-phys) (Step 0, items 1-3). On R^4 the vacuum sector carries no centre
charge: electric flux sectors exist only on tori. So the Jaffe-Witten gap is the **neutral** half. Every flux-half
tool (twist ratios, (X), the theta channel, Route T) is an instrument for the neutral half, not a proof of it. This
matches row 1161 ("the gap target needs no flux clause") and row 1200 Step 5.4; it is not new.

**1.2 Why no tool on file crosses the band (ARGUED; each clause cited).**
- A seed has to sit where the running coupling is of order one (rows 998 6b, 1219, 1225). With no computed
  certificate (GOAL.md), it must come from a structure that holds at every coupling.
- Structures that hold at every coupling and are on file: reflection positivity, gauge invariance, the Z_2 one-form
  symmetry, positive character coefficients, the loop (Schwinger-Dyson) equations with their bracket term (row 1011
  Proposition W), and convexity in beta. Each tool built from them has a named failing step in the tables of rows
  1189, 1194, 1199, 1229 and 1237, and methods 1-36 of `parts/gap.md`.
- The two posted 2D proofs (OpenAI; Ding, Huang and Yang; read in row 1007) cross their band with a continuous
  global non-abelian symmetry acting on all integration variables, or with an N-copy loop soup. Pure 4D SU(2) has
  neither on gauge-invariant data (row 1011 Lemma CEN; row 1016 CEN+). Both 2D proofs control the **charged**
  (spin) sector; their neutral sector comes from association of the O(4) ferromagnet (OpenAI Section 3.11, read in
  row 1009). In 4D association of link coordinates is empty by Elitzur's theorem (row 1194 2.2).
- So in 4D the crux has two layers. The flux half would need a band-crossing engine; the twist-index engine has a
  one-loop margin but no proof through the band (row 1200, (X)). The neutral half has no engine with a margin at
  all (row 1200 Step 5.4), and no conversion from charged to neutral decay without association is known in any
  non-abelian model (the lane's (SING); smallest open member K_3 of row 1194).

**1.3 Choice for this row.** Re-screening routes would repeat rows 1189-1238. I take the deepest layer, the neutral
half without association, in a model where the charged half is supplied: the cycle models K_N of row 1194 (N O(4)
sheets on a 2D base with product one; K_2 is the O(4) model at 2 beta; K_3 is the smallest open member). Row 1194
tried three ways (association, conditional sheets, dual gas); each stopped at the neutral response of one twisted
sheet. This row tries a fourth way, stated in Step 2, and records where it stops. Row 1194 (L226) notes that even a
proof of (K_3-N) is a mechanism, not a step of the chain; I accept that and say so in the result.

What would change on success: the lane would have its first neutral conversion with no association, which is the
missing kind of step in 1.2. On failure: the first failing step of a fourth way, so the next row does not repeat it.

## Step 2. A fourth way on (K_3-N), and where it stops (written 09:24Z by date -u)

Setting and statement as in row 1194 (`library/gap-mini-solve-e-fable.md` 3.1, 5.2): planes k_0, k_1, k_2 in
SU(2)^B on a rectangle B, sheets m_p = k_p^(-1) k_(p+1), density proportional to prod_p exp(beta E(m_p)),
E(m) = sum over bonds f = <y, y'> of <m(y), m(y')>, <a, b> = (1/2) tr(a b^(-1)). (K_3-N): exponential decay of
Cov(F, G) for F, G functions of m_0 on two bonds, invariant under m_0 -> a m_0 b, uniformly in B.

**2.1 The gauge-fixed form (PROVED, elementary; a renaming of row 1194 Lemma D1, so not new).** The density depends
on the planes only through the m_p, which are invariant under k_p(y) -> g(y) k_p(y) for one g(y) per site. Fix
k_0 = 1 and write A = k_1, B = k_2, and for a bond f put a_f = A(y) A(y')^(-1), b_f = B(y) B(y')^(-1). Then
m_0 = A, m_1 = A^(-1) B, m_2 = B^(-1), and

  <m_0(y), m_0(y')> = Re a_f,   <m_2(y), m_2(y')> = Re b_f,   <m_1(y), m_1(y')> = (1/2) tr(A^(-1) B B'^(-1) A') = <b_f, a_f>.

So the bond weight is exp(beta [<1, a_f> + <1, b_f> + <a_f, b_f>]) = exp((beta/2) |1 + a_f + b_f|^2 - 3 beta/2), where
1, a_f, b_f are read as unit vectors of R^4. The fields a, b are flat SU(2) connections on B (products of their
values around each plaquette of B are 1), and every pair of flat connections on the rectangle arises this way.
This is the bilinear form exp((beta/2)|Psi(y) Psi(y')^*|^2) of D1 with Psi = (1, A, B). The neutral observable of
(K_3-N) is a function of Re a_f. The residual rigid group is (a_0, a_1, a_2) acting by A -> a_0 A a_1^(-1),
B -> a_0 B a_2^(-1).

Every manipulation I tried from this form lands on a way of row 1194: integrating out B given A gives the twisted
sheet of C4 (e) (Way 2); the Gaussian identity for exp((beta/2)|.|^2) gives D1 (the fourth form there); the
character expansion of the three-vector weight gives the flux gas of C2 (Way 3); and Re a_f + Re b_f + <a_f, b_f> is
not of Ginibre type (D2; Way 1). So this is not a fourth way. It is recorded only because the flat-connection
reading makes the next check short.

**2.2 What the conditional frustration does at Gaussian order (GUIDE; a perturbative reading, not a bound).**
Row 1194 Way 2 stops because the twist field of the conditional sheet is frustrated by commutators of order 1/beta per
plaquette, of order one on blocks of side about beta, far below the mixing length s(beta). One might hope that this
frustration itself kills neutral correlations at scale beta. It does not, at least not at Gaussian order. Write
A = exp(X), B = exp(Y) with X, Y small in su(2) = R^3 and d the lattice gradient. To second order,
Re a_f = 1 - |dX_f|^2/2, Re b_f = 1 - |dY_f|^2/2, <a_f, b_f> = 1 - |dX_f - dY_f|^2/2, so the weight is
exp(-(beta/2) sum_f Q(dX_f, dY_f)) with Q(u, v) = |u|^2 + |v|^2 + |u - v|^2. Q has matrix [[2, -1], [-1, 2]] (times
the identity on R^3), eigenvalues 1 and 3: six massless Gaussian modes, with no frustration term at this order
(the commutators enter at third order). The neutral observable Re a_f = 1 - |dX_f|^2/2 then has covariance of order
1/(beta^2 r^4) at distance r: a power law on every scale where the expansion is valid. So the neutral sector of K_3
is massless to all orders of the spin-wave expansion, and (K_3-N) is a statement at the non-perturbative scale
s(beta), like the singlet gap of the O(4) model itself. The commutator frustration of Way 2 is a cubic effect
in this expansion. It is not a mechanism for decay at scale beta.

**2.3 How the posted 2D proofs reach the neutral sector, and why neither route exists here (ARGUED; cited).**
- OpenAI's O(3) continuum paper reaches the full transfer gap through a ferromagnetic correlation inequality: "the
  spin two-point function detects the full transfer gap (covariance of even monomials bounded by the square of the
  largest spin correlation, on any finite ferromagnetic graph)" (row 1010, `library/prior/gap-o3-continuum-rg-read-opus.md`
  L210). The O(4) paper reaches singlets by association (row 1009; row 1194 2.2).
- K_3 has neither: its energy is not of Ginibre type in sheet or plane coordinates (D2, Lemma HF of row 1188). For
  4D Wilson SU(2), association of link coordinates is empty by Elitzur's theorem (row 1194 2.2), and positive
  surface expansions grow with the volume (method 35). In 4D the charged objects are Wilson lines, not local
  fields, so even the form of the 2D inequality has no direct analogue.

**2.4 Stop.** By the stop rule of row 1194 2.3 (three ways failed at one statement), and since the attempted fourth
way is a renaming, I stop on (K_3-N). The statement where it stops is (N-tw) of row 1194 5.4, unchanged. What 2.2
adds: (N-tw) cannot be reached by a perturbative frustration argument; it needs the same non-perturbative input at
scale s(beta) as the O(4) singlet gap, with no ferromagnetic inequality to carry it.

