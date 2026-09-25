# Original charge current and initial charge-covariance growth

2026-09-25. Personal conditional theorem candidate; no independent check
of this candidate is claimed at its author seal. No publication or audit status.
This targets a bounded charge observable before fitting data. It does not identify
a laboratory preparation, detector, charge unit or lattice/time scale.

Use the three unchanged common-model parents at main60c5f194d940a7bbaf1cdd545296e31d74a02f1a.
Keep h=KD+delta H4, the full vacancy-gated D, H4=-2 sum over unordered
OVERLAPPING A-star pairs S_xy^*S_xy, S_xy=F_yF_xP, and original
L_ab,sigma=sqrt(kappa)Pj_ab,sigma F_aP. The permitted coherent alternative sums
the two signs without normalization at each separately recorded edge. All
integer Gauss fields and unsigned tensor hard-core matter remain present.

The root's sealed42 static branch identities are an explicitly imported conditional parent,
now separately PRE/POST checked; their proof will be restated rather than
silently importing an additional instrument. No root45 result or checker is used.

## 1. Existing current and exact charge continuity

On the finite physical graph define rho_x=q_x-1_A(x). All rho_x and their
finite test sums R_f=sum_x f_x rho_x are bounded. For link e oriented A to B,
define on the finite q,E basis core the charge current

 J_e = -i[h,E_e]
       -1/2 sum_mu (L_mu^*[E_e,L_mu]+[L_mu^*,E_e]L_mu).

D commutes with E_e. The remaining h and L terms are bounded finite sums of
integer electric translations with bounded matter coefficients. Their
commutators with E_e only multiply each term by its fixed integral shift.
Thus the displayed expression extends to a bounded operator. Its action on P
uses only the original finite local terms involving that link;
it is an expression in existing observables and maps, not a new primitive.
This is minus the formal adjoint-generator action on E_e. It is meaningful as
a bounded current even for normal states lacking an electric first moment.
In that case no time derivative of an undefined mean E_e is asserted.

Every original Hamiltonian term and jump preserves Gauss. On the core,
div E=rho, so L^*rho_x=-sum_e incidence(x,e) J_e. Both sides extend boundedly
and the identity holds on the physical space. It gives

 L^*R_f=sum_(a->b)(f_b-f_a)J_ab,
 L^*sum_x rho_x=0.

The Hamiltonian current and the formation contribution are kept separately
within this one full generator. A nonzero formation count is not net charge
creation. A circulation current can be present without a charge-density change.

## 2. Initial sector and bounded first derivatives

Supply any normal density in the minimal-number sector N=n=|A|. On P, Gauss
forces all A plus and all B vacant. Its field need not be zero, stationary or
have any electric moment. On this entire sector R_f=0 and h preserves the
sector. Write d_a=|N(a)|. For a mark a->b and outward destination c!=b,

 Delta rho_a=sigma-1, rho_b=-sigma, rho_c=1,
 Delta E=sigma e_ab-e_ac,
 w_f(sigma,c)=f_c-f_a+sigma(f_a-f_b).

The branch injections are isometries into mutually orthogonal matter words
at fixed edge. Hence insertion of a diagonal charge observable between branch
maps gives a scalar times the input-field identity. This remains true for
the coherent sign sum: it does not identify that state with a mixture, but
the present diagonal charge statistics agree. Different edge records are
never coherently added.

For a finite graph, D commutes with R_f and R_f^*R_g. Their Hamiltonian
commutators only use bounded H4 and are bounded. In the interaction picture
of self-adjoint KD, the remaining finite generator is bounded on trace class
and strongly continuous on each trace-class input. A normal state's first
expectation derivative therefore exists by the integral equation and
dominated convergence. No second derivative or uniform norm-continuity of
the conjugated shift operators is assumed.

The initial Hamiltonian and loss anticommutator contributions vanish because
both charge observables annihilate the input sector. The original recycling
term alone gives the initial derivatives below, without turning off any
later channel. At kappa=0 they vanish; no conditioning on a zero-rate mark
is made.

Summing the two signs cancels odd sigma terms. Summing over b and c!=b gives

 d/dt <R_f> at0
   =2 kappa sum_a (d_a-1) sum_(b in N(a)) (f_b-f_a),

 d/dt <R_f^*R_g> at0
   =4 kappa sum_a (d_a-1) sum_(b in N(a))
          conjugate(f_b-f_a) (g_b-g_a).                 (A)

At t=0 every <R_f> is zero, so the same formula gives the derivative of the
connected covariance <R_f^*R_g>-conjugate(<R_f>)<R_g>.
The form on the right is positive semidefinite; constants are in its kernel.
This is the initial covariance slope, not a classical noise process, a
frequency-independent spectrum, a finite-lag correlator or a diffusion law.

For the formation part alone, on this initial sector,

 <J_ab^formation>=2 kappa(d_a-1).

Indeed the sigma link shifts cancel in the sum, and the original outward
hop along ab occurs once for every other mark and both signs, giving
<L_formation^*E_ab>=-2 kappa(d_a-1). A magnetic circulation contribution can
remain for arbitrary field input. For the separately supplied zero-field basis vector, the expectation of
that off-diagonal Hamiltonian current vanishes; it need not vanish for
arbitrary field input. The charge-mean formula (A) needs no such extra field premise.

## 3. Degree-six cubic Fourier consequence before fitting

On an equal even cubic torus L>=4, let n=L^3/2 and use allowed k_i L in 2pi Z.
For f_x=exp(-ik.x), the six short link lifts give

 d/dt <R_k^*R_k> at0 =80 kappa n sum_i(1-cos(k_i)).     (B)

Normalize by all 2n sites: s(k,t)=<R_k^*R_k>/(2n). Then

 s'(k,0)=40 kappa sum_i(1-cos(k_i)),
 |s'(k,0)-20 kappa |k|^2| <=(5/3) kappa sum_i k_i^4.

The remainder follows from the elementary fourth-order cosine bound and is
geometric, not a continuum dynamical error estimate. The initial covariance
slope is independent of K,delta and the incoming field because R_f annihilates
the entire initial matter sector. Later evolution need not share that independence.

There is a cross-check through the already derived true first-event clock:
rate60 kappa n times the orientation/sign averaged birth structure factor
(4/3)sum_i(1-cos k_i) equals (B). This uses the event only for the derivative;
the direct full-generator derivation above retains every later birth.

The nonzero initial formation link currents point along the oriented bipartite
edges. They do not imply a macroscopic uniform vector current: the six physical
directions at each A cancel. The mean charge redistribution is staggered;
generic long-wavelength Fourier means vanish by lattice translation symmetry.
The covariance grows even where that mean vanishes.

## 4. Observation obligations

Equation (B) is a conditional charge-density covariance consequence of the
supplied model and initial matter preparation, calculated before any data fit.
It is not yet an observation prediction in SI units. A physical preparation
must justify the minimum-number matter sector; a charge unit, length and time
calibration and a detector coupling must be derived or explicitly supplied.
No charge-density measurement is identified with a photon count or energy
change. An initial slope alone cannot be compared to a measured finite-frequency
noise spectrum without a controlled time/frequency/readout relation.

The next observation task is a controlled local finite-time or finite-lag
charge readout under the full law, with justified physical preparation and
calibration. No experimental exclusion or agreement can be drawn from the
unidentified initial slope alone.

## 5. Exact controls, chronology and limits

current_noise_controls.py is a new standard-library program. It imports no
earlier author or checker code. It executes the original outward F move and
then j for every primitive mark/destination/sign on the cube, equal L=4,6
cubic tori, a seven-site path and K2,3. The irregular graph bipartition is
specified combinatorially, not inferred from the displayed coordinate labels.
The degree-three cube is never assigned the degree-six Fourier coefficient.
No six-site second-birth calculation is used.

Every complete charge deviation and electric shift is retained sparsely, with
all six integer charge-test values. All 8480 primitive rows satisfy original
Gauss and hard-core constraints. Each fixed edge's primitive matter words are
distinct, so the same diagonal-charge sums apply to the stipulated coherent
edge mark. This verifies a diagonal statistic; it does not equate recycling
maps or quantum states. Field-independence for arbitrary normal input is proved
by the branch-isometry argument, not inferred from testing zero input flux.

The controls check 180 real polarized covariance entries, including the
real/imaginary components of allowed complex Fourier modes, all charge means,
all link formation currents, their divergence and the actual mark norm/rate
factors. The path has degree-one A sites with no formation, which tests the
zero-rate endpoint. On L4 at k=(pi/2,0,0) the full covariance slope is 2560
in units of kappa and the per-site slope is40. On L6 at k=(pi,0,0) the
corresponding values are17280 and80. Constant tests have exactly zero mean
and covariance slope on every graph.

The primary ran once at09:10:37UTC, exit0, empty stderr, elapsed1.856014958s
externally and1.781567500s internally. A separately written root_readonly_check.py
reconstructed every stored geometry, primitive field/charge row, coverage set,
mark norm, current, mean and covariance without importing or executing the
primary. Its fresh run took.462467417s, exit0 and empty stderr; all seven
observed input files were byte/stat unchanged. All five compact result groups
were read completely. Long raw vectors were checked mechanically, not all
manually read. This is personal verification, not independent evidence.

The current/core argument, arbitrary-normal-state first derivative and all
volume/measurement qualifications are analytic proof obligations not replaced
by the finite controls. No second time derivative, finite-frequency spectrum,
finite-spin stopping/derivative transfer, thermodynamic dynamics, macroscopic
current, physical vacuum instability or experimental fit was computed.

There was no failed scientific execution. The original working argument,
complete program snapshots, streams, receipts and read-only check remain
unchanged. Root had already read the independent42 charge checks and other
earlier campaign results before this derivation; no fresh blindness is claimed.
No independent45 argument was read or used. The exact source pins and author
seal distinguish existing supplied premises from the new conditional observable.
