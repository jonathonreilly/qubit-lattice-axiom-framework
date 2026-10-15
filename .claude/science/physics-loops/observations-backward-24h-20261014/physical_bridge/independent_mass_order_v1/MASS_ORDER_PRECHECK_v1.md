# Independent fixed-point clock-functional mass-order precheck

Reviewer `/root/localized_history_check`; root remains scientific author.
This derivation is frozen without reading the new physical_bridge author note or
any other reviewer's work. It uses only the assigned real free KG model and
physical temporal weights that stay identical when the mass changes. No formal
audit, physical fit or theory-wide no-go is claimed.

## Fourier normalization and spatial interference

Use unitary spatial Fourier convention (2pi)^(-3/2). The real energy Hilbert norm
is ||(h0,p0)||_mu^2=integral(|p0|^2+|grad h0|^2+mu^2|h0|^2)=2E.
For omega=sqrt(k^2+mu^2), write C_A(omega)=integral c_A(t) exp(i omega t) dt.
The cosine and sine parts provide the two initial-data representers. Taking their
real Hilbert inner product gives the energy-dual Gram for a scalar combination

    G_mu=(1/(2pi^2)) integral_mu^infinity (k/omega)
          sum_(A,B) Re[C_A(omega) conjugate(C_B(omega))]
          sinc(k r_AB) d omega,
    k=sqrt(omega^2-mu^2), r_AB=|x_A-x_B|, sinc(0)=1.

The angular identity is integral_S2 exp(i k n.(x_A-x_B)) dOmega
=4pi sinc(k r_AB). Before changing frequency, the radial measure is
k^2/(k^2+mu^2) dk; dk=omega/k d omega produces k/omega above.
Conjugate symmetry enforces real data and supplies no additional factor of two.
For a single point at mu=0, this reduces to G_0=||c||_2^2/(2pi), matching the
ordinary proper-clock temporal norm. Smooth compact weights make the integral
finite. The observation is initially defined on smooth fields and extended by
this bounded dual norm, not by assuming arbitrary energy fields have pointwise
traces. At zero mass use the usual homogeneous energy completion; the counter-
example below annihilates an added constant explicitly.

At each positive physical temporal frequency, define the real spatial matrix
M_mu(omega)=(k/omega)[sinc(k r_AB)], with M_mu=0 below threshold. Its massless
counterpart is [sinc(omega r_AB)]. The prefactor decreases with mass, but the
interference phases also change. Dropping this second change is unjustified.
For finite k, d/dk [k sinc(k r_AB)]=cos(k r_AB), including diagonal entries.

For collinear points, r_AB=|s_A-s_B| and [cos(k r_AB)] is the Gram matrix of
(cos(k s_A),sin(k s_A)). It is positive semidefinite. Integrating it from k to
omega proves M_mu<=M_0 at every frequency, hence G_mu<=G_0 for arbitrary fixed
temporal weights on a finite collinear array. One or two points are special
cases. The same cosine-of-distance matrix need not be positive semidefinite for
noncollinear arrays.

## Concrete noncollinear counterexample, with zero sum at every time

Take three points

    x1=(-3/4,0,0), x2=(3/4,0,0), x3=(0,sqrt(7)/4,0),
    a=(1,1,-2), c_A(t)=a_A f(t).

The distances are r12=3/2 and r13=r23=1. The sum of all three weights vanishes
identically, not only after integration. Thus sum_A integral c_A=0 exactly and
a spatially uniform field history cancels pointwise. No constant-background
selection is used to manufacture the comparison.

For this vector, the frequency factor is

    q_mu(omega)=F(k)/omega,
    F(k)=6k+(4/3)sin(3k/2)-8 sin(k),
    q_0(omega)=F(omega)/omega.

At omega0=2pi, choose mu=pi sqrt(23)/6, so k0=11pi/6. Then

    q_0(omega0)=6,
    q_mu(omega0)=11/2+2/pi+sqrt(2)/(3pi),
    q_mu(omega0)-q_0(omega0)=-1/2+2/pi+sqrt(2)/(3pi)>0.286.

This reverses the claimed mass ordering at a real spatial contrast that already
annihilates constants. The derivative F'(2pi)=6+2cos(3pi)-8cos(2pi)=-4 also
locates the failure directly: reducing spatial wavenumber there increases the
quadratic response. It is spatial interference, not a change of temporal weights.

## Explicit smooth compact temporal weight and strict margin

Let T=40 and first consider g(t)=exp[-t^2/(2T^2)]cos(omega0 t). Define a smooth
cutoff using b(z)=exp(-1/z) for z>0 and b(z)=0 otherwise,
q(z)=b(z)/(b(z)+b(1-z)) for 0<z<1, q=0 for z<=0 and q=1 for z>=1. Put

    chi(t)=1-q(|t|/T-8),
    f(t)=chi(t) g(t).

The cutoff is one for |t|<=320, zero for |t|>=360, and smooth at all joins; the
absolute value causes no issue in its constant neighborhood of zero. Thus f
and every c_A are real C-infinity compact functions. The same f is used for
both masses. Their exact zero-sum property does not depend on f having zero mean.

A direct analytic margin avoids relying on a monochromatic distribution or a
numerical sign. On I=[2pi-0.1,2pi+0.1], k lies inside [5.64,5.88]. In both the k
and omega intervals, -4<=F'<=0: cos(k)>.75 and cos(3k/2)<0, with the analogous
bounds near omega=2pi. Also k'=omega/k<1.14, hence
|(F(k)-F(omega))'|<8.56. At the center |F(k0)-F(omega0)|<1.81. Therefore on I

    |[q_mu-q_0]'| < 8.56/6.18+2.666/(6.18^2) < 1.456,
    q_mu-q_0 > 0.286-0.1*1.456 > 0.13.

Globally each q is a nonnegative angular average of
|sum_A a_A exp(i k n.x_A)|^2, multiplied by at most one. Thus 0<=q<=16 and
q_mu-q_0>=-16, with the massive factor zero below threshold.

The unnormalized temporal transform of g is

    G(omega)=sqrt(2pi) T/2 *
      [exp(-T^2(omega-omega0)^2/2)+exp(-T^2(omega+omega0)^2/2)].

Its positive-frequency squared norm is
I_all=pi^(3/2)T[1+exp(-T^2 omega0^2)]/2. The fraction outside I is at most
2 erfc(4)+erfc(T omega0)<3.2e-8, using (a+b)^2<=2(a^2+b^2) and the Gaussian tail
bound erfc(x)<=exp(-x^2)/(x sqrt(pi)). Consequently

    G_mu(g)-G_0(g)
      >= I_all/(2pi^2) [0.13-(16+0.13)*3.2e-8] > 0.7.

The cutoff changes the time-domain L2 norm by at most

    delta=||f-g||_2 <= [T exp(-64)/8]^(1/2) < 3e-14.

For these a_A, each quadratic operator on a common temporal f has norm at most
16/(2pi). Hence the change of the difference of its two quadratic forms is at
most (16/pi)(2||g||_2+delta)delta < 1e-10. The explicit compact f therefore still
has G_mu(f)-G_0(f)>0.7-1e-10>0. All constants here refer to the stated energy-norm
and Fourier conventions. This is a finite smooth compact counterexample, not
just a narrow-band heuristic or a plane-wave state.

For even f, the mass-specific real Riesz data can also be displayed:

    h0hat_mu(kvec)=(2pi)^(-3/2) C(omega)
                    sum_A a_A exp(-i kvec.x_A)/omega^2,
    p0hat_mu=0.

They obey conjugate symmetry and finite energy; their squared energy-Hilbert
norm is the derived G_mu. The zero spatial sum also improves the low-frequency
behavior at zero mass. No observed field is thereby selected.

## Independent checks to execute

Implement both angular integration of the finite spatial array and its sinc
matrix, check the exact distances/frequency values and the scalar counterexample,
and numerically integrate the explicit packet. Use a direct temporal quadrature
of the compact smooth f for an independent transform check, compare with the
analytic Gaussian transform only with the explicit cutoff-tail error, and test
spatial/angular resolution independently. Preserve the analytic strict lower
bound separately from floating numerical products. Check real-data symmetry,
collinear/two-point ordering and a deliberately incorrect massless spatial phase
substitution. No author source or other review is needed.

## Scope distinction

The result refutes a universal massless upper-Gram claim for general multi-point
clock functionals, even with exact constant cancellation. It does not refute the
specific ideal two-way coherent-count fixture: its physically derived weights,
geometry, force contributions, shared clocks and allowed contrasts are additional
constraints. In particular a pure clock functional at two fixed points is
collinear and obeys the clock-only ordering above. A coherent joint clock/force
operator requires its own calculation; this result neither proves nor disproves
its ordering by analogy. There is no claim about all scalar theories, actual
radio data, nonlinear observables or an empirical exclusion.
