# Necessary full-field radial compatibility from the supplied Jordan action

This is a focused independent derivation for the author's final campaign block. It is not a formal audit, a new action selection, an observation test, or a full-solution reconstruction. The reviewer previously derived/reviewed the inherited M17 action and M19 metric identities. The parent supplied the target question (positive transverse-potential envelopes and reconstruction of squares), but no new formula. No parent `full_field_metric` working derivation or implementation was opened before this report and its controls were frozen. Exact inherited-source identities and the precise newly read portions are in `SOURCE_PREEXPOSURE_v1.json`.

## 1. Supplied action and domain

Use the complete physical Jordan action from M17, its natural-unit conventions and positive candidate parameters

\[
0<k<1/3,\quad a=(1-k)(1+3k)/4,\quad
\lambda=a/(1-3a)>1,\quad s=(1+k)/[k(1-3k)],
\quad f_0=Q/(1+s)>0,\quad H_v>0,\quad\nu>0.
\]

Here the notation \(w=s+z^2\) avoids conflating the Jordan curvature coefficient \(F_J=f_0w\) with the earlier Einstein-coordinate function also named F. The full action divided by its constant \(f_0\), with material stress zero on the interval, is

\[
\mathcal L/f_0=wR/2-\lambda^{-1}(\nabla z)^2
-h_x(z,x,y)(\nabla x)^2-h_y(z,x,y)(\nabla y)^2-P(z,x,y),
\]

\[
D_\perp=1+\frac{2(1+k)}3(x^2+y^2),\quad
h_x=(1+s)z^2\frac{4k}{9D_\perp},\quad
h_y=(1+s)z^2\frac{k}{3D_\perp},
\]

\[
P=P_0(z)+A_x(z)x^2+A_y(z)y^2,
\quad P_0=H_v^2\left[3(s+z^4)+\frac\nu a z^4\log^2z\right],
\]

\[
A_x=\frac{H_v^2 k}{1+s}(s+z^2)^2z^{r_x},\quad
A_y=\frac{2H_v^2 k}{3(1+s)}(s+z^2)^2z^{r_y},
\quad r_x=(1-k)/a,\quad r_y=(1+k)/a.
\]

All these are supplied candidate functions, not derived from data. Both \(A_x,A_y\) are strictly positive for every \(z>0\); \(r_y-r_x=2k/a>0\).

Take a connected finite annulus with calibrated physical areal radius and metric

\[
ds_J^2=-N(r)^2dt^2+dr^2/B(r)+r^2d\Omega^2,
\quad N>0,\ B>0,\ z>0.
\]

The metric is supplied with \(N\in C^3,B\in C^2\); an actual candidate solution has classical \(C^2\) radial scalar fields. No material stress, pressure term, horizon, angular field dependence, scalar time dependence, or missing metric component is silently admitted. No boundary or initial field value is selected. A trial field-normalization constant remains explicitly below. This is not a measured Newton-constant identification.

## 2. What the metric fixes without setting either transverse field to zero

Put \(A=N'/N\), and use the M19 mixed components \(G_t,G_r,G_a\) and \(R=-(G_t+G_r+2G_a)\). Define physical radial kinetic density divided by \(f_0\):

\[
\mathcal K=B\left[z'^2/\lambda+h_xx'^2+h_yy'^2\right].
\]

It is important that \(\mathcal K\) contains B. The three metric equations are

\[
\begin{aligned}
wG_t&=-\mathcal K-P-Bw''-(B'/2+2B/r)w',\\
wG_r&= \mathcal K-P-B(A+2/r)w',\\
wG_a&=-\mathcal K-P-Bw''-(B'/2+BA+B/r)w'.
\end{aligned}
\]

Their angular-time difference is independent of all scalar kinetic densities and potential:

\[
w(G_a-G_t)=d_{\rm met}w',\qquad d_{\rm met}=B(1/r-A).
\]

On a chart \(d_{\rm met}\ne0\), define

\[
u=(G_a-G_t)/d_{\rm met},\qquad w'/w=u.
\]

The symbol u here is M19's geometric logarithmic derivative, not the old Einstein-frame field coordinate. Consequently for a reference radius \(r_0\),

\[
w_C(r)=C\exp\left(\int_{r_0}^r u(t)\,dt\right),\qquad
z_C(r)=\sqrt{w_C(r)-s},
\tag{1}
\]

where C is an explicit trial positive constant subject to \(w_C>s\) throughout the chart. It represents \(F_J(r_0)/f_0\). It is not determined by the angular-time relation and must not be counted as a retired field-amplitude assumption. Absolute Q cancels from these vacuum equations.

Define the metric functions

\[
H=G_r-G_t-B(u'+u^2)-(B'/2-BA)u,
\]

\[
W=-G_t-H/2-B(u'+u^2)-(B'/2+2B/r)u.
\]

The radial-time difference and the time equation then require

\[
\mathcal K=wH/2,\qquad P_{\rm rec}=wW.
\tag{2}
\]

Thus, for each fixed trial \(k,C\), the transverse physical kinetic remainder is

\[
T=\frac{wH}{2}-\frac{Bz'^2}{\lambda}\ge0,
\qquad z'=\frac{wu}{2z}.
\tag{3}
\]

This does not require \(u\ne0\), \(H>0\), or division by H. Those stronger gates apply only if importing the one-field j inverse. Where u and H are nonzero, \(j=Bu^2/(2H)\) and (3) implies \(z^2\ge sj/(\lambda-j)\) with \(0<j<\lambda\). No differential j identity or unique inferred \(\lambda\) survives in general with moving transverse fields.

## 3. Positive-potential envelope from the exact radial field equation

The static scalar operator is

\[
Lz=Bz''+(B'/2+BA+2B/r)z'.
\]

Since \(\partial_z h_x=2h_x/z\) and likewise for \(h_y\), the full z equation divided by \(f_0\) is exactly

\[
E_z/f_0=\frac2\lambda Lz+zR-\frac{2T}{z}
-P_{0,z}-A_{x,z}x^2-A_{y,z}y^2=0.
\tag{4}
\]

For fixed trial \(k,H_v,\nu,C\), all quantities on the following left sides can be constructed from the supplied metric:

\[
\Delta=P_{\rm rec}-P_0,\qquad
\mathcal E=\frac2\lambda Lz+zR-\frac{2T}{z}-P_{0,z}.
\]

Let \(U_x=A_xx^2\), \(U_y=A_yy^2\), and

\[
\ell_x=\frac{4z}{w}+\frac{r_x}{z},\qquad
\ell_y=\frac{4z}{w}+\frac{r_y}{z},\qquad
\ell_y-\ell_x=\frac{2k}{az}>0.
\]

Because \(A_{x,z}=\ell_xA_x\), \(A_{y,z}=\ell_yA_y\), the potential and z equations imply

\[
\Delta=U_x+U_y,\quad \mathcal E=\ell_x U_x+\ell_y U_y,
\quad U_x,U_y\ge0.
\]

Therefore a necessary local compatibility constraint is

\[
\boxed{\quad T\ge0,\quad\Delta\ge0,\quad
\ell_x\Delta\le\mathcal E\le\ell_y\Delta.\quad}
\tag{5}
\]

The proof is the two exact identities

\[
\mathcal E-\ell_x\Delta=(\ell_y-\ell_x)U_y\ge0,
\qquad \ell_y\Delta-\mathcal E=(\ell_y-\ell_x)U_x\ge0.
\]

This works for all \(z>0\), not just M17's comparison-sign region \(z\ge1\). The derivative of the base regulator can be negative below one; it has been retained exactly in \(P_{0,z}\), not discarded. Explicitly

\[
P_{0,z}=H_v^2z^3\left[12+\frac\nu a(4\log^2z+2\log z)\right].
\]

For computation one may avoid explicit z'' by substituting (3):

\[
\boxed{\quad
\mathcal E=\frac{Lw}{\lambda z}+zR-\frac{wH}{z}-P_{0,z},
\quad Lw=w[B(u'+u^2)+(B'/2+BA+2B/r)u].\quad}
\tag{6}
\]

This uses metric derivatives through the same N''' and B'' as M19; it is not a removal or calibration of those suppliers. A constant time normalization leaves all displayed metric functions invariant.

## 4. Conditional reconstruction of the transverse squares

On the stated strict candidate parameter domain, (5) is exactly the pointwise admissibility criterion for two nonnegative potential pieces:

\[
U_x=\frac{\ell_y\Delta-\mathcal E}{\ell_y-\ell_x},\qquad
U_y=\frac{\mathcal E-\ell_x\Delta}{\ell_y-\ell_x},
\]

\[
\boxed{\quad x^2=U_x/A_x,\qquad y^2=U_y/A_y.\quad}
\tag{7}
\]

There is no division by \(\Delta\); the zero case forces both potential pieces and \(\mathcal E\) to zero. Endpoint equality in (5) sets one coordinate to zero at that radius, not its radial derivative. In particular an isolated zero of a field does not set its kinetic energy to zero. On a whole open interval with \(\Delta=0\), both coordinates vanish identically and so does T.

These formulas determine only squares for supplied trials. Signs, regular continuation across zeros, differentiability, and dynamics are additional questions. On an open interval where both reconstructed squares \(\xi=x^2\) and \(\eta=y^2\) are positive and differentiable, an actual solution must further satisfy

\[
\boxed{\quad
T=\frac{B(1+s)kz^2}{1+2(1+k)(\xi+\eta)/3}
\left[\frac{\xi'^2}{9\xi}+\frac{\eta'^2}{12\eta}\right].\quad}
\tag{8}
\]

At zero amplitudes this formula needs an actual smooth signed square-root continuation; its apparent 0/0 may conceal a nonzero field derivative. No smooth square-root theorem is inferred from pointwise nonnegativity. The baseline metric regularity ensures the algebraic quantities, but does not automatically supply the differentiability needed for (8) or reconstructed transverse Euler equations.

Even (5), (7), and (8), plus the full metric and z equations, are not a demonstrated sufficiency theorem for the complete action. The two remaining equations, with normalized kinetic coefficients above, are

\[
\begin{aligned}
E_x/f_0={}&2h_xLx+2Bh_x' x'
-B(\partial_xh_x)x'^2-B(\partial_xh_y)y'^2-2A_xx,\\
E_y/f_0={}&2h_yLy+2Bh_y' y'
-B(\partial_yh_x)x'^2-B(\partial_yh_y)y'^2-2A_yy.
\end{aligned}
\]

They must vanish individually. The radial Noether identity supplies only \(E_z z'+E_xx'+E_yy'=0\); once E_z vanishes it is one contraction of two remaining equations. A contraction cannot replace both equations. Constant nonzero transverse coordinates also have zero transverse kinetic density but positive transverse potential; kinetic equality alone cannot select zero coordinates.

## 5. Limits, counterchecks, and exact evidence

A failed trial in (5) excludes that trial from this supplied static radial material-vacuum solution class. It does not exclude all parameters or all scalar theories. Passing it is a necessary admission gate, not existence, uniqueness, stability, global completion, sector selection, state selection, or observation agreement. If \(d_{\rm met}=0\), the undivided angular-time equation must be used and this chart inversion is unavailable. If \(w_C\le s\), z is not an admitted positive coordinate. The limits k→0 and H_v→0 destroy or alter square reconstruction and are outside the strictly positive supplied domain. The calibration/derivative/noise problem for an actual metric remains entirely open here.

`independent_controls_v1.py` performs 34 exact symbolic/rational checks, with 34 passes and zero failures. It verifies the two kinetic derivative factors, logarithmic potential derivatives/gap, complete metric reconstruction from the two null differences, radial derivative identities, simplified residual, envelope remainders and inverse, squared-field kinetic identity, and domain/wrong-sign witnesses. No author code, aggregate, data or ODE is run.

A separate rational local algebra fixture uses k=1/10, a=117/400, s=110/7, z=1, H_v²=1/100, x²=4, y²=9. It gives A_x=117/7000, A_y=39/3500, ell_x=388/117, ell_y=4, Delta=117/700 and E=109/175; the inverse recovers exactly the two squares and both envelope inequalities are strict. It is explicitly an algebra fixture, not an independently constructed vacuum spacetime solution.

One discarded scratch expression mixed coordinate kinetic density with physical kinetic density and omitted B in the radial source. The corrected (4) uses T=B(h_xx'^2+h_yy'^2). The controls preserve a diagnostic witness: using coordinate density tau=3/7, B=3/5, z=2, the incorrect `-2 tau/z` differs from `-2 B tau/z` by -6/35. That error is not present in the frozen formulas or code. Below-lower and above-upper envelope witnesses give a negative reconstructed potential piece, as required. No failed numerical run or tolerance adjustment occurred.
