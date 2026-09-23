# Finite-time exponential tails for one electric link: analytic candidate

Root personal frontier draft, September 23, 2026, before its decisive
controls. This uses the **supplied compensated rotor target** and the
already checked local pair form and actual formation channels. It seeks a
stronger finite-time statement than the separate second-moment candidate,
for initial states that have a one-link exponential moment. It does not
claim a uniform all-future moment or microscopic large-spin control.

Let `e=(a,b)` be a fixed oriented link on a finite bipartite graph of
maximum degree z. Write `E=E_e`, `H=K D+V`, and use either resolved actual
channels or coherent edge channels with their specified sqrt(kappa)
amplitude. Take delta,kappa>=0. The commuting electric diagonal obeys
`[D,E]=0`. A jump term is a sum of charge- and matter-conditioned rotor
shifts `m in {-1,0,1}` on E. Only channels anchored at the unique A
endpoint a can shift E. A magnetic pair term `S_ac^* S_ac` also has net
link shift in `{-1,0,1}`: each of its two outward and two inward hops can
use e only through a; if the outbound and inbound hops both use e, the
single occupied B destination returns the same old charge and the two
shifts cancel. Hard-core occupation prevents the other A record from
replacing it before the return. This assertion needs an explicit pathwise
check; a naive composition of two unit shifts would allow size two.

Fourier-decompose bounded local operators under the link gauge action
`X -> exp(i theta E) X exp(-i theta E)`. Each component X_m has operator
norm at most ||X||. From the model's local commutator estimate,

    ||[E,V]|| <= C_h := 4 delta z^4 (z-1).

Since V has only shifts 0,+/-1, its nonzero components satisfy
`||V_+||+||V_-|| <= 2 C_h`. The sum of squared norms of actual jump channels
that touch e is at most

    R_e := 2 kappa z (z-1)^2,

in either convention: the two sign ranges are orthogonal on one edge,
while the old-record hop offers at most z-1 destinations.

For lambda>=0 define the one-sided weight `W=exp(lambda E)`; the same
argument applies to `exp(-lambda E)`. For bounded positive invertible W
and any local L, put `B=W^(1/2) L W^(-1/2)` and
`C=W^(-1/2) L W^(1/2)`. The weighted dissipator identity is

    W^(-1/2) D_L^*(W) W^(-1/2)
      = [B^*(B-C)+(B-C)^* B]/2.

If L has link shifts 0,+/-1, then
`||B|| <= 3 exp(lambda/2)||L||` and
`||B-C|| <= 4 sinh(lambda/2)||L||`. The magnetic commutator weighted
norm is at most `4 C_h sinh(lambda/2)`. Thus the proposed explicit bound is

    d/dt <W>_t <= c_z(lambda) <W>_t,
    c_z(lambda) = 4 C_h sinh(lambda/2)
      + 12 exp(lambda/2) sinh(lambda/2) R_e.          (1)

The constants are intentionally coarse but uniform in graph volume,
electric magnitude and K.

For domain control, use the bounded increasing one-sided cutoff
`w_R(n)=exp(lambda min(n,R))` and add epsilon I before taking inverse
square roots. Adjacent weight ratios remain between exp(-lambda) and
exp(lambda), so the same weighted estimates hold independently of R and
epsilon. The bounded-observable weak equation, Gronwall, epsilon->0 and
monotone R->infinity should yield

    <exp(+/-lambda E_e)>_t
      <= exp(c_z(lambda)t) <exp(+/-lambda E_e)>_0.     (2)

For the infinite locally normal target, apply (1) uniformly to finite
induced graphs and pass each fixed bounded `w_R(E)` through the checked
spatial local-norm limit; then increase R. This requires the initial
one-link exponential moments but no moment assumption on other links.

Consequently, for the initial all-A-plus, B-empty, zero-field state,

    Pr_t(|E_e| >= R) <= 2 exp[-lambda R+c_z(lambda)t],  (3)

for each lambda>0 and finite t, uniformly in graph volume. This is a
tail estimate for the **exact target state**, not an error bound on a
separately truncated dynamics. The quadratic second-moment result for
arbitrary finite-second-moment inputs does not follow from (2) without
an exponential initial moment. Neither (2) nor (3) gives uniform-in-time
field tightness, pointwise infinite-volume birth-rate decay, a source of
birth energy or a native TOE law.

Before promoting (1)-(3), check net magnetic shifts on complete small
physical sectors and independent field translations, the actual coherent
versus resolved channel norms and outputs, the weighted dissipator identity
and cutoff ratio estimates. Audit especially whether a net shift two can
occur when opposite charges exchange through a shared B neighbor. Preserve
any counterexample and narrow the theorem if one appears.
