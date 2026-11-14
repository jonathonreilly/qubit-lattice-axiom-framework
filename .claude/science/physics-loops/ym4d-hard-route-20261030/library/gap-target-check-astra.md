## Repo search

Terms: `Ky Fan`, `L[oö]wner.Heinz`, `Loewner.Heinz`, `Cordes`,
`SUPER-D`, `DEF_K`, `VIR.log`, `gap-target-check-astra`; then
`Bessel.{0,60}monoton`, `I_n/I_1`, `log.majori[sz]`,
`Schwinger.Dyson.{0,50}plaquette`, `plaquette.{0,50}loop.equation`,
and `force[ -]form\b`. Both searches covered Markdown and TeX on all
five requested refs in `/Users/jonreilly/Projects/Physics`, including
outside this lane. They returned 49 and 26 lines, below their caps of 100.

| Ref | Commit read |
|---|---|
| `origin/main` | `4d88da5504d356762deb6b1a1c2695336af9fb81` |
| `pr/10114` | `f76f6c649cff7dffbab664d8976e680e8f287fe9` |
| `pr/10133` | `89faef229ff6e6bde42baad15ed8270c2f4087d8` |
| `pr/10134` | `1e70c7211a2cdbc39001e619f1dd89db45e25851` |
| `pr/10141` | `c73ad7b177d94f89ff37b77386936e3d52b48b05` |

Relevant hits and source statements:

| File and lines | Statement and closeness |
|---|---|
| `origin/main:research/mass-gap/library/gap-mid-max.md:118–172` | `(DEF_K)` is `D_i'>=-K D_i` for **every individual ordered level**. Remark LEV makes its integrated form sufficient for Theorem TR; `(VIR-log)` asks a thermal derivative bound with a specified integral budget. This is the exact prior target. The blob is identical to this checkout's row 708 note; reused, not reproved. |
| `origin/main:research/mass-gap/library/gap-mid-check.md:35–41` | The prior check confirms Remark CH's characteristic-curve restriction and Remark LEV's termwise sufficient condition. It checks row 708, not Section 6 of row 913. It supplies no existing check of this task. |
| `origin/main:research/mass-gap/library/{gap-crux-fp,gap-flux-exercise,gap-form-exercise,gap-skeleton-final}.md` and `ROWS.md` | These hits repeat row 708's open deficit/transport target and its failed routes. They are locators to the preceding source, not additional proofs. The `prior/gap-vir-lit.md` and `prior/gap-fullread-1.md` hits likewise point to action sum rules and loop equations without a supplied level-rate bound. |
| `origin/main:archive/notes/docs/GAUGE_SD_LOOP_EQUATION_BETA_COUPLED_PLAQUETTE_BRACKET_NOTE_2026-07-10.md:90–108` | Haar differentiation of `Tr(UV)` gives a Wilson staple identity: `C2<Tr(UV)> = -(beta/(4N)) sum_p <Tr(UVUK_p)-(Tr(UV)Tr(UK_p))/N-Tr(UVK_p^dag U^dag)+(Tr(UV)Tr(K_p^dag U^dag))/N>`. The text uses SU(3), `C2=4/3`. Same integration-by-parts method as F, different trace/metric normalization; it gives no thermal or vacuum-subtraction estimate. Its numerical validations are not used. Located through the method search's archive-ledger pointer and a capped follow-up; the actual formula was read. |
| Local `gap-q8test-opus.md:157–180` (row 843) | Lemma 3.1 proves `I_(nu+1)/I_nu=E[u]` and its derivative `Var(u)>0` for `nu>-1/2, b>0`. This supplies the recalled Bessel monotonicity. Its existing row 854 check is read at `gap-q8test-check-astra.md:233–250`; no new Bessel attack is needed. |

The four PR refs gave no relevant exact-target hit. Their broad method
hits were archive pointers and unrelated Bessel-in-time statements, not
the coupling-ratio theorem. Searches found no earlier Ky Fan/ABS check
or Löwner–Heinz proof under these terms. A wider, capped loop-equation
search is used only as a locator, never as absence evidence.
Full bounded-search logs are in
`/tmp/gap-target-check-astra-20261113.pYDwkh/repo-{exact,method}-search.txt`.

The target-specific prior file is absent. The November 8 search digest
was read; it concerns earlier ultraviolet targets, not these statements.
The registry has no matching target, thermal-transport, Bessel or Araki
row. FINISH 914 is this check; the author separately proposes an Araki
rebuild and FINISH 915 owns a broader literature read. Neither is run here.
No duplicate check was located, and no open proof target is taken over.

Index first: `sa-index/README.md`, matching chunk-02 rows and their
neighbours (78–105), and `obligations.md:50–74`. Then read outline
2195–2257 and 2313–2335 at the supplied `31a47c543775`: GL3–GL4 prove
the convolution spectrum and decay; GL8 constructs the gauge-projected
transfer trace. CA-II 141025–141120 supplies the corresponding layer
integral construction. These are credited to Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their text. They are reused,
not recast as new work. No Balaban lemma is consumed by Section 6.

Provenance: OpenAI Codex, task-dispatched gpt-6-astra/xhigh;
checkout `32d4b2c3fdcd5d4d64cb641fca9629e067c611bd`, 2026-11-13.
Research-text check of row 913, not an audit; no scientific status is granted.
Only this report is being written. No numerical or computer-assisted proof.

### Completed check and remaining obligation

Read Section 6 line by line, the author's Section 7 corrections, and
the named source passages. The requested checks are complete.

| Statement | Verdict |
|---|---|
| Lemma F, including its thermal/twist applications | HOLDS AFTER CORRECTION |
| Lemma KF | HOLDS |
| Bessel-ratio monotonicity and Löwner–Heinz as used | HOLDS |
| Theorem ABS and (AN) | HOLDS AFTER CORRECTION |
| Identity 6.4 and `(KF-LEV)` iff `(SUPER-D)` | HOLDS |
| Finite magnetic-step interpretation | HOLDS AFTER CORRECTION |
| “Exactly row 708's `(DEF_K)`,” and “equivalent to `(VIR-log)`” | FAILS |

The remaining Wilson obligation is a bound on the vacuum-subtracted
response with the seed's rate budget. This report proves no such bound
and changes no ledger, registry, FINISH row or source text.

## 1. Lemma F — HOLDS AFTER CORRECTION

The local identities F1–F3 and the subtraction identity in F4 hold.
The thermal application needs its volume/time factor written explicitly.
The twisted application needs the force of the twisted action.

At source lines 251–255, each plaquette reads four distinct link variables.
For each one, write its trace as `x_p=<q,w_p>`, including reversed links.
On the unit three-sphere,
`grad x_p=w_p-x_p q` and `Delta x_p=-3x_p`.
Thus the four-link Laplacian is `-12x_p`, and
`<grad_e x_p,grad_e x_q>=<w_p,w_q>-x_p x_q`.
The first term is the trace of the two staples joined with opposite
orientations. This fixes the orientation implicit in `p v q`; for `p=q`
it is 1. There is no extra factor from the normalized trace.

Haar integration by parts against `exp(-b A_eps)` gives
`omega(Delta_e f)=b omega(<grad_e A_eps,grad_e f>)`.
Since `grad_e A_eps=-sum_q eps_q grad_e x_q`, summation gives exactly
`12 omega(x_p)=b omega(Phi_p^eps)`. A finite-bond DLR conditional law gives
the same identity. Local smooth integrands are bounded, so weak limits
preserve it. This includes signed-plaquette presentations of twists.

For two states of the same action, subtraction is literal. For different
twists, use each state's own `Phi_p^eps`. The needed global formula is

```math
\sum_p\epsilon_p\Phi_p^\epsilon
=\sum_e\left|\sum_{p\ni e}\epsilon_p\nabla_e x_p\right|^2
=|\nabla A_\epsilon|^2.
```

In particular F4's unsigned sum holds when every sign is 1. Write
`Q_t=|grad A_0|^2` on the time-t torus and
`q_infinity=lim_(n to infinity) omega_n(Q_n)/n` on the fixed spatial box.
At the differentiability points supplied by row 708, Lemma 4.2,

```math
\partial_b G(t;B;b)
=\frac b{12}\{\omega_t(Q_t)-tq_\infty\}
=\frac b{12}\,6t|B|\{\overline Q_t-\overline Q_\infty\},
\qquad \overline Q_t=\frac{\omega_t(Q_t)}{6t|B|}.
```

Thus `(b/12)` multiplies the *time-matched total-force difference*.
If “mean squared force” means per plaquette, the source omits `6t|B|`.
For the twist ratio on the same finite torus the precise formula is

```math
\partial_b\log\frac{Z_\epsilon}{Z_0}
=\frac b{12}\left\{
\omega_\epsilon(|\nabla A_\epsilon|^2)
-\omega_0(|\nabla A_0|^2)\right\}.
```

Multiplication by `eps_p` before summing is essential. The sheet-moving
version in row 899, (T1), gives this same formula. These identities bound
neither difference. The small-b single-plaquette check has coefficient
`b/4`; the displayed large-b discussion is only an asymptotic check and
is not independently verified here or used as a proof input. The
degree-two adjoint harmonic has eigenvalue
`-8` on each sphere, hence `-32` for its four-link plaquette. The U(1)
version uses `-1` per circle, hence 4 in place of 12. Both remarks hold.

## 2. Lemma KF — HOLDS

Source lines 260–265. Put `x_i=D_i(s')`, `y_i=theta' D_i(s)` and
`A_m=sum_(i<=m)(x_i-y_i)>=0`. For each finite N, convexity gives

```math
\sum_{i=1}^N(e^{-t y_i}-e^{-t x_i})
\geq\sum_{i=1}^N t e^{-t x_i}(x_i-y_i)
=\sum_{m=1}^{N-1}(c_m-c_{m+1})A_m+c_NA_N\geq0,
\quad c_i=te^{-t x_i}.
```

Ordered `x_i` make the coefficients nonnegative. The source's convention
`c_(N+1)=0` is precisely the last term, not an illicit infinite boundary
term. Monotone convergence of the two nonnegative exponential sums proves
the result. For Wilson transfer operators they are finite for every `t>0`:
the outline's factorial decay (GL3–GL4) makes the finite link tensor
product lie in every positive Schatten class; multiplication by bounded
spatial factors and restriction to a sector preserve this property.

With `theta'=exp(-integral_s^s' K)`, substitute `t/theta'` for t.
This gives the transport conclusion used in Theorem TR. This is a
sufficient condition, not a necessary condition for thermal transport.

The explanatory sentence at line 266 is inaccurate: individual ordered
eigenvalues also have variational characterizations (min–max). The
max-determinant formula stated for the product of the top k eigenvalues
is correct. This wording does not affect Lemma KF.

## 3. Theorem ABS — HOLDS AFTER CORRECTION

Both (AN) and (ABS) hold for the stated Wilson SU(2) operators. The
operator-order sentence in step (5) is false; the author's Section 7
already supplies its valid spectral repair. Both recalled inputs are
correct in the form used. No numerical guide is needed.

**Spectrum and normalization, lines 249, 269.** Outline 2195–2257
already proves the one-link coefficient
`c_j(b)=2 exp(-b) I_(2j+1)(b)/b`, including its positivity and factorial
decay. Divide the product kernel by `c_0(b)` once per spatial link.
This gives exactly `Khat_b`, not the unnormalized convolution.
The outline's GL8 and CA-II 141060–141102 identify integration of the
temporal links with vertex gauge averaging. Since the convolution and
spatial multiplication commute with this projection, restriction to
gauge-invariant functions gives the stated transfer operator. The
outline uses `K^(1/2) M K^(1/2)`; it has the same nonzero spectrum as
`M^(1/2) K M^(1/2)` by the `C*C, CC*` identity.
Centre-cut flips commute with both factors and the gauge projection,
so the same arguments restrict to each electric-flux sector.

These are finite spatial boxes. `W` is bounded and nonnegative, so
`M_b` is boundedly invertible, even though the positive compact kinetic
operator has no bounded inverse. No inverse of that kinetic operator is
used. Excitation energies for the *full* thermal sum must be measured
from the global vacuum, not separately reset to each flux sector's top.

**Bessel-ratio recall — HOLDS.** Reuse `gap-q8test-opus.md:157–180`,
Lemma 3.1, and its prior check `gap-q8test-check-astra.md:233–250`.
The written proof gives, for `nu>-1/2` and `b>0`,

```math
r_\nu(b)=\frac{I_{\nu+1}(b)}{I_\nu(b)}
=\mathbb E_{\nu,b}[u]\in(0,1),\qquad
r_\nu'(b)=\operatorname{Var}_{\nu,b}(u)>0,
\quad d\mathbb P_{\nu,b}\propto e^{bu}(1-u^2)^{\nu-1/2}du.
```

Its beta-integral and integration-by-parts proof has the required
vanishing endpoint term. All indices here satisfy its domain.
Thus `I_n/I_1=product_(nu=1)^(n-1) r_nu` is strictly increasing and
lies in `(0,1)`. Each `eps_n` is positive and strictly decreasing.
This verifies the author's recollection for *every* n, not only spin 5/2.

There is a small domain detail missing from Section 6: the infimum
defining theta is strictly positive at each finite `0<b<b'`.
To check it using the outline's existing series, write

```math
I_n(b)=\frac{(b/2)^n}{n!}L_n(b),\qquad
1\leq L_n(b)\leq\exp\!\left(\frac{b^2}{4(n+1)}\right).
```

The upper bound follows termwise from
`n!/(n+k)! <= (n+1)^(-k)`.
Consequently `eps_n(b')-eps_n(b)=-n log(b'/b)+O(1)` while
`eps_n(b)>= (n/2) log(n/2)-O(n)`. Their ratio tends to 1.
The remaining finitely many positive ratios have a positive minimum.
Hence `0<theta(b,b')<1`. This avoids a zero-power compactness ambiguity.

**Löwner–Heinz recall — HOLDS.** The precise statement is
`0<=A<=B => A^theta<=B^theta` for bounded positive operators on a
Hilbert space and `0<theta<=1`. It does not require commutation or a
bounded inverse of A. The primary read is Moslehian and Najafi,
[An extension of the Löwner–Heinz inequality](https://arxiv.org/pdf/1207.2864),
pp. 1–2, especially (1.3). One can check the needed statement directly:
`A/(lambda+A)=I-lambda(lambda+A)^(-1)` increases in A for every
`lambda>0`; integrate it against the positive weight
`(sin(pi theta)/pi) lambda^(theta-1) d lambda`.
The resulting norm-convergent integral is `A^theta` for `0<theta<1`.
The endpoint theta=1 is immediate. Thus the use on
`X^2<=Y^(-2)` is legitimate: here `Y=M^(1/2)` is invertible.

**Steps (1)–(4), lines 270–272 — HOLDS.** All link spectral projections
are independent of b, so `Khat_(b')<=Khat_b^theta` follows coefficient
by coefficient. Conjugating this order inequality by `M^(theta/2)` is
valid. Eigenvalue order follows from min–max on the invariant sector.
The log-majorization has the direction printed in the source. Indeed,
put `c=||XY||` for positive X,Y with Y invertible. Then
`X^2<=c^2 Y^(-2)`. Löwner–Heinz gives
`Y^theta X^(2theta) Y^theta<=c^(2theta) I`, hence
`||X^theta Y^theta||<=||XY||^theta`.
With `X=Khat^(1/2), Y=M^(1/2)` this is the top-eigenvalue comparison.
Apply the same argument to the kth exterior powers. They preserve the
products and positive powers here; their norms are products of the top
k singular values. All the relevant products are compact. Taking
negative logarithms gives (AN). This checks the existing argument;
it does not open the separately proposed Araki-rebuild task.

**Step (5) — correction required, already identified at line 298.**
`M` decreasing does not imply `M^(1/2) Khat M^(1/2)` decreases in
operator order. Instead use its isospectral positive operator

```math
R(b_s)=\widehat K^{1/2}M_{b_s}\widehat K^{1/2}.
```

This operator decreases in `b_s`, so its ordered eigenvalues decrease
and every ordered absolute energy increases. Since `s'>=theta s`,

```math
\mathcal E_k(s',s')\geq\mathcal E_k(s',\theta s)
\geq\theta\mathcal E_k(s,s).
```

This proves (ABS) in every sector without the false operator-order claim.

**Rate sentence, line 274 — HOLDS for SU(2).** The finite comparison also
implies the stated differential electric-rate bound. On a compact
positive b-interval, the same series estimate is uniform in n. The
identity `I_n'/I_n=n/b+r_n` bounds `|eps_n'|` by `(n-1)/b+1`.
Thus `-eps_n'/eps_n` tends uniformly to zero as n grows; the supremum
`K_el` is finite and continuous there. Integrating
`eps_n'>=-K_el eps_n` gives
`theta(s,s')>=exp(-integral_s^s' K_el)`.
Since the absolute energy sums are nonnegative, (ABS) implies their
transport bound with this latter factor. The two factors need not be equal.
An extension to other compact groups still needs the analogous positive
kinetic spectrum, monotone ratios and compactness hypotheses; it is not
an unconditional theorem about every possible class weight.
The cited continuous-time comparison at 3c.3(ii) is correct:
for `h=lambda K_E+xW`, `x e_i'=x<W>_i` lies between 0 and `e_i`.
It is a structural comparison, not an identification of that Hamiltonian
with the finite-step Wilson logarithm.

## 4. Identity 6.4 — HOLDS

Source lines 276–280. Set `H_m=sum_(i=1)^m D_i` and
`mathcal E_k=sum_(i=0)^(k-1) Ehat_i`. Then
`H_(k-1)=mathcal E_k-k mathcal E_1`. Substitution gives exactly

```math
H_{k-1}(s')-\theta'H_{k-1}(s)
=\mathrm{Dfc}_k-k\mathrm{Dfc}_1
+(\theta-\theta')H_{k-1}(s).
```

Thus `(SUPER-D)` is equivalent to `(KF-LEV)` for the same pair of
couplings and the same theta'. This is finite algebra. It needs no
interchange of an infinite sum. Nonnegativity of each `Dfc_k` uses ABS
with its spectral repair, but is not needed for the identity itself.

**The explanation at line 281 — HOLDS AFTER CORRECTION.** The three
nonnegative contributions exist at the level of absolute Ky Fan sums.
Insert the intermediate operators
`M^(theta/2) Khat_s^theta M^(theta/2)` and
`M^(theta/2) Khat_(s') M^(theta/2)` between the original operator
and `That(s',s')`. Their three comparisons are precisely steps (1)–(5).
After subtracting k times the vacuum contribution, none of the three
differences has a supplied sign.

The magnetic contribution is an *integral*, not the step length times
a magnetic expectation at one endpoint. At fixed temporal coupling s',

```math
\partial_u\widehat T(s',u)
=-\tfrac12\{W,\widehat T(s',u)\},\qquad
\partial_u\widehat E_i(s',u)
=\langle\psi_i(u),W\psi_i(u)\rangle.
```

This follows by differentiating the two multiplication factors and
applying the eigenvalue equation. Min–max for the isospectral operator
`Khat^(1/2) M_u Khat^(1/2)` gives locally Lipschitz ordered eigenvalues;
the finitely many positive eigenvalues in question stay away from zero
locally, so their negative logarithms are locally Lipschitz too. At a
multiple eigenvalue, the first-order equation is the compression of
the derivative to that eigenspace. Diagonalize this finite matrix.
The formula then holds almost everywhere for the ordered energies,
which suffices to integrate their derivatives. The kth magnetic
increment is

```math
\int_{\theta s}^{s'}\sum_{i=0}^{k-1}
\langle\psi_i(u),W\psi_i(u)\rangle\,du.
```

It can be described as the step length times a *path-averaged*
magnetic action. Its vacuum-subtracted part is the integral of
`sum_(i=1)^(k-1)(<W>_i-<W>_0)`. Row 708's approximate factor “about 3”
was a continuous-time interpretation of published rates, marked GUIDE.
It does not evaluate this discrete-time integral, or the other two
vacuum-subtracted contributions. No such numerical interpretation is
used in this check.

## 5. “Row 708's DEF_K in exact form” — FAILS

The shared difficulty is vacuum subtraction. The statements are not
identical. Row 708, `gap-mid-max.md:136–139,160–172`, explicitly makes
the level condition sufficient for thermal transport. Its `DEF_K` asks
for each ordered level separately:

```math
D_i'(s)\geq-K(s)D_i(s),\qquad i\geq1.
```

Its integrated form is `(LEV_K)`, assuming absolute continuity (or the
appropriate one-sided version at crossings). Section 6.4 instead asks
for each *prefix sum*. For `q(s,s')=exp(-integral_s^s' K)`, the valid
implications are

```math
(\mathrm{DEF}_K)\Longrightarrow(\mathrm{LEV}_K)
\Longrightarrow(\mathrm{KF\!\!-\!LEV})
\Longleftrightarrow(\mathrm{SUPER\!\!-\!D})
\Longrightarrow\hbox{thermal transport}.
```

Here `(SUPER-D)` uses `theta'=q`; the printed restriction `q<=theta`
must also be met. The algebraic equivalence itself holds without that
restriction. One may enlarge K to at least `K_el` to meet it, but the
resulting integral must still fit the seed's rate budget. Finite K by
itself is not that budget.

There is no reverse implication from prefix sums to individual levels.
Here is a hand counterexample to that claimed *algebraic equivalence*,
not a counterexample to a Wilson mass gap. On `0<=u<=1/2`, choose
`kappa>=0`, and set

```math
D_1(u)=e^{-\kappa u}(1+u),\qquad
D_2(u)=e^{-\kappa u}(3-u),\qquad
D_i(u)=i+2\quad(i\geq3).
```

They are positive and ordered. For every `u<v`, the first prefix obeys
`D_1(v)>=exp(-kappa(v-u))D_1(u)`. The second prefix is `4exp(-kappa u)`;
every further prefix adds a nonnegative constant. Hence `(KF-LEV)`
holds for every prefix and every pair, with `K=kappa`. But

```math
D_2'(u)+\kappa D_2(u)=-e^{-\kappa u}<0,
```

so `(DEF_K)` fails for level 2 at every point.
This example can also satisfy ABS: choose
`Ehat_0(u)=1+(4kappa+1)u` and `Ehat_i=Ehat_0+D_i`.
Every absolute level increases. The diagonal transfer operator with
eigenvalues `exp(-Ehat_i)` is positive, compact, and trace class at every
positive power. Thus all absolute Ky Fan comparisons hold for any
`theta<=1`. Choosing `kappa>=sup K_el` on a translated compact
positive-coupling interval also ensures `q<=theta` for the printed
Bessel factor. The example supplies no Wilson realization; none is
needed to disprove a claimed consequence of the displayed algebra.

The further identification with `(VIR-log)` as “equivalent” is also
unsupported. That condition tests a weighted thermal derivative, only
on the characteristic curve when Remark CH is used. Prefix-sum bounds
give a sufficient condition for it. Even at one differentiability point,
write `a_i=D_i'+K D_i`. The thermal inequality tests
`sum_i a_i exp(-t D_i)>=0`, whereas the Ky Fan condition tests every
`sum_(i<=m) a_i>=0`. At levels `(1,2,3)`, the choice `(a_1,a_2,a_3)=(1,-2,1)`
has thermal sum `exp(-t)(1-exp(-t))^2>=0` for every `t>0`, while its
second prefix is -1. Additional levels with `a_i=0` do not change this.
Thus even the local tests are distinct.

**Correct stopping statement.** ABS leaves an uncontrolled subtraction
of k vacuum defects. `(SUPER-D)` exactly formulates the remaining
Ky Fan condition; it is a sufficient weakening of row 708's individual
level condition. Neither this condition nor the weaker thermal-rate
condition is proved for the Wilson model. The stop at an uncontrolled
vacuum-subtracted response is valid. Calling it the exact same
`DEF_K`, or equivalent to `(VIR-log)`, is not.
The last variational observation in 6.5 is valid for trial subspaces:
a lower bound on the top-k eigenvalue product gives an upper bound on
`mathcal E_k`, whereas controlling `k Dfc_1-Dfc_k` needs a lower bound
on `Dfc_k` relative to the vacuum. The variational formula alone supplies
no such bound.

## Scope and verification record

The source is `gap-target-max.md:247–287` at the pinned checkout, with
the author's relevant correction at line 298. Original author: Claude
Fable 5.2 max, row 913. This report's evidence is the written algebra,
integration by parts, spectral comparison and explicit spectra above.
Different-provider authorship is provenance, not by itself independence.

No numerical job, finite enumeration, Lean run or guide script was run.
The author's large-b check, published-rate estimates, attack rankings,
transition facts, `(ONE-K)` and other claims outside Section 6 were not
independently verified. Nothing here changes the mass-gap or seed status.
Only this report is changed in the checkout; it is left uncommitted and
unpushed at the requested path. No remote write was made.

Source-boundary exception: platform instructions required a primary-source
web check for the technical literature claim, despite the task's local
reading boundary. One paper was read through the web tool for
Löwner–Heinz, as cited above. A shell attempt to save that PDF in the
new scratch directory failed with DNS error `Could not resolve host`;
no local PDF is claimed. All repository/file searches stayed within the
explicitly named repositories, supplied source folder and new scratch
directory. No wider transport-literature investigation was made.

RESULT: HOLDS for Lemma KF, both recalled classical inputs, and Identity 6.4; HOLDS AFTER CORRECTION for Lemma F's applications, Theorem ABS, and the finite magnetic-step interpretation; FAILS for the claimed exact equivalence with row 708's DEF_K or VIR-log. The vacuum-subtraction difficulty remains, and the Wilson thermal-rate bound and seed remain open.
