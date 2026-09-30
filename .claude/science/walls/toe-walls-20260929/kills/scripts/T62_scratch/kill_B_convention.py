"""Kill-check T62: route B (4D Poisson, N = past-light-cone 4-volume) under two unit conventions.
Inputs copied from the attacker's t62_counting_output.txt / t62_units_output.txt."""
import numpy as np
V4 = 6.396e242                 # Planck 4-volumes (attacker)
rho_over_rhoP = 1.134e-123     # H0=67.4, OmL=0.685 (attacker)
Lam_lP2 = 8*np.pi*rho_over_rhoP
s = np.sqrt(V4)
print("sqrt(V4) = %.4e" % s)
print("xi_rho    = (rho/rho_P)*sqrt(V4)  = %.4f  (attacker's pre-registered comparator; threshold 1.5 dec => 0.0316)" % (rho_over_rhoP*s))
print("xi_Lambda = (Lam*l_P^2)*sqrt(V4)  = %.4f  (Sorkin-style Lambda ~ 1/sqrt(V), G=hbar=c=1)" % (Lam_lP2*s))
print("log10 misses: rho-convention %.2f dec ; Lambda-convention %.2f dec" % (abs(np.log10(rho_over_rhoP*s)), abs(np.log10(Lam_lP2*s))))
print("pq for B = %.3f  (attacker's pre-registered prediction: 'exactly the laws with p*q = 2 pass')" % (0.5*np.log10(V4)/np.log10(8.073e60)))
