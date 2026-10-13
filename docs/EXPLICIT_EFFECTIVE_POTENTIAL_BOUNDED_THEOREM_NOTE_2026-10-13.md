---
claim_id: explicit_effective_potential_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Supplied ordinary-cell interaction: every fixed finite explicit coefficient order has a global coefficient remainder and a bounded even selfadjoint full-low potential norm remainder; later comparison records the conditional same-kinetic replacement consequence."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: publication_prepared_exact_root_review_pending
runner: scripts/explicit_effective_potential_identity_2026_10_13.py
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: "Fixed positive mass and velocity, fixed real smooth compact inputs and finite polynomial complexity; exact supplied cells, frame, polarization and CAR conventions."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Accepted ordinary coefficient and potential theorem with later conditional comparison evidence; exact core is unchanged and source assembly is accepted and new publication wrappers await review."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Root review of the exact publication wrappers, identity tools and driver before any runtime or publication action."
upstream_dependencies:
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
---

# Explicit effective potential: publication wrapper

Claim type: bounded_theorem

All 600 lines of the accepted core follow without alteration, SHA-256
`8f1e13d1ca4c42bbf4e5483c4035cacf28fd2bc82ee4b470776409e7753323be`.
The new wrapper and appendix describe source integration and later review
chronology. Root accepted the exact source assembly; this publication
wrapper and identity-only tool await separate exact review. No scientific
rerun or retained-status action occurs in publication preparation.

The order and all input smearings are fixed before the spacing limit. The
remainder constants depend on the chosen order, positive mass and velocity,
finitely many weighted Sobolev norms, and the fixed polynomial prescription.
The maps retain the actual one-sided cell phase, half-density, frame and
arcsine argument transport. The real CAR field norm, grading and two-point
normalization are literal; high-vacuum contractions are included in the exact
compression even when they are beyond every fixed power for these inputs.

The coefficients give bounded even selfadjoint operators on the full unital
low Fock representation. Compact physical support of the original input does
not by itself make every effective coefficient exactly local. No new spatial
classification or propagation result is included in this milestone.

The core establishes the coefficient/potential remainder. Its original
reservation about growing-time dynamics is preserved. The later accepted
comparison separately identifies the bounded same-kinetic replacement cost;
the appendix states that boundary without importing a kinetic domain proof
into this unchanged body. The companion corrected-dispersion and moment
theorems retain their own carrier, regularity, state and time assumptions.

The derivation excluded the then-new root candidates but was exposed to the
earlier first-order coefficient through its allowed smooth-high sources.
The later comparison is source-exposed. This assembly reuses exact accepted
source coverage and makes no fresh independent mathematical-review claim.
All original pending-review statements and failure records remain historical.

# Finite-order ordinary-cell potential expansion on the full low Fock space

Status: conditional-support; bounded theorem proposal under the supplied
one-dimensional chain, state, cell and current-preserving coordinate choices.
Claim type: bounded_theorem. Trace class: upstream_support. This is an ordinary
analytic derivation, not an audit verdict or formal verification. Current's
open_gate status remains inherited. No physical model-selection claim is made.

Every fixed finite order has a global L2 coefficient remainder and an operator
norm remainder for the induced finite even CAR polynomial. The expansions use
the actual one-sided cells, arcsine argument transport, half-density and frame.
They are asymptotic statements with constants depending on finitely many input
norms and on the chosen order. The high-vacuum contractions are present in the
exact compression but are beyond every fixed order for smooth compact inputs.
The second coefficient already contains a spatially nonlocal term.

## 1. Sources, exposure and exact scope

Let R be this note's directory and E=R/effective_potential_independent.
E/PROOF_SOURCE_PLAN.md was frozen before the first semantic read of scientific
contents; source bytes had already been copied and hashed for that plan.
The plan has SHA-256 `6629b761586abef8fdf295deb81be41d2a5a258533d4cef92d63cc30fe2a7591`.
All four allowed scientific notes were read completely from frozen copies:

| Name | SHA-256 | Use |
|---|---|---|
| CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md | `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff` | Current C2/C4/C8/C19/C20: exact symbols, frame, branches and cells |
| LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md | `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa` | Real CAR normalization, covariance, Fock realization and even-spin identification |
| SMOOTH_HIGH_BAND_DECOUPLING_INDEPENDENT.md | `c69d638eb4519d81e51dd39fd920b7323d320d5aea9c427ff109736bdcda75dd` | Exact high-tail estimate, full/low/high placement and compression conventions |
| SMOOTH_HIGH_BAND_DECOUPLING_CROSSCHECK.md | `1a10d9c613bf7760f0e9d6e55f9f690b495c4225a101bf69af2711ab245a6f58` | Source-exposed clarification of unital extensions, support and formal selfadjointness |

The last two sources expose the prior first-order coefficient. No blindness to
that coefficient is claimed. No root candidate, root addendum, campaign
STATE/HANDOFF, publication packet or another worker's active draft was read.
The crosscheck contains summaries of earlier root work; that expressly allowed
exposure is distinct from access to those original bodies. Exact source paths,
frozen copies and procedural identities are in E/SOURCE_MANIFEST.json, and
complete read ranges are recorded in E/READ_LOG.md.

The task uses fixed m,v>0, fixed real two-component inputs and a fixed finite
formally selfadjoint even polynomial. Its coefficients, degrees and number of
terms are independent of c. It is a bounded total potential. No extensive sum,
kinetic expansion, energy-dependent Schur term, growing-time comparison,
ground-state statement or current conservation of the perturbation is proved
here. Those are separate questions. The ordinary analytic tools below are
Fourier Plancherel, finite Taylor remainders, elementary changes of variables,
and finite CAR algebra followed by norm completion.

## 2. The exact low coefficient before expansion

Use the unitary Fourier convention
\(\widehat f(p)=(2\pi)^{-1/2}\int e^{-ipx}f(x)\,dx\). The cells are
\[
 (C_cf)_j=c^{-1/2}\int_{cj}^{c(j+1)}f(x)\,dx,\qquad
 J_cC_cf=(\ell_cf,h_cf).
 \tag{1}
\]
Here J_c is exactly Current C8. Both branch projections of J_cC_c are
contractions, and all these maps preserve position reality. The frame matrices
and scalar couplings used below are
\[
 F(p)=e^{-i\arctan(vp/m)\sigma_z/2},\qquad
 F_c(q)=e^{-i\arg(g_c-\mathsf J_ce^{-icq})\sigma_z/2},
\]
\[
 \sigma_c=\sqrt{m^2/4+v^2/c^2},\quad
 g_c=\sigma_c/2+m/4,\quad \mathsf J_c=\sigma_c/2-m/4.
\]
The chain entry has positive real part, fixing its continuous argument. Write
\[
 t=\arcsin(cp),\quad q_c(p)=t/c,\quad
 w=(1-c^2p^2)^{1/2},\quad |cp|<1,\quad
 a(t)=e^{it/2}\operatorname{sinc}(t/2).
\]
The literal low Fourier coefficient is
\[
 \widehat{\ell_cf}(p)=\mathbf1_{|cp|<1}w^{-1/2}F(p)^*F_c(q_c(p))
 \sum_{n\in\mathbb Z}a(t+2\pi n)
                  \widehat f(q_c(p)+2\pi n/c).
 \tag{2}
\]
For suitable dense test inputs this follows by integrating a Fourier mode over
one cell, then summing its translates; the contraction extends the map to L2.
Equation (2) is not used to bound an infinite alias sum term by term. The
positive cell phase is fixed by the interval [cj,c(j+1)].

For input Fourier support inside \(|ck|<\eta<\pi/2\), there are no aliases,
the input lies entirely in the low branch, and (2) is
\[
 \widehat{\ell_cf}(p)=\mathbf1_{|cp|<1}M(c,p)\widehat f(q_c(p)).
 \tag{3}
\]
There is a useful exact desingularization of its frame. Set
\[
 \mu=\frac{m}{2v},\quad \zeta(p)=\frac{vp}{m},\quad
 B=\frac12I+\frac14\sigma_z,
\]
\[
 A(c,p)=\frac{2\sqrt{1+\mu^2c^2}}{1+\sqrt{1-c^2p^2}},\qquad
 d(c,p)=\arctan(\zeta(p)A(c,p))-\arctan\zeta(p).
\]
Then
\[
 \boxed{M(c,p)=w^{-1/2}\operatorname{sinc}(t/2)
                    e^{itB}e^{-id(c,p)\sigma_z/2}.}
 \tag{4}
\]
To check (4) directly, distinguish the scalar coupling \(\mathsf J_c\) from
the isometry J_c. With
\(\sigma_c=\sqrt{m^2/4+v^2/c^2}\),
\[
 g_c-\mathsf J_ce^{-it}
 =e^{-it/2}\big[(m/2)\cos(t/2)+i\sigma_c\sin(t/2)\big].
\]
The bracket has positive real part on the low arc. Consequently the complete
complex entry has continuous argument \(-t/2+\arctan(\zeta A)\). Subtracting
the target angle \(\arctan\zeta\), applying the frame half-angle, and multiplying the cell phase
gives (4). The absolute density factor is \(w^{-1/2}\); the norm measure
identity is \(dp/w=dq\). It becomes singular at the moving edge, which is why
the proof below never Taylor expands over that edge.

## 3. Coefficients, including transport

Put \(E(p)^2=m^2+v^2p^2\) and
\[
 \kappa(p)=\frac{mp(m^2+2v^2p^2)}{8vE(p)^2}
          =\frac{mp}{4v}-\frac{m^3p}{8vE(p)^2}.
 \tag{5}
\]
Expansion at fixed p gives
\[
 q_c(p)=p+\frac{c^2p^3}{6}+\frac{3c^4p^5}{40}+O(c^6),
 \qquad d(c,p)=c^2\kappa(p)+O(c^4),
\]
\[
 w^{-1/2}\operatorname{sinc}(t/2)=1+\frac{5c^2p^2}{24}+O(c^4).
 \tag{6}
\]
These fixed-p expansions only identify coefficients; they are not the global
remainder argument. Define matrices
\[
 C=\frac5{96}I-\frac18\sigma_z,\qquad
 D=\frac{29}{192}I+\frac{23}{384}\sigma_z.
\]
For \(u=\widehat f\), the first four coefficient maps are
\[
 \widehat{T_0f}=u,\qquad \widehat{T_1f}=ipB\,u,
 \tag{7}
\]
\[
 \boxed{\widehat{T_2f}=
       \left(p^2C-\frac i2\kappa\sigma_z\right)u
                   +\frac{p^3}{6}u',}
 \tag{8}
\]
\[
 \boxed{\widehat{T_3f}=
       \left(ip^3D+\frac{p\kappa}{2}B\sigma_z\right)u
                   +\frac{ip^4}{6}B\,u'.}
 \tag{9}
\]
For example, the multiplier's cubic coefficient is
\(ip^3[(3/8)B-B^3/6]+(p\kappa/2)B\sigma_z\), equal to (9)'s multiplier.
The \(u'\) terms come from the argument transport. Dropping them changes the
coefficient already at order two.

All orders have an unambiguous finite prescription:
\[
 \boxed{\widehat{T_nf}(p)=\sum_{j=0}^{\lfloor n/2\rfloor}
 \left.\frac1{n!}\partial_c^n
       \left[M(c,p)\frac{(q_c(p)-p)^j}{j!}\right]\right|_{c=0}
       \partial_p^j\widehat f(p).}
 \tag{10}
\]
The smooth extension of (4) at c=0 is meant; no physical negative-spacing
model is introduced. Since q_c-p is even and starts at order two, only the
displayed finitely many derivatives occur. Equations (4) and (10), rather than
an assumed pattern in the first coefficients, define every finite order.
Each T_n preserves real inputs. This follows either from (4)'s reflection and
complex-conjugation identity or by differentiating the real coefficient map
on an alias-free core.
Write \(\mathsf T_n=\mathcal F T_n\mathcal F^{-1}\) for the Fourier
differential expression (10) when its input is already a Fourier function.

## 4. A global remainder with explicit sufficient finite regularity

For an integer r>=1 let k=ceil(r/2), and define
\[
 \mathcal X_r=\{f:x^jf\in H^{r+j}(\mathbb R;\mathbb C^2),\ 0\le j\le k\},
\]
\[
 \mathcal N_r(f)=\sum_{j=0}^{k}\|x^jf\|_{H^{r+j}}
   =\sum_{j=0}^{k}\|\langle p\rangle^{r+j}
                                    \partial_p^j\widehat f\|_2.
 \tag{11}
\]
The Sobolev norm here uses the multiplier \(\langle p\rangle^s\).
With the norm \(\mathcal N_r\), (12) is equivalently an
\(O(c^r)\) operator remainder from \(\mathcal X_r\) to L2.

**Coefficient theorem.** For fixed m,v>0, every integer r>=1 and fixed finite
c_0>0, there is a finite constant C_r, depending on these quantities and the
cutoff chosen in the proof, such that
\[
 \boxed{\left\|\ell_cf-\sum_{n=0}^{r-1}c^nT_nf\right\|_2
             \le C_r c^r\mathcal N_r(f),\quad
             f\in\mathcal X_r,\ 0<c\le c_0.}
 \tag{12}
\]
One may harmlessly reduce c_0 to one. Enlarging the constant covers any fixed
remaining compact interval of positive c, using contraction and the bounded
maps from \(\mathcal X_r\) to L2. The regularity is sufficient, not claimed
minimal. On a fixed bounded spatial interval, compactly supported
\(H^{r+\lceil r/2\rceil}\) inputs satisfy (11), with the bound also depending
on the interval. In particular fixed smooth compact inputs satisfy (12) at
every fixed r. Uniformity holds over bounded \(\mathcal N_r\)-families, not
merely from a declaration that each member is smooth.

**Proof.** Choose a real even smooth cutoff chi equal to one on
[-1/8,1/8], supported in (-1/4,1/4), and set
\(u_c(p)=\chi(cp)\widehat f(p)\). The omitted input satisfies
\[
 \|(1-\chi(c\,\cdot))\widehat f\|_2
                 \le C c^r\|\langle p\rangle^r\widehat f\|_2.
 \tag{13}
\]
By contraction of \(\ell_c\), its exact low image has the same bound. This
controls the entire omitted alias sum and the entire omitted edge region.
No pointwise upper bound on the singular half-density is used there.

For u_c the exact formula is (3), and the output is supported in
\(|cp|<\sin(1/4)\). All \(\mathsf T_nu_c\) are supported in \(|cp|<1/4\).
Thus it suffices to work on \(|cp|\le1/2\), where every factor of M is
uniformly bounded. For every fixed integer a>=0,
\[
 \|\partial_c^aM(c,p)\|\le C_a\langle p\rangle^a
                         \quad (|cp|\le1/2,\ 0\le c\le c_0).
 \tag{14}
\]
For the frame part, A(c,p) is a smooth function of (c,cp) in a compact set
and stays in a compact positive interval. For every a>=1 the functions
\(\partial_A^a\arctan(\zeta A)\) are uniformly bounded over all real zeta and
that A interval: their rational formulas are bounded at zeta=0 and decay at infinity.
The chain rule gives (14). The sinc, density and t factors have the same
bound directly. This justifies (14) also when |p| grows as c decreases.

Taylor-expand the transported input in its argument through degree k-1:
\[
 u_c(q_c(p))=\sum_{j=0}^{k-1}\frac{(q_c-p)^j}{j!}u_c^{(j)}(p)
 +\frac{(q_c-p)^k}{(k-1)!}\int_0^1(1-s)^{k-1}
                            u_c^{(k)}(y_s(p))\,ds,
\]
\[
 y_s(p)=p+s(q_c(p)-p).
 \tag{15}
\]
On this fractional band,
\[
 |q_c-p|\le Cc^2|p|^3,\quad
 |p|\le|y_s(p)|\le C|p|,\quad
 y_s'(p)=1+s((1-c^2p^2)^{-1/2}-1)\ge1.
 \tag{16}
\]
Since 2k-r is either zero or one,
\[
 c^{2k}|p|^{3k}\le Cc^r\langle p\rangle^{r+k}
                        \quad (|cp|\le1/2).
\]
Minkowski and the monotone change of variables y_s therefore bound the
L2 norm of M times the remainder in (15) by
\[
 Cc^r\|\langle p\rangle^{r+k}u_c^{(k)}\|_2.
 \tag{17}
\]

For each j<k put \(S_j=M(q_c-p)^j/j!\). Write
\(q_c=pR(cp)\), where \(R(z)=\arcsin(z)/z\) is smooth and even on the
fractional band. The product and chain rules, together with (14), give
\[
 \|\partial_c^aS_j(c,p)\|\le C_{a,j}\langle p\rangle^{a+j}.
\]
Moreover S_j vanishes to order 2j at c=0. Taylor's integral remainder in c,
through degree r-1, is therefore bounded by
\(C c^r\langle p\rangle^{r+j}\), and its retained coefficients give exactly
(10). Multiplication by \(u_c^{(j)}\), summation, and (17) prove (12) with
f replaced by the cutoff input and with \(\mathcal N_r\) of that input.

Leibniz' rule removes the c-dependent cutoff from that norm: whenever a>0
derivatives hit chi, the factor \(c^a\chi^{(a)}(cp)\) is supported where
\(|p|\asymp c^{-1}\), and its c^a factor removes a powers of the weight.
Hence
\[
 \|\langle p\rangle^{r+j}u_c^{(j)}\|_2
 \le C\sum_{b=0}^{j}\|\langle p\rangle^{r+b}\widehat f^{(b)}\|_2.
 \tag{18}
\]
Finally each coefficient multiplying \(\widehat f^{(j)}\) in T_n is bounded
by \(C\langle p\rangle^{n+j}\). On the support of 1-chi or a cutoff
derivative, \(|p|\ge1/(8c)\). Thus, for n<r, each term in
\(c^n\mathsf T_n[(1-\chi(c\,\cdot))\widehat f]\) is bounded in L2 by
\(C c^r\mathcal N_r(f)\), again using Leibniz' rule. Together with (13),
this proves the full global statement.

The argument initially applies to smooth Fourier inputs. Cutoff and
mollification are dense in the finitely weighted derivative norm (11);
the displayed bounds pass to that completion. Equivalently (15) holds for
the one-dimensional local Sobolev representatives, and (16) controls their
compositions. This supplies the stated \(\mathcal X_r\) domain. QED.

## 5. The finite continuum CAR-polynomial potential

To specify the common representation, let \(\mathcal K=L^2(\mathbb R;\mathbb C^2)\)
with position conjugation, let \(\mathcal P\) have Fourier multiplier
\(F(p)^*P_0F(p)\), where \(P_0=(I-\sigma_y)/2\), and put
\(\mathcal F_L=\mathcal F_-(\mathcal P\mathcal K)\). For real f, use
\(\gamma_L(f)=a^*(\sqrt2\mathcal Pf)+a(\sqrt2\mathcal Pf)\).
The high representation uses the constant multiplier P_0 in the same way.
These are exactly the supplied pure quasifree representations; no new state
is selected by this definition.

Let the prescribed polynomial, including its formal adjoint symmetry, be
\[
 V_c=\sum_\alpha z_\alpha\prod_{j=1}^{d_\alpha}
                    \gamma(\ell_cf_{\alpha j},h_cf_{\alpha j}),
 \qquad d_\alpha\text{ even}.
 \tag{19}
\]
Degree zero is allowed. A presentation such as \((U_c+U_c^*)/2\) is sufficient;
accidental selfadjointness from a spacing-dependent Gram identity is not the
hypothesis. All input functions are real. The Majorana norm is
\(\|\gamma_L(f)\|=\|f\|_2\), and the fields are real-linear.

Fix N>=0 and take all inputs in \(\mathcal X_{N+1}\). For 0<=n<=N define
full low-Fock operators by
\[
 \boxed{\mathcal V_n=\sum_\alpha z_\alpha
   \sum_{\substack{n_1+\cdots+n_{d_\alpha}=n\\n_j\ge0}}
      \prod_{j=1}^{d_\alpha}\gamma_L(T_{n_j}f_{\alpha j}),\qquad
 V^{[N]}(c)=\sum_{n=0}^{N}c^n\mathcal V_n.}
 \tag{20}
\]
The slot order is always preserved. For degree zero, only n=0 contributes.
In particular \(\mathcal V_0\) is the original continuum polynomial,
\(\mathcal V_1\) sums replacements of one slot by \(B\partial_xf\), and
\(\mathcal V_2\) sums one T_2 replacement plus every pair of distinct T_1
replacements. This is an explicitly finite even CAR polynomial at every
order. Every \(\mathcal V_n\) is bounded and selfadjoint on the full low Fock
space; formal adjunction reverses each word and preserves its total c degree.
T_n itself need not be bounded on bare L2: only its finitely many prescribed
smearings are used in a bounded field.

Let \(V_c^L\) be (19) evaluated with every high coefficient set to zero.
For r=N+1 and all inputs in \(\mathcal X_r\),
\[
 \boxed{\|V_c^L-V^{[N]}(c)\|\le C_{\mathrm{pol},r}c^r.}
 \tag{21}
\]
This is an operator norm estimate on the entire continuum low Fock space,
with no particle cutoff. To see it, first substitute
\(g_j^{[N]}(c)=\sum_{n=0}^{N}c^nT_nf_j\) into the full polynomial. Finite
product telescoping and (12) bound the substitution error by
\[
 C_rc^r\sum_\alpha|z_\alpha|\sum_j\mathcal N_r(f_{\alpha j})
 \prod_{k\ne j}\max\!\left(\|f_{\alpha k}\|,
                  \sum_{n=0}^{N}c_0^n\|T_nf_{\alpha k}\|\right).
 \tag{22}
\]
The substituted polynomial has finitely many powers of c. Its terms of total
degree at least r are bounded by c^r times the sum of their fixed coefficient
norms multiplied by \(c_0^{\text{degree}-r}\). Discarding them proves (21).
This proof also covers zero input slots without division by their norms.

## 6. Exact high-vacuum contractions and their remainder

On the low-first Fock tensor product use precisely
\[
 \gamma(\ell,h)=\gamma_L(\ell)\otimes I+
                  Z_L\otimes\gamma_H(h),\qquad
 P=I\otimes|\Omega_H\rangle\langle\Omega_H|.
\]
Define the unital full low-Fock potential W_c by
\[
 PV_cP=W_c\otimes|\Omega_H\rangle\langle\Omega_H|.
 \tag{23}
\]
For a single ordered monomial of degree d, write \(\ell_j=\ell_cf_j\),
\(h_j=h_cf_j\). If S is its set of high slots, let
\(\nu(S)=\#\{(i,j):i\in S,j\notin S,i<j\}\). Its exact compression is
\[
 \boxed{\sum_{\substack{S\subset\{1,\ldots,d\}\\|S|\text{ even}}}
 (-1)^{\nu(S)}\operatorname{Pf}(G_S)
                      \prod_{j\notin S}^{\text{original order}}
                                        \gamma_L(\ell_j).}
 \tag{24}
\]
For S in its inherited order, \((G_S)_{ab}=2\langle h_a,P_0h_b\rangle\)
for a<b, with negative lower triangle and zero diagonal; P_0=(1-sigma_y)/2.
The empty Pfaffian and empty field product are one. Moving each high parity
factor past later low odd fields produces the sign \((-1)^{\nu(S)}\).
An even number of parity factors then cancels. Odd high moments vanish;
the even high moments are exactly the displayed Pfaffians. This fixes both
the crossing signs and the covariance normalization, without assuming normal
ordering. Applying (24) to every monomial gives W_c, including scalar and
lower-degree corrections.

The exact high-tail estimate follows from the original q measure:
\[
 \|h_cf\|^2=\int_{\pi/(2c)<|q|<\pi/c}|(L_cC_cf)(q)|^2\,dq,
\qquad
 \|h_cf\|\le\|\mathbf1_{|p|\ge\pi/(2c)}\widehat f\|_2.
 \tag{25}
\]
Indeed a Fourier input inside \(|p|<\pi/(2c)\) has zero high output,
including all aliases, and h_c is a contraction. In particular
\(\|h_cf\|\le(2c/\pi)^s\||p|^s\widehat f\|_2\) for f in H^s; for a
fixed input the corresponding bound with the tail indicator is o(c^s).

For \(b_{\alpha j}=\|f_{\alpha j}\|\) and
\(t_{\alpha j}=\|h_cf_{\alpha j}\|\), one has the finite pair bound
\[
 \boxed{\|W_c-V_c^L\|\le
 \sum_\alpha|z_\alpha|\sum_{i<j}t_{\alpha i}t_{\alpha j}
                         \prod_{k\ne i,j}b_{\alpha k}.}
 \tag{26}
\]
For a concise proof, interpolate all high slots by a parameter u in [0,1]
before compression. The first derivative at u=0 has one high field and
vanishes. The second derivative is twice the unordered pair sum. Every
untouched field has norm
\(\sqrt{\|\ell_j\|^2+u^2\|h_j\|^2}\le b_j\). Taylor's integral weight
has integral 1/2, giving exactly (26), including higher even-high terms.

For the \(\mathcal X_r\) hypotheses of (12), (26) is O(c^{2r}). Combining
it with (21) proves the requested actual compression expansion
\[
 \boxed{\left\|W_c-\sum_{n=0}^{N}c^n\mathcal V_n\right\|
                 \le \widetilde C_{\mathrm{pol},N}c^{N+1}.}
 \tag{27}
\]
For fixed smooth compact inputs (25)-(26) hold at every finite order, so no
nonempty high contraction contributes to any finite coefficient in (20).
This is compatible with their being nonzero at every fixed c. It is not
permission to replace exact vacuum compression by setting the high fields
to zero in an unexpanded identity.

The actual finite-spacing physical low Fock range has all outside-band modes
in vacuum. W_c and V_c^L have in-band coefficients and even parity, so their
unital extensions are the same in-band operators tensored with identity on
outside modes, with the same norm. The comparison (27) takes place on full
low Fock space. No zero-energy extension of a finite-band Hamiltonian or norm
convergence of band projections is used.

## 7. Spatial meaning and scope of the expansion

The first correction is local in the given spatial coordinate:
\(T_1f=B\partial_xf\). The second is more revealing. Let
\(R_m=(m^2-v^2\partial_x^2)^{-1}\), the bounded Fourier multiplier E(p)^-2.
Equations (5) and (8) give
\[
 \boxed{T_2f=\frac16\partial_x^3(xf)-C\partial_x^2f
       -\frac{m}{8v}\sigma_z\partial_xf
       +\frac{m^3}{16v}\sigma_z\partial_xR_mf.}
 \tag{28}
\]
The ordinary convolution kernel of R_m is
\(G_m(x)=e^{-m|x|/v}/(2mv)\), as direct differentiation away from zero and
its derivative jump at zero verify. If f is supported in [L,R], then for x>R,
\[
 (\partial_xR_mf)(x)
 =-\frac{e^{-mx/v}}{2v^2}\int e^{my/v}f(y)\,dy,
 \tag{29}
\]
with the analogous positive left tail. A nonzero nonnegative scalar bump in
one component has a nonzero right moment, so T_2f has a nonzero exterior
tail while all other terms in (28) vanish there. Thus compact spatial input
does not generally give compact support for every T_n input of (20).
Particular polynomial cancellations or moment cancellations must be examined
separately before assigning a local algebra to a correction.

For the original compact inputs, V_c remains an actual finite even-spin
observable supported in their cell hull, by the parent even-Jordan-Wigner
identification. Spectral projection and frame comparison need not preserve
that finite support. These two statements concern different representations
of the same supplied construction. The potential expansion is bounded on
full low Fock space, but no local boost, causal interacting net, or extensive
interaction conclusion is inferred from it.

All constants are for fixed positive m,v and fixed finite polynomial data.
There is no assertion uniform in the expansion order, a changing input
family, its derivative/moment norms, polynomial degree, total coupling or
volume. No convergence of the infinite formal series is asserted. In
particular smooth compactness alone is used to permit each finite order,
not to supply an order-independent analytic radius.

The fixed-input quantifier has a direct control. Choose a nonzero real smooth
compact bump phi and normalize \(f_c(x)=\phi(x)\cos(2x/c)e_1\) to norm one.
Its two Fourier packets are centered at \(\pm2/c\), so its Fourier mass in
\((-1/c,1/c)\) tends to zero by the fixed envelope's Fourier tail. The exact
output \(\ell_cf_c\) is supported in that band. Therefore
\[
 \|\ell_cf_c-f_c\|_2\ge
             \|\mathbf1_{|p|\ge1/c}\widehat f_c\|_2\longrightarrow1.
 \tag{30}
\]
The family has a fixed compact support and each member is smooth, but its
derivative norms grow. Thus even the zeroth-order limit is not uniform over
the L2 unit ball of such smooth inputs. This does not change the fixed-input
or bounded-\(\mathcal N_r\)-family conclusion (12).

## 8. Verification and remaining obligations

The complete analytic argument above is the proof proposal. The separately
saved E/algebra_checks.py is a narrow same-context author diagnostic, not an
independent analytic checker. Its scalar route starts from the original
complex chain entry \(2(g_c-\mathsf J_ce^{-it})\), divides by its positive
energy norm, and takes the formal frame fractional power. It does not use
(4)'s arctangent factorization. It checks the first four coefficients for
both sigma_z eigenvalues, including the transported input jet. Its finite
CAR route starts from literal Pauli/Jordan-Wigner matrices and compares their
high-vacuum compression with (24). Complete result and repair records are
kept in E. Exact rational/symbolic residuals are zero for the multiplier and
transported jet at orders zero through three, for both sigma_z eigenvalues.
The literal degree-two, degree-four and degree-six compression matrices agree
entrywise after exact algebraic simplification. The explicit coefficient
covariance 2P_0 also agrees with all 36 literal Pauli-vacuum two-point entries
before it is used in the Pfaffian formula.

The scalar mutations are detected at their first changed coefficients:
omitting density gives \(-p^2u/4\) at order two; reversing the cell phase gives
\(-ipu\) at order one; omitting transport gives \(-p^3u'/6\) at order two;
reversing the frame gives \(-ip\sigma_zu/2\) at order one. The finite CAR
checks detect halving the two-point covariance and discarding the high
contractions at every tested degree. Omitting the graded crossing sign is
detected at degrees four and six and correctly survives degree two, where no
such crossing occurs. Complete rational residuals are in E/algebra_results.json.

The initial matrix check failed because it compared unsimplified exact complex
expressions by structural Matrix equality. The only mathematical-test repair
was to simplify each matrix difference entry before that comparison. The
initial source and complete failure log remain in E, with the repair recorded
in E/diagnostic_repair_log.json; no formula was changed to achieve agreement.
Source-copy tampering and a matching manifest rebind are both rejected by the
explicit pinned-source checks. These are provenance controls, not evidence
for the analytic remainder. The checks ran in Python 3.13.5 with SymPy 1.14.0.
They do not verify the all-order estimate, Sobolev density passage or physical
identification; those remain the ordinary proof obligations addressed above.

The exact source/proof identities, failures, diagnostics and final freeze are
kept in the owned evidence directory. The selected model and effort were not
changed. Separate reasoning with shared parent sources is same-family
corroboration; it does not establish formal verification or model diversity.
No transitive re-audit of the parent spin construction, retention decision,
canonical edit, Git operation, publication, editable prompt change or message
to another chat occurred. The supervisor owns the subsequent source-bound
review and any broader composition. The remaining review target is the exact
finite-regularity remainder argument (14)-(18), together with the matching of
the supplied cell/frame conventions to (4), not an intentionally assumed new
continuum lemma.

## 9. No-Go Discipline Gate: narrow scope controls only

This note's principal result is positive. The nonlocality example (29) and
the diagnostic failures only narrow specific stronger inferences; they are
not a universal no-go or a complete negative packet.

- **N1:** The tested failed shortcuts are dropping the density, reversing the
  cell/frame conventions, omitting transport and dropping vacuum contractions.
  They are defects in this specified formula, not five independent excluded
  routes to a physical theory. No five-route packet PASS is claimed.
- **N2:** No list or count of independent physical walls is asserted. Fixed
  data, positive m,v, sufficient regularity and the supplied coordinate choices
  are theorem hypotheses. No necessity or independence of those hypotheses
  is proved.
- **N3:** The completed proof was reread with those hypotheses, the unital
  Fock extension, real fields, formal adjoint symmetry and finite complexity
  explicit. The phrase scan and its context are retained in E. Its mention of
  a canonical edit concerns an action not taken, not a mathematical premise.
- **N4:** No prior no-go is used as a witness. The locality example computes
  the exact exterior tail of this T_2 on a nonnegative compact input. The
  varying-input example (30) uses the exact output band at zeroth order; it
  makes no necessity claim for the higher weighted Sobolev hypotheses. Neither
  imports an obstruction from a different norm or refinement.
- **N5:** The analytic claim covers coefficient L2 norms and fixed polynomial
  operator norms on full low Fock space. The symbolic checks cover scalar
  coefficient jets and finite CAR matrices. No per-site coupling derivation,
  extensive lattice theorem or formal N5 scientific execution certificate is
  claimed.
- **N6:** Changing the cell origin or frame, imposing weighted-moment
  cancellations, using special cancelling polynomials, or asking for decay
  instead of exact support are live mathematical variants. They need no new
  physical axiom to be considered and are not ruled out here.
- **N7:** The strongest challenge to a broad locality conclusion is a
  particular polynomial whose T_2 contributions cancel, or a test input with
  both exponential moments zero. Equation (29) leaves these possibilities
  open. The proved assertion is the explicit coefficient counterexample,
  not that every interaction correction is nonlocal.
- **N8:** Broad campaign, queue and earlier-cycle searches are outside this
  restricted independent assignment and were not performed. There is no
  novelty, route-exhaustion or complete no-go-packet readiness claim. N1,
  formal N5 and broad N8 packet coverage remain uncompleted.

## Later source binding and current publication scope

The complete 496-line comparison is fixed at
`47d94f2b67f97b1180d2b32a1445d2afda9b3ce8322ec5a278c47d486d872160`.
Its addendum preserves the actual arcsine band and zero extension used for
the coefficient map, the strict R > -K tail-cutoff condition, the
subnormalized-corner convention, common-observable qualification, and the
root diagnostic's execution after the original root seal. Its historical
kinetic-review reservation is not edited retrospectively.

Exact ordinary acceptances are `EFFECTIVE_POTENTIAL_ROOT_READ_ACCEPTANCE.json`
(`7668fdb282a1b4063b73bf9d300b81df37d6aa830ed153127a1714ffcaef91ee`)
and `EFFECTIVE_POTENTIAL_COMPARISON_ROOT_ACCEPTANCE.json`
(`85d4a9cc39efa47700e06034c0e76eca96c1fbe6c736b2ccdb5df3ac6c06c6a3`).
They accept the supplied-model analytic result and the stated conditional
comparison, not a transitive audit or a formal analytic certificate.

| Direct source | Role and boundary |
|---|---|
| [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md), `763082a6…` | Exact symbols, cells, low/high branches and frame; canonical `open_gate` is unchanged. |
| [Local](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md), `b5a8394a…` | Literal real CAR field normalization, covariance, Fock representation and even-spin interpretation. |
| Smooth-high independent, `c69d638e…` | Archived provisional high-tail and exact graded compression support. |
| Smooth-high comparison, `1a10d9c6…` | Archived source-exposed clarification of unital extensions, support and formal selfadjointness. |

Only the first two rows have canonical direct dependency edges. The last
two remain explicitly archived support rather than invented claim nodes.
The corrected kinetic theorem is a separate compositional resource; this
potential theorem does not depend on it or on the publication parent PR9510.

For the full-low norm remainder at potential order N, the later comparison
uses the same selfadjoint kinetic operator in both generators. Bounded
Duhamel then adds at most 2 T_c C_N c^(N+1) to a normalized-density comparison.
This is a separate finite-resource cost; it must vanish, or satisfy the
desired rate, on the chosen time window. It supplies no kinetic graph domain,
energy-readout bound, causal support or fixed uncorrected continuum target.
No uniformity as N grows is asserted.

The archived finite diagnostics preserve their actual scope and failures:
third-order scalar coefficients, explicit covariance checks and literal
finite Pauli compression at the reported degrees. The first unsimplified
matrix assertion failed; its source and traceback precede the repaired
successful records. These controls do not prove the all-order analytic
remainder and were not rerun in this assembly.

The publication packet is
`.claude/science/physics-loops/toe-corrected-dynamics-20261013`.
Its [source recovery and scope](../.claude/science/physics-loops/toe-corrected-dynamics-20261013/SOURCE_RECOVERY.md)
binds the accepted source freeze, exact comparisons and root records.
The [identity-only runner](../scripts/explicit_effective_potential_identity_2026_10_13.py) checks source bytes and
reconstruction only; it proves no coefficient, domain, commutator or
dynamical estimate. It has not been executed during publication preparation.
Root accepted the exact source assembly; the new publication wrappers,
tools and driver require separate review and actual execution receipts.
Original pending/false fields remain historical and unchanged. Current
stays `open_gate`; N1/N5 and broader no-go obligations remain pending.
No formal analytic, model-diverse, audit or retained status is conferred.
