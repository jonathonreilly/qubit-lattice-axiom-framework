# Microscopic two-port columns and bound states: distinct check

No required mathematical correction was found. The exact scattering matrix, mediator column and central-band bounds have the stated signs, phases and constants. The point-spectrum conclusions also hold: each legal sector has one symmetric eigenvalue above D; the disabled relative operator additionally has exactly one negative eigenvalue, while the enabled sector has none. These are statements about the specified infinite-lead operator. They do not supply a complete normalized scattering transform, a finite-seed packet comparison, or a new runtime certificate.

## Pins, reuse and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

* New source, completely read and SHA-256 verified: `common_product_microscopic_scattering/PROPOSAL.md`, `59b59ea3fc51e6ae364716a63ff4b9e001390cba112f48f0b4214c01318865a6`.
* Previously fully read microscopic cell source, hash refreshed unchanged: `mediated_common_product_program/PROPOSAL.md`, `739e99c44feb30f0bdc569d804f0e643ff993ab556056e1b6820f7012a9de088`.
* Previously fully read ideal-router source, hash refreshed unchanged: `common_product_autonomous_interface/PROPOSAL.md`, `bcc47793a94d578fcbf403115dcce099f6728752d0953a03d80051f75d3e22b5`.

The earlier finite composition and ideal-router checks are reused only for the established physical conventions and half-integer channel bases. The scattering geometry removes the finite source ends and is not that finite device. ROOT suggested the Robin formulas and packet route; I read the candidate before reconstructing its boundary equations and spectral arguments. This is source-exposed same-model checking with inherited effort, not blind or model-diverse replication. No separately developing packet result was read or used. Existing workflow snapshots are reused; no retained or formal audit status is assigned.

## Exact boundary equations and phase

After subtracting the common scalar 2b, the cell expansion gives endpoint onsite a_p, mediator onsite D_p and the two hoppings -b. Adding one radial lead bond contributes j to each n=0 diagonal. Thus the proposed endpoint equation is `E psi_0=(j+a)psi_0-j psi_1-bm(1,1)^T`. The mediator equation is `(D-E)m=b(psi_L,0+psi_R,0)`, with a positive right-hand sign. The relative operator is bounded and self-adjoint on the one-head space; positivity belongs to the full generator 2bI+h, not necessarily h.

Resolving symmetric and antisymmetric ports diagonalizes the matrix (1,1)^T(1,1) into eigenvalues 2 and 0. Elimination therefore gives v_+=a/j-2b²/[j(D-E)] and v_-=a/j. For a scalar boundary wave z^-n+s z^n, substituting E/j=2-z-z^-1 yields

    (1-v-z)+s(1-v-z^-1)=0.

Solving gives exactly `(1-v-z)/(z^-1-1+v)`. Its numerator and denominator have opposite real parts and equal imaginary part -sin k. For real v and 0<k<pi, the denominator cannot vanish and |s|=1. Substitution gives s(0)=z and s(2)=-z. With a_0=2j and a_1=0, the displayed enabled and disabled values of v follow. In both programs only the symmetric scattering eigenvalue differs from the ideal value z. The common momentum-dependent factor z has not been removed.

For general incoming f, psi_0=(I+S)f/sqrt(2pi). Since (1,1)f=sqrt(2)f_+, the mediator amplitude is precisely (6), including its factor sqrt(2), denominator sign and Fourier normalization. Summing one and s gives `(z^-1-z)/(z^-1-1+v)`. Antisymmetric input has exactly zero mediator amplitude. These checks fix the complex column rather than merely its squared magnitude.

Unitarity here establishes conservation of channel flux for equal lead velocities. It does not establish orthonormal generalized eigenvectors or completeness of a transform onto the physical space. In particular the bound-state channels checked below cannot be omitted from a purported complete transform.

## Central-band constants

On [pi/3,2pi/3], E lies in [j,3j]. Since j/D0=eta² and eta<=1/8, D0>=64j; D1>D0. All elimination denominators are therefore uniformly positive in this band.

Subtracting z algebraically gives `s-z=-v(1+z)/(z^-1-1+v)`. The denominator has modulus at least sin k. Since |1+z|=2cos(k/2) and sin k=2sin(k/2)cos(k/2), their ratio is 1/sin(k/2)<=2. Hence |s-z|<=2|v| without a fitted phase.

Enabled |v_+|<=6eta²/(1-3eta²) gives 12eta²/(1-3eta²)<=13eta², using 768/61<13. Disabled |v_+|<=2zeta/(1-3eta²zeta) gives 4zeta/(1-3eta²zeta)<=5zeta, using 512/125<5. Orthogonal channel and legal-program decompositions give a maximum of the two bounds rather than their sum; the sum remains a valid weaker ceiling. Passive-reference tensor factors do not change operator norm.

Thus multiplication by S-zC has the claimed essential-supremum bound on L2 spectral columns. That statement requires no physical spectral completeness theorem. It cannot, by itself, identify those L2 columns as a complete normalized physical output.

For the mediator, |1+s|<=2 and `b/(D_p-E)<=b/(D0-3j)=eta/(1-3eta²)` prove the stated common order-eta coefficient bound. A pointwise generalized coefficient is not an order-eta² physical packet error. Integrating it into a normalized packet needs further work, as the source says.

## Above-band eigenvalue

The antisymmetric channel is exactly the constant-boundary half-line with v=2 enabled or v=0 disabled. The half-integer sine/cosine bases provide spectrum [0,4j] with no square-summable eigenvectors. Before coupling the mediator, the symmetric half-line A_sym is the same respective v=2 or v=0 operator, hence has the same spectral interval and no point spectrum. Its endpoint diagonal 3j or j and interior row sums also establish ||A_sym||<=4j and positivity.

The original cell condition D0>2b already implies D0>4j, because j=b²/D0. Therefore D>=D0>4j even before imposing the stricter central-band eta domain. For E>4j, elimination of the lead gives the eigenvalue equation

    F(E)=D-E+2b²<0|(E-A_sym)^-1|0>=0.

The resolvent term is strictly positive. Its derivative is negative, so F'(E)=-1-2b²<0|(E-A_sym)^-2|0><0. F is positive for 4j<E<=D, and tends to minus infinity as E increases without bound. Thus it has exactly one root above D and no other root above the band. Every eigenvector there must have nonzero mediator component, since A_sym itself has no exterior eigenvalue. At the root, the resolvent constructs a nonzero square-summable lead component, establishing an actual eigenvector. This is not merely a formal Schur zero or a high-energy approximation.

## Below-band, thresholds and decaying-root equation

Completing the square in the mediator coordinate decomposes the quadratic form into a positive D term and the logical complement `A_sym-(2b²/D)|0><0|`. In the enabled sector this is exactly K_half>=0. Hence the full enabled relative operator has no negative spectrum.

In the disabled sector it is K_half minus a positive rank-one endpoint potential. A nonnegative operator minus rank one has at most one negative direction: on the codimension-one subspace x_0=0 its form is nonnegative. For x_n=sqrt(1-r²)r^n with 0<r<1, the norm is one and the bond sum is j(1-r)², while |x_0|²=1-r². The attractive term is linear in 1-r near r=1 and dominates the quadratic positive term. Choosing the mediator coordinate at the completed-square minimum gives a negative full form value. The coupling changes essential spectrum only by finite rank; the isolated mediator likewise adds no essential spectrum, so the bottom negative spectral value is an isolated eigenvalue. The at-most-one negative-direction bound proves exactly one, counting multiplicity. Positivity of the full 2b-shifted physical generator is unaffected.

For an exterior eigenvalue, let the symmetric lead tail be x_n=x_0r^n with real |r|<1. The interior recurrence gives E/j=2-r-r^-1. The endpoint equation after mediator elimination is `E/j=1+a/j-r-2b²/[j(D-E)]`. Subtracting them yields exactly `(D-E)(1-r^-1-a/j)+2b²/j=0`. Positive r gives E<0; negative r gives E>4j. No sign or factor two is missing.

At E=D, which lies above the band, the mediator equation forces x_0=0. The decaying recurrence then forces the entire lead tail to vanish, and the endpoint equation forces the mediator to vanish. Thus E=D is not an eigenvalue excluded only by division. Inside the band, all nonzero constant-coefficient tail solutions are oscillatory and not square summable. At the edges they are constant/linear times the possible alternating sign and likewise not square summable. If the tail vanishes, recurrence and endpoint coupling force the whole column to vanish. Hence there are no embedded or threshold eigenvectors. These arguments classify the stated point spectrum; they do not compute seed overlaps or establish a complete continuous spectral representation.

## Scope and work record

The exact bound states are genuine channels of the infinite microscopic operator. Their existence invalidates an unqualified claim of pure-continuum completeness, but does not prove that a separately constructed packet-specific comparison must fail. A direct full-vector comparison could pay omitted bound-state components. Such matching, packet normalization, finite outer-boundary residuals, final common-packet normalization and full emitter/mediator vacancy error remain separate obligations. No finite-duration or resource improvement is established by this check.

Only this report was written. No scientific executable, simulation, numerical integration, symbolic solver, sweep, source/W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. All calculations were analytical; hashing and directory creation were bookkeeping. No retained or audit status is assigned.
