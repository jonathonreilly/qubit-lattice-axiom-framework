# Two remaining vacancies: exact clocks and fixed-size dephasing limits

Date: 2026-09-22. Status: author conditional results, with exact finite
controls and an exploratory numerical screen; independent check pending.
All rates and the continuous-time generator are supplied. The limits below
hold at fixed even ring size and are not thermodynamic scaling claims.

## 1. The transient model and its mean-time operator

Let K>=4 be even and let H_2 have orthonormal basis |A>, where A is an
unordered two-element subset of the periodic ring Z/K. Thus D=K(K-1)/2.
Let n_x indicate a hole at x. The Hamiltonian H has matrix element kappa
between configurations related by one allowed nearest-neighbor hole hop,
with real kappa!=0. There is no additional H0 in the results below. Let
P_c project on configurations with adjacent holes and Gamma=beta P_c,
where beta>0. The transient, trace-decreasing generator is

    L_d(rho)=-i[H,rho]+d sum_x D[n_x](rho)-(1/2){Gamma,rho},
    D[A](rho)=A rho A^dagger-(1/2){A^dagger A,rho},  d>0.

The omitted birth gain goes to full occupation and cannot return. Monitoring
record occupation gives the same dissipator as monitoring hole occupation,
since D[I-n_x]=D[n_x]. In the gauge-ring construction this model is the
T=+1 charge-conjugation sector at two holes: the normalized sums of each
pair of complementary electric words identify its fibers with |A>, and
every ordinary hop has matrix element kappa. This identification is not
asserted for the T=-1 sector, which can carry a boundary sign.

The prior monitored completion theorem applies on this connected finite
configuration graph. Hence the survival mean is finite for every density
rho, and

    F_d = integral_0^infinity exp(t L_d^dagger)(I) dt,
    -L_d^dagger(F_d)=I,  E_rho[tau]=Tr(F_d rho).

The solution is unique and positive. Before the next birth, the choice of
birth overlap chi affects no term of L_d: all its allowed coarse birth maps
have the same loss Gamma. This is a statement about this last waiting time,
not about the initial two-hole state produced by earlier events.

## 2. An exact contact-weighted mean-time sum rule

More generally let L=A-(1/2){Gamma,.} on a D-dimensional transient space,
where A is a trace-preserving unital Lindblad generator and the transient
semigroup is stable. Taking the trace of -L^dagger(F)=I gives

    Tr(Gamma F)=D,
    E_(Gamma/Tr Gamma)[tau]=D/Tr(Gamma).

The Hamiltonian commutator and A's dissipative contribution have zero trace
because A(I)=0. This is the complete proof; stable absorption is a premise,
so the formula does not apply at a parameter value with a surviving dark
space. It also does not apply unchanged to a nonunital internal bath.

For the uniform ring, Tr(Gamma)=beta K. Translation covariance makes every
localized adjacent configuration have the same mean. Therefore, exactly
for every d>0 and kappa!=0,

    E_adjacent[tau]=(K-1)/(2 beta).

The lack of a kappa or d in this particular mean does not mean the complete
time distribution is independent of them. Rare long excursions can balance
quick absorption. For nonuniform dynamics the Gamma-weighted formula remains
valid when its hypotheses hold, but equality for each individual adjacent
configuration need not hold.

This is a continuous-time trace identity of the kind associated with quantum
return-time results. The discrete-time unital recurrence framework and its
dimension formula are established in the abstract and sections II-III of
[Sinkovicz et al., arXiv:1411.0568v1](https://arxiv.org/abs/1411.0568v1).
No discrete-time theorem is imported to prove the displayed identity, and
no new general quantum Kac principle is claimed.

## 3. The entire unmonitored dark subspace

Let S translate both holes by one site and

    P_pi=(1/K) sum_(j=0)^(K-1) (-1)^j S^j,
    P_D=P_pi(I-P_c).

The two projectors in this product commute. The Hamiltonian annihilates
the entire momentum-pi space: H P_pi=0. Consequently P_D is a dark
projector. Its dimension is

    r_K=K/2-2+1_(K divisible by 4).

Here is an exhaustion argument within this specified Hamiltonian. In a
translation sector P=2pi m/K, write the pair amplitude, away from coincident
holes, as

    psi(x,x+r)=exp[iP(x+r/2)] f_r,  1<=r<=K-1,
    f_(K-r)=(-1)^m f_r,  f_0=f_K=0.

The relative-coordinate hopping is

    (H f)_r=2 kappa cos(P/2)(f_(r-1)+f_(r+1)).

A dark eigenvector has f_1=f_(K-1)=0. If cos(P/2)!=0, the eigenvalue equation
at r=1 forces f_2=0, and induction forces every amplitude to vanish. Thus
only P=pi can contribute. At P=pi the hopping vanishes identically, so all
vectors in that sector with zero contact amplitude are dark. Reflection
r<->K-r leaves the midpoint r=K/2 available precisely when K/2 is even;
removing the one contact coordinate gives r_K above. Translation commutes
with the loss, so decomposing a putative dark invariant subspace into these
sectors is legitimate. H is self-adjoint, so its invariant subspaces have
an eigenbasis. This proves there are no additional dark states for this H.

Moreover every compressed local hole number is a scalar on this dark space:

    P_D n_x P_D=(2/K)P_D.

Translation by one acts as -I on the dark space, so all K compressed n_x
are equal. Their sum is 2P_D, proving the identity without choosing a dark
basis or assuming the local n_x commute with P_D.

## 4. Exact weak-monitoring coefficient at fixed K

For any fixed initial density rho and fixed beta>0, kappa!=0,

    lim_(d->0+) d E_rho[tau]
       = Tr(P_D rho)/(2-4/K).

To justify the singular limit, write L_d=L_0+d M. For d=0 the effective
Hamiltonian H_eff=H-i Gamma/2 is zero on the dark space and has spectrum
strictly in the lower half plane on its orthogonal complement. Indeed any
eigenvector with real eigenvalue has zero Gamma norm, hence belongs to the
dark invariant space already classified. H_eff is block diagonal between
that space and its complement. Its possible finite Jordan blocks in the
decaying part do not prevent exponential decay. Thus

    exp(t L_0)(rho) -> P_D rho P_D,

and the kernel of L_0 on operators is exactly B(ran P_D), with zero
semisimple and every other eigenvalue having strictly negative real part.
Let script-P(rho)=P_D rho P_D. The compressed perturbation is exactly

    script-P M script-P(rho)
      = sum_x (P_D n_x P_D) rho (P_D n_x P_D)-2 rho
      = -(2-4/K) rho

on this kernel. A finite-dimensional block inverse, with the complementary
block of L_0 invertible, therefore gives

    (-L_d)^(-1)=[1/(d(2-4/K))] script-P + O(1),

in any operator norm, at fixed K,beta,kappa. Taking the trace proves the
mean-time limit. In particular, for the uniform incoherent density I/D,

    lim_(d->0+) d E_(I/D)[tau]
       = r_K/[(K-1)(K-2)].

For a state entirely in the dark space the coefficient is 1/(2-4/K).
A state orthogonal to it has no 1/d divergence; this does not establish a
uniform bound as K grows. Local adjacent states have zero dark overlap,
consistent with the exact contact sum rule.

## 5. Exact strong-monitoring coefficient at fixed K

For an off-diagonal matrix unit |A><B|, the dimensionless monitoring part
has eigenvalue -(2-|A intersect B|), equal to -1 or -2. Its kernel is the
diagonal algebra. Eliminating these fast coherences to second order gives
the classical allowed-hole hopping rate

    h=2 kappa^2/d

per configuration edge. The factor follows directly from the two conjugate
off-diagonal entries generated by one H_AB=kappa; the intermediate coherence
for a single hop decays at rate d. Corrections involving the fixed birth
loss are of higher order in 1/d. Contact diagonal states have fixed loss
beta and are eliminated before the slow noncontact motion. Thus, after
rescaling time by d, the limiting population process has rate 2 kappa^2
per allowed configuration hop and is killed upon first reaching contact.

For completeness this is also a finite block-inverse argument for the mean:
first split diagonal/off-diagonal operator spaces and invert the latter
block, whose leading part is d times an invertible diagonal matrix. Its
Schur complement on populations is -beta P_c plus the stated graph generator
divided by d and O(d^-2). Split contact/noncontact populations next; the
contact block is invertible at leading order. The noncontact Schur complement
is the killed graph generator divided by d plus O(d^-2). It is invertible,
because every noncontact configuration has a path to contact. This proves
convergence of F_d/d to the diagonal classical hitting-time operator. Initial
off-diagonal density entries therefore affect only subleading terms.

With ordered separation r in {1,...,K-1}, the relative-coordinate walk has
rate 4 kappa^2 per direction in the rescaled time. Solving its elementary
second-difference Poisson equation with zero values at r=1,K-1 gives

    lim_(d->infinity) E_|{0,r}><{0,r}|[tau]/d
       = (r-1)(K-1-r)/(8 kappa^2).

The expression is symmetric under r<->K-r, so it is well defined for an
unordered pair. Its mean over the uniform incoherent input is

    lim_(d->infinity) E_(I/D)[tau]/d
       = (K-2)(K-3)/(48 kappa^2).

The adjacent coefficient is zero; its O(1) term is given exactly in section
2. The fixed beta does not enter the leading large-d coefficient because
contact absorption is fast on that rescaled clock, not because the physical
formation rate has ceased to matter in general.

## 6. What the finite computation does and does not establish

quantum_last_pair_clock_screen.py assembles the dual Poisson equation after
reducing simultaneous-translation orbits of ordered matrix indices (A,B).
It obtains the complete symbolic K=4 mean operator and recovers the earlier
independently checked dark-input clock, under the same H0=0 restriction.
It verifies exact dark projectors and compressed n_x for K=4,6,8,10,12.
The exploratory scan has K=4,6,8,12,16,24 and eight positive d values each,
with beta=kappa=1. For K<=8 it reconstructs the full matrix F and checks the
unreduced dual equation, Hermiticity and positive eigenvalues numerically.
All 48 linear systems have residuals below 1e-12. Larger rows are reduced
floating-point calculations, not certified interval results.

The first run stopped because SymPy's factor returned unevaluated 0*I for
four exact residual entries. Exact cancellation gives zero for all entries;
only that equality test was repaired. The full original script, error,
empty stdout and receipt are preserved under last_pair_clock_exploration/
structural_zero_comparison. The corrected complete run passed.

The two asymptotic formulas have different, nonuniform fixed-K regimes.
Balancing their leading coefficients would not justify an optimal d or a
large-K transport exponent. In particular it discards the potentially
size-dependent O(1) part of the weak-d expansion. The finite screen suggests
an intermediate useful monitoring range, but no optimizer, asymptotic
speedup, or universal monitoring principle is claimed.

These conditional clocks address an actual question for continuing record
formation: eventual filling need not imply a practical rate. They do not
derive physical time, monitoring, a gauge Hamiltonian or any TOE parameter.
The complete dark-space and limiting claims remain provisional research
pending independent scrutiny and the applicable negative-claim publication
gate; no universal obstruction to coherent motion has been asserted.
