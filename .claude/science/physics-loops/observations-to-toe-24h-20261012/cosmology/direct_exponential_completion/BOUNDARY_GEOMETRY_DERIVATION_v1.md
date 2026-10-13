# Boundary of the normalized limiting field geometry

This is a further calculation about the supplied exponential candidate, not a new action or empirical fit. It explains one restriction in the conditional finite-interval convergence theorem. The metric below is the normalized limit g=lim(K/k), not the literal degenerate action obtained by setting k=0.

Put D=1+2(x^2+y^2)/3 and r=exp(-u/2)>0. The exact coordinate change gives

    g=dr^2+r^2 h,    h=diag(4/(9D),1/(3D)).

The fixed-transverse-field curve x=y=0 from u=0 to u=+infinity has normalized length integral_0^infinity exp(-u/2)/2 du=1. In r coordinates it ends at r=0 after finite length. Radial curves with fixed transverse coordinates are geodesics for this metric. The metric on r>0 is therefore not geodesically complete toward that endpoint. This is a property of the normalized Riemannian field metric, not a claim about cosmological trajectories in physical time.

Direct computation of the two-dimensional Gaussian curvature of h at x=y=0 gives K_h=7/2. Direct three-dimensional Ricci contraction for g gives

    R[g](r,0,0)=5/r^2.

Equivalently the tangential cone sectional curvature there is (K_h-1)/r^2, and the radial sectional curvatures vanish. The scalar divergence means this endpoint cannot be repaired by a smooth, nondegenerate Riemannian extension along this approach. It is not just a coordinate singularity of this normalized metric. The exact runner differentiates the metrics before evaluating at x=y=0; replacing D by its origin value before differentiation would erase the curvature.

The limiting potential becomes

    W=3(1-r^2)^2/2+r^4[x^2/2+y^2/3+2nu(log r)^2].

For fixed finite x,y and positive supplied nu, lim_(r->0+) W=3/2. Thus a divergent potential barrier does not close this endpoint. This statement is pointwise for bounded transverse fields, not uniform when x,y diverge with r. It does not prove that the frozen cosmological history reaches the endpoint, or exclude a separate energy/trapping proof for particular initial conditions.

The actual three independent new-action histories and the independent normalized-limit integration remain unchanged. Their finite observed u range avoids this boundary. The compact bounded-solution premise in REGULAR_LIMIT_DERIVATION_v1.md must remain explicit; positivity of the field metric and potential alone has not supplied it. No all-time existence theorem, quantum cutoff, ultraviolet completion or empirical constraint is inferred from this calculation. Overall canonical normalization rescales distances and curvature; it cannot remove the finite-distance singular endpoint of this normalized shape metric.
