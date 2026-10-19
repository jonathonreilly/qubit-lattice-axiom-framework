<!-- Owning original: PR9764; source SHA256 5aebd5b8282b788d0257ceb299abe5b633c680cdecdbcae738da0577579c823d. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# COM derivative strengthening: focused hard check

Disposition: DEMOTE / not established for the complete fixed-order pole. The existing real-momentum pole and dispersion statement are unaffected. The proposed slow-arm form argument is sound, but a necessary complex-momentum fast-channel estimate is missing. No repository edits or formal audit.

## What the form argument proves

Put K=2-T, H_f=K+fn on the Dirichlet half-line, and take a contour enclosing only the first eigenvalue with contour dimensions comparable to f^(2/3). Since 0<=K<=H_f,

 ||K^(1/2)(H_f-z)^(-1)K^(1/2)|| <= sup_{t in spec H_f} t/|t-z| = O(1).

The last bound follows from the first two Airy eigenvalue scales and their nonzero scaled separation; high energies contribute a bounded ratio. A sufficiently small fixed complex perturbation gamma-1 therefore preserves invertibility on this contour by the form resolvent formula. Analytic continuation preserves its rank-one Riesz projection. This is a legitimate fixed-complex-gamma slow-arm construction, not an illicit bounded-operator perturbation by an unbounded potential.

It does not, by itself, prove the sharpened local endpoint estimate O(f), the complex-gamma boundary shift O(f), or the precise uniform Airy expansion. Those require a complex-sector Bessel/Airy estimate (or equivalent local form/recurrence estimates). They look plausible for the isolated slow arm but are additional steps. Real-gamma endpoint estimates alone do not justify them.

## Material obstruction in the complete operator

The existing corrected fast-strip proof is explicitly a self-adjoint real-parameter argument at imaginary depth eta comparable to f_fast=O(lambda^3), in fast units. It uses the norm bound 1/eta, the identity ||R v||^2=Im<v,Rv>/eta, and real elliptic transfer matrices over O(1/f_fast) sites. A fixed complex gamma changes the fast kinetic operator by O(|Im gamma|); it is not an O(eta) perturbation. None of those estimates extends by the stated argument to a lambda-independent complex-gamma disk.

The regular two-dimensional fast-host saddle is not the problem by itself: its detuning remains comparable to lambda for gamma near one. The separate confined fast arm is the problem. Its closely spaced levels, at spacing comparable to f_fast, can produce local Green-function variation on shrinking parameter scales. A strip bound on its value does not bound parameter derivatives independently of lambda. Meromorphic poles of an eliminated arm may cancel in the complete determinant, so this observation is not a counterexample to the full pole's differentiability. It is, however, a concrete gap in the proposed uniform holomorphic proof. One must establish that cancellation plus a uniform simple-pole/derivative bound, or prove another damping/continuation estimate; it cannot be presumed.

Evenness in p does not resolve this. Since gamma=1-p^2/8+..., the second p derivative at zero probes the first gamma derivative. A shrinking complex-gamma radius therefore still loses powers in the curvature estimate. Generic Cauchy estimates from only a gamma disk of radius O(lambda^3) do not retain an O(lambda^4) differentiated remainder. Likewise the real-p O(lambda^4) remainder may contain rapid parameter dependence; no uniform velocity error follows from its magnitude alone.

## Conditional algebra and permitted conclusion

If a lambda-independent complex-p neighborhood with a holomorphic remainder bounded by C_m lambda^4 is actually proved for the complete pole, Cauchy immediately gives

 E''(0)/Jz = lambda^2/2 - alpha_1 lambda^(10/3)/48 + O_m(lambda^4),

and, at fixed small real p,

 E'(p)/Jz = lambda^2 sin(p/2) - (alpha_1/24) lambda^(10/3) gamma^(-2/3) sin(p/2) + O_m(lambda^4).

Thus the proposed leading velocity expression is algebraically correct under that additional hypothesis. At present retain these as formal/conditional derivatives, not controlled curvature or group velocity of the complete pole. The sound new result is the isolated slow-arm rank-one complex-gamma contour construction. A full microscopic propagation or pole claim remains further outside scope.

Reviewed inputs: /private/tmp/neutral_com_pole_root.md, /private/tmp/neutral-com-pole-check.md, and native/CORRECTED_FAST_STRIP_PROOF.md in /private/tmp/scalar-environment-20261017/.claude/science/physics-loops/neutral-composite-24h-20261018.
