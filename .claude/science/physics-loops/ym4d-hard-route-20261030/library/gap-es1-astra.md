# Repo search

The assigned base is `715e012b799d2311c2798eb40ccc2783a1a171f6`.
`prior/gap-es1-astra.md` is absent at that base.
The lead's `prior/repo-search-2026-11-08.md` concerns thirteen earlier
construction obligations. It supplies no ES-1 result. Its transfer-operator
hit, the soft route's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, concerns a positive
one-step plaquette correlation, not a vacuum-energy defect.

The directly relevant prior work is Claude Fable's `gap-means-max.md`
206–323 (4.6–4.10): Theorem R, its converse R5, the hypothetical sector table, and
the Ising guide. ES-1 is expressly open there. Its check is row 744.
`gap-crux-restate.md` 3.4 already proves the full-sector shorter-time
defect bound (Lemmas K and X). `gap-seed-limit.md` Section 6 separates
the vacuum defect from the excited-state count.
`gap-phys-seed.md` Part 3 proves conditional seed/Casimir equivalences.
These arguments are inputs and are not claimed as new here.
An additional close hit is `gap-seed-sc.md` 99–137 and 156–200, by Claude Fable,
checked by Claude Opus in row 704. Proposition 4.4 already counts the
first wrapping plane and proves its coefficient. Theorem 2 already
finds order nine, rather than twelve, for the full four-torus defect
at side three. I use its one-direction proposition directly. I do not
repeat its surface counting or Haar integration. ES-1 adds the comparison
with the centre-even trace and the ground-energy defect; those are not
that theorem's conclusion.
The registry, open-core and l17c searches have no ES-1 owner;
FINISH row 748 owns this task. Row 749 owns the broader literature search.

Fresh bounded checks of main and PRs 10114, 10133, 10134 and 10141
found the earlier Gram-kernel and loop-eigenvector inputs, with no
ES-1 supplier in the passages inspected. Section 6 records the refs,
exact hits, scope and incomplete search. This is not an absence theorem.

Author: Codex gpt-6-astra max, as assigned in row 748.
Research text, not an audit; no scientific status is granted.
PROVED below means a written argument from named premises, not an
independent check. ARGUED, GUIDE and OPEN retain their literal meanings.
No numerical computation is used to discharge a step.

## Checkpoint

Target: a uniform comparison of
`eps = S_ev(a; a^3)` with
`delta = a(8 e(a^3) - e((2a)^3))`.
The quantifiers matter: a constant independent of coupling is stronger
than a constant allowed to depend on the action or on the chosen size.

Current result: Sections 1–4 prove a Wilson counterexample to the
coupling-uniform linear bound at side three, and a two-sided power
`3/4` bound on that small-coupling family. The failed route is the
linear comparison over all admitted sizes and couplings. The remaining
obligation is a different, precisely restricted ES-1 statement at
larger sizes or on the physical trajectory; Section 5 names the inputs
that this example does not supply. Next action: a separate proof check
of Lemmas 1–2 and Proposition 4 before using this conclusion downstream.
No independent check of this note has been performed.

Sources fetched once at the requested Sussman–Alpoge revision
`31a47c543775`: `/tmp/sa_ym4.tex` and `/tmp/sa_ca_I.tex`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the transfer-kernel and character-expansion inputs.
The SA-index README, matching rows and neighbours of `chunk-02.md`
83–112, `chunk-01.md` 64–73, and the matching obligations were consulted.
The source ranges read were SA 2195–2257 and 2313–2336 (GL3, GL8,
proved there) and 588–599 (polynomial decay does not imply a gap).
The CA 4.12–4.19 index has no match for this thermal/defect target;
the complete-account index locates its transfer proposition in Part III,
not the fetched Part I. CA-I 2698–2713 and 3217–3224 explicitly leave
clustering and a mass gap unasserted. These bounded reads supply the
transfer provenance, not a claim that the whole account was rechecked.
No Balaban text or formula is imported.

Fifteen principal local source/rule files were blob-compared with
the pinned base and matched. The checkout shares
Git metadata with another worker; its HEAD advanced during this run.
The argument is preserved on the isolated branch
`codex/gap-es1-astra-715e012b`, based on the assigned commit, with
this output also copied to the requested checkout. Only this research
file is an intended repository change.

## 1. A fixed-box trace bound for Wilson SU(2)

**Definitions.** Write `v = |B|` for the number of spatial sites and
`E = 3v` for the number of positively oriented spatial links.
All three sides of the periodic box `B` are at least three.
The coupling is `beta>0`. Write `F_beta(t;B)=log Z_beta(t;B)`
and `e_beta(B)=log lambda_0(B)`.
Use the Wilson normalization of `gap-transfer.md`:

\[
 T=P M C_\beta M P,\qquad
 M=\exp\left[-\frac\beta2\sum_{p\subset B}
                 (1-\tfrac12\operatorname{tr}U_p)\right].
\]

`P` is gauge averaging; `P_0` averages the three centre flips.
They commute with `M` and the kinetic operator. The top eigenvalue
`lambda_0` is simple and centre even, and

\[
 e^{-12\beta v}\le\lambda_0\le1,\qquad
 e^{-3\beta v}\le M\le1.
\tag{1}
\]

These are the existing transfer statements, not new claims.
The positive Gram expansion (2.2) of `gap-transfer.md` is

\[
 C_\beta=e^{-\beta E}\sum_{n\ge0}
  \frac{(\beta/2)^n}{n!}
  \sum_{\alpha\in I^n}|p_\alpha\rangle\langle p_\alpha|,
 \quad I=\mathcal E\times\{1,2\}^2,
 \quad p_\alpha(U)=\prod_{r=1}^n(U_{\ell_r})_{i_rj_r}.
\tag{2}
\]

Its diagonal sum satisfies
`sum_alpha |p_alpha(U)|^2 = (2E)^n`.
Thus the expansion converges in trace norm: the sum of the traces
of its positive summands is `e^{-beta E} exp(beta E) = 1`.

**Lemma 1 (PROVED).** For `Q=P`, every `Q p_alpha` with `n<3`
is constant. For `Q=P P_0`, the same holds with `n<4`.

**Proof.** Form the spatial multigraph of the `n` link occurrences.
A gauge transformation equal to `-1` at one vertex multiplies the
monomial by `(-1)^degree` there. Gauge averaging therefore kills
every multigraph with an odd-degree vertex.

The spatial graph is simple when all sides are at least three.
With one occurrence an odd vertex is present. With two occurrences,
the only surviving possibility is the same link twice. Its gauge
average is constant: independent gauge transformations at its two ends
act transitively on that single link variable. Degree zero is constant.

With three occurrences, an even-degree multigraph must be a triangle
of three distinct links. To see this, two equal occurrences leave the
third edge with odd ends; three equal occurrences have odd ends too.
Three distinct edges with all degrees even form one triangle.
Lift its three nearest-neighbour steps to the integer lattice. Their
sum cannot be zero, since its coordinate-sum parity is odd. Their sum
is a period vector, so all three steps lie in one direction whose
period is three. Such a triangle winds once around that direction.
Exactly one of its links crosses the chosen centre-flip plane. The
monomial changes sign under that flip, and `P_0` kills it. Since the
flip commutes with gauge averaging, `P P_0` kills it too. QED.

**Lemma 2 (PROVED).** Let `r=3` for the full physical sector and
`r=4` for the centre-even sector. For every integer `t>=1`,

\[
 S_Q(t;B)\le
 \left[e^{12\beta v}\frac{(3v\beta)^r}{r!}\right]^t.
\tag{3}
\]

Here `T_Q` is the restriction of `T` to `Ran Q`, and
`S_Q(t;B)=Tr((T_Q/lambda_0)^t)-1`.
The constants here depend on the fixed box. No volume-uniform bound
is claimed.

**Proof.** Project (2) with `Q` and multiply on both sides by `M`.
Lemma 1 writes the resulting operator as

\[
 T_Q=A_\beta |M1\rangle\langle M1|+R_Q,
 \qquad A_\beta>0,\quad R_Q\ge0.
\]

The remainder contains only degrees `n>=r`. Projection is a
contraction, and `||M||<=1`, so

\[
 \operatorname{Tr}R_Q
 \le e^{-\beta E}\sum_{n\ge r}\frac{(\beta E)^n}{n!}
 \le\frac{(\beta E)^r}{r!}.
\tag{4}
\]

The second inequality uses `(r+k)! >= r! k!` term by term.
If `mu_0>=mu_1>=...` are the eigenvalues of `R_Q`, the rank-one
min-max inequality gives `lambda_j(T_Q)<=mu_(j-1)` for `j>=1`.
For completeness, intersect the orthogonal complement of `M1` with
the complement of the first `j-1` remainder eigenvectors. This has
codimension at most `j`; on it the quadratic form of `T_Q` is at
most `mu_(j-1)` times the norm squared. Min-max gives the assertion.
Consequently

\[
 \sum_{j\ge1}\lambda_j(T_Q)^t
 \le\sum_{i\ge0}\mu_i^t
 \le(\operatorname{Tr}R_Q)^t.
\]

The last inequality holds for nonnegative summands and integer `t`;
finite partial sums give it first, then monotone limits do.
The top eigenvalue of either restriction is the same `lambda_0`.
Divide by its `t`-th power, and use (1) and (4). QED.

**Corollary 3 (PROVED).** At `a=3`,

\[
 \epsilon_\beta=S_{\rm ev}(3;3^3)
 \le e^{972\beta}\frac{(81\beta)^{12}}{24^3}
 =O(\beta^{12}).
\tag{5}
\]

Also, for each of `B=3^3,6^3`,

\[
 e_\beta(B)=\tfrac14 F_\beta(4;B)+O(\beta^{12}).
\tag{6}
\]

Indeed `F(4;B)=4e(B)+log(1+S(4;B))`, and (3) with
`r=3,t=4` bounds the last term between zero and a fixed multiple
of `beta^12` as `beta` decreases to zero. This uses no exchange
of a Taylor expansion with an infinite-time limit.

## 2. The ground-energy defect at side three

**Prior input (PROVED in `gap-seed-sc.md`, Proposition 4.4).**
For fixed periodic transverse box `B`, let
`c_B=min(4,b_1,b_2,b_3)` and let `cyc(B)` count its cycles
of length `c_B`. Then, for `k>=3`,

\[
 F_\beta(k;B)-\tfrac12 F_\beta(2k;B)
 =\operatorname{cyc}(B)(\beta/4)^{c_Bk}
   +O(\beta^{c_Bk+1}).
\tag{7}
\]

All lower coefficients vanish by that file's Corollary 2.3.
For `c_B=3`, its explicit count is
`cyc(B)=number_of_sides_equal_to_3 times |B|/3`.
The cited proof gives the coefficient by a wrapping plane, its Haar
integral, and cancellation of all short cumulants. Those steps are
already done. The fixed-torus remainder is an analytic remainder,
not a numerically estimated error.

**Proposition 4 (PROVED from (6)–(7)).** For the Wilson SU(2)
action at side three,

\[
 \delta_\beta
 :=3\{8e_\beta(3,3,3)-e_\beta(6,6,6)\}
 =216(\beta/4)^9+O(\beta^{10}).
\tag{8}
\]

**Proof.** Keep the original time length equal to four. Define

\[
 \begin{aligned}
 D_1&=2F(4,3,3,3)-F(4,6,3,3),\\
 D_2&=2F(4,6,3,3)-F(4,6,6,3),\\
 D_3&=2F(4,6,6,3)-F(4,6,6,6).
 \end{aligned}
\]

Equation (6) and exact telescoping give

\[
 \delta_\beta=\tfrac34(4D_1+2D_2+D_3)+O(\beta^{12}).
\tag{9}
\]

Exchange the side being doubled with time. In (7), the transverse
boxes for `D_1,D_2,D_3` are respectively
`(4,3,3)`, `(4,6,3)`, `(4,6,6)`, with `k=3`.
For the first two boxes the shortest cycles have length three:

\[
 \operatorname{cyc}(4,3,3)=2(36)/3=24,
 \qquad
 \operatorname{cyc}(4,6,3)=72/3=24.
\]

For the third box `c_B=4`, so its first term has order twelve.
Because each `D_i` is twice the left side of (7),

\[
 D_1=48(\beta/4)^9+O(\beta^{10}),\qquad
 D_2=48(\beta/4)^9+O(\beta^{10}),\qquad
 D_3=O(\beta^{12}).
\]

Substitute in (9). The coefficient is
`(3/4)(4 times 48 + 2 times 48)=216`. QED.

## 3. The precise negative result

**Theorem 5 (PROVED).** There is no finite constant `C`, independent
of `beta`, for which

\[
 \delta_\beta\le C S_{{\rm ev},\beta}(3;3^3)
\tag{10}
\]

holds for all sufficiently small positive Wilson couplings.
This remains false when the right side is restricted to arbitrarily
small even thermal sums.

More precisely, for every `C>0` and `eta>0`, there is `beta>0`
such that `epsilon_beta<eta` and `delta_beta>C epsilon_beta`.
For every exponent `alpha>3/4`, the same assertion holds with
`C epsilon_beta^alpha` in place of `C epsilon_beta`.

**Proof.** By (8), there is `beta_0>0` such that
`delta_beta >= c beta^9` on `(0,beta_0)`, where
`c=108/4^9>0`. This follows from the definition of the
`O(beta^10)` remainder: reduce `beta_0` until its modulus is
at most `108(beta/4)^9`.
By (5), after also requiring `beta<=1`,

\[
 0\le\epsilon_\beta\le K\beta^{12},
 \qquad K=e^{972}81^{12}/24^3<\infty.
\]

Choose `beta` positive and small enough that
`K beta^12<eta` and `C K^alpha beta^(12alpha-9)<c`.
Such a choice exists because `12alpha-9>0`.
Then `C epsilon_beta^alpha<delta_beta`. Take `alpha=1`
for (10). No value of `beta` has to be found by a computation. QED.

**Corollary 6 (PROVED).** Fix any finite collection of boxes `B_j`
whose sides are at least three, integers `t_j>=3`, and constants
`C_j>=0`, all independent of `beta`. No bound

\[
 \delta_\beta\le
 \sum_j C_j S_{{\rm ev},\beta}(t_j;B_j)
\tag{11}
\]

holds for all sufficiently small positive `beta`.
Each term on the right is `O(beta^(4t_j))=O(beta^12)`
by (3); the left side has the positive order-nine coefficient (8).
Thus a longer time, or a fixed larger box on the thermal side alone,
does not repair this coupling-uniform linear comparison for
the original defect at `a=3`.

**Scope (PROVED distinctions).** These counterexamples use Wilson's
own action. In particular they do not arise from a nonlocal scalar
normalization of partition functions, an abstract table of spectra,
or the use of another gauge group. The base size remains three while
`beta` tends to zero. Both `epsilon_beta` and `delta_beta` tend to
zero. The result therefore does **not** refute an unspecified modulus
`delta<=f(epsilon)` with `f(epsilon)->0`, nor prove that an even
seed can fail while the even sum tends to zero.

**OPEN.** A bound with a constant allowed to depend on the coupling;
a bound after excluding small lattice sizes or moving the *defect*
to a larger size; a sufficiently weak nonlinear modulus; and a
cutoff-uniform bound restricted to the proposed physical scaling
trajectory. No mass-gap conclusion follows from the counterexample.

## 4. A weaker bound, with the sharp power for this example

**Lemma 7 (PROVED from the existing one-link diagonalization).**
For each box of Section 1, every integer `t>=1`, and `0<beta<=4`,

\[
 S_{{\rm ev},\beta}(t;B)
 \ge e^{-9\beta vt}(\beta/4)^{4t}.
\tag{12}
\]

**Proof.** Let `W=tr U_p` for one spatial elementary plaquette.
Then `1` and `W` are orthonormal in Haar `L^2` and are gauge
invariant and centre even. The plaquette uses four distinct links;
its holonomy is Haar distributed. The mean of its trace is zero
and the mean square is one, by `gap-seed-sc.md` Lemma 4.1.

Use the existing one-link eigenvalues `c_0,c_(1/2)`:
`gap-transfer.md` 2.5–2.6 and `gap-vir-sc.md` Lemma C.
The constant and this loop are eigenvectors of the kinetic operator,
with eigenvalues

\[
 c_0^E,\qquad c_0^{E-4}c_{1/2}^4.
\]

The positive character series in `gap-transfer.md` 2.5 gives
`c_0>=exp(-beta)` and
`c_(1/2)>=exp(-beta) beta/4`: keep respectively its degree-zero
and degree-one terms. For `beta<=4`, both displayed kinetic
eigenvalues are at least `d=exp(-beta E)(beta/4)^4`.

The two-dimensional space
`M^(-1) span{1,W}` lies in the physical even sector. For every
vector `psi` in that space,

\[
 \langle\psi,T\psi\rangle
 =\langle M\psi,C_\beta M\psi\rangle
 \ge d\|M\psi\|^2
 \ge e^{-9\beta v}(\beta/4)^4\|\psi\|^2.
\]

Min-max bounds the second even eigenvalue below by that number.
Since `lambda_0<=1`, its ratio to `lambda_0` has the same lower
bound. Its `t`-th power is one term in the even thermal sum. QED.

The loop eigenvector used here is already in the soft route's
`MASS_GAP_LOCAL_BLOCK_ASTRA.md` (5)–(7), by Codex. Its application
there is a lower bound on a centred one-step correlation. Here the
two-dimensional min-max space gives a lower spectral bound instead.

**Corollary 8 (PROVED).** There are `beta_*>0` and explicit positive
constants `c_*,C_*` such that, for `0<beta<beta_*` at `a=3`,

\[
 c_*\epsilon_\beta^{3/4}
 \le\delta_\beta\le C_*\epsilon_\beta^{3/4}.
\tag{13}
\]

One choice is

\[
 B_*=\frac{2\,324^{12}}{24^3},\qquad
 c_*=108B_*^{-3/4},\qquad C_*=324\,2^{3/4}.
\]

**Proof.** Choose `beta_*` below `min(4,log(2)/972)` and small
enough that the remainder in (8) has modulus at most
`108(beta/4)^9`. This is a stated existence choice from (8).
Writing `u=beta/4`, equations (5), (8) and (12) give

\[
 \tfrac12 u^{12}\le\epsilon_\beta\le B_*u^{12},
 \qquad108u^9\le\delta_\beta\le324u^9.
\]

Taking the power `3/4` gives (13). Theorem 5 rules out every
larger power, with a coupling-independent constant, on this family.
These constants are deliberately crude; their finiteness is what is
used. The size `a=3` and small-coupling interval are essential to
this proved weaker form. QED.

## 5. What extra input must change

**PROVED, given the cited seed-to-limit results.** Locality,
reflection positivity, nonnegative character coefficients, and
exponential clustering do not by themselves restore (10).
Wilson's action has the first three properties. For all sufficiently
small couplings used above, `gap-seed-sc.md` Theorem 3 supplies a
full periodic seed. `gap-crux-restate.md` Theorem S and
`gap-seed-limit.md` Theorem L then give the stated exponential
clustering of periodic limit states. Thus this counterexample can
be taken inside that already proved strong-coupling regime.

**ARGUED mechanism.** The low-order contribution to the defect is
a spatial wrapping plane. Upon exchanging axes it is an electric-flux
contribution. Centre-even projection removes the degree-three
winding-loop state but does not remove the spatial plane's
contribution to the periodic vacuum energy. Locality permits this
configuration; positivity makes its leading coefficient positive.
Qualitative clustering does not compare its suppression exponent
with that of the even excitation.

**PROVED necessary changes for this family.** A bound
`delta_beta<=C(beta) epsilon_beta` must allow
`C(beta)>=c beta^(-3)` for some fixed `c>0` as `beta` tends to zero.
This follows from (5) and (8). Alternatively, a coupling-uniform
power bound must have power at most `3/4` by Theorem 5.

**OPEN possible repairs.** Exclude size three and prove a new bound
on the remaining sizes; move the vacuum defect as well as the thermal
box; or supply a quantitative estimate controlling noncontractible
spatial contributions by the chosen even trace. In particular, merely
assuming that two odd fluxes can fuse into an even state is not the
linear estimate. The contribution counted in (7) has one winding
sheet's cost. A proof must compare that cost, with its multiplicity,
to the actual even thermal quantity on its stated shape.

The long-box growth-rate formula in `gap-means-max.md` 4.9 remains
an existing route. This note neither re-proves it nor supplies its
missing estimate from one bounded box to arbitrarily long boxes.
The Casimir input in Theorems ZD and ZD-c of `gap-phys-seed.md`
therefore remains separate at the physical target.

## 6. Bounded repository-search record

I fetched main and the four named PR heads. The fresh bounded search
used `ES-1`, `even thermal`, `vacuum.energy defect`, `Casimir`,
`winding plane/sheet`, and finite-size ground-state variants.
On the PRs it screened mass-gap, seed, transfer and thermal filenames,
then searched the distinct candidate blobs. The local-block note above
was read at 1–38 and 106–154; its matching blob is identical on
PRs 10114 and 10133. A `thermalization` hit in the crossover note is
simulation vocabulary, not a thermal-trace theorem.

| Ref checked | Revision | Relevant disposition |
|---|---|---|
| `origin/main` | `a527a6fdaeb2` | The Wilson temporal-gauge bridge note, Sections 0–3, already proves positive character coefficients and Gram kernels. Reused through the lane's transfer proof; no defect comparison in the passage read. |
| PR 10114 | `f76f6c649cff` | Local-block loop eigenvector and positive correlation witness, as above. Related input, different conclusion. |
| PR 10133 | `89faef229ff6` | Same local-block blob; three additional mass-gap candidate blobs yielded no ES-1 hit in this search. |
| PR 10134 | `1e70c7211a2c` | No filename candidate in the searched YM4D paths. |
| PR 10141 | `fb99b4dddc72` | No filename candidate in the searched snapshot paths. |

The main note is
`docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`.
The soft-route paths above are relative to
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.
These are bounded checks, not an exhaustive absence claim. An initial
broad main/PR content scan was stopped because it pulled unrelated
material. Its partial output is not evidence of absence. The narrower
search completed; its ref inventory and targeted logs are in
`/tmp/ym4d-gap-es1-astra-715e012b/`.

RESULT: PROVED here, not independently checked: Wilson SU(2) at a=3 has epsilon=O(beta^12) and delta=216(beta/4)^9+O(beta^10), so coupling-uniform linear ES-1 fails, even with a fixed larger thermal box or longer time; on this small-coupling family delta is comparable to epsilon^(3/4). Larger-size and physical-trajectory versions remain OPEN; no mass-gap result or status is granted.
