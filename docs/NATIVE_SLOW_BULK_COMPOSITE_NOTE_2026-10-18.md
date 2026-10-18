# Slow bulk composite and its existing-interaction readout

Status: bounded-support. Native finite-order coefficients and an explicitly
projected coefficient-model resonance are distinguished below. No native
infinite-volume pole, cosmological scalar, fermion, gravity bridge or empirical
validation is claimed.

## Target and premises

The question is whether a large feature of one physical qubit per site can
carry a neutral mode and a coupling without appending an interaction. We keep
exactly the supplied directional Hamiltonian

\[
H=-\sum_{x,a}J_a\sigma_x^a\sigma_{x+e_a}^a,
\qquad J_x=J_y=\lambda J_z>0.
\]

The cubic geometry, positive anisotropy, prepared uniform longitudinal state,
and original readout \(C=\sum_x Z_xZ_{x+2e_z}\) are premises, not observations
or derived measurement identifications. All data here are exposed development
calculations. There is no calibration set or independent empirical test.
[The preceding bulk note](NATIVE_BULK_SEGMENT_RESONANCE_NOTE_2026-10-18.md)
derives the four-wall manifold and faster adjacent-column family. Its
transverse curvature had the wrong sign for a simple scalar interpretation.
This block tests another family while retaining its open decay channels.

## 1. Native second-order graph

A configuration in the compact even-plane-parity four-wall manifold consists
of two columns sharing an interval of length ell. Long intervals with axial
separation two have vacuum-subtracted second-order diagonal -4, and each
endpoint moves one layer with coefficient -1/2 in the x orientation and +1/2
in the y orientation, in units Jz lambda^2. The scalar combination

\[
A_\ell=(|2e_x,\ell\rangle+(-1)^\ell|2e_y,\ell\rangle)/\sqrt2
\]

therefore has length hopping -1 at zero longitudinal center momentum.
Long diagonal-separation intervals have diagonal -4 and no such hopping:
the two XY path orders cancel. Other long separations also remain frozen at
this order; they have not been erased from the native Hilbert space.

At ell=2, all nonnearest relative displacements form a two-dimensional host
with hopping -1 and diagonal -4. Remove the origin and four nearest sites,
which belong to different configurations or to the faster first-order block.
The normalized host states are A=(four axial-distance-two sites)/2 and
D=(four diagonal sites)/2. The A channel couples with amplitude -1 to the
long arm ell>=3. This is Pslow K2 Pslow, not an autonomous invariant subspace
of the native Hamiltonian. Its host band [-8,0] contains the arm bottom -6.

The native fourth-order plaquette coefficient gives string tension
sigma=lambda^4 Jz/8 for these axial-distance-two intervals. Thus in slow
energy units Jz lambda^2 the arm has

\[
(H_s u)_n=-u_{n-1}-u_{n+1}+[-4+f_s(n+2)]u_n,
\quad n=\ell-2\ge1,\quad f_s=\lambda^2/8.
\]

The offset n+2 matters: the first long-arm interval is ell=3. A preliminary
n+1 convention was corrected before the final calculations. The graph and
source vertices are checked by physical-bit paths; these are local
coefficient calculations, not diagonalization of a 225-qubit Hilbert space.

## 2. Slow host and conditional resonance

Subtract the host diagonal -4 and write E for the shifted slow energy.
The free relative resolvent is integrated over the square Brillouin zone;
a five-site Schur complement removes the cross-shaped holes. Its outgoing
boundary matrix at E=-2 is approximately

\[
G_s=\begin{pmatrix}
-.3060521439-.2464356213i & .18390671-.19590895i\\
.18390671-.19590895i & -.44518088-.24284087i
\end{pmatrix}.
\]

Set Sigma=G_s,AA and a=Sigma/(1+Sigma)=-.2796521331-.4544316488i.
For fixed Airy index with positive zero magnitude alpha_k,

\[
E_k=-2+\alpha_k f_s^{2/3}+f_s(2+a)+o(f_s).
\]

The length scale is f_s^(-1/3)=2 lambda^(-2/3), level spacing is of order
Jz lambda^(10/3), and full width is

\[
\Gamma/J_z=.1136079122\lambda^4+o(\lambda^4).
\]

These statements initially concern only the specified slow coefficient
model. Direct outgoing root controls at lambda=.3,.2,.1,.05,.025 give
width/lambda^4=.11118858,.11201583,.11291297,.11332026,.11349127.
A narrow pole is embedded in a continuum, not a stable bound state.

## 3. Deriving the readout and restoring the fast channel

The preceding native first-order fast block F has a two-dimensional d-wave
host state d, an adjacent-interval arm beginning at ell=2 with endpoint e,
and coupling -2 between them. Exact native second-order cross vertices are

\[
v_A=Fd/2=-d_2-e,\qquad v_D=-2e.
\]

Here d2 is the axial-distance-two d-wave host state. Direct second-order
vacuum-to-slow readout vanishes: two native edges cannot reach either slow
ell=2 support. The coupling instead comes through the existing fast block,
whose original readout is -sqrt(2) lambda d. No new interaction or independent
scalar-source parameter is introduced.

Let G be the outgoing fast host d resolvent and g the isolated fast arm
endpoint resolvent. Include its native leading confinement
v_n=f_f(n+1), hopping -2, f_f=lambda^3/16. With z=lambda(E-4),

\[
R_{dd}=G/(1-4gG),\quad R_{de}=-2gG/(1-4gG),\quad
R_{ee}=g/(1-4gG).
\]

The induced readout divided by lambda^2 has components

\[
u_A=(1-zR_{dd})/\sqrt2,\qquad
u_D=\sqrt2(1-R_{dd}/G).
\]

In the controlled complex strip described next, u tends to (1,2)/sqrt2.
Convergence is generally logarithmic, not O(lambda). A naive replacement of
the confined arm by its unconfined resolvent is not valid pointwise on the
real axis. Its confinement level spacing is itself of order lambda^4 Jz.
Real-axis pole/zero oscillations cannot be dismissed by an unannounced average.

### Confined-arm strip bound

For z=x-i eta, |x|<=1 and c0 f_f<=eta<=c1 f_f, the self-adjoint arm resolvent
obeys constants 0<c<=|g|<=C independent of small f_f. Here is the proof rather
than an assumed gap. Set u=(z-Harm)^(-1)|1>, u0=-1/2. Its transfer matrix is
T_n=[[(v_n-z)/2,-1],[1,0]]. For the first M=floor(c*/f_f) steps, choose c*
small enough for a uniform ellipticity margin. The real transfer matrix has
bounded eigenbases varying by O(f_f); the imaginary perturbation is O(eta).
All prefix products and inverses are bounded by C exp(C M(f_f+eta)), uniformly.
Thus each adjacent pair of u components has norm bounded below by a constant
times |g|^2+1/4. The resolvent identity Im g=eta sum|u_n|^2 yields
Im g>=b(|g|^2+1/4), and hence the stated upper and lower bounds. The tail need
only be self-adjoint and the finite chain, if used, must contain those steps.
This proves bounds, not pointwise convergence of g.

The outgoing fast host satisfies |G(z)| comparable to log(1/lambda) near
z=-6lambda in this strip. Consequently |gG| grows and z/g tends to zero,
giving the source limit above. The physical lower-sheet arm resolvent and
outgoing continuation of the open host must not be conflated.

### Coupled-model pole persistence

In the explicitly defined fast/slow coefficient model the fast-induced
slow self-energy is delta=lambda M, where

\[
M_{AA}=(z^2R_{dd}-z)/4,\quad M_{AD}=-zR_{de},\quad
M_{DD}=4R_{ee}.
\]

These are resolvent identities using Fd/2; confinement does not change Fd
because d lies in the host. Uniformly in a disk of radius rho f_s about the
*exact partial-model* pole, lying strictly below the real axis,
M_AA,M_AD=O(lambda), M_DD=O(1/log(1/lambda)). Thus
G_eff=(I-G_s delta)^(-1)G_s differs from G_s by O(lambda/log).
The disk maps precisely to the previously proved fast strip; no presumed
coupled pole is used to obtain the strip estimate.

For completeness the required endpoint sensitivity is controlled, not
inferred from a finite root fit. With e=E-4 and
 e=-6+alpha_k f_s^(2/3)+f_s w,

\[
m_{arm}^{-1}=-J_{2-(e+4)/f_s}(2/f_s)/J_{3-(e+4)/f_s}(2/f_s)
\longrightarrow (2-w)/(w-3).
\]

The uniform turning-point expansion gives, for compact complex c,
J_(2/f-alpha f^(-1/3)+c)(2/f)=f^(2/3)c Ai'(-alpha)+O(f).
The common leading Airy zero has therefore been resolved one order further.
Away from w=3 the ratio error is O(f^(1/3)); analytic Cauchy estimates give
the derivative limit too. The limiting denominator root w=2+a is simple,
with derivative (1+Sigma)^2. This uses the standard uniform complex-order
extension of the [DLMF Bessel transition expansion](https://dlmf.nist.gov/10.19.E8)
and [uniform expansions](https://dlmf.nist.gov/10.20#ii), not a new special-function result.

Rouche's theorem about the exact partial pole then bounds the displacement
by O(f_s lambda/log) in slow units, or **O(Jz lambda^5/log)** physically.
It is smaller than the lambda^4 width, so the coupled coefficient-model
resonance survives. Comparing against only the leading Airy approximation
would not establish this smaller shift. Numerical coupled controls have
residuals below3.3e-10; width/lambda^4 at lambda=.2,.1,.05,.025,.02 is
.14270258,.12444387,.11726074,.11463489,.11438912. The rescaled displacement
|delta e_phys| log(1/lambda)/(Jz lambda^5) stays between .0937 and .1334 in
these controls. This checks the analytic coefficient-model argument; it does
not validate the omitted native coefficients.

## 4. What the readout and dispersion actually say

For the limiting source u=(1,2)/sqrt2 the partial-model complex resonance
residue is

\[
( u^T G_s A)^2(1-a)^2\lambda^6/8
=(-.03036209-.03638514i)\lambda^6.
\]

This is not a positive spectral weight. The positive real-axis response
of this specified slow model has a Fano dip from interference with its host.
At lambda=.1 the sampled minimum is about .06085 against background .3203.
That line shape uses the limiting source, not a full native detector formula;
the confined fast channel's real-axis nonuniformity remains separate.

The slow arm gives positive longitudinal quadratic coefficient Jz lambda^2/4.
The partial slow host's transverse boundary dispersion gives approximately
+.0005351 Jz lambda^4. Positivity improves on the previous fast family, but
the scales are strongly anisotropic. Neither is a Lorentz-invariant cone or
an observed scalar dispersion. Rest energy remains near8Jz.

## 5. Boundary, failure memory and next test

The native H supplies the displayed coefficients and source vertices. The
resonance theorem is for a projected coefficient model that includes the
specified fast coupling and both leading tensions, **not the complete native
normal form**. Native higher-order terms, other channels, uniform growing-
length remainders, equilibrium-state selection and measurement mapping remain
open. The separately checked fast K2 block is recorded as evidence but is
not silently included in the pole solver. Unknown terms may affect mass,
dispersion or even the validity of the model reduction.

Failed shortcuts preserved: discarding the slow continuum; assigning width
only to the fast channel; replacing the confined fast arm pointwise on the
real axis; interpreting a negative complex residue as negative probability;
using the wrong ell offset; treating an asymptotic source as an O(lambda)
accurate finite-lambda detector; and treating finite-dimensional bit-path
checks as full many-qubit spectra.

Next test: derive symmetry constraints and omitted native coefficients on
the entire resonant neighborhood, then establish a uniform projection error
smaller than the signal/width. A chosen long interval or selected readout is
not a derivation of a cosmological state or universal matter coupling.

## Reproduction and review

Run `python scripts/native_slow_bulk_composite.py`. It records source hashes,
exact path output and explicitly labelled coefficient-model controls.
The native pack contains focused checks for the axial graph, source, host,
response, fast K2 block, confined-strip bound and coupled endpoint argument.
No formal audit verdict is applied. The canonical block is bounded support
for the user's missing mode/coupling, not a retained scalar proposal.
