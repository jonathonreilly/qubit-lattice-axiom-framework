# Repo search

The target-specific prior note is absent at the assigned commit.
The lead's prior/repo-search-2026-11-08.md covers older construction
obligations. Its nearby hit is the soft route's
MASS_GAP_LOCAL_BLOCK_ASTRA.md, lines 106–154, on PR 10114 at
f76f6c649cff7dffbab664d8976e680e8f287fe9. I opened it: it supplies a
loop eigenvector and a positive one-step correlation, not ES-1.
The same digest reports the identical blob on PR 10133.
It reports searches of main and PRs 10114, 10133, 10134 and 10141;
that historical search is not a fresh absence theorem.

On main at a527a6fdaeb22ef8a0d1224cc2ba7bc42c48d3bc, I also opened
docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md,
Sections 0–3. Its positive Wilson kernels are an upstream input.
Its open temporal slab is not the present periodic, twisted-sector problem.

The closest results are the assigned local inputs: Claude Fable's
gap-means-max.md Section 4 and gap-crux-restate.md Section 3.4, and
Codex's gap-es1-astra.md. The latter already gives the SU(2) order-nine
versus order-twelve counterexample. Its surface coefficient comes from
Claude Fable's gap-seed-sc.md, Proposition 4.4; I read that proof and
its indicated counting and Haar-integral steps. None is claimed as new.
This task checks Opus's argument, rather than launching another ES-1 attack.
The registry, open-core and l17c searches found no duplicate check owner.

Codex; task assignment gpt-6-astra / max; FINISH row 753.
Source commit: 4ea2b71e1cdcb76d2af09373a21c0bf299579eaf.
Author checked: Claude Opus 5.5, row 751.
Research text, not an audit; this grants no status.
Unqualified source line numbers below refer to gap-es1-opus.md.

## Verdicts

| Statement and source lines | Verdict | Finding |
|---|---|---|
| Lemma 2.1, 52–56 | HOLDS | Exact factor 1/4 and negative sign in exp(−Delta) |
| Theorem V(a), 60,68 | HOLDS | The doubled trace gives the stated lower bound |
| Theorem V(b), 62–70 | HOLDS | The four retained sectors give the stated upper bound |
| Theorem V(c), 66,72 | HOLDS | Both inequalities hold for any four-element L |
| Corollary V1, 74–78 | HOLDS | Its displayed inequalities hold; the equivalence retains the sector-sum hypotheses |
| Theorem LB(i)–(iv), 92–113 | HOLDS | Including the finite-b factor and the limiting identity |
| Z₂ membership in the stated class, 121–127 | HOLDS | Finite-matrix verification below supplies the omitted argument |
| Lemma Z2-a, 129–141 | HOLDS AFTER CORRECTION | Its printed prefactor uses counting measure; declare that convention or insert the Haar factor |
| Lemma Z2-b, 143–151 | HOLDS | The minimum area and all equality cases have a hand count |
| Lemma Z2-b′, 153–155 | HOLDS | Exact nonzero spatial frustration has at least four plaquettes |
| Lemma Z2-c, 157–166 | HOLDS AFTER CORRECTION | The explicit bound and min–max step hold; state the following O(u^(4t)) consequence for fixed t |
| Theorem Z2(a)–(c), 168–192 | HOLDS | With the consistent normalization above; fixed-box constants, uniform for time at least three |
| Proposition FUSE-suff, 204–217 | HOLDS AFTER CORRECTION | Both displayed bounds hold. Use max(1,K) in its numerical sufficient condition |
| Z₂ application of (F-l), 220 | HOLDS AFTER CORRECTION | The cited upper bounds alone do not imply it; the lower-bound repair below does |

No requested theorem is refuted. The corrections do not change the
coefficient 216 or the exponent obstruction. Checked line by line by
Codex: the first normalization mismatch is line 133 under the inherited
Haar convention; the missing fusion inference is line 220.

## 1. The sign and both bounds of Theorem V

Write \(\lambda=\lambda_0(A)\), \(S=\epsilon_{cd}\), \(S'=S'_{cd}\).
For every nonzero sector define its spectral purity

\[
 b_z=\frac{Z_z(2a;A)}{Z_z(a;A)^2}.
\]

Nonnegative eigenvalues give
\((1+s_z)^{-2}\le b_z\le1\). Give a zero sector zero contribution.
Crossing then gives the exact identity

\[
 e^{-\Delta}(1+S')
 =\frac{(1+S)^2}{4}\sum_z p_z^2 b_z.                 \tag{1}
\]

This also checks Lemma 2.1 directly: its numerator is
\(Z_0(a;2a,c,d)=\lambda_0(2a,c,d)^a(1+S')\).
The exponent after division by \(\lambda^{2a}\) is \(-\Delta\).

For (a), \(\sum p_z^2b_z\le\sum p_z^2=4-Q\). Therefore

\[
 \Delta\ge\log(1+S')-2\log(1+S)-\log(1-Q/4).
\]

The logarithm is defined: \(4-Q=\sum p_z^2>0\), since \(p_0=1\).
In particular the sign of the \(S'\) term is positive.

For (b), put \(h=H_L\), \(\sigma=\sum_{z\in L}s_z\). Then

\[
 \begin{aligned}
 \sum_zp_z^2b_z
 &\ge\sum_{z\in L}p_z^2(1-2s_z)\\
 &\ge\sum_{z\in L}(2p_z-1-2s_z)
 =4-2h-2\sigma.
 \end{aligned}
\]

Here \(p_z^2\le1\), \(p_z^2\ge2p_z-1\), and \(s_z\ge0\).
With \(\eta=(h+\sigma)/2<1\), (1) gives exactly V(b).
No ground-state vector in a twisted sector was assumed even or simple.

For (c), write \(q_z=1-p_z\) on L. Both
\(\sum_Lq_z\) and \(\sum_{L^c}p_z\) equal h. The exact expression is

\[
 Q=2h-\sum_Lq_z^2-\sum_{L^c}p_z^2.
\]

Each square sum lies between zero and \(h^2\). This proves
\(2h(1-h)\le Q\le2h\), including the vacuous lower bound when \(h>1\).
Using \(-\log(1-y)\ge y\), \(\log(1+S)\le S\), and
\(-\log(1-y)\le2y\) for \(y\le1/2\) proves V1.

The wording after V1 needs its printed qualification. In particular,
\(h\le4(\Delta+2S)\) when \(h\le1/2\), whereas the converse bound reads
\(\Delta\le h+\sigma+S'\). Thus an even-only equivalence also needs
control of \(\sigma\) and \(S'\). Theorem V does not supply that control.
The more precise asymptotic description is
\(\Delta=h/2+O(h^2+\sigma+S+S')\) when these quantities are small;
it is not an exact equality with h/2.

## 2. Z₂ belongs to the required class

Fix \(0<u=e^{-2\beta}<1\). Let a spatial box have V sites and
\(E=3V\) links. Work first on counting-measure \(\ell^2(\{\pm1\}^E)\).
Let P average vertex gauge transformations, and put

\[
 K=\bigotimes_{\ell=1}^{E}
       \begin{pmatrix}1&u\\u&1\end{pmatrix},
 \qquad D_m(\sigma)=u^{f_m(\sigma)},\qquad
 T_m^*=D_m^{1/2}K D_m^{1/2}\big|_{\operatorname{Ran}P}.
                                                               \tag{2}
\]

The one-link eigenvalues are \(1+u\) and \(1-u\), both positive.
The diagonal \(D_m\) is positive. Gauge averaging commutes with K
and \(D_m\). Consequently (2) is self-adjoint and strictly positive.
It is finite dimensional, hence trace class.

The normalized-Haar transfer operator is \(T_m=2^{-E}T_m^*\).
Indeed, inserting \(P=2^{-V}\sum_gU_g\) between layers gives one
normalized sum over temporal links per layer. The factor \(2^{-E}\)
gives the spatial-link sums. Expanding the trace yields precisely the
normalized torus integral, including its closing temporal links.
This verifies the trace identity without deleting a gauge constraint.

The centre flip \(C_\nu\) multiplies a configuration by the flat
1-cocycle on a transverse link cut. It preserves every spatial
plaquette, commutes with K and P, and is a unitary involution.
Inserting \(C^e\) in the trace changes the closing temporal
plaquettes on precisely the electric stacks. Thus, for every e,m,

\[
 Z^{e+m}(t;B)=\operatorname{Tr}(T_m^tC^e),\qquad
 Z_{\chi,m}(t;B)=\operatorname{Tr}(T_m^tP_\chi)\ge0.
                                                               \tag{3}
\]

This includes intersecting electric and magnetic twists.
Relabelling axes preserves the finite partition sum and its twist class.
On the gauge-orbit basis the periodic transfer kernel has strictly
positive entries. Replacing a maximizing Rayleigh vector by its
absolute value increases the form unless its nonzero entries have
one phase. Applying the matrix then makes every entry strictly positive.
Two orthogonal maximizing vectors are consequently impossible.
Thus the largest eigenvalue is simple with a positive eigenvector.
Each commuting flip preserves that vector, so it is even.

The remaining input is domination of every twisted eigenvalue by
\(\lambda_0(B)\). This does not follow from \(D_m\le D_0\), which
is generally false. Instead, put \(v=(1-u)/(1+u)\). For each plaquette,

\[
 u^{(1-\eta_p\sigma_p)/2}
 =\frac{1+u}{2}(1+v\eta_p\sigma_p).
\]

After expansion, summing links kills terms with odd link incidence.
Every surviving coefficient is nonnegative before its twist sign.
Replacing each twist sign by +1 proves \(0<Z^k(T)\le Z^0(T)\).
For a fixed magnetic m, take the t-th roots of
\(\operatorname{Tr}T_m^t\le\operatorname{Tr}T_0^t\) and let \(t\to\infty\).
The largest twisted eigenvalue is at most \(\lambda_0(B)\);
every sector eigenvalue obeys the same bound.

These facts give (TM-tw), (TM-c), (F1) and (S3). Lemma A is the
nonnegative-eigenvalue inequality. Lemma K applies: normalized weights
give \(u^{6abcd}\le Z(a,b,c,d)\le1\), so its bulk infimum is finite.
R1 is the already checked finite Fourier/axis-exchange identity, and
R2(a) follows from it. No SU(2)-specific representation identity is needed.

**Normalization correction, lines 126,133,137.** If Z retains the
normalized-Haar convention of the inputs, its surface prefactor is

\[
 C_T=2^{-|E(T)|}N_{\rm fl},
\]

not \(N_{\rm fl}\); the sector prefactor is \(C_T/8\).
Alternatively, explicitly use unnormalized counting partition functions
throughout that subsection. Then the trace operator is \(2^VT_m^*\).
Passing between these conventions adds \(4|B|\log2\) to \(e(B)\).
That term cancels in every Delta and in delta. Sector ratios and
thermal sums also agree. Thus the correction changes no counterexample.

## 3. Surface counts and the min–max bound

**Z2-a.** In additive \(\mathbb F_2\) notation the map
\(\sigma\mapsto d\sigma+\widehat k\) has image exactly
\(\widehat k+\operatorname{im}d\). Every fibre has
\(|\ker d|=N_{\rm fl}\) elements. This proves the corrected surface sum.
Only the empty cocycle contributes at order zero to \(p_T\).
All other terms have degree at least one, and there are at most
\(2^{|P(T)|}\) terms. Thus \(1\le p_T\le1+2^{|P(T)|}u\).
The electric-character signs and factor 1/8 in line 137 follow from (3).

**Z2-b.** A nonzero \(\mu\nu\) period forces an odd number of
\(\mu\nu\)-plaquettes on each of its
\(N_{\mu\nu}=\prod_{\rho\ne\mu,\nu}n_\rho\) parallel coordinate tori.
Different orientations count disjoint plaquettes, so their bounds add.
At equality for one period there is one plaquette per plane and no
other orientation. The cube cocycle equation forces its two in-plane
coordinates to agree in neighbouring planes. They therefore agree
everywhere. The sheets are exactly the \(n_\mu n_\nu\) choices of
those coordinates. Moving a sheet one lattice step changes it by
the coboundary of the intervening link strip, so all have the stated class.

**Z2-b′.** Spatial frustration is dual to an even-degree edge set
on the three-torus. A nonempty such set contains a cycle.
The graph is simple for sides at least three. A cycle of length three
must wind straight around a side of length three: a lifted closed
walk in \(\mathbb Z^3\) has even length. This three-edge cycle has
nonzero period and cannot be dual to an exact 2-cochain.
Hence a nonzero exact frustration set has at least four plaquettes.
A single spatial-link flip has exactly four, so the minimum is attained.

**Z2-c.** The flat gauge orbits are the eight holonomy classes.
One can see this by transporting along paths in a fundamental box:
flatness removes contractible path changes, leaving three cycle signs.
The centre flips translate those signs freely. In a fixed character
sector, a function restricted to the flat configurations is therefore
a scalar multiple of \((-1)^{\chi\cdot h}\).
Let \(\Omega_\chi\) be the normalized vector with this flat restriction
and zero elsewhere.

Use the harmlessly rescaled operator \(T^*\) from (2).
Every row of \(K-I\) has absolute sum
\(g=(1+u)^E-1\); symmetry gives \(\|K-I\|\le g\).
Since D equals one on the flat set,

\[
 \mu_0\ge\langle\Omega_\chi,T^*\Omega_\chi\rangle\ge1-g.
\]

If \(\psi\perp\Omega_\chi\) in this sector, its entire flat restriction
vanishes. Z2-b′ gives

\[
 \langle\psi,T^*\psi\rangle
 \le(1+u)^E\|D^{1/2}\psi\|^2
 \le(1+u)^E u^4\|\psi\|^2.
\]

The complement of \(\Omega_\chi\) has codimension one.
Courant–Fischer therefore bounds \(\mu_1\), even though
\(\Omega_\chi\) need not be an eigenvector. Consequently

\[
 s_\chi(t)\le(d_\chi-1)
 \left(\frac{(1+u)^E}{1-g}\,u^4\right)^t
 \le d_\chi\{2(1+u)^E u^4\}^t.                    \tag{4}
\]

This is the printed estimate. Its \(O(u^{4t})\) consequence is for
fixed B,t, with a constant \(C_{B,t}\). A constant independent of t
does not follow by dropping the exponential prefactor; that stronger
claim would need another argument.
The consequence actually used in Theorem Z2 is uniform in \(t\ge3\):
choose u so that \(g<1/2\) and \(3u^4\le1\). Then

\[
 s_\chi(t)\le27d_\chi u^{12}\qquad(t\ge3).           \tag{5}
\]

There is no time-uniformity defect in Theorem Z2(a).

## 4. The coefficient 216 and the obstruction

Choose the four electric sectors L. The relevant counts are:

| Torus | Magnetic class giving order nine | Area | Sheets per class | Electric characters | Leading heavy weight |
|---|---|---:|---:|---:|---:|
| (3,3,3,3) | \(k_{23}\), \(k_{24}\) | 9 each | 9 each | 4 each | \(72u^9\) |
| (3,3,6,3) | \(k_{23}\) | 9 | 18 | 4 | \(72u^9\) |
| (3,3,6,6) | none | at least 18 | — | — | \(O(u^{18})\) |

For each order-nine class the e=0 character sign is +1.
A nonzero electric twist adds another period and costs at least
nine additional plaquettes. A nonminimal cocycle in the original
class has at least ten plaquettes. The finite surface polynomials
and \(p_T=1+O(u)\) thus give the claimed \(O(u^{10})\) remainders.
On (3,3,6,3), the other magnetic pair \(k_{24}\) costs 18;
the two-bit class costs at least as much. No sector is omitted.

Equation (5) bounds S, S′ and every light-sector sum by \(O(u^{12})\)
on each fixed box needed here. With \(h=H_L\), Theorem V gives

\[
 \frac h2-\frac{h^2}{2}-2S\le\Delta
 \le\frac h2+\frac{\sigma}{2}
       +\left(\frac{h+\sigma}{2}\right)^2+S'
\]

for sufficiently small u. Hence

\[
 \begin{aligned}
 \Delta(3,3)&=36u^9+O(u^{10}),\\
 \Delta(6,3)&=36u^9+O(u^{10}),\\
 0\le\Delta(6,6)&=O(u^{12}),\\
 \delta&=(4\cdot36+2\cdot36)u^9+O(u^{10})
        =216u^9+O(u^{10}).
 \end{aligned}                                                   \tag{6}
\]

This verifies the four plaquette-count and spectral steps without a run.
For small u, \(\delta\ge108u^9\) and \(\epsilon\le C u^{12}\).
The even space contains the constant and a nonconstant spatial plaquette;
strict positivity of (2) gives \(\epsilon>0\). Therefore
\(\delta/\epsilon^\gamma\to\infty\) for \(\gamma>3/4\).
Both epsilon and delta nevertheless tend to zero, so (ES) eventually holds.

The comparison also fails against any fixed finite collection of thermal
boxes and times at least three, independent of u. The constants depend
on those boxes. This is not a bound uniform over boxes that grow with
\(u^{-1}\), a large-a obstruction, or a continuum mass-gap conclusion.

## 5. Theorem LB

Keep c,d fixed, \(e_b=e(b,c,d)=\ell b+\kappa(b)\), and
\(L_b=\log(1+S_{\rm ev}(a;B_b))\).
Crossing retains the periodic term and gives
\(\lambda_0(A)^b/4\le Z_0(a;B_b)\), proving (i).
For \(b\ge a\), sectorwise spectral domination gives

\[
 Z_z(b;A)\le\lambda_0(A)^{b-a}Z_z(a;A).
\]

Summing and using \(\sum_z Z_z(a;A)=4Z_0(a;A)\) proves (ii).
Thus for \(b\ge a\),

\[
 L_b=b\kappa(a)-a\kappa(b)+r_b,\qquad
 -\log4\le r_b\le\log(1+\epsilon_{cd}).              \tag{7}
\]

Lemma K supplies \(0\le\kappa(b)\le\kappa(a)\).
For \(b>a\), (7) gives
\((b-a)\kappa(a)\le\log4+L_b\).
Also \(\Delta=a(2\kappa(a)-\kappa(2a))\le2a\kappa(a)\).
These are (iii), with the stated factor \(2a/(b-a)\).
Dividing (7) by b proves (iv), since \(\kappa(b)\) and \(r_b\) are bounded.
Finally the three weights 4,2,1 give its bound on delta.
Each cross-section has its own bulk infimum ell.
The identity determines a growth rate; it supplies no short-box estimate.

## 6. FUSE-suff: arithmetic and the missing application step

There are twelve heavy sectors and four light sectors. Thus (FUSE_K) gives

\[
 \eta\le6K\sqrt S+2KS,\qquad
 \Delta\le2\eta+S'
 \le12K\sqrt S+4KS+S'.                             \tag{8}
\]

Discarding \(-2\log(1+S)\) increases the upper bound.
The three nonnegative deficits telescope with total weight seven.
Both displayed inequalities in lines 211–213 therefore hold.

For the numerical corollary, state \(K_*=\max(1,K)\) and require
each indicated even sum to be at most
\(q=10^{-16}/(144K_*^2)\). The hypotheses hold with \(K_*\), and

\[
 6K_*\sqrt q+2K_*q
 \le5\cdot10^{-9}+10^{-16}/72<1/2,
\]
\[
 \delta\le7\left(10^{-8}+\frac{10^{-16}}{36K_*}
                         +\frac{10^{-16}}{144K_*^2}\right)
 \le7\cdot10^{-8}+\frac{35}{144}10^{-16}<10^{-7}.
\]

Also \(\epsilon\le q<10^{-7}\). The list has six uses of boxes;
spatial permutations identify two pairs, which causes no problem.
The source's arithmetic is correct for \(K\ge1\). That restriction
should be explicit for its abstract class. Indeed the smallness
hypothesis forces \(0\in L\); if S is positive, (F-l) already gives
\(S=s_0\le KS\), hence \(K\ge1\). Using \(K_*\) also covers degenerate
zero-sum cases without an unstated lower bound on K.

**Line 220: missing inference and hand repair.** Upper bounds
\(s_z=O(u^{12})\) and \(S=O(u^{12})\) do not imply \(s_z\le KS\).
This is the first failing inference in that application paragraph.
The needed lower bound can be supplied by the two-dimensional
min–max construction used in gap-es1-astra.md Lemma 7, in the Z₂ basis:

Let \(\Omega_0\) be the normalized indicator of the flat set.
Flip one fixed spatial link in every flat configuration, and let
\(\Omega_1\) be the normalized indicator of the resulting set.
The two sets are disjoint and invariant under gauge transformations
and centre flips. Their frustrations are respectively zero and four.
Thus their indicators are orthogonal even vectors, and D has values
1 and \(u^4\) on their supports. Since
\((1-u)^E I\le K\le(1+u)^E I\), every vector in their span satisfies

\[
 \langle\psi,T^*\psi\rangle\ge(1-u)^E u^4\|\psi\|^2.
\]

The second even eigenvalue is therefore at least \((1-u)^E u^4\).
The first is at most \((1+u)^E\), so

\[
 S_{\rm ev}(3;B)
 \ge\left(\frac{1-u}{1+u}\right)^{3E}u^{12}.         \tag{9}
\]

For each fixed box, (5) and (9) give \(S\asymp u^{12}\).
They prove (F-l) with a coupling-independent constant.
The heavy weights are \(O(u^9)\), while \(\sqrt S\ge c u^6\);
therefore (F-h) also holds for sufficiently small u.
A maximum over the three fixed shapes supplies one finite K.
This repairs the application, but does not establish the coefficient
81 asserted only as ARGUED in line 196. No Wilson SU(2) fusion estimate
is supplied by this Z₂ argument.

## 7. Comparison with row 748 and source limits

The two counterexamples have the same geometric mechanism.
Row 748 uses Wilson SU(2) at small beta: a winding spatial plane costs
\((\beta/4)^9\). The even projection removes the length-three winding
loop; the first allowed local kinetic degree is four, giving an
\(O(\beta^{12})\) thermal sum at time three.
Opus uses Z₂ at large beta: a nontrivial dual sheet costs \(u^9\),
whereas nonflat even excitations cost at least four per time slice.
The same side-three area versus four-link local cost explains the
common exponent ratio 9/12 and coefficient 216.

They are electric/magnetic counterparts, not an asserted exact duality
between SU(2) and Z₂. The proof routes also differ: row 748 uses a
positive Gram expansion and the existing Haar/cumulant plane coefficient;
Opus uses frustrated cocycles and the flat-space min–max complement.
The shared mechanism is not two independent discoveries of different
obstructions. Row 748 already states the stronger group-specific
counterexample; this file does not constitute a new check of its whole chain.

The Sussman–Alpoge outline and CA-I were fetched once at 31a47c543775.
Before source reading I used the SA-index README, matching chunk rows
and neighbours, and obligations. Relevant reads: chunk-01, 60–74;
chunk-02, 83–112; obligations, 17–28; then SA 588–599,
2195–2257 and 2313–2336. GL3 and GL8 supply transfer-kernel provenance;
the gap passage explicitly requires an additional spectral estimate.
The CA 4.12–4.19 index has no match for the thermal/flux/defect target.
No claim of whole-account absence is made, and no CA-I proof is imported.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the
authors of their text, for those source inputs.

The requested local input reads were gap-means-max.md Section 4,
gap-means-max-check.md Sections 1–3, gap-crux-restate.md Sections 1
and 3.4, and gap-es1-astra.md in full. No mathematical program,
enumeration, guide-run output, Balaban formula, or machine certificate
was used to discharge a step. The original source, registries and
status files were not edited.

Recovery: the report is on the isolated branch
codex/gap-es1-opus-check-4ea2b71e1, based on the assigned commit.
The nine principal source/rule files compared with that commit matched
the requested checkout. Hash bookkeeping is in
/tmp/ym4d-gap-es1-opus-check.OgG880/source-hashes.txt.
The remaining source action is to apply the qualifications and the
line-220 repair; that edit belongs to the source's owner.

RESULT: The requested core bounds and Z₂ counterexample hold, with the normalization and constant qualifications above; delta = 216 u^9 + O(u^10), the fixed-box even sums are O(u^12), and Z₂ satisfies the class inputs. FUSE-suff's displayed inequalities hold; its Z₂ (F-l) application needs the supplied lower-bound repair. Row 748 has the same area-versus-local-excitation mechanism. No physical-trajectory bound, mass gap, or scientific status is granted.
