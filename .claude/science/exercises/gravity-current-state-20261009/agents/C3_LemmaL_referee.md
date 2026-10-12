# Lemma L (massive-matter exercise): referee report (codex gpt-5.6-sol, xhigh; 2026-10-10)

# Independent referee: C3 Lemma L

## VERDICT: CONFIRMED WITH CORRECTIONS

The exact positive-ladder identity is correct for the intended deterministic,
strictly causal hop kernel, subject to the usual finite-volume/integrability
limit.  The statement as written is too broad: pair-determinism alone does not
imply strict causality, translation/Lorentz invariance, a nonzero light-cone
normalization, or excitation by nonzero end data.  Those extra hypotheses are
needed for the no-repeated-point proof and for the exponential conclusion.
Also, the positive end factors need not be uniformly \(O(1)\), so Lemma L does
not validate the M-A packet prefactor used by S0.

## Findings

### 1. Exact ladder: correct with explicit hypotheses

Let the Poisson intensity measure be diffuse, let \(b\in\mathbb R\), and assume
\(h(x,z)=0\) unless \(z\prec x\), with \(h(x,x)=0\).  Work first in a bounded
causal region, where the Neumann/path expansion is finite, and then take any
limit in which the amplitude is in \(L^2\).  Expanding the two replicas and
classifying a pair of paths by all their common Poisson vertices gives an exact
identity.

The zero-common-vertex class is exactly
\(\mathbb EF\,\overline{\mathbb EF}\), because the factorial moment measure of
a diffuse Poisson process is a product measure and collision diagonals have
measure zero.  It therefore cancels from the covariance.  If the common
vertices are \(z_1\prec\cdots\prec z_r\), strict causality makes their order the
same in both paths.  Applying multivariate Mecke to the private vertices in
each intervening stretch gives the product of the two one-replica mean
kernels.  Thus each internal rung is

\[
Q(x,z)=\rho |b|^2 |G_m(x,z)|^2,
\]

and the two ends are modulus squares of the corresponding mean propagated
source and detector fields.  For the real kernels used here this reduces to
the claimed \(\rho b^2G_m^2\).  Hence every contraction term is nonnegative.

The two stretches do **not** have to be probabilistically independent in the
same interval.  Their required factorization follows from the Poisson
factorial moment measure after all common labels have been extracted.  This is
the missing justification in the proof sketch at
`C3_exercise_M_massive_matter.md:177-180`.

There are no repeated-point paths under the strict causal-support assumption:
\(x_0\succ x_1\succ\cdots\) cannot return to an earlier vertex.  Without that
assumption, matrix powers can contain cycles or diagonal revisits and this
proof, and therefore the lemma as worded merely for a “fixed function of the
two events,” fails.

This also explains exactly why the M-A obstruction disappears here.  Link
weights depend on interval emptiness, whereas a deterministic pair hop does
not.  The unevaluated \(E_2\) and signed pair-path sectors identified in
`C3_M-A_report.md:109-128` and `C3_M-A_referee.md:17-19,42-49` are absorbed into
\(|G_m|^2\) by the deterministic-hop Mecke calculation.  Lemma L does not apply
back to Johnston links.

### 2. Rungs and ends are nonnegative, not necessarily strictly positive or \(O(1)\)

For real \(b\), each rung is nonnegative.  For complex kernels the statement
must use \(|G_m|^2\), not \(G_m^2\).  The end functions are likewise modulus
squares and may vanish for unexcited or disjoint data.  Their positivity does
not bound their size after division by \(|\mathbb EF|^2\).

That distinction is load-bearing for S0.  M-A's missing transition-overlap/end
normalization can be very large, and its scan was not a bound
(`C3_M-A_referee.md:21-40,49`).  The S0 preregistration explicitly imports the
M-A form with \(C=1\) and \(P_{\rm tr}=1\)
(`work_S0/PREREG.md:16-17,29-30`).  Lemma L proves the sign of the exact ends;
it does not prove that imported numerical prefactor.

### 3. Exponential growth: correct for the intended homogeneous smeared class, not “always”

Pair-determinism by itself does not imply a \(1/\kappa^2\) singularity.  For
example, it permits the zero kernel, nonstationary kernels, kernels with no
long-time support, and zero end data.  The universal wording at
`C3_exercise_M_massive_matter.md:180` is therefore false.

For the intended four-dimensional, translation- and Lorentz-invariant
light-cone smear, however, the conclusion follows.  Write \(s=t^2-r^2\), take
a localized profile \(F(s)\) with \(I_0=\int F(s)ds\ne0\), and normalize the
massless mean hop as \(F(s)/(2\pi I_0)\).  At large \(t\),

\[
\int d^3x\,|G_m(t,\mathbf x)|^2
=t\left[J_F+O(m^2)\right]+o(t),\qquad
J_F=\frac{\int F^2ds}{2\pi(\int Fds)^2}.
\]

If the profile has width \(S=\ell_k^2\), then \(J_F=O(S^{-1})\), so the relative
coefficient correction is \(O(m^2\ell_k^2)\).  Consequently the zero-spatial-
momentum rung transform is

\[
\widetilde Q(\kappa)=
\frac{m^4\ell^4J_F}{\kappa^2}
\left[1+O(m^2\ell_k^2)\right]+\hbox{less singular terms}.
\]

The positive renewal resolvent then has a positive pole, for nonzero ends, at

\[
\kappa=m^2\ell^2\sqrt{J_F}
\left[1+O(m^2\ell_k^2)\right].
\]

This confirms the leading formula in its stated small-\(m\ell_k\) regime.  It
does not establish a uniform error bound out to \(m\ell_k=0.3\); the proposed
quadrature check remains listed as future work at
`C3_exercise_M_massive_matter.md:188-191`.

### 4. Coefficient checks

For the box \(F=1\) on \([0,S]\),

\[
J_F=\frac1{2\pi S},\qquad
\kappa_F=\frac{m^2\ell^2}{\sqrt{2\pi}\,\ell_k}.
\]

The advertised coefficient check is an exact algebraic identity,

\[
k_0\,6^{1/4}=(2\pi\sqrt6)^{-1/2}6^{1/4}
=1/\sqrt{2\pi}=0.3989422804,
\]

and the stored run reports it correctly at
`work_S0/out/s0_signed_hop_price.out:5`.

The \(m^3\ell^2/4\) result is also consistent with the exact ladder, but it is
**not** a reproduction by the four-dimensional \(J_F\) formula.  In the 2D
causal-matrix model,
\(G_m=\tfrac12J_0(m\sqrt{t^2-x^2})\), and

\[
\int_{-t}^{t}|G_m|^2dx\longrightarrow\frac1{4m}.
\]

Thus \(\widetilde Q(\kappa)\sim m^3\ell^2/(4\kappa)\), whose renewal pole is
\(\kappa=m^3\ell^2/4\).  This is the separate dimension-specific controlled
asymptotic described at `E1p_referee.md:143-147`; it corroborates the ladder
mechanism, not the 4D \(J_F\) coefficient.

### 5. S0 and the post-hoc Z2 lead

The preregistered S0 verdict is correctly **FAIL**.  For Z at the 25 kDa,
10 ms bar, the exact-moment rerun gives
\(\ell_k\ge3.379\times10^{-26}\) m from noise but
\(\ell_k\le3.653\times10^{-27}\) m from mean stability, an empty window of
width 0.108 (`work_S0/out/s0c_exact_moments.out:7-12`).  This agrees with the
announced fixed-reading result at
`C3_exercise_M_massive_matter.md:167-169`.

The corrected Z2 arithmetic is also reproducible: exact rational moments give
\(\sqrt{J_F}=1.197\), first nonzero normalized moment
\(\langle u^3\rangle=1/20\), and a molecular window
\([5.068\times10^{-26},1.004\times10^{-24}]\) m, a factor 19.8
(`work_S0/out/s0c_exact_moments.out:13-18`).  The original Z2 row and the
\(n\ge2\) rows of the first post-hoc script are invalid floating-point results,
as recorded at `C3_exercise_M_massive_matter.md:171-173,197-198`.

Z2 is therefore a legitimate **post-hoc numerical lead**, not a changed S0
verdict and not yet a model result.  Besides the conditional \(\kappa_F\)
asymptotic, it relies on (i) the unproved imported M-A packet prefactor and
(ii) the \(j=3\) and higher mean-pole series used in
`work_S0/scripts/s0c_exact_moments.py:29-30`, whereas the preregistered source
states only the \(j=1,2\) terms (`work_S0/PREREG.md:15`).

## Strongest correct statement

For a diffuse Poisson process and a deterministic, square-integrable,
strictly causal pair kernel with real \(b\), the covariance of the causal
path-resolvent amplitude has an exact Mecke expansion over common vertices.
After the zero-common-vertex term cancels \(|\mathbb EF|^2\), every remaining
term is a nonnegative ladder term with rung
\(\rho b^2|G_m|^2\) and nonnegative modulus-square ends.  Hence there are no
Johnston-type emptiness overlaps or signed inter-ladder terms in this class.

For a nontrivial homogeneous Lorentz-invariant 4D light-cone profile of width
\(\ell_k\), nonzero normalization, nonzero ends, and \(m\ell_k\ll1\), this
ladder has leading growth rate
\(m^2\ell^2\sqrt{J_F}[1+O(m^2\ell_k^2)]\).  The box coefficient is exactly
\(1/\sqrt{2\pi}=0.398942\).  The 2D rate \(m^3\ell^2/4\) follows separately
from the 2D rung asymptotic.  None of these facts fixes S0's packet end
prefactor; therefore S0 remains a conditional FAIL for Z, while exact-moment
Z2 is only a post-hoc candidate for a separately preregistered test.
