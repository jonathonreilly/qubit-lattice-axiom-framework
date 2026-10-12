---
claim_id: spatial_particle_to_nonlinear_fluid_limit_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For the supplied tuned D3Q27 local population CTMC, the specified iid principal-cutoff preparation at amplitude delta and a supplied smooth nonlinear fluid lifetime admit an explicit stopped L2 path bound. The simultaneous choices ell comparable to delta squared and N at least delta to minus 19 give O(delta) path error with O(delta squared) failure probability, including multinomial initial fluctuations, actual local jumps, nonlinear Fourier aliasing and stopping overshoots."
upstream_dependencies:
  - supplied_finite_velocity_collisions_and_gibbs_equilibration_bounded_theorem_note_2026-10-08
  - d3q27_dissipative_hydrodynamic_approximation_bounded_theorem_note_2026-10-09
  - d3q27_nonlinear_fluid_limit_bounded_theorem_note_2026-10-11
runner: scripts/spatial_particle_to_nonlinear_fluid_limit_2026_10_11.py
---

# A simultaneous spatial particle to nonlinear fluid limit

**Date:** 2026-10-11

**Type:** bounded_theorem

**Status:** proposed_retained

Current surface status: conditional-support. Independent retained-status audit has not occurred.

**Source baseline:** current main `a13caa4885f547c8d206265b031ba7649e539fd9`;
provisional transport parent `73a76d2141d30d75c6aebfb2f2f9baa6e0a025bf`.

**Runner:** [exact finite controls](../scripts/spatial_particle_to_nonlinear_fluid_limit_2026_10_11.py).

**Evidence cache:** `logs/runner-cache/spatial_particle_to_nonlinear_fluid_limit_2026_10_11.txt`.

For the supplied strictly local count process, this note proves a quantitative
comparison of its entire classical path with nonlinear incompressible momentum
flow and the specified advected diffusive scalar on a supplied smooth lifetime.
The fluctuation amplitude is \(a=\delta\). One sufficient simultaneous schedule is

\[
 m=\text{least odd integer}\ge\max\{3,2\pi\delta^{-2}\},\qquad
 N=\max\{2,\lceil\delta^{-19}\rceil\},\qquad a=\delta.
 \tag{1}
\]

For sufficiently small \(\delta\), with explicit conditions below, the
\(L_M^2\) path error is at most \(C_{\mathrm{path}}\delta\) with failure
probability at most \(C_{\mathrm{prob}}\delta^2\). The constants depend on
the declared smooth fluid solution, its fixed lifetime and the fixed collision
model; they are independent of \(\delta,m,N\). The rate choice, transport,
clock, particle interpretation and initial preparation are supplied premises.
The result does not identify the scalar with a physical temperature or supply
native M2 dynamics.

The proof first controls a deterministic nonlinear grid solution in \(H^4\),
including its actual quadratic aliasing. A stopped \(L^2\) comparison then
controls every cell component of the particle error. Pointwise collision
conservation \(P\Gamma=0\) survives the grid and exact conditional drift:
its pairing with microscopic dissipation avoids a singular nonlinear Gronwall
exponent. The random jump quadratic variation is retained explicitly.

## 1. Dependencies and exact scope

The [finite collision contract](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md)
supplies the D3Q27 reaction model. The
[hydrodynamic parent](D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md)
proves its five-dimensional invariant kernel, microscopic inverse, positive gap
and tuned constitutive response. The
[nonlinear-fluid parent's full correctors](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md#3-full-correctors-and-fluid-equations)
provide all five projected solvability conditions, pressure correction, the
coefficient \(2/5\) in scalar advection, and the exact quadratic residual.
Its regularity and smooth-lifetime hypotheses are imposed below at \(s=4\).
The continuum [positivity and lifetime conclusion](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md#4-uniform-stability-and-existence)
is conditional on its own preparation and smallness conditions. Here grid
positivity and continuation are proved with the explicit conditions (15) and
(22); they are not inferred from an unspecified continuum solution.

| Source | Source SHA-256 and used content |
|---|---|
| [Finite collision contract](SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md) | `888ede1aba130d9bf4df5ffecfbadf9c4e45dd94a49ca3a350894a052e0677c0`; reaction network and Gibbs weights |
| [Dissipative hydrodynamic parent](D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md) | `038e1ed6942d79720aa1dd7360d90f9fa1067016940ceb3554efeb99c21ed0c1`; finite kernel, gap, inverse and constitutive coefficients |
| [Nonlinear fluid parent](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md) | `c81c0029fb70d1cea0ecf41ee893caf357747bcda138af5d1bef5ed5848a114a`; complete correctors, five-moment compatibility, residual and regularity |

The two hydrodynamic sources are provisional branch dependencies, absent from
the stated current-main baseline. Their selective independent checks do not
constitute applied retained-status audits. This theorem uses their explicit
finite identities and corrector construction. Its deterministic grid estimate
is proved directly against the cutoff corrector, so an intermediate exact
continuum kinetic solution is unnecessary.

The [earlier particle-to-linear-fluid note](SPATIAL_PARTICLE_TO_LINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-09.md#1-model-and-target)
uses the same local classical count process with a smaller fluctuation
amplitude. The new argument retains the order-one fluid nonlinearity at
\(a=\delta\) and proves its particle and mesh comparison. The classical
process, preparation and every required finite-rate estimate are specified
again below. This unit contains no quantum measurement or history conclusion.
It makes no claim of external novelty of the general energy method.

## 2. Fixed model, norms, and the smooth target

Use \(V=\{-1,0,1\}^3\), \(e_v=|v|^2\),
\(M_v=(2/3)^{3-e_v}(1/6)^{e_v}\), and
\(m_*:=\min_vM_v=1/216\). All 288 reversible four-distinct-species exchanges
\(r:\{i,j\}\leftrightarrow\{k,l\}\) preserve velocity and \(e\).
Count each reversible exchange once; its two directions are separate count
transitions in Section 4.
The nine axial exchanges are
\(\{s e_c-e_a,s e_c+e_a\}\leftrightarrow
\{s e_c-e_b,s e_c+e_b\}\), where \(c\) is one coordinate, \(a,b\)
are the other two, \(s\in\{-1,0,1\}\), and the \(e_a\) here are spatial
unit vectors. They receive
\(\alpha_*=(-4579+3\sqrt{7614177})/1072>1\); all other rates are 1.
This is exactly the rate choice of the linked nonlinear-fluid theorem.

To fix every sign and factor, write \(W=\operatorname{diag}M\),
\(\nu_r=\mathbf e_k+\mathbf e_l-\mathbf e_i-\mathbf e_j\), where
\(\mathbf e_i\) are species basis vectors, and
\(q_r=\kappa_rM_iM_j\). Detailed balance gives \(M_iM_j=M_kM_l\).
Define

\[
 B=W^{-1}\sum_rq_r\nu_r\nu_r^{\mathsf T},\qquad
 \Gamma(g,h)=W^{-1}\sum_r{q_r\over2}\nu_r
 (g_i h_j+g_j h_i-g_k h_l-g_l h_k).
\]

Let \(P\) be the \(M\)-orthogonal projection onto
\(\mathcal K=\operatorname{span}\{1,v_x,v_y,v_z,e\}\), set
\(Q=I-P\), \(R=(B+P)^{-1}-P\), and let \(\lambda>0\) be the
least positive eigenvalue of \(B\). The finite parent proves rank 22 of
the stoichiometric matrix, so these are all collision invariants and
\(R\) is the microscopic inverse. Its identities include

\[
 B\ge\lambda Q,\quad P\Gamma(g,h)=0,\quad
 \Gamma(U,U)=B(U^2/2)\ (U\in\mathcal K),
 \quad BR=RB=Q.
 \tag{2}
\]

Here \(B\) and \(P\) are self-adjoint in
\(\langle g,h\rangle_M=\sum_vM_v\overline{g_v}h_v\).
Each invariant annihilates \(\nu_r\), which proves \(P\Gamma=0\)
reaction by reaction. If \(U\in\mathcal K\), then
\(U_i+U_j=U_k+U_l\); squaring this identity proves the quadratic
identity in (2). For the population collision operator
\(\mathscr C(f)=\sum_r\kappa_r\nu_r(f_i f_j-f_k f_l)\), the exact
expansion is

\[
 \mathscr C(M(1+\delta h))
       =-\delta WB h+\delta^2W\Gamma(h,h).
\]

Thus the continuum fluctuation equation is precisely
\(g_t+Tg/\delta+Bg/\delta^2=\Gamma(g,g)/\delta\), with
\(T=v\cdot\nabla\), as in the nonlinear parent. Put

\[
 J_r=\sum_{v\in r}M_v^{-1},\qquad
 C_R=\sum_r\kappa_rM_iM_jJ_r=\operatorname{tr}B,\qquad
 S=\sum_r\kappa_rM_iM_j.
 \tag{3}
\]

Every constant is fixed by the finite supplied model. If an explicit
upper bound is preferred to \(\lambda^{-1}\), the hydrodynamic parent gives
\(\lambda^{-1}\le b_*=6224911145567/509693499350\), since all these rates
are at least 1. Replacing \(\lambda^{-1}\) by \(b_*\) in all exponents
below only enlarges the bounds.

The exact enumeration in this packet also gives
\(C_R=(124+4\alpha_*)/3\) and
\(S=97/432+\alpha_*/54\), so the finite sums in (3) need no numerical
eigenvalue or fitted input.

Space is the torus \((\mathbb R/2\pi\mathbb Z)^3\) with measure
\(dx/(2\pi)^3\). For odd \(m\ge3\), let \(\ell=2\pi/m\),
\(w=m^{-3}\), and cell centers \(x_z=\ell z\), with
\(z\in(\mathbb Z/m\mathbb Z)^3\).
Write \(K_m=\{-(m-1)/2,\ldots,(m-1)/2\}^3\). The DFT is
\(\widehat h(k)=w\sum_ze^{-ik\cdot x_z}h_z\), and

\[
 \|h\|_{s,m}^2=\sum_{k\in K_m}(1+|k|^2)^s
                         \sum_vM_v|\widehat h_v(k)|^2.
 \tag{4}
\]

In particular \(\|h\|_{0,m}^2=w\sum_{z,v}M_v|h_{z,v}|^2\).
The continuum norm \(\|h\|_s\) uses the same Fourier expression with
\(k\in\mathbb Z^3\) and normalized continuum Fourier coefficients;
\(\|\cdot\|_0=\|\cdot\|_{L_M^2}\).
The cell volume in this norm is \(w\), not \(\ell^3\).
Let \(\mathcal P_m\) denote continuum Fourier cutoff to \(K_m\),
\(\mathcal S_m\) evaluation at the cell centers, \(J_m\) trigonometric
interpolation, and \(I_m\) piecewise constant cell interpolation.
Both interpolations preserve \(\|\cdot\|_{0,m}\); in particular the noisy
field will need no regularity for its piecewise constant interpolation.

The upwind operator is

\[
 (A_mh)_{z,v}=\sum_d{|v_d|\over\ell}
           (h_{z-\operatorname{sign}(v_d)e_d,v}-h_{z,v}).
 \tag{5}
\]

Its Fourier symbol has nonpositive real part, and
\(L_m=A_m/\delta-B/\delta^2\) is dissipative in every norm (4).
This is a statement about the sum of two dissipative operators; no
commutation between streaming and \(B\) is assumed.

The continuum and grid Sobolev estimates, uniformly in \(m\), are

\[
 \|h\|_\infty\le E\|h\|_{s,m},\quad E=6/\sqrt{m_*},\qquad
 \|\Gamma(g,h)\|_{s,m}\le G_s\|g\|_{s,m}\|h\|_{s,m},
 \quad G_s={4(6\,2^s)S\over m_*^{3/2}},\quad s\ge3.
 \tag{6}
\]

Here \(\|h\|_\infty\) is the maximum absolute component over space
and velocity, and the same estimates hold in the continuum. For completeness,
count the shell \(|k|_\infty=n\), which has \(24n^2+2\) points. For
integer \(s\ge3\), the decreasing-function integral bound gives

\[
 \sum_{k\in\mathbb Z^3}(1+|k|^2)^{-s}
 \le1+26\left(1+{1\over2s-3}\right)<36.
\]

Cauchy--Schwarz in Fourier space proves the embedding in (6). Write
\(\langle k\rangle=(1+|k|^2)^{1/2}\). The weight split
\(\langle p+q\rangle^s\le
2^{s-1}(\langle p\rangle^s+\langle q\rangle^s)\), followed by
Young's convolution inequality and the Fourier \(\ell^1\) bound 6,
gives the scalar product constant \(C_s=6\,2^s\).
For one reaction, \(\|W^{-1}\nu_r\|_M\le2/\sqrt{m_*}\), and
each scalar component has \(H^s\) norm at most the full weighted norm
divided by \(\sqrt{m_*}\). The four products with the factor \(1/2\)
therefore give \(4C_s q_r/m_*^{3/2}\); summing proves \(G_s\).

On the finite grid, the principal representative of \(p+q\) has Euclidean
length at most \(|p+q|\), so the same weight split holds. Finite-group
convolution has the same Young inequality, and its embedding sum is bounded
by the preceding continuum sum. These observations prove every constant in
(6) uniformly in \(m\). Pointwise \(P\Gamma=0\) remains true after
aliasing and after multiplication by the scalar Sobolev weight.

Let a real smooth solution on \([0,L]\) be supplied:

\[
 \nabla\cdot j=0,\quad
 j_t+j\cdot\nabla j+\nabla\pi=\nu\Delta j,\quad
 \rho_t+\tfrac25j\cdot\nabla\rho=D\Delta\rho,
 \qquad \nu=67/361,\ D=4/49.
 \tag{7}
\]

Assume \(\overline\rho(0)=0\), fix \(\overline\pi=0\), and impose
precisely the [nonlinear parent's smooth-lifetime hypothesis at \(s=4\)](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md#3-full-correctors-and-fluid-equations):

\[
 \rho,j\in C([0,L];H^8)\cap C^1([0,L];H^6)
                         \cap C^2([0,L];H^4).
\]

Pressure is the zero-mean solution of
\(-\Delta\pi=\sum_{a,b}\partial_a\partial_b(j_a j_b)\);
its Fourier multiplier inherits the required regularity. This fixed smooth
interval is an input, with no assertion of global three-dimensional
regularity. The scalar equation and \(\nabla\cdot j=0\) preserve
\(\overline\rho=0\).

Let \(A=(5-3e)/2\), \(U=\rho A+3j\cdot v\), and
\(H(r,J,E)=rA+3J\cdot v+(3/2)E(e-1)\), whose five moments are
\((r,J,E)\). To specify the exact corrector dependency, set

\[
 F_1=\tfrac25\rho j-D\nabla\rho,\quad
 J_1=F_1-\overline{F_1},\quad
 E_1=3\pi+|j|^2-\overline{|j|^2},
\]
\[
 u_1=Q(U^2/2)-RTU+H(0,J_1,E_1),\qquad
 u_2=R[2\Gamma(U,u_1)-U_t-Tu_1].
\]

These are the fields named \(w,z\) in the nonlinear parent. Its
[complete five-moment calculation](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md#3-full-correctors-and-fluid-equations)
proves \(P(U_t+Tu_1)=0\), including mass, pressure and energy, and hence

\[
 BU=0,\qquad TU+Bu_1-\Gamma(U,U)=0,\qquad
 U_t+Tu_1+Bu_2-2\Gamma(U,u_1)=0.
\]

Define
\(R_1=(u_1)_t+Tu_2-2\Gamma(U,u_2)-\Gamma(u_1,u_1)\),
\(R_2=(u_2)_t-2\Gamma(u_1,u_2)\), and
\(R_3=-\Gamma(u_2,u_2)\). With
\(S_0=\sup_{t\le L}(\|R_1\|_4+\|R_2\|_4+\|R_3\|_4)\),
expanding the quadratic equation gives the exact residual
\(\mathcal R^\delta=\delta R_1+\delta^2R_2+\delta^3R_3\):

\[
 G^\delta=U+\delta u_1+\delta^2u_2,
\quad
 G_t^\delta+TG^\delta/\delta+BG^\delta/\delta^2
                  -\Gamma(G^\delta,G^\delta)/\delta
       =\mathcal R^\delta,
\quad \|\mathcal R^\delta\|_4\le\delta S_0.
 \tag{8}
\]

These are exact identities, with \(T=v\cdot\nabla\). Define finite,
\(\delta\)-independent constants

\[
 K_4=\sup_{t\le L}(\|U\|_4+\|u_1\|_4+\|u_2\|_4),\quad
 K_6=\sup_{t\le L}(\|U\|_6+\|u_1\|_6+\|u_2\|_6),
\]
\[
 I_0=\|u_1(0)\|_4+\|u_2(0)\|_4,\qquad
 C_f=\sup_{t\le L}(\|u_1\|_0+\|u_2\|_0).
 \tag{9}
\]

The declared regularity makes \(K_6\) finite: the source has
\(u_1\in C H^7\) and \(u_2\in C H^6\). Here and below continuum norms
are weighted in velocity by \(M\).

## 3. Deterministic grid estimate, including the nonlinear alias error

Set \(q_m=\mathcal S_m\mathcal P_mG^\delta\), and

\[
 \sigma_m=[1+((m+1)/2)^2]^{-1},\qquad
 C_{\rm nl}=(2G_4+\sqrt{26}\,G_6)K_6^2.
 \tag{10}
\]

The exact grid residual is

\[
 r_m=q_m'-L_mq_m-\Gamma(q_m,q_m)/\delta,
\qquad
 \|r_m\|_{4,m}\le\varepsilon_m
 :=\delta S_0+{\ell K_6\over2\delta}
                         +{\sigma_m C_{\rm nl}\over\delta}.
 \tag{11}
\]

For this estimate abbreviate \(G=G^\delta\) and write
\(H=\mathcal P_mG\). The exact residual decomposition is

\[
 r_m=\mathcal S_m\mathcal P_m\mathcal R^\delta
 -{A_m\mathcal S_mH+\mathcal S_mTH\over\delta}
 +{\mathcal S_m\mathcal P_m\Gamma(G,G)
                       -\mathcal S_m\Gamma(H,H)\over\delta}.
\]

Here is a full justification of the alias term.
First
\(\|G-H\|_4\le\sigma_m\|G\|_6\). Bilinearity and the continuum
product bound give

\[
 \|\Gamma(G,G)-\Gamma(H,H)\|_4\le2G_4K_6^2\sigma_m.
 \tag{12}
\]

The continuum product \(F=\Gamma(H,H)\) is supported in \(2K_m\).
The DFT of its sampled values is
\(\sum_{n\in\mathbb Z^3}\widehat F(k+mn)\).
For \(k\in K_m\), at most 26 noncentral preimages can occur
(a deliberately loose bound; this support permits at most seven).
For each such preimage, \(|k|\le|k+mn|\), and it is outside \(K_m\).
Cauchy--Schwarz over the preimages, followed by summation over \(k\) and
velocity, therefore gives

\[
 \|\mathcal S_mF-\mathcal S_m\mathcal P_mF\|_{4,m}
 \le\sqrt{26}\,\|(I-\mathcal P_m)F\|_4
 \le\sqrt{26}\,\sigma_m G_6K_6^2.
 \tag{13}
\]

Pointwise evaluation satisfies
\(\Gamma(\mathcal S_mH,\mathcal S_mH)=\mathcal S_m\Gamma(H,H)\).
Combining (12)--(13) proves the nonlinear part of (11).
There is no unestimated replacement of a grid product by a continuum product.

The streaming symbol satisfies
\(\|\operatorname{symbol}(A_m)+i\operatorname{diag}(v\cdot k)\|_M
\le\ell|k|^2/2\), from
\(|e^{-iy}-1+iy|\le y^2/2\). This gives the middle term of (11).
The collision matrix and time derivative commute with the cutoff, so neither
produces a \(\delta^{-2}\) cutoff remainder. Finally the sampled cutoff of
\(\mathcal R^\delta\) has the same \(H^4\) norm as its continuum cutoff.
These observations prove every term of (11).

Let the deterministic grid field solve

\[
 g_m'=L_mg_m+\Gamma(g_m,g_m)/\delta,\qquad
 g_m(0)=v_m^0:=\mathcal S_m\mathcal P_mU(0).
 \tag{14}
\]

Put

\[
 a_d={G_4^2(2K_4+1)^2\over2\lambda},\qquad
 d_m=e^{a_dL}(\delta I_0+L\varepsilon_m).
 \tag{15}
\]

Assume \(d_m\le1/2\). Then on \([0,L]\)

\[
 \|g_m-q_m\|_{4,m}\le d_m,\qquad
 \|g_m\|_{4,m}\le K_g:=K_4+1,\qquad
 \|g_m\|_\infty\le R_0:=EK_g.
 \tag{16}
\]

For completeness, if \(d=g_m-q_m\), then its nonlinear error is
\(2\Gamma(q_m,d)+\Gamma(d,d)\), entirely microscopic. While
\(\|d\|_{4,m}\le1\), dissipativity and Young's inequality give

\[
 \tfrac12(\|d\|_{4,m}^2)' +{\lambda\over2\delta^2}\|Qd\|_{4,m}^2
 \le a_d\|d\|_{4,m}^2+\varepsilon_m\|d\|_{4,m}.
 \tag{17}
\]

Regularizing the square root at zero and integrating proves (16), since the
initial error is at most \(\delta I_0\). The bound \(d_m\le1/2\) prevents
exit from the bootstrap ball. Finite-dimensional local existence and this
uniform bound give continuation to \(L\). Under the later condition
\(\delta(R_0+1)\le1/2\), the deterministic populations
\(f_{m,z,v}=M_v(1+\delta g_{m,z,v})\) are at least \(M_v/2\)
throughout this interval. Thus the positivity and lifetime needed by this
grid comparison are proved here with their actual smallness condition.
The related [continuum positivity and continuation theorem](D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md#4-uniform-stability-and-existence)
has its own prepared-data and smallness hypotheses; no intermediate exact
continuum kinetic solution is needed in the present proof.

Independently, the corresponding population ODE is
\(f_m'=A_m f_m/\delta+\mathscr C(f_m)/\delta^2\).
At a zero population its outflow and all consuming reaction terms vanish,
while inflow and reaction gains are nonnegative. Thus this locally Lipschitz
ODE preserves nonnegativity. Transport telescopes and every reaction
conserves mass, so the normalized total mass stays one. Its finite mass
simplex is compact for fixed \(m\), giving a separate global continuation
argument whenever its initial populations are nonnegative.

## 4. The exact count process and its initial law

Let \(n_{z,v}\) be nonnegative integer counts with total \(N\ge2\), and set

\[
 F^N_{z,v}={n_{z,v}\over Nw},\qquad
 h^N_{z,v}={F^N_{z,v}/M_v-1\over\delta}.
 \tag{18}
\]

The count process has precisely the earlier supplied transitions:

* a hop \((z,v)\to(z+\operatorname{sign}(v_d)e_d,v)\) at rate
  \(|v_d|n_{z,v}/(\delta\ell)\);
* a forward/reverse collision in one cell at rates
  \(\kappa_r n_{z,i}n_{z,j}/(\delta^2Nw)\) and
  \(\kappa_r n_{z,k}n_{z,l}/(\delta^2Nw)\).

Every pair uses distinct species, so these are the exact count products;
there is no same-species falling factorial or extra factor of two. A collision
acts only inside its cell; a hop connects nearest-neighbor cells according to
its velocity component. Both preserve total particle number, total label
momentum and total label energy. Transport permits variable mass density in
each cell: only \(w\sum_{z,v}F^N_{z,v}=1\) is fixed, not
\(\sum_vF^N_{z,v}=1\) separately at every cell. No global mixing replaces
this spatial transport. The process has finitely many states and bounded
rates at fixed \(N,m,\delta\), so it is nonexplosive.

For a collision, the increment in (18) is
\(W^{-1}\nu_r/(Nw\delta)\). Multiplying by its forward rate minus
reverse rate, substituting \(n=NwM(1+\delta h^N)\), and using the exact
population expansion above gives \(-Bh^N/\delta^2+
\Gamma(h^N,h^N)/\delta\). Hop increments give \(A_mh^N/\delta\)
because \(M\) is constant in space. Thus the exact conditional drift is

\[
 L_mh^N+\Gamma(h^N,h^N)/\delta.
 \tag{19}
\]

This is a conditional generator identity. It does not replace an expected
product of random counts by a product of their expectations.

Prepare \(N\) labeled particles independently with probabilities

\[
 p_{z,v}=wM_v(1+\delta v^0_{m,z,v}).
 \tag{20}
\]

The finite grid integrates the principal cutoff exactly. Since the mass
moment of \(U\) is \(\rho\) and \(\overline\rho(0)=0\), these
probabilities sum to 1. They are positive whenever
\(\delta E\|U(0)\|_4\le1/2\), which follows from the stronger smallness
condition used below. Their count law is multinomial and
\(\mathbb E h^N(0)=v_m^0=g_m(0)\).

Writing \(e=h^N-g_m\), its exact initial \(L^2\) fluctuation is

\[
 \mathbb E\|e(0)\|_{0,m}^2
 ={1\over Nw\delta^2}\sum_{z,v}{p_{z,v}(1-p_{z,v})\over M_v}
 \le {27\over Nw\delta^2}.
 \tag{21}
\]

The coefficient 27 uses this particular preparation, not a generic
independence assumption. Indeed
\(\sum_{z,v}p_{z,v}/M_v=27+\delta w\sum_{z,v}v^0_{m,z,v}=27\):
\(\sum_vv=0\), \(\sum_v(5-3e_v)/2=-27/2\), and the cutoff density has
zero grid mean. The \(p^2\) term from the exact multinomial covariance is
retained until taking the upper bound. The previous source's coefficient 54
is also safe, but is unnecessary for the exact initial data (20).

## 5. Stopped particle estimate without a singular exponential

Assume

\[
 0<\delta\le1,\quad d_m\le1/2,\quad
 \delta(R_0+1)\le1/2.
 \tag{22}
\]

Set

\[
 r=\sqrt{wm_*},\qquad
 \tau=\inf\{t\in[0,L]:\|h^N(t)-g_m(t)\|_{0,m}\ge r\},
 \tag{23}
\]

Use \(\inf\varnothing=+\infty\). An initially excessive error gives
\(\tau=0\). Strictly before exit,
\(|e_{z,v}|\le\|e\|_{0,m}/\sqrt{wM_v}<1\), so
\(\|h^N\|_\infty\le R_0+1\) and \(F^N_{z,v}\le2M_v\).
These bounds concern the pre-jump state; no bound on the exit overshoot is
assumed.

The velocity bilinear estimate gives

\[
 \|\Gamma(a,b)\|_M\le{C_R\over2}\|a\|_\infty\|b\|_M.
 \tag{24}
\]

To verify its constant, one reaction contributes at most
\((\kappa_rM_iM_j/2)\sqrt{J_r}\|a\|_\infty\sum_{v\in r}|b_v|\),
and the last sum is at most \(\sqrt{J_r}\|b\|_M\).
Summing proves (24). Apply it cellwise to the polarization
\(\Gamma(h^N,h^N)-\Gamma(g_m,g_m)=\Gamma(h^N+g_m,e)\).
Its \(L^2\) norm is at most
\(A_p\|e\|_{0,m}\), where

\[
 A_p={C_R\over2}(2R_0+1),\qquad
 L_p={A_p^2\over\lambda}
     ={C_R^2(2R_0+1)^2\over4\lambda}.
 \tag{25}
\]

The nonlinear expression is microscopic. The drift part of the squared
error energy is therefore at most

\[
 -{2\lambda\over\delta^2}\|Qe\|_{0,m}^2
  +{2A_p\over\delta}\|Qe\|_{0,m}\|e\|_{0,m}
 \le -{\lambda\over\delta^2}\|Qe\|_{0,m}^2
                                         +L_p\|e\|_{0,m}^2.
 \tag{26}
\]

The upwind part is dissipative. Thus \(L_p\) has no factor \(\delta^{-1}\)
or \((\delta\ell)^{-1}\). Conservation alone would not bound the random
jumps; their quadratic terms must still be added to this drift inequality.

A hop changes two entries of \(h^N\). Its exact squared jump norm is
\(2/(N^2w\delta^2M_v)\). Before \(\tau\),
\(\sum_zn_{z,v}\le2NM_v\). Since
\(\sum_{v,d}|v_d|=54\), the sum of hop rates times these squared norms is
at most \(216/(Nw\delta^3\ell)\).

A collision jump has exact squared norm
\(J_r/(N^2w\delta^2)\). Each direction in each cell has rate at most
\(4\kappa_rNwM_iM_j/\delta^2\). Summing both directions and all
\(m^3=1/w\) cells therefore gives \(8C_R/(Nw\delta^4)\).
The complete energy-bracket density is bounded by

\[
 V_0={1\over Nw\delta^2}
       \left({216\over\delta\ell}+{8C_R\over\delta^2}\right).
 \tag{27}
\]

Apply the time-dependent finite-state jump energy identity to
\(Y(t)=\|h^N(t)-g_m(t)\|_{0,m}^2\), stopped at \(t\wedge\tau\).
The comparator is stopped at the same time. All rates and drift are
evaluated before the stopping jump; that jump's full quadratic increment
is included by the stopped compensator. Every martingale is integrable
because the state space is finite at fixed parameters. Equations
(21), (26), and (27) give

\[
 \mathbb E Y(t\wedge\tau)
 \le\mathbb E Y(0)+\int_0^t
                   [L_p\mathbb E Y(s\wedge\tau)+V_0]\,ds.
\]

Here replacing the pre-exit indicators by stopped nonnegative energies and
the full constant \(V_0\) only increases the right side. Gronwall yields

\[
 \mathbb E Y(L\wedge\tau)
 \le {e^{L_pL}\over Nw\delta^2}
       \left[27+L\left({216\over\delta\ell}
                                      +{8C_R\over\delta^2}\right)\right].
 \tag{28}
\]

On \(\{\tau\le L\}\), the stopped energy is at least \(wm_*\).
This covers continuous exit due to comparator motion, an overshooting jump,
and \(\tau=0\).
Consequently

\[
 \boxed{\Pr(\tau\le L)\le\min\{1,\Pi_0\},\qquad
 \Pi_0={e^{L_pL}\over Nw^2\delta^2m_*}
       \left[27+L\left({216\over\delta\ell}
                                      +{8C_R\over\delta^2}\right)\right].}
 \tag{29}
\]

On the complementary event the entire path error relative to \(g_m\) is
less than \(r\). Neither a law-of-large-numbers closure at positive times
nor a bound that ignores the exit jump was used.

## 6. Quantitative path bound and the simultaneous schedule

For any deterministic grid field, orthogonality of distinct principal
frequencies across the cell centers gives

\[
 \|I_mg-J_mg\|_{L_M^2}\le\sqrt3\ell\|g\|_{1,m}.
 \tag{30}
\]

For example, write a point in the cell as \(x_z+y\). Averaging the squared
Fourier difference over \(z\) removes cross-frequency terms, and
\(|e^{ik\cdot y}-1|\le|k||y|\) bounds the remaining integral.
The stated constant is larger than the centered-cell optimum.

Using (16), \(J_mq_m=\mathcal P_mG^\delta\), the cutoff tail bound, and
\(\|G^\delta-U\|_0\le\delta C_f\), the event \(\tau>L\) implies

\[
 \boxed{\sup_{t\le L}\|I_mh^N(t)-U(t)\|_{L_M^2}
 \le \sqrt{wm_*}+d_m+\sqrt3\ell K_g+\sigma_mK_6+\delta C_f.}
 \tag{31}
\]

Its probability is at least \(1-\min\{1,\Pi_0\}\). This is the classical
path theorem for every odd \(m\ge3\),
integer \(N\ge2\), and \(\delta\) satisfying (22), with the exact
initial law (20) and the stated fixed-model and smooth-lifetime hypotheses.
It controls the actual particle path, not only one observation
time. Interpolation is applied to the noisy difference only in \(L^2\),
where it is an isometry.

To verify (1) with explicit constants, put \(c_m=2\pi+2\) and
\(c_\ell=2\pi/c_m\). For \(0<\delta\le1\),

\[
 2\pi\delta^{-2}\le m<c_m\delta^{-2},\quad
 c_\ell\delta^2<\ell\le\delta^2,\quad
 \sigma_m\le\delta^4/\pi^2.
 \tag{32}
\]

Therefore

\[
 \varepsilon_m\le\delta
    \left(S_0+K_6/2+C_{\rm nl}/\pi^2\right),\quad
 d_m\le C_d\delta,
\]
\[
 C_d=e^{a_dL}\{I_0+L(S_0+K_6/2+C_{\rm nl}/\pi^2)\}.
 \tag{33}
\]

Conditions (22) hold for all sufficiently small \(\delta\), for instance
when \(\delta C_d\le1/2\) and \(\delta(R_0+1)\le1/2\).
Equation (31) is at most \(C_{\mathrm{path}}\delta\), where one explicit choice is

\[
 C_{\mathrm{path}}=\sqrt{m_*}(2\pi)^{-3/2}
             +C_d+\sqrt3K_g+K_6/\pi^2+C_f.
 \tag{34}
\]

The three smaller deterministic/noise terms in fact have orders
\(\delta^3,\delta^2,\delta^4\), respectively. Also

\[
 \Pi_0\le C_{\mathrm{prob}}\delta^2,\qquad
 C_{\mathrm{prob}}={e^{L_pL}c_m^6\over m_*}
             \left[27+L(216/c_\ell+8C_R)\right].
 \tag{35}
\]

Indeed \(1/(Nw^2\delta^2)\le c_m^6\delta^5\), and the bracket in (29)
is at most the bracket in (35) times \(\delta^{-3}\).
The initial, hopping, and collision contributions to failure are respectively
\(O(\delta^5),O(\delta^2),O(\delta^3)\). These are simultaneous limits
on one process; there is no hidden ordered-limit step. The exponents are
sufficient bounds, not a particle-cost optimum or a physical prediction.

## 7. Analytical obligations and finite evidence

The linked primary runner is self-contained standard-library code using exact
rational arithmetic and \(\mathbb Q(\omega)\), with
\(\omega^2+\omega+1=0\), on a genuine \(3^3\) Fourier grid. It
reconstructs all 288 conservative reactions and their nine axial members,
and recovers the exact axial and nonaxial coefficients of \(C_R\) and \(S\).
It sums the actual rate-times-jump energies at a realizable equilibrium count
state and checks the complete conditional drift at a separate nonuniform
integer count state. A direct DFT checks all collision and directed-hop jump
norms in \(H^0,H^3,H^4\). These latter finite norms are normalization
controls; only the \(L^2\) stochastic path theorem is asserted in this unit.

For nonuniform positive initial probabilities, the runner evaluates the full
multinomial covariance trace and compares it with a separately assembled
Fourier variance. It exhibits an admissible stopping overshoot and verifies
the complete square in (26). An actual quadratic collision product has modes
outside the principal cube; its sampled DFT is checked against the folded
coefficients, and all five invariant contractions still vanish. Finite
principal-map inventories at \(m=3,5,7,9\), dissipative upwind symbols and
separate initial/hop/collision/mesh scale exponents provide additional controls.

The final author baseline passed in 1.804423 seconds under Python 3.13.5;
`AUDIT_TIMEOUT_SEC=180` is a harness budget. Its declared input paths are
provenance/cache dependencies; it does not load expected results from those
notes. Thirteen actual scratch-source mutants were run, each failing a
mathematical assertion. They alter cell-volume normalization, hop endpoints,
collision direction count, collision drift volume, hop clock, exit energy,
the projected-energy coefficient, initial probability volume, multinomial
covariance, microscopic collision output, alias folding, mesh power and
particle-number power. Full source hashes, outputs and failure sites are
preserved in the campaign evidence pack. These are author checks, not a formal
audit or an independent proof of the analytic limit.

The finite drift and rate controls use the positive unit-rate member of the
collision family; axial dependence of \(C_R\) and \(S\) is checked
coefficient by coefficient. They do not re-prove the tuned spectral gap,
constitutive response or full fluid correctors. Those are the explicit linked
parent dependencies. The runner's positive rational gap value is a control
for the scalar complete square, not an eigenvalue certification. Likewise,
the finite alias inventories do not replace the all-grid proof (12)–(13),
and checking scale exponents does not prove stopped Dynkin's formula.

| Proof obligation | Evidence and limitation |
|---|---|
| Five-invariant kernel, microscopic inverse and fixed positive gap | Linked finite hydrodynamic proof; explicit model premises in Section 2 |
| Full mass, momentum, energy and pressure compatibility | Linked nonlinear-parent Section 3, with exact correctors and residual restated here |
| Uniform continuum/grid algebra and actual nonlinear alias error | Full Fourier and cutoff arguments (6), (11)–(13) |
| Deterministic grid lifetime and positive populations | Bootstrap (17), finite ODE continuation and explicit smallness (22) |
| Exact conditional count drift and initial count law | Generator derivation (18)–(21), with actual finite count controls |
| Stopped drift, jump quadratic variation and overshoots | Full argument (23)–(29); finite normalization and overshoot controls |
| Interpolation and simultaneous polynomial schedule | Full argument (30)–(35), including rounded mesh and particle counts |
| Smooth nonlinear fluid lifetime | Supplied regular solution of (7); global three-dimensional existence is outside the statement |
| Independent research checking | Antecedent full cutoff/L2 proof selectively checked; final-source coverage is determined by the separately bound review record, not by these author controls |
| Native carrier, local dynamics, physical scalar, preparation and clock | Remain explicit physical interfaces; no new framework axiom is adopted |

Scoped formal-verification targets include the principal-frequency alias map
and its weighted tail estimate, the exact multinomial covariance trace, the
norm-square jump expansion, and the time-dependent stopped Dynkin argument
including exit overshoots. The five-moment corrector obligations remain with
the linked parent. No Lean execution or applied retained-status audit is
claimed. The theorem is a conditional implication for the stated process,
preparation and supplied smooth solution; its sufficient particle exponent is
not claimed to be optimal.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Compose microscopic spatial dynamics with controlled nonlinear macroscopic transport."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Test native local dynamics, particle preparation, clock and readout interfaces for the supplied nonlinear path theorem."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Quantitative conditional simultaneous particle and mesh limit to the specified nonlinear fluid system, with an explicit path error and failure bound."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
