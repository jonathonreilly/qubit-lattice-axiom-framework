## Repo search

Refs searched in `/Users/jonreilly/Projects/Physics`: `origin/main`,
`pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`.
Initial terms: `CUT-TH`, `WALL-2`, `gap-fw-wilson`, `ring deficit`,
`wall domination`, and `free.wall.{0,80}doubl`. The broad `WALL-2` term
matched dates in unrelated campaign paths; that truncated search establishes
no absence. The narrowed `WALL-2\)` search completed on all five refs.
Its only hits were `docs/NATIVE_DILUTE_FIELD_NOTE_2026-10-18.md:228` and
its copy under `outputs/neutral_continuation7_review_2026_10_18/proofs/pr9819/`:
“full lowering deficit is 99/R^2”. This substring match is not a ring or wall
statement and supplies no input.

A completed method search used `free.wall|thermal excess|ring Casimir|
wall.to.wall|Neumann.{0,30}image|trace.{0,30}doubling`, with cap 70.
Other thermal-trace discovery searches hit their caps and establish no
absence. Relevant hits and reused local prior work are:

| Source read | Exact relevant statement and closeness |
|---|---|
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/LCONV55.md:248–261`, also hit on pr/10133; STEP55 and check-file echoes | Its wall-to-wall holonomy kernel has second-order form `diag(-144,-144,0)`. This is a background-Hessian calculation, not the wall thermal deficit or a doubling bound. No input is taken. |
| `origin/main:docs/GAUGE_VACUUM_PLAQUETTE_PERRON_REDUCTION_THEOREM_NOTE.md:135–183` | It reduces a fixed finite Wilson transfer state to its unique positive Perron vector and preserves commuting positive symmetries. This is a related transfer method, not a free-wall comparison. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`, located through the requested November 8 digest | For a centred loop F, `kbar_B >= (1+v_N/rho)^(-1) (F tensor F*)`. This already supplies the rank-one convolution comparison method. Lemma OS's constant-state specialization is not a new method; its wall-defect calculation is the present check's object. |
| `gap-next3-max.md:392–458` and `gap-crux-restate.md:176–205,236–238` | FW1–FW6, the vector-weight obstruction, symmetric-trace enlargement, and the twist/projection identity are existing inputs. Row 907 does not first prove them. |
| `gap-fw-gauss-opus.md:17–86,118–124` | Neumann mode formulas give the image identity and the wall bounds. The added boundary field is the changed model checked below. |
| `gap-sc-box.md:49–78,118–175`; `gap-seed-sc.md:156–181` | Covered supports, analytic small-beta control and the first torus-tube coefficient already exist. Section 13 uses them rather than rebuilding the expansion. |
| `gap-crux-exercise2-check-astra.md:227–266`, pointed to by `gap-glue-check-astra.md:405–421`; `gap-q8test-check-astra.md:171–183` | Centre-even Q8/2T flat states already obstruct a small even trace. The exact criterion is central versus noncentral holonomy, and Q8 has four even characters. Section 9 applies this existing obstruction to the one-ring geometry; it is not a new finite-group attack. |

The first method search also hit unrelated Wilson-hop/Casimir notes,
Neumann observable-image notes, and an archived free two-step transfer
comparison. Their hit statements concern other models or meanings of
“wall”; none states the present target. No inspected source covers this
whole check, and the registry gives no competing owner for it.
`prior/repo-search-2026-11-08.md` was read; its relevant rank-one locator is
used above. Row 909 contains no additional “Repo prior work” field.

Ref identities observed at the end of the search, in the order listed above:
`8920090caae2`, `f76f6c649cff`,
`89faef229ff6`, `1e70c7211a2c`, `c73ad7b177d9`.
Index searches for free walls, ring deficit, CUT-TH, wall-to-wall exchange,
transfer/convolution and finite-group/even-flux objects found the cited
convolution and polymer entries, but no named wall-comparison supplier.
The exact wall-label search in `sa-index/ca-full/` returned no matches.
No assertion about an uninspected CA-I–III passage is made.

## Provenance and scope

Codex, gpt-6-astra, xhigh; 2026-11-13; checkout
`e11d623d1c64b3de82fd705a2033df77c2d12cf7`. Research check of FINISH row 907,
by Claude Fable 5.2 max, for row 909. Not an audit; grants no status.
The requested prior file `library/prior/gap-fw-wilson-check-astra.md` is absent.
The registry search `free.wall|gap-fw|CUT-TH|WALL-2` has no match.
Only this report is edited. No numerical result will discharge a step.
The reviewed source's Git blob is `75fa712847a01731429090978973948f2066a054`;
the on-disk blob was compared with the pinned commit again at completion.

Completed scope: ring dictionary; reflection positivity and the image
defect; both doubling identities; both obstructions; cut and centre-even
correction; Theorem C and S1–S4; small-beta tubes. The arguments and verdicts
were saved incrementally. The source's GUIDE scan was neither used as a
proof input nor rerun. This check proves no order-one wall estimate,
limit-state theorem, or mass gap. It does not recheck the full transfer or
polymer foundations cited below, or the Maxwell/Proca mode derivations.
The configured checker was used directly; no subagent or numerical run
was used. The differing check paths include a path difference-equation
solution, momentum pairing, and explicit flat-state counts.

## 1. Ring dictionary: HOLDS

Source 3.1(a)–(e), lines 72–80, and the convexity addendum before Step 6.
Here and below, source line numbers refer to `gap-fw-wilson-max.md` at the
pinned checkout. Spectator sides remain fixed in every limit.

Closing the free side introduces `a N_1` plaquettes and Haar links. Each
new plaquette has Haar mean zero for circumference at least three. Jensen
and the pointwise bound give `W <= P <= exp(beta a N_1) W`.
The time limit therefore gives `e(n) <= eps(n) <= e(n)+beta N_1`.
Dividing by `n` identifies the two bulk densities. Thus `p=eps-f n` is
exactly the ring deficit, not a new wall estimate. Log-convexity of each
trace, followed by the time limit, makes `eps` convex. Submultiplicativity
gives `p>=0`; `p(n)/n -> 0` rules out a positive forward difference of this
convex sequence. This proves D1, including monotonicity.

Both expansions of `log P-a n f` give D2. Since `p(n)<=p(a)` for `n>=a`
and the opposite-channel log-sum is nonnegative, D3 follows:

`g_P(a;n) >= n p(a)-a p(n) >= (n-a)p(a)`.

Consequently the ring has `n p(a)<=2 g_P(a;n)` on `a<=n/2`.
Also `delta_e(n)<=p(n)+D_inf`. All these are correct. They do not give
WALL-1 for the free-wall family.

The sentence saying WALL-1 and WALL-2 “ask” for a slab-to-ring bound needs
one logical qualification: `a delta_e<=C b p`, together with WALL-1, is
**sufficient**, not equivalent to WALL-2. WALL-1 bounds `b p` above by `g`;
it does not bound `g` above by `b p`.

## 2. Reflection positivity: HOLDS AFTER CORRECTION of scope

The explicit word inequalities in 3.2 hold. Since `Q=|v><v|` has rank one,
each word containing Q reduces to a positive scalar times `R^k Q R^l`.
For two such words, Hilbert–Schmidt Cauchy–Schwarz is the product of two
log-convexity inequalities for `W`. For a pure power and a cut word it is

`W(a,n+k+l+1)^2 <= P(a,2n) W(a,2k+1) W(a,2l+1)`.

Substitution gives CS-1. Applying FW6 at `k+l+1`, and then midpoint
convexity, already gives CS-1 without its nonnegative ring term.

**Correction:** this checks the stated monomial-word family. It does not
classify all consequences of reflection positivity, insertions, or linear
combinations of words. The author's explicit “Not explored” qualification
must survive the later claims that RP gives “only” these facts or that the
entire suggested route is closed. No theorem excluding every RP argument
has been proved.

## 3. Lemma OS, OS1–OS3 and the void defect: HOLDS

Use the Wilson convolution formula already proved by Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text: outline
GL3, lines 2197–2257. Their weight includes `exp(-beta)`; removing that
constant gives precisely `c_j=2 I_(2j+1)(beta)/beta`. The SA index was
consulted first: chunk-02 lines 78–105 and obligations lines 62–86.
This is a cited input, not a new derivation of their coefficient formula.
Their normalized-Haar transfer identity GL8, lines 2315–2336, was also
read; its gauge average carries no extra volume factor.

Each link convolution is at least its constant-state summand. Tensoring,
gauge projection, and conjugation by `B_0^(1/2)` preserve this inequality:
`R >= c_0^N Q`. No monotonicity of the higher coefficients is needed.
At beta zero use `c_0=1, c_j=0` for `j>0`; the source's assertion that
*all* coefficients are strictly positive applies only to beta positive.

Put `kappa=c_0^N`. The three consequences follow respectively from
`Tr(R^(n-1)(R-kappa Q))>=0`, the monotonicity of the squared
Hilbert–Schmidt norm on positive operators, and evaluation of
`R-kappa Q` on `R^(b-1)v`. These yield exactly OS1, OS2, OS3.
The time limit gives

`delta_e(b) <= p(2b)/2 + Delta_w`,
`Delta_w >= 2 delta_e(b)-delta_e(2b) >= delta_e(b)`.

Thus the image inequality is weaker than an already available bound;
`Delta_w>=delta_e(1)` includes the one-site free side. This part is sound.
The statement in 7.3 for general domination also holds **provided** there
is one family `kappa(a)` independent of `b`, and the finite rate
`eta=lim_a log(kappa(a))/a` exists. Replace `N_1 log c_0` by eta.
Without a specified rate the displayed limiting `Delta_kappa` is undefined.

## 4. Both exact doubling identities: HOLDS

Source 4.1 and Step 11. Define `tau=gamma-a delta_e` with all other sizes
fixed. Direct subtraction of FW5 gives

`g(a,b+h)-g(a,b)=h p(a)+tau(a,b+h)-tau(a,b)`.

Subtracting twice FW5 at b from FW5 at 2b instead gives

`g(a,2b)-2g(a,b)=p(a)-c(a)+tau(a,2b)-2tau(a,b)`.

The wall term is `p-c=log(r_0/w_0)-a D_inf`. The underlying vector
inequality also holds: after dividing by `w_0 r_0^(b-1)`, every
normalized spectral weight decreases with b, so
`W(a,2b)<=(r_0/w_0) W(a,b)^2`.

These identities retain the cancellation between gamma and the
zero-temperature wall interaction. Dropping gamma instead leaves exactly
`a[2 delta_e(b)-delta_e(2b)]`, as the source says. DBL does not require
WALL-2. That non-necessity is demonstrated by the models checked next.

## 5. Boundary-field obstruction: HOLDS

Source 4.2. This is an obstruction for the stated class of Gaussian models
with variable boundary fields, not for Wilson's fixed free boundary.
The reference mode formulas are in `gap-fw-gauss-opus.md:17–86`.
The following check avoids the image-sum derivation of the boundary response.

Let `r=exp(-mu)` and `m^2=r+r^(-1)-2`. Solving the path difference equation
`(m^2-Delta_N)h=delta_1+delta_b` gives

`h_x=r(r^(x-1)+r^(b-x))/[(1-r)(1-r^b)]`.

The interior equation follows from the defining quadratic for r. At the
left endpoint, `(m^2+1)h_1-h_2=1`; reflection gives the other endpoint.
Thus `H_b=G_b(1,1)+G_b(1,b)=r(1+r^(b-1))/[(1-r)(1-r^b)]` and

`I(b)=H_b-H_infinity=(1+r)r^b/[(1-r)(1-r^b)]>0`.

This equals the source's image sum and is at least
`[r^(b-1)+r^b]/(2 sinh(mu))`. Completing the square adds exactly
`J^2 a cd H_b` to `log W`; the Hessian is unchanged. Therefore
`g_J=g_0`, `p_J=p_0`, `c_J=c_0`, `tau_J=tau_0`, while
`delta_e^J=delta_e^0+J^2 cd I(b)`. The displayed lower bound on
`a delta_e^J/g_J` follows from `g_0<=bcd F_a(mu)` and diverges with J.

For DBL_2, pair the Neumann momenta of the 2b path as `2j,2j+1`.
Since `theta -> F_a(omega(theta))` decreases, each pair contributes no
more than twice its `2j` member. Hence `g_0(a,2b)<=2g_0(a,b)` directly.
The boundary source leaves this unchanged. Reflection positivity across
each reflection preserving the box follows by splitting the symmetric
linear source into its two reflected halves. It does not impose a bound
on J. The unbounded-C_2 obstruction is valid.

As in the Gaussian reference, bare normalization need not satisfy Wilson's
FW2 sign. Use the limiting definitions of f and D_inf here; a suitable
per-bond normalization can restore supermultiplicativity without changing
the tested quantities. This example does not supply Wilson's boundary
vector from its unchanged local bulk weight.

## 6. Family T: HOLDS for the mixed trace/vector class

Source 6.1(a)–(c). Write its ground energy as
`e(b)=H b-D_1 cd+z^2 cd exp(-mb)`, with H independent of b.
The remaining factor is `(1-exp(-ma))^(-n bcd)`. For integer `n bcd`
this is the trace of that many oscillators, with genuine integer state
multiplicities. In a free side the remaining nonexponential factor is
`exp(z^2 a cd exp(-mb))`; expanding this exponential supplies positive
vector weights. The gluing defect in that side is

`a cd [D_1+z^2(exp(-m(b+b'))-exp(-mb)-exp(-mb'))] >= 0`

when `D_1>=2z^2`. Spatial permutation symmetry is exact. These prove the
claimed mixed-family properties. They do not put T in the *literal*
all-free, four-axis symmetric, unit-vector class defined in row 898
Step 6.2; T is its trace/vector analogue.

The listed data `g=n bcd F_a`, `p=n cd F_a`, `c=p`, `tau=0`,
`delta_e=z^2 cd exp(-mb)` follow. WALL-1 and DBL_2 hold with equality.
For an even `b>=6`, take `a=b/2`, `m=2 log(2)/b`. Then

`a delta_e/g=z^2/(8n log(2)) >= z^2/(8n)`.

The last inequality follows from `log(2)=integral_1^2 dt/t<1`.
No numerical evaluation is needed. This proves the second obstruction.
It does not reproduce Wilson locality and the shared local boundary
construction. The pointwise multiplication-operator bound in 6.1(c)
holds, but supplies no summed spectral overlap estimate.

## 7. COV: HOLDS AFTER CORRECTION of its spectral reading

Source 4.4. Take three blocks of lengths L,b,L, so that the total length
is `2L+b` (the printed closed integer interval needs that site convention).
Integrating the two coupling derivatives gives the finite identity

`log W(T,b)+log W(T,2L+b)-2log W(T,L+b)
 = beta^2 integral integral Cov(X_1,X_2)`.

After division by T the affine and wall constants cancel, leaving the
displayed second difference of delta_e. Taking L to infinity leaves
delta_e(b). Taking L to infinity at fixed T instead leaves gamma(b,T).
These are sequential limits, not an exchange of them.

**Correction:** the crossed vector sum detects only states with nonzero
wall overlap. Its leading decay rate is the lowest *wall-visible* energy,
which need not equal the gap of the full `R_T`. A centre-odd state, for
example, has zero overlap with the even wall vector. Nor does this identity
justify exchanging a spectral large-distance asymptotic with `T -> infinity`.
The “every light state” and equality-of-gap interpretation following COV
is not an established consequence. The covariance identity itself holds.

## 8. CUT and the extensive bounds: HOLDS AFTER CORRECTION of one reading

Source 5.1–5.2. Differentiation or division of the partition functions gives
`F_cut=log P-log W`, `phi_cut=eps-e=p(n)+D_inf-delta_e(n)` and

`g_P-g=F_cut-a phi_cut`.

OS1 and the pointwise crossing bound give the stated upper and lower
bounds on F_cut. For fixed a the b-channel Perron limit gives
`lim_n F_cut(a;n)=eps(a)-omega(a)=p(a)-c(a)+a D_inf`.
This proves both extensive bounds on c without interchanging limits:

`p-a(beta N_1-D_inf) <= c <= p+a Delta_w`.

Keeping `p_infinity=lim_n p(n)` gives exactly the source's formula
`lim_n[a phi_cut(n)-F_cut(a;n)]=c-p+a p_infinity`.
**Correction:** the following sign interpretation of `c-p` requires
subtracting `a p_infinity`, or a separate proof that `p_infinity=0`.
It does not follow from the displayed formula with merely `p_infinity>=0`.
The algebraic restatement of WALL-1 in 5.2, with `+p/C_1`, holds.

## 9. Step 10: the SU(2) even identities HOLD; the universal flux test FAILS

The twist/projection input is already in `gap-crux-restate.md:105,236–238`.
For the free transverse sides, the same link change of variables inserts
the central flip on one time slice. Every spatial plaquette has zero or two
flipped links. The flip commutes with the transfer, is an involution, and
fixes its unique positive Perron vector. The twist stack is the same set
of `cd` plaquettes after exchanging the two periodic directions.
Consequently `P^ev=(P+P^tw)/2` is symmetric and is a positive trace on the
even subspace in both channels. Its top eigenvalue, eps, f and p are
unchanged. D2, D3 and Lemma E therefore hold for `g_P^ev`.

For finite beta the twisted integrand is strictly positive. Thus
`0<=u<1/2` and `g_P-g_P^ev=-log(1-u)` hold. Put the stack on the cut:
at zero cut strength, both partition functions are W, so their average
is W with no factor of two. At full strength it is `P^ev`. Differentiation
gives exactly the printed weighted average of X and its twisted version.
Since `P/2<=P^ev<=P`, the zero-temperature cut rate remains phi_cut.
The corrected identity

`g_P^ev-g=F_cut^ev-a phi_cut`

is exact. For fixed n,c,d the coupling integral and the zero-temperature
limit can be justified without an extra infinite-volume hypothesis: the
compact transfer kernel is strictly positive, continuously in s on `[0,1]`.
Its simple top eigenvalue and separated spectral projection are smooth in s.
The trace limit of the logarithmic derivative gives the derivative of that
eigenvalue. Alternatively boundedness `|X_cut|<=a N_1` supplies domination
once this pointwise limit is taken. No n limit is exchanged here.

**FAILS:** “Frozen finite groups: u -> 1/2, g_P^ev and g are both small”
(source line 306). The pre-existing centre-even flat-state obstruction
is recorded in the Repo search above; it already rules out this universal
claim. Z_2 has two flat ring classes, and the projection leaves one.
For its application here, Q_8 on a ring times a contractible free box has
the flat gauge classes

`{1}, {-1}, {+i,-i}, {+j,-j}, {+k,-k}`.

The central flip exchanges the first two classes and fixes the last three.
In the frozen transfer its even subspace has dimension four and its odd
subspace dimension one. The normalized full and even traces tend to five
and four, respectively. Thus `u -> 1/5`, `g_P^ev -> log(4)`, whereas
the contractible free box has one flat class and `g -> 0`.
RING-CMP-ev with a fixed theta below one still fails this Q_8 freezing test.
This is an exact five-state calculation, not enumeration by a program.

**FAILS:** the same line's U(1) identification, “even means zero flux”.
The flip at `-1` has eigenvalue `(-1)^q` on electric charge q. Its even
projection retains q=2 as well as q=0. Zero flux requires averaging over
the *whole* U(1) centre, not the two twists in Step 10.

Use “centre-even” or “neutral under the chosen central involution”, not
“flux-free”, for this construction. These failures do not refute the
SU(2) conditional implication. They refute its advertised universal
finite-group test and the asserted elimination of all flux sectors.

## 10. CUT-TH and S3: HOLDS AFTER CORRECTION of the constant

For the symmetric hypothesis `|g-h|<=theta h`, with `h=g_P^ev` and
`0<=theta<1`, all constants in 5.3 and corrected S3 hold:

`C_1=2/(1-theta)`, `k=4(1+theta)/(1-theta)`.

Indeed `h(a;b)>=(b-a)p(a)`. Trace submultiplicativity in the other channel
gives `h(a;2b)<=2h(a;b)+2a p(b)`, and
`p(b)<=p(a)<=h(a;b)/(b-a)`. Therefore `h(a;2b)<=4h(a;b)` on `a<=b/2`.
Sandwiching g between `(1-theta)h` and `(1+theta)h` proves both claims.

The CUT-TH actually printed at line 240 and in Step 10 is asymmetric:

`-theta' h <= F_cut^ev-a phi_cut <= theta h`.

It gives `(1-theta)h<=g<=(1+theta')h`. With fixed finite
`theta'>=0` and `0<=theta<1`, the correct constants are

`C_1=2/(1-theta)`, `k=4(1+theta')/(1-theta)`.

The source's stated k follows only after adding `theta'<=theta`, or
replacing CUT-TH by its symmetric version. An upper bound alone cannot
give the upper sandwich at 2b. This is a constant/hypothesis correction
to the RESULT line, not a proof of CUT-TH for Wilson.

## 11. Theorem C: HOLDS

Source lines 219–227. All three rectangular doubling steps are expressly
hypotheses at every ladder level. Thus, with `A=k^3`,
`s_(j+1)<=((1+s_j)^A-1)^2` follows from trace squaring.
Here is a hand bound not dependent on check 902's decimal arithmetic.
For `0<=x<=1/(4A^2)` and `A>=1`, `y=Ax<=1/4`, and

`(1+x)^A-1 <= exp(y)-1 <= y/(1-y) <= (4/3)Ax <= 2Ax`.

The middle inequality follows by comparing the exponential series with
the geometric series. Set `B=4A^2`. Induction gives
`B s_j <= (B s_0)^(2^j)` and keeps each s_j inside the required interval.
The first excited eigenvalue contributes `exp(-a_j m_j)` to s_j, hence

`m_j >= [2^j log(1/(B s_0))+log B]/(2^j a_0)
       >= log(1/(B s_0))/a_0`.

At `s_0=0`, including beta zero, either state the theorem with `0<s_0`,
or use the natural extended convention `m=+infinity`: H-DBL then forces
every ladder trace remainder to vanish. No assertion for intermediate
non-dyadic boxes or a limit state follows. The source's exclusions hold.

## 12. S1, S2, S4 and the half-distance reduction: HOLDS

Source lines 232–236 and 312–320.

| Statement | Check |
|---|---|
| S1 | FW6, WALL-1 and WALL-2 give `k=1+C_1+C_2`. |
| S2 | DBL-ID and CORNER give the same k. Also `tau(2b)-tau(b)<=a delta_e(b)`, so WALL-2 implies CORNER. |
| S4 | DBL-ID2 gives `k=2+C_w+C_tau` exactly. WALL-1 is unused. |
| Half-distance | `floor(b/2)>=a` gives `p(floor(b/2))<=p(a)`; hence `a delta_e<=C' a p(a)<=(C'C_1/2)g`. |

Take nonnegative uniform constants, or enlarge the resulting k to at least
one for Theorem C. These implications require each mixed rectangle on the
ladder, not merely the initial cube. No one of their Wilson hypotheses
at order-one beta is established here.

In the Gaussian boundary-field example c,p,tau are independent of J; in T,
c=p and tau=0. Thus CORNER/S4 do avoid the unbounded wall source in these
examples. For the Neumann scalar the positive wall term gives `C_w=0`;
the image formula's decreasing propagator gives `tau(2b)<=2tau(b)`.
The direct mode-pairing proof in section 5 independently confirms k=2.

## 13. Small-beta tubes: HOLDS AFTER CORRECTION of scope and justification

Source 4.3, 5.4 and the small-beta parts of 6.2–6.3. For SU(2), fixed
`a>=3`, fixed free spectator sizes `c,d>=2`, and `b>=2`, the three leading
terms are correct. A uniform statement over the entire ladder does not follow.
Here is the missing fixed-size justification, using existing inputs.

**Existing inputs, reused.** `gap-sc-box.md:49–78,118–175` supplies the
covered-support condition, four-plaquette slice count, polymer activity
bound `(4|beta|)^|X|`, and at most `400^(n-1)` rooted n-plaquette supports.
`gap-seed-sc.md:156–181` already proves the torus-tube Haar moment and
that its first connected coefficient equals its moment. These are credited
to their authors, Claude Opus 5.5 and Claude Fable 5.2 respectively; the
rooted counting method is itself credited there to the older IN1 note.
The general convergent connected logarithm is Sussman–Alpoge's theorem,
outline lines 1271–1347, not a theorem first proved here.

**Why limits and coefficients are legitimate.** Use their polymer criterion
with `a_X=|X|` and majorized activities `exp(|X|)|w(X)|`. For
`|beta|<=1/51200`, the incompatible sum is bounded by

`24 |X| sum_(n>=1) 400^(n-1) (4 exp(2)|beta|)^n
 <= |X| (864/51200)/(1-14400/51200)
 = (27/1150)|X| < |X|`.

Here `exp(1)<3` follows from the exponential series. The cited rooted
theorem therefore gives an exponential reserve in total support size.
Root a cluster at any plaquette of its union and apply that theorem;
summing root polymers through the plaquette uses the same geometric
series. The diameter and the number of possible placements touching a
fixed cut are bounded by total support size plus one. The reserve absorbs
these factors. Thus the local cluster sums, their cut sums, and their
Taylor series converge absolutely on smaller discs, uniformly in the
finite-volume approximants. Normalized bulk sums and boundary sums have
termwise limits: clusters reaching a remote boundary have diverging size
and vanish under the reserve. This justifies the limits defining f, e,
D_inf, delta_e and p in this small disc. It asserts no useful relative
error uniformly in a or b.

**Slab count.** Group the infinite-tube connected clusters by their span r
in the free direction, after quotienting translations in that direction.
Let A_r denote their signed contribution per unit time and per such
placement, summed over the free transverse coordinates. A span-r cluster
has `(b-r)_+` placements in the b-site slab. Absolute convergence gives

`e(b)=sum_r (b-r)_+ A_r`, `f=sum_r A_r`,
`D_inf=sum_r r A_r`, `delta_e(b)=sum_(r>b)(r-b)A_r`.

Terms from the trivial plaquette coefficient are included in the first
three affine quantities and have no tail for `b>=2`.
A covered cluster spanning r slabs has at least four plaquettes in each
slab and at least one cap at each end. At total degree `4r+2`, every slice
must be a unit square cycle; no intermediate cap or displaced square can
be paid for. Hence it is the straight capped tube. Any repeated plaquette
or larger representation raises the degree. The first tail has `r=b+1`,
with placement factor one. There are

`n_t=(c-1)(d-1)+(c-1)d+c(d-1)`

choices per unit time. A fundamental sheet contributes `2^(V-E+F)u^F`,
where `u=I_2/I_1`; this is the usual edge Haar contraction, with one factor
`1/2` per edge and one closed index sum per vertex. The sphere factor is
four, the torus factor one. A proper nonempty subset has an exposed link,
so its moment vanishes; the first logarithmic coefficient is the same
moment, as in the cited tube lemma. Therefore

`delta_e(b)=4 n_t u^(4b+6)(1+O(u^2))`.

**Thermal count.** The existing covering argument cancels every coefficient
below `4a` in `log W(a,b)-a e(b)`. Equality requires a unit square in each
of the a time slabs, with no caps: one straight torus tube. Its coefficient
is one in units of `u^(4a)`. Thus

`g(a,b)=n_s(b)u^(4a)(1+O(u^2))`,
`n_s(b)=b(c-1)(d-1)+(b-1)[(c-1)d+c(d-1)]`,
`p(a)=n_t u^(4a)(1+O(u^2))`.

The p coefficient follows by dividing by b and taking the local cluster
limit just justified. The parity improvement in these remainders is valid:
on a box with only one periodic direction, order that direction last and
multiply a link in direction mu by `(-1)^(sum_(nu<mu) x_nu)`.
Every plaquette changes sign and the link signs remain periodic. Hence
the relevant partition functions and their limiting logarithms are even
in beta. Since u is odd analytic with nonzero derivative at zero, the next
possible relative power is `u^2`.

The displayed ratios at source lines 140–142 now follow, at fixed sizes.
In particular `delta_e(b)/p(2b) ~ 4u^(6-4b)` diverges for `b>=2`.
This refutes a beta-independent image constant C; it does not refute
WALL-2 on `a<=b/2`, or a bound with C depending on beta.
Moreover `n_s(b)=b n_t-R`, where `0<=R=(c-1)d+c(d-1)<=n_t`, so
`1-1/b<=n_s(b)/(b n_t)<=1`. This checks the leading WALL-1 claim.
The leading WALL-2 ratio is precisely
`4a n_t u^(4(b-a)+6)/n_s(b)`, and tends to zero in its stated domain.

**Corrections to the physical readings.** The later `b^(3/2)` phase-space
claim is conditional on a massive one-particle band, a nonzero wall form
factor, and three effectively infinite spatial directions. None is proved
by this coefficient calculation. With fixed finite c,d the corresponding
quadratic-band phase-space power is `b^(1/2)`, not `b^(3/2)`.
Likewise “true at leading order” is not a uniform WALL-1/2 theorem on
all sizes at one positive beta.

The U(1)/finite-subgroup coefficients require their own representation
normalizations. For U(1) an unoriented fundamental closed surface has two
orientations, contributing `2(I_1/I_0)^F`, not one such term. The source's
literal universal coefficient claim therefore FAILS. The SU(2) formulas
above and the conclusion that the image distance differs from `2b` are
unaffected. No claim about a full one-particle band is imported from
Tadeusz Balaban; none of his estimates enters this check.

## 14. Real multiplicities and Step 11's last comparison

**HOLDS AFTER CORRECTION:** source 6.1(d)'s rigidity for its displayed
ansatz. Write `M(x)=alpha+pi x+nu q^x`, `0<q<1`, `nu>0`.
The source's premise that the remainder itself must be integer is not
justified: alpha and pi were not shown integer. Instead, if all M(x) are
integers then

`M(x+2)-2M(x+1)+M(x)=nu(1-q)^2 q^x`

is an integer tending to zero. It must eventually vanish, contradicting
`nu>0`. Thus this exact finite-ell ansatz has no nonzero exponential
remainder at all. A bump at zero requires the separately allowed limit
`q=0`, not a positive finite ell. This proves rigidity only for that
ansatz, not a classification
of all crossed trace families. The unconditional trace engine stays open.

**FAILS** if read as a bounded combined S4 cost: Step 11's statement that
the depleted real-multiplicity example violates the separate bounds “but
not their sum”. An exact example removes any possible cancellation claim.
For integer `x>=0`, take

`M(x)=epsilon+nu[2^(-x)-1/32+(x-5)/64]`, `epsilon,nu>0`.

Its forward difference is `nu[1/64-2^(-x-1)]`, so its minimum is epsilon
at x=5,6. It has the stated positive-exponential ansatz. Take a=3, b=6,
`M(5)=epsilon`, while `M(11)=epsilon+129nu/2048`.
For `g(a,b)=M(b-1)F_a`, therefore,

`g(a,12)/g(a,6)=1+129nu/(2048epsilon) -> infinity`.

DBL-ID2 forces the *sum* of its two correction terms, divided by g(a,6),
to diverge as well. The individual sufficient conditions remain valid;
there is no uniform combined bound on this example. Real multiplicities
are not genuine trace multiplicities, as the source correctly emphasizes.

The numerical values quoted from Step 9 remain GUIDE only. In particular
an observed doubling ratio cannot infer separate bounds on C_w and C_tau;
their two terms can cancel. No script, Maxwell/Proca scan, or continuum
dispersion estimate was used to decide any verdict above.

## Coverage and disposition

| Source statement | Verdict | Report section |
|---|---|---|
| 3.1(a)–(e), D1–D3 | HOLDS | 1 |
| 3.2 word inequalities / unrestricted “only RP” reading | HOLDS / HOLDS AFTER CORRECTION | 2 |
| Lemma OS, OS1–OS3, RP-IMAGE, domination defect | HOLDS, with the stated endpoint/rate conventions | 3 |
| DBL-ID, DBL-ID2 and the vector joining inequality | HOLDS | 4 |
| 4.2 boundary-field obstruction | HOLDS | 5 |
| 6.1(a)–(c), family T obstruction | HOLDS in the mixed trace/vector class | 6 |
| COV and its gap interpretation | HOLDS AFTER CORRECTION | 7 |
| CUT, c bounds, asymptotic wall-term interpretation | HOLDS AFTER CORRECTION | 8 |
| Step 10 SU(2) even trace, twist, cut and flux-number identities | HOLDS | 9 |
| Step 10 universal frozen-group and U(1) tests | FAILS | 9 |
| Symmetric S3 | HOLDS | 10 |
| Asymmetric CUT-TH giving the printed k | HOLDS AFTER CORRECTION | 10 |
| Theorem C, seed `1/(4k^6)`, dyadic gap | HOLDS | 11 |
| S1, S2, S4; WALL-2 implies CORNER; half-distance reduction | HOLDS | 12 |
| Fixed-size SU(2) small-beta tubes and ratios | HOLDS AFTER CORRECTION of justification and scope | 13 |
| Literal group-independent surface coefficient | FAILS | 13 |
| Real-multiplicity obstruction / integer rigidity proof | HOLDS / HOLDS AFTER CORRECTION | 14 |
| Claimed bounded sum in the depleted example | FAILS | 14 |

The remaining named hypotheses are Wilson WALL-1/2, CORNER, H-W, H-tau,
CUT-TH and H-DBL at order-one coupling, the seed there, and the limit-state
step. This check supplies none of them. The frozen-group objection was
already known; it is an application error in Step 10, not new research.
No audit, ledger, registry, FINISH row, source note, or remote was changed.
The report is a local uncommitted file in the requested lane.

RESULT: Row 909 — the ring dictionary, void domination defect, both doubling identities, both abstract C_2 obstructions and Theorem C HOLD; CUT-TH needs k=4(1+theta')/(1-theta) unless its bounds are symmetric, and the RP/spectral/asymptotic readings need the stated corrections; Step 10's universal flux-removal test and Step 11's depleted-family cancellation FAIL; the fixed-size SU(2) tube coefficients HOLD with the supplied justification, without a uniform wall theorem, order-one seed, mass gap, or status grant.
