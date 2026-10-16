# Remove the nonzero-coordinate restriction from a necessary response test

Root's final extension of block16 within the same supplied block15 action.
This derives a division-free weak identity that tolerates coordinate zero
crossings as well as arbitrary hidden preparation. The action, regularity,
physical actuation/readout and time calibration remain conditional.

Write R=f-m*q''-k*q-4*lambda4*q^3=g*q*w and Omega2=C/tau,
G=g^2/tau. Direct product differentiation, without division by q, gives

    q^2*R''-2*q*q'*R'
      +(2*q'^2-q*q''+Omega2*q^2)*R+(G/2)*q^5=0.

The terms involving w and w' cancel; the remainder is
g*q^3*(w''+Omega2*w)+(G/2)*q^5, zero by the hidden equation.
It is valid at zeros of q for sufficiently smooth actual solutions. No
limit through 1/q is taken.

For a finite-window test function psi with psi=psi'=0 at both ends, define

    A=q^2*psi''+6*q*q'*psi'+(6*q'^2+3*q*q'')*psi,
    B=q^2*psi.

Two integrations by parts on R'' and one on R' yield
integral R*(A+Omega2*B)+(G/2)*integral q^5*psi=0.
The boundary terms vanish independently of hidden data. Also integral q*A=0,
as the same integration by parts, or direct substitution of R=q, verifies.
Thus the observable relation is

    integral f*A = -Omega2*integral f*B
      +m*integral q''*A +m*Omega2*integral q''*B
      +k*Omega2*integral q^3*psi +4*lambda4*integral q^3*A
      +(4*lambda4*Omega2-G/2)*integral q^5*psi.

This uses exactly the same six shared coefficients and consistency/stability
conditions as block16. Neither measured force derivatives nor division by
the coordinate appear. Arbitrary hidden initial states can differ on each
trajectory. Actuation derivatives q',q'' and adequate regularity still enter.
Classical pointwise derivation can use smooth q,f; the finite integrals can be
defined more weakly, but no distributional existence theorem is claimed.

For an exactly known q trajectory and frozen candidate parameters, a
pointwise force error eps_f gives

    |delta residual| <= eps_f*integral |A+Omega2*B|.

Errors in the actual trajectory, its derivatives, parameters, clock and
quadrature need additional bounds. Removing 1/q does not remove calibration
or guarantee favorable signal-to-noise near an almost-zero trajectory.

This is a necessary test, not a sufficient global reconstruction. A trajectory
identically q=0 makes every displayed integral vanish even for an arbitrary
reported force, whereas the original force equation requires f=0. The
eliminated test loses information there. Zero coupling also retains block16's
spurious homogeneous solutions. Full-rank excitation and separate physical
checks remain needed; no initial state, fundamental potential or quantum
probability law has been derived.

The numerical control uses signed, zero-crossing imposed histories with
different hidden preparations, estimates the common six coefficients on three
synthetic shapes, and checks an additional shape without refitting. These
are simulated validation cases only.
