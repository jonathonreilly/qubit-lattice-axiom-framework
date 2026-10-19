<!-- Original PR9788 source SHA256 1546f4ad9f0ec839aef7f9e2e7e608fb227084fc6dfb73926c47eafce5a99cce. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Fixed-box light original-readout window: physical coefficient check

Scope: fixed even longitudinal length L>=6 and fixed transverse periodic size R>2L, V=R²L, followed by lambda->0. This is separate from the earlier growing-volume darkness limit. Inputs are the checked native fourth-order plaquette coefficient, first winding coefficient/source coefficient, and a consistent real canonical reduction to N=0.

## 1. Source mixing is essential and gives b-a

Write the nonconstant leading diagonal effective Hamiltonian as

    D4=-(J lambda^4 L/128) sum_p P_p,

and the first off-diagonal winding term as

    K=-gamma_L sum_edges Xbar_i Xbar_j.

An adjacent pair flip toggles four plaquettes, hence costs

    Delta4=J L lambda^4/16.

The original source coefficients are Cdiag=a D4 and Ckin=b K, up to constants and higher terms, with

    a=3/(J sqrt(V)),   b=A_L/(2J sqrt(V)).

For g in P0, first ground mixing into this four-plaquette space is -K g/Delta4. In a transition matrix element the corresponding difference of diagonal source values is a Delta4. It therefore contributes -a K, while the direct source contributes b K. The leading physical transition is

    (b-a) P4 K g.

This accounts for both endpoint eigenvector corrections; the constant source value cancels. Using bK alone would give the wrong answer. The sign is consistent with a perturbation +hC: the intermediate gap increases/decreases according to the previously checked source derivative convention.

## 2. Edge norm and normalization

For every aligned P0 background, an edge flip produces four bad plaquettes. If two edge flips applied to possibly different P0 backgrounds gave the same spin configuration, their product would change at most four columns. Any nonidentity difference between P0 row/column patterns changes at least R columns. Since R>4, this cannot happen. Within one background, distinct physical edges have distinct pair masks as well.

Thus the edge-flip images of all P0 basis vectors are mutually orthogonal, and for any normalized superposition g in P0,

    ||sum_edges Xbar_i Xbar_j g||²=2R².

There is no ground-rank factor or constructive/destructive dependence on g. Consequently the total leading positive-window source weight is

    2R² gamma_L² (b-a)²
      = [2 gamma_L²/(J² L)] (A_L/2-3)².

The closed form A_L=6(L-1)(L-2)/(2L-3) makes the bracket nonzero for every even L>=6. This norm is a weight summed over the window, not a claim that one eigenstate carries it.

## 3. Fixed-box perturbative control

A proper proof should perform two reductions, rather than use an unrefined full-H projector estimate. First reduce across the order-one N=0 versus wall-sector gap. Then divide the N=0 Hamiltonian by lambda^4. The leading diagonal plaquette operator has a fixed finite-box gap between its ground space, its four-bad-plaquette eigenspace, and the other distinct plaquette-energy levels.

All lower-than-L native off-diagonal N=0 coefficients vanish by the winding count. Diagonal higher coefficients preserve P0 and are constant there by plane symmetry. After division by lambda^4, the first ground-to-excited mixing is order lambda^(L-4), giving the source transition above at order lambda^L. Higher diagonal terms of order lambda^5 change its coefficient relatively by O(lambda); the next possible off-diagonal terms and source terms are also higher order. The degeneracy within the four-plaquette space causes no difficulty when its whole spectral cluster is retained.

For sufficiently small lambda at this fixed box, the interval [0.9,1.1]Delta4 relative to the actual ground energy contains precisely this perturbed plaquette-energy cluster and no N>0 states. Its endpoints lie in gaps. A finite-order source/Hamiltonian normal form can be taken sufficiently far beyond L to make its remainder negligible at the claimed lambda^L amplitude accuracy. The first-order source connection has already been checked: in the real word-derived canonical gauge it does not alter the leading winding coefficient. An arbitrary independent effective-block gauge cannot be mixed into this calculation without transforming both H and C consistently.

The resulting summed weight is therefore the displayed expression times [1+O(lambda)], uniformly over normalized exact ground vectors. An exact ground may be selected by much higher-order splitting inside P0; it need not converge to a prechosen P0 basis vector. Uniformity follows from the isometric edge map on all P0, not from assuming equal ground-space ranks. Ground mixtures follow by linearity. Since the window is strictly above the ground, subtracting the ground expectation of the uniform source does not change this positive-window weight.

## 4. Qualifications

This provides a positive light-energy original-readout window at fixed geometry as lambda->0, conditional on the stated native effective coefficients. It does not select one isolated pole or establish propagation. Its constants and small-lambda threshold depend on R and L. Substituting growing L or R into the fixed-box expansion is not justified and would erase the distinction from the previously proved all-algebraic darkness family.

The source is the existing normalized distance-two ZZ sum, not an assumed detector coupling. Calling the resulting low-energy excitation cosmological, relativistic, or gravitational still requires independent physics. The nonzero window weight is compatible with the earlier observation that an isolated pure tunneling doublet can be source-dark: here the leading diagonal plaquette energy and its derivative are crucial, and b differs from a.
