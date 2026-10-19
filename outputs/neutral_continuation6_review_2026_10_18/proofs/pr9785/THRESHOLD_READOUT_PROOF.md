<!-- Original PR9785 source SHA256 afbe2b96e406ec35a795e2e47bcf6405e11bc0f64280764076bc156013171a5e. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Original-readout threshold measure of the native large feature

Status: bounded-support. This derives a shrinking-energy-window response of
the original microscopic readout, including a large-feature contribution and
the neighboring continuum. The limiting atom is not a proof of an isolated
microscopic eigenvalue at finite lambda. No cosmological scalar or empirical
identification is made.

## Coefficient resolvent from the original source

Use the native host-plus-two-rays coefficient operator `K_4(Q)` and the
variables in `NATIVE_CONSTITUENT_SCATTERING_PROOF.md`. In the normalized even
root basis, the original leading source vector is `f=(-1,b)`, with no
adjustable coefficient. Let `mu_b` be its positive spectral measure and
`m_b(z)=<f,(z-K_4)^-1 f>`. Write

\[
g=g_0,\quad D=(g_x-g_0,g_y-g_0)^T,\quad
G=M-2DD^T/g,\quad A=\sigma^{-1}I-M,\quad q=2D^TA^{-1}D.
\]

The attached rays have self-energy `sigma=(z-sqrt(z²-16))/2`, on the branch
asymptotic to `4/z` at infinity. In particular,
`sigma=(z+sqrt(z²-16))/2` for real `z<-4`. The full root resolvent satisfies

\[
R=(G^{-1}-\sigma I)^{-1}
 =\sigma^{-2}(\sigma^{-1}I-G)^{-1}-\sigma^{-1}I.
\]

A rank-one inverse gives the exact identity

\[
m_b(z)=\sigma^{-2}f^TA^{-1}f-\sigma^{-1}f^Tf
       -\frac{N(z)}{g(z)+q(z)},\quad
N(z)=2\sigma^{-2}(f^TA^{-1}D)^2. \tag{1}
\]

Transposes and analytic squares, not complex absolute squares, belong in
this resolvent identity. It has negative imaginary part in the upper half
plane. The small matrix A is invertible on the shallow-bound scaling domain
for `b<bc` sufficiently close to `bc`.

Let `Eh=-4(1+b)`, `Eb=Eh-delta`, `l=log(1/delta)`, and let `v` be the positive
unit critical root vector. Existing native threshold calculations give

\[
g(E_b)+q(E_b)=0,\quad q(E_b)\sim c l,\quad
A^{-1}D\sim\frac{qv}{2v^TD},\quad c=\frac1{8\pi\sqrt{b_c}}.
\]

The simple small eigenvalue of A is of order `1/l`; variations of M and D
across the delta energy scale are `O(delta l)` and do not compete with it.
Thus, locally uniformly for `z` in the upper half plane,

\[
\frac{N(E_h+\delta z)}{l^2}\to cW_0,\quad
W_0=\frac{c(f^Tv)^2}{2\sigma^2(v^TD)^2}
 =0.025744944098352\ldots,
\]

and `g(Eh+delta z)+q(Eh+delta z) -> c log(-z)`. The logarithm has argument
in `(-pi,0)`. The first two terms of (1) are `O(l)`, so

\[
\boxed{\frac{m_b(E_h+\delta z)}{W_0 l^2}
             \longrightarrow -\frac1{\log(-z)}.} \tag{2}
\]

The normalization agrees with the independently derived bound residue
`W_0 delta l²`. No factor of two from a different scattering-channel
convention is inserted into this source measure.

## Positive-measure limit, including the threshold

Define `nu_delta(B)=mu_b(Eh+delta B)/(W0 delta l²)`. Its Stieltjes transform
is exactly the left side of (2), because the delta from changing the
resolvent denominator cancels the delta in the measure normalization.
The limiting positive measure is

\[
\boxed{d\nu(s)=\delta_{-1}(ds)
        +\mathbf1_{s>0}\frac{ds}{(\log s)^2+\pi^2}.} \tag{3}
\]

The unit atom follows from the residue at `z=-1`. The continuum follows from
`log(-s-i0)=log(s)-i pi` and Stieltjes inversion. There is no threshold atom
at zero. The continuum has infinite total mass but finite Stieltjes weight
at infinity; hence (3) is a local scaling law, not a total spectral-weight
normalization.

Here is a direct convergence argument that does not infer a measure merely
from pointwise real-axis densities. Equation (2) at `z=i` uniformly bounds
`integral (1+s²)^-1 dnu_delta(s)`. For a compact continuous test F, integrate
`-Im m_scaled(x+i eta)/pi` against F. This equals the integral of
`P_eta*F` against `nu_delta`. On a larger fixed compact interval, uniform
continuity of F and the uniform local mass bound control the difference
from F. Outside it, the Poisson tail is at most `C_F eta/(1+s²)`. Thus the
smoothing error tends to zero uniformly in delta. Complex convergence at
fixed eta then proves vague convergence, including intervals containing
zero and the bound atom. The transform in (2) has no extra real constant or
linear term, as is fixed by its decay on the negative axis and at imaginary
infinity. Therefore for every compact continuous F,

\[
\frac{\int F((e-E_h)/\delta)\,d\mu_b(e)}{W_0\delta l^2}
 \to F(-1)+\int_0^\infty\frac{F(s)\,ds}{(\log s)^2+\pi^2}. \tag{4}
\]

This logarithmic shallow-bound scaling is consistent with the prior
constituent scattering result. The new result here is its normalized
original-readout spectral measure and the microscopic transfer below, not
a claim to invent two-dimensional logarithmic scattering.

## Transfer to the actual one-qubit Hamiltonian

Now take the previously specified even cubes `L~lambda^-4`, the allowed COM
mesh approaching the threshold family, and **`delta=lambda^alpha` with
`0<alpha<1/3`**. Use the native local normal form and ground projection
bounds from `MICROSCOPIC_LARGE_FEATURE_WINDOW_PROOF.md`, the source Gram
bounds, and the linear interval-length estimate for each fixed higher
coefficient. The stricter exponent here controls a complete test-function
response rather than only a positive selected window.

For any actual normalized ground vector `g_s`, set
`q_Q=(C_Q-<g_s,C_Q g_s>)g_s`. Its dressed connected original source
is `lambda T f+O(lambda²)` in norm; global ground/remainder errors are
smaller. This statement uses the normalized Fourier readout. Vacuum scalar
terms at this nonzero Q cancel, and fixed-order local source states have
bounded Gram sums. It does not use the extensive global source norm for
this leading-vector estimate.

Let ell be one on the host and the interval length on a ray. In the native
coefficient graph, only bounded nearest-neighbor ray hops change ell, so
`[ell,K_4]` is bounded. Therefore

\[
\|(\ell+1)e^{-isK_4}f\|\le C(1+|s|). \tag{5}
\]

The established local normal-form estimate is
`||(D_j-E_j,vac)psi||<=C_j||(ell+1)psi||` for this compact sector, with the
image allowed to leave it. Apply Duhamel against the known coefficient
propagator, not an assumed closed exact subspace. At physical time
`t=tau/(J lambda delta)`, its normal-form comparison error on f is bounded
by

\[
C\lambda\left(\frac{|\tau|}{\delta}
                  +\frac{\tau^2}{\delta^2}\right), \tag{6}
\]

plus the already smaller global remainder and finite-volume errors.

For an explicit finite-volume justification, restrict the Fourier integral
to `|tau|<=lambda^-1`. The largest physical time is then of order
`lambda^(-2-alpha)`, smaller than L, and the coefficient propagation time
is smaller still. Finite-range propagation and the ground-orbit column
criterion make wrap and background-overlap errors superpolynomial. On the
remaining tail, unitarity bounds both propagators by one. For a smooth
compact F its Fourier transform is Schwartz, so the tail can be made
smaller than any required power even after the normalization below.
Fixed-order dressing tails and the global remainder obey the existing
power bounds in this volume family.

Define the positive microscopic response functional

\[
\mathcal R_\lambda[F]=
\frac{\langle q_Q,
 F\!\left(\frac{H-E_g-8J-J\lambda E_h}{J\lambda\delta}\right)
 q_Q\rangle}
 {\lambda^2 W_0\delta l^2}. \tag{7}
\]

Fourier functional calculus with (6) gives coefficient-vector error
`O_F(lambda/delta²)`. The two physical source factors multiply this by
`lambda²`. The source-vector correction contributes `O_F(lambda³)`.
After the denominator in (7), the leading error is

\[
O_F\left(\frac{\lambda}{\delta^3l^2}
             +\frac{\lambda}{\delta l^2}\right)=o(1)
\]

for the stated alpha range. All estimates are uniform over ground vectors;
mixtures follow by linearity. Thus for every real smooth compact test F,

\[
\boxed{\mathcal R_\lambda[F]\to
 F(-1)+\int_0^\infty\frac{F(s)\,ds}{(\log s)^2+\pi^2}.} \tag{8}
\]

This concerns the actual original ground-state readout, without preparing a
selected bound vector or adding a probe interaction to the Hamiltonian.
It is a correlation/spectral observable, not a physical preparation
protocol. An atom in the scaling limit can be weight in a shrinking exact
spectral window at finite lambda; (8) does not prove a finite-lambda pole.

## Controls and surviving assumptions

The replay checks the finite-root resolvent identity and the broadened
complex response of the full infinite coefficient graph. At `b=.2`, after
normalizing by its actual coefficient bound residue, the imaginary
transform agrees with `-1/log(-z)` at three broadened points to below
`1.4e-9` relative error. The critical asymptotic residue coefficient still
has about a six-percent correction there; that is reported, not hidden by
the residue normalization. These are complex-resolvent controls with a
positive broadening, not direct zero-broadening spectral data or full
microscopic many-body numerics.

The supplied compass Hamiltonian, selected weak regime and momentum path,
physical units, actual ground preparation and connection of the readout to
a measurement remain premises. The excitation center remains near `8J`; vanishing binding does not make
this a massless mode. No scale, Lorentz symmetry, universal
matter coupling, cosmological field, or empirical success is derived here.
All calculations are exposed development; no calibration data or
independent observational tests are used.
