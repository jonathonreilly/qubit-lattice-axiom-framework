# Independent check of the single-spectator threshold bound

No material error was found in the stated extension. For the supplied native
Hamiltonian at fixed mu,tau>0, its argument proves

    T0 >= (2a/g) I_15 >= [16a/(sqrt(3)pi)] I_15,
    a=min(tau,mu/12),
    g=(2pi)^(-3) integral_[-pi,pi]^3 [4 sum_j sin^2(k_j/2)]^(-1) dk.

This covers the complete complex fifteen-dimensional symmetric incoming
space. It is a bound on the already defined relaxed zero-threshold quadratic
form. It neither identifies the dilute many-particle equation of state nor
proves a phase or an on-shell positive-energy scattering result. This is a
focused independent mathematical check, not a formal review, audit or PASS.

Coverage binds `independent-native-lower-check/SINGLE_PIN_EXTENSION.md`, SHA256
`d5d1ecea06f9159ef9efda5090c235fc5ea424dad5ddb02deb761e173bab52a6`.
The original lower REPORT, SHA256
`78b011a124cb004efafafe7247b95b626ad2487ee2b29f6b311edeefc9329fa2`,
has not been changed. The extension strengthens its separate threshold
consequence, without altering its all-N capacity comparison.

## Independence and dependencies

Before reading the extension, I froze PRECOMPARISON.md at 05:37:02 UTC with
SHA256 `3de7d9c857f11d9c7517e768b5548cb6ae7777c2e157d1538fdbe447b044721b`.
The dispatch had exposed the proposed constant, nine forward bonds, and far
amplitude. The precomparison is an independent derivation and domain check,
not a blind discovery. I then read the entire extension. No parent code or
new control implementation was read, imported or executed. The new literal
control below is independently written.

I reread the complete landed density note at main
`30a9461ee19a49b99fa6628fe942f08e504e8903`, SHA256
`7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0`,
and the complete earlier independent threshold and variational-upper checks.
Selected campaign procedure remains
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The actual hard-core carrier,
Hamiltonian, quantum interpretation and positive parameters remain supplied
premises. No external theorem, fitted value or foundational selection enters.

The reused threshold definition concerns physical infinite-lattice N=4,
total momentum zero, and constant normalized two-pair incoming channels.
Its affine energy is E(Phi_A)+2 Re<chi,F_A>+<chi,H4 chi>, with bounded H4
and compact collision source F_A. Its compact-correction infimum equals
the l2-correction infimum. No bounded inverse on all l2, square-integrable
zero-energy minimizer, or uniform spectral gap is an input here. The new
bound also does not depend on the static 35-pin capacity estimate in my
earlier author report; that would be a circular unnecessary dependency.

## Literal gradients, common pin and removal count

The landed full-carrier identity and collective-to-bare estimate give
H0>=a Egrad. Egrad sums the gradient squares of the three centered axial
words d_i and twelve signed plane words v_ij^(s,t). Resolving the output of
each annihilator in the occupation basis gives exactly a sum over residual
sets eta. An occupied input configuration contributes once per removed
physical bond appearing in the word sum. There is no matching-sector
normalization or factor one-half to insert.

Define the nine forward fields

    B_i(x)=b_x b_(x+2e_i),
    B_(ij,r)(x)=b_x b_(x+e_i+r e_j), i<j, r=+1,-1.

The centered axial field d_i(x) is B_i(x-e_i), so its summed gradient norm
is unchanged. The literal plane word with signs s,t has endpoints
x+s e_i and x+t e_j. If s=+1 its forward anchor is x+t e_j and r=-t;
if s=-1 its anchor is x-e_i and r=t. In both cases its coefficient is s t.
Consequently every forward plane field occurs twice among the four centered
words, by translations and harmless signs. This proves the exact identity

    Egrad = sum_(eta,x,j) [sum_axial |delta_j f_eta|^2
                              +2 sum_plane |delta_j f_eta|^2],

where f_(eta,d)(x)=<eta|B_d(x)psi>. Dropping one copy of each plane term
gives precisely the extension's nine-component lower inequality.

If y belongs to eta, f_(eta,d)(y)=0 for every forward type d: annihilation
at y cannot produce an output still occupied at y. Thus all components
have the same exact pin. In contrast, keeping axial midpoint labels without
translating them would give different pin locations. The extension performs
the necessary translation; it changes Fourier phases but no norms or
zero-momentum normalization. No projector is commuted through an overlapping
annihilator in this argument.

## Scalar capacity and all fifteen channel factors

For finite-support u on Z^3, Fourier inversion and Cauchy-Schwarz yield

    |u(y)|^2 <= g integral ell(k)|u_hat(k)|^2 dk/(2pi)^3
              =g sum_(x,j)|u(x+e_j)-u(x)|^2.

The integrable singularity 1/|k|^2 is the reason this estimate works in
three dimensions. If f=v+u and f(y)=0, it follows that its gradient energy
is at least |v|^2/g. There is no extra factor two in this scalar convention:
one forward nearest-neighbor difference per coordinate has Fourier symbol
ell=2 sum_j(1-cos k_j). Since ell>=4|k|^2/pi^2 on the Brillouin cube,
enclosing it in the radius sqrt(3)pi ball gives g<=sqrt(3)pi/8 exactly.

The real nine-by-five matrix U has axial rows
(1/sqrt(2),1/sqrt(6)), (-1/sqrt(2),1/sqrt(6)), (0,-2/sqrt(6))
in its E columns and each plane's two rows (-1,+1)/sqrt(2) in its T column.
The T mode is the actual uniform Q_T/sqrt(2) mode. Thus U^T U=I_5.

Let A be any complex symmetric matrix, with Hilbert-Schmidt channel norm,
and Phi_A=(1/sqrt(2)) sum_ab A_ab C_a^dagger C_b^dagger Omega. For a graph
residual of type d0 and a far removed bond of type d, the two creator orders
produce

    v_(d,d0)=sqrt(2) (U A U^T)_(d,d0).

The factor also holds for off-diagonal normalized symmetric basis vectors.
For fixed residual, all alternative contact matchings and compact relative
corrections differ from this constant on a finite set of removed anchors.
Each of its nine components therefore obeys the scalar pin bound. There are
nine unique graph-residual types per translation cell, not nine divided by
two. Summing yields

    E(Phi_A+chi) >= (a/g) sum_(d,d0)|v_(d,d0)|^2
                  = (2a/g)||U A U^T||_HS^2
                  = (2a/g)||A||_HS^2.

Both copies of the isometric U are used in the final equality. It is a
Hermitian norm identity for arbitrary complex symmetric A, not a positivity
claim extrapolated from coherent directions A=z z^T. Counting both possible
removed separated pairs is already part of the actual gradient energy;
eliminating that count would incorrectly halve the threshold coefficient.

## Compact support, volume order and threshold infimum

The incoming profile itself is not l2. The preceding use of the full-carrier
inequality is justified locally, rather than by pretending otherwise. Fix
a compact relative correction chi first. For a graph-edge residual, the
deviation of its removed-pair amplitude from v has finite support. Its
gradients therefore have finite support in relative position. The incoming
zero-mode pair equations likewise cancel the actual Hamiltonian/SOS rows
outside the collision region. All relevant source, correction and bare
energy terms consequently embed faithfully in sufficiently large tori.

At those sizes, divide the literal local energy and gradient sums by V and
pass to the infinite relative sums. Each graph residual is counted once per
translation and type. This uses precisely the earlier checked local energy
normalization. It is not a global isometry of the torus N=4 occupation space:
distant four-site configurations can have nontrivial translation stabilizers.
Such configurations are outside the fixed connected supports contributing
to these gradients and energy, where the separated-pair cancellation is
exact. They do not modify the local coefficient.

One must not instead minimize an unconstrained finite periodic scalar field
with a single pin; the constant mode would invalidate that replacement.
The extension explicitly takes volume first at fixed compact correction,
then applies the infinite-lattice scalar estimate to the constant-plus-
compact profile. Its bound is uniform over that correction's support.

Finally take the infimum over compact chi. This equals the established l2
affine infimum because bounded H4 and finite F_A make the affine energy
continuous in l2. For two corrections chi,chi', its difference is bounded by
[2||F_A||+||H4||(||chi||+||chi'||)]||chi-chi'||. Finite-support corrections
are dense, even when a minimizing zero-energy response is not in l2. No
exchange of an infimum with an unpriced finite-volume minimization occurs.

## Actual independent control and limits

`check_literal.py` uses exact arithmetic in Q(sqrt(2),sqrt(3)) and unordered
physical four-site sets. It enumerates the two annihilated/created endpoint
subsets directly, with all ordered creator terms. It does not use a bosonic
matching replacement or a parent implementation. It verifies all fifteen
centered-to-forward translations and the multiplicities (1,1,1,2,2,2,2,2,2),
1,215 far creation amplitudes, 1,215 literal common pins, and all 225 entries
of the fifteen-channel image Gram matrix. Raw off-diagonal symmetric basis
matrices have norm squared two and image norm squared four; diagonal basis
matrices have norm squared one and image norm squared two. Vanishing cross
Gram entries proves the complex linear combination normalization as well.

The single run passed without a failed assertion. It was priced at 30 CPU
seconds/150 MB and used 0.499274 CPU seconds, 0.499397 wall seconds and
21,200,896 bytes peak RSS. Thread caps were one; deadline and STOP checks
were active. No numerical value of g, full T0 matrix, infinite Green inverse,
many-particle ground state or order parameter was computed. The scalar
capacity and volume/domain statements are analytic checks, not deductions
from this finite control.

No correction to the extension was requested. Its constant is stronger than
the earlier coarse static-block bound by a factor 21/2; the older weaker
claim remains valid and its frozen bytes are preserved. The conclusion
supplies neither a many-body T0 lower functional nor condensation, and does
not resolve positive-energy scattering or a framework-law selection.
