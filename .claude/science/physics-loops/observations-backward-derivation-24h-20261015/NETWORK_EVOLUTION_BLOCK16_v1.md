# Test the adaptive connection without choosing its initial state

Personal follow-on to block15. The supplied adaptive action remains conditional;
this block eliminates its hidden initial state from a necessary measured-response
identity. It does not derive that state, the action, or the quantum measurement
rule. Standard differential elimination and weak testing are used, not claimed
as new general methods. No experimental record is fitted here.

## An input/output equation with arbitrary hidden preparation

Use the block15 equations with constant m,tau,k,C>0, real g, and lambda4:

    m*q'' + k*q + 4*lambda4*q^3 + g*w*q = f,
    tau*w'' + C*w = -g*q^2/2.

On an interval with |q|>=qmin>0, define quantities obtainable from a prescribed,
calibrated trajectory and its conjugate force:

    z=f/q, a=q''/q, b=q^2, Omega2=C/tau, G=g^2/tau.

Then z=m*a+k+4*lambda4*b+g*w. Apply D^2+Omega2 and use the w equation:

    z'' = -Omega2*z + m*a'' + m*Omega2*a + k*Omega2
          + 4*lambda4*b'' + (4*lambda4*Omega2-G/2)*b.

Every homogeneous w solution is annihilated. The identity holds for arbitrary
initial w,w' on every trajectory, even if preparation changes between trials.
There is no periodic-branch, reset, uniform-ensemble, or common-initial-state
premise. This is a genuine removal of those premises from this necessary test.
It is not a prediction of a trajectory without initial data.

The relation alone cannot identify the actual microscopic mechanism; any other
realization with the same input/output law passes. At g=0 the eliminated
equation also has spurious homogeneous solutions unless z=m*a+k+4*lambda4*b
is imposed separately. This is another reason to claim necessity, not an
unqualified equivalence. Division through q=0 is excluded; no global
reconstruction through zeros is asserted.

## A finite-window identity that avoids differentiating measured force

Choose a real twice differentiable test function psi with psi=psi'=0 at both
ends of a finite window. Twice integrating by parts gives

    integral z*psi'' =
      c_z*integral z*psi + c_a2*integral a*psi''
      + c_a*integral a*psi + c_1*integral psi
      + c_b2*integral b*psi'' + c_b*integral b*psi,

    (c_z,c_a2,c_a,c_1,c_b2,c_b)
      = (-Omega2,m,m*Omega2,k*Omega2,4*lambda4,
         4*lambda4*Omega2-G/2).

The boundary terms vanish for every hidden preparation. Time derivatives of
the measured force are not required; q'' still must be supplied by the known
actuation history or independently calibrated. Errors in actuation are not
silently removed by this reformulation.

A common candidate fitted across different histories must satisfy

    c_z<0, c_a2>0, c_1>0,
    c_a = -c_z*c_a2,
    G=2*(-c_z*c_b2-c_b)>=0.

These are restrictions on a shared fit, not separately adjusted parameters
for each history. The potential stability inequality from block15 becomes

    lambda4>=G/(8*Omega2)  iff  c_b>=0,

under the positive Omega2 domain. Thus stability supplies a directly checkable
coefficient sign within this measurement model. It does not fix c_b to zero
or select the potential. The observable combinations do not fix g's sign or
the separate normalization of the unobserved w coordinate.

Identifying six coefficients requires a full-rank collection of the six
integral columns and controlled conditioning. A constant trajectory supplies
no such guarantee; its a,b derivative columns vanish and others are dependent.
Our synthetic example uses several prescribed positive waveforms, different
hidden preparations, and disjoint additional waveforms for a numerical
prediction check. These are simulated controls, not an independent empirical
test or evidence that any apparatus obeys this action.

## A deterministic uncertainty bound for a frozen candidate

With candidate parameters fixed before a test window, suppose errors in z,a,b
are bounded pointwise by eps_z,eps_a,eps_b. Let

    P=psi''+Omega2*psi, B=4*lambda4*psi''+
      (4*lambda4*Omega2-G/2)*psi.

For residual integral [(z-m*a)*P-k*Omega2*psi-b*B],

    |delta residual| <= (eps_z+m*eps_a)*integral |P|
                       +eps_b*integral |B|.

This permits arbitrary correlated errors. Parameter uncertainty, quadrature
error, unmodelled modes, and error in the time coordinate need separate bounds;
the pointwise inequality is not a statistical confidence statement. A positive
lower bound for both actual and reconstructed |q| is needed when obtaining
ratio-error bounds from primitive q,f uncertainties.

## What this changes for the campaign

The useful direction is to test a single neighborhood-evolution response over
multiple controlled histories. Hidden preparation can be eliminated rather
than supplied for this necessary test. Action selection, actual force and
coordinate identification, the quantum outcome process, and a real independent
dataset remain open. This does not erase the physically different initial
states; it constructs an observation that is insensitive to them within the
chosen candidate class.
