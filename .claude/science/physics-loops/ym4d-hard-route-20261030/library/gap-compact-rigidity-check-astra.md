# Repo search

Written by Codex (GPT-6; exact model variant and effort are not
exposed in this session), checking source commit
`f4960e6ba194a8986bc35eeacb9cd629227762a3`. Research text, not an audit;
no status grant and no mass-gap claim. The filename is the assigned lane
identifier, not evidence of a model variant.

The target-specific prior map is absent. The lead's November 8 digest
concerns earlier hard-route suppliers; its transfer-correlation hit is
related background, not this compactness/recurrence argument. The registry
has no match for compact-rigidity or gap-dichotomy. Specific source checks
and their limits are recorded below.

Scope: row 1017, Sections 3.1–3.7 and 6.1, including UF, CE, OM, CR,
TRI, LV, PT-inf and SI. Upstream analytic hypotheses remain hypotheses.
No continuum construction, physical seed, mass gap, numerical proof,
formal verification or status change is covered.

## Check sequence and checkpoint

1. Read the pinned statements and their necessary definitions.
2. Check CR and the extraction/recurrence interfaces first.
3. Record my verdicts on every requested statement before reading row 1019.
4. Read row 1019 and repaired (W), and resolve each disagreement by line.
5. Check the form-2 consumer and finalize one RESULT line.

Downloaded Sussman–Alpoge sources once at `31a47c543775` into the fresh
scratch directory `/tmp/sa-gap-compact-rigidity-check-astra.6VrmSQ/`.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text. Their work supplies context and named inputs, not an
unconditional proof of the claims under check.

## Source checks and limits

The lead's `prior/repo-search-2026-11-08.md` records searches of main and
PRs 10114, 10133, 10134 and 10141. It predates this target. Its closest
outside-lane hit is the older soft-route
`MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`. I fetched PR 10114 at
`f76f6c649cff7dffbab664d8976e680e8f287fe9` and read that passage and
its scope at 1–10. It proves a one-time plaquette correlation comparison;
it neither constructs the present limit set nor proves rigidity. Credit
that prior Codex construction; no part is rederived here. The digest's
other targets concern background, covariance and history suppliers, not
the present scalar torus limits. This is a bounded comparison, not a
fresh absence theorem over all branches.

Main's workflow map and its rules were read at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`. The user's specified research
note and verdict vocabulary govern this output; no audit or status
machinery was run. No named target-specific prior-work hit was supplied
in the task beyond the lane files being checked.

The SA index README, matching chunk rows and neighbouring rows were used
before source excerpts. `chunk-01.md:60–70` and `obligations.md:17–24`
lead to outline 527–563 and 588–599. The former preserves positivity
only when all moment-form entries converge; the latter explicitly
separates polynomial decay from a gap. Neither is a compactness theorem
for these torus traces. The CA 4.12–4.19 index README and
`chunk-11.md:155–170` lead to CA-I 56584–56630: a diagonal extraction
of couplings at fixed depth, conditional on clause (0). That is a
related compactness method, not the two-index, no-seed limit set here.
These are existing results of Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. No new proof of them is claimed.
No Balaban paper or further literature theorem enters this check.

Below, R means `gap-compact-rigidity-max.md`, P means
`gap-phys-seed.md`, and S means `gap-crux-restate.md`, all at the pinned
checkout. Line references are to those unchanged files. I read
R131–398, S29–45 and S170–219, P247–328, and the repaired (W) at
`gap-zd-astra.md:403–420`. Theorem S, Z3, ZD-c and SH remain named
inputs, not newly certified upstream results. The checks below verify
their uses. No numerical, machine-enumeration or computer-assisted proof
was used; tools only read, fetch and write text.

## Original verdicts, written before opening row 1019

This section records my own reading before `gap-compact-rigidity-check-opus.md`
was opened. The task already disclosed that it contains scope repairs;
their text and verdicts were not read. The repaired (W) from the separate
ZD check was read, as required.

### 1. Definitions, R133–158 — HOLDS AFTER CORRECTION

Use integral physical times in the finite data: take units with
`u_j/4` an integer at least 3 eventually, as in P311, or discard every
initial scale at which an evaluated time is not an integer at least 3.
R147 only asserts `u_j≥3`; R151 at `k=0,b=1` otherwise asks for
`S_j(u_j/2;u_j^3)`. This is not defined, for example, at `u_j=3`.
All extraction arguments are eventual and survive this correction.

R133–143: (E2) makes the top eigenvalue positive and every trace used
finite. Normalize by it. Dominated convergence, dominated at time 3,
gives `S(k;B)→0`. Thus `E_0>0` would contradict `Delta(k,B)≥0`
for large k. The normalization and `E_0≤0` are correct.
Although E2 need only imply summability of the cubes of the eigenvalues,
the uses of Theorem S here require only traces at times at least 3.
Its spectral inequalities extend to this domain; summability at time 1
is not needed in its algebra.

R145–156 define a countable coordinate space and eventual inequalities.
Keep both `j_i→∞` and `k_i→∞`. R158 is a definition, not a statement
that an eternal function comes from the specified trajectory. Below,
Omega always means limits from that one trajectory with that one bound.

### 2. Lemma UF, R162–166 — HOLDS

The domain correction in item 1 is understood. Failure of the weaker
1/5041 seed follows from failure of PHYS-SEED. Conversely a seed at
the alternative SH threshold must first be converted uniformly to
the 1/5041 seed, as P320 states.

Here is an exact check of the strict margin in R164. Set `t=1/5041`
and `F(x)=((1+x)^64−1)^2`. The series for the exponential gives
`exp(y)≤1/(1−y)` for `0≤y<1`. Hence

`F(t)≤(64/4977)^2<t`, since `64·71=4544<4977` and `5041=71^2`.

More generally `F(x)≤5041x^2` for `0≤x≤t`. At x=0 this is immediate;
for `0<x≤t` use `((1+x)^64−1)/x≤64/(1−64t)<71`.
Seed sizes therefore form an upper tail. If their first size were
eventually bounded by L, the thermal sum at 2L would have limsup
at most `F(t)<t`, contrary to the hypothesis. For each i infinitely
many j have first seed beyond `2^i`. Choosing these j increasingly
gives the stated simultaneous eventual lower bounds. R166 is a
fixed-coupling interpretation only; no continuum gap is inferred.

### 3. Theorem CE(i)(a), R170,180 — HOLDS

For a constant family with no seed anywhere, every sufficiently dilated
fixed dyadic size is above `a_0`. H1 and H2 then hold. Its j-coordinate
can be set to i; only the scale coordinate changes the datum.

### 4. Theorem CE(i)(b), R170,180 — HOLDS

Put physical units `l_1=1`. UF supplies an infinite subsequence whose
first seed tends to infinity. At stage i fix `k_i=2i+i_0`, choosing
`i_0≥0` with `2^i_0≥L_0`. There are finitely many physical sizes
`2^(k_i+m)`, `|m|≤i`; each is at least `L_0`. The limsup bound
makes H1 hold eventually at all of them simultaneously. The UF
subsequence still contains arbitrarily large indices with first seed
beyond `2^(k_i+i)`. Choose one beyond the previous index. Thus no
interchange of a limsup with infinitely many sizes occurs. Use
`i(m)=max(1,|m|)` in the last sentence of R180.

### 5. Theorem CE(ii), extraction, R172,182–184 — HOLDS

Multiplying one side uses the elementary trace power inequality and
subtracts the same volume term f. Repeating it gives
`0≤Delta_i(x)≤C(x)`. At a fixed `(T,B)`, one ground-level summand
gives `e_0^i(B)≥−C(T,B)/T`, while item 1 gives the upper bound 0.
Every higher level has this lower bound. The one-point compactification
at `+∞` is therefore compact for each level coordinate. There are
countably many size and rank coordinates, so a diagonal subsequence
exists. Finite initial domain failures are discarded for each coordinate.

### 6. Theorem CE(ii)(a), R174,182,190 — HOLDS

The four-side permutation equalities pass to the limit. The final
bound uses `D_0`, rather than `D_0+1`, because H1's error tends to zero.
The bound has exactly the aspect ratio `product(x)/min(x)^4`.

### 7. Theorem CE(ii)(b), R175,186–192 — HOLDS

At time `T/2` the number of levels at most E is bounded by
`exp(TE/2+C(T/2,B))`. With the integer cutoff R(E) of R186,
the tail at time T is bounded by

`exp(−TE/2+C(T/2,B))`.

This bound holds for finite partial tails of the limit, then for the
whole limit tail by increasing partial sums. The finite head converges
termwise, including levels escaping to infinity. Let E tend to infinity.
This proves equality of the full traces, not merely a lower bound.
The finite ground-level bound prevents loss of the whole spectrum.
The normalized trace identity in R192 then proves convergence of S.
Multiplicity remains integral because the converging list retains each
rank; coincident finite ranks are counted separately. Infinitely many
coincident finite ranks would contradict the same trace bound.

This is positivity of the transfer trace in each direction. It does
not give reflection positivity for an observable field or a complete
continuum theory. R204 and R221 must be read with that restriction.

### 8. Theorem CE(ii)(c), R176,192 — HOLDS

The three displayed inequalities are closed inequalities in the
coordinates just shown to converge. Theorem S uses finite S values;
the Delta bound uses exponentials of finite values. For the general
sentence, read “closed inequalities in finitely many convergent
coordinates,” not an arbitrary inequality involving a discontinuous
function or subtraction of two infinities. These are precisely the
engine inequalities used here. Strict inequalities need not persist.

### 9. Theorem CE(ii)(d), R177,194 — HOLDS

H1 gives `D_*(b)≤D_0`; H2 and convergence of S give `s_*(b)≥t`.
Applying the displayed Delta estimate at time `b/2` gives
`t≤exp(8D_*(b/2))−1`. Relabel b/2 to obtain the lower bound
at every dyadic scale. The gap estimate at times b/4 and b/2 is

`s_i(b)≤exp(64D_i(b/4)−z_i(b)/4)`.

Thus `z_i(b)≤256D_i(b/4)+4log5041`. This bounds the first excited
level on cubes, so it cannot escape to infinity. Pass to the limit.

The two printed decimal bounds admit short hand checks. Since
`log(1+x)>x/(1+x)` for x>0,
`d_min>1/40336>247/10^7`; the last comparison is
`40336·247=9,962,992<10^7`.
For the other bound, the atanh series gives
`log2<842/1215+1/6804<6932/10000`.
The alternating logarithm series gives
`log(71/64)<7/64−49/8192+343/786432=81655/786432<13/125`.
Hence `4log5041=8log71<8(6·0.6932+0.104)=34.1056<34.11`.
These are rational estimates, not computer evaluations.

### 10. Theorem CE(ii)(e), R178,196 — HOLDS AFTER CORRECTION

Explicitly assume A4: commuting centre involutions, a common
eigenbasis with the transfer operator, and an even simple finite-data
vacuum. E1–E3 alone do not define a twist or centre action.
Under A4 each rank has a joint sign triple. Diagonal extraction makes
these triples eventually constant rank by rank. The signed tail is
bounded by the unsigned tail in item 7. This proves the displayed
twisted trace identity. Twist quotients can tend to zero; use [0,1]
for their compact limit range. Only the distinguished rank-0 level
is forced even; other levels may merge with it and carry other signs.
The grading need not be faithful and is not an action on observables.

### 11. Proposition OM(a), R225,227,233 — HOLDS AFTER CORRECTION

Add `j≥n` to the diagonal choice in R233. It is needed for the
definition of admissibility, just as `k≥n` is. For each n one can
also choose the original sequence index large enough that its H1
error is at most 1/n. The resulting sequence approaches E on every
fixed coordinate and satisfies H1–H2 on every fixed scale window.
Thus Omega is closed in the compact countable product. Shifting k
by +1 or −1 preserves admissibility, with finite initial terms removed.
The coordinate permutation sigma and its inverse are continuous.

### 12. Proposition OM(b), R228,234 — HOLDS

The extraction theorem proves the first equivalence. Under a fixed
BDD-Delta bound, failure of PHYS-SEED gives a sequence by CE(i)(b).
In the other direction, fix a seed at physical l with a uniform
margin q<1. At scale `2^p l`, Theorem S gives `S≤q^(2^p)/5041`
for every sufficiently large j, uniformly in p. Along an admissible
sequence `2^k_i b/l` is a nonnegative integral power of 2 eventually,
and its exponent tends to infinity. This contradicts H2 even at one
fixed b. This direction needs no BDD bound.

### 13. Proposition OM(c), R229,235 — HOLDS

There is also a shorter proof: take a minimizer E of the continuous
real function Lambda on compact nonempty Omega. Since sigma E is
in Omega, `Lambda(sigma E)≥Lambda(E)`. A maximizer gives the opposite
sign. Taking `Lambda(E)=D_E(1)` proves the stated stall. The source's
uniform-decrement proof also works. Different functionals may have
different stall elements; no common element for all functionals is claimed.

### 14. Proposition OM(d), R230,236 — HOLDS

A nested chain of nonempty closed invariant sets has nonempty
intersection, so a minimal such set M exists. Every full orbit in M
is dense. A finite cover by translates of a neighbourhood U of E
therefore supplies, for every integer t, a return at `t+n_l`, with
`|n_l|≤N`. Every interval of `2N+1` consecutive integers contains a
return. This proves bounded gaps. The numerical phrase “at most 2N”
in R236 should use a positive integer bound, e.g. `2N+1`, to cover N=0.
This does not alter the proposition's stated conclusion.

### 15. Proposition OM(e), R231,237 — HOLDS

For an arbitrary uniformly recurrent E, bounded-gap returns give
times `n_i→∞` with `sigma^n_i E→E`. The nonincreasing bounded
sequence `Lambda(sigma^n E)` has a limit; these returns make it
equal to `Lambda(E)`. Thus every forward value equals that value.
Each negative translate is also uniformly recurrent, giving equality
on the whole orbit. Continuity gives equality on its closure. This
proves constancy of Lambda, not that E itself is a fixed point.

### 16. Theorem CR, R241–249 — HOLDS AFTER CORRECTION

Fix one trajectory, its physical dyadic grid P, and a BDD-Delta
bound `(L_0,D_0)`. Define `Omega=Omega_Z(D_0)` only from its
admissible sequences. Use the repaired wall:

> (W) There exist a BDD-Delta bound `(L_0,D_0)` and `L in P`
> with `L≥4L_0` and `z^−(L)>256D_0+30`.

For any fixed BDD bound, the equivalent fixed-bound version asks
for such an L above that bound's threshold. PHYS-SEED gives it for
every such bound, since the physical dimensionless gap grows without
bound on the tail. No assertion involves all abstract critical elements.

Check each arrow at R243:

1. W gives a uniform seed: choose a positive margin below the strict
   excess `z^−(L)−256D_0−30`. For all large j the finite gap is
   above the required threshold while
   `D_j(L/(4a_j))≤D_0+epsilon`. Choose epsilon so the total error
   is less than the margin plus `30−29.64`. Corollary Z1 and the
   fixed SH conversion give PHYS-SEED. The condition `L≥4L_0`
   is exactly what permits this D bound.
2. PHYS-SEED gives W: P320 supplies a uniform q<1, bounded D on
   the tail, and `z^−(L)≥2(L/l)log(1/q)`. Choose L large enough.
3. PHYS-SEED iff Omega is empty is item 12.
4. Empty Omega has no recurrent element. Nonempty Omega contains
   one by item 14. These prove (3) iff (4).
5. Empty Omega satisfies (5), for example with its empty zero
   function. If Omega is nonempty, any continuous Lambda has a
   stall by item 13, so (5) is false. These prove (3) iff (5).

No rate of strict descent is needed. Compactness supplies a uniform
decrement if a continuous strict descent exists on a nonempty Omega;
that is already impossible. This is an equivalence, not a rigidity proof.

The explanatory inference in R245(ii) **FAILS**: OM(e) does not make
an element fixed when a monotone exists. A two-cycle with constant
Lambda is a compact dynamical counterexample. Replace that clause by:
“A continuous nonincreasing Lambda is constant on each recurrent orbit
closure; this need not make the datum fixed.” R247's caution is correct.

### 17. Corollary TRI, R350–354 — HOLDS AFTER CORRECTION

Replace (III) by: “For some finite D_0, the limit set
`Omega_Z(D_0)` of this family contains a uniformly recurrent element.”
If I fails and a BDD bound exists, CE and OM supply III for that bound.
If I holds, Z3 excludes II, and item 12 excludes III for every finite
D_0. II and III are not asserted disjoint. Without the trajectory
restriction, R253's abstract constants would make III hold even for
a seeded family, contradicting the exclusion sentence in R350.

### 18. Lemma LV, R394–398 — HOLDS

For a finite lowest level a and T tending to infinity through dyadic
values, multiply the trace by `exp(Ta)`. Every strictly higher term
tends to zero, dominated by the summable shifted trace at one fixed
positive time. The limit is exactly the finite multiplicity at a.
Two different lowest levels give incompatible limits. Subtract the
common block and repeat. If no finite levels remain, pad both lists
with infinity. This proves uniqueness including finite-rank spectra.

For continuity on Omega, the uniform local trace bounds give compact
extended-real coordinate intervals as in item 5. From any sequence
converging in Delta, every subsequence has a further spectrally
convergent subsequence. The tail argument identifies its trace with
the limiting Delta, and uniqueness identifies every rank. Hence the
whole sequence converges in each spectral coordinate. The finite
ground energy gives continuity of S. The first gap on cubes is finite
by item 9, so `s_*(1),z_*(1)` are real continuous functions on Omega.
Outside cubes use the extended topology for levels that may be infinity.

### 19. Lemma PT-inf, R257–262 — HOLDS AFTER CORRECTION

Require a common blow-down sequence with both `j_i→∞` and `k_i→∞`,
and pointwise finite limits on every dyadic torus. The finite product
identities are the cited PT input: free-energy densities add, traces
multiply, and relative spectral levels form a tensor-sum multiset.
The limiting traces multiply too. Nonnegative double sums give
`1+S_*=(1+S_*^1)(1+S_*^2)`. Levels are tensor sums with
multiplicity, sorted and padded by infinity, by LV.

**(i) HOLDS** on this domain. The second D is nonnegative; the first
factor supplies the lower critical bound. Upper bounds add. The
product thermal sum is at least the first one. Its gap is the smaller
factor gap, so the first factor's upper gap bound is at most the
desired bound with `D_*^1+D_*^2`. This includes merged ground levels.

**(ii) HOLDS** on this domain, with a uniform seed of the second
family. Fix its physical seed l and margin q<1. At fixed dyadic b,
write `2^k_i b=2^p_i l`, where `p_i→∞`. Z3 gives
`D_i^2(b)≤1024q^(2^p_i)/5041→0`. The aspect-ratio bound then
gives `Delta_*^2(x)=0` for every x. The product limit is exactly
the first limit. Convergence at fixed k would not suffice; a seeded
datum generally has nonzero Delta at a fixed finite torus.

R253's constant examples are correct: choose epsilon tending to zero
fast enough that the dilated thermal four-volume times epsilon tends
to zero on each finite scale window. Then Delta tends to log m and
S tends to m−1. They disprove universal rigidity of the abstract
class, not rigidity of one specified Wilson trajectory. Ising, photon
and five-dimensional realization assertions in R255,269–270 are not
used or certified here.

### 20. Proposition SI, R278–282 — HOLDS; following inference FAILS

For E in Omega and integer t, `sigma^(−t)E` belongs to Omega and
hence to Q. Thus E belongs to `sigma^t Q`. Intersect over t. This
proves precisely R280, with no closedness assumption on Q.

The first unsupported inference is R282: an asymptotic condition at
one end need not become an equality at all scales. For example
`lim_(m→−∞) D(2^m)=c` is already shift-invariant, and intersecting
its translates leaves that condition unchanged. Abstract critical
constants also retain that boundary condition. The blanket sentence
“No boundary condition at one end ... is a kept property” is false.
Replace it by: “Every kept property holds along every integer shift
of each element. The bounds in CE do not establish preservation of
the trajectory's ultraviolet normalization.” If a specified UV law
forces D to diverge at small scales, CE's uniform bound excludes
that law; neither SI nor this check proves such a UV law for Wilson.

End of the pre-1019 record. The comparisons below were written only
after those original verdicts were saved. No source file was edited.

## Comparison with row 1019 and final repairs

O means `gap-compact-rigidity-check-opus.md`. It was then read whole.
Its author is Claude Opus 5.5, max; the checked author is Claude Fable
5.2, max. This session is a different-provider reading, not a claim
that changing provider itself establishes independence. The hand paths
above include a rational UF margin, the minimum/maximum proof of OM(c),
and an explicit scale-window diagonal and quantifier check for CR.

### Required repairs D1–D3 and D7–D9

| Repair | Exact disposition |
|---|---|
| D1, O73,237 | Agree. Add `j≥n` in R233, together with `k≥n` and the finite scale window. Item 11 gives the repaired proof. |
| D2, O133,233 | Agree. In OM(b) and CR, D_0 must be an actual BDD-Delta bound of the same trajectory, not an arbitrary cutoff. Items 12 and 16 use that hypothesis. |
| D3, O172,235 | Agree. TRI(III) means existence in `Omega_Z(D_0)` for some finite D_0. Item 17 supplies the exact wording and exclusions. |
| D7, O87,241 | Agree. Enforce integral times at least 3. S0 suffices on the physical grid; abstract blow-down uses only eventual valid coordinates. Item 1 states both alternatives. |
| D8, O88,241 | Agree; add explicitly to item 1: a critical eternal datum must possess CE(ii)(b)'s ordered spectral form in every direction, with finite ground level and finite trace at every positive dyadic time. Otherwise s and z in R158 are undefined. LV makes the representation unique. |
| D9, O117,242 | Agree. Replace the blanket finite-value statement in R176,192 by a closed inequality in continuous converging coordinates. Item 8 checks each actual engine inequality used. |

D8 sharpens my pre-1019 definition discussion; it changes no extraction
claim, since CE constructs exactly that spectral form. For arbitrary
abstract eternal functions it is a necessary definition clause.

### Disagreements and their resolution

1. **Wall domain: the ZD check is right; O63 is incomplete.** O63
   infers `D^+(L/4)≤D_0` from the old wall. If L is the first or
   second point of P, L/4 is outside P. Neither O151 nor O229 repairs
   this. Use the exact wall in item 16, from `gap-zd-astra.md:413–414`.
   First unsupported step of the old implication: O63 (and Q246 below).
   The repaired implication holds; no counterexample to the old
   implication as a theorem about actual Wilson data is asserted.

2. **The numerical return-gap sentence: this check supplies the correct
   bound on successive return times; O137 is too strong in that
   convention.** O137 accepts R236's bound `2 max|n_l|`. On a
   three-cycle, U a singleton has a cover with shifts −1,0,1;
   successive returns differ by 3, exceeding 2N=2. A singleton
   system also permits N=0 while successive returns differ by 1.
   Use `2N+1`. If “gap” counts missing integers instead, 2N is
   harmless; the stated bounded-gap conclusion is identical. This
   corrects the general finite-cover calculation, not recurrence or CR.

3. **The D^+ caution: row 1019 is right about the extra example.**
   My item 16's sentence “R247's caution is correct” accepted its
   logical warning but did not separate the stronger existence
   assertion. O179,239 correctly point out that monotonicity of
   `D^+(L)=limsup_j D_j(L/a_j)` alone supplies no simultaneous
   lower bounds for an arbitrary moving-scale diagonal. The source
   has not proved that this assumption produces a limit with
   constant D. Retain the warning that strict decrease of D^+ does
   not prove CR(5); mark that example unproved unless the needed
   joint convergence is supplied. This amends my original reading;
   it does not amend the CR proof, which does not use R247.

4. **Literal versus repaired verdicts: qualifications are necessary.**
   O12 and O256 say “first failing step: none” while O233–242
   identify unqualified statements that need repair. On the repaired
   mathematical chain, we agree: there is no remaining failing step.
   On literal R text, “none” is too broad: R233 omits j-divergence,
   R241 needs D2, and R350's family-free exclusion is false. This
   note therefore uses HOLDS AFTER CORRECTION. The substantive
   repairs and their mathematical conclusions agree with row 1019.

There is no other mathematical disagreement in the requested claims.
The two-cycle used in item 16 refutes the claimed inference from
OM(e) as a topological statement; it is not a constructed Wilson limit.
In particular I agree with O177/D5 on stationarity versus a fixed
datum, O195/D12 on both divergent indices in PT-inf, and O203/D14
on SI's invalid asymptotic inference. O139's direct recurrence proof
is the same repair of its loose parenthesis as item 15. O121/D10
correctly adds commuting flips. Its phrase “vacuum even” must mean
the distinguished rank-0 vector, not every vector in a possibly
degenerate limiting ground space. The unsigned torus datum alone
does not specify the signs or an observable algebra.

### 21. Data A_(m,epsilon), R253 — HOLDS

For completeness, here is the exact scale dependence in the no-rigidity
example, also agreeing with O185. The density is f=0. Put
`c_i=81 epsilon_(j_i)16^k_i` for u=3. Then

`Delta_i(x)=log(1+(m−1)exp(−c_i product(x)))`,
`s_i(b)=(m−1)exp(−c_i b^4/2)`.

Choose `j_i,k_i→∞` with `c_i16^i→0`. This is possible by choosing
k_i first and then j_i sufficiently large. H1 holds with `D_0=log m`.
For each fixed b, H2 holds eventually since s tends to m−1≥1.
The limiting spectrum has m zero levels; the remaining levels are
infinite. Thus Delta is log m, s=m−1 and z=0 at every scale, and
sigma fixes the datum. The initial invalid times for u=3 are discarded.
This is the source's abstract example, not a new Wilson construction.

### 22. Proposition NR, R264 — HOLDS AFTER CORRECTION

Any class containing all admissible limits of all data families
contains the example in item 21. Thus it cannot exclude all critical
elements. The photon sentence is conditional on the existence of the
photon limit and its stated bound; no photon theorem is proved here.
Replace “all its sums with other limits” by “sums realized along a
common sequence admissible for the product family.” This is O199/D13.
PT-inf's scalar inequalities alone do not assert membership in a
specified Omega. No contradiction for the Wilson trajectory follows.

### 23. The scope table and interpretations, R202–221,266–272

**HOLDS AFTER CORRECTION** as a summary of the preceding statements:
retain the four directional spectral trace representations, axis
permutations, the specified closed engine inequalities and, under A4,
the extracted sign grading. Keep the allowed losses of simplicity,
high levels, non-dyadic sizes, uniqueness and fixed-point invariance.
The object contains no observable field. R204 and R221 must not claim
observable reflection positivity from traces alone. R214 and R221
must not claim that *all* ultraviolet information is necessarily lost:
no preservation of the trajectory's ultraviolet normalization has
been proved, while SI permits shift-invariant information to survive.
PT-inf proves precisely the loss of a uniformly seeded factor's
torus contribution, with the corrected divergent-index hypothesis.

The Ising realization in R255, the application to NP in R269 and the
five-dimensional premise in R270 remain source-labelled recollections
or conditional readings. Their physical premises were not independently
checked. R272's conclusion that abstract torus rigidity fails follows
already from item 21. This restriction leaves the requested compactness
and CR implications intact.

## Form 2 of the dichotomy

Q means `gap-dichotomy.md`. Read Q75–194 and Q214–284. This checks
the form-2 statements and their logical assembly; it does not recheck
the continuum gap leg, source-supply table or historical status claims.

| Numbered consumer | Verdict and exact reason |
|---|---|
| Q1.4, 123–136 | HOLDS. The same trajectory defines Omega; both indices diverge; the spectral clause incorporates D8. S0 at Q95 covers D7. |
| Q2.2, CE at 166–171 | HOLDS, given the named engine inputs and A4 for the centre statement. D9 is explicit. Read “vacuum even” as distinguished rank 0; the ground eigenspace can be larger. |
| Q2.2, OM(a)–(d) at 173–177 | HOLDS with its applied D1 and D2. The numerical return-time correction does not change any quoted conclusion. |
| Q2.2, CR(1)–(5) at 179–182 | HOLDS AFTER CORRECTION of Q119 to the repaired wall in item 16. The remaining arrows, Q273–275, hold. |
| Q2.2, TRI(I)–(III') at 184–190 | HOLDS. D3 is explicit. I excludes both other cases; no exclusion between II and III' is inferred. |
| Q2.2, link at 192–194, proof 282–284 | HOLDS given ZD-c. Under BDD, III is exactly not-PHYS-SEED. CE and OM then give recurrence for each BDD bound. Conversely recurrence for any finite bound excludes PHYS-SEED. Under BDD this is III. |

Q246 invokes the old wall outside the guaranteed range for L/4;
this is the precise consumer line needing correction. Q243 already
uses `L≥4L_0`, so the bound quoted in branch III has no such defect.
With the corrected wall, form 2 is a valid conditional equivalence.
It does not eliminate either unbounded Casimir free energy or a
recurrent critical limit of the specified trajectory.

## Final verdicts and limits

All HOLDS verdicts are mathematical implications from the named inputs.
This note supplies no physical realization of those inputs and grants
no scientific or audit status.

| Statement | Final verdict |
|---|---|
| Definitions, critical element | HOLDS AFTER CORRECTION: D7 and D8. |
| UF | HOLDS on the corrected time domain. |
| CE(i)(a), CE(i)(b) | HOLDS. |
| CE(ii) extraction, (a), (b), (d) | HOLDS. |
| CE(ii)(c) | HOLDS AFTER CORRECTION: D9, closed continuous inequalities. |
| CE(ii)(e) | HOLDS under A4 with the explicit commuting-flip and distinguished-vacuum scope. |
| OM(a) | HOLDS AFTER CORRECTION: D1. |
| OM(b) | HOLDS AFTER CORRECTION: D2 for its converse. |
| OM(c), OM(d), OM(e) | HOLDS; use the corrected positive return-gap bound and the direct recurrence argument. |
| CR(1)–(5) | HOLDS AFTER CORRECTION: D2, trajectory-specific Omega and repaired W. |
| TRI | HOLDS AFTER CORRECTION: D3. |
| LV | HOLDS; finite real gaps on cubes, extended topology where levels escape. |
| PT-inf, (i), (ii) | HOLDS AFTER CORRECTION: both indices diverge; a uniform seed in (ii). |
| SI | HOLDS; R282's asymptotic/no-boundary-condition inference FAILS at R282. |
| A_(m,epsilon) | HOLDS. |
| NR | HOLDS AFTER CORRECTION of the conditional product sentence. |
| R245's fixed-point inference | FAILS at R245(ii); replace fixedness by Lambda-stationarity. |
| Q form 2 | HOLDS AFTER CORRECTION of W, given the named inputs. |

Not covered: construction of the continuum datum, physical matching of
S0 to the account, the whole proofs of S/SH/Z3/ZD-c, a mass gap,
observable completeness, faithfulness of the centre action, the recalled
comparison-model realizations, Remark MON, the sharpened SH constants
in R198, and Lean verification. No proof script or numerical test ran.
No checked source, registry, ledger, FINISH row, or remote content was changed.

Final checkpoint: requested line check, pre-1019 verdict record,
comparison and form-2 assembly are complete. The only output is this
research note, left uncommitted and unpushed on local branch
`research/gap-compact-rigidity-check-astra-f4960e6ba`. The open inputs
(W), (BDD-Delta) and (LIOU) remain open.

RESULT: HOLDS AFTER CORRECTION — the compactness/recurrence chain and CR's five-way equivalence hold with D1–D3, D7–D9, the stated spectral/centre/product scope, and W requiring L≥4L_0; form 2 survives. R245's fixed-point inference and R282's blanket boundary-condition inference fail. No mass gap, new rigidity input, or status grant follows.
