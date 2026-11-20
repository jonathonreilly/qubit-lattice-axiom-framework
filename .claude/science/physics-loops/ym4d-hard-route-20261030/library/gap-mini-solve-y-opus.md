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
  (spin) sector. Ding, Huang and Yang and OpenAI's O(n) paper do not claim the neutral sector (row 1007: "A full
  transfer gap ... requires a separate argument"). Where OpenAI reaches it, in the O(4) paper (Section 3.11, row
  1009) and the O(3) continuum paper (row 1010 L210), it uses association or a ferromagnetic correlation
  inequality. In 4D association of link coordinates is empty by Elitzur's theorem (row 1194 2.2).
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
is massless at Gaussian order (and, by the usual reading of 2D asymptotically free sigma models, at every finite
order; RECALLED, not checked here), and (K_3-N) is a statement at the non-perturbative scale s(beta), like the
singlet gap of the O(4) model itself. The commutator frustration of Way 2 is a cubic effect
in this expansion. It is not a mechanism for decay at scale beta.

**2.3 How the posted 2D proofs reach the neutral sector, and why neither route exists here (ARGUED; cited).**
- OpenAI's O(3) continuum paper reaches the full transfer gap through a ferromagnetic correlation inequality: "the
  spin two-point function detects the full transfer gap (covariance of even monomials bounded by the square of the
  largest spin correlation, on any finite ferromagnetic graph)" (row 1010, `library/prior/gap-o3-continuum-rg-read-opus.md`
  L210). The O(4) paper reaches singlets by association (row 1009; row 1194 2.2). Its exact form, as read in row
  1009 (`library/prior/gap-o4-pinned-cell-read-opus.md` L175-187): write q = (cos alpha z, sin alpha w) with z, w on
  the circle; given alpha the two circle sectors are independent XY models with non-negative couplings, the alpha law
  is associated, and Ginibre and random-cluster FKG finish the covariance bound (3.67); "the untwisted zero-field
  ferromagnet ... This restriction is essential". In the gauge-fixed form of 2.1 the K_3 bond energy
  Re a_f + Re b_f + <a_f, b_f> has its third term (1/2) tr(A A'^(-1) B' B^(-1)) quartic in the site quaternions, and in
  the same Hopf coordinates its phase expansion has signs that no constant shift makes non-negative (row 1194 D2).
  Choosing the middle sheet m_1 = A^(-1) B as a coordinate instead of B gives E(m_0) + E(m_1) + E(m_0 m_1), the form
  D2 treats, and conditioning on m_0 gives the twisted sheet of Way 2. I found no third coordinate system.
- K_3 has neither: its energy is not of Ginibre type in sheet or plane coordinates (D2, Lemma HF of row 1188). For
  4D Wilson SU(2), association of link coordinates is empty by Elitzur's theorem (row 1194 2.2), and positive
  surface expansions grow with the volume (method 35). In 4D the charged objects are Wilson lines, not local
  fields, so even the form of the 2D inequality has no direct analogue.

**2.4 Stop.** By the stop rule of row 1194 2.3 (three ways failed at one statement), and since the attempted fourth
way is a renaming, I stop on (K_3-N). The statement where it stops is (N-tw) of row 1194 5.4, unchanged. What 2.2
adds: (N-tw) cannot be reached by a perturbative frustration argument; it needs the same non-perturbative input at
scale s(beta) as the O(4) singlet gap, with no ferromagnetic inequality to carry it.

## Step 3. A bookkeeping finding for the lead and for check row 1242 (READ; written 09:25Z by date -u)

Row 1233 (`library/gap-mini-solve-u-opus.md` L140 and RESULT) lists "(DET)'s (ID-a), (ID-b), (I-loc)" among the
remaining inputs of its one-cutoff carry. It cites none of rows 990, 993, 994 (grep of that file for 990, 993, 994,
idab, iloc: no match). Those rows already treat the three items. Their standing on file, from their RESULT lines:

- (I-loc): row 990 (`library/gap-iloc-opus.md`) PROVED it for the repository's step form at U = 1 and ARGUED it for
  the account's block map; row 993 item (2) (`library/gap-idab-opus.md`) PROVED the block-map identity (CMP 109
  (0.3), (0.10)-(0.12) are SA's QC1-QC3), closing that case by Lemma LR; the cross-provider check of row 987
  (`library/gap-det-check-astra.md` L282, L393) gives (I-loc) HOLDS AFTER CORRECTION as a supplied reading.
- (ID-a), (ID-b): row 993 PROVED (ID-a) with one identification ARGUED (that the unprinted z^(k)(c) of CMP 119 (3.33)
  is the pivot factor computed there, which is L^9 at U = 1) and (ID-b) up to one ARGUED normalization (r4); the gpt-6-astra check (`library/gap-idab-check-astra.md`, RESULT) gives HOLDS AFTER
  CORRECTION for both, conditional on the named background and inverse-existence inputs; row 994 (same provider)
  finds no FAILS and reduces (r4) to one positive scalar that cancels in (DET), given that SA's display is in one set
  of coordinates.
- Still open there, as those rows record: pr-lay W; the full-E_0 torus comparison (the identification "the
  account's E_0 is reading (i)" FAILS as justified, `library/gap-idab-check-astra.md` L196-201; row 993 notes that
  (DET) needs only a bound); and the background and inverse-existence inputs named in that check.

So the accurate list of (DET)-side inputs for row 1233's Proposition 3.7 is: pr-lay W, the E_0 torus bound, and the
named background and inverse-existence inputs, not (ID-a), (ID-b), (I-loc) as open items. This is a citation
correction, not a new result. I make no claim on (EDGE) or on the 9.1 hypotheses; check row 1242 is reading them.

## Step 4. Results, what stays open, and a note for the lead (written 2026-11-20T09:27Z by date -u)

No numeric run was made (free memory was 56 percent at 09:06Z; no job was needed). No subagent. No outside source
was fetched. Rule 0a: `library/open-core.md` has no line on (K_3-N) or (N-tw) (grep at the time of this step);
the FINISH rows that treat them are 1110, 1115, 1194 (cited in Steps 1-2).

### 4.1 Table

| Item | Label | Where | New? |
|---|---|---|---|
| The Jaffe-Witten gap is the neutral half on R^4; flux-half engines are instruments only | ARGUED | 1.1 | no: row 1161, row 1200 5.4 |
| Where the posted 2D work reaches the neutral sector (OpenAI's O(4) and O(3) papers), it uses association or a ferromagnetic inequality; neither exists for K_3 or 4D Wilson SU(2) | ARGUED (cited) | 1.2, 2.3 | the pairing of the two facts is this row's; each fact is on file (rows 1009, 1010 L210, 1194 2.2, 1188 HF) |
| Gauge-fixed form of K_3: two flat SU(2) connections a, b on B with bond weight exp((beta/2)abs(1 + a_f + b_f)^2) | PROVED (elementary) | 2.1 | no: a renaming of row 1194 Lemma D1 |
| At Gaussian order K_3 has six massless modes, quadratic form Q(u, v) = abs(u)^2 + abs(v)^2 + abs(u - v)^2 with eigenvalues 1, 3, and neutral covariance of order 1/(beta^2 r^4); the commutator frustration of Way 2 is cubic | GUIDE (perturbative) | 2.2 | not on file in this form; it adds to row 1194 Way 2 that the frustration is not a decay mechanism at scale beta |
| (K_3-N), (N-tw) | OPEN | 2.4 | stop rule of row 1194 2.3 applies; the fourth way tried here is a renaming |
| Row 1233's list of remaining inputs omits rows 990, 993, 994 (and the astra checks of 987 and 993) on (I-loc), (ID-a), (ID-b) | READ (citation correction) | 3 | yes, as bookkeeping |
| (N-phys), the one-cutoff seed, the Jaffe-Witten gap | OPEN | - | - |

### 4.2 What stays open

- (N-phys), equivalently (modulo the ultraviolet carry) a finite seed for Wilson SU(2) at one coupling in the
  account's window. No route found here; Step 1 gives the reasons, which agree with rows 1219, 1225, 1229, 1233, 1237.
- The neutral half without association, in its smallest instance (K_3-N), stopping at (N-tw) of row 1194.
- The account's premises (T0 chain), and for the one-cutoff route the inputs of row 1233 as corrected in Step 3.

### 4.3 For the lead (evidence only; this row edits no other file)

1. Rows 1188-1238 and this one all stop at the same place. The neutral half has no engine with a margin (row 1200
   5.4), and Step 2.2 adds that in the smallest sheet model the obstruction is non-perturbative at the mixing
   length, not a small-scale frustration effect. A further plain-brief row is likely to rebuild this map again.
2. If crux budget continues, the cleanest open problem I can name is 2D: a singlet (neutral) gap for a 2D
   asymptotically free sigma model with a transitive non-abelian rigid group and no ferromagnetic inequality, with
   K_3 of row 1194 as the smallest case. Its charged half is supplied (row 1194 E1, given OpenAI's estimate (3.61)).
   A mechanism there would be the kind of step 4D needs; a failure there is cheaper to diagnose than in 4D. This is a
   suggestion, not a claim that the problem is easier than it looks.
3. Check row 1242 may use Step 3 when it reaches row 1233's list of remaining inputs.

### 4.4 Credits

Jaffe and Witten (the problem). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (the
account whose premises the gap chain reads; nothing of theirs is used in a step here). Balaban (CMP papers, through
rows 990-994). OpenAI (the posted 2D O(3), O(4) and O(n) proofs, as read in rows 1007, 1009, 1010); Ding, Huang and
Yang (the second posted 2D proof, read in row 1007). Bhattacharjee, Bhattacharya, Lockwood, Romanov, Sessford and
Singha Roy, and Zeng Chunping (the published sources of row 1218, used only through that reading). The lane rows
cited above, in particular row 1194 (Claude Fable 5.2: the cycle models K_N, Lemmas C0-C4, D1, D2, E1, (N-tw)),
rows 1011 and 1016 (Lemma CEN, CEN+), row 1132 and 1135 (route (A)), rows 990, 993, 994 and their gpt-6-astra checks.

RESULT: Row 1241 (Claude Opus 5.5 max, Mac mini worker 2, 08:41Z-09:28Z by date -u; author only, checked by no one; no numeric run, no subagent): the mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing is disproved; (N-phys) stays OPEN with no route beyond the record (Step 1, ARGUED: on R^4 the gap is the neutral half; where the posted 2D work reaches the neutral sector (OpenAI's O(4) and O(3) papers) it uses association or a ferromagnetic inequality, and neither exists for 4D Wilson SU(2) or for the sheet models). Worked item: the smallest neutral lemma without association, (K_3-N) of row 1194; the attempted fourth way (a gauge-fixed form with two flat SU(2) connections and bond weight exp((beta/2)abs(1 + a + b)^2), PROVED, elementary) is a renaming of row 1194 Lemma D1, so the stop rule applies at (N-tw); GUIDE (spin-wave order): K_3 has six massless modes with an unfrustrated quadratic form and neutral covariance of order 1/(beta^2 r^4), so the commutator frustration of row 1194 Way 2 is a cubic effect and not a decay mechanism at scale beta. READ (citation correction for the lead and check 1242): row 1233's remaining inputs (I-loc), (ID-a), (ID-b) are treated by rows 990, 993, 994 and the gpt-6-astra checks of rows 987 and 993; the open (DET)-side items are pr-lay W, the E_0 torus bound and the named background and inverse-existence inputs. OPEN: (N-phys), (K_3-N), (N-tw), the account's premises, the Jaffe-Witten gap. Output library/gap-mini-solve-y-opus.md.
