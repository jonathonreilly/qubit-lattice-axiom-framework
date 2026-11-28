# Proof lane PW: weighted bounds for the actual decoupled response

Provenance: Research text prepared by Codex in checkout `49fd51008a977cd1ccd1e2ececc6a3ec47079934`; no audit or retained status is asserted. Source material from the Yang--Mills outline and complete account at upstream revision `31a47c543775` is credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. All mathematical discharge in this note must be by hand.

## 1. Contract and current checkpoint

The target is the actual walk prescription of `o1-decoupled.md`, with the
composition prescription for the slice Green operator in `pw-bridge.md`
§7.4. Write its three field outputs as \(H(s),H_1(s),\mathfrak G(s)\).
The required assertion is
\[
 \|H(s)\|_{Y_w\to X_w},\quad
 \|H_1(s)\|_{Y_w\to X_w},\quad
 \|\mathfrak G(s)\|_{F_w\to X_w}
       \le C_{\rm PW}e^{16\bar\kappa}.                         \tag{PW}
\]
Here \(X_w\) includes both \(mA\) and \(m^2\nabla_{\mathbf U}A\),
\(F_w\) includes \(m^3f\), and \(Y_w\) uses dimensionless **raw** rows
with counting measure. Weights have a fixed sufficiently small rate in
the ambient layered metric. Every parameter obeys
\(|s(\Delta)|<e^{\bar\kappa}\). The constant must be chosen before
\(\kappa,\bar\kappa,M\); an eventual parameter-cube side can depend on
\(\bar\kappa\), as IN1 permits.

The per-length physical lifts are denoted \(\mathsf H=H\mathsf m\)
and \(\mathsf H_1=H_1\mathsf m\), where \(\mathsf m\) multiplies
a row by its length. A transpose of these symbols uses the physical
row pairing; a transpose of the raw row map uses counting measure.

This is an independent-current problem. The regular-pair hypotheses are
those in SA 10129–10137: real local gauges of first-order size
\(\alpha_0\), a complex first-order perturbation of size \(\alpha_1\),
and \(|J(b)|\le\gamma_0m_b^{-3}\). They give no difference bound on
\(J\). At switched parameters the sums obey no asserted field equation.
SA 10369–10372 and 10562 and `o1-decoupled.md` explicitly prohibit
importing \(QH(s)=1\) or the undecoupled gauge equation into this argument.

The earlier real, unswitched result is `dr.md` Theorem 9. It uses the
P82 rerun with flux sources and S1–S4; it does not already establish
(PW). The bridge in `pw-bridge.md` is a conditional implication, with
four named premises. The work below first addresses its energy premise
by a different reduction, retaining all remaining dependencies.

**Checkpoint.** The proof is assembled in §§2–8; the current dependency
and recovery record is at the end of §10. The flat/model inputs remain
the explicitly named frozen P82 imports. An algebraic splitting alone
is not used as a pointwise estimate or a decoupling argument.

Source identities: all repository citations are to the stated checkout
unless a later change is explicitly recorded. The two upstream texts
were fetched once to `/tmp/sa_ym4.tex` (32,992 lines) and
`/tmp/sa_ca_I.tex` (166,711 lines), at revision `31a47c543775`.
The outline index and neighbouring rows were consulted before the cited
bounded source excerpts. No numerical run is used as mathematical evidence.

## 2. A local congruence for the eight-variable system

This calculation uses the **actual** unfolded form of `h-walk.md`
§4, not an independently invented off-shell continuation. Let
\(D=D_U\), \(A_s=\Delta_U+Q'^{\mathsf T}m^{-2}Q'\), and
\(K=mQ\). For the moment use a real reference, set both currents to
zero, and replace the Wilson Hessian by \(q^{\mathsf T}q\), with the
same curl and boundary convention as P82. Take row mass one. The
physical row multiplier is converted to counting coordinates by
\(\zeta=m^3\nu\), since
\[
 \langle QA,\nu\rangle_{\rm rows,physical}
       =\langle KA,\zeta\rangle_{\rm count}.                 \tag{2.1}
\]
Write \(t=D^{\mathsf T}A\). The quadratic form of the eight-variable
matrix on \((A;h,\lambda,\mu;h',\lambda',\mu';\nu)\) is
\[
\begin{split}
 \mathcal Q_8={}&\langle A,(q^{\mathsf T}q+K^{\mathsf T}K)A\rangle
 +\langle t,A_s\lambda\rangle-2\langle t,h'\rangle
 +2\langle h,h'\rangle+2\langle h,A_s\lambda'\rangle\\
 &+2\langle\lambda,A_sh'\rangle
 -2\langle\lambda,Q'^{\mathsf T}\mu'\rangle
 -2\langle\mu,Q'\lambda'\rangle+2\langle KA,\zeta\rangle .
                                                               \tag{2.2}
\end{split}
\]
All pairings are the fixed physical fine/top or counting-row pairings.
The coefficient of \(\langle t,A_s\lambda\rangle\) is one, rather
than two: this is the polarization convention in h-walk (4.1).

**Lemma 1 (exact splitting).** The following invertible local change of
variables turns (2.2) into the P82 five-variable quadratic form plus
the negative of its scalar subsystem:
\[
\begin{aligned}
 p&=h'+t/2,& H&=p+h/2,& u&=h-H,\\
 \chi&=\lambda'-\lambda/2,& \psi&=\lambda+\chi,& v&=-\chi,\\
 M_s&=\mu'+\mu/2,& n&=\mu-M_s,& N&=-\zeta.
\end{aligned}                                                   \tag{2.3}
\]
Here \(M_s\) is a top multiplier, not a block size. Precisely,
\[
 \mathcal Q_8
 =\mathcal Q_5(A,H,\psi,M_s,N)-\mathcal Q_{\rm sc}(u,v,n),       \tag{2.4}
\]
where
\[
\begin{aligned}
 \mathcal Q_5={}&\langle A,(q^{\mathsf T}q+DD^{\mathsf T}
                      +K^{\mathsf T}K)A\rangle
 -2\langle D^{\mathsf T}A,H\rangle+\|H\|_2^2\\
 &+2\langle H,A_s\psi\rangle
 -2\langle\psi,Q'^{\mathsf T}M_s\rangle-2\langle KA,N\rangle,\\
 \mathcal Q_{\rm sc}(u,v,n)
       ={}&\|u\|_2^2+2\langle u,A_sv\rangle
                        -2\langle v,Q'^{\mathsf T}n\rangle .
                                                               \tag{2.5}
\end{aligned}
\]
Squares in these algebraic identities mean bilinear squares when
variables are complex.

*Proof.* Substitute \(h'=p-t/2\) in (2.2). The two terms containing
\(\langle t,A_s\lambda\rangle\) cancel by symmetry of \(A_s\).
The remaining terms with \(t\) are \(\|t\|_2^2-2\langle t,p+h/2\rangle\).
Set \(H=p+h/2\), so
\(2\langle h,p\rangle=\|H\|_2^2-\|h-H\|_2^2\).
The remaining scalar derivative terms are
\[
 2\langle\lambda,A_sp\rangle+2\langle h,A_s\lambda'\rangle
 =2\langle H,A_s(\lambda+\chi)\rangle
                         +2\langle u,A_s\chi\rangle.
\]
The top terms are
\(-2\langle\psi,Q'^{\mathsf T}M_s\rangle
  -2\langle\chi,Q'^{\mathsf T}(\mu-M_s)\rangle\).
Now put \(v=-\chi\) and \(N=-\zeta\). This is (2.4).
For invertibility the explicit inverse is
\[
\begin{aligned}
 h&=H+u,&h'&=(H-u-D^{\mathsf T}A)/2,\\
 \lambda&=\psi+v,&\lambda'&=(\psi-v)/2,\\
 \mu&=M_s+n,&\mu'&=(M_s-n)/2,&\zeta&=-N.
\end{aligned}                                                   \tag{2.6}
\]
Thus no inverse, current derivative, or field equation was used. ∎

**Status and norm consequence.** This is an unconditional finite-matrix
identity whenever the stated transposes and boundary spaces match.
The map and its inverse are bounded in the product energy norms:
\(D^{\mathsf T}:E\to L^2\) is bounded, the two scalar slots have the
same norm, and the top and row conversions are isometries in their
specified scaled norms. The transformation has fixed finite read range.
Consequently inverse and supported-source decay estimates for the
five-variable and scalar blocks transfer to the baseline eight-variable
system, **provided the scalar norm used by both blocks is the same**.
P82 uses full weighted second differences, whereas h-walk uses the
\(A_s\) graph norm. Their comparison cannot be skipped.

A fixed positive row mass \(a_0\) changes only the five-variable block.
Its extra form \((a_0-1)\|KA\|^2\) is absorbed by the bounded triangular
change \(N\mapsto N-(a_0-1)KA/2\) in (2.5). This uses the actual
row trace estimate \(\|KA\|_{\rm count}\le C\|A\|_E\).
It changes constants by functions of the early fixed \(a_0\), not
of mesh, \(M\), or \(\bar\kappa\).

## 3. Removing the constraint multiplier: a coercivity lemma

Deleting the \(\nu\) row and column is required for the massive
\(G_1\) factors in the slice Green formula. An inverse for a saddle
matrix alone does not imply an inverse for its unconstrained block.
Positivity supplies the missing implication here.

**Lemma 2 (positive saddle implies massive coercivity).** Let \(E,Y\)
be finite-dimensional Hilbert spaces, \(K:E\to Y\) bounded, and
\(T:E\to E^*\) self-adjoint and nonnegative. Suppose
\[
 \langle a,Ta\rangle\le C_T\|a\|_E^2,\qquad
 \|Ka\|_Y^2\le c_K\langle a,Ta\rangle,                         \tag{3.1}
\]
and the saddle matrix
\(\left(\begin{smallmatrix}T&-K^{\mathsf T}\\-K&0\end{smallmatrix}\right)\)
has inverse of norm at most \(B\) in \(E\oplus Y\).
Then
\[
 \langle a,Ta\rangle
 \ge [B(\sqrt{C_T}+\sqrt{c_K})]^{-2}\|a\|_E^2.                \tag{3.2}
\]

*Proof.* Cauchy–Schwarz for the nonnegative form gives
\(\|Ta\|_{E^*}\le\sqrt{C_T}\langle a,Ta\rangle^{1/2}\).
Apply the saddle inverse to the image of \((a,0)\), namely
\((Ta,-Ka)\), and use (3.1). This gives
\(\|a\|_E\le B(\sqrt{C_T}+\sqrt{c_K})
\langle a,Ta\rangle^{1/2}\), proving (3.2). ∎

For the **real baseline**, elimination of the scalar subsystem gives
\[
 T_0=q^{\mathsf T}q+DRD^{\mathsf T}+a_0K^{\mathsf T}K,
 \quad R=1-SQ'^{\mathsf T}(Q'S^2Q'^{\mathsf T})^{-1}Q'S,
 \quad S=A_s^{-1}.                                           \tag{3.3}
\]
The middle factor \(R\) is an orthogonal projection at real data
(P82 Lemma 2). Thus \(T_0\ge0\),
\(\|Ka\|^2\le a_0^{-1}\langle a,T_0a\rangle\), and boundedness
of curl, divergence and the actual row trace gives the first inequality
in (3.1). P82's five-variable inverse, with zero auxiliary sources,
supplies the saddle bound with the matched norms. Lemma 2 therefore
gives a uniform **unconstrained** inverse at this real baseline.

This argument does not assert positivity at a complex reference or
after the current corrections. Those require a small bounded
perturbation in the same energy spaces. Nor does (3.2) by itself give
local decay or a bound on first differences in a supremum norm.

## 4. Coefficients on the complex regular-pair envelope

The background inputs used from frozen P82 are its I1, I2, I4 and I5, together with P82 Lemmas 1–4, which frozen P82 proves from I1, I2 and I5. From the dr.md §1 walk specification this note also uses the h-walk walk identity, the h-walk Lemma C cut-down clauses and the h-walk-gate repairs. The P82 inputs are:
the matching flat five-variable/scalar inverses, smooth local-model
geometry, the exponential pillar count, and the actual one-step
straightening formulas with their carrier incidence. They retain their
stated hypotheses; this note does not promote their check records to
proofs. No assumption about a current-corrected inverse is included in
this list. I6–I8 (physical background supply and the real Kato estimate)
are not used to construct the inverse below.

### 4.1 The absolute second-jet bound

**Lemma 3 (fixed-leg estimate).** On an admitted actual row carrier of
length \(m_c\), the raw straightened logarithm \(q_c(a)\) satisfies
\[
 \sum_{b'}\|D_bD_{b'}q_c(0)\|
             \le C_L\eta^4m_c^{-2}.                         \tag{4.1}
\]
This holds at complex first-order references below an early ceiling.
The same estimate holds with the two fine legs exchanged. Derivatives
in (4.1) are counting-coordinate derivatives in physical fine fields.

*Proof.* Use the fixed real class gauge on the carrier and its required
enlargement. The complex reference potential has scaled supremum
\(O_L(\alpha_0+\alpha_1)\). The exponential and logarithm series give
this also for its first difference; no gauge for a complex connection
is constructed. Recall the part of P82 Lemma 1, lines 247–269, that
uses only the supremum of this potential. Straightening the reference
relative to the identity produces raw radii \(u_r\) and incremental
endpoint gauges \(z_r\) with
\[
 u_0\le C_L\epsilon L^{-j},\quad
 u_{r+1}\le L(1+C_Lu_r)u_r,\quad
 \|z_r-1\|\le C_Lu_r,\qquad m_c=L^j\eta.                  \tag{4.2}
\]
These inequalities are finite analytic estimates for the actual
one-step straightening, including **both** endpoint factors. They use
I5's flat row sum \(L\), column sum \(L^{-3}\), and the vanishing
of the straightened increment at zero. The proof is unchanged for
complex matrices: replace the real norm estimates for the finite
series by their absolute complex norm estimates.

For completeness, a first-exit argument gives
\(u_r\le2C_L\epsilon L^{r-j}\). Indeed, while this bound holds,
the product of the relative errors is at most
\(\exp(C'_L\epsilon\sum_{r<j}L^{r-j})\); choose the early ceiling
so this is strictly less than two. The geometric sum is at most
\((L-1)^{-1}\). The endpoint gauges have bounded condition numbers
for the same reason. In differentiating the actual recursion the
intermediate endpoint factors are the incremental \(z_r\)'s.
Their errors are summable, not a fixed error repeated at every level.
For a nonzero additional increment, let \(a_r\) be its straightened
raw value in these reference frames. The same first-exit argument
gives \(\|a_r\|_\infty\le C_Lr_0L^{r-j}\). Each one-step
Jacobian at \(a_r\) consequently has row and column bounds
\(L(1+C_L(\epsilon+r_0)L^{r-j})\) and
\(L^{-3}(1+C_L(\epsilon+r_0)L^{r-j})\), including the
incremental frame changes. Their relative errors have the same
geometric sum. Multiplication of these actual Jacobians therefore gives
\[
 \sum_b\|K_a(c,b)\|\le C_Lm_c,
 \qquad \|K_a(c,b)\|\le C_L\eta^4m_c^{-3},
 \qquad K_a=q'(a),                                           \tag{4.3}
\]
on a fixed complex supremum ball \(m_c\|a\|_\infty<r_0\).
The density factor is \(\eta L^{-3j}\), the initial physical
factor \(\eta\) times the **column**, not row, product. The proof
of (4.2) works on this ball after replacing \(\epsilon\) by
\(\epsilon+r_0\). No fine first-difference bound on this additional
increment is required for this analytic row calculation. The first
differences of the reference will be used separately below.

Fix an output color coordinate and an input bond/color coordinate in
the second estimate of (4.3). This Cauchy step needs the reference to lie in the ball of half the radius; that suffices, since (4.1) is used only at the reference itself. Cauchy's one-variable formula on
\(a+zh\), with \(|z|=c/(m_c\|h\|_\infty)\), gives
\[
 \|DK_a[h](c,b)\|\le C_L\eta^4m_c^{-2}\|h\|_\infty.       \tag{4.4}
\]
For a scalar linear functional on a finite product of complex
coordinates, its norm on the coordinate supremum ball is exactly
the sum of the absolute coefficients: choose the coordinate phases
to align them. Apply this fact to each fixed color entry of (4.4)
and sum the finitely many color entries. This converts (4.4) to the
absolute fine-leg sum (4.1), without a factor equal to the number of
fine bonds. Symmetry of the second derivative exchanges the legs.
The one-step outward endpoint convention and the bounded adjacent
carrier multiplicity are retained from I5. ∎

This gives an independent extraction of the moment used in SA
11510–11639 (PX141–PX154) and `nl-r9.md` §3.1. In per-length
coordinates (4.1) is
\(\sum_{b'}\|D_bD_{b'}(q_c/m_c)\|
 \le C_Lm_c(\eta/m_c)^4\), exactly the required second-jet
normalization.

Let \(E_j=\Delta^{(2)}[j]\), with \(|j(c)|\le\gamma_jm_c^{-3}\).
Pairing the per-length Hessian with physical row volume \(m_c^4\)
and dividing by fine volume \(\eta^4\) gives the absolute local
row sum
\[
 \sum_{b'}\|E_j(b,b')\|\le C_L\gamma_j m_b^{-2}.            \tag{4.5}
\]
Here coefficients act by counting sums; equivalently use physical
kernels and include their \(\eta^4\) input measure. Bounded adjacent
carrier overlap and comparability of their scales justify replacing
\(m_c\) by \(m_b\). Symmetry gives the column bound. Hölder followed
by interchange of finite sums proves every local \(L^q\) bound,
\(1\le q\le\infty\), after scaling to \(m=1\). In particular
\[
 |\langle A-D\lambda,E_j(C-D\mu)\rangle|
       \le C_L\gamma_j\|(A,\lambda)\|_{E\oplus\Lambda}
                             \|(C,\mu)\|_{E\oplus\Lambda}.  \tag{4.6}
\]
This is stronger than a quadratic-form estimate alone. It is the
all-scale coefficient estimate needed by the bridge and by tree
vertices.

### 4.2 The other local comparisons

The raw-row and site-row density estimates and their comparison with
the matching flat model are P82 Lemma 1's (17)–(19). Its proof consists
of the summable products above, the pillar averaging formula, and
finite exponential identities. Those steps apply to complex small
potentials as well. In a fixed real class gauge they give
\[
 \|(K_{\mathbf U}-K_1)A\|_{\rm count}
       \le C_L\epsilon\|m^{-1}A\|_2,
 \qquad
 \|(A_{s,\mathbf U}-A_{s,1})\lambda\|_2
       \le C_L\epsilon
          (\|m^{-1}\partial\lambda\|_2+\|m^{-2}\lambda\|_2),
                                                               \tag{4.7}
\]
where \(\epsilon=C_L(\alpha_0+\alpha_1)\) and only the read
closure of the local cutoff is compared. For the second inequality,
opposite transported shifts have first-order difference coefficients
\(O(\epsilon/m)\) and zeroth-order coefficients
\(O(\epsilon/m^2)\). This is where the first difference of the
reference, absent from the purely analytic argument (4.2), is used.
Site-average differences obey the same absolute coefficient bounds
as their values, with an extra factor \(\epsilon\). Schur's
inequality gives the averaging-mass part of (4.7).
These comparisons also make the actual and baseline graph norms
equivalent on the cutoff read closure, with fixed constants. On a
bare model compare with its actual real unitary connection instead
of with the identity.

The Wilson comparison follows directly from the four plaquette
insertions. At plaquette holonomy \(P=1\) their mixed trace is the
product of their sums. Subtracting it at general \(P\) leaves a
factor \(P-1\) in each of sixteen terms. With
\(|P-1|\le\alpha_0\eta^2m^{-2}\), two insertion factors \(\eta\)
leave physical volume \(\eta^4\) times \(C\alpha_0m^{-2}\).
Complex prefixes have bounded condition number on the local class.
Thus the Wilson remainder is of small mass-form size. Changing the
plaquette curl to the consistent forward curl changes a coefficient
by \(O(\epsilon\eta/m^2)\). Multiplication by a neighbouring
fine difference costs at most \(2/\eta\), so this error is also
a bounded value/shift operator of size \(C_L\epsilon/m^2\).
For the forward curl, expansion of opposite shifts cancels the mixed
second differences against \(DD^{\mathsf T}\); the uncancelled
shift commutators contain \(P-1\). It follows, on every full
interior stencil, that
\[
 \Delta^{\rm W}+DD^{\mathsf T}
       =\Delta_{\mathbf U}^{\rm component}+V_0,
 \qquad \|V_0 A\|_{q,\rm loc}
       \le C_L\epsilon\|m^{-2}A\|_{q,\rm loc+}.             \tag{4.8}
\]
This derivation is the finite identity behind SA 11315–11384; it
requires no derivative of curvature. At the genuine action boundary
we use the all-bare estimate, not (4.8) with missing plaquettes.

Finally polarizing the explicit independent-current form (2.2)'s
omitted \(c_J\) gives
\[
 |B_J((A,\lambda),(C,\mu))|
   \le C_L\gamma_0\|(A,\lambda)\|_{E\oplus\Lambda}
                          \|(C,\mu)\|_{E\oplus\Lambda}.     \tag{4.9}
\]
For example \(m^{-3}|\lambda||A|
=(m^{-2}|\lambda|)(m^{-1}|A|)\), and the term with \(D\mu\)
uses \(m^{-1}D\mu\). Apply Cauchy–Schwarz. Endpoint shifts have
bounded transports and comparable scales. No difference of \(J\)
occurs. Its strong scalar variation is retained as a divergence of a
bounded flux, as in `dec-field.md` Lemma 3.1, rather than as a bounded
zeroth-order coefficient.

## 5. The energy premise from the frozen flat systems

**Lemma 4 (passing to the graph norm).** Put
\[
 \|\lambda\|_\Lambda^2=\|m^{-2}\lambda\|_2^2
 +\|m^{-1}D\lambda\|_2^2+\|A_s\lambda\|_2^2.
\]
On the matching flat or bare models,
\(\|\lambda\|_\Lambda\le C_L\|\lambda\|_{H_m^2}\).
Consequently an inverse bound from the dual of P82's full product
norm to that full norm implies its graph-norm inverse bound.
The same implication holds locally with a fixed stencil enlargement.

*Proof.* The Laplacian is a sum of the second differences counted in
\(H_m^2\). The absolute averaging coefficients bound
\(Q'^{\mathsf T}m^{-2}Q'\) by the weighted mass norm. On bare
models both claims follow also from \(m=\eta,Q'=I\). This proves
the norm inequality. If \(\|x\|_{\rm graph}\le C\|x\|_{\rm full}\),
duality gives \(\|F\|_{{\rm full}^*}\le C\|F\|_{{\rm graph}^*}\).
Insert both inequalities into the full inverse estimate. Derivatives
are restricted after evaluation, as in P82; localizing the coefficient
bound only enlarges the read stencil. No reverse norm inequality and
no corner elliptic estimate is needed. ∎

Apply Lemmas 1 and 4 to P82 I1's matching flat local inverses and
P82 Lemma 3's bare local inverses. This supplies a uniform baseline
eight-variable inverse in graph norm on each local model. For the
version without the row multiplier, first use Lemma 2 on the
five-variable block's saddle Schur complement, then eliminate the
scalar subsystem. All off-diagonal blocks are bounded in the stated
norms: for instance
\(|\langle D^{\mathsf T}A,A_s\lambda\rangle|
\le C\|A\|_E\|\lambda\|_\Lambda\).
Thus it supplies the corresponding unconstrained local inverse too.
The scalar three-variable local inverse was already included.

Fixed comparable positive top masses cause no problem. Replacing
\(A_s\) by \(A_s+Q'^{\mathsf T}bQ'\) in (2.5) is the bounded
triangular multiplier change
\(M_s\mapsto M_s-bQ'H\). The scalar block has the identical change
\(n\mapsto n-bQ'u\). Here \(|b|\le C_Lm^{-2}\), so the scaled
norms are preserved up to a fixed constant. This addresses the
comparable top weight allowed in SA 10139, as well as the row mass
handled after Lemma 1.

**Proposition 5 (complex current-corrected local energy).** Under
P82 I1, I2, I4, I5, with sufficiently small early regular-pair and
coefficient ceilings, the actual constrained eight-variable system,
its row-multiplier-deleted version, and its scalar subsystem have
uniform graph-energy inverse bounds on the original sequence and
every h-walk cut-down. For a source supported near a pillar \(z\),
\[
 \|\mathbb K^{-1}F\|_{\mathcal X,y}
       \le B_L e^{-\tau d(y,z)}\|F\|_{\mathcal X^*},          \tag{5.1}
\]
with the analogous inequalities for the other two systems. The
constants and positive rate are chosen before \(M_1,\kappa,
\bar\kappa,M\). The coefficient \(j\) may be any complex row
function satisfying \(\sup_c m_c^3|j(c)|\le\gamma_j\).

*Proof.* Repeat the **local-model parametrix**, not the pointwise
part, of P82 Lemma 4. Use an auxiliary tile side \(M_P\), to be
fixed early, and I2's two-difference cutoffs \(\sum_i\chi_i^2=1\).
On an interior tile use its matching flat model in the supplied real
class gauge. On a bare tile use the actual real unitary connection
and matched Dirichlet spaces. The preceding paragraph supplies the
three required baseline inverses, with a common bound \(B_0(L)\).

Equations (4.6)–(4.9) bound the difference between the actual and
baseline forms, on the entire cutoff read closure, by
\[
 C_L(\alpha_0+\alpha_1+\gamma_0+\gamma_j)
                         \|\Psi\|_{\mathcal X}\|\Phi\|_{\mathcal X}.
                                                               \tag{5.2}
\]
For the apparently third-order mixed block use the form
\(\langle D^{\mathsf T}A,A_s\lambda\rangle\); (4.7) bounds
each changed factor. This uses only first-order reference regularity.
For bare tiles compare only to the real unitary connection, using
the complex perturbation and Wilson curvature bound; no small real
gauge is needed there.

The model commutator has norm \(C_L/M_P\) in the same spaces.
For \(DA_s\), write it as
\([D,\chi]A_s+D[A_s,\chi]\), and move the outside \(D\)
onto the energy test field in the second term. The first two cutoff
differences suffice. Averaging commutators use the oscillation of
the cutoff on a carrier and its absolute coefficient bound. All other
blocks are first differences, masses or bounded-form current terms.
Multiplication by these smooth cutoffs is bounded in graph norm,
because \(A_s(\chi\lambda)=\chi A_s\lambda+[A_s,\chi]\lambda\).
Bounded-overlap assembly and duality therefore apply just as in I2.

Writing \(B=\sum_i\chi_i\mathbb K_i^{-1}\chi_i\), one obtains
\[
 \mathbb K B=I+R_P,\qquad
 \|R_P\|\le A_L(M_P^{-1}+\alpha_0+\alpha_1+\gamma_0+\gamma_j).
                                                               \tag{5.3}
\]
Choose the power \(M_P\) first so the first term is at most
\(1/8\), then the four early ceilings so the rest is at most
\(1/8\). All spaces are finite and square. Hence
\(\mathbb K^{-1}=B\sum_{n\ge0}(-R_P)^n\), uniformly.
Both \(B\) and \(R_P\) have propagation at most
\(h_*=D_LM_P\), since their local inverses remain inside the
finite matching model boxes. The \(n\)-th term vanishes at a local
output farther than \((n+1)h_*+C_L\) from the source and has norm
at most \(B_0,4^{-n}\). Summing this tail proves (5.1), for example
with \(\tau=(\log2)/(D_LM_P)\) after fixed support margins.

For h-walk's cut-downs, Lemma C's (C1)–(C4) preserve the bare-boundary
spaces, the necessary local gauges and the smallness inequalities.
At a point whose cut-down scale is smaller, each regular-pair
inequality only weakens. A gauge cube belongs to the original one-
or two-layer neighbourhood, so its original bound also weakens.
Choose the cut-down size and gap above these parametrix floors, then
the actual \(M_1,R_1\) above h-walk's containment floors.
The cut-down metric dominates the original metric. This proves the
stated uniformity. The failed cross-sequence canonicity of h-walk
(C5) is not used. Holomorphy follows from finite matrix inversion
throughout this complex open envelope. ∎

No exponential weight was multiplied into a scalar graph-norm field
in this proof. The Lipschitz cusp counterexample in h-walk-gate §5
therefore does not affect (5.1).

### 5.1 Existence of the defining Schur factors

There is one additional check before identifying the inverse with
the operators in SA 10141–10155. Invertibility of the scalar saddle
does not alone imply invertibility of \(A_s\).

The elementary discrete Poincaré inequality on each flat pillar is
\[
 \|m^{-1}\lambda\|_2^2
 \le C_L(\|D\lambda\|_2^2+
                     \|m^{-1}Q'\lambda\|_{\rm top}^2).      \tag{5.4}
\]
One hand proof of the flat inequality subtracts the arithmetic mean,
writes each difference of two values along the four coordinate
segments, applies Cauchy–Schwarz along each segment, and sums the
two endpoints. A fine edge is counted at most \(C(m/\eta)^5\)
times before dividing by the number \((m/\eta)^4\) of sites;
the segment-length factor is at most \(4m/\eta\). The resulting
coefficient of an unscaled fine difference is \(C(m/\eta)^2\),
giving \(Cm^2\|D\lambda\|_2^2\). At bare pillars the average
is the identity. In each supplied real gauge, the row and derivative
comparison of §4 adds at most \(C_L\alpha_0^2
\|m^{-1}\lambda\|_2^2\). Sum with bounded overlap and absorb it.
This proves (5.4) for the real reference.

Consequently the real form of \(A_s\) controls
\(\|D\lambda\|_2^2+\|m^{-1}\lambda\|_2^2\) uniformly.
The complex change has relative form norm \(C_L\alpha_1\), by
the same row and first-difference comparisons. A Neumann argument
in this first-order energy space proves invertibility of the actual
complex \(A_s\). If \(Q'A_s^{-2}Q'^{\mathsf T}\) were singular,
its nonzero null vector \(\mu\), together with
\(h=A_s^{-1}Q'^{\mathsf T}\mu\) and
\(\lambda=-A_s^{-2}Q'^{\mathsf T}\mu\), would be a nonzero
null vector of the scalar subsystem. Proposition 5 excludes this.
Thus the site Gram inverse exists. Elimination now is legal.

Deleting the row multiplier in Proposition 5 gives invertible
\(T=G^{-1}\) or \(G_1[j]^{-1}\). The constrained inverse then
implies invertibility of \(QT^{-1}Q^{\mathsf T}\), by the ordinary
finite Schur complement. h-walk Lemma U's elimination identifies
its \(A\nu\) and \(AA\) blocks with the defining lifts and
constrained Green operators. This independently checks the Schur
complement of the congruence: it is precisely
\(q^{\mathsf T}q+DRD^{\mathsf T}+a_0K^{\mathsf T}K\) at the
baseline. At the actual pair it is
\[
 T=\Delta^{\rm W}+DRD^{\mathsf T}+Q^{\mathsf T}aQ
           -\Delta'_\pi[J]-\mathsf S^{\mathsf T}E_j\mathsf S,
 \qquad \mathsf S=1-DA_s^{-1}RD^{\mathsf T}.
\]
Take \(j=0\) for the first system and
\(j=\mathsf H^{\mathsf T}J\) for the second, in that order.
There is no substitution of a saddle inverse for an
unproved massive inverse.

## 6. From local energy to the field and its first difference

This section uses and checks the represented-source route in
`pw-bridge.md` §§3–5. It applies to the actual cut-down inverse before
the switches are inserted. It is not an equation for a switched sum.

Set \(p=h'+D^{\mathsf T}A/2\) and represent sources by
\[
 f=f_\circ+\tfrac12Dg'_h,\qquad
                  g_\lambda=u_\lambda+D^{\mathsf T}z_\lambda. \tag{6.1}
\]
In local scale-one units, \(\mathcal S\) is the sum of the
\(L^8\) norms of \(f_\circ,g_h,g'_h,u_\lambda,z_\lambda,
g'_\lambda\) and the maxima of the three top/row sources
\(g_\mu,g'_\mu,f_\nu\). The scalings are respectively
\[
 (m^3,m^2,m^2,m^4,m^3,m^4,1,1,m).                            \tag{6.2}
\]
The support includes the supports of these representing densities
and their stencils. Infima over representations on that support are
allowed. Pairing divergences against first differences proves
\(\|F\|_{\mathcal X^*}\le C_L\|F\|_{\mathcal S}\) for a
source supported on a fixed pillar enlargement.

The solution norm \(\mathcal R\) is
\[
 A,\lambda,\lambda',h\text{ in }W^{2,8},\qquad
 p\text{ in }W^{1,8},\qquad \mu,\mu',\nu\text{ in local maxima},
                                                               \tag{6.3}
\]
with scalings \((mA,\lambda,\lambda',m^2h,m^2p,
m^4\mu,m^4\mu',m^3\nu)\). Derivatives use coordinates \(x/m\)
and the local measure is \(m^{-4}\eta^4\). In particular this norm
controls the desired \(X\) output. It does **not** bound
\(\nabla p\) in supremum.

The exact eight equations, after the source combination (6.1), are
\[
\begin{aligned}
 (\Delta^{\rm W}+DD^{\mathsf T})A
   &=f_\circ+Dp+\tfrac12Dh-Q^{\mathsf T}aQA-Q^{\mathsf T}\nu-F_A,\\
 A_sh&=g'_\lambda+Q'^{\mathsf T}\mu,\\
 A_sp&=u_\lambda+D^{\mathsf T}z_\lambda+Q'^{\mathsf T}\mu'
                                         -F_\lambda-D^{\mathsf T}Z_\lambda,\\
 A_s\lambda&=D^{\mathsf T}A+g'_h-h,\\
 A_s\lambda'&=g_h-p+\tfrac12D^{\mathsf T}A,\\
 Q'\lambda&=-g'_\mu,\quad Q'\lambda'=-g_\mu,\quad QA=f_\nu.
\end{aligned}                                                   \tag{6.4}
\]
The two current forms have, for \(q=2,3,8\),
\[
 \|F_A\|_q+\|F_\lambda\|_q+\|Z_\lambda\|_q
 \le C_L(\gamma_0+\gamma_j)
                (\|A\|_q+\|\lambda\|_q+\|D\lambda\|_q).   \tag{6.5}
\]
For \(c_J\), differentiation in \(\lambda\) leaves the transpose
of \(D\) outside the bracket of \(J\) with \(\lambda\);
all other terms are endpoint products. For \(E_j\) the variations
are \(E_j(A-D\lambda)\) and its divergence. Equation (4.5) and
Hölder give (6.5). This verifies the strong input used here, not
merely its energy-form analogue.

**Lemma 6 (local mixed estimate).** On fixed nested pillar
neighbourhoods of any admitted cut-down,
\[
 \|\Psi\|_{\mathcal R,y}\le C_L
   \left(\sum_{x\in y^{++}}\|\Psi\|_{\mathcal X,x}
                         +\|F\|_{\mathcal S,y^{++}}\right).  \tag{6.6}
\]
The number of neighbours and the constant are independent of mesh
and \(M_1\).

*Hand proof of the analytic ingredients.* On the unit lattice the
free Green multiplier is
\(\Lambda(t)^{-1}=(4\sum_i\sin^2(t_i/2))^{-1}\).
For \(k\le3\), a product of \(k\) differences has multiplier
derivatives bounded near zero by \(C_a|t|^{k-2-a}\).
For \(|x|=R\), split at \(|t|=R^{-1}\); the small ball contributes
\(CR^{-2-k}\). On its complement integrate \(k+3\) times in
a coordinate with \(|x_i|\) comparable to \(R\). The differentiated
integral is at most \(CR\), giving the same bound. Cutoff
derivatives have that scale too. After rescaling,
\[
 |D^kG_\eta(x)|\le C_k(|x|+\eta)^{-2-k},\quad 0\le k\le3. \tag{6.7}
\]
The multiplier of \(D_iD_j^*\Delta^{-1}\) has absolute value
at most one. Its kernel has size \(C(|x|+\eta)^{-4}\) and
first-difference modulus \(C(|x|+\eta)^{-5}\), by (6.7).
For a dyadic bad cube in the usual average-height decomposition,
subtract the kernel at a chosen point of the cube. Its mean-zero
bad part contributes at most \(C2^{-r}\|b_Q\|_1\) on the
\(r\)-th outer shell. The enlarged cubes have total volume at most
\(C\|f\|_1/t\), and the good part has squared \(L^2\) norm
at most \(16t\|f\|_1\). Chebyshev and the multiplier bound give
the weak \((1,1)\) estimate with mesh-independent constant.
Single-site cubes have zero bad part.

For \(1<q<2\), split \(f\) at height \(t\), apply the weak
bound to \(|f|>t\) and the \(L^2\) bound to \(|f|\le t\),
and integrate the distribution function against \(qt^{q-1}\).
The two integrals at a site are constants times
\(|f|^q/(q-1)\) and \(|f|^q/(2-q)\). Duality gives the bound
for \(q>2\). Thus the required discrete Calderón–Zygmund estimates
hold, including all orientations and finitely many complex colors.

Cut off a source outside an intermediate cube and convolve with
\(G_\eta\). The kernels of orders two and three are locally
integrable uniformly in mesh, and the second derivatives use the
preceding bound. The remaining harmonic function has all needed
interior derivatives bounded by its \(L^2\) norm: test against a
squared cutoff, iterate Caccioppoli on commuting flat differences,
then telescope in the four coordinates. This proves, on fixed
nested cubes,
\[
\begin{aligned}
 \|u\|_{W^{2,q}}&\le C_q(\|u\|_{2,\rm outer}+\|F\|_{q,\rm outer}),
                  &&\Delta u=F,\\
 \|u\|_{W^{1,q}}&\le C_q(\|u\|_{2,\rm outer}
                     +\|F\|_{q,\rm outer}+\|Z\|_{q,\rm outer}),
                  &&\Delta u=F+D^*Z .
\end{aligned}                                                   \tag{6.8}
\]
For bounded radius-to-mesh ratio direct point evaluation proves the
same scaled inequalities. Finally \(DG_\eta\), restricted to a
fixed ball, is uniformly in \(L^a\) for every \(a<4/3\).
Apply the convolution inequality with \(a=6/5,24/19,8/7\),
respectively, to a cut-off function written as
\(\Delta^{-1}D^*Du\). This proves the strict embeddings
\[
 W^{1,2}\longrightarrow L^3,\quad
 W^{1,3}\longrightarrow L^8,\quad
 W^{1,8}\longrightarrow L^\infty .                           \tag{6.9}
\]
These are the hand ingredients of pw-bridge §4; no boundedness of
a Riesz transform on \(L^\infty\) is being invoked.

*Bootstrap for (6.6).* In the real class gauge,
\(\Delta_{\mathbf U}=\Delta+B\partial+C\), where
\(|B|+|\partial B|+|C|\le C_L(\alpha_0+\alpha_1)\) in
local units. The drift can also be written as a divergence of a
bounded coefficient times the field, plus a bounded value term.
This follows from the finite-difference product rule and is useful
before a derivative of that field is known. The averaging masses
and transposed top/row terms map local energy to bounded forces,
by their density bounds. Each individual multiplier is controlled
by its local weighted \(\ell^2\) norm.

Starting with graph energy, (6.8) gives
\(\lambda,\lambda'\in W^{2,2}\). Write the drifts in the
\(h,p\) equations as divergences; their \(L^2\) values and
(6.5) give \(h,p\in W^{1,2}\). Then the \(h\) equation gives
\(h\in W^{2,2}\), and the field equation gives
\(A\in W^{2,2}\), since \(Dp,Dh\in L^2\).
The first embedding in (6.9) puts the controlled fields and their
first differences in \(L^3\), with \(p\in L^3\).
The \(p\) equation in divergence form gives \(W^{1,3}\);
the other four equations give \(W^{2,3}\).
Repeat using the second embedding: the sources and the controlled
first differences are in \(L^8\), so \(p\in W^{1,8}\) and
the other four fields are in \(W^{2,8}\). A fixed number of nested
margins suffices. Equation (6.9) now controls the field gradient
in supremum. There is no step asserting a supremum bound for
\(Dp\), or differentiating \(J\).

At a genuine bare boundary, \(m=\eta\); direct point evaluation
in the scaled energy norm controls all the finitely many differences
just used. Nonbare outputs have a full interior neighbourhood by
separation. Artificial cut-down boundaries lie outside the cutoff
and commutator read neighbourhoods. This completes the proof. ∎

### 6.1 Closure under the prescribed cutoffs

There is a necessary cancellation here; an arbitrary rough source
norm would not suffice. For \(F=[\mathbb K,\chi]\Psi\),
\[
 g'_h=-[D^{\mathsf T},\chi]A+[A_s,\chi]\lambda.
\]
Subtracting \(Dg'_h/2\) from the field source cancels the whole
\(D[A_s,\chi]\lambda/2\) term, including its averaging mass.
The remaining principal field terms are
\[
 [\Delta^{\rm W}+Q^{\mathsf T}aQ,\chi]A
 +\tfrac12[D,\chi]A_s\lambda
 +\tfrac12D[D^{\mathsf T},\chi]A-[D,\chi]h'
 +[Q^{\mathsf T},\chi]\nu.                                  \tag{6.10}
\]
Current-block commutators add the bounded force terms of (6.5).
In the scalar-dual entry the exact identity is
\[
 \tfrac12[A_sD^{\mathsf T},\chi]A+[A_s,\chi]h'
   =[A_s,\chi]p+\tfrac12A_s[D^{\mathsf T},\chi]A.             \tag{6.11}
\]
Keep the kinetic part of the last term as a divergence. Its flux
uses one derivative of \([D^{\mathsf T},\chi]A\), hence at most
two cutoff differences and one of \(A\). No third cutoff difference
or second difference of \(p\) is needed. The other entries are
\([A_s,\chi]\lambda'\), \([A_s,\chi]h-[Q'^{\mathsf T},\chi]\mu\),
and averaging commutators on \(A,\lambda,\lambda'\).
These identities check every differential source slot.

With the actual walk cutoffs, their first two scaled differences
are \(O_L(M_1^{-1})\). Thus
\[
 \|[\mathbb K,\chi]\Psi\|_{\mathcal S,y}
       \le C_LM_1^{-1}\sum_{x\in y^+}\|\Psi\|_{\mathcal R,x}.
                                                               \tag{6.12}
\]
For source multiplication,
\((\chi F)_\circ=\chi f_\circ-[D,\chi]g'_h/2\), and
the flux slot has the analogous product rule. For solution
multiplication,
\(p(\chi\Psi)=\chi p+[D^{\mathsf T},\chi]A/2\).
They preserve \(\mathcal S\) and \(\mathcal R\). A coefficient
vertex has no \(g'_h\) slot and is bounded in these norms by
\(C_L\sup m^3|j_\beta|\), using (4.5) and (6.5).
Thus (6.12) applies throughout the **actual** walk and tree products.

Combining Proposition 5 with (6.6), for a represented source supported
near \(z\), gives
\[
 \|\mathbb K_\kappa^{-1}F\|_{\mathcal R,y}
       \le C_L e^{-\tau d(y,z)}\|F\|_{\mathcal S}.           \tag{6.13}
\]
The local source term in (6.6) is absent when \(y\) is far from
\(z\), and otherwise costs a fixed enlargement of the constant.
This proves the pointwise local input that energy alone did not give.

## 7. The actual walks, the second lift, and the composed Green operator

All coefficients in this section are unswitched coefficients until
§8. Their cut-down inverse matrices, cutoffs and read sets are the
ones in h-walk, with the fixed-region field-read and count repairs
recorded in h-walk-gate §§5–8 and o1-decoupled Definition D. No new
choice of a Boolean interpolation replaces them.

For \(j=0\), the exact local/global agreement on the cutoff stencil
gives \(\mathbb K B=1-R\), with
\(R_\kappa=-[\mathbb K,\widetilde h_\kappa]
\mathbb K_\kappa^{-1}\theta_\kappa\). Iteration gives the
prescribed terms \(T_\omega\). Apply (6.12)–(6.13) successively,
partitioning intermediate sources by smooth pillar cutoffs. For a
fixed walk of \(n\) steps this yields
\[
 \|T_\omega F_z\|_{\mathcal R,y}
 \le C_L(C_L/M_1)^n
       e^{-(\tau/2)t_\omega(y,z)}\|F_z\|_{\mathcal S}.       \tag{7.1}
\]
Indeed, before summation the exponent is \(-\tau\) times the sum
of all leg lengths. Half of it pays the path meeting all required
cells. Sum the other half backwards over the intermediate pillars;
each sum is bounded by \(K_{\tau/2}\). P82 I4 supplies these
constants after an early gap floor. This also makes the remainder
small, since only boundedly many walk cells meet a fixed output
pillar and the sum is \(O_L(M_1^{-1})\).

A raw row column uses source \(f_\nu=e\delta_c/m_c\), whose
dual and local \(\mathcal S\) norms are bounded by \(C_L|e|\).
This is why the conversion from \(\mathsf H\) to \(H\) leaves
no source-length factor. The physical transpose coefficient is
\[
 j_\beta(c)=m_c^{-4}\langle [T_\beta]_{A\nu}e_c,J\rangle_f.
\]
The unnormalized source \(e_c\) has dual norm \(m_c\).
Cauchy–Schwarz on each pillar gives
\(\|J\|_{E^*,y}\le C_L\gamma_0\).
Split the exponential in (7.1) between its endpoint distance and
the obligation to visit the cells, and sum the endpoint. The exact
scale cancellation is \(m_c^3m_c^{-4}m_c=1\). Hence
\[
 m_c^3|j_\beta(c)|
 \le C_L\gamma_0(C_L/M_1)^{|\beta|}
                      e^{-(\tau/4)t_\beta(c)}.               \tag{7.2}
\]
At most a fixed number of terminal cutoff supports meet a given row.
Backward walk counting proves absolute summability, and in particular
\(\|m^3j^{(0)}\|_\infty\le C_0\gamma_0\), where
\(j^{(0)}=\sum_{|\beta|=0}j_\beta\). The full sum satisfies
\(\|m^3\mathsf H^{\mathsf T}J\|_\infty
\le C_J\gamma_0\) with another early constant. Shrink the
current ceiling so that both bounds are at most the already
established \(\gamma_j\).

Use this **same** \(j^{(0)}\) in the local second-system matrices;
insert the positive-length \(j_\beta\)'s as the actual vertices.
Proposition 5 applies to these matrices without requiring their
coefficients to equal a physical current. If \(B^{(0)}\) is their
parametrix and \(V_\beta\) the coefficient vertex, then exactly
\[
 \mathbb K_1B^{(0)}=1-R^{(0)}+
                  \sum_{|\beta|\ge1}V_\beta B^{(0)}.
\]
The additional remainder has norm at most
\(C_L\gamma_0\sum_{m\ge1}(C_L/M_1)^m\), by (7.2), the
vertex bound and the endpoint sums. Choose the early floor so the
total remainder norm is at most \(3/4\). Expanding its Neumann
series is precisely h-walk's decorated-tree expansion, for both
the constrained and row-multiplier-deleted systems. This checks
resummation as well as coefficient bounds. If a trunk has \(n\)
steps, \(v\) vertices and branch lengths \(m_i\ge1\), the
available smallness power and total tree size are
\[
 p_*=n-v+\sum_i m_i,\qquad N=n+\sum_i(m_i+1),\qquad
 3p_*-N=2(n-v)+2\sum_i(m_i-1)\ge0.                           \tag{7.3}
\]
Retain the coefficient factor \(C_L^{n+\sum_i m_i}\); it must
not be shortened to \(C_L^n\). The trunk and branch paths join
at their interaction pillars. Allocate \(\tau/4\) to a tree
meeting their cells and endpoints; the remaining trunk exponent
sums its intermediate pillars. This proves
\[
 \|T^{(1)}_\omega F_z\|_{\mathcal R,y}
 \le C_L(C_LM_1^{-1/3})^{N}
          e^{-(\tau/4)t_\omega(y,z)}\|F_z\|_{\mathcal S}.    \tag{7.4}
\]
There are at most \(C_0C_1^N\) terms at a fixed root: choose the
trunk, its vertex positions, the backward branches and a composition
of the total length. All these choices have exponential counts by
bounded overlap. The prefactor covers the length-zero multiplicity.
Fixed stencil offsets cost \(C_L^{N+1}\), never
\(\exp(cM_1)\). These statements prove the second-system tree
estimate with its actual coefficient factors.

The constrained \(A\nu\) blocks in (7.1), (7.4) are the given
\(H,H_1\) coefficients. The constrained \(AA\) blocks of (7.4),
called \(P_\omega\), sum at one to
\(G_1-\mathsf H_1QG_1\).
Deleting \(\nu\) gives field terms \(G_\alpha\) summing to
\(G_1\), with exactly the same estimates, coefficient and branch
choices. The scalar system gives terms \(L_\sigma\) for its
\(h\leftarrow h\) block, summing to \(P_{\rm sc}=1-R\).
Its two equations \(A_sh=s_\lambda+Q'^{\mathsf T}\mu\),
\(A_s\lambda=s_h-h\) give \(W^{2,8}\) for both scalar outputs;
their commutators use at most two cutoff differences. Thus these
terms accept an \(L^8\) scalar input and satisfy (7.1).

The prescribed three families for the slice Green operator are
\[
 P_\omega,\qquad G_\alpha DD^{\mathsf T}G_\beta,
 \qquad G_\alpha D L_\sigma D^{\mathsf T}G_\beta.             \tag{7.5}
\]
For a pillar-supported force, the rightmost \(G_\beta\) gives
\(W^{2,8}\), so \(DD^{\mathsf T}G_\beta f\) is an \(L^8\)
force of the required scale. In the third family the types are
\[
 m^3f\ \,\xrightarrow{G_\beta}\,mA\
 \xrightarrow{D^{\mathsf T}}m^2v\
 \xrightarrow{L_\sigma}m^2h\
 \xrightarrow D m^3Dh\
 \xrightarrow{G_\alpha}mA_{\rm out}.                         \tag{7.6}
\]
All derivatives act on complete coefficients, including their
cutoffs. Only the first difference of the reference is needed to
compare second covariant differences with ordinary ones. Partition
the intermediate sources into smooth pillar pieces. Reserve
\(3\tau/16\) for the combined tree and \(\tau/16\) for each
of the at most two intermediate sums; successive convolution uses
\(K_{\tau/16}\). Every factor initially has rate at least
\(\tau/4\). Thus each composite \(O_\omega\) satisfies
\[
 \|O_\omega f_z\|_{X,y}
 \le C_L(C_LM_1^{-1/3})^{N}
                e^{-(3\tau/16)t_\omega(y,z)}\|f_z\|_{\mathcal S}.
                                                               \tag{7.7}
\]
Splitting \(N\) between at most three factors costs at most
\((N+1)^2\le4^{N+1}\). Successive roots overlap the preceding
terminal cell, so their choices have a bounded multiplicity. The
count remains \(C_0C_1^N\). The two joining edges carry no
\(M_1\) power and are not falsely counted as smallness factors.
This completes the unswitched coefficient estimates needed for all
three actual operators.

## 8. Insert the switches once per full hull

Use o1-decoupled Definition D, including every length-zero term and
the extra field reads in \(j^{(0)}\). For the three families (7.5),
form the composite coefficient **before** tagging. Its tag set is
the union of all constituent full enlarged hulls and connecting
derivative stencils. The operator is exactly
\[
\begin{split}
 \mathfrak G(s)={}&\sum_\omega s^{\mathsf P(\omega)}P_\omega
 -\sum_{\alpha,\beta}s^{\mathsf P(\alpha,\beta)}
                                    G_\alpha DD^{\mathsf T}G_\beta\\
 &+\sum_{\alpha,\sigma,\beta}s^{\mathsf P(\alpha,\sigma,\beta)}
                             G_\alpha D L_\sigma D^{\mathsf T}G_\beta.
\end{split}                                                     \tag{8.1}
\]
This is the specification already adopted in `dr.md` §1 and
pw-bridge (7.4). Multiplying separately decoupled factors would give
a different family and an unnecessary \(e^{48\bar\kappa}\)
estimate. We do not make that replacement.

Every full read hull lies within \(R_*=C_LM_1\) of the connected
tree counted above. The original walk cell, its sharper enlargement,
the cut-down's field reads, and the bounded number of extra
zero-length-coefficient read boxes are included. For a composite
there are at most two extra connecting stencils; enlarge the fixed
constant in \(R_*\) once. These are fixed-region field read sets;
no unproved equality between different region sequences is needed.

Take a parameter grid satisfying (P), meaning a set of ambient
metric diameter less than \(\ell_{\mathsf P}/2\) meets at most
sixteen closed parameter cubes. The sufficient physical-side
condition in o1-decoupled line 116 follows from
\(d(x,x')\ge|x-x'|/\xi_{\max}\) and the four coordinate
projections. Traverse a tree of length \(t\) twice and cut the
traversal into arcs of length at most \(\ell_{\mathsf P}/4\).
If \(\ell_{\mathsf P}>8R_*\), each thickened arc has diameter
less than \(\ell_{\mathsf P}/2\). Therefore
\[
 \#\mathsf P(\omega)\le16+128t/\ell_{\mathsf P},\qquad
 |s^{\mathsf P(\omega)}|
     \le e^{16\bar\kappa}
               e^{128\bar\kappa t/\ell_{\mathsf P}}.         \tag{8.2}
\]
The constant sixteen includes the root and length-zero terms. It
appears **once** for the connected hull of a composite, not once
for each factor.

Choose
\[
 \ell_{\mathsf P}>8R_*,\qquad
 \ell_{\mathsf P}\ge2048\bar\kappa/\tau.                   \tag{8.3}
\]
Then switch growth spends at most \(\tau/16\) of the tree
exponent. Equations (7.1), (7.4), (7.7) leave at least
\(\tau/8\) for a common endpoint bound. Fix the early \(M_1\)
floor so that the exponential count times
\(C_LM_1^{-1/3}\) is at most \(1/2\). The sum over all term
sizes is at most a fixed constant. Thus, for raw row columns and
pillar-supported forces respectively,
\[
\begin{aligned}
 \|H(s)(\cdot,c)e\|_{X,y}
  +\|H_1(s)(\cdot,c)e\|_{X,y}
       &\le C_Le^{16\bar\kappa}e^{-(\tau/8)d(y,c)}|e|,\\
 \|\mathfrak G(s)f_z\|_{X,y}
       &\le C_Le^{16\bar\kappa}e^{-(\tau/8)d(y,z)}
                                             \|f_z\|_{\mathcal S}.
\end{aligned}                                                   \tag{8.4}
\]
The estimates are valid for the entire closed parameter radius
\(|s_\Delta|\le e^{\bar\kappa}\) wherever the reference remains
in its open admitted envelope. In particular they hold on the
requested open polydisc.

For \(w(y)/w(z)\le e^{\theta d(y,z)}\), \(\theta\le\tau/16\),
multiply (8.4) by \(w(y)\). The remaining endpoint exponential
sums by \(K_{\tau/16}\). There are boundedly many rows per pillar.
For a general force use smooth pillar-supported pieces, each with
\(\mathcal S\) norm at most \(C_Lw(z)^{-1}\|f\|_{F,w}\).
This proves all three operator bounds (PW). At no point is a
derivative taken of the weight or of a switch.

Normal convergence on the pair and parameter domains proves joint
holomorphy. At \(s=1\) the same absolute bounds justify composing
and summing (7.5). Equation (8.1) then gives
\[
 \mathfrak G(1)=G_1-\mathsf H_1QG_1
                    -G_1D(1-P_{\rm sc})D^{\mathsf T}G_1
 =G_1-\mathsf H_1QG_1-G_1DRD^{\mathsf T}G_1,                  \tag{8.5}
\]
with the exact order and signs of dec-field (5.3).
The two lift identifications were proved by elimination in §5.1.
Equations (8.4), not an equation for \(H(s)\), establish the
switched estimate.

## 9. Constant order, alternative routes, and scope

The choice order is IN1 rows 1–10, with Amendment 1, not a choice
of a regularity constant after seeing \(M\) or \(\bar\kappa\).
In detail:

1. Keep row 1's fixed exponents and margins. In row 2 choose odd
   \(L\) above both its original floors and \(L_0^\natural\).
   Fix the frozen flat/averaging constants.
2. Within row 3 (c4-order rows 4–5), choose \(M_P\), a provisional
   larger regular envelope, the local inverse constant and
   \(\tau\). Choose auxiliary cut-down size and gap with
   \(\tau\rho'\ge256\log L\), all containment floors, and the
   common smaller rate if other packages already require one.
   The pillar sums are uniformly bounded above on all geometries
   beyond this auxiliary gap. Compute the constants in §§6–7 on
   that larger envelope. Shrink the final current ceiling to ensure
   \(\max(C_0,C_J)\gamma_0\le\gamma_j\); this does not redefine the rate
   or constants already established on the larger envelope.
3. Still in row 3, choose the actual \(M_1\) and then \(R_1\),
   with the walk/tree count floors, P82 divisibility, and
   \(R_1\ge8L^3\). All constants in (8.4), including its final
   weight sum, have uniform bounds for larger \(M_1,R_1\).
   Fix \(C_{\rm PW}\) from these bounds now.
4. Row 4 may then choose \(\kappa\), respecting
   \(\kappa\ge\kappa_0^\natural(L)\). Row 5 chooses
   \(\bar\kappa\), then \(\ell_{\mathsf P}\) by (8.3), and
   eventually \(M\) large enough for the parameter grid and the
   other listed floors. Only the explicit factor
   \(e^{16\bar\kappa}\) enters (PW).
5. The actual radii/current bounds in row 6 lie below the fixed
   envelopes. Rows 7–10 and the final coupling choice do not
   redefine \(C_{\rm PW}\). Both floors added by Amendment 1
   are compatible with this order.

The Boolean proposal in `dr.md` §5 and dr-draft §6 is an alternative
construction. Its exact interpolation identity is valid, but a
real-wall inverse bound does not supply its mixed-difference
majorant. Nor does it identify that interpolant with these walk
coefficients. The single-cube empty-region mismatch and possible
nonbare artificial boundaries remain objections to the proposed
wall realization. We have not proved a uniform weighted-wall
theorem WW. It is unnecessary for the actual walk family, whose
terms were estimated directly in §§6–8. This is not a counterexample
to WW under an eventual correct specification or to (PW).

The rough-current and energy-spike examples in dec-field remain
valid. The former refutes treating a scalar current variation as
a bounded pointwise coefficient; (6.5) keeps its divergence. The
latter refutes an energy-to-supremum embedding for arbitrary fields;
(6.6) uses the local equations and the exact represented sources.
Similarly the graph-norm cusp example refutes arbitrary Lipschitz
conjugation in that norm; Proposition 5 uses finite propagation.
None of these route failures was promoted to a counterexample to
the field bound.

Frozen CP12 supplies conditional physical-reference regularity.
Its on-shell current hypotheses do not apply to the independent
current here. This proof uses the regular-pair gauge clause itself,
not a claim that CP12 constructs all complex reference pairs. The
separate **admission** question at dr.md line 32 remains: a named
ST1 chain domain must actually lie in this regular-pair envelope.
The complete account explicitly separates application supply from
its free-current operator implication (CA-I 49495–49547).
Likewise this proof does not establish the nonlinear response,
cross-sequence transport, or all of DR. Those are different claims
from the three specified operator bounds (PW).

## 10. Source and proof ledger

The following bounded passages were checked against the sources,
after consulting their index entries and neighbouring rows. SA and
CA authorship is as credited in the Provenance line.

| Source | Use and status in this note |
|---|---|
| SA 5762–5803 | R9 consists of specified maps, including walk coefficients; its current increment and response properties are additional inputs. |
| SA 10113–10155, 10163–10198 | Geometry, regular complex pairs, actual raw/per-length conventions, ordered defining inverses and explicit off-shell current continuation. These define the objects estimated here. |
| SA 10354–10404 | Weighted first-order norms and the claimed \(Ce^{16\bar\kappa}\) estimate. The claim itself was not used as a proof. |
| SA 10529–10583 | Unfolding, divergence sources, trees, parameters, the lack of switched identities and the constant order. The quantitative estimates were supplied above. |
| SA 11315–11384 | Four-insertion Wilson formula, curl convention, curvature-shift remainder and complex form comparison; boundary qualifications retained. |
| SA 11508–11639 | Actual straightening recursion and two-leg moments. Lemma 3 extracts the absolute fixed-leg estimate by Cauchy and checks its physical normalization. |
| CA-I 49495–49547; indexed in ca-4.12-4.19/chunk-06 | Application supply is outside the free-current operator implication; no chain-domain inclusion is inferred from it. |
| Frozen p82.md, whole; especially I1/I2/I4/I5 and Lemmas 1–4 | The existing flat/model backbone, boundary spaces, averaging formulas and counts remain imports with their stated hypotheses. Lemmas 1–5 above extend its energy argument to the actual unfolded systems. |
| Frozen cp12.md, whole | Checked for the physical-reference and regularity boundary; not used to infer independent-current or complex gauge admission. |
| dr.md, whole; dr-draft.md §6 | Earlier real first-lift result, flux/scalar route, Boolean interpolation and the unresolved wall specification distinguished from the present actual-walk route. |
| dec-field.md and o1-decoupled.md, whole | Counterexamples to auxiliary steps, the exact PW contract and the adopted full-hull switch specification. |
| pw-bridge.md, whole; nl-r9.md §3.1; h-walk §§3–7 and gate §§5–8 | The represented sources, local bootstrap, cutoff cancellations and composition scheme were checked and used. The bridge's energy and absolute second-jet premises are addressed in §§4–5, rather than imported as four inverse inequalities. |

The supplied Balaban OCR copies were also consulted: CMP **99**
(1985), 389–434, pp. 421–423, (3.128)–(3.138) and Theorem 3.12
(local text lines 1820–1954), and CMP **109** (1987), 249–301,
pp. 261–263, (1.8)–(1.16) (lines 662–785). The former preserves a
derivative on the neighbouring factor and excludes a Laplacian
estimate; the latter introduces the independent pair and first-order
reference conditions. These guided the route. Garbled OCR formulas
are not premises or verbatim transcriptions in this proof. The
explicit algebra and estimates above supply the needed statements.
The local-model and random-walk method is credited to Tadeusz
Bałaban; the inherited flat port also credits Jonathan Dimock.

**Final checkpoint.** The new hand arguments are the local congruence,
positive-saddle coercivity, absolute fixed-leg Cauchy estimate,
complex graph-energy parametrix and scalar Schur-factor check.
The represented-source bootstrap and its two cancellation identities
then apply to the unchanged coefficient specification. The final
length/parameter sum proves all three bounds. The frozen flat/model
imports and the regular-envelope hypothesis remain explicit; no
additional PW-specific energy, second-jet, or weighted-wall lemma is
left as an assumption. The admission of any further application
domain is separate. No numerical calculation, interval certificate,
or finite test has discharged any part of the argument. This is one
author's research proof, without an independent review or status.

Final bookkeeping: the checkout is still pinned at `49fd51008`, and
the tracked sources used above are unchanged against that pin. Only
`library/pw.md` was added. A recovery copy is kept at
`/tmp/pw-49fd51008-evidence/pw.md`; the two fetched source hashes
are in `/tmp/pw-49fd51008-evidence/source-sha256.txt`.
The file's whitespace check is editorial bookkeeping, not a
mathematical verification.

## Result

**Proof**

Under the frozen P82 inputs I1, I2, I4 and I5 (with P82 Lemmas 1–4) with their matching
boundary and geometry hypotheses, the dr.md §1 walk specification (with the h-walk identity, Lemma C cut-down clauses and h-walk-gate repairs), and a parameter partition satisfying (P) of §8 (as in o1-decoupled Theorem B; (P) fails if parameter cubes get finer in finer layers), the **actual** decoupled walk
family specified in dr.md §1 satisfies
\[
 \boxed{\displaystyle
 \|H(s)\|_{Y_w\to X_w},\quad
 \|H_1(s)\|_{Y_w\to X_w},\quad
 \|\mathfrak G(s)\|_{F_w\to X_w}
       \le C_{\rm PW}e^{16\bar\kappa}.}
\]
It holds for every admitted real or complex regular pair with an
independent bounded current, every weight of rate
\(\theta\le\tau/16\), and the whole decoupling polydisc, with
the early ceilings and geometric floors specified above.
\(C_{\rm PW}\) and \(\tau>0\) are fixed before \(\kappa\)
and are uniform in depth, mesh, volume, admissible region shape,
and \(M_1\) above its floor. They are independent of \(M\)
and of \(\bar\kappa\); the latter enters only through the
displayed factor and the permitted parameter-length choice.
The proof grants no audit or retained status and does not assert
the separate DR chain-domain admission.

## Change log (freeze, 2026-11-05)

Written by Codex in one proof-lane round. Refereed line by line by a fresh Claude session ([pw-gate](../gates/pw-gate.md)): first failing step none, 3 findings, all repairable. Applied by the lead (Claude):

1. §4 and the Result name every input used: P82 Lemmas 1–4 (proved in frozen P82 from I1, I2, I5), and the h-walk identity, Lemma C cut-down clauses and h-walk-gate repairs from the dr.md §1 walk specification. The mathematics is unchanged.
2. The Cauchy step for (4.4) needs the reference in the half-radius ball; stated. (4.1) is used only at the reference.
3. The Result's hypotheses include the parameter-partition condition (P) of §8, which o1-decoupled Theorem B already carries.

Referee on how the proof passes dr-draft §6's three failures: the rough current enters only the field row and one auxiliary unknown's equation, as the divergence of a bounded flux with no difference of the current; switched operators are absolutely convergent sums of unswitched terms times switch monomials, each bounded on its own; WW is not needed.

Not read line by line by the referee: SA 11315–11384 and 11510–11639; the text re-proves those steps by hand.

Status: **frozen.** [PW] is proved as claimed, conditional on frozen P82, the dr.md walk specification, the regular-pair envelope and (P). This removes [PW] from dr.md's Outstanding list.

