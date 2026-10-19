# Distinct check: local witness for an actual mediated product seed

Conditional support; no correction required in this witness. The exact residual identity and outside-window operator bound follow from the stated corrected installation premises. They do not need an attached global gap, isolated-cell preparation theorem or a loaded stationary inverse. The stationary construction remains under separate review; its uncorrected literal addition of another j n_p is expressly excluded by the witness.

I read the complete witness at SHA25657892f7690a5f634c44c2fe0752c5cfb682d3fbfbda1aa4c1ca4edd45bb0fdee, the complete isolated mediator source/check, and the complete stationary interface. The latter still displays the port double-addition wording in its source snapshot. For this check the witness's explicit correction is a hypothesis: remove the existing j n_p contribution before installing the new path whose compression restores exactly j n_p. I do not certify the uncorrected stationary Hamiltonian or treat its under-review status as a completed premise check.

## Exact local vector calculation

On the single-head invariant sector, with shared internal vector iota_e and common diagonal c_att+2j+e, the first mediator's centered internal block is -A1. Its endpoint couplings are -gamma1 C_L and -gamma1 C_R. Because 0<q<J, the odd/even off-diagonal block JI+qS is invertible. Its finite geometric inverse implies

    C_L^T A1^-1 C_L=0,
    C_R^T A1^-1 C_L=(-1)^(n1-1)q^(n1-1)/J^n1,
    ||A1^-1 C_L||²=J^-2 sum_(l=0)^(n1-1)(q/J)^(2l)=d_n1.

Only these finite inverse identities are imported from the isolated-cell proof. No isolated low spectral projector is used.

For X_e=-gamma1 A1^-1 C_L iota_e, the internal rows of (H-E_e)(V_e+X_e) are -gamma1 C_L iota_e-A1X_e=0. The s0 row is gamma1² C_L^T A1^-1 C_L iota_e=0. The s1 row is gamma1² C_R^T A1^-1 C_L iota_e=t1 iota_e, with the sign exactly as stated. All remaining rows vanish. In particular X_e is supported solely on mediator1 and V_e solely on s0; no occupied amplitude is initially on s1, s2, p or the other two mediator paths. A single application of H therefore cannot propagate the newly produced s1 residual farther. The argument does not assert that subsequent powers or time evolution remain there.

The shared B cancellation is valid only because it acts identically on these head coordinates and B iota_e=e iota_e. Extra contacts on this support, unequal diagonal compensation, additional source edges, different head-number sectors or an unprepared internal state can invalidate the identity. These are explicit hypotheses, not consequences of the inverse calculation. The port convention is irrelevant to this particular residual vector's support but remains necessary to define the advertised actual apparatus consistently. Domain membership is required; the supplied bounded finite-range graph with finite-support vectors supplies it.

## Gram identities and the actual spectral projection

The head supports of V_e and X_e are orthogonal, and X_e^*X_e=c1 I_e. Thus Y_e^*Y_e=(1+c1)I_e, W_e is an isometry and

    (V_e-W_e)^*(V_e-W_e)
       =2[1-(1+c1)^(-1/2)]I_e.

The inequality delta_p²<=c1 follows, for example, by differentiating the two scalar sides from equality at c1=0: the left derivative is (1+c1)^(-3/2)<=1. No small-c1 expansion is needed. The residual norm is exactly |t1|/sqrt(1+c1).

The e=1,3 input subspaces and their internal images are orthogonal before spectral projection; the same head-only dressing map acts on each. Hence W is an isometry and ||V-W||=delta_p with no extra sqrt(2). This remains true with arbitrary passive references. It does not imply that E_H(I^c)W_e has orthogonal ranges for different e.

For the actual self-adjoint H, each energy outside the common union I lies at distance at least d from each corresponding E_e. The spectral theorem on the domain vectors gives

    ||E_H(I^c)W_e||<=||(H-E_e)W_e||/d.

For x=x1+x3, triangle followed by ||x1||+||x3||<=sqrt(2)||x|| yields the stated sqrt(2) residual charge. Contractivity of the same actual spectral projection on V-W then gives

    ||E_H(I^c)V||
      <=delta_p+sqrt(2)|t1|/[d sqrt(1+c1)].

This covers the full prepared operator, every outside spectral type and passive references. No global commutation [H,B]=0, gap, outside-mass orthogonality, absence of traps, or in-band regularity is presumed. Overlap between the two intervals causes no problem: being outside their union still implies both distance inequalities. If the displayed upper bound exceeds one, it remains valid and can trivially be capped at one.

## Length specialization, limits and exposure

For n1=2m-1 the sign of t1 is positive, so lambda_m=sqrt(3)t1 is positive and the specialization sqrt(2/3)lambda_m/[d sqrt(1+c1)] is correct. The geometric sum gives c1 increasing to gamma1²/(J²-q²) for fixed positive coefficients. The resulting nonzero preparation allowance is only a limit of this upper certificate, not an actual leakage lower bound. The witness is a mathematical comparison vector; the prepared state remains product V and its discrepancy is charged once.

The calculation establishes neither represented output, actual source pulse, mediator vacancy at readout, phase matching nor complete-device performance. No isolated-cell preparation or gap theorem is transferred, and the old unmediated sixth-moment formula is not used. The displayed residual identity is a useful local fact even while the rest of the mediated stationary construction remains conditional.

Root authored this witness and supplied its corrected port premise. I did not author the mediator or witness sources, but have shared prior source/attachment/phase ancestry and authored unmediated source and preparation-moment arguments. This is a distinct local algebra and spectral-bound check with that exposure disclosed; it is not blind review or recertification of the whole stationary apparatus. No scientific computation, spectrum, solver, dynamics, sweep, Git/canonical/publication/checkpoint/prompt/model change or delegation occurred. Only this review was created.

Exact inspected source identities:

- `mediated_product_seed_witness/PROPOSAL.md`: `57892f7690a5f634c44c2fe0752c5cfb682d3fbfbda1aa4c1ca4edd45bb0fdee`.
- `bipartite_mediator_supply/PROPOSAL.md`: `836caee25d87e31c757e8965b4de85d5998a613dcc5862072d6cddc2a380c8dc`.
- `bipartite_mediator_supply_check/REVIEW.md`: `78af05b19696d2cae2cf147c1e666c9c1a39ca0a2ba9c67a8d1746c12c72de8f`.
- `mediated_critical_source_interface/PROPOSAL.md`: `2972451d77aae751d5cf64c7022468e372d078a5bfda36b7a9c7b8477036596e`.
