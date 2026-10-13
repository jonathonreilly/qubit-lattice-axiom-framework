# Source-exposed precision check: the scalar-band identification J

Status: required type correction in a historical sentence; no formula or
estimate correction found. This is an author/source-exposed analytic precision
check, not a blind review, retained audit, formal proof or new runtime result.

The exact independent DERIVATION.md has 390 lines and SHA-256
9597693aa9fc6aebb93de7419d4e4dbb74a6156531179fef27e6107e75cf7c96.
Its only literal J occurrences are lines 79–80. The accepted corrected859
source, WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md, SHA-256
c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b,
defines at lines 452–454 scalar conjugation C and J=Gamma C, explicitly
linear, unitary and energy intertwining. No threshold source was opened for
this check; the corrected859 source is sufficient.

Gamma and C are antiunitary. Consequently Gamma C is linear: for a complex
scalar z, Gamma C(z f)=Gamma(conj(z) C f)=z Gamma C f. Both factors are
surjective isometries between their stated bands, so J is unitary from the
positive scalar band to the negative band. C commutes with the scalar real
energy multiplier, and Gamma intertwines the band energies. Thus
E_- J=J E_+ on D(E_+), with J mapping the energy domains onto each other.
The same assertion holds for fractional powers by spectral calculus.

The corrected reading of independent390 lines 79–80 is:

> Let beta1=PK1P_-. In the accepted scalar band frame beta1 J has kernel
> lambda Delta(p,q) I_h,T(E(p)+E(q)), with J=Gamma C a linear, unitary,
> energy-intertwining map.

The original antiunitary adjective is mathematically wrong: beta1 is linear,
so an antiunitary J would make beta1 J an antilinear operator, inconsistent
with the stated ordinary integral-kernel representation. It must be corrected
in a new wrapper or edition; it is not silently reinterpreted as correct.

For the load-bearing estimate T5, right composition by this unitary preserves
the Hilbert–Schmidt norm. If (e_j) is an orthonormal basis of the positive
band, (J e_j) is an orthonormal basis of the negative band, so
sum_j ||E_+ beta1 J e_j||^2 = ||E_+ beta1||_HS^2. The displayed kernel and
E(p)<=E(p)+E(q) therefore give exactly T5, with the same constants and
Plancherel factor. This uses the linear/unitary J intended by corrected859.
It requires no additional regularity, moment assumption or domain change.

All subsequent inverse-block, graph-domain, positive-column, truncation and
projector arguments in independent390 use Z, its blocks, E and Gamma, rather
than J. Their antiunitary Gamma conjugations remain correct and are not
replaced by J. A literal occurrence scan of the full proof, independent
analytic evidence, comparison, decisive comparison evidence and root306
found no further J use. The root306 antiunitary conjugations refer to Gamma,
not Gamma C. No other type correction or consequent formula correction was
identified in that inspected scope. The existing analytical proof coverage
of the other formulas is reused at the pinned identities.

This corrects the earlier acceptance/review's unconditional statement that
no source correction was needed: one type adjective needs this explicit
precision. The frozen original independent proof, comparison, review and
acceptance are preserved unchanged. The finite-first-energy theorem and the
compared actual-cell graph extension retain their precise hypotheses and
conclusions. This precision does not turn an identity check into mathematics
certification and adds no threshold science or universal no-go conclusion.
