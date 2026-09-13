# A constructive escape from the first metric mismatch

Derived after preserving the first sigma1 mixing calculation; this is not a
retroactive change to its negative result. Nonzero mixing need not split the
four cone metrics. The direction of that mixing is a substantive parameter.

Let the onsite term be tau_x(m1 sigma1+m3 sigma3), write
m3+i m1=mu exp(i theta), and keep the original momentum-dependent terms.
Put L=2+zeta-cos ky-cos kz and t=cos kx. At ky=0 or pi,

q=det(B+i A)=L^2-2Lt exp(i b)+exp(2i b)-mu^2 exp(2i theta).

At a zero near the original four nodes (so L>0 and ky=0), its real and
imaginary parts after multiplication by exp(-i b) give

L^2=1-mu^2 sin(2theta-b)/sin b,
t=[cos b-mu^2 sin(2theta)/(2sin b)]/L.

The derivatives remain q_x=2 sin x L exp(i b),
q_z=2(c-i t sin b)sin z, c=L-t cos b. Their scalar product is
Re(q_x^*q_z)=4 sin x L sin z (L cos b-t).
Also

t-L cos b=mu^2 sin(2(theta-b))/(2L sin b).

Thus common metrics occur along two orthogonal onsite mixing directions
(theta=b modulo pi/2), not only at zero mixing. Generic nearby changes of
this angle preserve T and Mz but restore the off-diagonal metric contrast.
This exact statement is local to the simple four-node phase; no claim about
all large-mu roots or new phases follows from these local root expressions.

## Positive aligned family

Choose theta=b: m1=mu sin b, m3=mu cos b, R=sqrt(1-mu^2).
For 0<b<pi/2, 1/2<zeta<1, mu^2<1-zeta^2, the complete zero set is

kx=+-acos(R cos b), ky=0, kz=+-acos(1+zeta-R).

Indeed exp(-ib)q has imaginary part sin b(R^2-L^2). On ky=0 or pi,
L is strictly positive, so q=0 forces L=R and then t=R cos b.
For ky=pi, L>=2+zeta>1>=R, impossible. For ky=0, L>=zeta;
strict R>zeta gives the two nonzero z roots, and 0<R cos b<1 gives
the two nonzero x roots. At R=zeta, the opposite charges meet at z=0.
For mu^2>1-zeta^2 there are no zero-energy roots (including mu^2>=1);
the compact Brillouin torus then has a positive gap. This is an exact
single-particle spectral statement for this selected family.

At each node the nonzero spectator energies are +-2 sin x*. The two-band
metric is

G=diag(R^2,1,R^2 sin^2 b sin^2 z*/sin^2 x*).

One sees this without diagonalizing eigenvectors: q_x=2 sin x* R exp(ib),
q_z=-2i R sin b exp(ib)sin z*, so the cross term vanishes, and divide
|q_i|^2 by E_+^2=4sin^2 x*. The ky term anticommutes exactly with the
remaining Hamiltonian and therefore contributes one. The determinant is
strictly positive and chirality is sign(kx*kz) by continuity from mu=0.
All four metrics are equal in the same original coordinates. A common
coordinate normalization D=sqrt(G), y=a D^-1 n, gives a unit matter cone;
this does not select a dynamical photon metric or a physical length scale.

The momentum-independent commutant should be only the scalar identity for
mu!=0: coefficients of sigma2 and sigma3 force any commuting operator to
be flavor-only; the sin(kx) tau_z(cos b sigma1-sin b sigma3) term forces
it to commute with tau_z, and the nonzero tau_x mixing then forces it to
commute with tau_x. Thus no constant onsite change of basis restores two
independently conserved flavor copies. This needs a direct rank check as
an independent challenge, but the commutant argument is elementary.

Initial projected eigenvector challenges at three parameter triples and all
four nodes agree with the determinant-derived common metric at 2e-15 or
better. These checks followed the derivation and do not prove its whole range.

A second aligned direction theta=b+pi/2 is a live alternative with R=sqrt(1+mu^2)
and t=R cos b. Its small-mu four-node phase also has a common metric; it is
not needed to establish the positive family above and is not ruled out.

Native gauge dynamics, stability against interaction-driven symmetry breaking,
selection of the mixing angle, and protection of metric equality under generic
allowed renormalization remain open. No axiom update is forced by either the
first mismatch or its explicit constructive repair.
