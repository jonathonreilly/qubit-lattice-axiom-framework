# A covariant block pointer for records, vacancy, transport and renewed birth

2026-09-22. Author conditional construction; independent check pending.
This supplies an explicit quantum model on logical blocks. It does not select
a microscopic law from the framework axioms, identify a block with one native
site, establish a photon, or make a TOE claim.

## Hilbert space and exact code

Take three ordered pairs of qubits. In each pair use its singlet plus
Cartesian triplet basis, so a proper cubic rotation acts as U_R=1 direct-sum R.
The six-qubit block has H=(C direct-sum C^3)^tensor3, dimension64, and
V_R=U_R^tensor3. This is the collective spin action on six M2 factors after
a fixed basis choice. The ordering of pairs is part of the block definition;
a homogeneous embedding of such blocks into physical lattice sites is not
given here.

Let Z contain the six vectors +/-ei and the eight vectors (+/-1,+/-1,+/-1).
For z in Z put w_z=(1,z)^tensor3 and collect these columns in F. Its Gram
matrix is the integer matrix G_zw=(1+z.w)^3. The exact characteristic
polynomial is

    (t-6)^2 (t-48)^4 (t^2-92t+192) (t^2-88t+384)^3.

All roots are positive: 6,48,46+/-2sqrt481,44+/-4sqrt97, with respective
multiplicities 2,4,1,1,3,3. In particular F has rank14. Define

    W = F G^(-1/2),       |a> = W e_a.

The positive inverse square root exists uniquely. W^dagger W=I14. If P_R
permutes the labels, V_R F=F P_R and P_R commutes with G and its positive
inverse square root. Therefore V_R W=W P_R exactly. These fourteen states
are orthonormal, with the declared proper-cubic action and no phase ambiguity.

An additional invariant vacuum is

    |0> = (sum_(i=1)^3 [|0 i i> - |i 0 i>])/sqrt6.

It is rotation invariant by contraction of vector indices. Each w_z is
symmetric under permutation of the three tensor factors, whereas the two
terms above have opposite overlaps with w_z. Thus the vacuum is orthogonal
to every code column. Its norm is one. Let C be the fifteen-dimensional
span of the vacuum and the fourteen colors. There is unused orthogonal
space of dimension49; the following operators vanish there where specified.

The exact checker builds F and the full group action, checks rank and the
characteristic/annihilating polynomials, verifies all 336 column covariance
identities and all 24 vacuum identities, and checks vacuum orthogonality.
Numerical polar orthonormalization is only a diagnostic. The initial optional
radical-projector simplification was interrupted and is preserved separately;
it is not part of the proof or completed evidence.

## Exact quantum realization of a local classical record process

Consider any finite graph of these blocks and a continuous-time classical
process on the fifteen labels, specified by nonnegative rates for transitions
inside a bounded stencil X. For each local input word c and allowed output
word d with rate r_X(d|c), define

    J_(X,c,d) = sqrt(r_X(d|c)) |d><c|_X tensor I_(outside X),
    L(rho) = sum_J [J rho J^dagger - (1/2){J^dagger J,rho}].

This is a finite-dimensional Lindblad generator. For a density matrix
diagonal in the product code basis its gain and loss terms are exactly the
classical forward equation. The diagonal code algebra is invariant, so
the complete joint law, including correlations, is reproduced at all times.
This is a standard orthogonal-pointer lift; the explicit covariant code is
the additional construction here. No classical-to-quantum novelty priority
is claimed for the Lindblad recipe.

Apply this to the prior routed fourteen-color process with the fixed
winding matching. Its four-position rates are k0/2+h/4, and are nonnegative
when k0>=|gamma|. Each J replaces |l,a,b,r> by |l,b,a,r>. The generator is
local on four logical blocks. For each color c, N_c=sum_x |c><c|_x commutes
with every jump; no color is changed or lost. Choosing k0>|gamma| gives a
strict rate floor. The entire quantum generator is defined, not only its
linear tangent. Four logical blocks are not four original physical sites.

The internal code is rotation covariant. A physical cubic rotation also
rotates the routes and matching. Accordingly the generator is covariant
as a family indexed by the matching and rotated stencil data. The fixed
matching white(u)=u+e1 alone has a preferred axis and is not claimed to be
invariant under all rotations.

## Vacancy motion and reuse of a freed block

There are several separately supplied choices of dynamics. They should not
be conflated.

1. **Incoherent motion.** For a directed edge x to y and color a use
   sqrt(kappa_a)|0,a><a,0|. This moves the unchanged label and leaves a
   vacuum. Reverses may be included separately. Context-dependent rates
   are implemented by adding orthogonal context projectors to the stencil.
2. **Coherent motion.** A Hermitian term
   H_xy=sum_a kappa_a(|0,a><a,0|+|a,0><0,a|) moves a label coherently
   between an occupied and an empty block. It preserves every N_a, the
   code space, and the maximum of one record per logical block.
3. **Birth.** J_(x,a)=sqrt(beta_a)|a><0| at x creates a new label only in
   a vacuum. On the code space the adjoint generator obeys
   L_birth^*(N_record)=sum_(x,a) beta_a |0><0|_x >=0, and the color version
   counts the births of that color. In the quantum-jump description each
   birth increases record count by one. No annihilation channel is included.

Rates constant within the A orbit and within the B orbit respect the cubic
label symmetry. Nonnegative neighbor-dependent birth rates are also possible
through the same orthogonal-context construction. Their form, clock, coupling
to an environment and any energy balance are supplied physical assumptions.

For example start with |a,0>, move a to the second block, then birth b in the
first. The allowed history is |a,0> -> |0,a> -> |b,a>. The original label a
persists and the source is reused. This demonstrates the requested logical
record behavior in a quantum model. It does not identify the block pointer
with the repository's elementary Record at one M2 site or supply unique
identifiers for an unlimited history of identically colored records.

The fourteen-color routed lift is an exact implementation of its classical
statistics. Its classical waves are not, by that fact alone, quantized
electromagnetic excitations. Coherent vacancy motion is a different option;
birth then causes quantum backaction and requires its own analysis.

## Information metric and next decision

On the occupied code support the uniform state is I14/14. For the transverse
color tangents e_a,2/2 and b_a,3/8, the quantum chi-squared weights are
u=7, v=7/4, with zero transverse cross term. The relation u=4v is exact.
This is consistent with the direct Lindblad construction; the construction,
rather than a metric test alone, proves complete positivity.

The code deliberately uses perfectly distinguishable block pointers. Its
state space and supplied operations are explicit costs of this realization.
The next physical questions are whether a native arrangement and preparation
can generate these roles, and how coherent motion and irreversible formation
affect one another. These questions remain open here. No axiom amendment or
formal retained status is proposed.

Reproduction: `python3 six_qubit_orthogonal_code_check.py`; exact results,
command, source hash, timestamps, stdout and stderr are saved alongside this
note. The mathematical Lindblad argument is analytic and is not replaced by
the finite rank checks.
