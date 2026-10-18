# Native collision coefficient for large neutral features

Status: bounded-support. This is a coefficient-level result for the original
one-qubit Hamiltonian. It is not an exact four-body scattering amplitude,
a decay rate, a cosmological identification, or an observation test.

## Premises and normalization

Use the same supplied microscopic Hamiltonian

\[
H=-J\sum_r(Z_rZ_{r+e_z}+\lambda X_rX_{r+e_x}
                         +\lambda Y_rY_{r+e_y}).
\]

The weak-coupling normal form, aligned-column vacuum sector, and native
compact layer-even two-column feature are those of
`LARGE_BOUND_FEATURE_PROOF.md` and `TWO_FEATURE_LADDER_PROOF.md`.
No interaction is added here. Work with the first coefficient `K_N` in a fixed
broken-z-bond sector. The incoming pair feature has COM momentum
`Q=(0,2 acos(b),0)` and coefficient energy
`E=-4(1+b)-delta`, with `b<bc`. Its two-singleton relative host is inversion
even, `phi(r)=phi(-r)`, with

\[
\phi(e_x)=u v_x/\sqrt2,\qquad
\phi(e_y)=u v_y/\sqrt2,\qquad v_x^2+v_y^2=1.
\]

Here `u>0` is the total root amplitude of the normalized host-plus-rays
feature. The positive root vector `v` and the attached x/y vertical rays
are derived from the native two-body eigenproblem, not chosen couplings.
Write the unnormalized-in-COM pair coefficient

\[
f(i,j)=e^{iQ\cdot(i+j)/2}\phi(i-j).
\]

This convention deliberately omits finite-volume COM factors. Every collision
coefficient below states its plane-wave convention; none is a normalized
cross section. Near the critical value, the existing threshold proof gives
`u²` proportional to `delta log²(1/delta)` and a relative feature radius
proportional to `delta^(-1/2)`.

## Exact native contact residual

For four distinct singletons `S={i,j,k,l}` in a common z layer, the coefficient
of `Bdag²|vac>` is twice the sum over its three pairings. Apply the *native*
`K_8`, including the six-flip inputs with a length-two vertical ray in one
feature. A four-singleton output can receive these inputs by removing the
other vertical endpoint. Both endpoints and both orders in `Bdag²` must be
counted. Applying the two-body bound-state equation to each pairing cancels
these ray inputs and the two copies of `E`.

The remaining terms are precisely the independent-pair hopping terms that
would land one constituent on a site already occupied by the other pair.
The physical spin hopping forbids those terms. Since its hopping coefficient
is minus one, their subtraction leaves

\[
R(S):=[(K_8-2E)P_8B^{\dagger2}|0\rangle]_S
 =4\sum_{i\to j\ \text{occupied xy neighbors}} f(j,k)f(j,l). \tag{1}
\]

The sum is directed; `k,l` are the two remaining sites. Equation (1) concerns
this four-singleton output channel, not every output of the collision.
It derives the contact contribution from spin exclusion and the existing
Hamiltonian. It introduces no new potential. At the exactly soluble
`b=0` anchor, an independent direct physical-bit calculation includes all
native reverse inputs and checks 710 outputs, 168 nonzero, to `5.4e-15`.

## On-shell plane-wave coefficient

Let `p_1,...,p_4` have sum `2Q` modulo reciprocal lattice vectors. Use the
full 24-term outgoing permanent

\[
F(S)=\sum_{\pi\in S_4}\exp[-i\sum_a p_a\cdot r_{\pi(a)}].
\]

Define `K` as the sum of `F(S)R(S)` per xy translation and per common layer.
Anchoring the target of each directed contact at zero gives

\[
K=4\sum_{d=\pm e_x,\pm e_y}
 \sum_{k<l;\ k,l\notin\{0,d\}} f(0,k)f(0,l)F(0,d,k,l). \tag{2}
\]

At every `delta>0` the bound-state sums converge. Set

\[
S_p^{(d)}=\widehat\phi(p-Q/2)-f(0,d)e^{-ip\cdot d},
\quad
G_q^{(d)}=\widehat{\phi^2}(q-Q)-f(0,d)^2e^{-iq\cdot d}.
\]

The zero-relative-site coefficient is zero. Summing the ordered assignments
of the two remaining momenta to `k,l` in the unordered sum in (2) yields

\[
K=4\sum_d\sum_{a\ne b}e^{-ip_b\cdot d}
 \left[S_{p_c}^{(d)}S_{p_e}^{(d)}-G_{p_c+p_e}^{(d)}\right], \tag{3}
\]

where `c,e` are the remaining two labels. The subtraction is the excluded
`k=l` term. Duplicate momentum labels still count separately in this
24-term convention.

## Large-feature limit without squaring a weak limit

Use normalized torus measure `dk/(2pi)²`. Let
`g0`, `gx`, `gy` be the free host Green coefficients at `E`,
`D=(gx-g0,gy-g0)`, and `sigma=(E+sqrt(E²-16))/2`.
The exact host Fourier coefficient is

\[
\widehat\phi(k)/u=
\frac{\sqrt2\sigma[v_x(\cos k_x-g_x/g_0)
                         +v_y(\cos k_y-g_y/g_0)]}
 {E+4\cos k_x+4b\cos k_y}.
\]

For `A_k=1-cos(kx)`, `B_k=1-cos(ky)`, this splits as

\[
h_b(k)+\frac{\tau_b}{\delta+4(A_k+bB_k)},\quad
h_b=\frac{\sqrt2\sigma(v_x A_k+v_y B_k)}
               {\delta+4(A_k+bB_k)},\quad
\tau_b=\sqrt2\sigma(v\cdot D)/g_0>0. \tag{4}
\]

The positive term has mass `a_b=-sqrt2 sigma(v.D)`, since the integral of
its denominator inverse is `-g0`. The bounded negative term has opposite
mass, because `phi(0)=0`. At `b=bc`, define

\[
h(k)=\frac{\sigma}{2\sqrt2}
             \frac{v_x A_k+v_y B_k}{A_k+bB_k},
\qquad a=-\sqrt2\sigma(v\cdot D)>0. \tag{5}
\]

The positive part of (4) is an approximate identity of mass tending to `a`:
outside any neighborhood of zero it is `O(1/log(1/delta))`. The regular
part is uniformly bounded and converges off zero. For a fixed nonzero `q`,
these facts prove

\[
\widehat{(\phi/u)^2}(q)\longrightarrow
 I(q)+2a h(q),\qquad I(q)=\int h(k)h(q-k)\,dk/(2\pi)^2. \tag{6}
\]

For completeness, split the torus into disjoint neighborhoods of `0` and
`q`, and their complement. The regular-regular integral converges by bounded
dominated convergence. In each mixed term the regular factor is smooth near
the peak and tends to its value at `q`. In the peak-peak term one denominator
is bounded away from zero in each neighborhood, so the integral is bounded
by a constant times `tau_b² |g0|=O(1/log(1/delta))`; on the complement it is
`O(tau_b²)`. It therefore vanishes. This also holds for the moving `q` below,
which stays separated from zero. No product of delta distributions is used.

## Compatible breakup momenta and a strict positive bound

Choose two copies each of `p+=(theta,qy)` and `p-=(-theta,qy)`, with

\[
q_y=Q_y/2-\pi/2,\quad
\cos\theta=1+b+\delta/4-\cos q_y.
\]

Their total momentum is `2Q` modulo `2pi` and their free four-singleton
energy is `-8(cos(theta)+cos(qy))=2E`. This is an asymptotic free breakup
channel, not a constructed exact outgoing scattering state.

In the limit all single arguments `p-Q/2=(±theta,-pi/2)` and double arguments
`p+p'-Q=(0 or ±2theta,-pi)` avoid zero. Thus (3)-(6) apply. Reflection makes
`K/u²` real. Direct finite summation of the momentum labels gives

\[
\lim K/u^2=C-64(1+b)I(0,-\pi)
                  -32(1+b)I(2\theta,-\pi). \tag{7}
\]

Here `C` is exactly the finite sum (3), with `u=1`,
`phi_hat(p-Q/2)=h(p-Q/2)`, `f(0,d)=exp(iQ.d/2)v_axis/sqrt2`, and
`phi²_hat(q-Q)=2a h(q-Q)`. This finite expression, rather than a fitted
constant, defines `C`.

Because `h<=0` and `|h|<=M=-sigma max(vx,vy/b)/(2sqrt2)`,

\[
I(q)\le\int h^2\le M\int|h|=Ma.
\]

Consequently (7) is at least `C-96(1+b)Ma`. The outward-rounded interval
calculation uses the previously certified
`bc in [.2347569009270,.2347569009271]` and derives the root ratio from
`vx/vy=sigma Gxy/(1-sigma Gxx)`. It verifies `vy/b>vx` and gives

- `C in [83.743085321718,83.743085322965]`;
- `a in [.5110396346990,.5110396347003]`;
- `M in [1.3396839006926,1.3396839006950]`;
- **`C-96(1+b)Ma in [2.5891438341,2.5891438357] > 0`.**

Thus the native contact coefficient is nonzero for sufficiently large
near-threshold features, with leading size dependence `K=Theta(u²)`, hence
`Theta(delta log²(1/delta))` in the stated convention. Bounded torus
quadrature suggests the limiting ratio is approximately `51.0521`; this
numerical estimate is not needed for the nonzero proof.

## Exact anchor and limits of the result

At `b=0`, use the different unnormalized host convention
`f((x,y),(X,Y))=(-1)^min(y,Y) (1/sqrt2)^|X-x|` for `|Y-y|=1`, zero otherwise.
The length-two y-ray is `-froot/sqrt2`. Using the six-term, rather than
24-term, outgoing permanent and `cos(theta)=3sqrt2/4-1`, direct geometric
summation gives `(309-513sqrt2)/7`, approximately `-59.4987939282`.
Different host phase/normalization and permanent conventions explain why
this is not directly comparable to (7). The anchor is leading-dark to the
original readout and is not a large feature.

The result supplies a native nonzero on-shell Born/contact numerator, not
an exact on-shell T matrix. Repeated collisions, distorted outgoing states,
other four-body channels and higher-order microscopic corrections remain.
A nonzero numerator does not prove an exact decay, exclude an embedded
state, or determine a lifetime. The Hamiltonian, weak regime, selected
momentum family, state preparation and physical units remain premises.
There is no observational calibration or independent empirical test here.
