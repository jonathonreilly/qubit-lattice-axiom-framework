# Six-column endpoint eigencluster: original-readout vertex

The proposed projection argument is sound for the specified single-upper-interface height operator, assuming the previously certified isolated finite eigencluster at total height momentum zero. It derives a nonzero inter-fiber vertex near zero momentum without proving a dispersive or uniquely resolved branch.

## Fiber regularity

Let R=(sum_c h_c)/6. A simultaneous two-column height raise/lower changes R by +/-1/3, while a height exchange leaves R unchanged. Thus a COM Fourier fiber acquires exp(+/-ik/3) on the pair moves, with the sign depending on the transform convention, and phase one on exchanges. Bounded degree and bounded hopping amplitudes imply K6(k) is bounded and norm analytic near real k=0. The common-height quotient can have a length-dependent gauge under k->k+2pi; this does not obstruct a local analytic gauge near zero.

Choose a closed contour enclosing a finite discrete eigencluster below -7 and separated from the rest of K6(0) by a positive distance. A below-threshold trial ensures at least one such cluster once the essential lower bound is established, though it need not identify a unique eigenstate. Norm continuity of K6(k), the resolvent identity, and the contour integral give a norm-continuous finite-rank Riesz projection P(k) of constant rank for sufficiently small real k. Degeneracy inside this cluster is harmless. This step does not require differentiating individual eigenvalues or proving a separate uniform essential threshold at each k.

## Exact upper-interface readout

For one column with down spins below the upper boundary h, the two distance-two bonds crossing that interface have centers h and h+1. Each changes the reference ZZ value by -2, giving

-2[exp(iph)+exp(ip(h+1))]
=-4 cos(p/2) exp(ip/2) exp(iph).

Summing six columns and writing h_c=R+(h_c-R) yields the specified upper-interface excess operator

C_p^upper=-4 cos(p/2) exp(ip/2) exp(ipR) D_p,
D_p=sum_(c=1)^6 exp[ip(h_c-R)].

This is a direct readout identity. In a finite down interval the lower interface contributes a second term; at p=0 the full interval excess is -8 per column, whereas the upper-interface contribution here is -4 per column. The two must not be conflated. A fixed remote lower boundary, subtraction of its contribution, or a precisely defined single-interface geometry must remain explicit. Normalization factors such as 1/sqrt(V) from another definition of C also remain external to this unnormalized six-column formula.

The exp(ipR) factor maps the source COM fiber to the momentum-shifted fiber (p or -p according to the common Fourier convention). The remaining relative-space vertex is D_p.

## Strong convergence is sufficient

Each D_p is a bounded multiplication operator with ||D_p||<=6. Pointwise in every relative-height configuration it tends to6, so dominated convergence gives strong D_p->6I. Operator-norm convergence on the whole infinite height space is neither asserted nor needed.

Because P(0) has finite rank, strong convergence is uniform on its unit sphere:

||(D_p-6I)P(0)|| ->0.

Together with norm continuity of P(p),

||P(p)D_pP(0)-6P(0)||
<=6||P(p)-P(0)||+||(D_p-6I)P(0)|| ->0.

Consequently the projected original upper-interface vertex tends to -24P(0). For sufficiently small p it is nonzero and has a nonzero minimum singular value on the source cluster, after identifying the nearby finite-rank ranges. This conclusion does not need a preferred vector within a degenerate eigencluster. It remains valid if the eigencluster consists of several resolved levels.

## Meaning and limits

At p=0 the vertex is proportional to identity within the cluster; that is an elastic statement, not an inelastic line. At small nonzero p it couples the neighboring COM fibers, but these may have equal energies if the band is flat. Thus the vertex alone establishes neither propagation, group velocity, finite-frequency response, nor a nonzero curvature. It also does not imply nonzero matrix elements for every arbitrarily chosen pair of eigenvectors inside degenerate clusters; the verified object is the full cluster map.

The interface sector, chosen six transverse columns, and endpoint-only operator remain supplied. The formula is not a full native-H eigenmode theorem, an embedded-feature construction, or a detector/cosmological identification. The lower-interface and finite-volume normalization qualifications above are necessary when connecting it to the previously defined original uniform C.
