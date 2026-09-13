# Native scalar: structural work beyond unchanged error envelopes

Started after the Block11 checkpoint 5abd365975, pushed to the campaign branch.
Deadline remains 2026-09-13 11:38:24 UTC. Personal execution, no subagents.

Current status: the separate-source quadratic witness now proves56<h²alpha<280
under the named supplied native/gap/scalar premises. See BLOCK12_DERIVATION.md
section6 and BLOCK12_AUTHOR_REVIEW.md. The prospective route text below is
retained as the discovery history, including plans superseded by actual results.

## Target and prior-art reading

Determine whether the actual infinite canonical native node alpha is nonzero,
or derive a materially stronger checkable route. Its value remains open.
The complete-sixth consequence is a conditional motivation, not an input to
the scalar calculation. No native Hamiltonian, vacuum, or denominator may
be changed and then reported as the native answer.

The third-order star note (a814da6c), infinite node note (64c1efc6), and
finite-excitation Ward proof blocks1–2 (4f096449) were fully reread for the
active formulas. The rest of the finite-excitation note was read earlier;
the latest broad reread was partly truncated and is not claimed complete.
The quartic note a2aca4bc, correlated note ac5e0c24, and stronger-estimator
note ac7bc8d6 were fully reread. All preserve indeterminate alpha intervals.
The shared-center scattering amplitude3, complement relation, and corrected
Ward boundary terms are ALREADY DERIVED. Do not present them as new.

The existing diagnostic quadratic active/spectator resummation already
appears in the third-order star note. Repeating its square-root frequencies
would not advance the native interacting problem.

## Candidate analytical control, not a native result

A finite S6-symmetric star with two active frequencies a,b>0 and an auxiliary
soft zero mode gives an exactly tractable Ward test beyond the equal-frequency
L4 fixture. It is only a diagnostic. In the active paired frame, g=a_u,
v_A=u/3+(sqrt2/3)w_A, with disjoint-pair w_C dot w_A=-1/2. Take the reference
frequency a on u, b on the standard representation, and impurity
B_A=-i a a_u b_(v_A). Its even and odd two-mode denominators are

    D_even=[[a/3,a sqrt2/3],[a sqrt2/3,2a/3+b]],
    D_odd =[[2a/3,-a sqrt2/3],[-a sqrt2/3,a/3+b]].

Their determinants are ab/3 and2ab/3, positive for all a,b>0. The first
positive-inverse state is

    x_A=(3/a+2/b)Omega-(3/b)u wedge v_A.

Introduce a genuine auxiliary zero Majorana a_q, gamma_center(epsilon)=
sqrt(1-epsilon²)a_u+epsilon a_q, while the original row coupling becomes
a sqrt(1-epsilon²)v_A. The first derivative of the impurity is
V_A=-i a a_q b_(v_A). Extract the zero-mode vacuum amplitude divided by
epsilon before taking epsilon→0. This supplies an actual bounded finite
Ward derivative, not a fictitious zero mode in a flat gapped bath.

Writing L_A=-i a b_(v_A), the preliminary hand algebra gives

    y_A=D_A^-1 L_A D_A^-1 Omega
       =3u/(2a)+(9/(2b)+3a/b²)v_A,
    g x_A=(3/a+3/b)u-(3/b)v_A.

The soft derivative kernel for a disjoint pair should be

    <x_C,x_A>+<y_C,g x_A>+<g x_C,y_A>
       =18/a²+27/(ab)+18/b²+6a/b³.

If the CAR check agrees, summing90/8 proves positivity ONLY for this finite
two-frequency diagnostic family. It is not the ordinary L4 vacuum coefficient;
the zero-mode derivative probes a different quantity. Check the sign against
literal3-active-mode and4-mode-with-soft-source Fock operators before using
this as a regression control. General native bath frequency measures and
their mixed quench correlations remain unaddressed. Do not make a PR from
this toy calculation alone or call its positivity a native sign bound.

## More direct native option

NEW structural route at the first diagnostic checkpoint: use the exact
commutator v=R J R Omega=R W Omega-W R Omega. Instead of the coupled
bound (j/delta)E plus an inner residual, separately approximate R Omega
and R W Omega. With xhat=-p(D)Omega and yhat=-p(D)W Omega, vhat=yhat-Wxhat
is [W,p(D)]Omega, so ||v-vhat||<=||W||E+Y. This uses the already proved
Ward tail W, with a NEW source-error certificate Y; it does not assume Y=E.
For quadratic p, [W,D]=-J gives vhat=-p1 J Omega-p2(DJ+JD)Omega.
The actual native CAR identity (DJ+JD)Omega=-2gamma(Kd)Omega should reduce
this to a linear source. Derive and check its normalization before evaluating
a nominal. The required W-source moments may use additional inverse-radial
scalars; locate those suppliers, do not silently substitute vacuum moments.

This route now outranks the unrestricted degree-(2,1) trial below because it
removes the explicit j/delta amplification analytically and has a simple
local trial vector. Whether the additional source error is small is OPEN.

At the first table checkpoint, check_block12_ward_table.py passes both actual
L8 AP one-particle81-entry tables (max scaled residual2.4e-14), and separate
small Fock identities. The full-operator anticommutator shortcut is rejected;
the claimed identity is on the original vacuum. The diagnostic checker also
passed9exact groups; its plan hash is now stale after additions to this plan
and should be refreshed once before committing the block.

Next exact implementation: a small formal Clifford algebra on sorted words
in w,a_j=K^j a,d_j=K^j d through j=4 or5. Place w FIRST in the ordering.
Use gamma_i gamma_j+gamma_j gamma_i=2 dot(i,j) and the analytical Gram
table in BLOCK12_DERIVATION.md. Free commutation replaces each a_j,d_j by
i times its next power and w by6i d0. Iterate O_next=[H0,O]+i a0 d0 O
only through5. Start once from I and once from w. Obtain moments0..10
as <O_floor(n/2)^* O_ceil(n/2)> in the Gaussian state, normal-ordering the
Clifford product first and then Wick-contracting with the proved covariance
table. This avoids an unbounded Fock space or a degree10 operator expansion.

The W-source moments should be AFFINE in A0=E omega^-2 and C0=E omega^-1:
the two W factors can be removed by W² before contraction, leaving terms
with at most one W. Preserve these correlations symbolically before interval
evaluation; treating every moment's A0 independently would create spurious
width. First source checks are m0_W=72A0(P)/12(O) and
m1_W=(mu/3)m0_W+24C0(P)/4mu(O).

For the new signed nominal, xhat is at most quadratic and gvhat at most
quadratic, so a SIX-field table (a,Ka,d_A,Kd_A,d_C,Kd_C) suffices. With
n=|A intersect C| and m=number of opposite leg matches between A,C,
dot(d_A,d_C)=n, dot(Kd_A,Kd_C)=6n+m,
kappa(d_A,Kd_C)=-[mu*n+(nu/6-mu)*m], where mu=L1 and nu=L3.
Other entries follow the single-source table and parity. The five ordered
disjoint classes are OO(m0)6, OP(m0)12, PO(m0)12, PP(m2)12, PP(m1)48.
This NEW commutator-trial nominal needs only mu,nu. It must not reuse the
old degree20 nominal in the quartic packet.

Existing exact vacuum moments0..10 and both original p coefficient families
are in ref a2aca4bc, path
.claude/science/physics-loops/native-quartic-ward-20260910/source_draft/packet/INPUTS.json.
Read/parse it into compact floats or selected fields for inspection; it is a
large one-line rational JSON. The moment supplier source and quartic theorem
have been fully read, but source data truth remains inherited/conditional.
The original highprecision Green node catalog is NOT present at its old
/private/tmp/toe-24h-probes-20260908 path. Do not assume those old files exist.
The freeze's full interpreter inventory is huge; parse/filter it rather than
printing it. Source recovery may be available in named git archive maps.

For a first bounded certificate one can retain analytic broad bounds
A0 in[1/6,17/60] and C0 in[1/sqrt6,23/50], using already proved source
inequalities; no midpoint is a certificate. Sharper A0 is in the accepted
Green scalar packet. C0 may require a new positive-integral certificate or
recovery of accepted A-node data. Decide from the actual polynomial width
before acquiring a new scalar. Do not launch an unchanged moment/envelope
scan. First derive the finite source moments and new nominal exactly.

The existing best quartic envelope retains a degree-two outer polynomial p
and CONSTANT inner q. Its dominant coupled error still contains (j/delta)E
and a large inner residual. A genuinely different inner polynomial requires
new signed nominal contractions and a fresh certificate; merely changing
the norm envelope is already exhausted in the reviewed notes.

Derive the degree-(2,1) source and cross-channel closure analytically using
O_(n+1)=[H0,O_n]+B_A O_n on the original vacuum. First determine exactly
which CAR covariance moments and source norms it requires, then compare with
the authenticated existing moment suppliers. Any resulting calculation must
retain all90 signed terms and its actual approximation error. A positive
nominal or a better finite residual is not alpha nonvanishing. No large
Fock solve or unbounded parameter scan is authorized by this working plan.

## Decision discipline

Do not deepen the provisional Block6 chart theorem as an unquestioned premise.
Use primary native Ward identities and source gap with their conditional
status. A same-author calculation is not independent source review. Preserve
any failed sign/formula or inconclusive certificate. At a genuine structural
wall, checkpoint and return to the remaining matter/source or formation
information residual rather than restating the same positivity obligation.

Other pending delivery work: Block10 cold-scope review; Block11 canonical
milestone packaging. Both are already durable on the pushed campaign branch.


## Current outcome

The exact moment recurrence,90-term nominal, common-p certificates, positive
return-series Green refinement, distinct-q derivation and fixed scalar
certificate are complete. The common-p intervals remain inconclusive. The
separate-source trials give positive intervals; the conservative standard-library
witness certifies56<h²alpha<280. The source bound on A0 is inherited from
281dbe3f; C0 follows from a new positive series bound at exactly N256. The
provisional Block6 improved chart is not a premise. Same-author source review
and finite checks are complete; independent source review is pending. Next
work is durable commit and conditional canonical milestone packaging.
