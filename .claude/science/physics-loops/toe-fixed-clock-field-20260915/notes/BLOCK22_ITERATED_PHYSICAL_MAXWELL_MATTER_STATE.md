# Physical local observables in the iterated zero-coupling state

Provisional personal derivation, 2026-09-16 UTC. No independent audit. This note
uses the fixed-box state convergence of Block21 and the declared paired Wilson
example of Block20. It gives local physical correlation functions in the ITERATED
limit g->0 at each fixed L, followed by L->infinity. The lattice spacing a is fixed.
It is not a theorem about the phase at any fixed positive g or a->0.

## 1. Model, state and probes

Use untruncated integer U(1) rotors, exact Gauss law div E=Q, the two conjugate
number-conserving Wilson species with charges +/-1, and no extra Q^2 interaction.
Set electric and magnetic direction weights to one and use b=kappa=pi/3, zeta=1/2
as in Block20. The full finite-volume Hamiltonian, with all matter hopping retained,
is the model in Block21. Take its ground state at each sufficiently large fixed
L=6m or6m+3, then g->0. The minimizing flat twists are respectively
(pi,pi,pi) and (0,pi,0); all hypotheses used here are the ones verified there.
Eventual ground simplicity follows from the simple leading oscillator ground and
its separated first slow level. Independent audit of those premises remains pending.

Let C_L be oriented plaquette curl from real link one-forms to plaquette two-forms.
Define, on link space,

    Omega_L=(C_L^* C_L)^(1/2),   Omega_L^+=inverse on its positive subspace,
                                                   zero on its kernel.       (1)

Gradient and harmonic directions belong to that kernel. On a periodic cube the
positive subspace has dimension 2(L^3-1). For fixed finitely supported real link
and plaquette test arrays u,v, embedded in the box, define physical probes

    E_g(u)=g sum_e u_e E_e,
    B_g(v)=g^-1 sum_p v_p sin(theta_p),
    W_g(u,v)=exp(i E_g(u)/2) exp(i B_g(v)) exp(i E_g(u)/2).          (2)

All exponentials are bounded unitaries, preserve Gauss law, and are defined by
the actual electric operators and plaquette holonomies. No gauge-fixed vector
potential is declared a physical local observable. The use of sin(theta_p)
removes a branch choice of the plaquette angle.

Matter probes are bounded, even, gauge-invariant finite-support polynomials:
for example endpoint CAR bilinears joined by a fixed oriented link path, with
the conjugate link product for the negative charge, and finite products of such
operators. Local neutral pairs are also allowed on the full neutral matter
space. Paths are fixed as L grows and do not wind around the box.

## 2. The fixed-L state and the Gaussian field law

Block21's leading min-max proof gives more than eigenvalue convergence for the
ground state. Its normal excited component and excited matter-band component
vanish in norm. The normal state, at q=g x, tends to the unique oscillator ground.
At t=t_*+sqrt(g)y the slow state tends to its unique oscillator ground, even when
excited slow levels are degenerate. The matter vector tends to the unique filled
state at the minimizing flat twist. Thus in a local physical chart the normalized
ground converges strongly to

    chi_Maxwell(x) tensor chi_slow(y) tensor u_matter(t_*).         (3)

Charge connections were removed only locally; restoring them yields the physical
operators in (2), not new unconstrained states. Longitudinal electric offsets
are O(1) at fixed L, so their contribution to gE vanishes. A harmonic electric
momentum is O(g^-1/2), so its contribution to gE also vanishes. The surviving
electric variables are transverse normal momenta. Likewise sin(theta_p)/g tends
to C_L x. The normal Hamiltonian, in physical transverse coordinates, is

    a H_Maxwell=(1/2)||P||^2+(1/2)||C_L A||^2,
                        A,P in ran(C_L^*).                       (4)

Its ground covariances are

    <P P^T>=Omega_L/2,
    <B B^T>=C_L Omega_L^+ C_L^*/2,
    <P_i B_p+B_p P_i>/2=0.                                      (5)

Consequently the exact bounded probes have the limit

    lim_(g->0) <W_g(u,v)>
      =exp[-(u^T Omega_L u+v^T C_L Omega_L^+ C_L^* v)/4].          (6)

A direct operator justification avoids inferring characteristic functions from
moments alone. The electric exponential in (2) translates the normal rescaled
coordinate by a finite transverse displacement, the slow coordinate by O(sqrt(g)),
and gives a charge-offset phase tending to one. The magnetic exponential is a
bounded multiplier converging pointwise to exp(i v.C_L x). These converge strongly
on compact smooth vectors, hence on (3) by density and their norm-one bound.
The symmetric product is the Weyl exponential of the two limiting linear
canonical variables; its scalar commutator phase cancels between the half shifts.
This proves (6) and, by repeating the same argument, finite ordered products.
It does not require Gaussianity at any nonzero g.

The local matter probe tends to its finite-matrix value in the flat connection
and is independent of x,y in this limit. Thus for every declared matter probe O,

    lim_(g->0) <W_g(u,v) O>
       =exp[-(u^T Omega_L u+v^T C_L Omega_L^+ C_L^* v)/4]
                                                    <O>_Slater,phi_*.        (7)

This is factorization of these limiting physical probes. It is not a tensor
factorization of the original Gauss-constrained microscopic Hilbert space.

## 3. Fixed-time correlation functions, not only static moments

The fixed-L state comparison also has a real-time version for these probes,
uniform for time in any fixed compact interval. In the local chart rescale
q=g x, t=t_*+sqrt(g)y and subtract the exact ground energy. On compact smooth
normal/slow vectors and the finite matter space the generator converges to

    H_lim = [H_Maxwell-Eperp/a]+[h(t_*)-e(t_*)]/a,                (8)

acting as identity evolution on the frozen slow y factor. In norm on such
vectors: the normal cosine remainder is O(g^2) times a polynomial in x, the
matrix variation in t is O(sqrt(g)) times a polynomial in y, normal matter
variation is O(g), and the slow kinetic term is O(g). Local connections and
the longitudinal term have already been handled as in Block21. Fixed chart
cutoffs have vanishing tails on the Gaussian/Schwartz vectors and their needed
derivatives.

Duhamel applied to the limiting oscillator evolution of Schwartz vectors
therefore gives norm convergence of the finite-time propagators on this dense
set. The limiting finite matter evolution is bounded, and the oscillator
preserves all required Schwartz seminorms on compact time intervals. Unitarity
extends the comparison to vectors obtained by the bounded probes. Combining
with their strong convergence and (3) proves every finite product correlation
of W_g and the stated matter probes at fixed finitely many times. No interval
growing like 1/g or L, and no adiabatic-in-time assertion, is included.

For example the limiting ordered photon correlations, with the time argument
on the FIRST operator, are

    <P(t) P(0)^T>=(1/2)Omega_L exp(-i Omega_L t/a),
    <B(t) B(0)^T>=(1/2)C_L Omega_L^+
                                  exp(-i Omega_L t/a) C_L^*.    (9)

Polynomial correlations such as (9) can alternatively be obtained by applying
the propagator comparison to the converging single-field vectors. To justify
that extra norm convergence, the full ground energy and the bounded matter
variation give <N_g>->Eperp: coercivity first bounds <|q|^2>=O(g^2), so the
normal matter change is O(g), while the matter flat energy is bounded below
by its minimum. Separate lower semicontinuity of normal kinetic and potential
energies, together with equality of their limiting sum, then forces convergence
of both positive energy parts. Outside each rescaled ball their energy tends
to zero by exhaustion; V>=c|q|^2 controls the coordinate tails. Thus the scaled
electric and linearized magnetic operators acting on the ground vector converge
in norm. On the original torus sin^2(theta_p)<=2[1-cos(theta_p)] supplies the
same magnetic tail control. This proves the two-field correlations in (9).
The bounded
characteristic functions (6)-(7) are the main convergence statement; arbitrary
unbounded microscopic moment sequences are not inferred solely from them.

## 4. Infinite volume after g->0

For unit weights and nonzero lattice momentum k, put
d_i(k)=exp(i k_i)-1, omega(k)=sqrt(sum_i |d_i(k)|^2). In the link-base Fourier
convention,

    Omega(k)=omega(k)[I-d(k)d(k)^*/omega(k)^2].                   (10)

The curl counterpart in (5) is C(k)C(k)^*/omega(k). Both symbols tend to zero
in norm at k=0, so defining them as zero there gives continuous bounded matrices.
Their finite-grid quadratic forms against every fixed-support test array
therefore converge by ordinary Riemann sums. Equations (6),(9) define the
infinite-volume free transverse Maxwell state and its fixed-time correlations.
There are two positive-frequency polarizations at nonzero momentum,

    frequency(k)=2 sqrt(sum_i sin^2(k_i/2))/a.                    (11)

This is a massless SMALL-MOMENTUM lattice dispersion. The lattice spacing has
not been removed. It is not a massless interacting pole at g>0.

For matter, the negative-band projectors of the paired Wilson matrices are
bounded and smooth except at their finitely many Weyl nodes. Their shifted
Riemann sums converge to the same Brillouin-zone integral along either twist
subsequence. Fixed-time factors exp(-i h_s(k)t/a) are smooth and bounded and
do not change this conclusion. A fixed open path supplies only its flat
phase, which tends to one as L grows. Equivalently include that phase in
the shifted Bloch momentum before taking the sum. Wick's rule gives all
finite physical neutral polynomial correlations.

Hence the alternating GLOBAL minimizing twist does not obstruct a single local
iterated state. The resulting physical correlations are the free transverse
Maxwell correlations multiplied by the appropriate neutral Slater correlations
of the four declared Weyl cones. The bare Weyl metric is diag(1,1,3/4), whereas
unit gauge weights give an isotropic photon. A common speed or metric has NOT
been obtained in this zero-coupling limit. Blocks11–14 considered a different,
conditional positive-coupling infrared flow and cannot be substituted here.

## 5. What is resolved, and what is still missing

The output is an observable-level comparator reached from ground states of the
full supplied Gauss-constrained Hamiltonian in a specified order of limits.
It identifies which low global levels are invisible to these rescaled local
field probes and retains the nonidentity finite-volume matter vacuum.

It does not prove that the same local correlations are approached when L goes
to infinity first at a fixed positive g, give a sufficient joint rate g(L),
show persistence of Weyl matter against pairing/confinement, construct a
renormalized continuum theory, select this Hamiltonian from the framework,
or force an axiom update. Setting g to zero before the infrared limit removes
the interactions whose long-distance control remains the principal phase
obligation. The result is conditional model mathematics pending independent
review, not an empirical prediction.

The companion checks finite curl matrices against their independent Fourier
symbols and tests scaled local probes in Block21's coupled two-coordinate
fixture. The latter is a noncubic discriminator of state convergence, not a
numerical verification of an arbitrary-volume many-body theorem.
