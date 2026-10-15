# Independent accelerated massless scalar response review

Reviewer `/root/inertial_response_check`; focused mathematics only, not a formal
audit. Root retains scientific authorship. This report freezes the independent
derivation and concrete controls before any new accelerated-response author
draft or code is read. The prior M5 inertial result is known and used only for
its constant-velocity limit. No observations or physical count model were read.

The exact massless laboratory-energy dual norm is obtained by pushing each
prescribed path into its direction-dependent arrival coordinate. It includes
acceleration and cross-path terms which cannot generally be discarded. The
joint direct-field and force response has a relative minus sign after this
change of variable. An arbitrary additive constant background is a separate
zero-energy obstruction for the direct-field part unless its total coefficient
cancels or the background is fixed.

## Independent result

For each unit vector n, prescribed path x(s), velocity u=x' and A=1-|u|², put

    d=1-n.u, tau=s-n.x(s), B=A(n-u)/d,
    C(tau(s))=c(s)/d(s), H(tau(s))=B(s).W(s).

The path is C2 and strictly subluminal with bounded acceleration on a finite
interval containing the coefficients. Compact real c is L2 and compact real
vector W is H1; the zero endpoint trace makes H compact H1. The phase map is
strictly increasing with a positive derivative margin on that compact interval.

In the massless energy completion of compactly supported smooth initial data,
with fixed constant background, the real Hilbert norm is ||h||²=2E. For a finite
sum over paths responding to the same field, the exact dual norm is

    G = 1/(8pi²) integral_S² integral_R
        |sum_j [C_j(tau)-partial_tau H_j(tau)]|² d tau dOmega.

The sharp bound is |L|² <= 2E G. Each path is extended by zero into one common
arrival coordinate before summation. Same-path pure force reduces to

    G_force=1/(8pi²) integral ds integral_S²
      |B.W' + Bdot.W|²/d dOmega,
    Bdot=[-2(u.u')(n-u)-A u']/d + A(n-u)(n.u')/d².

Thus C2 path regularity and bounded acceleration suffice; a jerk is not needed.
Substituting the instantaneous velocity into the inertial W'-tensor retains
only the B.W' square and is not generally exact or an upper bound. No general
reverse enclosure is proved here. A finite-mass extension is not established:
the massive phase is not k times a single arrival coordinate.

The derivation explicitly uses real Fourier pairing. With unitary spatial
transform, a real free field has arbitrary complex positive-frequency amplitude
a(k) and ||h||²=4 integral |k|²|a(k)|²d³k. The original coefficient of the joint
functional is Chat-ik Hhat. Since Fourier[H']=ik Hhat for the chosen negative
exponential convention, its arrival amplitude is C-H', not C+H'. Half-line
Parseval gives the displayed 1/(8pi²) factor.

For constant u=beta e and ell=log[(1+beta)/(1-beta)], the direct coefficient is
K=ell/(4pi beta) and the field-force cross vector is
S=(1-beta²)(2beta-ell)e/(4pi beta²). The local density is
K c²-2c S.W'+W'^T T W', where T is the immutable M5 inertial tensor. At rest,
K tends to 1/(2pi), S tends to zero and T tends to I/(6pi). At an instantaneous
rest event with acceleration v, the full density instead contains

    c²/(2pi) + 2c(v.W)/(3pi) + |W'|²/(6pi)
       + [|v|²|W|²+7(v.W)²]/(30pi).

Direct sphere quadrature checks these angular coefficients separately from the
laboratory plane-wave calculations below.

## Concrete independent controls

The pure-force run has 18 successful checks and zero failed checks. Its velocity
bump is u=beta sin²(pi s)e1 on [0,1], zero elsewhere, with a compact quintic
window W=e1 w that is constant on the moving interval and transitions only on
the stationary intervals [-1,0] and [1,2]. It is a valid C2 prescribed path and
compact H1 window. The instantaneous tensor substitution gives 10/(21pi) for
every beta, while the omitted acceleration square is strictly positive.

| beta | Instantaneous substitution | Exact derivative norm | Missing term |
| --- | --- | --- | --- |
| 0.2 | 0.151576136278 | 0.168680396410 | 0.017104260132 |
| 0.4 | 0.151576136278 | 0.224444144087 | 0.072868007810 |
| 0.7 | 0.151576136278 | 0.420567801431 | 0.268991665153 |

For beta=0.4, original laboratory plane-wave integration gives 0.224441920536
at k cutoff 80 and 0.224443868957 at cutoff 160. These approach the separate
derivative norm 0.224444144087, with signed errors -2.22e-6 and -2.75e-7. The
laboratory integral uses A(n-u).W and the phase s-n.x directly, with neither
Bdot nor an inverse arrival map in that oracle.

The joint run adds 27 successful checks and zero failed checks. It reuses only
the independently frozen elementary window, path and quadrature functions;
it does not rerun the pure-force suite. In the beta=0.4 plateau fixture with
c equal to the path acceleration component, the exact signed joint norm is
0.512773761190. The wrong plus-sign square gives 0.191858755529. Clock-only and
force-only contributions are 0.127872114272 and 0.224444144087, so merely adding
them omits the positive cross term 0.160457502831. Original laboratory joint
integration gives 0.512761867780 at cutoff 80 and 0.512772284404 at cutoff 160.
The latter differs from the exact derivative form by 1.48e-6 and decisively
distinguishes the sign.

For two distinct stationary paths, one direct-field window and one force window
with the same compact quintic shape, separate piecewise-polynomial time and
original plane-wave frequency integrations agree:

| Separation | Exact common-field norm | Lab Fourier norm, cutoff160 | Incorrect diagonal sum |
| --- | --- | --- | --- |
| 0.3 | 0.517600807330 | 0.517600806871 | 0.435436900580 |
| 0.7 | 0.571484456288 | 0.571484455828 | 0.435436900580 |

The real-time form is w(tau)-n1 w'(tau+n1 r), while the independent spectral
coefficient is what(k)[1-ik n1 exp(ik n1 r)]. Their cross term is at equal
arrival phase, not equal laboratory time. Coincident opposite responses cancel
exactly. The controls are correlated mathematical computations, not 45
independent observations, and finite numerical cutoffs do not prove the general
theorem or provide a rigorous truncation estimate. The full written derivation
supplies its domain and universal statement.

## Independently identified domain correction

If unrestricted finite-gradient-energy fields include h+h0 with arbitrary
constant h0, then energy and force are unchanged but the functional shifts by
h0 sum_j integral c_j ds. For nonzero total direct coefficient this rules out
an energy-only bound on that unrestricted class. The independent fixture has
integral c=2, h0=3 and response shift6 at zero added energy. The valid theorem
must use the anchored dot-H1 Sobolev representative (L6), or require cancellation
of the total direct coefficient so the observable is well defined modulo
constants. This was reported to root before access to any author draft; root
acknowledged that the author version would state the anchored domain explicitly.
No author source implementing that correction has yet been inspected.

Endpoint qualifications also remain essential. A force-window jump produces an
arrival-time delta after differentiation; an isolated direct field evaluation
is not an L2 coefficient. Those situations are outside the theorem as stated.
A physical application must demonstrate cancellation of any such terms or keep
the energy-bound application open. No actual one-way count derivation is included
in this independent assignment.

## Frozen evidence and scope

The pure-force freeze SHA-256 is
`999cba5e80ca715ed11517e593113939f2b06fda041eff18f14345cdd70ef14a`;
its result SHA-256 is
`81f9adb7290283578ca731375dce2e32b2377d50f34b68db150d0a0a4f18e98b`.
The joint freeze SHA-256 is
`25be3acf4716d8f47f7236f2f554622c629521d7a73fbefc3be43274ad59e7bb`;
its result SHA-256 is
`d7d38ec759d72ab293cb4dc36f53cde65b78bea952801a8b77c8b3adda37e9fe`.
The freeze records bind both derivations and independent programs before their
execution and before author access. Original stdout/stderr and exact source
hashes are preserved in this directory. No execution failure occurred in these
two runs; rejected instantaneous and wrong-sign candidates remain explicit.

The proof is massless, linear, common-field and based on prescribed paths with
the stated regularity. It derives neither actual path dynamics nor an action,
field-energy supplier, constant background, observational calibration or physical
clock/count model. The independently derived formulas are ready for a focused
comparison against exact author source identities, separately recorded after
those sources are provided. No source/index/branch/lock/publication mutation or
formal audit has been performed.
