# Independent review: moving-geometry nonlinear Euler extension and quantitative corollary

## Finding and review boundary

No actionable mathematical defect was found in the independently reconstructed
arguments under their stated hypotheses. The proof uses the actual evolving
geometry marginal, exact owner-block weights, a deterministic local tensor
boundary estimate, and conditional color mixing. It does not assume a
stationary or isotropic matching law. The quantitative corollary supplies
conservative sufficient bounds, with different fixed-time and time-supremum
rates.

This is selective scientific source review, not a formal audit, retention
decision, independent authorship claim, or verification of a physical
interpretation. New proof steps were reconstructed before opening author
controls. Previously checked rate definitions, nonlinear flux/entropy algebra,
and elementary permutation comparison were reused only at bound identities.

The complete qualitative note was read at SHA-256
`939c87d2d4688e3f4e66550d3a54e024966866b8744db80d4befd3f1d68317d1`.
The complete quantitative addendum was read at
`0671866c54f6f1865e3c63b8b4377800c85bf27303b7f28eca8a7d425b76c1ed`.
All source paths and byte identities are recorded in the manifests and final
seal. No primary files, Git state, PR, audit status, or earlier review packet
were changed.

## What has been proved conditionally

Take even cubic tori, fixed positive routed-rate floor, fixed bounded
plaquette rate, autonomous matching evolution, and the supplied strictly
positive periodic C3 solution of the fourteen-color conservation law on a
fixed time interval. Let the initial color law have conditional relative
entropy h_N(0)=o(K) against the profile product, where K=N^3/2. The reference
geometry marginal is the actual marginal rho_N(t). Then the argument proves
uniform-time convergence of h_N(t)/K to zero and of smooth empirical color
tests to the supplied solution, uniformly over initial geometry laws.

The added comparison gives, with r_N=h_N(0)/K+N^(-1/7),

    sup_t h_N(t)/K <= C_T r_N,
    sup_t E|Z_N(t)|^2 <= C_T r_N,
    E sup_t |Z_N(t)|^2 <= C_T r_N^(2/3).

The last two statements concern different quantities. Exact conditional
profile-product preparation gives the sufficient exponents 1/7 and 2/21,
respectively. The constants may depend on the fixed profile bounds, rates,
time interval, and test. The argument makes no useful finite-size threshold
or optimality claim. It is an asymptotic bound along even N.

## Reconstruction of the new proof steps

**Actual geometry marginal and conditional entropy.** Write
mu(M,c)=rho(M)pi(c)f_M(c), with pi the uniform color product. An autonomous
geometry mark takes (M,c) to (M',P c), at a color-independent rate a.
Consequently rho(t)pi solves the full joint forward equation: routed color
dynamics annihilates pi at every M and each geometric permutation preserves
pi. For positive marginal masses the mark's contribution to H0' is exactly

    -a rho(M) KL(pi f_M || pi(f_M' composed with P)) <= 0.

Finite-state log-sum contraction extends this statement through zero geometry
masses. Adding the routed contribution proves the stated integrated bound
K log(14)/(2Nr_*) on the averaged bare color Dirichlet form. This explicitly
includes the derivative of rho(t); no assumed stationary geometry density is
differentiated or discarded. Conditioning is at the current time, not on a
future geometry history.

**Owner cubes and count conditioning.** An owner appears in exactly
w_L=L^3+L^2 translated physical cubes, because the two endpoint-origin sets
each have size L^3 and their intersection has size L^3-L^2. All N^3 physical
origins are included. Thus sum m_z=K w_L, with L^3/2<=m_z<=L^3, and the
weights omega_z=m_z/w_L sum to K even when block sizes vary with geometry.
The image of the physical cube graph under pair ownership is connected;
each nonloop is an actual routed swap. Parallel physical images are retained.
At fixed block size, the finite family of connected graphs and count sectors
has a positive minimum gap. An internal physical edge occurs in exactly
L^3-L^2 cubes, giving the claimed full-form normalization.

At fixed M, exterior colors and block counts, the reference law is uniform
on arrangements. The square-root-density Cauchy-Schwarz/Poincare estimate
then applies to each centered bounded block current. The further average
over rho is a probability average, so it introduces no factor counting
geometries. Summed and time-integrated with the preceding dissipation, this
is the required K C_(L,T)/sqrt(N) qualitative replacement estimate.

**Rough routing tensor.** The displacement a_delta(u) is kept inside the
current average. Nonfixed route cycles have length at least N/2, so their
four contexts are distinct for N>=8 and remain at bounded distance. Four
draws without replacement differ from product sampling by O(1/m_z).
Fixed routes have zero displacement. A bounded-width strip accounts for
all excluded contexts.

For each matching, q_delta moves points at most two steps. Thus
q_delta(B_z) differs from B_z only at O(L^2) anchors. Substitution in
T_z=(1/2)sum_delta,u a_delta(u) tensor delta cancels the leading
sum_B d_M(v), using sum_delta delta=0, and gives T_z=m_z I+O(L^2).
No pointwise tensor identity or matching isotropy is true or needed. An
explicit sufficient independent bound is ||T_z-m_z I||_F<=54L^2 for
L>=16. Dividing by the owner weights gives the source's O(1/L) boundary
error; canonical and smooth-coefficient errors have the stated orders.

**Actual immutable plaquette marks.** Direct tracking of four distinct keys
in both square orientations confirms that the two rate-nu rotation marks
both flip geometry, while one swaps the two black-position colors and one
acts as their identity. Hence geometric flip rate is 2nu and color drift
has only one rate-nu swap term. Its coefficient and flippability depend on
M alone. The difference of two indicator vectors has exactly zero mean
in every uniform count sector. Boundary truncation and conditional mixing
therefore remove its integrated Euler contribution. Individual realized
plaquette currents need not vanish.

**Weighted entropy closure.** The identity
h=H0-E_mu Theta-K log(14) accounts for the full nonstationary reference.
Owner-block weights are introduced at each time algebraically; no random
block time derivative is taken. Exact coverage transfers any smooth scalar
sum to the black-site Riemann sum with O(KL/N) error. The constant entropy
term integrates a divergence, and the linear term cancels on the simplex
tangent by the checked PDE/symmetrizer identity. The residual is bounded
by C sum omega_z |pbar_z-p_z|^2.

Owner overlap can be colored with chi=32L^3 slots for L>=16. Conditional
on every M, disjoint owner blocks have independent comparison colors. The
fourteen-coordinate bound E exp[(m_z/14)|pbar_z-Epbar_z|^2]<=29 and the
fixed alpha=1/1792 satisfy 2alpha chi=L^3/28<=m_z/14. Holder's inequality
and sum omega_z=K give the displayed exponential bound, uniformly in M;
averaging any rho preserves it. The Gronwall coefficient multiplying h/K
is independent of L. Fixed-L then large-N and finally large-L limits prove
the qualitative statement. Bounded empirical drift and the O(1/(NK))
martingale bracket justify the separate uniform-time conclusion.

**Even-cube quantitative transfer.** Coordinate-ordered paths in any embedded
cube have length at most 3(L-1), and an edge at cut a has exactly
2a(L-a)L^2 ordered all-site path uses, at most L^4/2. Choosing distinct
inside representatives of owners, contracting matching edges and erasing
loops preserves those upper bounds. A simple owner edge has at most two
physical representatives. The endpoint-only transposition word has length
at most 6L and uses each path edge at most twice. In the stated bare
Dirichlet convention this gives D_all<=12L^5 D_simple. Combining the
previously checked Var<=(2/m)D_all with m>=L^3/2 gives
g_L>=1/(48L^2). Even side length introduces no additional hypothesis.

Normalized currents have geometry-uniform bounded size. The only growing
Poincare factor is g_L^(-1/2); internal-form coverage is O(L^3), while
global integrated energy is O(K/N). Hence replacement per pair is
C_T L^(5/2)/sqrt(N). Boundary, canonical, coefficient and mean-shift
constants carry exactly the other L dependencies displayed in the note.
Choosing even L of order N^(1/7) balances this error with 1/L and keeps
the required L>=16, N>10L eventually. No hidden geometry-count or
overlap-coloring factor enters Gronwall.

**Two empirical bounds.** For signed real test weights |phi|<=B, the
variable phi I has range length |phi|. The correct product tail is
2exp(-2Kz^2/B^2); integrating it gives Eexp(KW^2/B^2)<=3. Entropy
inequality plus the Riemann error yields the stated fixed-time mean-square
bound. Removing the empirical martingale leaves a pathwise Lipschitz
process. A time mesh gives C[(r_N+1/(NK))/delta+delta^2]; taking
delta=r_N^(1/3) proves the separate r_N^(2/3) supremum estimate. No
independence between time samples is assumed.

## Independent controls and countercontrols

The qualitative checker used three irregular owner cubes with N=180,L=16,
all 32,120 bounded route stencils represented in the saved rows, complete
contracted-graph connectivity and exact tensor sums. The detailed counts
are 10,315, 11,450 and 10,355 nonfixed four-context checks. A separate
N=12,L=4 all-origin enumeration verified the exact coverage with variable
m_z; that small control checks combinatorics, not the theorem's L>=16
condition. The rough-matching fixture is a finite deterministic sequence
of legal flips, not a kinetic simulation or phase screen.

The 392-state isolated plaquette projection was assembled independently.
It checks the evolving reference equation, the full conditional-entropy
derivative against its negative-KL expression, and finite-time contraction
for both nonstationary positive and point-mass initial geometry marginals.
The derivative was -0.9872993392171526 in the selected nonstationary case;
the reference forward-equation residual was below 4.4e-19. These numerical
controls supplement the exact general calculation, rather than prove it.

The addendum checker counted every ordered coordinate path in even cubes
L=2,4,6. Maximum physical-edge loads 8,128,648 equal L^4/2. A separate
irregular N=48,L=4 owner cube checked all 1,035 endpoint words; maximum
weighted comparison load was 1,381 against the sufficient 12,288 bound.
Exact algebra checks the permutation-induction slack and all rate powers.
A nonidentical six-site product with signed weights gives exponential-square
moment 1.0656585 below 3; a correlated tilt satisfies the resulting entropy
bound. Formal enormous N=L^7 examples are arithmetic checks only.

Three countercontrols preserve the needed distinctions. A rough matching
violates the pointwise tensor identity. Color-dependent geometric rates
increase initially zero conditional color entropy, so autonomy cannot be
dropped. Finally a randomly located Lipschitz triangular bump has
fixed-time second moment 2d^3/3 and time-supremum square d^2; fixed-time
O(r) alone cannot imply time-supremum O(r). A separate exact binomial tail
rejects an erroneous factor 8K in place of the correct 2K Hoeffding exponent.
These are scoped countercontrols, not counterexamples to the stated theorem.

Both pre-comparison first executions and the selective comparison succeeded.
No independent failed attempt was discarded.
Runnable sources, complete output, empty stderr and command receipts are
retained. Full derivations are in INDEPENDENT_DERIVATION.md and
ADDENDUM_DERIVATION.md.

## Pre-comparison and final-source evidence

The qualitative pre-seal predates access to both the quantitative addendum
and all new author controls:
`PRE_COMPARISON_SEAL.json`, SHA-256
`2f689daecd524cd8d794705d868fa25f079718c1ca0b3587b358bb832d2d358d`
(7 sources, 7 artifacts).

The separate addendum pre-seal predates all new author controls:
`ADDENDUM_PRE_COMPARISON_SEAL.json`, SHA-256
`2d483da8b77733716081012126b6b4d30fa62d5ebf7d77fbd1e389171c7766f9`
(3 new sources, 7 artifacts, all 14 prior bindings authenticated unchanged).

The complete final author checker, complete results, both run streams and
receipt were read and authenticated at the supplied identities. The checker
is `dimer_moving_nonlinear_check.py`, SHA-256
`2000fcf382ab9eeb833d8d67d608776017a37c9848c29263dee32c06f5038052`;
the results are `dimer_moving_nonlinear_checks/RESULTS.json`, SHA-256
`9248bcdc11b78f955d90ea0710bc228ce37b4d1ab38eb6037024d0301ef30cc0`.
All six embedded source bindings agree. Its three groups cover conditional
geometry entropy, owner-block identities, and the exponential constants.
There is no separate author checker for the quantitative corollary; that
argument and the independent addendum controls above are its reviewed support.

The selective post-seal checker imports no author module and does not run
the author suite. It assembles the author's 392-state entropy fixture with
an independent sparse row generator; all reported entropy values agree to
5.6e-17, including the actual-marginal correction and the autonomy
countercontrol. It independently reconstructs all twelve saved selected
block rows across the three fixture cases: matching counts, contracted
connectivity, exact tensor residuals and six image-boundary counts agree.
It also checks every saved exponential-constant row exactly. The complete
all-origin extrema/coverage loops in the author results were authenticated,
not repeated. The corresponding identities have independent proofs and
separate controls above. The author explicitly distinguishes its small
N=12,16 local-geometry controls from the theorem's L>=16,N>10L range.

The preserved failed author fixture was also inspected: initial checker
SHA-256 `9e50a523f96c1ee5ac4fd76e9fc6cce1f164553acdad16333deda17858a55577`,
diagnosis `1fd32fc154a2011f8076e0720d66f713eb6cd67f64bec4fdf54931b0e1aa886c`,
return code 1 and complete traceback retained externally in its declared
development directory. Byte reconstruction verifies the only changes are
initializing attempted-flip fixtures from columnar rather than frozen winding
geometry and requiring an accepted flip. No mathematical assertion, grid,
seed or threshold was removed. Independent fixture reconstruction confirms
zero accepted flips from the old winding state and 1,737/4,115 in the two
corrected rough fixtures. This is a corrected test-coverage failure, not a
failure or repair of the primary theorem. No source/prose drift or new
actionable issue emerged from the comparison.

`COMPARISON_RESULTS.json`, complete logs and its receipt record this bounded
coverage. Both pre-comparison seals and all their rows were authenticated
unchanged. `FINAL_SEAL.json` binds the final report, all independent
artifacts and the exact reviewed sources. Author output authentication is
kept distinct from the independent proofs and selective recomputations.

## Limits

The smooth interior continuum solution and entropy-close inhomogeneous color
preparation are supplied. No existence time, shock continuation, boundary
profile theorem, birth-generated inhomogeneous preparation, full microscopic
total variation, fine-key/projector statistics, nonlinear geometric-Gauss
evolution, or quantum realization is established. Geometry may be arbitrary
and nonstationary, but its transitions must remain autonomous, bounded, and
the specified color permutations. These arguments do not extend by analogy
to color-dependent geometric rates. The quantitative exponents are upper
bounds from this comparison, not measured kinetics or optimal exponents.
