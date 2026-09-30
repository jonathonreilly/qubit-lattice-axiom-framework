# Actual bright-hole linear-field residence

Author proof candidate, not yet independently checked. This is an actual common-physical-time partial bound for the unchanged microscopic law and bare Omega of CONTRACTfc46be59. It uses the previously focused-checked DEFECT(D10), local circuit/jump expansion and FIRST_FIELD_MOMENT. It does not assume the new quadratic-energy reduction; root subsequently supplied receipt2c0d2830 for that separate reduction.

Let N=|A|, C_S=S(S+1), epsilon² C_S=delta/K. Work at finite spin and safe even torus, uniformly before taking either limit. Put

    b_h = 1 - product_(b~h) n_b,
    R_h = w_h b_h q_h,
    q_h = 1 + sum_(e in Z_h) |E_e|,

where the sets Z_h are translates of a fixed finite link set of size r, with bounded incidence. For the residence consumer take all links whose A endpoint is within graph distance two of h, so r<=114. The projection w_h b_h is a bright hole: at least one adjacent B is empty. It is a proof test, not an additional monitored outcome. q_h commutes with it.

For every fixed T there are constants independent of S and volume such that

    epsilon^-2/N integral_0^T sum_h <R_h>_sigma dt <= C_(r,T),    (B1)
    epsilon^-2/N integral_0^T sum_h <R_h>_rho dt <= C'_(r,T).     (B2)

Here sigma=Y rho Y*, with exact local normal-form Y and the actual microscopic rho. All later births and all original coherent gain/loss terms remain in that state. No first-event approximation is made. The rotated UNWEIGHTED bright reward has the stronger bound

    epsilon^-2/N integral_0^T sum_h <w_h b_h>_sigma dt
                                                   <= C_T epsilon. (B3)

There is no claim of the same vanishing rate in physical coordinates. Bare virtual bright holes can contribute to the coordinate return at order epsilon². Translation invariance of the PHYSICAL law/Omega turns(B2) into the same bound at each fixed center; no translation covariance of Y is presumed.

## 1. Original loss and its exact spin minimum

Let G_h=sum_(mu at h) j_mu* j_mu, keeping separately the original resolved instrument and original unnormalized coherent-edge instrument. Both have the identical positive diagonal effect

    G_h = w_h sum_(b~h) (1-n_b) [2-2E_hb²/C_S].               (B4)

For a coherent edge, the two created A charges are orthogonal, so the effect has no sign cross term. Their output coherence has not been discarded from the dynamics. The loss equality does not identify the two instruments.

Since |E_hb|<=S on the actual box,

    G_h >= 2/(S+1) w_h b_h.                                  (B5)

This includes every exact boundary zero of an individual signed shift: the other sign retains squared weight2/(S+1). Equation(B5) is an operator inequality on the full tensor carrier and hence on Gauss states and with any reference ancilla. It imposes no restriction on other holes, distant B records or local field correlations.

## 2. The bare loss has a smaller actual integrated activity

The exact dressed original jump has grade-minus-one part

    J_(mu,-1) = j_mu + epsilon² K_mu(epsilon),
    ||K_mu(epsilon)|| <= c,

with uniformly bounded local support and incidence. Its first-order correction has grades0 and-2; this is the actual parity/grade calculation in DEFECT, not a splitting of the observed instrument. The squared triangle inequality yields

    sum_mu j_mu* j_mu
       <= 2 sum_mu J_(mu,-1)*J_(mu,-1) + c epsilon^4 N I.

The complete original-state estimate(D10) therefore gives

    kappa epsilon^-2 integral_0^T sum_h <G_h>_sigma dt
        <= 2 integral_0^T <D_minus>_sigma dt
                                      + c kappa epsilon² NT
        <= C_T epsilon² N.                                  (B6)

Only the positive grade-minus-one contribution is bounded by D_minus. All other grades and their original coherences were retained in the derivation of(D10); they are not removed from sigma. This diagnostic activity is not the physical original count rate.

## 3. The finite-spin price is exactly affordable at linear weight

Since q_h<=1+rS, equations(B5)-(B6) imply

 epsilon^-2 integral sum_h <w_h b_h q_h>_sigma
     <= (1+rS)(S+1)/(2kappa)
                    [kappa epsilon^-2 integral sum_h<G_h>_sigma]
     <= C_T epsilon² (1+rS)(S+1) N/(2kappa)
     <= C_T (r+1) delta N/(2kappa K).                         (B7)

The final step uses S>=1 and the stipulated combined scaling. This proves(B1). The same proof with q_h=1 gives(B3), since epsilon²(S+1)<=C epsilon at fixed delta/K and epsilon<=epsilon0.

No physical first field moment or weighted preparation was needed for(B1). The linear field norm price contributes S and the bright loss minimum contributes S; their product is paid by the actual epsilon² activity in(B6). Replacing q_h by q_h² would cost epsilon² S³, which is not uniformly bounded. That route supplies neither quadratic residence nor linear-weight uniform integrability.

## 4. Returning the positive reward to physical coordinates

We give the local weighted circuit estimate needed for(B2), rather than use a global norm of Y-I. Set X_h=sqrt(R_h). Choose a fixed enlarged finite link set Z'_h containing the complete circuit cone of R_h, and Q'_h=1+sum_(e in Z'_h)|E_e|. Then

    ||[X_h,Y*] (Q'_h)^(-1/2)|| <= c epsilon.                  (B8)

Here is a direct uniform proof. In the field/matter basis, X_h is diagonal with 0<=X_h(alpha)<=sqrt(Q'_h(alpha)). For any local matrix A with field displacement d(alpha,beta),

 |X_h(alpha)-X_h(beta)|/sqrt(Q'_h(beta))
                                     <= 1+sqrt(1+d(alpha,beta)).

A matter projection can change abruptly; the displayed bound allows that. Row and column Schur estimates thus bound [X_h,A](Q'_h)^(-1/2) by a constant times the first-displacement Schur norm of A. Products with local gates are controlled by the same weight-ratio inequality. All coefficients of the fixed-order local normal-form gates have uniform displacement Schur norms, including diagonal normalized compensation and exact forbidden spin paths. Local exponentials and their analytic remainders preserve those bounds.

Only gates in the fixed circuit cone act on X_h. Expanding each such gate about its identity gives a weighted O(epsilon) difference, since each exponent starts at order at least one. The number of gates in the cone is uniform. Finally factor

    [X_h,Y*] = Y* (Y X_h Y* - X_h).

The left global unitary is harmless; the difference in parentheses is local. This proves(B8) without a global Schur bound for Y or a false global small-norm approximation.

For a vector psi, squared triangle and(B8) give

    ||X_h Y* psi||² <= 2||X_h psi||²
                                  + c epsilon² ||(Q'_h)^(1/2)psi||²,

hence, as positive forms,

    Y R_h Y* <= 2 R_h + c epsilon² Q'_h.                     (B9)

Mixed states and ancillas follow by positive trace. The checked first field moment in sigma and bounded incidence imply

    sum_h <Q'_h>_sigma(t) <= C_T N,  0<=t<=T.

Integrating(B9) proves(B2). This return uses an ordinary unconditioned first moment only in an epsilon² remainder; it does not assume the sought conditional hole-field estimate.

## 5. Exact remaining dark reward and scope

The full positive reward splits without cross terms:

    sum_h w_h q_h = sum_h w_h b_h q_h
                + sum_h w_h product_(b~h)n_b q_h.            (B10)

Consequently, in either coordinate system, uniform scaled FIRST-field residence is equivalent to a bound on its dark summand, up to the already bounded bright part. Both summands are positive. The checked signed-current reduction may now use(B1) to discard the bright part at bounded cost, but it still needs the actual dark contribution or a weaker direct signed-current cancellation.

This result is about an integral, not pointwise conditional field laws, hazard identification or tails of the weighted reward. It does not infer a uniform spin fast gap, a source probability for dense B islands, field uniform integrability, or a full quantum generator. No new computation is used: the exact scalar loss and the source-bound activity/circuit estimates prove the result.
