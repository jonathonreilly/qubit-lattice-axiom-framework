# Post-PRE comparison with the author exponential candidate

Compared only after `PRE_SEAL.json` fixed the blind independent argument,
script, results, and their SHA-256 identities. The PRE files remain unchanged.
The author source examined here is
`local_field_exponential_author/ONE_LINK_EXPONENTIAL_MOMENT_BOUND.md` at SHA-256
`e9665bd438eb597d5163ee458766b0ac686f3060bf7aa828c4b930fbf756aeb3`.
I also read the earlier draft (`db4839b3d23c4273b0f66d0440c4253451a99cef8df837120a1ffa2f1456f891`),
control interpretation (`84b1ed76f76ecf53fbd7a5d01a46ed78a3d678d749d045713cc56d830e8c7096`),
and the two author control scripts (`616b3b645e8d5ac1bd9ed447456faf6e9111e016c69193797568734d4764be30`,
`5708dc7b57ffe05c4d7a4c5e414576b400fce594e4059ce1ef51423e11bf7802`).

## Verdict within this bounded comparison

The author's stated one-sided exponential theorem and coefficients survive
this independent reconstruction. I found no counterexample to the final
note's link-shift lemma, weighted dissipator identity, or finite-volume
cutoff passage. The result is still conditional on the supplied compensated
rotor target and on the checked bounded-locality spatial limit; this
comparison is not a formal audit verdict.

The independently sealed PRE proves the slightly different direct weight
`exp(lambda |E_e|)` with a coarser Hamiltonian constant and a smaller
coherent-jump constant. The author's `exp(+/-lambda E_e)` result implies
finiteness of the absolute exponential moment from the same initial moment.
Its **own general bounded-weight lemma also applies directly** to

    W_N=exp(lambda min(|E_e|,N)),

because this weight is bounded, boundedly invertible, monotone in `N`, and
its ratios across adjacent integer fields lie in `[exp(-lambda),exp(lambda)]`.
This gives the sharper direct statement

    <exp(lambda |E_e|)>_t
       <= exp(c_z(lambda)t) <exp(lambda |E_e|)>_0,          (A)

with precisely the author's `c_z(lambda)`. From zero field, its direct
Markov bound has prefactor **one**:

    Pr(|E_e|>=R) <= exp[-lambda R+c_z(lambda)t].          (B)

The author's displayed factor two is valid but unnecessary. The same
Poisson-form optimization then has prefactor one when `R>A_z t>0`.
No correction to the author's one-sided theorem is required; (A)-(B) are a
narrow strengthening relevant to the requested absolute one-link moment.

## Coefficients

For `e=(a,b)`, the final author note correctly counts at most
`sum_{d~a}(deg(d)-1)<=z(z-1)` pair anchors. It also correctly sharpens the
PRE's crude `||S_ac||<=z^2` path estimate by observing

    ||[E_e,S_ac]|| = ||F_c [E_e,F_a]|| <= z.

Consequently, for `V_G=-2delta sum S_ac^*S_ac`,

    ||[E_e,V_G]|| <= 2delta*z(z-1)*2z^3
                   = 4delta z^4(z-1) = C_h.

The net pair matrix shift is at most one, so Fourier projection of the
bounded commutator gives
`||V_+||+||V_-||<=2C_h`. Adjacent weight ratios then give the author's
Hamiltonian coefficient `4C_h sinh(lambda/2)`. The independent tree
witness in the PRE shows why replacing `z(z-1)` here by `z-1` would be
invalid: a pair sharing a B neighbor other than `b` can still shift `e`
through different input B occupations. The final author note makes the
safe `z(z-1)` count, so this is not a defect in its coefficient.

The author correctly uses orthogonal final A-charge ranges for the two
newborn signs. Each resolved channel has norm at most
`sqrt(kappa)(z-1)`; a coherent edge channel has squared norm at most
`2kappa(z-1)^2`. There are at most `2z` resolved or `z` coherent channels
anchored at `a`, hence in either convention
`sum ||L_mu||^2 <= R_e=2kappa z(z-1)^2`.

The author's weighted dissipator identity is exact:

    V_N^{-1} D_L^*(W_N) V_N^{-1}
      = [B^*(B-C)+(B-C)^*B]/2,
    B=V_N L V_N^{-1}, C=V_N^{-1} L V_N.

With shift components `-1,0,+1`, the stated estimates
`||B||<=3exp(lambda/2)||L||` and
`||B-C||<=4sinh(lambda/2)||L||` hold. Their product is
`12exp(lambda/2)sinh(lambda/2)||L||^2`, yielding exactly the claimed

    c_z(lambda)=4C_h sinh(lambda/2)
                +12exp(lambda/2)sinh(lambda/2)R_e.

The PRE used an independent elementary-path factorization instead. It
gave a larger Hamiltonian term
`4delta z^5(z-1)(exp(lambda)-1)` and jump terms
`4kappa z(z-1)^2(exp(lambda)-1)` resolved or
`8kappa z(z-1)^2(exp(lambda)-1)` coherent. The discrepancy is conservative
bookkeeping, not disagreement on the model. After comparison, combining
the author's Hamiltonian estimate with the PRE path factorization gives a
valid optional smaller jump term. Orthogonality of the two sign ranges
also holds after left/right multiplication by the diagonal electric
weight, so the coherent transformed operator and its difference from the
unweighted operator have the square-sum sign bound. This reduces the
path-factorization jump term to
`4kappa z(z-1)^2(exp(lambda)-1)` for **both** conventions. It is an optional
coefficient refinement; the author's displayed coefficient remains valid.

## Shift support, domains, and spatial limit

The author's all-graph `S_ac^*S_ac` argument agrees with the PRE's
intermediate-output argument. If both paths use `e`, hard-core occupation
and the common final B charge force cancellation; otherwise there is at
most one unit shift. A birth path uses `e` either as the old-record edge
or as the marked newborn edge. The author controls sample finite physical
sectors and a few circulation translations; they are properly described
as corroboration, not an exhaustive proof for every graph and field.

For the author's one-sided cutoff, `exp(lambda min(E_e,R))` is bounded
above but approaches zero as `E_e -> -infinity`; adding `epsilon I` makes
it boundedly invertible. The adjacent ratio bound persists uniformly in
`R,epsilon`. The cutoff commutes with diagonal `D_G`, and a bounded
interaction-picture equation justifies its expectation for arbitrary
trace-class initial states. Sending `epsilon -> 0` and then `R -> infinity`
is legitimate by monotone convergence. The PRE's absolute cutoff `W_N`
avoids `epsilon` entirely. Neither route needs finite `D_G` expectation.

The author's full-tensor extension addresses a real boundary issue:
restricting an infinite Gauss state to an induced graph need not satisfy
an artificial boundary Gauss law. The local shift/norm and diagonal
arguments operate on the full effective tensor space, and the compensated
volume construction uses its normal local embeddings. Applying the
finite-volume estimate to ordinary local restrictions, passing each
bounded cutoff through local observable norm convergence, and then taking
the monotone limit is sound conditional on that checked spatial theorem.
It does not establish a volume-uniform microscopic/spin approximation.

## Control provenance and limits

The author `shift_and_weight_check.py` imports the root capacity builder,
so its path8/ring8/cube8 sweeps are author controls. The author
`finite_weight_generator_check.py` directly reads the independent path7
physical matrix and checks finite weighted forms, but its results remain
author checks. The independent PRE has its own six-vertex tree witness,
physical-matrix scan, and weighted finite check. These different controls
agree on shift support and the sign of the finite weighted generator.
No finite scan settles the unbounded domain or arbitrary-graph proof.

No author candidate file was edited in this comparison. No PR, checkpoint,
or formal audit status was changed.

## Check of the new absolute-value corollary

After this comparison, root added
`local_field_exponential_author/ABSOLUTE_FIELD_EXPONENTIAL_COROLLARY.md`
at SHA-256 `f0a7f9f0f8a33262cf679e577588e8dacfc26dffcd7ce585e38031dd87778ed0`.
I read its complete 58-line argument and checked it against the sealed PRE
and the unchanged original author note. Its weight
`W_N=exp(lambda min(|E_e|,N))` is bounded, at least one, monotone in `N`,
commutes with `D_G`, and satisfies the required adjacent ratio bound.
Consequently the original weighted generator lemma gives (A) with the
author's unchanged `c_z(lambda)`. The locally normal volume passage is the
same bounded-cutoff-then-monotone route as above. The prefactor-one tail,
its Chernoff optimization for `R>A_z t>0`, and the `A_z=0` frozen-zero case
follow as written. I found no new defect or hidden additional moment
premise in this corollary. The original author note remains byte unchanged
at `e9665bd438eb597d5163ee458766b0ac686f3060bf7aa828c4b930fbf756aeb3`.
