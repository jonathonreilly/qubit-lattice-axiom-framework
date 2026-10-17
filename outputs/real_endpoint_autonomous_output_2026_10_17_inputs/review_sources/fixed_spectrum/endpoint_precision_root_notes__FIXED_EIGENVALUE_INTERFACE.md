# Proposed fixed-eigenvalue local-block interface

Root proposal, unchecked. This is not covered by the compensated-background theorem. Sources: canonical endpoint note at97ccd9f9, and static precision proposal233364359dc3e79b54debf331eb75e6454f093cdbec36c36e1ba4fe17acc1381. Author of structural proposal has been sent the candidate direction, so a later agreement is source-exposed, not independent discovery.

Consider replacing the three emitter-endpoint local positive terms by their positive combined block. Its one-excitation matrix is [[E0,-kappa0],[-kappa0,J]]. Keep its two eigenvalues fixed, and vary only the real rotation defining its eigenvectors. Write its new entries [[E0+Delta,-kappa_a],[-kappa_a,J-Delta]]. Trace is fixed automatically, and determinant invariance requires

    (J-E0)Delta-Delta^2 = kappa_a^2-kappa0^2.

Choose the root continuous at Delta=0. With g=J-E0>0 and s=kappa_a^2-kappa0^2,

    Delta=2s/(g+sqrt(g^2-4s)).

For kappa_a<=kappa0, s<=0, Delta<=0 and |Delta|<=|s|/g. Thus a small relative hopping change produces emitter detuning of order kappa0^2 times that relative change rather than kappa0 times it. BUT the background endpoint changes by -Delta; the checked positive precision theorem does not cover this alteration.

For pre-emitter resolvent R=(E-H_bg)^-1 and endpoint projection P, let G=P R P*. A common endpoint shift delta_b changes the endpoint Green matrix exactly to

    G_b=G(I-delta_b G)^-1,
    G_b-G=delta_b G^2(I-delta_b G)^-1.

For ||G||<=36 on the certified complex disks and |delta_b|36<1,

    ||G_b-G||<=|delta_b|36^2/(1-36|delta_b|).

Here delta_b=-Delta. This is an endpoint Green-function interface only; it does not by itself certify scattering rows, complete source column, moment constants or output profile. Those additional changes must be propagated before claiming a device theorem.

The combined positive block may be extended to the full two-qubit space with vacuum eigenvalue0 and double-occupation eigenvalue E0+J, preserving number and realness. A rotation within the one-excitation sector preserves positivity and locality. Fixed eigenvalues are themselves supplied physical data. Common scaling of the whole block changes the emitter energy at order E0 times the scale error and is not controlled by this orientation-only argument. Unknown eigenvalue errors retain the detuning precision obligation. No native coefficient mechanism, thermal seed, full-device robustness or universal obstruction is established.
