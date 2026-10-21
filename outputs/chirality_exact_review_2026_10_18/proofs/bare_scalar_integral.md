# A prescribed bare scalar-exchange integral

This is a formal one-loop coefficient for a supplied massless Euclidean scalar stress and supplied spatial-TT plus instantaneous exchange kernel. It omits seagull vertices and counterterms and deletes the spatial zero mode. It is not a gauge-complete observable, an all-orders result or a controlled Planck-scale prediction.

In lattice units let s_mu=2sin(k_mu/2), c_mu=cos(k_mu/2), Q=sum_(i=1..3)s_i², x=s_4², theta_ij=delta_ij-s_i s_j/Q. The stress derivative at zero external momentum is

U^a_mm=sin(k_a)(1/2-delta_ma),
U^a_mn=-(delta_am s_n c_m+delta_an s_m c_n)/2 for m!=n.

The supplied bilinear exchange is

W(J',J)=J'^TT:J^TT/(Q+x)+[r'r/2-(r'A+A'r)/2+2P'_perp.P_perp+P'_L P_L/2]/Q,

where r=J44,A=theta:J_spatial,P_i=Ji4 and P_L=s.P/sqrt(Q). A spatial-TT projection of U^a vanishes. Direct contraction gives

W_inst(U4,U4)=[(5/8)sin² k4+(1/8)c4² Q]/Q,
W_inst(Ua,Ua)=[-(3/8)sin² ka+(1/2)x ca²-(3/8)x ca² sa²/Q]/Q

for spatial a. Include the massless scalar propagator1/(Q+x). The normalized k4 averages are

R=<1/(Q+x)>=1/sqrt(Q(Q+4)),
<x/(Q+x)>=1-QR,
<x²/(Q+x)>=2-Q+Q²R.

Cubic averaging of the spatial coefficient minus the time coefficient reduces the three-dimensional integrand to

d(q)=1/(16Q)+tau/(32Q²)-1/6+QR/6, tau=sum_i s_i⁴.

Write W3=integral d³q/(2pi)³ 1/Q, which is integrable at the deleted point in three dimensions. Four-dimensional permutation symmetry gives integral QR=3/4. Integration by parts yields

sum_i partial_(q_i)[sin q_i/Q]=1/Q-1/2+tau/(2Q²),

so integral tau/Q²=1-2W3. Boundary faces cancel periodically; the omitted small sphere contributes O(radius) and tends to zero. Thus

I_s-I_4=W3/16+(1-2W3)/32-1/6+(3/4)/6=-1/96.

With the supplied convention delta c_exchange=-16pi(G/a²)(I_s-I_4), the formal coefficient is pi G/(6a²). Watson's constant cancels and no empirical value is imported. The D2 quartic-time-derivative stress addition has zero first derivative at zero external momentum, so it does not alter this particular coefficient. This does not justify the campaign's general gravity, reflection-positivity, tuning or observational exclusions.
