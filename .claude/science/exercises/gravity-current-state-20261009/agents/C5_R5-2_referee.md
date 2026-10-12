# VERDICT: CONFIRMED WITH CORRECTIONS

The campaign reading **INCONCLUSIVE** is correct.  The Mellin transform and the
one-dimensional Hecke obstruction for the unweighted retarded sum survive
adversarial checking, and the supplied numerical outputs reproduce.  The main
corrections are scope corrections: Proposition 1 is an ensemble-
\(L^2\), shell-constant, rapidly decaying-kernel result and needs separate
threshold and exceptional-mode clauses; the 3+1 samples are small universal-
cover balls, not Haar samples and not lower bounds for the quotient rms; a
64-point trapezoidal rule is not literally the exact Haar integral; and
section 4.2 is a conditional fixed-profile Mellin asymptotic, not a proof that
every fixed smooth or flat-at-zero law fails.

## 1. Proposition 1

### Mellin transform and poles

**Confirmed.**  For \(\Re s>1/2\), absolute convergence justifies interchanging
the \(\beta\)- and \(d\)-integrals.  After the \(\beta\)-integral gives
\(\Gamma(s)(\cosh 2d)^{-s}\), the identity

\[
\sinh d\,\sin rd=\frac{\cos((r-i)d)-\cos((r+i)d)}{2i}
\]

and the standard cosine transform of \(\cosh^{-s}\) give exactly the displayed
formula (`R5-2_report.md:70-75`).  A high-precision direct integration route,
independent of the worker's nested \(\beta\)-quadrature, agrees at
\(2.4\times10^{-71}\) or better (`referee_runs/r52_referee_checks.py:39-55`;
`referee_runs/r52_referee_checks.out:1-3`).

For real \(r\ne0\), the poles are simple and occur at
\(s=1/2\pm ir/2-k\), \(k\ge0\).  Even and odd \(k\) alternate between the two
Gamma products, and the remaining Gamma factor is finite and nonzero.  The
independent residues through \(k=3\) are all nonzero
(`referee_runs/r52_referee_checks.out:5-13`).  Thus the pole statement at
`R5-2_report.md:76` is correct for real nonzero \(r\).

At \(r=0\), the two simple-pole strings coalesce.  Taking the analytic
\(r\to0\) limit gives

\[
\widetilde H_0(s)=\pi 2^{s-3}
 \Gamma(s/2+1/4)\Gamma(s/2-1/4)
 \bigl[\psi(s/2+1/4)-\psi(s/2-1/4)\bigr],
\]

which has double poles at \(s=1/2-k\).  Numerically,
\((s-s_0)^2\widetilde H_0(s)\) tends to a nonzero limit for \(k=0,1,2\)
(`referee_runs/r52_referee_checks.py:26-36,70-79`;
`referee_runs/r52_referee_checks.out:15-18`).  This correctly implements the
R4-1 referee's \(\ell\log\ell\) correction
(`C5_R4-1_referee.md:82-90`).

### Necessity, sufficiency, and uniformity

**Confirmed with corrections.**  Under the spectral expansion already
confirmed for R4-1 (`C5_R4-1_referee.md:56-67`), the following is the precise
statement for a real shell-constant weight \(f_m=O(m^{-A})\), \(A>5\), on the
fixed-peak Gaussian family:

- For every tempered mode \(r_j>0\), Palm/Haar
  \(\|\Delta_\ell\|_2=O(\ell^{-4})\) holds exactly when
  \(D_j(1/2+ir_j/2-k)=0\) for \(k=0,1,2\); the conjugate points then vanish
  automatically.
- For each threshold mode \(r_j=0\), both
  \(D_j(1/2-k)=0\) and \(D'_j(1/2-k)=0\) are required for
  \(k=0,1,2\).
- For each exceptional mode \(r_j=i\tau_j\), \(0<\tau_j<1\), both distinct
  real values \(D_j(1/2+\tau_j/2-k)\) and
  \(D_j(1/2-\tau_j/2-k)\) must vanish for \(k=0,1,2\).

The \(k=1,2\) necessity is sound.  Once the preceding powers have been
removed, multiplication by \(\ell\) and then \(\ell^3\) leaves a nonconstant
sinusoid in \(\log\ell\); an \(O(\ell^{-4})\) coefficient cannot contain it.
At threshold, cancelling a double-pole residue requires a double zero of
\(D_j\), hence \(D_j=D'_j=0\), not merely the first R4-1 coefficient
(`R5-2_report.md:88-95`).

The convergence argument is valid but omits one arithmetic bound that should
be stated: the L7 shell mass gives
\(|\Psi_j(m)|\ll\|\psi_j\|_\infty C_m m\), and the local-density formula gives
\(C_m=O_\delta(m^\delta)\).  Hence the Dirichlet series and its derivative are
absolutely and locally uniformly convergent throughout the strip used in the
shift.  This is what licenses the sum/integral interchange; \(A>5\) is more
than sufficient.

For the high tempered spectrum, Stirling gives exponential \(r_j\)-decay,
while \(\|\psi_j\|_\infty\ll r_j\) and Weyl's law supply a summable polynomial
factor, so the mode sum is uniform.  Threshold and exceptional modes are
finite and must be handled separately.  In particular, if
\(\tau_{\max}\) is the largest exceptional parameter, the shifted line must
satisfy
\(-5/2+\tau_{\max}/2<\Re s<-2\); otherwise the growing branch of the
\(k=3\) exceptional pole is crossed.  Such a line exists because
\(\tau_{\max}<1\), and its remainder is still \(o(\ell^{-4})\).  Therefore the
equivalence survives, but the uniform remainder as written at
`R5-2_report.md:88-93` is incomplete for exceptional modes.

Finally, this is not an exact reduction for arbitrary orbit-dependent weights:
those are explicitly outside the report's proved class
(`R5-2_report.md:195-199`).  Nor is it pointwise for every realization; it is
the Palm/Haar quotient norm inherited from R4-1.  The headline and strongest
statement (`R5-2_report.md:34,57`) need those qualifications.

## 2. Full-lattice Poisson claim

**Confirmed, with the symbol written more precisely.**  For
\(h_{\ell,u}(x)=P(Q(x))e^{-|x|_{E,u}^2/(2\ell^2)}\), Poisson summation gives a
zero-dual-vector continuum term independent of \(u\), while every nonzero
dual vector is a polynomial in \(\ell\) times a Gaussian.  Compactness of
\(\Gamma_L\backslash H^3\) supplies a uniform positive dual minimum after
choosing quotient representatives.  Thus the quotient-wide frame dependence
is exponentially small, not merely small on the sampled patch
(`R5-2_report.md:110-112`).

The complete distributional multiplier is a reciprocal-lattice comb,

\[
\widehat K(k)=\frac{(2\pi)^4}{\operatorname{covol}(L_7)}
 P(-\Box_k)\sum_{G\in L_7^*}\delta(k-G),
\]

up to the Fourier convention.  Near the central Brillouin point this is the
reported \(P(-\Box_k)\delta(k)\), not the regular multiplier \(-k^2\).
Consequently these nonretarded polynomial weights compute global moments and
do not construct a d'Alembertian (`R5-2_report.md:113-114`).  The numerical
flatness reproduces, but is only an illustration; the \(\ell=9\) full-lattice
entry is visibly at the truncation reach (`scripts/r52_A_R77.out:35-42`).

## 3. The 1+1 Hecke step

**Confirmed, including the functional-equation move.**

1. If \(7\nmid m\) and \(|Q(n)|=m\) is represented, then
   \(Q(n)\equiv n_1^2\pmod7\).  Since \((-1/7)=-1\), its sign is positive for
   \((m/7)=+1\) and negative for \((m/7)=-1\).  This is the correct timelike
   criterion (`R5-2_report.md:124`; `scripts/r52_D_1plus1_analog.py:15-24`).
2. \(\mathcal O_{\mathbb Q(\sqrt7)}=\mathbb Z[\sqrt7]\), its ordinary class
   number is one, and the negative Pell equation is impossible modulo 7, so
   every unit has norm \(+1\).  Therefore
   \(\sigma((\alpha))=\operatorname{sgn}(N\alpha)\) is well-defined on ideals.
   Its archimedean character is
   \(\operatorname{sgn}(\alpha)\operatorname{sgn}(\alpha')\): it is indeed odd
   at both real places.  Off 7 it equals \((N\mathfrak a/7)\), by the same
   represented-norm sign test.  Thus the selector
   \((1-\sigma)/2\) and the difference
   \([L(s,\chi_k)-L(s,\chi_k\sigma)]/2\) are correct
   (`R5-2_report.md:125`).
3. With \(\chi_k(\mathfrak a)=|\alpha/\alpha'|^{i\nu_k}\), the unshifted
   completion has
   \(\Gamma_{\mathbb R}(s+i\nu_k)\Gamma_{\mathbb R}(s-i\nu_k)\), matching the
   Mellin transform of \(K_{i\nu_k}\).  Twisting by \(\sigma\) changes both
   factors to
   \(\Gamma_{\mathbb R}(s+1+i\nu_k)\Gamma_{\mathbb R}(s+1-i\nu_k)\).
   The shift in `R5-2_report.md:126-128` is therefore right.
4. The report does **not** incorrectly invoke an Euler-product theorem directly
   at \(\Re s=0\).  At \(s=i\nu_k\), all shifted completion factors are finite
   and nonzero, so the functional equation transfers vanishing exactly to
   \(L(1-i\nu_k,\overline{\chi_k\sigma})\).  The standard boundary
   nonvanishing theorem for unitary Hecke L-functions on \(\Re s=1\) then gives
   \(L(i\nu_k,\chi_k\sigma)\ne0\).  Hence the residue
   \(\Gamma(i\nu_k)L(i\nu_k,\chi_k\sigma)\) is nonzero for every \(k\ne0\), as
   claimed (`R5-2_report.md:129-130`).  This is the essential use of the
   functional equation, not an optional gloss; compare the general
   [Jacquet--Shalika nonvanishing theorem](https://doi.org/10.1007/BF01390166).

One numerical label must change: 64 equally spaced rapidities are a
trapezoidal approximation to the Haar integral, not the “exact Haar average”
(`scripts/r52_D_1plus1_analog.py:28-30`; `R5-2_report.md:132`).  It is an
excellent approximation here: independent 32-, 64-, and 128-point grids agree
to displayed precision for \(\ell=4,8,11\)
(`referee_runs/r52_referee_checks.out:33-36`).  This wording correction does
not affect the analytic Hecke result.

## 4. The 3+1 numerics and sampling

**Reproduced, but their evidentiary scope is narrower than the prose.**  The
supplied R77 NPZ was loaded with `allow_pickle=False`; every printed standard
deviation and the T0/Tfin ratios reproduce
(`referee_runs/r52_referee_checks.py:82-91`;
`referee_runs/r52_referee_checks.out:20-26`).  The reach assertion is a
conservative seven-width cutoff (`scripts/r52_A_cone_sums.py:13-15`), and the
full-lattice row is a useful truncation diagnostic.

However, the 12 frames occupy only \(0\le\eta\le0.1941\), one of them is
forcibly replaced by \(\eta=0\), and no quotient fundamental domain or
equidistribution map is used (`scripts/r52_A_cone_sums.py:25-33`;
`referee_runs/r52_referee_checks.out:20-21`).  Exactly as in the R4-1 referee
correction (`C5_R4-1_referee.md:44-48`), this is a small hyperbolic ball in the
universal cover.  Its standard deviation is neither a Haar-rms estimate nor a
proved lower proxy for one.  The data establish local frame dependence over
\(4\le\ell\le9\), with T0/Tfin ratios 0.148--0.538 through \(\ell=8\); they do
not establish an asymptotic exponent or the proposed 3+1 theta-lift mechanism
(`R5-2_report.md:138-151`).  T0 and T1 are also neither decaying weights nor
mean-\(\Box\) kernels, as the report correctly concedes at
`R5-2_report.md:151`.

The smooth-family rerun is bit-for-bit consistent with the supplied output,
including slopes +3.66, +4.01, and +3.85
(`scripts/r52_C_infinite_smooth_recheck.out:1-33`).  It uses the same
40-frame, \(\eta\le1\) R4-1 ball, so it is local finite-window evidence, not a
Haar or asymptotic verification.  The code also solves the moment equations
only through \(m=200\) and evaluates realization sums only through \(m=160\),
with small numerical tail estimates (`scripts/r52_C_infinite_smooth_recheck.py:8-27`).
Thus “these sampled kernels show growing local deviations” is checked;
“smooth decaying infinite kernels still drift like \(\ell^3\)” is not a
class theorem and is not numerically established as an asymptotic law
(`R5-2_report.md:157-168,208-212`).

## 5. Section 4.2 prefactors

**The formal Mellin scaling is correct only under the stated analytic and an
additional fixed-profile hypothesis; the concluding no-PASS sentence is too
strong.**  With a profile \(\widehat F\) independent of \(\Lambda\), Mellin
inversion does give

\[
D_j(s_0)=\frac1{2\pi i}\int \widetilde F(w)
 \Lambda^{w-3}L_j^T(s_0+w)\,dw.
\]

If \(L_j^T\) is holomorphic across the shift and has adequate vertical growth,
the pole of \(\widetilde F\) at \(w=0\) gives the
\(\Lambda^{-3}\widehat F(0)L_j^T(s_0)\) term; a profile flat at zero has an
entire Mellin transform and permits superalgebraic shifts if \(L_j^T\) is
entire (`R5-2_report.md:170-176`).  The conversion
\(\Lambda^{-3}=L^{-6}\) is also correct.

Those premises are not established for the 3+1 positive-index series, and the
profiles fitted in section 4.1 depend on \(L\) because the discrete moment
system is re-solved at every scale.  Indeed the inferred values
\(\Lambda^3c_0=53.15,32.13,24.17\) are not yet a fixed rescaled profile
(`referee_runs/r52_referee_checks.out:28-31`).  More importantly,
“\(D_j(s_0)\ne0\) generically” cannot imply that **no** fixed law of the class
meets PASS; exceptional or engineered profiles are exactly the open problem.
Only the 1+1 unweighted family has the proved nonzero L-value.  Therefore
`R5-2_report.md:175-177` must remain a suggested generic asymptotic, with the
sentence “no fixed law of this type meets PASS” deleted or restricted to a
profile for which a nonzero mode coefficient has separately been proved.

## 6. Reading, labels, and no-go discipline

**INCONCLUSIVE is confirmed** against the immutable readings
(`TESTS.md:2877-2884`).  No explicit retarded infinite-orbit kernel meeting the
mean and realization-rms requirements was constructed, so PASS is unavailable.
No argument covers every infinite-orbit kernel with a convergent forward-tube
symbol, so FAIL is unavailable.

The universal negative route also fails the no-go stress test: R4-1 proves
only finite support (`C5_R4-1_referee.md:140-149`); orbit-dependent weights,
non-smooth/Hecke-adapted sequences, slower-decay sequences requiring analytic
continuation, and exact infinite spectral synthesis remain unclosed
(`R5-2_report.md:195-201`).  The strongest steelman is precisely an
infinite-dimensional weight sequence engineered to satisfy the countably many
mode conditions while retaining the four mean moments.  Nothing in the packet
constructs it, but nothing excludes it.  No “new axiom” conclusion follows;
the supplied axioms explicitly leave downstream dynamics and physical
operators to separate derivation (`MINIMAL_AXIOMS_2026-06-29.md:85-95,114-130`).

The explicit N1--N8 disposition is **FAIL for a universal no-go**:

- **N1:** at least five materially distinct counter-routes remain relevant:
  direct infinite shell-sequence spectral synthesis (**UNTESTED**); a
  Hecke-operator annihilator (**ATTEMPTED only in the non-target 1+1
  diagnostic**); a positive-index theta-lift construction with no relevant
  automorphic components (**UNTESTED/SUGGESTED**); weights resolved
  orbit-by-orbit within each shell (**UNTESTED**); and slower-decay tube
  kernels whose Dirichlet series closes only after analytic continuation
  (**UNTESTED**).  Thus the required attempted-or-prior-ruled-out route packet
  is absent, independently of the underlying mathematics.
- **N2:** there is no justified independent-wall count.  The mean moments,
  three pole cancellations, continuation, and orbit freedom can constrain one
  another.
- **N3:** the hidden scope conditions are shell constancy, \(A>5\), scalar
  linearity, fixed kernel, retardation, the Gaussian test family, Palm/Haar rms,
  and the automorphic expansion; all must remain explicit.
- **N4:** the R4-1 witness residual is finite support and therefore does not
  match the present infinite-support residual.
- **N5:** the proved statements are modewise/ensemble or 1+1; the 3+1 checks
  are local-ball samples.  None is a lattice-wide pointwise statement for
  every realization.
- **N6:** this is a mathematical kernel-construction problem, not evidence that
  a new axiom is required.
- **N7:** the infinite-dimensional exact-synthesis steelman is admissible and
  unclosed.
- **N8:** R4-3's flat-at-zero mesoscale mechanism was not retired; R5-2 makes
  its conditional prefactor estimate sharper but does not prove the required
  coefficient is nonzero or zero.

Recommended label corrections are:

- retain **proved** for the Mellin formula and full-lattice Poisson statement,
  with the reciprocal-comb qualification;
- retain **proved mod recalled Hecke theory** for the 1+1 \(f\equiv1\)
  obstruction;
- label both 3+1 studies **checked on sampled local frame balls**, not Haar or
  asymptotic;
- retain **suggested/conditional** for the theta-lift mechanism and all of
  section 4.2;
- replace broad “retardation destroys the cancellation” and “no fixed law”
  language by the exact subfamilies actually covered.

## Strongest correct statement

For real shell-constant weights \(f_m=O(m^{-A})\), \(A>5\), in the fixed linear retarded scalar L7 model and on fixed-peak observer-frame Gaussians at a Palm point, the confirmed automorphic expansion implies that the Haar-rms relative error is \(O((a/\ell)^2)\) exactly when every tempered mode has \(D_j(1/2+ir_j/2-k)=0\) for \(k=0,1,2\), every threshold mode has double zeros \(D_j=D'_j=0\) at \(1/2-k\), and every exceptional mode has both real-branch zeros at \(1/2\pm\tau_j/2-k\); the four independent mean conditions must also hold.  Nonzero finite-orbit kernels cannot satisfy even the leading conditions, the 1+1 unweighted retarded family fails every nonconstant mode by the correctly shifted odd narrow-class character and Hecke functional equation, and the supplied 3+1 smooth and scale-free families show substantial local finite-window frame dependence.  But orbit-dependent and engineered infinite sequences remain open, the 3+1 samples are not Haar/asymptotic proofs, and section 4.2 does not exclude exceptional profiles; therefore neither fixed PASS nor fixed FAIL is met and the campaign reading remains **INCONCLUSIVE**.
