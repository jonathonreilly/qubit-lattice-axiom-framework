# Repo search

Codex (GPT-6; dispatch names `gpt-6-astra/xhigh` at FINISH:807, but this
runtime does not expose a more specific serving-model ID),
2026-11-15. Research check at `d756e17a5e393f03ad5d937ce60bd76379e77081`;
not an audit, no status grant, no mass-gap claim. This check covers the
specified finite-volume reductions and the dichotomy assembly. It does not
prove their Wilson-model hypotheses, the continuum datum, or the RG chain.

The target-specific `prior/gap-zd-astra.md` is absent. The lead's general
`prior/repo-search-2026-11-08.md` addresses thirteen other targets. Its
record says main and PRs 10114, 10133, 10134, 10141 were searched. The task
and FINISH row 730 name no further “Repo prior work” hit. I did not repeat
that broad search. I checked the following primary passages instead:

| Hit | Source checked | Closeness and use |
|---|---|---|
| General digest's local-block hit | PR 10114 at `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md` 1–18, 90–173, fetched and read with `git show` | A positive one-time plaquette correlation; line 169 explicitly distinguishes it from a gap lower bound. No Casimir/seed equivalence supplied by this passage. Its header's strong-coupling result is a different endpoint; not rechecked here. |
| Existing thermal algebra | `gap-crux-restate.md` 29–45, 99–106, 170–219; `gap-mid-max.md` 142–148; `gap-seed-shape.md` 87–138 | These are the actual inputs, credited and reused in items 1–14. No new attack on their owners. |
| Earlier state-count converse, identified by row 727 | `gap-seed-limit.md` 208–234, especially N1–N3 at 214–226 | Corollary Z2 is a specialization: n=2a, theta=1/2, A_n=exp(64D(a)). N3 then has exactly the condition liminf D(a)/a<m_0/64. Claude's priority observation is right. |

The rules map was fetched from current main
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`; all mathematical verdicts
remain pinned to the requested checkout. Searches for the target, Casimir,
thermal sum, PHYS-SEED and Theorem ZD found no matching owner in
`open-registry.md`. The target is this missing cross-provider reading, not
a fresh proof of the already written reductions.

## Checkpoint and source boundary

- Source checkout remains pinned; work branch: `codex/gap-zd-astra-20261115`.
- Downloads made once, in the new directory `/tmp/sa-gap-zd-astra.FN3VlX`:
  outline, 32992 lines; complete account I, 166711 lines; source commit
  `31a47c543775`.
- Original verdicts 1–14 saved before opening `gap-phys-seed-check.md`.
- Claude comparison and dichotomy assembly completed below.
- Only this output file changed; no source, registry, status or audit edit.
- No mathematical run, numerical certificate, or computer-assisted proof.
- No commit or push. The report is left locally for the lead.

Credit for the outline/account: Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their text. Their conditional RG inputs build on
Tadeusz Balaban. Credit for the local reductions: Claude Fable 5.2, row 720;
for the later assembly: Claude Fable 5.2, row 1024.

The outline index README, relevant chunk rows and their neighbours, and
`obligations.md` were consulted. Searches for “Casimir”, “thermal sum” and
seed/gap combinations locate no indexed version of these reductions;
the Casimir hit in chunk 02 is the group Casimir in a different calculation.
Chunk 01:65–72, chunk 29:73–78 and obligations:21–28 point to the relevant
scope boundary. The bounded source reads SA588–599 and SA31871–31882 say
that polynomial decay does not establish a mass gap. They do not supply
the finite-volume equivalence checked here. CA-I2695–2710, located from
GOAL's scope discussion, likewise explicitly excludes a mass-gap assertion.
The `ca-4.12-4.19` README and targeted chunk search concern stage admission
and operator estimates, not this thermal criterion; none is imported.
These are bounded searches and source comparisons, not an absence theorem
about the whole account. No Balaban paper was needed or copied.

## Original verdicts, recorded before reading row 727

All line numbers below refer to the pinned checkout. `P` abbreviates
`gap-phys-seed.md`; `R` is `gap-crux-restate.md`; `H` is `gap-seed-shape.md`.
HOLDS means the stated implication from the named inputs. It asserts no
Wilson seed and supplies no audit standing. No verdict below uses a run.

### 1. Inputs and constants — HOLDS

R31–45 fixes the sign: F=log Z, f=inf F/volume, D=F−f volume≥0.
For any positive spectrum, normalize its power sum to one; increasing
the power decreases its norm. This proves Lemma A's side monotonicity,
including nonintegral ratios of integer side lengths. Also
sum λ_i^(2t)≤λ_0^t sum λ_i^t. These are exactly the two facts P uses.

The proof of Proposition Delta, `gap-mid-max.md` 144–146, has the right
sign: log λ_0(b³)≥fb³, while F(a,b³)≤(b/a)³F(a⁴). Their difference
is at most (b/a)³D(a). The lead note at line 10 retains this proposition.
The final gapless-model contrapositive additionally uses positivity of the
finitely many smaller-box gaps, from the simple top eigenvalue.

R174–219 supplies the two-direction crossing identity, its nonnegative
deficit, enlargement E', the recursion S, and S3'. In E', the reference
bulk constant depends on the other two sides; it cancels separately at
each application. It need not be common to the three applications.
The recursion follows from three enlargements and
sum r_i^(2t)≤(sum r_i^t)², with multiplicities retained. S3' brackets each
integer L between D and 2D; it does not use the false integer factorization
already corrected at R211.

H87–138 gives the shape conversions used below. At r=4 the exponent is
8 log(1+x²)+336 log(1+x³), so for x≤1/25 it is at most 21.44x².
For u≤0.034304, e^u≤(1+u/2)/(1−u/2)<1.03491, giving
phi(x)<22.2x² and 22.2/25<1. At r=2, enlargement at fixed time gives
(1+s)^64−1<0.0396<1/25 for s≤1/1650. These prove the two used lines.
For explicit hand bounds one may use
e^x−1≤x+x²/[2(1−x/3)] (0≤x<3), obtained from
(k+2)!≥2·3^k. At x=0.03904 this is below 0.0399;
at x=64/1650 it is below 0.0396. Thus no floating-point evaluation is
needed for the two decimal thresholds.

### 2. Lemma Z, P253–257 — HOLDS

The simple top eigenvalue gives 0≤r_i≤r_1<1. Multiply
r_i^(T−T_0)≤r_1^(T−T_0) by r_i^T_0 and sum. Proposition Delta bounds
log(1+S(T_0;b³)). Exponentiation preserves order. Every time and side
is in the stated domain, including T=T_0 and b=T_0.

### 3. Corollary Z1, P259–266 — HOLDS

T_0=b/4≥3 and T=b/2. The exponent is at most
64D(b/4)−bm(b³)/4≤−7.41. The discarded minus one only weakens the bound.
For a hand certificate of even the printed sharper bound:
sum_(k=0)^9 1/k! = 986410/362880 > 2.71828, hence
e²>7.38904, e⁴>54.5979, and e⁷>1096.625 by rational multiplication.
The terms through degree four of e^0.409 exceed 1.505209.
Their product exceeds 1650.64. Thus log(1650)<7.409<7.41.
The general-shape formula follows by substituting T_0=theta b/r,
with the implicit requirement that the displayed lattice times are integers
and T_0≥3. The rounded sufficient constants 44.5 and 25.8 have positive
slack against 6 log(1650) and 8 log(25), respectively.

### 4. Lemma Z', P268–272 — HOLDS

Lemma A(b) gives the initial upper bound 2F(T_0,b³)−F(2T_0,b³).
Increasing the three spatial sides gives
F(T_0,b³)≤rho³F(T_0⁴). Increasing the time from 2T_0 to b instead gives
F(2T_0,b³)≥(2/rho)F(b⁴). That term is subtracted, so this lower bound
has exactly the needed direction. The result is (2/rho)Phi_rho(T_0).
At rho=2 the second comparison is equality. No positivity of F is used.
The spectral tail argument is the one in item 2.

### 5. Corollary Z1' and count identity, P274–281 — HOLDS

The exponent is Phi_4(b/4)/2−bm(b³)/4≤−7.41. The same strict numerical
slack applies. Cancellation of f gives Phi_4(n)=256D(n)−D(4n).
For the infinite sum, its remainder is
256^(−K)D(4^K n)=n⁴[F((4^K n)⁴)/(4^K n)⁴−f]→0.
Indeed the cube density decreases to f: each fixed rectangular torus is
eventually dominated coordinatewise by these cubes. Thus both the bound
Phi_4≤256D and the telescoping identity hold. No thermodynamic limit is
needed to state or use C'_b itself.

### 6. Lemma Z3, P283–294 — HOLDS

Step 1: writing F(n,B)=ne(B)+g(n;B) cancels the ground-state term.
The four successive doublings have coefficients 8,4,2,1; all intermediate
F terms cancel. Since g≥0, d_i≤2g(n;B_i). The coefficients after this
bound sum to 16+8+4+2=30.

Step 2: start with S(D_k/2;D_k³)≤s_k. For each enlarged side h_i,
E' has exponent 2h_i/D_k<8, since h_i<4D_k. Their product is below
512. If h_i≤2D_k, their product is at most 64. The successive boxes
remain admissible; the fixed sides change only between applications.

Step 3: for D_k≤L<2D_k, both L and 2L lie in [D_k,4D_k).
The time L is larger than D_k/2, so g decreases. This gives
Phi(L)≤30·512s_k=15360s_k. At L=D_k it gives 30·64s_k=1920s_k.

Step 4: the density limit in item 5 with factor 16 gives the telescoping
series. The size 2^iL has index k+i, and s_(k+i)≤s_k.
Sum 16^(−i−1)=1/15. This gives 1024s_k, and, using the special bound
at every 2^iD_k, 128s_k. The case s=0 is immediate by the same bounds;
gap formulas involving log(1/q) then mean absence of excited spectrum.

### 7. Theorem ZD, P296–304 — HOLDS

- (A)→(B): 128q^(2^k)/5041→0 by item 6.
- (B)→(A): Proposition Delta gives the r=4 seed. Its recursion has
  22.2s'_0<22.2/25<1. After k steps, double the time only:
  N=2^(k+1)a, 2N=2^(k+2)a, and S(N;(2N)³)≤(s'_k)²→0.
- (A)→(D): item 6 bounds D at every large integer side; S3' gives
  a positive lower bound for m at every such side, hence bm is unbounded.
- (D)→(C),(C'): choose a sufficiently large multiple of four.
  The thresholds are respectively 256D_0+29.64 and 512D_0+29.64,
  since Phi_4(b/4)≤256D_0. Finite initial sizes do not cause
  unboundedness for finite positive box gaps. A rank-one box, if admitted
  as a degenerate case, already supplies a zero thermal seed.
- (C),(C')→(A): items 3 and 5 give the r=2 threshold. H138 enlarges
  the box from b to 2b at time b/2, giving r=4 with strict slack.
  Apply the preceding r=4 recursion and time doubling. All sizes are
  integers, and all times are at least three.

### 8. Corollary Z2, P306–307 — HOLDS

A strict liminf below m_0/64 supplies arbitrarily large a with
D(a)/a≤m_0/64−0.116/a. Multiplication by 256 gives slack
256·0.116=29.696>29.64. At b=4a this implies C_b.
Conversely, failure of every C_b gives
D(a)>m_0a/64−29.64/256>m_0a/64−0.12 for all sufficiently large a.
This remains a conditional converse, with a state-count hypothesis.

### 9. Theorem ZD-c, P311–320 — HOLDS AFTER CORRECTION

The equivalence holds. Replace the abbreviated second implication at P320
by the following, to retain its uniform strict margin:

> Choose L≥4L_0 in P with z^−(L)>256D_0+30. For all sufficiently
> large j, b_jm_j>256D_0+30 and D_j(b_j/4)≤D_0+10^(−3),
> where b_j=L/a_j. Consequently
> b_jm_j−256D_j(b_j/4)>29.744 and
> S_j(b_j/2;b_j³)≤exp(−7.436)<1/1650.
> The bound is independent of j, so its limsup is strictly below 1/1650.

The printed conclusion only states ≤1/1650; that inequality alone does
not imply the strict limsup definition. The existing constants repair it,
without a stronger premise. Alternatively pass through r=4 and a fixed
number of recursive steps to the threshold 1/5041.

For the other directions, fix a tail bound s_j≤s_*<1/5041, with
q'=5041s_*<1. If the starting threshold is 1/1650, the r=4 conversion
and a fixed number of steps give such an s_*, uniformly in j. Lemma Z3
then gives D^+(2^kl)≤1024q'^(2^k)/5041. S3' gives
z^−(L)≥2(L/l)log(1/q') for every admitted L≥l. This proves
(BDD-Delta), tail-unbounded (Z-UNB), and (PHYS-SEED-Delta).

Conversely a strict Delta seed gives a uniform r=4 seed by item 1, then
a uniform r=2 seed as in item 7. For (Z-SEED) with finite z^−(L), choose
eps>0 so that z^−(L)−eps>2(psi^+(L)+eps)+29.64; a fixed tail satisfies
C'_b with positive slack. If z^−(L)=+infinity, (Z-SEED) requires finite
psi^+(L); replace z^−(L)−eps by any finite number above
2(psi^+(L)+eps)+29.64 and then take a tail on which z_j exceeds it.
In either case the thermal bound has strict limsup below 1/1650.
From a physical seed, Phi_4≤256D(L/4) tends to zero along the tail,
while z^−(L) grows at least linearly. This gives (Z-SEED).
Only finitely many sizes are fixed before each j-limit; no uniformity in
all sizes at once is assumed. P is closed under the required doublings;
division by four is used only for L≥4L_0 or along a sufficiently late tail.

### 10. Corollary Z4, P322–323 — HOLDS AFTER CORRECTION

The displayed dichotomy is correct: one admissible C_b gives (A), then S3'.
Its last sentence drops the side and scale restrictions. Replace it by:

> At a coupling with no seed and D(a)≤D_0 for all a≥a_0, every
> periodic cube of side b≥max(12,4a_0), divisible by four, has an
> excited level strictly below (256D_0+29.64)/b above its ground state.

Failure of C_b is precisely this strict inequality. P322 supplies no such
bound with the same constant for smaller sides or arbitrary residues.

### 11. Lemma DIL, P344–349 — HOLDS

At finite volume F'=−6|n|abar_n and F''=Var(A)≥0. Also 0≤A≤12|n|,
so every normalized F is 12-Lipschitz, uniformly in the torus. Cube
densities converge pointwise to f; hence f is convex, 12-Lipschitz,
and f(0)=0. This justifies the integral at the endpoint zero, not merely
on compact subintervals of beta>0. A convex function has differing left
and right derivatives at at most countably many points. The fundamental
theorem for absolutely continuous functions gives the displayed identity.
Delta is locally absolutely continuous, so it is nondecreasing exactly
when its derivative is nonnegative almost everywhere. Thus the sign is
abar_inf−abar_n, as printed. In P351, the verbal plaquette comparison
must likewise be read almost everywhere, not at undefined derivatives.

### 12. Proposition MB, P353–363 — HOLDS

The identity D(n)=rho^(−4)[Phi_rho(n)+D(rho n)] is exact at fixed beta.
The first use of MONO compares the same integer torus rho L_0 nu at
beta(nu) and beta(rho nu); it does not compare different lattice sizes.
Thus M(nu)≤rho^(−4)[P_0+M(rho nu)]. Iteration gives a geometric sum
and a remainder at most rho^(−4i)A→0, by APR. Finally the same-torus
comparison at rho^kL_0nu yields the stated bound at the coarser coupling.
Every size is integral because n_0 and rho are integers. Neither this proof
nor item 11 establishes MONO or the account's supply of APR.

### 13. Corollary MB1, P365 — HOLDS AFTER CORRECTION

Make its inherited premises explicit:

> Under all hypotheses of Proposition MB, including APR and the geometric
> spacing sequence, a size L_1=4rho^kL_0 with
> z^−(L_1)>256P_0/(rho⁴−1)+30 gives a physical seed at L_1.

The proof uses MB's uniform bound at L_1/4 and item 9's strict-margin
argument. Unbounded z^− on these sizes supplies such an L_1.
For general rho this is a seed on the stated rho-based family; to identify
it with the particular dyadic P in ZD-c, require L_1 in that P (or define
the physical-seed predicate on a family containing these sizes).
[This originally requested restriction is withdrawn by the interpolation
argument in comparison point 4 below; APR remains necessary in the proof.]
APR cannot be deleted from the MB argument merely because its supplier
is discussed in P363. No RG supply is proved in this check.

### 14. Proposition NM, P375–378 — HOLDS

No seed at beta_t excludes (B) by item 7, so D(n;beta_t)>0.00061
for every n≥3. A seed at beta_1 and item 6 give
D(2^(k+1)N;beta_1)≤128q^(2^k)/5041<0.00061 eventually.
The integral in item 11 is then negative on [beta_t,beta_1]. Therefore
abar_n−abar_inf is positive on a set of positive measure; otherwise its
integral could not be positive. The claimed loss of monotonicity follows.
For a generalized model class the last clause requires the same
coupling-differentiation identity; spectral positivity alone says nothing
about a plaquette derivative. For Wilson normalization that identity was
proved in item 11. The comparison-model and numerical prose P367–374,
P378 is not used as evidence.

Original-verdict checkpoint: verdicts 1–14 were saved before opening
`gap-phys-seed-check.md`. The comparison below records subsequent changes
of judgment. During final proofreading the hand arithmetic in item 3 and
the extended-real case in item 9 were expanded without changing verdicts.

## Comparison with Claude's row 727

The complete 137-line check was opened only after the checkpoint above.
Its provenance is Claude Opus 5.5, high effort, at `258009092`.
The following covers every verdict in our overlapping scope.

| Statement | Row 727 lines | Resolution |
|---|---|---|
| Z, Z1, other-shape remark | 42–46 | Agree: HOLDS with integral admissible times. |
| Z', Z1', count identity | 48–54 | Agree on both theorems. One missing factor in the check's telescoping explanation is corrected below. |
| Z3 | 56–60 | Agree on all four steps and all constants. |
| ZD | 62–69 | Agree on all five equivalent forms. |
| Z2 | 71, 106 | Agree mathematically. Claude is right to credit the prior state-count criterion; see the repo-search addendum. |
| ZD-c | 73–78 | Same mathematical verdict and exactly the same strict bound exp(−7.436). My original label requested proof completion; Claude already writes that completion at line 75. No new mathematical defect is claimed. |
| Z4 | 80 | Agree on the repair. Claude also explicitly puts max(4a_0,12) in the first dichotomy clause, which my original item 10 should also do. |
| DIL | 84 | Agree. The endpoint requires justification; the uniform Lipschitz argument above supplies it. |
| MB | 86–92 | Agree, including the essential vanishing remainder. |
| MB1 | 94 | Agree that APR must be retained. My initially requested size-family restriction is unnecessary after enlargement by E'; Claude's APR repair suffices on admissible common lattice spacings. |
| NM | 96 | Agree on the theorem. Claude is right that its printed dependency mark omits ZD and hence SH; DIL also supplies the last clause. |

The differences, with who is right, are these:

1. **ZD-c label, not mathematics.** Row 727:75 explicitly supplies the
   strict-margin step absent from P320's final bound. Claude's HOLDS is
   right for the theorem. Item 9 above records the same proof completion
   as HOLDS AFTER CORRECTION of the written proof. There is no disagreement
   about the equivalence, its constants, or its hypotheses.
2. **Telescoping normalization.** Row 727:54 writes
   `256^(-K)D(4^K n) = F/abs − f`. The right side needs the factor n⁴.
   Item 5 has the correct equality. Codex is right about that equality;
   Claude's zero-remainder conclusion remains right, since n is fixed.
3. **Z4's starting domain.** My original item 10 called the displayed
   dichotomy correct without explicitly repairing its first range as well.
   Claude is more precise at row 727:80: in *both* places use
   `b divisible by 4, b≥max(4a_0,12)`. This excludes undefined D(1), D(2).
   Adopt Claude's complete repair. For a_0≥3 the maximum is redundant.
4. **MB1's sizes: my initial restriction was unnecessary.** A size
   4rho^kL_0 need not belong to a preassigned dyadic P. But a uniform seed
   at that size gives a uniform 1/5041 seed at some size ell. For any large
   L in P choose k with 2^k ell≤L<2^(k+1)ell. The proof of S3' gives
   S_j(2^k ell/(2a_j);(L/a_j)³)≤q'^(2^k)/71. Since L/2≥2^k ell/2,
   the same bound holds at time L/(2a_j). Choose fixed L large enough
   that it is below 1/5041. All these lattice times must be admissible,
   as in S0; in MB one can always take the compatible base l_1=4L_0.
   Thus the literal dyadic seed follows too. Claude's APR repair is right;
   the extra restriction I initially requested is withdrawn. This is a
   check of the necessary size interpolation, not a new hypothesis.

No other in-scope mathematical disagreement was found. The tiny decimal
roundings in the check are not used here as exact identities or certificates.
Its verdicts on Sections 1.1.5, 1.3 and Lemma FLOW lie outside this task;
they receive no new verdict here.

## Check of the dichotomy assembly

Here `Q` denotes `gap-dichotomy.md`. The three requested assembly steps
are checked below. The CE/OM/CR/TRI package is a named input to form 2;
this is not a new complete check of that package. Its source statements
and proofs at `gap-compact-rigidity-max.md` 131–196, 223–243, 350–352,
394–396 were inspected for the exact contracts used. Repairs at
`gap-compact-rigidity-check-opus.md` 129–172, 233–242 were compared with Q.
In particular, Omega belongs to this family, its bound is fixed, and its
admissible sequences have both j_i→infinity and k_i→infinity.

### 15. Quoted ZD-c, Q144–146 and Q222–233 — HOLDS

Q222–233 spells out the four implications. Q228 uses the strict
exp(−7.436) bound, so item 9's proof-completion issue is already resolved.
Q229–230 must be read as the two-stage conversion *and a fixed number of
recursive steps*, as its citation to P304 says. Enlargement alone only
reaches the r=4 threshold. All these steps stay in P.

### 16. Partition (I), (II), (III), Q148–156, Q240–242 — HOLDS

Write B=(BDD-Delta), U=(Z-UNB). Item 9 gives I iff B and U.
The three predicates are therefore B and U, not B, B and not U.
They are exhaustive and pairwise disjoint by elementary logic.
The negation of B is exactly:

> For every L_0 in P and every finite C, some L in P with L≥L_0
> satisfies D^+(L)>C.

Thus Q151 requires unboundedness on *every tail*. An isolated infinite
value at a size excluded by a later tail would not by itself prove (II).
The parenthesis at Q151–152 must not be read as that stronger assertion.

### 17. Bound in (III), Q153–156 and Q243–245 — HOLDS

Fix any bound (L_0,D_0). If one L≥4L_0 in P had
z^−(L)>256D_0+30, item 9's single-size argument would give I.
Then U would hold, contrary to III. Therefore z^−(L)≤256D_0+30
at every such L. Conversely this finite tail bound excludes U, so with
B it is an equivalent version of III.

For each fixed L and eps>0, the definition of liminf supplies infinitely
many j with z_j(L)<256D_0+30+eps. Since the physical energy is
m_j/a_j=z_j(L)/L, Q155–156 has the correct units and quantifiers.
This is not a bound for all sufficiently fine lattices, nor a lower bound
of order 1/L, nor a single subsequence asserted to work for all L at once.

### 18. (I) iff (W), Q119, Q158, Q246–247 — HOLDS AFTER CORRECTION

The intended wall is equivalent to I, but Q119 has a domain omission.
It permits L=l_1 or L=2l_1. A bound on the sizes *of P* from L/4 on
then does not bound D^+(L/4), since L/4 is outside P. The first unsupported
use is Q246: its invocation of Step 2 needs precisely that missing bound.
The same implicit step occurs in check 1019:63.

Replace Q119 by this exact version:

> (W): there are a bound (L_0,D_0) of (BDD-Delta) and L in P with
> L≥4L_0 and z^−(L)>256D_0+30.

Then W→I is item 9. Conversely I gives B and U, so choose L≥4L_0
above the same threshold. This proves I→W. The repair does not change
the intended seed-equivalent wall. It fixes the domain of its stated
sufficient criterion. No counterexample to the unqualified wall is claimed.
The partition and item 17 already impose L≥4L_0 and do not need this repair.

### 19. Quoted Z4, Q160–162 and Q251–252 — HOLDS

Q includes the full corrected range b≥max(4a_0,12), b divisible by four.
One threshold crossing gives a seed and then S3'. If no crossing occurs,
branch G holds. The two branches cannot both occur: branch M makes bm
unbounded along those multiples, whereas branch G bounds it.
This is a statement at one coupling; item 17 is its liminf analogue,
with the larger constant 30 and an infinite-subsequence conclusion.

### 20. Use of CE and OM, Q166–177 and Q256–269 — HOLDS GIVEN those inputs

Q applies CE with the actual family and the actual (BDD-Delta) bound.
It retains the integer-time domain through S0. Q267–269 explicitly adds
j≥n to the diagonal selecting the closed set Omega. Q174–175 distinguishes
two directions: a physical seed empties every Omega(D_0); the converse
uses D_0 from a bound of B. These are exactly the source's repaired clauses.
The centre grading and numerical constants of the critical element are
not needed to infer nonemptiness or recurrence; no extra cross-provider
verdict on those internal proofs is supplied here.

### 21. Theorem CR's logical assembly, Q179–182 and Q273–275 — HOLDS AFTER CORRECTION of W

Use item 18's definition of W. Under B with D_0 a bound, CE and OM give
I iff Omega(D_0) is empty. An empty Omega has no recurrent element.
A nonempty Omega has one by OM(d), giving the converse. An empty Omega
also admits the unique empty continuous function, for which the last
condition is vacuous. If Omega is nonempty, OM(c) contradicts that
condition for every continuous Lambda. Thus all five statements agree.
This checks their logical linkage, conditional on CE and OM; it neither
proves B nor excludes any critical element of this family.

### 22. Form 2 and the link, Q184–194 and Q279–284 — HOLDS GIVEN CE and OM

If I and II fail, B holds and I fails. For every bound (L_0,D_0), CE
produces an admissible sequence, CE(ii) produces a member of Omega(D_0),
and OM(d) produces a uniformly recurrent member. This proves III'.
I excludes II by item 9. I excludes III' because OM(b)'s seed direction
empties Omega(D_0) for *every* D_0. No exclusion of II with III' is used.

Now assume not II. If III holds, the preceding construction proves III'
for every B-bound. If III' holds for even one D_0, I is impossible by
OM(b), so B and not I imply not U and hence III. CE(ii) makes each
resulting element critical. This proves both directions of the requested
link with exactly the quantifiers in Q192–194. It does not require W,
so item 18's wording issue does not invalidate the link.

### 23. Explanatory scope, Q381–386 — HOLDS AFTER CORRECTION

Q382–383 says the scaled gap is bounded “for every box” and that the
excitation energy is “of the order of 1/L”. This drops the liminf scope
of Q154–156 and suggests a two-sided estimate. Replace those sentences by:

> In case (III), the limiting upper Casimir free energy is bounded on
> the dyadic tail. For each admitted size L≥4L_0 and every eps>0,
> infinitely many lattices have a first excitation with physical energy
> below (256D_0+30+eps)/L. The theorem gives no positive lower bound
> for that excitation and does not assert this upper bound for every j.

The plain-language gap statement at Q386 must retain Q204–211's continuum
datum, positive-time convergence and totality, not existence alone.
Those inputs, their supply, and the full limit-state leg G2/G3 were not
checked in this task. G1's lattice inequality at Q198–200 follows directly
from S3' and Z3 with N_j=l/(2a_j) and one q'<1.

## Final verdicts and limits

| Numbered statement | Final verdict |
|---|---|
| Z; Z1; Z'; Z1'; Z3 | HOLDS, given the named inputs. |
| ZD | HOLDS, all five forms. |
| Z2 | HOLDS; credits N3 of row 700 as the earlier state-count converse. |
| ZD-c | HOLDS AFTER CORRECTION of the abbreviated proof, using the already available strict bound exp(−7.436); equivalence unchanged. Row 727 already supplies that completion. |
| Z4 | HOLDS AFTER CORRECTION: both clauses retain b divisible by four and b≥max(4a_0,12). |
| DIL; MB | HOLDS; DIL includes endpoint absolute continuity; MB retains APR. |
| MB1 | HOLDS AFTER CORRECTION: retain APR and the other MB hypotheses. No additional size-family restriction is needed. |
| NM | HOLDS; its dependency mark must include ZD/SH and DIL. |
| Form 1 partition; bound in (III) | HOLDS under S0 and the stated engine. |
| (I) iff (W); CR's W clause | HOLDS AFTER CORRECTION of W's domain, as in item 18. |
| Form 2; link between forms | HOLDS GIVEN CE and OM with their stated repairs. This is an assembly check, not a full new check of CE/OM. |
| Plain-language explanation of (III) | HOLDS AFTER CORRECTION: a liminf upper bound on the specified tail, not a two-sided energy estimate or a bound for every cutoff. |

No named core implication FAILS after these explicit repairs. The new
wall-domain issue is a missing premise in the printed proof, not a
counterexample to Wilson theory. No uniform Casimir bound, unbounded scaled
gap, monotonicity in beta, APR supply from the account, or continuum theory
has been proved here. No claim that (II) or (III) is false is made.

Recovery: the file contains the original verdicts, their later resolutions,
the source revision and exact source ranges. The next action is for the lead
to apply the stated wording repairs if desired; this run changes no other
lane file. Text and git checks are bookkeeping only. No numeric, symbolic,
Lean, or other computer-assisted proof step was run, and no proof status was
awarded. The full CE/OM/CR internal arguments, the transfer-operator
construction, RG supply, comparison models and continuum reconstruction
remain outside this check's verdict scope.

RESULT: Row 730 research check by Codex: ZD and ZD-c hold conditionally, with the explicit strict-margin proof completion; Z4 and MB1 need the recorded domain/APR repairs; the dichotomy partition and bound in (III) hold, and its two forms agree given the repaired CE/OM inputs; repair W to require a bound reaching L/4, and retain the liminf scope in the prose; no mass gap, no audit or status grant, no computer-assisted proof; report saved locally, uncommitted and unpushed.
