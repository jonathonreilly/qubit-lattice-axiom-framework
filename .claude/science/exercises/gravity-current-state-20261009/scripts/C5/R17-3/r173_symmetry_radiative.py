"""R17-3 probes (c) and (d).
C1  (sympy) Under R14-5's shift S_c: rho_v -> rho_v + c, lambda -> lambda - kappa c (and every vacuum level shifted),
    Lambda_late := lambda + kappa rho_v,late is invariant, so the symmetry cannot constrain its value.
    Extended to the creation law: IE's equation R' = -3h is invariant (h_vac = 0); its datum C is translated, C -> C + c:
    a free action on R, with no fixed point.
C2  Affine symmetries of a bounded spectrum: a reflection E -> 2s - E maps spec to itself only about the midpoint s;
    the fixed energy is s = (E0 + Emax)/2, never E0 (unless the spectrum is a point).  Checked on the KS sea (r173_recordmap).
U   Lemma U (uniqueness of the ground-state reference): among shift-covariant references ref[H + c] = ref[H] + c,
    <H>_psi - ref >= 0 for all psi and = 0 for some psi  <=>  ref = E0 = min spec H.  Checked on random Hermitian H.
D1  Radiative sizes for (N), an independent constant: one-loop Coleman-Weinberg vacuum terms
    n m^4/(64 pi^2) [ln(m^2/mu^2) - c] at mu = m (order of magnitude n m^4/(64 pi^2)); RECALLED masses, d.o.f.
D2  (S) under a parameter change that flips which minimum is global (tilted double well, our universe stays in the
    + well): Lambda_late = V_+ - E0 jumps from 0 to 2 eps v when eps crosses 0 (P93 in miniature).
"""
import numpy as np, sympy as sp
rv, rvl, lam, c, kap = sp.symbols('rho_v rho_vlate lambda c kappa', real=True)
Lt = lam + kap*rvl
Lt_shift = (lam - kap*c) + kap*(rvl + c)
print("C1  Lambda_late before/after the shift: %s  ->  %s ; difference = %s" % (Lt, sp.simplify(Lt_shift), sp.simplify(Lt_shift - Lt)))
R, C, rho, h = sp.symbols('R C rho_tot h', real=True)
print("    IE: R = rho_tot - C ; under rho_tot -> rho_tot + c at fixed reader datum: Lambda_late = R - (rho_tot - rho_vlate) -> %s"
      % sp.simplify((rho + c - C) - (rho + c - (rvl + c))))
print("    i.e. the shift moves the datum C -> C + c (free translation); no value of C is a fixed point.")
rng = np.random.default_rng(1)
print("C2/U checks on random Hermitian H (dim 6):")
for trial in range(3):
    A = rng.normal(size=(6, 6)) + 1j*rng.normal(size=(6, 6)); H = (A + A.conj().T)/2
    w = np.linalg.eigvalsh(H)
    s = 0.5*(w[0] + w[-1])
    refl = np.sort(2*s - w)
    sym = np.allclose(refl, w)
    # candidates for ref: E0, trace/dim, midpoint ; test positivity on 20000 random states and attainment of zero
    psis = rng.normal(size=(20000, 6)) + 1j*rng.normal(size=(20000, 6)); psis /= np.linalg.norm(psis, axis=1)[:, None]
    ev = np.real(np.einsum('ij,jk,ik->i', psis.conj(), H, psis))
    for name, ref in [('E0', w[0]), ('Tr/dim', np.trace(H).real/6), ('midpoint', s)]:
        pos = (ev - ref).min() >= -1e-12 and (w[0] - ref) >= -1e-12
        zero = abs(w[0] - ref) < 1e-12
        print("   trial %d %-8s ref=%+.4f : weight>=0 on all states: %-5s ; some state weightless: %s" % (trial, name, ref, pos, zero))
    print("   trial %d: spectrum reflection-symmetric about its midpoint? %s (random H: generically no)" % (trial, sym))
print("   KS sea (r173_recordmap_vacuum.out item 3): the chiral reflection fixes the trace zero; the sea sits at -1.1938 per site below it.")
rhoL = 2.520e-47
print("D1  One-loop vacuum terms ~ n m^4/(64 pi^2) in units of rho_Lambda (RECALLED masses/dof; a re-tune is needed for each):")
for name, m, n in [('electron', 0.000511, 4), ('muon', 0.10566, 4), ('b quark', 4.18, 12), ('W', 80.38, 6), ('Z', 91.19, 3), ('Higgs', 125.1, 1), ('top', 172.7, 12)]:
    v = n*m**4/(64*np.pi**2)
    print("   %-8s: %.2e GeV^4 = %.1e rho_Lambda ; fractional mass change that shifts it by rho_Lambda: %.1e"
          % (name, v, v/rhoL, rhoL/(4*v)))
print("   EW tree step m_h^2 v^2/8 = %.3e GeV^4 = %.2e rho_Lambda (R5-3, counted once)" % (125.1**2*246.22**2/8, 125.1**2*246.22**2/8/rhoL))
print("D2  (S) with a tilted double well V = l (phi^2 - v^2)^2 + eps phi, universe in the + well (l = v = 1):")
for eps in [-0.02, -0.005, 0.0, 0.005, 0.02]:
    phis = np.linspace(-2, 2, 400001)
    V = (phis**2 - 1)**2 + eps*phis
    E0 = V.min()
    plus = phis > 0
    Vp = V[plus].min()
    print("   eps=%+.3f: V_+ = %+.5f, E0 = %+.5f, Lambda_late under (S) = V_+ - E0 = %+.5f (2|eps|v = %.3f when eps > 0)" % (eps, Vp, E0, Vp - E0, 2*abs(eps)))
