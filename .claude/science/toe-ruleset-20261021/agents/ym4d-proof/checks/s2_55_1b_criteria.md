# s2_55_1b — criteria (written before the script). Supplements s2_55_1 C2/C4, which assume the right half of ROTDEF's
# Xi_v uses the sign xi~ = -a v (-(2a^2)^{-1})[pi(Q+) - pi(Q-)] (Q_pm = U^{-1} W_pm^{-1}, the same plaquettes based at the
# far end). If the opposite sign were ROTDEF's convention, the two halves' divergences would cancel and div Xi_v would be 0.
# ROTDEF §3.2 (C) fixes the sign: both halves must generate the same first-order variation.
Gate D1 (exact, SU(2), series in a real parameter t to order t^3): with U = exp(tA), W_pm = exp(tB_pm) (A, B_pm rational
traceless anti-Hermitian), the left generator xi = -(1/2)[pi(U W+) - pi(U W-)] (a = v = 1) and the right generator with
sign -1, xi~ = +(1/2)[pi(Q+) - pi(Q-)], agree at order t: coefficient_t(xi - U xi~ U^{-1}) = 0 (the right variation
U e^{s xi~} = e^{s U xi~ U^{-1}} U is compared as a left variation). PASS iff the t^0 and t^1 coefficients of
xi - U xi~ U^{-1} vanish and the t^1 coefficient of xi is nonzero (non-vacuous), on 3 data sets.
Control D1x (must FIRE): with sign +1 the t^1 coefficient of xi - U xi~ U^{-1} is nonzero.
VERDICT PASS iff D1 PASS and D1x FIRES.
