# Exact staggered parities of the full native pair law

Fix the actual supplied full-site H0=S+mu Ddiag+W with mu,tau>0 on an even
cubic torus L>=6. Coordinates x_i are integers modulo even L. Define

    U_i=exp(i pi sum_x x_i n_x), i=1,2,3.

They are commuting Hermitian involutions and preserve every number sector.
No branch, pair matching or low-density projection is involved.

For the literal annihilators,

 U_i b_x U_i*=(-1)^(x_i)b_x,
 U_i d_j(x) U_i*=d_j(x),
 U_i v_ab^(s,t)(x) U_i*=(-1)^(1_{i=a}+1_{i=b})v_ab^(s,t)(x).

For axial endpoints their coordinate sum is2x; for a plane pair the extra
sum is s e_a+t e_b. Its parity is independent of s,t and of x. Modulo-even-L
wrapping preserves these statements at every seam. Consequently both QE
components have character+1, and each QT_ab has the displayed character,
independent of its center. Every original gradient square is invariant,
as are each axial S square and each plane S difference square. Ddiag is
diagonal. Therefore

                       [H0,U_i]=0.                         (P1)

This is a literal full-carrier symmetry, with the actual coherent channel
signs and shared centers. Expanding an original square is optional, not a
replacement model.

Let T_i translate by one site in direction i. Translating the coordinate
sum changes it by plus or minus N and a multiple of L times an integer
boundary-plane charge. Hence

       T_i U_j T_i*=(-1)^(N delta_ij) U_j.                (P2)

In an odd-N sector take any simultaneous eigenvector of H0,T_1,T_2,T_3;
translations commute, so such a basis exists inside every eigenspace. The
vectors

       U_1^s1 U_2^s2 U_3^s3 psi, s in{0,1}^3,

have exactly the same energy, charge and norm, but translation eigenvalues
z_i(-1)^si. These eight momentum triples are distinct and therefore the
vectors are orthogonal. Every odd-N eigenvalue has multiplicity at least8.
This includes the canonical ground and remains true for H0-nu N. More
generally, on a rectangular torus each even-length axis contributes one
such independent doubling. No doubling is asserted from an odd-length axis.

The scalar chemical potential and arbitrary diagonal occupation potentials
preserve(P1), but a nonuniform potential generally destroys(P2)'s use as a
spectral symmetry because it destroys translation invariance. Translation
is retained in the theorem.

## Exact boundaries

This is only a discrete dipole parity. Continuous dipole conservation is
false. For disjoint axial pairs d_1(0) and d_1(e_2), the full offdiagonal
pair coefficient from W is

 <d_1(e_2)*Omega,H0 d_1(0)*Omega>=-2tau/3.                  (P3)

The onsite S and diagonal terms cannot connect these two different axial
centers; the only connecting gradient has sum_A u_(A1)^2=2/3. The total
coordinate sum changes by2e_2. Thus a continuous linear phase exp(i alpha
sum_x x_2 n_x) changes this matrix element by exp(2i alpha). Dipole-U(1) LSM
papers requiring all linear phases are not applicable. The exact discrete
parities correspond only to alpha=pi.

On odd L the parity proof fails at a real row, not just a coordinate convention.
Take d_1(0) with endpoints e_1,(L-1)e_1 and d_1(e_1) with endpoints0,2e_1.
They are disjoint for L>=5. Their coefficient is again-2tau/3, while their
first-coordinate sums have opposite parity when L is odd. Thus the naively
defined U_1 does not commute with H0 on an odd torus. This is an exact negative
control for the geometry hypothesis, not a statement about its spectrum.

The existing odd-N lower bound H0>=a/72 (a=min(tau,mu/12)) is an absolute
energy bound and is compatible with this degeneracy. It does not bound an
odd-particle excitation above an extensive finite-density state. The new
symmetry argument also does not do so.

All eight partners have identical expectation values for every diagonal
occupation observable, since each such observable commutes with U_i. This
fact does not say their offdiagonal matrix elements vanish. It does show
that their mere existence does not guarantee distinguishable density means.
The actual N=1 sector provides a decisive limit: H0=mu I there, so the whole
sector is ground space and every positive-energy density spectral measure,
with the FULL ground projection removed, is zero. Thus(P1)-(P2) cannot alone
be interpreted as a local positive-frequency density mode or sound.

## Closest matched prior

The main Sep21 note on eight species and site-sign/coin maps proves a different
single-walker coin symmetry. Its varying-field antiunitary doubling and formal
corner-label orbits do not imply this many-body occupation-parity algebra.
That complete note was read, including its explicit warning against treating
formal branch labels as eightfold eigenspace degeneracy. Here the eightfold
statement follows from eight distinct exact translation eigenvalues at odd N.
No worldwide novelty claim is made for the elementary projective symmetry
argument.
