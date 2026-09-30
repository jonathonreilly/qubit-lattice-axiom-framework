# Two-period positive filter: independent expansion before author proof

Root has received the author's new brief proposing t=U1+U2 and double frequency zeros; no new proof/code/results read. The mechanism exposure is explicit. This calculation independently checks its order-two coefficient, not the physical-time energy consumer.

Let omega=delta epsilon^-4, p=2pi/omega, and F_t=exp(tL)exp(-tH0). Let Q be its mean at t=U1+U2 with independent uniform[0,p] variables. It is unital CP. Its characteristic function chi(z) is the square of the one-period characteristic function, so chi(r omega)=0 and chi'(r omega)=0 at every nonzero integer r. At zero chi=1 and E[t]=p. For neutral inputs, the output is the true future-state average over a delay at most2p.

Take D to be the EXACT nonpositive-grade diagnostic, including H0 and every same-grade correction. It commutes with H0. Let Pplus be the positive-grade diagonal dissipator and Voff the off-diagonal superoperator difference, so L=D+Pplus+Voff. Put V(t)=exp(tH0)Voff exp(-tH0). On neutral O the exact algebra is

 (LQ-QD)O=E[F_t(Pplus+V(t))O].

The leading positive-grade term is Pplus O, of local order epsilon². Average V(t)O=0 exactly. Expand F_t once: I+integral_0^t B(s)ds+R2(t), B(s)=exp(sH0)(L-H0)exp(-sH0). Since Voff on neutral inputs has local strength epsilon^-1, R2 V is order epsilon³ on fixed support, while the correction multiplying Pplus is order epsilon4. The worst unprojected remainder order is therefore epsilon³.

Write superoperator Fourier components B_q and V_r with r nonzero on neutral inputs. The B0 V_r integral has coefficient E[t exp(i r omega t)]=0. For q nonzero, its coefficient is

 E[(exp(i(q+r)omega t)-exp(i r omega t))/(i q omega)]
 =delta_(q,-r)/(i q omega).

Therefore the surviving second-order term is sum_r i B_(-r)V_r/(r omega)=P_super B K1. B0 cannot contribute to the final neutral projection. This reproduces the signed homological feedback with its plus sign, while the single-uniform B0 K1 boundary term is absent. To leading order Boff=epsilon^-1 C1 and K1=epsilon³ k3, giving epsilon² P C1 k3. Exact Pplus and full same-grade D are retained.

The first expansion of Q itself is I+K1+p B0+O_local(epsilon4), because E[(exp(i r omega t)-1)/(i r omega)]=i/(r omega). The positive covariance completion has a larger diagonal coefficient p than the one-period value p/2. Higher repeated uniform convolutions may kill more frequency derivatives but do not remove the neutral feedback automatically. No such higher-order claim is made.

All local error statements require bounded-support linked actions with the actual registered append and uniform finite-range bounds. They are not global norm bounds, do not price a backward test spreading for physical time, and do not establish the missing integrated energy/residence estimate. Q preserves positivity of true future averages; its inverse or a fictitious Q-transformed state need not be positive.
