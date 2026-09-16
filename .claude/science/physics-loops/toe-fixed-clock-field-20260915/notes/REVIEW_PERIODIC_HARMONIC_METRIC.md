# Review cross-check: the harmonic electric metric in integer cycle coordinates

Personal additional check of Block21, without a new claim status. For a periodic
L^3 cubic graph, let C be ANY integer fundamental-cycle matrix with identity
chord rows, D C=0, and K=C^T W_E C. Let U be the link-by-three matrix of uniform
unit fields in each coordinate direction. A uniform connection A=U phi/L has
cycle holonomies theta=H phi, with H=C^T U/L. The entries of H are integers:
each cycle's oriented displacement is an integer multiple of L.

If B=[N,H] is a normal/tangent coordinate frame, the transformed kinetic matrix
is B^-1 K B^-T. Its tangent Schur complement has inverse equal to the lower-right
block of B^T K^-1 B. Therefore

    S^-1=H^T K^-1 H.                                            (1)

For direction-dependent constant positive weights W_E=diag(w_i) on links,
W_E^-1 U is divergence free. Since C spans every real divergence-free field,

    C (C^T W_E C)^-1 C^T U = W_E^-1 U.

Substitution in (1) gives

    H^T K^-1 H=U^T W_E^-1 U/L^2=L diag(1/w_i),
    S=diag(w_i)/L.                                              (2)

This verifies the normalization in actual integer Gauss coordinates, independently
of the continuum-looking canonical calculation in Block21. It also shows why
the normal block must remain fixed while the tangent Schur complement is taken.

The finite checker constructs a rooted tree, every fundamental integer cycle,
and all periodic plaquettes directly at L=3,4,5. It checks D C=0, identity chord
rows, C Z=F, Z^T H=0, and the exact integer identities C X0=U and H^T X0=L^2 I,
where X0 records each chord's direction. These prove K[X0 diag(1/w_i)/L]=H
and (2) without a floating inverse. The checker is a normalization challenge;
the arbitrary-volume proof is the displayed cycle-space argument. No independent
scientific audit or uniform interacting-phase estimate is supplied.

