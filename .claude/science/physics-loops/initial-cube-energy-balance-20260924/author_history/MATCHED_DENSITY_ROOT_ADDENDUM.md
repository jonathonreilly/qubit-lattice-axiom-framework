# Matched rare density on the entire initial interval

Root extension after reading the initial-balance PRE and POST, 2026-09-24.
This is not part of the earlier blind root proof. It combines the attributed
PRE matched scalar argument with the POST L2-in-age density argument.
It requires released-source comparison before publication.

Use precisely their original compensated cube, canonical input and scaling.
Let y_i,e,1(t,s) be the canonical Hermitian first-high coordinate of the raw
j_i first-birth path, with the prefactor kappa epsilon^-2 outside its density
integral. On 0<=tau<=t/epsilon^2 put

    f_i,e(t,tau)=epsilon^-2 exp(i delta tau/epsilon^2)
                      y_i,e,1(t,t-epsilon^2 tau),
    f_i,tr(t,tau)=exp(tau L) R_i u4(t).

Set both vectors to zero outside that interval and define

    Sigma_tr,e(t)=kappa sum_i integral_0^(t/epsilon^2)
       |exp(tau L)R_i u4(t)><exp(tau L)R_i u4(t)| d tau.

Then, uniformly for 0<=t<=T,

    ||epsilon^-4 U1,e* rho6,e(t) U1,e-Sigma_tr,e(t)||_1 ->0. (A1)

All coordinates are embedded in the same first-high physical rotor space.
Proof: the inherited uniform source remainder gives an O(epsilon^2) error
in f_i,e, with squared-age integral O(epsilon^2). The principal exact
profile has the common tail bound C_T(1+R)^(-3/2)+C_T epsilon^(1/2)
uniformly on the entire physical-time triangle. The truncated rotor profile
has the corresponding tail bound. Below a fixed R, uniform strong convergence
of the bounded fast generators, uniform source convergence and uniform
continuity of u4 give convergence uniformly on
0<=epsilon^2 tau<=t<=T, including t=0. Both profiles are zero outside this
same triangle; no discontinuity comparison of different cutoffs occurs.
Split at R, take epsilon->0, then R->infinity. This proves the uniform L2
vector comparison. The norm sums are uniformly bounded, so the integrated
rank-one inequality |||f><f|-|g><g|||_1 integrated <=
||f-g||_L2(||f||_L2+||g||_L2) proves (A1).

At t=epsilon^2 tau in a compact tau interval, (A1) gives the root's
Sigma_init(tau) by uniform continuity of u4 at zero. At any fixed positive
time its truncated upper limit can be removed by the rotor tail, giving
the parent Sigma(t). The latter step is uniform down to a_e precisely when
a_e/epsilon^2->infinity, as already shown for the scalar trace in PRE.
For density necessity, the missing tail is positive and its trace equals
its trace norm, so the same positive scalar gap applies at a finite-ratio
subsequence. This is an absolute matched statement, not a relative one on
every more rapidly shrinking clock or every additionally magnified observable.

Sources: initial-energy-balance-independent/PRE.md
785f3c87cec7db2d00f2548745b22fd68e74afa09a307081446fc80763555b3a;
POST.md1b8a71eedd1d014e22b23a87e7658cd01fd0645f932b8292dce08ddc645c42c4;
full-ensemble-energy-publication note
b2fe61b2a821fea5cc99e4e87b2d28536673a10cab5c2bed5b51daffa6cc2d9d.
No original seal, source, axiom, instrument or audit status changes.
