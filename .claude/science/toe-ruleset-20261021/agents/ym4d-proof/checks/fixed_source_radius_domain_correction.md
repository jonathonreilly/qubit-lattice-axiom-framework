# FR-DOMAIN-1: affected author correction

Status: frozen for affected independent confirmation; no author verdict.
Author: `/root/soft_fluctuation_covariance`, requested Astra/max configuration,
without independent backend attestation. The same-family independent reviewer
is `/root/review_fixed_source_radius`.

The original source is preserved by the coordinator in commit
`9c17b28bb27d5aae88063db081130ea7fe78d16b` with SHA-256
`9c628d8499abe6e8d23113f008f6c78c182b9ca52fdb6f87a73394cc13c6e882`.
The corrected source SHA-256 is
`6304245bdf27afa6c7f364da9bc41d8971cc0f2058c1e3484edef84df44cff86`.
The original receipt and read manifest are unchanged. Their original source
identity is historical, not silently restamped to the corrected source.

## Finding accepted

FR8 permits a reader holomorphic only near the finite closed disc of radius
`a=(1+r)p`. This does not define its full real Gaussian integral. For example,
`f(z)=(R-a)/(R-z)` for real `R>a` has modulus at most one on that disc and
a pole on the real Gaussian integration domain. Entire holomorphy alone is
also insufficient: `g(z)=exp(z^4-a^4)` has modulus at most one on the disc,
while its positive real Gaussian integral diverges. These analytic examples
confirm the domain defect; they are not numerical probes.

## Exact repair and proof scope

FR9 now compares only polynomial moments against the normalized full Gaussian
of precision `1+eta`, with its square-root branch fixed at eta=0. Linear
combinations are bounded by summing the displayed monomial estimates. It
expressly excludes arbitrary finite-disc readers and makes no general
entire-reader claim.

The U=0 determinant comparison now expands the remaining quadratic
exponential into polynomial coefficients. Its absolute summation is justified
separately on every mixed real/end domain by
`sum_(i<j) e_ij |z_i z_j| <= sum_i s_i |z_i|^2/2`, where
`s_i=sum_(j!=i)e_ij<=1/64`. For endpoint degrees k_i the summed integrand is
bounded by the product of
`|z_i|^(k_i) exp[-Re((1+eta_i)z_i^2)/2+s_i|z_i|^2/2]`.
This has positive real Gaussian precision `1-r-s_i`; the explicit end-segment
bound also remains Gaussian. On a changed real tail, reserving
`exp(-p^2/64)` leaves precision `1-r-s_i-1/32>0`. The end-segment estimate
`Re((1+eta_i)z_i^2)>=3p^2/4`, together with
`|z_i|<=(1+r)p`, leaves room for the same factor. Absolute integration and
summation are therefore justified before using the tree-moment estimates.
One does not sum a loose factorial bound over residual exponential degrees.
No nonlinear decoration is extended to the full real domain.

FR8, FR11, FR18-FR20 and their bounded finite-polydisc reader class are
unchanged. The actual nonlinear selected-sector statement, fixed source
radius, explicit vacuum/determinant/cube normalization, shrinking curvature
window and exact complementary integrals are unchanged. The Gaussian
comparison is used only for U=0; the nonlinear log difference continues to
come from the finite-contour mixed-decoration construction.

Only three source locations changed: the FR9 domain/definition paragraph,
the U=0 determinant-comparison proof, and the footer identifying the affected
receipt. There are no changes to a scientific checker, numerical criterion,
result, original read manifest or original receipt. All eleven non-source
artifacts in the original receipt were byte-verified unchanged. The reported
54/54 predicates are historical evidence, not a new run or a certification
of this analytic correction.

## Read evidence and authority

For this repair the author reread the complete original FR source, its
original receipt, and PROCESS_LIGHT. No new primary-source theorem or
literature premise is used. The original source's full-domain claim was
repaired in place; Git preserves its earlier version. The correction receipt
binds the new source, this note, historical identities and unchanged evidence.
The root coordinator owns Git, shared status, locks, publication and audit
operations. None was edited in this correction. Affected independent
confirmation is still required. Hard histories, full-transform nonvanishing,
interacting multilevel induction, continuum existence and physical mass gap
remain open.
