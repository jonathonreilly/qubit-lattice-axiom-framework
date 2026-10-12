# VERDICT: CONFIRMED WITH CORRECTIONS

The bounded F2 obstruction is correct for the fixed K2 nearest-neighbour scalar, its fixed
$O(\kappa)$ pseudo-translation/stress data, the two fields $h,\phi$, and local
translation-covariant transformation symbols regular at $q=0$.  It is not a theorem about
arbitrary finite extensions of the field content, altered leading matter generators, or
singular/nonlocal transformations.  These qualifications are compatible with the FIXED
reading in `TESTS.md:2247-2252`, but the phrase “finite field content” must be read as the
specified finite content $h,\phi$, not as a quantifier over every possible finite set of
auxiliary or multiband fields.

## 1. Reduction

**Confirmed.**  At order $\kappa^2$, in the coefficient
$\xi h\phi^2$, and for a constant translation parameter $c$, the exhaustive variation
within the stated two-field, parity-even ansatz is

\[
 \delta_0 S_{hh\phi\phi}=0,\qquad
 \delta_2^\phi S_m=E\,B,\qquad
 \delta_2^h S_{FP}=(Kh)^T X,\qquad
 \delta_1^h S_{h\phi\phi}=A^T T,
\]

together with the fixed variation of the $hT$ vertex under $L_c\phi$.  Thus:

- the seagull drops because $D c=0$;
- every local $B(h,\phi)$ term is proportional to one external scalar equation of motion
  and vanishes when both scalar legs are put on the complex shell;
- $K(q)=O(q^2)$, so a finite-range/regular $X(\phi,\phi)$ contributes only at $O(q^2)$;
- the $h^3$ vertex has neither the required matter degree nor a nonzero leading variation
  for constant $c$.

This is exactly the necessary subsystem stated in `F2_report.md:53-76` and assembled in
`f2_jet_system.py:4-18`.  Passing to the complex shell is legitimate: a local off-shell
Noether identity is a Laurent-polynomial/analytic identity and must also hold on its complex
zero variety.  Using a constant parameter is likewise legitimate because a local identity
valid for arbitrary compactly supported $\xi$ has identically zero coefficient and hence
also vanishes after the formal constant specialization.

Restricting $A_c(q)$ to its 1-jet is legitimate.  Every finite-range symbol is analytic at
$q=0$; $X$ begins two orders later in $q$, while an exact solution must make both the
zeroth and first Taylor coefficients vanish.  Field-dependent parameters are included at
the relevant degree: $D\lambda(c,h)\subset A$, and
$D\lambda(c,\phi\phi)\subset X$ (indeed the latter is killed exactly by $KD=0$).

There is no omitted $\delta\phi\sim\phi^2$ rescue of this coefficient.  Acting on $S_m$
it has field degree $\phi^3$, and acting on $hT$ it has degree $h\phi^3$.  A parameter
linear in $\phi$ similarly generates the wrong field degree.  Matter-dependent structure
functions constrain algebra closure, not this necessary action-invariance coefficient; any
local transformation they induce at the relevant field degree is already sorted into
$A,X,B$.  This statement would need revision if one enlarged the class to odd-scalar
vertices, new auxiliary fields, or nonanalytic transformations.  Those are outside the
worker’s declared scope (`F2_report.md:190-202`).

## 2. Rank-5 jet map and range independence

**Confirmed.**  Per matrix entry, a range-$r$ stencil maps coefficients at offsets $o$ to
$(A_0,M_0,\ldots,M_3)$ through the five rows $(1,io_0,\ldots,io_3)$.  For every $r\ge1$,
the offsets $0,e_0,\ldots,e_3$ already give five independent columns, so the map is onto;
for $r=0$ it has rank one.  The worker rerun gives ranks $(1,5,5,5)$ for $r=0,1,2,3$
(`f2_jet_system.out:24-30`), and the independent implementation reproduces them
(`F2_referee_checks.out:12-16`; code at `F2_referee_checks.py:77-85`).

Consequently the first-jet problem is identical for every $r\ge1$.  More strongly, the
proof permits arbitrary constant matrices $A_0,M_\mu$, a superset of the jets allowed by
any symmetry-respecting finite stencil.  Failure in that enlarged jet space proves failure
for every finite range even if a particular placement convention made the physical jet map
smaller.  This is why no separate $r=2,3,\ldots$ search is needed.

## 3. Analytic proof and witness

**Confirmed, and strengthened.**  The (O(\kappa)) identity fixes

\[
T_0(p)=T(p,-p)=n\otimes f,
\]

independently of stress improvements.  For K2, (n=2v, f=v, v=\sin p), hence
(T_0=2v\otimes v), as checked in `f2_general_kinetic.out:1-2` and used in
`F2_report.md:78-82`.

The step (Z) (\Rightarrow A_0=0) is valid.  Here is an independent exact spanning
argument, stronger than the sampled rank check.  If a symmetric quadratic form
(Q(v)) vanished for all shell values, write (c_i=\cos p_i), so
(\sum_i c_i=4+m^2/2) and (v_i^2=1-c_i^2).  At generic (c), the four signs of (v_i)
can be changed independently; this kills every off-diagonal coefficient of (Q).  The
remaining identity (\sum_i d_i(1-c_i^2)=0) on the affine hyperplane
(\sum_i c_i=C) cannot be divisible by its defining linear polynomial without producing
cross terms, unless every (d_i=0).  Therefore the (v\otimes v) span all ten symmetric
components, and (Z) forces (A_0=0).

With (A_0=0), (F) says

\[
X_\mu=M_\mu^T(W\odot v\otimes v)-i\delta_{\mu0}\cos p_0
       (W\odot v\otimes v)=v_\mu\Lambda(p).
\]

Taking (v_1X_0-v_0X_1=0) and its ((2,2)) component gives exactly

\[
\cos p_0\,v_1v_2^2=P(v),
\]

where (P) is a fixed homogeneous cubic.  Thus (\cos p_0) would have to be constant
along every shell ray in (v)-space on which (v_1v_2\ne0).  This validates
`F2_report.md:151-166`.

The supplied random 40-digit witness reran verbatim: its shell residuals remain below
(3\times10^{-40}), with spreads (11.21044068) and (67.02086079)
(`f2_witness.out:1-18`).  An independent closed-form witness removes the report’s
unproved word “generic.”  Put

\[
C=4+m^2/2,\quad a=C/2,\quad s^2=1-a^2,
\]

and take the same sine vector (v=(s,s,s,s)) with the two cosine vectors

\[
(a,a,a,-a),\qquad(-a,a,a,a).
\]

Both obey the shell equation because their cosine sums equal (C), both obey
(\cos^2p_i+\sin^2p_i=1), and they have identical nonzero (v) but opposite
(\cos p_0).  They correspond to genuine complex momenta because
z_i = cos(p_i) + i sin(p_i) is nonzero and has inverse cos(p_i) - i sin(p_i).
For every physical (m^2\ge0), (a\ge2), so (s\ne0).  The independent
check verifies this at (m^2=0,0.25,1,3) (`F2_referee_checks.out:18-22`; construction at
`F2_referee_checks.py:88-116`).  Hence the contradiction holds for every (m^2\ge0), not
only the two masses printed by the worker.

## 4. Controls and Leibniz diagnostic

**Confirmed.**  The requested worker jet system reran with the stored results:

- continuum/local-SLAC-symbol controls: (1.4\times10^{-15}) to
  (3.3\times10^{-15});
- K2 lattice scalar: (0.455) to (0.527) at the massive sample points and (0.494) at
  (m^2=0);
- natural continuum translation: (8.2\times10^{-17}), versus (0.668) on the lattice;
- replacing only (\cos p_c) by one: (1.65\times10^{-15}) and
  (1.76\times10^{-15}).

These are recorded at `f2_jet_system.out:5-22`.  A separate implementation that imports
none of the worker code and eliminates (A_0) analytically finds continuum residuals
(1.5\!-!2.8\times10^{-15}) and lattice residuals (0.403\!-!0.508), with the expected
36/40 rank of the (M)-only system (`F2_referee_checks.out:1-10`).  The sample-dependent
residual is not itself the proof, but it is a clean control for the analytic obstruction.

The full finite-(q) fits are consistent supportive evidence, not needed for the theorem
(`f2_full_system.out:2-22`).  In the A-only systems, the nullities 40 and 360 equal the
dimensions of A = D N with N of ranges zero and one; on-shell stress conservation makes
those directions exact nulls, and the sampled ranks leave no additional numerical nulls.
Two descriptive claims should be weakened:

1. The four-point norm sequence (24.5,266,6.97\times10^3,1.44\times10^5) establishes
   coefficient blow-up, but not a reliable (s^{-2}) law; the script comment itself says
   (1/s) (`f2_coeff_growth.py:1-4`) while the observed effective exponent is not stable
   (`f2_coeff_growth.out:2-5`).  Only unboundedness is relevant.
2. `F2_report.md:48-51` attributes executable input checks to `f2_common.py`, but that file
   defines the symbols and contains no main check/output.  The underlying (KD=0) and
   (O(\kappa)) identities are nevertheless supported by the K2 artifacts and by the
   independent checks above.  This is a reproducibility-label correction, not a physics
   failure.

The continuum success and the “set (\cos p_c=1)” success isolate the failure of the
Leibniz/linear-translation derivative within the fixed jet identity.  “The entire
obstruction” should be understood at that fixed identity and fixed (O(\kappa)) data, not
as a theorem excluding altered leading generators.

## 5. Fixed verdict and scope

**FAIL (bounded) is correct.**  A non-uniform-(\xi) completion must satisfy its constant
translation specialization.  The latter already fails at the first (q)-jet, so assembling
the remaining non-uniform equations cannot rescue it.  The proof uses only the
(h\phi^2\xi) coefficient, so adding higher polynomial orders in the same (h,\phi)
Taylor expansion cannot change this coefficient.  No Ward identity follows, and therefore
F2 supplies no derivation of (\mu_E=\mu_{T2}).

The no-go stress test closes the in-scope alternatives: seagull, (B), (X), arbitrary
finite-range (A), and higher field degree are distinct failed routes; the single
load-bearing wall is the nonconstant (\cos p_c) factor.  The witness attacks that exact
residual.  The strongest steelman routes—altering the leading matter generator, adding
auxiliary/interband fields, or allowing singular/nonlocal symbols—are genuine but outside
the claimed class and must remain open.  Perfect/nonlocal actions are already identified as
escapes in `F2_report.md:198-207`, so no similar retired wall is being suppressed.

**Strongest correct statement:** For K2’s nearest-neighbour scalar on (\mathbb Z^4), with
the displayed (O(\kappa)) pseudo-translation and symmetric stress held fixed (up to local
improvements and on-shell-trivial symmetries), no translation-covariant finite-range—or,
more generally, (C^1) at (q=0)—completion using only (h) and (\phi) can make the
action gauge invariant through (O(\kappa^2)).  The constant-translation
(h\phi^2\xi) coefficient already forces an impossible first-jet identity, for every
finite range and every (m^2\ge0).  This proves the FIXED bounded FAIL for that class, but
does not exclude altered leading matter generators, odd-field interactions outside the
graded ansatz, fermions, auxiliary or multiband finite-field extensions, infinite towers,
or singular/nonlocal/quasi-local completions.
