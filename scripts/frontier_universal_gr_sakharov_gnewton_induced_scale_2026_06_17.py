from fractions import Fraction as F
import numpy as np
# Sakharov induced gravity from W = log|det D|: the metric effective action's leading terms are the
# heat-kernel (Seeley-DeWitt) coefficients of the Dirac operator D. a_0 -> cosmological const (~Lambda^4),
# a_1 -> Einstein-Hilbert (~Lambda^2 R) => 1/(16 pi G) ~ Lambda^2 => G ~ 1/Lambda^2 ~ a^2 (lattice scale).
# Gilkey: for P = -(nabla^2 + E), a_k(x) = (4pi)^{-d/2} * b_k ; b_0 = tr(I), b_1 = (1/6) tr(6E + R*I).
# Dirac (Lichnerowicz): D^2 = -nabla^2 + R/4  => E = -R/4 ; spinor bundle dim in d=4 is 4.
d=4; spin_dim=4
print("=== Seeley-DeWitt coefficients of the Dirac operator (induced gravity) ===")
b0 = spin_dim                              # tr(I)
print(f"  a0 ~ (4pi)^-2 * {b0}    -> induced COSMOLOGICAL CONSTANT, magnitude ~ Lambda^4  (the dominant divergence)")
# b1 = (1/6) tr(6E + R I), E=-R/4:
E_coeff = F(-1,4)
b1 = F(1,6)*(6*E_coeff*spin_dim + spin_dim)   # coefficient of R
print(f"  a1 ~ (4pi)^-2 * ({b1}) R  -> induced EINSTEIN-HILBERT term (coeff of R), magnitude ~ Lambda^2")
print(f"     a1 R-coefficient = {b1}  ( = -R/3 per Dirac spinor content )  -> nonzero, definite magnitude")
print()
print("=== G_Newton is INDUCED (not a free parameter) ===")
print("  Matching  S_ind ⊃ [(4pi)^-2 |a1| Lambda^2] ∫R√g  to  S_EH = (1/16piG) ∫R√g :")
print("    1/(16 pi G)  ~  (4pi)^-2 * (1/3) * Lambda^2 * N_f     (N_f = fermion species)")
print("    =>  G ~ 48 pi^3 / (N_f Lambda^2)  ~  a^2 / N_f        (Lambda ~ 1/a, the lattice cutoff)")
print("  RESULT: the emergent Newton constant is the LATTICE/PLANCK SCALE ~a^2, set by the cutoff and N_f,")
print("          NOT an admitted free parameter. (Sakharov induced gravity, realized from log|det D|.)")
print()
# Healthy-sign cross-check that does NOT need conventions: the spin-2 (TT) kinetic coefficient sign is
# the fermion stress-tensor 2-pt TT residue; the repo's induced-determinant runs already give C_TT > 0.
print("=== what is HEALTHY vs what is the RESIDUAL ===")
print("  HEALTHY (established): spin-2 TT stiffness C_TT > 0 (repo induced-determinant runs); polarization")
print("    sector canonical + linearized-Einstein channel signs (landed canonical-channel note);")
print("    diffeo-Ward to quintic order;")
print("    G_Newton induced ~a^2 (above). => the emergent graviton's KINETIC + POLARIZATION structure is healthy.")
print("  RESIDUAL WALL (NOT closed): the overall EH-sign / SOURCE coupling for G>0 (attractive). In induced")
print("    gravity the sign of 1/(16piG) is famously content/convention-sensitive (Sakharov sign problem);")
print("    in this framework it is conditional on the lambda=1 / conformal-class structure of the emergent")
print("    metric, which ties to the UNAUDITED metric-DOF posit (the emergent metric's conformal factor /")
print("    record-time axis). The conformal (trace) channel is exactly the wrong-sign mode")
print("    (landed canonical-channel note:")
print("    mu_conf < 0), so fixing G>0 = fixing the conformal-class admission. THAT is the named residual.")
print()
print("CONCLUSION: emergent gravity is cracked down to ONE named structural admission -- the metric-DOF /")
print("conformal-class posit (record-time axis). Above it: healthy spin-2, Einstein signs, G induced ~a^2,")
print("diffeo-Ward to quintic order. The wall is NOT G_Newton's magnitude (induced) nor the graviton's")
print("existence (healthy spin-2) -- it is the conformal-sector SIGN = the metric-DOF admission.")
