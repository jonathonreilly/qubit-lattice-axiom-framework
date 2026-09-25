# Adding a reference excitation to the original charged probe: actual energy

Personal root derivation, 2026-09-24. Sealed author candidate before independent
reconstruction. Conditional on the same supplied common matter/field law and
original instrument; no physical particle identification, new apparatus,
axiom, absorption mechanism or finite laboratory prediction is adopted.

## 1. The missing identification tested here

The earlier optical-band analysis constrains REFERENCE oscillator energies.
A charged preparation is not an eigenstate or ground state of the full law.
We now compute the actual full-Hamiltonian mean increment between its supplied
one-reference-excitation and vacuum preparations. This does not measure an
implemented preparation's work or any postclick energy transfer.

Use the exact preparation of PR9143 (note SHA
14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b):
all A plus except d=(1,1,0),h=(2,2,0) minus, three B blockers at
(0,-1,0),(0,0,1),(0,0,-1) plus, and one further B plus at c=(1,0,0)
or e=(0,1,0). Its Gauss-consistent embedding is
J_-=(|m_c>V_com U_dc^-1-|m_e>V_com U_de^-1)/sqrt(2).
Use the same fixed common integer flow V_com in both arms and keep

    h_g=(g²/(2tau)) D+(1/(4tau g²)) H4,
    H4=-2 sum_{a<c, sharing a B neighbor} (F_c F_a P)* F_c F_a P.

The electric D, all original marks and actual postformation matter sectors
are retained. We evaluate input expectations, not a restricted evolution.
Let phi_0,g and phi_1,g be the normalized compact vacuum and one-particle
packets of the weak-field parent, with real eigenbasis f_r and

    Omega_r=sqrt(lambda_r),  sum |alpha_r|²=1,
    mu=sum |alpha_r|² Omega_r >0,
    d_zr=(z.f_r)/sqrt(2 Omega_r), chi_z=sum alpha_r d_zr.

The dimensionless reference energy is mu; in the chosen generator units
its frequency is mu/tau. An SI energy interpretation would add hbar.
Fix an even cubic torus L>=16. Take g->0 at each fixed L, tau and alpha.
All error constants below may depend on that graph and preparation.

## 2. Exact local magnetic compression

Let H4_empty be the all-A-plus, B-empty field block. The following is an
operator identity for angle multiplication on the initial field sector:

    J_-* H4 J_- - H4_empty = F(A),
    F(A)=4722 + sum_{z!=0} a_z exp(i z.A).                    (1)

There are 140 nonzero words, with a_z=a_-z>0. Every word is a contractible
integer circulation. The exact finite certificate has this distribution:

| a_z | number of oriented words | plaquette filling area l_z |
|---:|---:|---:|
| 1 | 22 | 1 |
| 1 | 6 | 2 |
| 2 | 110 | 1 |
| 85 | 2 | 1 |

The two coefficient85 words are the original probe plaquette p and -p.
Consequently sum a_z=418, F(0)=5140, and

    sum a_z l_z² = 436.                                    (2)

Every listed filling is an exact signed sum of elementary plaquette rows;
its area is its coefficient l1 norm, not a Euclidean area approximation.
The complete word and filling certificates are saved. Both sides8 and16
were evaluated; after unwrapping, their local polynomials agree exactly.
Only L>=16 is used in the stated uniform local construction.

Here is the exhaustive finite-algebra rule underlying the certificate.
For each unordered overlapping pair x,z, apply the two actual outward
hard-core hops F_x then F_z. A charge q leaving A along its stored A-to-B
edge contributes that edge's exponent -q. Carry each initial branch string
and its sign, group final matter words, and square their Laurent amplitudes.
The prepared contribution to H4 is minus that polynomial, because -2 is
multiplied by the preparation's normalization1/2. Subtracting the empty
block adds twice the corresponding empty-input norm polynomial. This is
exactly the pair form, and keeps interference only between identical final
matter words. No replacement of distinct outputs by coherent amplitudes
is made.

A pair contributes a difference only if an A center is one of the two
minus sites or its B neighborhood meets an occupied B site of either
branch. Otherwise it acts identically on both matter branches, its two
output matter families remain distinct, and its norm equals the empty
block. There are266 pairs in this active union. Their finite neighborhoods
can be unfolded inside [-5,6]^3; the vertices remain distinct for L>=16,
and all contributing paths use the same local adjacencies as the explicit
side16 certificate. Remote pairs cancel exactly, not approximately. This
establishes the same polynomial for all the stated sizes. The side8 control
is a separate finite check, not the proof of arbitrary-volume locality.

Divergence cancellation, conjugate coefficients, word lengths <=6, the
flat sum5140 and all filling equalities are checked with integer arithmetic.
Since6<L, these circulations have no harmonic winding. Initial zero electric
winding entails Haar harmonic-angle averaging; (1) survives that average.
We do not replace the full charged dynamics or its postbirth winding sectors
by zero angles. The prior flat coefficient5140 is a consistency control for
(1), not a derivation of its nonconstant coefficients.

## 3. Actual full-energy difference

Define the actual input mean difference

    Delta_g=<J_-phi_1,g,h_g J_-phi_1,g>
                 -<J_-phi_0,g,h_g J_-phi_0,g>.

On physical basis words, Gauss gives the exact electric identity

    D=sum_e E_e²-sum_{a in A} q_a(q_a-1).

Indeed the linear piece is sum_a q_a div E_a with div E_a=q_a-1.
In our two branches the final sum is4. J_-*D J_- is the average of
sum(E+s_c)²-4 and sum(E+s_e)²-4, where s_c,s_e are the two fixed integer
flow shifts. Matter orthogonality removes cross terms. The constant shifts
cancel in Delta_g. Vacuum and one-particle oscillator states have even
probability parity and zero first electric moments, even for complex alpha;
the smooth compact cutoff changes those statements only by exponential
tails. The electric contribution therefore tends to mu/(2tau).

For any contractible circulation z, Gaussian differentiation gives

    <exp(i g z.x)>_1-<exp(i g z.x)>_0
        =-g² exp(-g² v_z/2) |chi_z|²,
    v_z=sum_r d_zr².                                      (3)

The original initial block has H4_empty=constant-2sum_p(W_p+W_p*).
Because sum_p |chi_p|²=mu/2, its magnetic mean difference tends to
mu/(2tau). Inserting (1) and (3) yields the full result

    Delta_g = (1/tau)[mu - (1/4)sum_{z!=0} a_z |chi_z|²]
                     + O_{L,alpha,tau}(g²).                (4)

The compact normalization and cutoff-derivative corrections are exponential
up to fixed powers of g. Quadratic electric Sobolev moments of the compact
Hermite packets justify the unbounded expectation. Equation(4) does not
follow just from bounded characteristic-function convergence.

All a_z are positive, so the limiting mean increment is <=mu/tau.
There is no general equality with reference excitation energy.

## 4. An exact failure of the unrestricted photon-energy reading

Take the bright reference packet alpha=d_p/sqrt(v_p), which maximizes the
original selected mark's leading contrast. Then |chi_p|²=v_p,
mu=||c_p||²/(2v_p)=2/v_p, and v_p>=1/sqrt(3). The two coefficient85 words
alone give

    lim tau Delta_g <= 2/v_p-(85/2)v_p
                      <= -73/(2sqrt(3)) <0.                (5)

Thus adding this particular reference one-excitation LOWERS the actual
full mean energy of the supplied charged preparation for sufficiently
small g at fixed graph. This is an analytic counterexample to identifying
every reference creation with a positive-energy full-system photon.
It is not negative total energy, an instability of every state, or a
violation of energy conservation: the charged input is highly excited and
not the actual ground state. The changed reference packet changes its
magnetic preparation energy. No dynamical production protocol is asserted.

The broad preparation mean and variance found in PR9147 remain present.
Their common leading terms do not determine the order-one difference (4).
The full side16 Fourier control gives limiting tau Delta approximately
-32.1855 for this broad-band packet, but (5), not that floating number,
certifies the sign. This example cannot be advertised as an optical photon.

## 5. A positive low-reference-band mean-energy bridge

The same obstruction becomes small for a truly low-band packet. Suppose
alpha is supported on 0<Omega<=epsilon, 0<epsilon<=2. A nonempty band on the
cubic torus has L epsilon>=4. The integer-momentum cube estimate gives
N_epsilon/V <=27 epsilon³/64. For an elementary plaquette,

    sum_{Omega<=epsilon} d_pr²/Omega_r
      =(1/(2V))sum_{0<D<=epsilon²} D_xy/D
      <=27 epsilon³/128.                                 (6)

Here D=4sum sin²(k_mu/2), D_xy contains its x,y terms. This bound includes
both transverse polarizations with their exact Fourier norm; harmonic zero
modes are absent and the plaquette curl annihilates them.
Weighted Cauchy with mu=sum|alpha|²Omega and a filling of area l_z gives

    |chi_z|² <= mu l_z² (27/128) epsilon³.                 (7)

For clarity, apply weighted Cauchy to chi_z and then the triangle inequality
to the restricted vectors Omega^-1/2 d_p making up d_z. Every plaquette
has the same (6), including different orientations and positions.
Using (2), the actual added mean obeys

    (1-(2943/128)epsilon³) mu/tau
       <= lim_{g->0} Delta_g <= mu/tau.                   (8)

When its lower coefficient is positive, this is a quantitative positive
mean-energy increment near the reference energy. It is NOT a narrow
actual energy distribution, a transition line, invariant photon subspace,
absorption theorem, stable detector or positive-time count law. It compares
two supplied initial states and leaves their large apparatus energy spread.
A hard band is stronger than a mean-energy bound; rare ultraviolet tails
cannot simply be discarded to apply (8).

Only under the same separate physical photon/clock and archival cosmology
identifications as PR9124 would a hard optical ceiling E_lab imply
epsilon<6E_lab/E_QG,min. Equation(8) would then bound this LIMITING relative
mean discrepancy by (2943/128)(6E_lab/E_QG,min)^3. No finite-g error estimate
at the resulting tiny scale, no empirical confirmation and no stronger
statistical interpretation of that observational bound is supplied.

## 6. Scientific controls and scope stress test

The new author program evaluates the full local polynomial from pair norms,
with disclosed reuse of prior vertex/preparation and active-pair logic. It
does not import the earlier flat action certificate as a substitute for
link monomials. A separate program verifies all signed plaquette fillings
and evaluates finite Fourier overlap sums. Those sums are floating controls,
not interval enclosures. Band membership at an exact floating threshold is
diagnostic only; the analytic cube bound supplies the all-size inequality.
The finite-g rows evaluate uncut harmonic compression, not full compact
rotor propagation. All rows, including negative increments, are preserved.

N1: narrow-band photons, collective energy-selective matter, native bound
states, source preparation and other physical identifications remain open.
N2: mean-energy mismatch, broad variance and short-window count limits are
separate facts, not independent universal obstructions. N3: exact charged
preparation, hard reference band, fixed graph before g->0, Haar harmonic
fiber and supplied SI map are explicit. N4: we control full input mean
expectations with their domain, not a reservoir or transition ledger.
N5: (5) is a specific counterexample; it is not a framework no-go. N6: (8)
is the surviving positive low-band mean-energy bridge. N7: actual absorption
requires dynamics and physical source/detector identification beyond an
input expectation. N8: earlier reference count and energy results retain
their stated scopes; this resolves one previously uncomputed identification.
Independent reconstruction remains required before publication promotion.
