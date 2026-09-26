# Independent moving-geometry reconstruction before author controls

Reviewed note SHA-256:
`d7e0ed4f6dfc8ef8e5ccd6c9382643a2df5013ba4cb9c73f47bcb23b40dbade3`.
The complete note was read. The corrected routed theorem, its independent
proof assessment and the preparation theorem/check are reused at the
identities in `PRE_COMPARISON_SOURCES.json`. No new moving-geometry author
checker/results or dynamic aggregate has been opened.

## F1: qualify the scalar speed and mode count by orbit isotropy

The arbitrary fixed full-support p matrix-propagation statement is supported
by the reconstruction below. The following specialization in Section 1,
lines 40–42, additionally needs

    p_a=rho_A/6 on A,  p_a=rho_B/8 on B,

as required in the preceding routed note. Positive orbit masses alone do not
give four propagating and nine static modes. At gamma=1, take
p(A+x)=3/28, p(A-x)=1/28 and every other p=1/14. This is full-support with
rho_A=3/7,rho_B=4/7, but X=(1/14,0,0), Y=0. Symbolically differentiating
the supplied current and restricting it to the probability tangent gives,
for direction e3, the monic characteristic polynomial

    z^5(14z-1)^2(14z+1)^2(196z^2-17)(1372z^2-103)/10330523392.

There are eight nonzero real eigenvalues, counting multiplicity, and five
zero ones. The actual mode Q=2pi e3 multiplies all eigenvalues by 2pi and
does not change these counts. The exact entropy covariance identity
A C=C A^T also holds in this example. The isotropic positive control has
polynomial z^9(7z-2)^2(7z+2)^2/2401, as expected.

`mode_scope_countercontrol.py` constructs the current symbolically rather
than inserting a guessed characteristic polynomial. The narrow requested
repair is to restrict the scalar wave-speed and four/nine count sentence
to orbit-isotropic probabilities, preserving the arbitrary-p matrix theorem.
At gamma=0 all thirteen modes are static for every p, so that degeneration
does not need the extra restriction. Root has agreed to this scope repair
and kept the reviewed source frozen for the pre-comparison seal.

## 1. Actual records, matching and the color projection

Index square corners cyclically 0,1,2,3, with black corners 0,2. If the
initial dimers are (0,1),(2,3), put the first pair's antipodal records at
0,1 and the second pair's at 2,3. A clockwise cyclic permutation sends
the dimers to (1,2),(3,0); a counterclockwise permutation does the same to
geometry. Every individual record has moved one edge without changing its
content. Clockwise followed by counterclockwise restores every record.

At the black vertices, one sense swaps the two pair colors and the other
leaves them in place. Starting with the other matching orientation reverses
which sense swaps. Reversing the temporary black class also preserves the
one-swap/one-identity conclusion. This uses the **antipodally even** color
map: changing which member of a pair is at the black endpoint does not
change its color. It would not justify the same projection for an arbitrary
odd readout of the individual projector.

Thus two rate-nu channels give geometric rate 2nu but color-observable drift
nu(F after swapping the two black colors-F). The identity color channel
still moves records and geometry. It cannot be deleted from the physical
process simply because its color increment is zero.

The geometry generator is autonomous: flippability and both rates depend
only on the matching. Its clock/rotation-mark history can therefore be
sampled independently of the initial colors and routed-exchange random
drivers. Conditioning on that entire marked history leaves deterministic
matching intervals and prescribed, invertible permutations of black colors.

## 2. Conditional invariant law and the switched energy estimate

Fix such a finite marked history on [0,T]. Every interval generator L_m
preserves the same product measure pi_p and, separately, the uniform law
on each global color-count sector. Every prescribed boundary permutation
also preserves these measures. Starting with pi_p makes the conditional
one-time color law pi_p at every time. Initial geometry need not have an
invariant distribution. The conclusion is one-time independence of colors
from the entire marked geometry history, not independence of their paths.

All full-matching routed graphs are connected. Hence their symmetric parts
have the common kernel consisting of global-count functions. For an F_m
orthogonal to this kernel, choose the mean-zero sector solution
-S_m f_m=F_m. On each interval [a_m,b_m], define exactly the note's forward
martingale increment and the backward increment using L_m*.

The conditional reversed process exists as the finite composition of
adjoint interval semigroups and inverse boundary permutations: the same
stationary color measure occurs at both ends of every factor. Consequently
the backward expression is a true martingale increment for the reversed
conditional filtration. The forward increments are orthogonal in increasing
time order; the backward increments are orthogonal in decreasing time order.
The deterministic f_m may change at every interval. Given the marked history,
they are prescribed functions, not functions chosen from future color data.

Writing A=sum M_m^+ and B=sum M_m^-, endpoints cancel **within each interval**,
so A+B=2 sum integral F_m. Uniform conditional one-time laws give

    E|A|^2 = E|B|^2 = 2 sum_m length_m <f_m,-S_m f_m>.

Using |A+B|^2<=2|A|^2+2|B|^2 proves

    E|sum_m integral F_m|^2
        <= 2 sum_m length_m ||F_m||_{-1,S_m}^2.

There is no telescoping across unequal f_m, no derivative of f_m at a
geometry switch, and no multiplier involving the number of switches.
The finite torus has finitely many geometric events almost surely on each
finite microscopic interval, including [0,Nt]. Averaging the conditional
bound is legitimate. Complex observables are handled by real and imaginary
parts, or by the corresponding complex Dirichlet form.

A nonstationary **color** entrance cannot be silently substituted in this
identity. The independent two-state countercontrol has stationary law
(100/101,1/101), starts at its rare state, and gives integral second moment
0.1801625794 at t=1/2 against the misapplied stationary bound 1/101. This
does not contradict the note: its reference colors are conditionally
stationary, and Section 6 separately transfers from prepared nonstationary
entrances. Nonstationary geometry is allowed and is a different issue.

## 3. Routed-current replacement with changing geometry

For the centered current remainder, the local canonical conditional
expectation leaves it orthogonal to every global-count function. The
previous fixed-matching H-minus-one bound is uniform over matching patterns
and bounded deterministic Fourier-gradient coefficients. On each conditioned
geometry interval these data are deterministic; the switched estimate gives
the same O(A_l l^3/N) accelerated integrated bound. Explicitly, the macro
integral is N^-1 times the microscopic integral over [0,Nt].

The other replacement estimates use only product color independence at
one time, finite block overlap and uniform geometric boundary sizes. These
properties hold conditional on the history. Cauchy--Schwarz in time bounds
their integrals without any temporal independence assumption. The q_delta
and d_u cancellation is an identity at the current matching. The final
ordinary black-site cubes and Fourier coordinates do not move with M, so
there is no omitted coordinate-derivative term.

This preserves the previous integrated error
C_T[A_l l^3/N+1/l+C_l/N^2], with constants independent of the geometry
history. This is an extension of that already checked proof, not a claim
that partial-match color products remain stationary during formation.

## 4. Plaquette drift and Dirichlet comparison

For a color-only Fourier component F on fixed black sites, the actual joint
plaquette drift is K_M F, where

    K_M=nu sum_{flippable squares p}(T_{u_p v_p}-I).

This auxiliary operator at a fixed M preserves uniform count laws. Its
black-pair swap is a contracted graph edge, and for N>=8 two opposite black
vertices determine at most one elementary square. The symmetric routed
form has at least k0/2 per such edge. Therefore

    D_K(f)<=a D_S(f),  a=2nu/k0.

The bound is conservative: the two nonmatching sides actually give two
routing channels on each flip edge in the checked fixtures. No sharpening
is needed. By the bilinear Dirichlet identity and Cauchy--Schwarz,

    |<K F,f>|^2 <= D_K(F)D_K(f) <= a D_K(F)D_S(f).

Taking the variational supremum proves ||K F||_{-1,S}^2<=a D_K(F). The
forcing K F is orthogonal to each count sector's constant because K is
stationary there; F itself need not be globally count-centered.

A swap across opposite black corners has increment
(phi(u)-phi(v))(xi_v-xi_u)/sqrt(K), with phase difference O(|Q|/N).
There are at most 3N^3=6K squares and bounded colors, so
D_K(F)<=C nu |Q|^2/N^2. The switched estimate on microscopic [0,Nt]
then bounds the integrated **actual unconditioned joint drift** by
C t nu^2|Q|^2/(k0 N). Conditioning is only a method to estimate this
functional; it is not used to replace random event times inside the joint
generator or martingale decomposition.

Routed and geometric color jumps both have size O(1/(N sqrt(K))) and
there are O(K) channels at fixed bounded rates. The joint bracket over Nt
is O(1/N). The prior variation-of-constants argument and its fixed-mode CLT
therefore apply in the ordered block/volume limits. This establishes the
arbitrary-p matrix conclusion; F1 only concerns its isotropic specialization.

## 5. Preparation after random completion while geometry moves

Conditional on a marked history after completion, every interval contracts
the centered density norm at least at the common rate g_N. A prescribed
color permutation is an isometry of that norm. Their composition therefore
has the same point-mass and arbitrary-entrance TV bound at the final common
elapsed time, regardless of the number of geometric jumps.

Autonomous geometry and color-independent birth probabilities retain the
multinomial count law independently of that complete history. Mixing the
uniform count-sector targets gives pi_p independently of the history.
At the prepared observation time, the reference matching law is the actual
law of the **current** matching M_(tau_fill+t_prep), not a claim that M
remained at its completion value. The stated history-level comparison
preserves the geometry marginal. Subsequent common joint Markov kernels
contract TV, and the earlier C K epsilon_N bound transfers mean-square
propagation for epsilon_N=N^-4.

Adding these color-independent plaquette moves before completion preserves
the autonomous finite geometric state space and iid color birth increments.
Existing positive-rate birth/slide paths to full packing still exist. Thus
there is no closed nonfull communicating class; the finite nonexplosive
geometry chain still reaches full packing almost surely in finite mean at
each fixed volume. This does not supply a volume-uniform completion-time
bound. Stationarity of partial-match color configurations is not assumed.

## 6. Reversible geometric-field boundary

For the outgoing staggered link field B_i(x)=sigma_x(n_i(x)-1/6),
sum_i[B_i(x)-B_i(x-e_i)]=sigma_x(sum incident matching edges-1)=0.
Use the edge-midpoint Fourier convention. For an i-oriented matching on
an ij square based at x changing to the j orientation, its increment is

    Delta Bhat(k)
      = 2i sigma_x exp[-ik.(x+(e_i+e_j)/2)] / sqrt(V)
          [-sin(k_j/2)e_i+sin(k_i/2)e_j].

Reversing the flip negates this expression. Contraction with the Fourier
divergence vector sin(k/2) is exactly zero. Its squared vector norm is
4[sin^2(k_i/2)+sin^2(k_j/2)]/V <= |Q|^2/(N^2 V).
The physical geometry flip rate is 2nu, not nu. Summing all three square
orientations yields D_geo(Bhat)<=C nu |Q|^2/N^2 uniformly over the invariant
geometry law, because the local bound is pointwise.

Every finite communicating class of the symmetric geometry chain has a
uniform reversible law, and mixtures remain reversible. Under such an
initial law, for complex observables the inner product is conjugate-linear
in its first argument; the spectral theorem gives

    E|F(M_t)-F(M_0)|^2 = 2<F,(I-exp(t L_geo))F>
                       <= 2t D_geo(F).

The constant part cancels even if the mode has a nonzero mean. Taking t=Nt
proves the displayed O(1/N) absolute mean-square increment bound. No
geometric gap, mixing of winding sectors, variance lower bound or phase
claim is used. This argument needs stationary reversible geometry and
does not establish the same claim for arbitrary nonstationary geometric
entrance. It says nothing about a relative error divided by a vanishing
structure factor or a microscopic photon count.

## Independent finite controls

The main checker uses three noncommuting stationary four-state generators
and deterministic boundary permutations. Separate augmented finite-state
moment equations track both forward/backward martingale sums and the
additive functional for 1,2,9,37 intervals. They verify each martingale
second moment equals twice the summed interval energy and their paired
functional equals the separately computed integral. These are numerical
matrix-exponential controls with exact interval Poisson solves, not a
replacement for the proof above.

It also checks 64 immutable record/orientation/parity/rotation cases;
edgewise form domination on N=8 winding, columnar and independently generated
irregular matchings; one-marker-sector H-minus-one comparisons; and 96
Gauss Fourier increments at N=8,10, including wrapped squares, both flip
orientations and non-axis modes. A two-state reversible face control checks
the rate and factor-two spectral inequality. The separate symbolic
asymmetric-product countercontrol establishes F1.

Both checker executions succeeded on their first attempt with empty stderr.
No failed calculation was discarded. The substantive unresolved item at
this pre-comparison boundary is only F1; the load-bearing moving-geometry
proof estimates reconstruct under their stated hypotheses.
