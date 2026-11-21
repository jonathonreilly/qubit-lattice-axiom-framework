# HCM-R under the literal final-stage rim test

Check: `../gates/hcm-false-check.md`, Claude (Opus 5.5); second round: `hcm-r2.md`.

Codex, 2026-11-08. Checkout `9e8d6a446d57fd7f04da80366b99d9509fd38c54`.
FINISH assignment 502. Research text. Not an audit. Grants no status.
No computer-assisted proof. This note changes no test or construction.

**Result: stop (c).** The named open lemma is RIM-LB, the actual
rim-history mass lower bound in §4. Three routes to it fail in §5.
HCM-R is neither proved nor refuted. Finding 9 does not yet prove its
claimed divergence.
This is the first-round result. The second round, hcm-r2.md, tests
finding 7's shift proposal and stops at the earlier conditional
escape supplier RIM-C. It does not justify narrowing the gap to RIM-N alone.

## 1. Ports and the question left by them

There is no `library/prior/hcm-false.md` at this checkout.
The H-C-MARK row in `open-registry.md` has no other owner.
The prior-work record is `prior/lfi.md`, row H-C-MARK, together with
`hc-mark.md` and findings 9–10 of `../gates/hc-mark-check.md`.
The one-operation counterexample and the three accounting reductions in
`hc-mark.md` are already done. They are inputs, not new work here.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every source construction below. Credit Tadeusz
Bałaban for the multiscale preparation and retention method.
The references are **Y**, `YM4_1400.tex` at
`2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`; **SA**,
`YM4_sketch_500.tex` at `31a47c543775`; and **I**,
`theorem_0_complete_account_raw_I.tex` at `31a47c543775`.
Line numbers refer to those files. The local full-read indices were used
before the bounded source reads. Source status below describes their
argument, not independent verification of the entire construction.

| Premise | Source and source status | Use here |
|---|---|---|
| Final-stage bare rim holonomy equals a top plaquette holonomy, with threshold $3(1-\beta_s/2)\varepsilon_mL^{-2m}$ | Y 72324–72338, proved there by the geometric argument | Ported local identity |
| The mismatch occurs for the average of a low-action bare field | Y 72340–72373, proved by a commuting affine field | Already theirs; no novelty claim |
| One pure-gauge birth and a disjoint tiny rim perturbation pass the earlier tests and fail the final test | Y 72375–72432, proved there using the stated real averaging and background estimates | Ported one-operation example, with those estimates as inputs |
| Earlier stage comparisons give an inset conclusion; the outer joining collar needs separate control | Y 72243–72322; SA 17612–17630, sketched conditional stage comparison | No replacement of local layer units by top units |
| Failed operations may repeat after a new wait | SA 17575–17585, 17610, cited construction rules | Repetition is allowed; no mass lower bound is stated |
| Frame averaging and the reference draw occur after preparation | Y 63836–63860; SA 17585–17608, definition and exact splitting argument | A stage failure has not drawn that reference law |
| Later spaces on stopped nests need an application-specific supply | I 49495–49546, expressly an application condition; Bałaban CMP 122a p. 191 cited as printed | Admission is an input, not a probability estimate |
| Per-mark allowance $q_t=C_{\rm cnt}T_t\widehat r_t$ suffices | `in1.md` (31)–(32), lines 484–527; `hc-mark.md` §2, conditional proof | The consumer needs a weighted continuation estimate |
| Quiet eligible components are nonwrapping boxes with outer room; old mark reads enter the later floor | Y 63684–63694, 63738–63770, 78408–78435, proved from the stated region rules | Ported geometry; does not assert that a field realizes a proposed record |
| Move kernels are normalized, but the component's coordinate integrand retains its normalizers | SA 17499–17514, proved from the defined moves; SA 18026–18042, cited coordinate convention | The two masses cannot be identified without their factors |
| Stability uses termwise majorants and a loaded label bound | I 157028–157085, hypotheses h1, h5–h6 of a conditional theorem | Cited inputs, not a restricted-history lower bound |

The question is about `hc-mark.md` (4), with its actual kernels,
normalizers, stored data and exterior compatibility. A failed indicator
at one fixed evaluation is not yet a lower bound for the integral of
all paths reaching the next failed indicator.

## 2. Which rim is tested

Put $\tau_m=3(1-\beta_s/2)\varepsilon_mL^{-2m}$.
Consider an eligible component whose preparation reaches its final stage.
Use the literal full test, not the inset implication.
At a flat outer face choose the bare plaquette in Y 72327–72334.
Its four bonds are determining bonds of the localized level-zero layer.
Write $b_1,\ldots,b_4$ for the four top bonds which they lift.
The ordered product is

\[
 \partial U^{\rm loc}(p)
   =V_m(b_1)V_m(b_2)V_m(b_3)^{-1}V_m(b_4)^{-1}
   =\partial V_m(p_m).                                      \tag{1}
\]

Changing the stage variables cannot change (1) at fixed top rows.
This statement concerns the norm of the holonomy if a common gauge
conjugation is present. It is independent of the minimization inside.
The first-member collar convention leaves these bare bonds in place
(Y 72335–72338).

The operation rule applies again after a drop-out. It has no exception
for the last test of a renewed operation (Y 63836, 63862; SA 17610).
Quarantine puts the earlier mark below the new preparation bottom.
The full old read halo then lies in the new floor (Y 78408–78435).
It does not replace the new outer determining rows.
Thus **every renewed operation that reaches the final stage has this
rim test**, under the same nonwrapping quiet-box geometry.
An operation which stops earlier never executes it. This distinction
matters in a probability calculation.

Earlier tests do not *universally imply passage* of this last test.
The first-operation example Y 72375–72432 is already a counterexample
to that implication, including its retained constraints and gauge
support. Its earlier stages read away from the outer joining collar
(Y 72416–72419). The carried density bound at the top is of order
$\varepsilon_m$, not $\varepsilon_mL^{-2m}$
(SA 17624; Y 63876).
At a later operation the old read halo is in the floor, as above.
These facts rule out the suggested automatic payment by the earlier
ordinary test on the same rim.

There is a stronger assertion in finding 9 which does **not** follow:
that the conditional distribution of this top plaquette, after all
earlier outcomes, still fluctuates on scale $g_m$.
Failure of a deterministic implication supplies no lower bound on
that conditional fluctuation scale. Nor does a counterexample with
defect $8\varepsilon_mL^{-2m}$ prove that defects of order $g_m$
reach every final stage with large mass.
This does not rule out a quasi-invariance proof without a density bound.
The check proposes that route, modulo a relative margin lemma.
The second round finds additional scaling and noncommuting-shift
obstructions; see hcm-r2.md §§3–8.

## 3. The conditional law and the order of quantifiers

Fix all exterior determining rows of the final-stage rim, as HCM-R
allows. Conditional on reaching that stage, its failure probability is
exactly

\[
 \mathbf1\{\|\partial V_m(p_m)-1\|\ge\tau_m\}.                \tag{2}
\]

For flat rows it is zero. For rows beyond the threshold it is one.
There is no uniform assertion that it tends to one over these fixed
data. One must instead estimate the mass of reaching suitable data,
and then reaching the next such state without a funded exit.

The distinction between two source measures is essential here.
SA 17499–17514 defines normalized *move kernels* on the full state.
Tests and deletions are such moves. Deleting a variable does not draw
a new Wilson field. In contrast, the component integral in
SA 18026–18042 uses Haar–Lebesgue coordinates and retains every
Gaussian normalizer, gauge normalizer and elimination determinant in
its integrand. These are the factors majorized in HCM-R (3a).
The reference law of Y 63856–63860 is drawn only after preparation
and the central integration. A final-stage regularity failure occurs
before that draw. It cannot use that reference law as its incoming law.

There is also no infinite terminal horizon with the birth coupling
held fixed. IN1 (1), with $\theta_K\ge X_0$, gives

\[
 K-h\le\frac{\theta_h-X_0+c_5}{\underline\lambda}.             \tag{3}
\]

This follows by rearranging
$\underline\lambda(K-h)-c_5\le\theta_h-\theta_K$.
It does not prove HCM-R. It does invalidate the particular limit
“terminal level tends to infinity while this birth balance is fixed”
at fixed $\theta_h$. Uniform failure must use a family with growing
birth coupling, or another explicitly admissible family, and compare
its mass with its own balance.

Finally, $\theta_m g_m^2=1$ is an energy scale, not a mass estimate.
For a specified plaquette of defect $ag_m$, IN1's Wilson convention
gives energy $a^2/2$. It gives no lower bound on the volume of field
configurations producing that defect with the other indicators equal
to one. The same issue remains for the smooth low-action family
already constructed in Y.

## 4. The lower bound that would refute every majorant

Here is a precise test of the proposed refutation. It uses the kernels
of `hc-mark.md` (3a), without replacing their reference measure.

Fix one compatible real exterior evaluation and the stored inner data.
Let $\mathcal Q_K$ be a measurable family of continuations from the
first unpaid rim stop to terminal level $K$. Every path in this
family has one lineage, no funded event and no healing. Take a fixed
region record, so its continuing volume is a fixed number $v_K$.
Let $M_K$ be the integral over this family of the products of the
actual absolute kernel factors. Include their normalized frame weights,
Jacobians and normalizers. Exclude the initial paid factor and exclude
the explicit volume price. Old factors are counted only where (3a)
counts them. This is an unweighted mass, not necessarily a probability.

**Majorant lower-bound lemma.** For every admissible choice of the
common majorants $H_\rho$, `hc-mark.md` (4) implies

\[
 e^{B_h}\ \ge F(s_{\rm first\ rim})
       \ \ge e^{(c+c_{\rm ent})v_K}M_K.                       \tag{4}
\]

Indeed, iterate $a+TF\le F$ through the finitely many remaining levels.
Discard all paths outside $\mathcal Q_K$. Every remaining kernel
and weight is nonnegative. At its terminal state use $F\ge1$.
At each integration use $H_\rho\ge|J_\rho|$ at the one compatible
real evaluation, where $J_\rho$ is the actual new factor.
Repeated nonnegative integration gives (4). The factors
$e^{\kappa_1\Delta N}\ge1$ may be dropped. This proves the lemma.
It is uniform in $H_\rho$ precisely because the lower bound uses
actual factors at a compatible evaluation.

Only a sufficiently large mass lower bound is missing from this
argument. Positive mass by itself is insufficient.

Name that input **RIM-LB (actual rim-history mass lower bound)**.
All the other domain and kernel inputs of HCM-R are held fixed.
The following concrete version would suffice:

* For arbitrarily large $\Theta$, choose an admissible frame with
  $\theta_{h+s}=x_{h+s}=\Theta-\lambda s$,
  $\underline\lambda\le\lambda\le\overline B$, and
  $0\le s\le D=\lfloor\Theta/(2\lambda)\rfloor$.
  Take $[\Theta/2,\Theta]$ in one rounded-radius plateau, with
  radius $R$, and a torus large enough for all the read sets.
* Supply a paid birth with $E_h^{\rm pay}\le C_0P_h^2$, and an
  actual positive-mass family $\mathcal Q_\Theta$ of the kind above.
  Its repeated attempts follow the quiet single-lineage schedule.
  The first is at $h+R$, subsequent ones are $R+1$ levels apart.
  They reach and fail their final rim tests. All other exits are absent.
* In the exact coordinates and with one compatible exterior history,
  its mass satisfies
  \[
    M_\Theta\ge e^{-C_*v_\Theta},\qquad
    v_\Theta\ge(D-R-1)[1+\log(\Theta/2)](MR)^4.                \tag{5}
  \]
  The finite constants $C_0,C_*$ are independent of $\Theta$,
  absolute level, cutoff and terminal level. IN1 row 7 already fixes
  $c=C_vc_r$ and $c_{\rm ent}$. The bound must satisfy
  $C_*<c+c_{\rm ent}$ for those constants. The refuter cannot increase
  $c$ to obtain this inequality. All constants precede the last floor $X_0$.

This asks for much less than continuation probability near one.
It still requires the complete mass, including the cost of reaching
each final test. No other registry row supplies this specialized
lower bound; a general common-envelope upper bound is not (5).

**Consequence of RIM-LB.** Keep IN1's fixed $c$ and $c_{\rm ent}$.
Assume $C_*<c+c_{\rm ent}$, then choose the final floor and $\Theta$.
The already proved schedule calculation in
`hc-mark.md` §6.1 gives

\[
 \frac{v_\Theta}{P_h^2}
 \ge b_0\frac{\Theta}{(\log\Theta)^{2p_0-4r-1}}
       \longrightarrow\infty.                              \tag{6}
\]

Here $b_0>0$ is fixed. Equations (4) and (5) would give
$B_h\ge(c+c_{\rm ent}-C_*)v_\Theta$, whereas
$B_h=E_h^{\rm pay}-q_h-2P_h\le C_0P_h^2$.
This contradicts (6). It would refute HCM-R for **every** admissible
majorant. The finite-terminal weighted masses would be unbounded
across this admissible family. No assertion about an infinite horizon
at a fixed birth coupling is needed.

IN1 (31) would remain a valid conditional counting inequality.
Its use in (32) would lack the mark payments
$q_t=C_{\rm cnt}T_t(4c_1M^4R_t^5+\kappa_1)$.
The original birth cannot finance (6). These are consequences of
RIM-LB; (5) has not been established by the ported example.

## 5. Three routes to RIM-LB

These test the proposed *refutation*. They are different from the
three payment routes already exhausted in `hc-mark.md`.

### Route 1: conditional small-field fluctuations

Suppose the incoming normalized law, conditional on the previous
outcomes, wrote the rim logarithm as $g_mX$, with $X$ having a density
bounded by a fixed constant in three-dimensional Lie algebra coordinates.
In a fixed small logarithm chart, $f=\|e^{ig_mX}-1\|\le\tau_m$ implies
$|X|\le2\tau_m/g_m$. Integration over that ball would give

\[
 \Pr(f\le\tau_m\mid\text{past})
       \le C(\tau_m/g_m)^3
       \le C'P_m^3L^{-6m}.                                  \tag{7}
\]

This is a valid elementary deduction from the stated density bound.
If the conditional probability of any other exit were also bounded
at each step, a union bound would control a whole finite chain.
One would still need a lower bound on the unnormalized kernel masses
to pass from this probability calculation to (5).

These conditional estimates are not supplied by “typical size $g_m$”.
The incoming law is conditioned by the old tests and deltas.
At fixed rim rows it is the point mass in (2). The normalized Wilson
reference draw occurs too late. Ordinary failed-test energy
certificates are pointwise statements; they do not on their own give
uniform conditional tail probabilities through arbitrary stopped data.

Here is an exact test of the inference from low energy and support.
For $P_m>2$ and $\tau_m<g_m$, let $B_0$ be the SU(2) ball
$f<\tau_m/2$, and let $B_1$ be the annulus $g_m<f<2g_m$.
Both have positive Haar measure. For any $0<\alpha_m<1$, form
the mixture of their normalized Haar restrictions with weights
$1-\alpha_m,\alpha_m$. All its fields pass the ordinary bound
$f<\varepsilon_m$, and their single-plaquette Wilson energy is
at most $2$. Its support does not obey the final rim bound.
Yet its rim-failure probability is exactly $\alpha_m$, which
may tend to zero at any rate. This is a counterexample to the stated
inference, **not** a proposed Yang–Mills history law.

**First failed step of this route:** identify and bound the actual
conditional outgoing-row law, including the probability of reaching
the final stage. The two geometric checks do not supply (7) or (5).

### Route 2: a single smooth field for several candidate rims

There is a useful deterministic extension of the source's affine
example. Fix finitely many proposed renewal levels
$m_0<\cdots<m_J=m_*$, with their offsets and frame values fixed.
Let $e_*=\max_\ell\varepsilon_{m_\ell}$. In level-$m_*$ units use
the source's commuting potential, affine on a box containing all the
candidate four-block carriers, with coefficient

\[
 a_*=16e_*L^{2m_*-4m_0}.                                    \tag{8}
\]

Cut it off outside a larger box. The averaging calculation is ported
from Y 72340–72367; it is not repeated here. At candidate level
$m_\ell$ its plaquette angle is exactly

\[
 a_\ell=a_*L^{-2(m_*-m_\ell)}
        =16e_*L^{2m_\ell-4m_0}.                             \tag{9}
\]

Translate every level by a common large integer $b$, retaining the
fixed differences and coupling values. Then $a_*\to0$.
For $a_*\le1$, the elementary bound
$2\sin(a_\ell/2)\ge a_\ell/2$ gives

\[
 \|\partial V_{m_\ell}-1\|
   \ge8\varepsilon_{m_\ell}L^{-2m_\ell}>\tau_{m_\ell}.       \tag{10}
\]

Thus all the proposed lifted plaquettes can fail on averages of
**one** bare field. There is no algebraic incompatibility between
these particular coarse holonomies. Its bare action is at most
$C a_*^2$, by the source's cutoff calculation. The constant is
fixed for this finite list and box. An affine frame prefix has bare
coupling $O(1+b)$, so its Wilson exponent still tends to zero.

This is not a proof that the actual operation realizes every mark
on that list. A full realization must also pass each intervening
ordinary, stage, collar and kept-coordinate test with the actual
retained data. The source proves that verification for its first
operation, not for this whole list. In particular one must check
the old guards on their complete footprints; Y 77526–77552 retains
them at a failed prospective test. A small value of the action in
(8) does not remove those indicators.

Even granting such a strict finite realization, continuity gives
only positive mass. In a regular free-coordinate chart, a positive
continuous density $j$ near a point $z_0$ obeys

\[
 \int_{B(z_0,\delta)}j\,d\mu
       \ge\tfrac12j(z_0)\,\mu(B(z_0,\delta))>0              \tag{11}
\]

for a sufficiently small ball contained in all the strict tests.
This is the appropriate argument for positive weight; the commuting
ansatz itself has zero ambient Haar measure. But neither the radius
nor the density lower bound in (11) has been bounded in terms of
$v_\Theta$. A ball preserving a rim margin of order
$L^{-2m_0}$ can give a bound with a loss proportional to $m_0$
per restricted coordinate. That bound is useless for (5), whose
constant must be independent of the absolute level.

**First failed step of this route:** turn a simultaneous field
witness into the complete history family and a mass estimate at the
rate in (5). A finite open neighborhood, even if all its tests are
checked, does not provide that rate.

### Route 3: choose the exterior in the mass supremum

Choose exterior rows so that the last rim indicator is certainly
negative. This removes no cost of reaching that indicator.
At such an evaluation $p$, let $A_{\rm pre}(p)$ be the event
that the entire preceding segment reaches the intended last stage.
Let $J(p,z)\ge0$ be its complete real kernel density, using the
positivity input. Its contribution is

\[
 Z(p)=\int J(p,z)\,d\mu(z),\qquad
 M_-(p)=Z(p)\,Q_p(A_{\rm pre}(p)),\quad
 dQ_p=J(p,z)d\mu(z)/Z(p),                                   \tag{12}
\]

when $0<Z(p)<\infty$. The conditional final failure is one.
The two quantities on the right of (12) remain to be bounded below.
The envelope inequality gives $\int H\ge M_-(p)$.
It gives no numerical lower bound for $M_-(p)$.

The same issue survives a proof that all the conditional continuation
probabilities are close to one. The actual segment integral includes
its $Z$. A normalized law is unchanged when its density is multiplied
by a positive constant. Its unnormalized mass is changed by that
constant. Hence a normalized-law estimate alone cannot bound the
product of these masses. A loss $e^{-C_*\Delta V}$ suffices only if
$C_*<c+c_{\rm ent}$ for IN1's already fixed $c=C_vc_r$.
Establishing such a rate is the normalization clause of RIM-LB.
Y 77545–77549 removes the interrupted stage's own normalizer,
but retains the prefix's factors in their birth coordinates.

One may choose a different exterior for a different finite horizon.
Within each claimed history, the rows must still satisfy the stored
averaging constraints and successive state maps. Choosing unrelated
favorable top data separately at each renewal does not construct
such a history. The single-field attempt (8) addresses part of this
compatibility problem, but supplies no lower bound for (12).

IN1 H-E, (16), is an upper-envelope assumption. It supplies neither
factor on the right of (12) from below. The complete account's
stability theorem likewise assumes its termwise majorants and loaded
label sum (I 157028–157085, hypotheses h1, h5–h6). Its conditional
proof is not a lower bound for this restricted history family.

**First failed step of this route:** bound the complete compatible
prefix mass in (12) by $e^{-C_*\Delta V}$, uniformly through the
successive stopped states. Taking an exterior supremum cannot replace
this estimate.

## 6. What this adds, and what it does not

Sussman and Alpoge already identify the scale mismatch for top data
obtained by averaging a low-action bare field. They also give a birth,
earlier passed tests and a final failure with vanishing fresh payment
(Y 72340–72432). None of that is a new counterexample here.

The additional results are narrower. The same literal test applies
to a renewed operation when its final stage is reached. The majorant
comparison (4) states exactly which lower bound would refute HCM-R
uniformly in its admissible envelopes. Equation (3) fixes the horizon
quantifiers. Equations (8)–(10) put several candidate failing rim
holonomies on one smooth bare field, without asserting that its whole
stopped history has been realized. The probability and normalization
arguments show why those facts still do not prove (5).

No earlier passed test has been identified which pays the rim failure.
No unused credit has been found which proves HCM-R. Conversely, no
complete positive-weight repeated-history family with the required
mass lower bound has been proved. The stronger “failure is typical”
claim in finding 9 remains an input. Finding 10 proposes a change to
the rim construction; it is not a proof about the literal test studied
here, and no such change is made.

Stop **(c)** is therefore the appropriate outcome. The single open
lemma is **RIM-LB**, including the actual-history realization and the
uniform mass rate (5). The three failed routes are conditional
small-field concentration, a smooth field with a positive-neighborhood
argument, and a favorable exterior evaluation in the mass supremum.
They do not establish either truth or falsity of HCM-R (4).

| Claim | Status | Scope or source |
|---|---|---|
| Bare lifted rim holonomy and its literal threshold | Ported from Y 72324–72338 | Identity at the final stage |
| The same rim test is present at a renewed final stage | Proved here from the cited construction, §2 | Conditional on reaching that stage in the stated quiet-box geometry; Y 63836, 63862, 63738–63770, 78408–78435 |
| Earlier passing tests do not universally force final-rim passage | Ported from Y 72375–72432 | One actual first-operation counterexample; no conditional-law assertion |
| Averaged low-action field with vanishing fresh payment | Ported from Y 72340–72432 | Already theirs, not new here |
| Fixed exterior makes the tested holonomy deterministic | Proved here, (1)–(2) | Does not estimate the prefix mass |
| Remaining horizon is bounded at fixed birth coupling | Proved here, (3) | Input: IN1 frame inequality (1) |
| A path-mass lower bound applies to every admissible majorant | Proved here, (4) | Input: actual compatible kernels and HCM-R's domination convention |
| RIM-LB would refute HCM-R and the proposed old-birth financing | Proved here, (4)–(6) | Conditional; uses the schedule count already proved in `hc-mark.md` §6.1 |
| Several candidate failing rims can be averages of one smooth field | Proved here, (8)–(10), using the affine averaging calculation ported from Y 72340–72367 | A field construction, not a complete stopped-history realization |
| A strict regular finite-coordinate realization has positive mass | Proved here, (11) | Requires positive continuous density and strict indicators; no uniform rate |
| Low energy and support alone imply a useful rim-failure probability | Refuted as an inference, §5 route 1 | The mixture is not a Yang–Mills history law; it does not refute a quasi-invariance argument. A probability estimate still needs the normalization comparison (12) to imply (5) |
| Full admission, kernel supply, ordinary owned gains and H-E | Input | Held at their existing scopes; their other registry rows are not reopened |
| **First open input: RIM-LB, the complete compatible repeated-rim history mass bound (5)** | **Input — open after three routes** | **No proof or refutation of HCM-R; no unconditional divergence or IN1 closure** |
