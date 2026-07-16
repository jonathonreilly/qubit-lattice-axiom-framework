# Route Portfolio

## Orthogonal attack frames

| Attack frame | Intended movement | Hard-residual pressure | Decisive test |
|---|---|---:|---|
| representation-ring positive type | constructive theorem | 3 | expand `exp[(beta/6) chi_(3 plus 3bar)]`; every tensor-power multiplicity is a nonnegative integer |
| explicit Peter-Weyl quadratic form | constructive theorem | 3 | diagonalize one-link convolution with eigenvalues `c_lambda/d_lambda` and tensor over spatial links |
| gauge-projector operator algebra | constructive theorem | 3 | prove `C_beta P_G=P_G C_beta`, identify its kernel with temporal-link integration, and factor `Q_beta>=0` |
| Osterwalder-Schrader half-space frame | independent conceptual check | 2 | compare the `M Q M` factorization with reflected half weights and identify any missing boundary term |
| finite nonabelian exhaustive model | exact runner/falsifier | 3 | on an `S_3` loop model, enumerate the projector, transfer trace, spatial insertion, repeated-source sandwich, and a pointwise-positive non-PSD control |
| source-algebra isometry | constructive scope repair | 3 | prove `I_p phi(U)=phi(U_p)` is isometric and `A_p I_p=I_p J`, without requiring `T I_p subset I_p` |

## Selection

The selected block synthesizes the representation-ring, Peter-Weyl,
gauge-projector, finite-model, and source-algebra frames. The OS frame is used
as a sign/order cross-check, not as a literature import.

The proof is blocked if and only if one of these exact identities fails:

1. `c_lambda(beta)>=0`;
2. `C_beta P_G=P_G C_beta`;
3. the `C_beta P_G` kernel equals the temporal-link-integrated mixed Wilson
   factor;
4. the trace of `(M Q M)^(L_t)` reproduces all spatial and mixed Wilson weights;
5. the spatial plaquette insertion lands on one slice as multiplication;
6. the plaquette-holonomy pullback preserves Haar inner products.

No negative global claim is planned, so the no-go-discipline gate is not
triggered by this selected route.
