# First weighted-source calculation: a useful jump form and a surviving fast field current

Author working derivation; not independently checked and not (W1). The actual normalized-spin jump words, physical Gauss sector and original mark stacks are retained. A-to-B link orientation is used. In CONTRACT, the compensation symbol D_a means the electric polynomial sum n_a(1-n_b)E_ab(E_ab-q_a); it is distinct from the landed note's D_(a,S), the diagonal of F_a*F_a. Thus the source compensation is exactly (F_a*F_a+D_a/[S(S+1)])Q_gate,a.

## Exact positive quasilocal jump inequality

For an even periodic cubic torus let a(e) be the A endpoint of link e, and use the periodic L1 distance. Set

    f(a,e)=2^{-d(a,a(e))},
    Phi_a=2756+sum_e f(a,e) E_e²,
    X=sum_a w_a Phi_a.

All weights are physical diagonal observables. For each link,

    sum_a f(a,e)<=sum_(x in Z³)2^{-|x|_1}=27.

The torus sum is bounded by the infinite-lattice sum by choosing shortest coordinate representatives. Since each A has6 links, ||Phi_a||<=2756+162 S² at finite spin, independently of volume. X is an extensive SUM, not a localized version of the old exponential count tilt. No claim about the actual expectation is made from its norm alone.

Consider one actual birth at A center b on link e. Before the birth w_b=1; afterwards w_b=0. All other A holes are unchanged, and E_e changes by sigma. Write m=E_e on input. The exact change is

    X_out-X_in=-Phi_b+sum_(a!=b)w_a f(a,e)(2sigma m+1).

The second coefficient is at most26. Completing the square gives, for every real m,

    26(2|m|+1)<=m²/2+1378=(m²+2756)/2.

Since f(b,e)=1 and Phi_b includes m², every legal jump therefore obeys

    X_out-X_in<=-Phi_b/2.                             (J1)

Each resolved jump is a weighted partial permutation. For the original coherent edge jump, its two output A charges are orthogonal and X is diagonal; the cross terms vanish in THIS positive observable calculation without refining the observed mark. Consequently (J1) is an operator-form inequality on the whole finite carrier, including coherent input states and Gauss restrictions:

    sum_mu D[j_mu]* X <= -(1/2)sum_b Phi_b Gamma0_b,
    Gamma0_b=sum_(mu at b)j_mu* j_mu.                  (J2)

Here no kappa/epsilon² is included in Gamma0. Also Phi_b(out)<=2Phi_b(in), because only one unit link shift occurs and2756>=2. Thus

    sum_mu D[j_mu]* X <= -(1/4)sum_(b,mu at b)j_mu*Phi_b j_mu. (J3)

This is a rigorous candidate control of ACTUAL weighted mark activity by the bare dissipator. It holds equally at spin boundaries: blocked transitions contribute zero. The Hamiltonian has not yet been bounded. For fixed radius r, physical w_a Q_a² is bounded by C_r w_a Phi_a, with a finite geometric constant from Cauchy–Schwarz and the positive minimum of f on the finite ball. Physical translation invariance of rho_micro from Omega then turns a bound on <X>/|A| into the requested local moment. This is a valid way to use a global sum; replacing exp(C|A|t) by exp(C|B_r|t) would not be.

## Exact source-word obstruction to pointwise fast-current absorption

The previous occupation-tilt witness alone has ZERO Phi difference, so it does not establish a field obstruction. Add a real original magnetic circulation first. Let

    h=(0,0,0), a=(1,0,1), c=(1,1,0),
    c2=(1,1,2), b0=(1,0,2), d=(1,1,1), e=(2,0,1).

From Omega, the complete original S* S pair with S=F_c2 F_a contains the circulation

    E_(a,b0)=+1, E_(a,d)=-1,
    E_(c2,b0)=-1, E_(c2,d)=+1

with coefficient+1. Thus the actual pair-form term has coefficient−2delta. Its selected four elementary hops are legal and have unit normalized weight even at spin1. This is a supplied-source word, not a new field ensemble or an assertion about its positive-time probability.

Append the actual legal source word: at c move to(1,0,0), then plus birth at(0,1,0); at a move to(0,0,1), then plus birth at e; at h move to(0,-1,0), then plus birth at(-1,0,0), then move to(0,0,-1). Call the resulting physical basis word gamma. It has one A hole at h, seven B occupations and all six neighbors of h occupied. Its original loss is zero. Next move the occupied A at a to b0 and refill a from e, obtaining beta. The hole and its six occupied neighbors are unchanged, so beta also has zero original loss.

The complete gated same-hole block is

    F_h F_h* - sum_(a' distance2 from h) F_a'* F_a'.

Its gamma-to-beta and reverse matrix elements are exactly−1. Only the a term can change the two indicated link fields; the compensation gate at a is zero because h is a distance-two hole. The selected fields are1->0 on both changed links, so the coefficient remains exactly−1 for every integer spin. The diagonal Delta_S commutes with X.

The global positive field-hole sum has values

    X_gamma=2756+37/8=22085/8,
    X_beta =2756+33/8=22081/8.

Hence the two-dimensional compression of i delta[Hbar_S,X] has eigenvalues plus/minus delta/2, whereas both compressed loss and weighted original activity vanish. No finite multiple of the bare weighted loss can dominate this current. A grade-zero fast pole remains after inverse-ad_W corrections; it cannot be removed using only the penalty homological inverse. This rejects that pointwise positive-congruence extension, not (W1), not time-integrated absorption, and not the original microscopic limit from Omega.

check_weighted_current.py retains the complete pair seed and both complete same-hole sparse outputs, verifies Gauss, loss, exact rational weights, spin1 boundary compression and the no-circulation zero-difference control. It used0.087956 CPU seconds and21,807,104 bytes RSS under the25CPU hard cap/30CPU150MiB price. No assertion failed. Its physical word implementation is openly copied from the previous author control; it is not independent checking. The all-volume constants and all-spin selected-path argument are the analytic derivations above.

## Next live family

Retain the exact negative jump form(J3). A successful proof needs a time-integrated or corrected estimate for the fast grade-zero field current under the ACTUAL state, including preparation and source weights. Separately, the epsilon^-1 same-mark cross dissipator can be treated by a local oscillatory observable corrector for bounded grade-zero tests. Its cancellation is promising because every cross term has nonzero W grade, unlike the field-current obstruction. That lemma must keep the full gain/loss map and original marked registers; it will not by itself prove the unbounded weighted moment.
