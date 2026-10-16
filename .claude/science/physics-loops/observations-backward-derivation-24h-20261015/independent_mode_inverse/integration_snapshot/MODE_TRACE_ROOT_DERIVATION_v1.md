# Pressure-trace reconstruction: root's post-exposure derivation

The focused checker independently found this four-column route before reading
root's five-coefficient inverse. Its frozen source is
`independent_mode_inverse/DERIVATION_BEFORE_AUTHOR_EXPOSURE_v1.md`.
Root then personally read that proof and its complete control program and
rederived the route below. This source and its calculations are post-exposure
integration, not a second independent discovery or independent CAS result.
The earlier root source and controls remain unchanged.

Use the primary inverse's action, clocks and variables. To avoid confusion with
the common measurement gain, call the additional background ratio G=x/b.
Let q=bx, ell=h-q, R=r/(M^2 A^2), Fbar=-x'-(3h-2q)x.
The original Einstein spatial trace becomes in matter time

    2P''+2(q+4ell)P'+(4ell'+4qell+6ell^2+x^2)P
                     -xw'+(Fbar-bR)w=0.             (1)

This follows by converting P_ddot=A^2(P''+qP'), H=Aell,
H_dot=A^2(ell'+qell), v=MAx and u=Mw in the Einstein pressure equation.
Its scalar pressure is v u_dot-v^2P-V_phi u, so the dust energy term is not
misidentified as pressure. In (1) use J=bw,
xw'=G J'-G(b'/b)J and x'/b=G'+G(b'/b). The coupling derivatives cancel.
Raychaudhuri gives R=-2h'+2q'-2hq+2q^2-qG. Thus

    2P''+8hP'+(4h'+6h^2)P = Atrace P'+Ctrace P
                                      +Etrace J'+Ftrace J,             (2)
    Atrace=6q,
    Ctrace=4q'+8hq-2q^2-qG,
    Etrace=G,
    Ftrace=G'+3(h-q)G-2h'+2q'-2hq+2q^2.              (3)

These are coefficients, not the conformal A or scalar force Fbar.
If the observed rows (P',P,J',J) have rank four, solve (2), set
q=Atrace/6 and G=Etrace, and check the other two coefficients. If qG>0,

    x=sigma sqrt(qG), b=q/x,
    R=-2h'+2q'-2hq+2q^2-qG>0,
    R'+(3h-2q)R=0.                                  (4)

The original background equations then construct the local A(phi),V(phi) as
in the primary note. Their fixed-density curvature is derived from their
force rather than supplied:

    kappa=(Fbar'+2q Fbar+3b ell R)/x
          =-x''/x-3h x'/x-3h'+2q'-6hq+4q^2+3ell R/G. (5)

The local scalar speed and coupling magnitude are reconstructed from these
data. Field reflection/origin and the positive A0 normalization remain as
in the primary construction. The exact local action class and the ideal
potential/clock/derivative readouts remain explicit conditions. This does
not determine the origin of initial modes or a global action extension.

The trace relation contains no explicit wave number. Consequently a rank-four
fit is only a necessary step. Define w=J/b and reconstruct Z,delta from the
momentum and Hamiltonian equations in the primary note, using the registered
kj2. Retain scalar KG and bare dust continuity as residuals. The particle
Euler equation follows from (2) and the background dust condition, but is also
checked explicitly. Full compatible inputs give a local original-equation
solution. The checker's example with shifted registered wave numbers passes
the trace fit but fails scalar/continuity: it is an intentionally incompatible
input, not a physical forward solution. This protects the sufficiency boundary.

Root's new computation reuses the FROZEN root-authored variable-coupling
original-equation forward generator from `check_mode_inverse_jets_v1.py`.
It separately constructs the pressure-trace design and response jets and
recovers their coefficients and first/second derivatives from the potential
histories using overdetermined least squares. Those reconstruct q,G,b,R,kappa
and are compared with the forward action only afterward. No checker code or
checker fixture is imported. This is a personal cross-check using root's
existing forward implementation, not an independent forward simulator.

The two inverses provide complementary equation-level tests. Root's original
five-column equation reconstructs curvature from the scalar response and then
checks background compatibility. The four-column trace route reconstructs
q,G and derives curvature from compatible background evolution, then checks
the scalar response. Their rank assumptions differ; neither is claimed
minimal or universal. A covariance/noise and physical measurement map is still
needed before treating either ideal data protocol as an observational test.
