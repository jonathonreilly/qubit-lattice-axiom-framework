# Focused v2 interval classification and repaired-domain comparison

Root remains scientific author. This is a post-exposure mathematical/source correspondence check, not a formal audit or a new empirical analysis. Original proofs, v1 source snapshots, the negative-q finding and its witness are unchanged.

## Scope and identities

I captured `WORKING_v2.md` before reading it: SHA256 `0aad424f1fd7fe582c7005edab096e7e0a3787ef8ef84ca2ccd813d3490a6397`, 9,173 bytes / 183 lines. The full source was displayed, but this report assesses only physical continuity, the linear lift, interval classification equations (1)–(4), and the tensor discriminator. Background equations (5)–(10), empirical/literature assertions and the claimed 259 author controls are outside this assessment.

I subsequently froze `growth_inverse_v2.py`, SHA256 `fefc0b0552ce7baef474d018ea4f60bd5437ec5d7fdfa51b116b57e2b1d80e01`, 4,708 bytes / 122 lines. I read the full `real_number`, `positive_q`, `coupling_shape`, `validate_rows`, `integrated_inverse`, `lift_inverse` and `tensor_inverse` function bodies. I did not assess the background helper bodies or run an author aggregate. No extended-results file or empirical data was opened. Both frozen sources have immutable copies and exposure receipts in this directory.

## Conservation and lift

The physical-velocity correction agrees with my frozen continuity supplement. Euler supplies the same force/Weyl quotient using W, while exact linear continuity gives delta/W0=J+C with J=integral What+3(Phihat-Phihat0). The displayed potential map uses the measured slip r, correctly distinguishing it from a geometric q obtained through a separate finite-mass inverse. Its sign and factor one-half follow from Phi=(1-r)(Phi+Psi)/2. All channels must share the fixed mode normalization and physical clock/wavenumber calibration.

The conditional Weyl discrepancy endpoint identity follows by multiplying L=b delta/F+epsilon_L by F and subtracting endpoints. The endpoint bound uses F_i>0 and cannot estimate the physical epsilon_L bounds itself. Correcting continuity does not remove gravitational quasistatic/source errors.

The lift row and parameter ordering are correct: [1,-Jq,-q,-P What(1-3q)] times [C,u,w,v] equals -J, with u=1/beta, w=uC and v=1/B. The source checks augmented-rank consistency, full rank, the nonlinear product identity, 3<u<4, positive v and q<1/u. Its newly shared q guard also imposes positive q. The admitted row equations then imply J+C>0 on the supplied positive P,What branch. Finite rows do not certify all unsampled epochs.

## Equation (3): necessity and uniqueness boundary

Let A_i=B_i/beta_i and D_i=A_i(J+C_i)>0. Equality of the two reduced readouts gives D1(beta1-q)=D2(beta2-q). If the coefficient D1-D2 vanished at a point, the equality would give D1(beta1-beta2)=0, impossible for distinct beta and D1>0. Equation (3) therefore has no hidden zero denominator on the physical interval.

If J has a nonconstant interval range and q varies, equation (3) is a nondegenerate fractional-linear function of J. Thus q not representable by such a fractional-linear function on that range permits at most one beta. This statement assumes a candidate exists and concerns exact functions: it is not an error-tolerant identifiability result. For a fixed beta and nonconstant J, B and C are also fixed by the affine relation. If J is constant, that additional uniqueness of B,C need not hold.

A varying-q fractional-linear relation is a necessary exceptional condition for two shapes, not sufficient by itself. The observed P What and all positivity gates must also support both. The source states this through the premise that candidate 1 is valid and the separate second-tuple gates.

## Equation (4): exact second-shape classification

Write q=(u0 J+v0)/(w0 J+x0), with determinant Delta=u0*x0-v0*w0 nonzero. Define

    l_beta(J)=(beta*w0-u0)J+beta*x0-v0.

Multiplying the common readout identity by its nonzero denominator gives

    (B1/beta1) l_beta1(J)(J+C1)
      =(B2/beta2) l_beta2(J)(J+C2).                           (A)

On a varying-J interval this is a polynomial identity. For distinct beta1,beta2, the determinant of the two linear factors equals (beta1-beta2)Delta, so they have no common zero. If both factors are nonconstant, l_beta2 must therefore be proportional to J+C1, while l_beta1 is proportional to J+C2. Their roots and leading coefficients give exactly the three formulas (4). Substituting them makes (A) identically zero; the independent symbolic check confirms this without using the author implementation.

This proves necessity and sufficiency for a SECOND DISTINCT FINITE physical tuple only when all of the following hold: a valid first tuple, varying J on an interval (equivalently varying observed q under the nondegenerate relation), nonzero rational denominator throughout it, nonzero formula denominators, beta2 distinct from beta1 and inside (1/4,1/3), 0<q<min(beta1,beta2), B2>0, and the stated positive readout/density gates. No extra third distinct beta can occur under those hypotheses.

The denominator cases have definite meanings:

* If x0-w0*C1=0, nonzero Delta implies v0-u0*C1!=0; no finite beta2 makes l_beta2 vanish at -C1. This is an algebraic-continuation pole, not a physical zero-density epoch.
* If beta1*w0-u0=0, l_beta1 is a nonzero constant. The left side of (A) has degree one, whereas a distinct finite beta2 would give degree two with nonzero B2. Such a second tuple cannot exist.
* Given nonzero Delta and x0-w0*C1, the apparent denominator beta2*w0-u0 equals -Delta/(x0-w0*C1), automatically nonzero.
* If the formulas return beta2=beta1, the exchanged factors are a repeated root; this returns the original tuple, not a distinct solution.
* A formal second beta inside the shape interval can nevertheless give B2<0. For example, on 0<=J<=1, q=(11J-19)/(40(J-2)), beta1=29/100,C1=3,B1=1. Here q decreases from 19/80 to 1/5, below beta2=13/50, but (4) gives B2=-26/29 and C2=-7. The second physical tuple must be rejected. Positive B is substantive, not redundant.

A precise local clarification was sent to root: state varying J/nonconstant observed q immediately before (4). A nondegenerate rational expression evaluated at one constant J does not itself imply varying observed q; W>0 does not ensure delta'=J'W0 is nonzero. The source already treats constant q separately and earlier explains this limitation, so this is a requested explicit scope clarification rather than a disagreement with its intended branch. The reviewed bytes predate the promised wording addition.

The constant-q branch remains separate. With nonconstant J and compatible positive-slope affine P What, every chart-admissible beta can rescale B. With J constant, the degeneracy can include B and C separately. The independently frozen varying-q ambiguity fixture also reproduces equation (4) exactly. A calibrated tensor ratio at two distinct q values remains injective in beta; this supplies no absolute F scale or physical tensor calibration by itself.

## Exact controls and domain repair

Fourteen new focused exact checks pass: general substitution, denominator identity, linear-factor determinant, both exchanged factors, the two denominator edges and degree drop, repeated-root behavior, a negative-B refusal witness, the previous positive interval fixture, and the constant-J scope warning. These checks are post-exposure source checks and are separate from the original 43 independently derived controls. No ODE or aggregate run was added.

The repaired source's `real_number` requires SymPy's finite-real predicates to be exactly true. `positive_q` then requires 0<q<1/3. Both inverse functions call it; the integrated inverse obtains it through `validate_rows`. The tensor inverse additionally requires positive F_ratio, distinct q endpoints, a finite inverse denominator and the candidate chart. Thus the earlier missing-lower-domain defect is repaired in the reviewed v2 bytes.

For affected execution only, I supplied the ORIGINAL preserved negative-q witness to these two repaired functions. Both now reject with ValueError, 'positive candidate coupling below one third required'. The receipt is Q_DOMAIN_REPAIR_CHECK_v1.json. I did not repeat the author aggregate, the original 43 controls or the separate background checks. The v1 defect and its original positive returns remain preserved.

## Disposition

No additional mathematical discrepancy was found in the reviewed v2 conservation/lift/classification formulas under their explicit interval and domain conditions. The varying-J wording clarification remains to be bound to later source bytes. F1 is closed for the exact v2 function snapshot above. Complete background membership, empirical admission, physical scale calibration and formal review status are outside this report.
