## Repo search

The lead searched main and the open YM4D branches before assigning this leaf.
I used [the search record](prior/repo-search-2026-11-08.md), especially its
R2 section, lines 423–444. It found representation precautions, not a joined
independent-current response certificate.

I read [loc-3](loc-3.md) and [loc-4](loc-4.md) in full.
Claude's Theorem W, corrected by Codex in loc-4 §7, already gives the
locality implication that consumes D1. It retains D2, D3, SUP and D4.
I also read [r2-heal](r2-heal.md) and
[its check](../gates/r2-heal-check.md) in full. The check identifies this
existing reduction. I do not repeat the replay or bracket proofs.

I fetched PR #10114 and read `SOFTHARD.md:534–547` at
`f76f6c649cff7dffbab664d8976e680e8f287fe9`.
That soft-route contribution requires both adjoining hard constraints,
including crossing rows, and retains singular parts of the disintegration.
It is a representation contract. It proves no D1 operator bound.
Here it rules out deleting a seam row to simplify the joined problem.

The target is the DR-owned `D1-FIXEDPOINT` row, specialized by
[hstep-tree §5](hstep-tree.md), FINISH 542. `DR-locP` already supplies
fixed-region component locality, conditionally on its actual solver inputs.
Its Outstanding paragraph, drlocp:198, excludes changing-region existence.
`PRINT-JOIN` instead concerns the stage interaction spaces and bounds.
This note does not attack that row or D4-CARRIED.
There is no `prior/leaf-d1.md` at the requested pin.

# D1-JOIN: the first joined response entry

Codex, 2026-11-08. Repository baseline
`5e09ceb63dee6bb25006f5c51006f8552f6a481f`.
Research text, not an audit. Grants no status.
This session writes only this file.
The library and gate inputs were checked against that baseline after
the checkout's HEAD moved concurrently. They match it.
All mathematical tests below are hand arguments.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every source construction used below.
Credit Tadeusz Bałaban for the multiscale, constrained-inverse and local
parametrix methods. Credit the repository authors cited at each use.

Source line numbers use these fixed versions:

- **SA:** `YM4_sketch_500.tex`, `31a47c543775`.
- **Y:** `YM4_1400.tex`, `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **I:** `theorem_0_complete_account_raw_I.tex`, `31a47c543775`.

Existing copies at the three requested `/tmp` paths were reused.
The outline index, its neighbouring rows and obligations were read before
the corresponding source passages.

## 1. Kill test, before the operator argument

Take left and right blocks separated by one zero-switch layer.
Put the imposed datum \(B'\) only on the left.
Keep the independent background current on both sides.
The test concerns the increment \(j\), not the background current itself.

Use the adopted equations, [red](red.md) §2 and
[nl-r9](nl-r9.md) (4.1)–(4.4). Keep their complete hulls and two-read
collars. In particular,

\[
 a=H_{1,s}B'-\mathfrak G_sW_s^{\rm red}(a),\qquad
 h=a-H_s\mathcal C(h),\qquad
 M_s=M_s^{\rm walk}-a_0I.                                      \tag{1}
\]

The diagonal in (1) has no switch factor. The local row \(K=mQ\)
also remains the actual row. It is not set to zero on the wall.

Every nonzero crossing walk coefficient has a zero factor from its
complete hull. Thus it vanishes. The remaining possible local runs have
reach at most \(2r_g\). The endpoint margin in drlocp (4), (16) contains
them. In particular, the diagonal in \(M_s\) cannot bypass a split factor.
These are precisely the hypotheses of the existing drlocp Lemmas 2.1–2.2.
Their proof is used here, not replaced by a claim that all factors split.

On the unforced component, \(a=h=0\) solves (1):
\(\mathcal C(0)=W_s^{\rm red}(0)=0\).
The existing small-ball uniqueness implication then selects that solution.
No condition \(\mathbf J=0\) was used.

Check the current separately. The active red/d3-local prescription uses
the force anchor. For clarity, drlocp (7) writes both recorded anchors as

\[
\begin{split}
 F_*(h)&=F'_U(h)-F'_U(0)+J_*,\\
 \lambda(h)&=(I+H_s^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
                         H_s^{\mathsf T}F_*(h),\\
 \lambda_0&=H_s^{\mathsf T}J_*,\\
 j(h)&=R_hK_h^{\mathsf T}\lambda(h)-K_0^{\mathsf T}\lambda_0.
\end{split}                                                     \tag{2}
\]

Here red uses \(J_*=F'_U(0)\); ST1 uses \(J_*=\mathbf J\).
They are not identified with each other.
At \(h=0\), \(\mathcal C'_0=0\), \(R_0=I\) and \(K_h=K_0\).
Consequently \(\lambda(0)=\lambda_0\) and \(j(0)=0\).
The paired series has the same contained reads, by drlocp Lemma 2.2.
Hence the left source cannot change this calculation on the right.

**Outcome:** the prescribed zero-wall algebra passes, for either recorded
anchor separately. Both \(h\) and \(j\) vanish on the unforced component.
This is conditional on native complete-hull coefficients and the small
solver ball. Those are what D1-JOIN must still certify.
There is no counterexample to the actual joined response in this test.
Switching the diagonal, dropping a crossing row, or restricting an
ambient inverse would change the test's equations.

This specializes the repository's existing component argument.
Its source is Sussman–Alpoge's R9 requirement, SA 5762–5803, and the
current construction at SA 10404–10410. The source calls existence and
splitting substantive inputs. The test does not promote them to theorems.

## 2. What the sources already supply

The following results are reused. Their proofs are not new work here.
The word “proved” in this table describes the source argument and its
stated hypotheses. It grants no repository status.

| Result | Source and scope |
|---|---|
| Joined geometry and row assignment | Claude's a3-close:104–137, Lemma J. The truncated tower meet is separated. New collar rows retain their own levels and lifted data. |
| Native canonical operator families | Sussman–Alpoge, Y 33528–33622, 40675–40749, 40831–40930. Proved on their regular-pair domain, including complete gauge cubes, outward completions and local compression collars. |
| Parameterized row and column bounds | Y 40955–41029. Proved for the specified carrier families and auxiliary partition. Y 41015–41024 expressly withholds identification with a separately prescribed history partition. |
| Small response, including current | Y 41183–41348. Proved on the stated datum ball \(r=c_Yb_Y^{-8}\). The displayed current has independent-current anchor. |
| Zero-wall restriction | Y 41350–41388. Proved for the retained ambient coefficients. A different regional sequence still needs equality of its determining data and operators. |
| Repository contraction | Codex's dec-field:247–278. Proved from the actual maps' [PW] and [NL], on \(b<cB^{-4}\). |
| Repository nonlinear bounds | Codex's nl-r9:179–267,330–359; checked by Claude in pw-bridge-gate §§C–D. They retain the named linear, row and geometric inputs. |

The older CA account does not settle the application by its locality theorem.
I 58187–58230 assumes free-current bounds and the joined-domain expansion.
I 59813–59838 assumes the localized large-field representation.
I 49495–49546 places the application's gauge-family supply outside the
operator theorem. The CA index classifies these supply conditions separately.

There is a useful correction to a possible port objection.
The canonical current correction in Y is not ruled out by a sign mismatch.
Y 30604–30648 explicitly converts its gauge generator to the forward
difference used in SA 10163–10192. It also converts the raw second jet.
Those formulas agree on a common graph with the same rows and site map.
This is Sussman–Alpoge's calculation; it must not be redone as an obstruction.
It does not identify two different graphs or two decorated families.

## 3. The exact native entry that remains to certify

Choose the first joined localization move with two collared parts.
Use its actual truncated towers. In the notation of a3-close:112,

\[
 \Omega_q^J=\Omega_q\cap T^1_{\min(q,j_1)}
                         \cap T^2_{\min(q,j_2)}.                 \tag{3}
\]

This uses that note's separated-collar hypotheses.
It is not a union of two independently solved backgrounds.
The one-layer wall in §1 is a switch wall inside this joined problem.
It is not a replacement for a geometric separation hypothesis in (3).

Form the action, site map, straightened rows and boundary conventions
on this sequence. Use its row lengths \(m_J(c)\).
The required normalization dictionary is

\[
\begin{split}
 K^J&=m_JQ^J,\\
 H^J&=\mathsf H^Jm_J^{-1},\qquad
 H_1^J=\mathsf H_1^Jm_J^{-1},\\
 W_0^J&=Q^J\mathsf G^J(Q^J)^{\mathsf T_{\rm phys}},\\
 M^J&=m_J^3\bigl((W_0^J)^{-1}-a^J\bigr)m_J^{-1}.
\end{split}                                                     \tag{4}
\]

Here \(a^J(c)=a_0m_J(c)^{-2}\).
Thus \(M^J\) contains exactly the diagonal \(-a_0I\).
The counting-row transpose satisfies

\[
 (H^J)^{\mathsf T}f
       =m_J^3(\mathsf H^J)^{\mathsf T_{\rm phys}}f.               \tag{5}
\]

Equations (4)–(5) are the existing nl-r9 conversion, applied in native units.
Using the ambient lengths on new collar rows would change these equations.
The local \(K^J\) is unchanged by the switches; notation \(K_s^J\)
must not introduce a new decoration.

For \(H_s^J,H_{1,s}^J,M_s^J\), use the prescribed native walk families.
For \(\mathfrak G_s^J\), use pw-bridge (7.4): compose the undecorated
coefficients first, and tag their full union once.
The products in the nonlinear map and in (2) retain repeated powers.
The paired current uses \(H_s^{J,\mathsf T}\), its derivative-column
pairing with the Wilson force, \(K_h^{J,\mathsf T}\), and
\((I+H_s^{J,\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}\).

Retain D2 explicitly. Every coefficient's complete hull must carry its
actual reference gauges, rows, outward endpoint reads and local charts.
The geometric partition denominator and every consecutive nonlinear
stencil also belong to that hull. A short path alone is not this input.

**Named unresolved lemma J-ENTRY.**
For this two-part move, on its original admitted independent-current
domain, the native assignments just described obey the actual [PW]
majorants and the paired-current majorants, uniformly on
\(\lvert s_\Delta\rvert<e^{\bar\kappa}\). One constant
\(B=C_{\rm op}e^{16\bar\kappa}\) is independent of depth, volume and
the parts' sizes. The prescribed entering datum set lies in
\(\lVert B'\rVert_Y<cB^{-4}\), with

\[
 c\le\min\{r_0/4,(16C_W)^{-1},(16C_C)^{-1}\}.                   \tag{6}
\]

Retain also drlocp:56's paired-current Neumann condition
\(B C_{\rm der}(2R_*)\le1/2\), \(R_*=2Bb_*\), on the common
solution ball. It is part of the entry, not a consequence of locality.

The [PW] norms here are precisely

\[
\begin{split}
 \|a\|_{X,w}
 &=\sup_y w(y)\max\{\xi_y|a|_y,\xi_y^2|\nabla_{\mathbf U}a|_y\},\\
 \|f\|_{F,w}&=\sup_y w(y)\xi_y^3|f|_y,\qquad
 \|b\|_{Y,w}=\sup_c w(c)|b(c)|,\\
 &\|H_s^J\|_{Y_w\to X_w},\
   \|H_{1,s}^J\|_{Y_w\to X_w},\
   \|\mathfrak G_s^J\|_{F_w\to X_w}\le B .
\end{split}                                                     \tag{7}
\]

The remaining row bounds are
\(\|K^J\|_{X_w\to Y_w},\|(K^J)^{\mathsf T}\|_{Y_w\to F_w}\),
\(\|H_s^{J,\mathsf T}\|_{F_w\to Y_w}\), and
\(\|M_s^J\|_{Y_w\to Y_w}\), with the absolute coefficient versions
needed by (2). The field columns also need their paired first-difference
sums. The weights have the admitted fixed small layer-metric rate.

J-ENTRY names the unresolved certificate in D1-JOIN.
It is not a new registry row or a claim of impossibility.
The three attempts below address this same certificate.

## 4. Route 1: port the complete native response

This is the shortest candidate. Apply Y's native operator theorem to (3),
then its parameter theorem and response theorem.
The geometry part is already supplied by a3-close Lemma J.
The normalizations (4)–(5) match Y 40715–40733 and 30630–30648.
There is no extra volume factor in that conversion.

Two identifications are still required before this is an application.

First, the source theorem decorates its constructed coefficients.
The active repository map uses the separately prescribed h-walk and
pw-bridge coefficients. Equality of their complete sums at \(s=1\)
does not identify these parameterized maps.
Y 41350–41388 makes exactly this distinction.

Here is the elementary test of that inference. Add two cancelling
coefficients \(T,-T\) to an undecorated family. Give them complete cube
sets \(\{1\}\) and \(\{1,2\}\), respectively.
Their undecorated sum is zero. Their decorated sum is

\[
                 s_1T-s_1s_2T=s_1(1-s_2)T.                    \tag{8}
\]

It need not vanish at \((s_1,s_2)=(1,0)\).
Thus a bound for one decorated family cannot be transferred by
identifying only the undecorated operator.
Equation (8) is a counterexample to that inference, not to the actual families.
It does not dispute Y's own coefficient bounds.

Second, the prescribed current must be retained.
Y 41205–41225 and its proof at 41310–41348 use
\(J_*=\mathbf J\) in (2), after writing the force difference as an
energy pairing. Red and d3-local use \(J_*=F'_U(0)\).
The already recorded difference, drlocp (8), is

\[
 j_F(h)-j_J(h)=
 \left[
 R_hK_h^{\mathsf T}
 (I+H_s^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}
       -K_0^{\mathsf T}
 \right]H_s^{\mathsf T}\bigl(F'_U(0)-\mathbf J\bigr).             \tag{9}
\]

At zero datum the bracket vanishes. This explains the passed kill test.
At a general independent-current pair the last factor is not zero by definition.
No source identity read here annihilates (9) at nonzero datum.
Physical-current agreement therefore does not justify this substitution.
This is the existing repository distinction, not a new counterexample.

The force-anchored current could instead be estimated directly.
That would require its native paired column majorants.
Y's pairing argument gives the method; it does not identify those
majorants with a different decorated family.

**Failure of route 1:** the port proves the theorem for its own
admitted family and current. The same-map application required by J-ENTRY
has not been proved. I do not replace the active specification by it.

## 5. Route 2: transfer the two existing problems through the seam

Try to use the already bounded operators of the two parts.
At the linear level, write a joined matrix in block form as

\[
 \mathbb A=
 \begin{pmatrix}A_L&E\\F&A_R\end{pmatrix}.
\]

Solving the second equation and substituting into the first gives

\[
 (\mathbb A^{-1})_{LL}
       =(A_L-EA_R^{-1}F)^{-1}.                                 \tag{10}
\]

It is not \(A_L^{-1}\). This calculation applies before any
nonlinearity or current continuation is considered.
The following hand example makes the loss explicit:

\[
 \mathbb A_t=\begin{pmatrix}1&t\\t&1\end{pmatrix},\qquad
 \mathbb A_t^{-1}
   ={1\over1-t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix},
              \qquad 0<t<1.                                   \tag{11}
\]

Both single-part inverses equal one. At \(t=1/2\), the left
compression of the joined inverse is \(4/3\), not one.
Its norm grows without bound as \(t\uparrow1\).
Even positivity of each finite joined matrix does not give a uniform bound.

A restriction of an ambient inverse has the same problem.
If \(A_L\) is the native restricted matrix, compression of the inverse
instead sees the Schur complement in (10).
The missing term represents paths leaving the part and returning.
It is not removed by restricting the output coordinates.

These examples do not embed a bad matrix into Yang–Mills.
They show exactly what the proposed transfer would have to estimate:
the native seam Schur complement, with its actual rows and pairings.
The real joined geometry theorem supplies neither that estimate nor
an identity deleting \(EA_R^{-1}F\).
The SOFTHARD representation contract also forbids deleting crossing constraints.

At a true separating zero switch, the prescribed tagged crossing
coefficients vanish, as in §1. That fact concerns the decorated
equations. It cannot replace the native inverse construction at \(s=1\).

**Failure of route 2:** existing bounds for the two parts do not prove
J-ENTRY by inverse restriction or block elimination.
No uniform native seam Schur estimate was obtained by this route.

## 6. Route 3: rebuild the native walk through local inverses

Now use Bałaban's local parametrix method on (3) itself.
This avoids both substitutions above.
For the prescribed native unfolded matrix \(\mathbb K_J\), the candidate is

\[
 \mathbb B_J=\sum_\kappa
       \widetilde h_\kappa\mathbb K_{J,\kappa}^{-1}\theta_\kappa,
 \qquad
 \mathbb R_J=I-\mathbb K_J\mathbb B_J,\qquad
 \mathbb K_J^{-1}=\mathbb B_J\sum_{n\ge0}\mathbb R_J^n.           \tag{12}
\]

The last identity needs a convergent majorant. It is not a definition
that proves invertibility.

There is substantial existing work to retain.
H-walk Lemma L and its repaired Theorem W give (12) under the
native conjugation package (I1). Pw-bridge §§5–7 then upgrades its
energy output to the first-order norms in (7).
Nl-r9 §4 supplies the transpose and normalized Gram-inverse bounds.
The Claude check of pw-bridge confirms these implications.
I do not redo their bootstrap, tree summation or contraction.

In particular, their local inverse estimate is

\[
 \|\mathbb K_{J,\kappa}^{-1}F\|_{\mathcal X,y}
       \le C_Ee^{-\tau d_J(y,z)}\|F\|_{\mathcal X^*},
 \quad \operatorname{supp}F\text{ near }z.                      \tag{13}
\]

This is for the native compression with its mixed rows.
H-walk:178–190,223–225 supplies it on **every** separated sequence
in its admitted class. It allows every coefficient \(j\) with
\(\sup_c m_J(c)^3|j(c)|\le\gamma_j(L)\), not just a physical current.
Thus (13) is not a new missing seam theorem.
The graph norm and the absolute second-jet coefficient bound are the
existing a2-layers/a2-curved inputs, with their recorded repairs.

With (13) for the actual local systems, the existing argument gives
commutator size \(CC_E/M_1\).
It also gives the absolute walk bounds and column sums.
For the fixed parameter geometry, pw-bridge (6.4)–(6.5) spends
only a reserved fraction of the decay rate:

\[
 |s^{\mathsf P(\omega)}|
 \le e^{16\bar\kappa}
       e^{128\bar\kappa\,t_\omega/\ell_{\mathsf P}},\qquad
 \ell_{\mathsf P}\ge2048\bar\kappa/\tau .
                                                                    \tag{14}
\]

Apply these results in the following order.

1. Use the separated sequence (3), with its native scales, rows and
   inner-plaquette action. A3-close Lemma J supplies the geometry.
   H-walk's local models are now cut-downs of this sequence itself.
   They include each of its crossing rows. No inverse from either
   original part occurs in (12).
2. On each complete read, retain the existing regular-pair ceilings
   \(a_h(L)\) and \(\gamma_j(L)\) of h-walk Theorem H.
   The allowed D2 admission must supply the reference gauges on these
   full reads. For these local models, h-walk Lemma L supplies (13);
   pw-bridge [Coefficients] supplies the strong-norm upgrade.
   This step uses no derivative bound on the independent current.
3. Use the prescribed Definition D tags, including the repaired
   cutoff-denominator reads and the current branches.
   Use the union tag in pw-bridge (7.4) for \(\mathfrak G_s^J\).
   Thus the sums estimate the actual repository prescription.
   They do not require equality with Y's separately tagged response.
4. Keep the existing parameter floors in (14) and
   \(\ell_{\mathsf P}>8R_*\).
   There is no new volume loss in the join.
   Indeed \(\Omega_q^J\subset\Omega_q\), so the native scale is no larger
   and the native metric is no smaller. A set of native diameter
   \(<\ell_{\mathsf P}/2\) also has ambient diameter
   \(<\ell_{\mathsf P}/2\).
   Hence o1-decoupled's hypothesis (P) passes to this join for the
   same parameter cubes, whenever it holds for the prescribed
   ambient partition. The native hull radius still has the bound
   \(R_*=C_LM_1\).

These substitutions give (7) from pw-bridge:512–519 on the admitted
native operator class. Nl-r9 §4 gives the associated raw transpose
and \(M_s^J\) bounds on that same class.
The existing column estimates retain the derivative leg needed for
the force pairing in (2). The current inverse still requires the
small solution ball. It is not an inverse supplied merely by (13).

This is the useful partial result of route 3. The number of parts
does not enter the constants. A new coercivity proof at the seam
would repeat the already universal h-walk input.

The application has two limits. First, the original local core must
actually admit the full native gauges at these ceilings.
Loc-3's D2 *read* clause alone does not assert this admission;
the stronger admission allowed in the task is kept explicit.
No smaller core is silently substituted.
Second, even granting that admission, the prescribed source ball
must fit (6). Native inverse estimates do not imply this numerical
inclusion. The separate calculation below tests it.

**Failure of route 3:** the native walk route supplies the operator
implication, but does not finish J-ENTRY on the prescribed domain.
It reaches the unchanged datum-ball inclusion in §7.
This is a failed completion of the route, not a refutation of the
native inverse theorem.

## 7. The unchanged datum ball

There is a concrete coordinate conversion to retain.
ST1-r4 (6)–(7) distinguishes the raw logarithm from the source in
the straightened response equation:

\[
 B_{\rm raw}=i^{-1}\operatorname{Log}(DV^{-1}),\qquad
 B'=b_V(B_{\rm raw}).
\]

On an interior row \(B'=B_{\rm raw}\).
On an outward row with outer endpoint \(z=c_+\),

\[
 e^{iB'(c)}
   =e^{iB_{\rm raw}(c)}\operatorname{Ad}(V(c))v_z(B_{\rm raw}).
\]

Use the mirror formula when the outer endpoint is \(c_-\).
The factor \(v_z\) reads the interior lower-level rows in its block.
These are the Sussman–Alpoge straightened rows, Y 16128–16205,
as recorded in ST1. They cannot be removed at a new collar row.
The joined target datum \(D\) uses the old data on old rows and
the prescribed lift on new rows, by a3-close Lemma J.
A bound for \(B_{\rm raw}\) must therefore be passed through
this particular completion before it is a bound for \(B'\).

Write \(B=C_{\rm op}e^{16\bar\kappa}\), as in the repository contraction.
Its sufficient datum radius is

\[
             r_{\rm DF}=cC_{\rm op}^{-4}e^{-64\bar\kappa}.
                                                                    \tag{15}
\]

The required comparison is with the move's prescribed source set,
in the raw row units of (4). It is not enough to find some
smaller neighbourhood of zero.

For the TD/DR source specification, td:24–36 and drlocp:77 prescribe
the full product ball of radius
\(s_D=\epsilon_De^{-c_D\bar\kappa}\).
Once its completed source is identified with this move's \(B'\),
that whole open ball fits (15) exactly when

\[
       \epsilon_D C_{\rm op}^4
               e^{(64-c_D)\bar\kappa}\le c.                       \tag{16}
\]

For the common radius \(s_D\le b_*<r_{\rm DF}\) used in drlocp,
the inequality must be strict. This is an elementary comparison
of the two radii; no solver theorem proves it.
If \(c_D\ge64\) and \(\epsilon_D<cC_{\rm op}^{-4}\), it holds for
all \(\bar\kappa\ge0\). If \(c_D<64\), that argument fails at
sufficiently large \(\bar\kappa\).
For the chosen finite \(\bar\kappa\), (16) is the actual test.
Failure of this sufficient-radius test would not prove that the
response itself fails to exist.

Td2:169–182 fixes \(c_D,\epsilon_D\) before \(\bar\kappa\), and then
fixes \(s_D\). It imports the response with these constants.
It does not establish (16) for the independently obtained
\(C_{\rm op},c\). Drlocp:56 already lists \(s_D\le b_*\) as a
premise when its solver and TD's response are combined.
Thus citing that note as the proof of (16) would be circular.
Replacing \(s_D\) by \(\min(s_D,r_{\rm DF}/2)\) would change the
prescribed ball and is not done.

There are two useful but insufficient smaller-source estimates.

* **Real joined datum.** Sussman–Alpoge, Y 13332–13352, bounds the
  actual real collar datum by \(C_{\rm join}\epsilon_1\), uniformly
  in the parts, and explicitly requires it to lie in the response
  disc. Applying dec-field instead requires
  \(C_{\rm join}\epsilon_1<r_{\rm DF}\).
  This estimate concerns the specified real comparison.
  It does not bound every independent complex datum in the
  prescribed product ball.
* **Completed fluctuation source.** From TD's stated Lipschitz
  and linear-source bounds, for \(\|\zeta\|\le A_1\ell^{p_0}\),

  \[
   \|S(v_0+u(s\odot\zeta))\|_{\rm src}
   \le C_AA_1(1+c_Te^{\bar\kappa})
                      e^{-\ell/2}\ell^{p_0}.                    \tag{17}
  \]

  This tends to zero after the earlier constants are fixed.
  TD's last coupling choice can therefore make this subset of
  sources smaller than a fixed positive \(r_{\rm DF}\), provided
  the stated source chart remains admitted.
  It does not reduce the radius of the full independent source
  ball used for its Cauchy estimates.

The complete-response route has a distinct radius
\(r_Y=c_Yb_Y^{-8}\), Y 41183–41225.
It also needs a comparison with the original ball.
The names “small datum” and “regular pair” do not imply either
inclusion. Nor does equality of the physical response imply it.

The precise unresolved assertion is therefore J-ENTRY on the
original domain, even after granting its allowed D2 admission:
identify this joined move's completed datum in the specified raw
row spaces and prove its full prescribed bound against (15).
Equation (16) is the test when that source set is the TD/DR ball.
For a different joined-chart ball, its actual radius and conversion
must replace \(s_D\); TD's radius cannot be assigned to it by name.

## 8. Result and handoff

This stops at alternative **(c)** of the task.
The single named unresolved lemma is **J-ENTRY**, stated in §3.
Three distinct routes to it were attempted:
the complete-response port (§4), transfer through the seam (§5),
and the native local-inverse expansion (§6).
Their failures are failures to complete the stated lemma.
They are not three counterexamples to Yang–Mills.

The kill test passed under the named native solver hypotheses.
The hand examples (8) and (11) refute only the proposed transfer
inferences. There is no counterexample here to D1-JOIN.

The useful entry supplied to DR is the native normalization
dictionary, the direct use of the already universal local-inverse
theorem, and the explicit datum-radius comparison.
This does **not** supply D1 to loc-3/loc-4 Theorem W.
It supplies no all-history statement, D4 admission, stage
interaction theorem, or audit status.
The next work remains on this leaf; no later move type is unlocked.

| Item | Result of this note | Remaining condition |
|---|---|---|
| Repository prior work | Reused, not reproved | Theorem W still consumes D1 |
| Joined geometry | Existing a3-close Lemma J applies in its stated setting | Its collared-geometry hypotheses |
| Zero-wall kill test | Passes conditionally, including the current increment | Native hulls and the common small solver ball |
| Raw rows, transposes and local diagonal | Native normalization identified in (4)–(5) | Actual rows and outward completions retained |
| Native row and column estimates | Existing theorem applies by §6's substitutions | Full D2 gauge admission, existing ceilings and parameter floors |
| Complete-response shortcut | Does not identify the active off-shell current and tags | The matches isolated in §4 |
| Original datum ball | Inclusion in \(cB^{-4}\) not proved | Actual datum identification and (15), or (16) where applicable |
| D1-JOIN / J-ENTRY | Open after the three routes | No new scientific status |

**First open input:** J-ENTRY's original-domain inclusion, starting
with the actual completed joined datum and its unchanged ball.
Do not reopen the universal seam inverse or the fixed-region
component proof to supply this missing comparison.
