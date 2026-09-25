# Original birth energy and coherence for mixed low-band field inputs

Personal root candidate, 2026-09-24, fifth campaign. No independent check at
creation. This asks whether the zero-field pure input is responsible for the
large birth energy and apparatus-coherence coefficient. It does not choose
a physical initial state or change the original formation instrument.

## 1. Input class and actual operation

Retain the supplied compensated lambda=0 cube and joint scaling
epsilon^2 S(S+1)=delta/K with fixed delta,K>0. Let P4 be the N=4, W=0
physical rotor space. Its matter configuration is all A positive and all B
vacant; its electric fields satisfy the homogeneous Gauss constraint.

Fix any finite set of physical electric words and let K0 be its linear span
in P4. For all sufficiently large S this subspace lies in the spin box.
Allow any density matrix rho_epsilon supported in K0, with arbitrary
coherences and mixtures, and even epsilon dependence. The subspace K0 is
fixed independently of epsilon. Its field magnitudes and dimension are fixed.
This is not the class of all epsilon-dependent high-flux preparations.

Prepare the actual canonical Hermitian low-band state

    rho_in=U4,epsilon rho_epsilon U4,epsilon*.

For one original plus, minus or coherent mark on edge ab=(0,1), define

    omega_i=alpha^2 j_i rho_in j_i*,
    p_i=Tr omega_i,
    rho_birth,i=omega_i/p_i,

with alpha a fixed admissible operational amplitude. It is not identified
with a physical GKLS timestep. Let U6,epsilon be the canonical all-cluster
Hermitian rotation in N=6. All energy moments below use the original H6,
not a projected energy filter or a no-event Hamiltonian.

## 2. Local operator identities behind B and R

Write F=sum_c F_c for outward charge hops. For the edge mark j at A center a,
the exact hard-core algebra gives [F_c,j]=0 for c!=a, [F_c,F_d]=0 for c!=d,
F_a^2=0 and jP4=0. Shared B endpoints make both orders vanish; no opposite
same-link spin shifts are exchanged in those commutations.

The leading low and first-high coordinates of the rotated actual map are

    B_i=j_i F P4=j_i F_a P4,
    R_i=(j_i F^2/2-F j_i F)P4=-F_a j_i F_a P4.         (1)

To see the second equality, put F=F_a+F_remote. Remote factors commute
through j and annihilate its action on P4; the two copies of
F_remote jF_a in jF^2 cancel the remote part of F jF. These are operator
identities at every finite spin, not values only on the zero-field vector.

For the rotor, B_i and R_i are scalar multiples of isometries on the whole
physical P4 space:

    B_i* B_i=b_i I,       R_i* R_i=r_i I,
    (b_i,r_i)=(2,4),(2,2),(4,6).                        (2)

Here is a direct physical-word proof. Let c,d be the other two B neighbors
of a besides the marked b. B_plus has two outputs, corresponding to moving
the original positive charge to c or d before the mark creates a plus at a
and a minus at b. The two matter outputs are orthogonal. B_minus also has
two orthogonal outputs, now with the negative charge at a. Rotor shifts
have unit amplitude. Each output electric word determines the source word
uniquely by undoing its fixed star shifts.

For R_plus, the second outward hop sends the recreated positive charge to
the remaining leaf. The two orders, first c then d or first d then c,
produce the identical physical charge/field output, with coefficient -2.
Thus R_plus*R_plus=4I. For R_minus the recreated negative charge goes to
the other leaf. Its two placements give orthogonal matter outputs, each
with coefficient -1, yielding 2I. The plus and minus outputs are orthogonal
for both B and R, so the coherent sum yields b=4,r=6.

There is no interference between different input electric words: outside
star links are unchanged, and a difference of two divergence-free input
fields supported on a tree star must vanish. Equivalently each fixed output
matter label determines its complete shift from the source. Therefore these
norm identities hold on arbitrary superpositions and mixed states, not just
on a list of basis inputs. Every R output has its A vacancy at a and its B
vacancy opposite a; it remains dark for the original immediate birth loss.

At finite spin (2) is replaced by diagonal multiplication operators. Put

    h_+(m)=1-m(m-1)/C,  h_-(m)=1-m(m+1)/C,
    f_sigma(m)=1-m(m+sigma)/C,

with a forbidden boundary shift assigned weight zero. For a source field E,

    b_sigma,S(E)=f_sigma(E_ab)[h_+(E_ac)+h_+(E_ad)],
    r_plus,S(E)=4 f_+(E_ab)h_+(E_ac)h_+(E_ad),
    r_minus,S(E)=f_-(E_ab)
       [h_+(E_ac)h_-(E_ad)+h_+(E_ad)h_-(E_ac)].         (3)

The coherent values are the sums over signs. These formulas preserve the
actual spin weights and can vanish at boundaries. They are not constant
through the finite spin box. On the fixed finite input space K0, however,
b_sigma,S=b_sigma I+O(C^-1) and r_sigma,S=r_sigma I+O(C^-1), uniformly in
operator norm. In the joint scaling this is O(epsilon^2).

## 3. Uniform canonical output expansion on this input class

The general uniformly bounded graded resolvent/polar construction gives,
on K0,

    Pi0 U6* j_i U4 =epsilon B_i,infinity+O(epsilon^3),
    Pi1 U6* j_i U4 =epsilon^2 R_i,infinity+O(epsilon^4),
    Pi2 U6* j_i U4 =O(epsilon^3).                      (4)

Using rotor maps in (4) is legitimate because their finite products on K0
differ from the spin maps by O(C^-1)=O(epsilon^2). The maps are understood
inside the sufficiently large physical spin box. The remainders are uniform
on K0. The last bound suffices here; the separate cubic commutator argument
can improve it, but no improved exponent is needed for the present claims.

For low energy moments, ordinary norm expansion alone is insufficient. Use
w=1+sum E_e^2 as in the weighted parent proof. Finite-hop operators, their
adjoints, D/C and the canonical power series are uniformly bounded in its
conjugated norm. Every vector in K0 has a fixed common w bound. Thus the
low component of the normalized actual output has bounded D action and
bounded physical low Hamiltonian action, because that block is
KD+delta H4_S+O(epsilon^2). The input has the same property, giving
F_H4(rho_in)<=4 Var_H4(rho_in)=O(1) uniformly over rho_epsilon in K0.

The exact Hermitian first and second high blocks have centers
delta epsilon^-4 and 2delta epsilon^-4 and widths O(epsilon^-2).
Taking traces in (4), using (2) and the weighted low bound, proves uniformly
over the stated input density matrices

    p_i=alpha^2 b_i epsilon^2[1+O(epsilon^2)],
    Tr(H6 omega_i)=alpha^2 delta r_i+O(epsilon^2),
    Tr(H6^2 omega_i)=alpha^2 delta^2 r_i epsilon^-4
                                      +O(epsilon^-2). (5)

The second high output contributes at most O(epsilon^2) to the selected
mean and O(epsilon^-2) to the selected second moment under the loose final
bound in (4). After normalization,

    Tr(H6 rho_birth,i)=delta(r_i/b_i)epsilon^-2+O(1),
    Var_H6(rho_birth,i)=delta^2(r_i/b_i)epsilon^-6
                                               [1+O(epsilon^2)]. (6)

The squared conditional mean is only O(epsilon^-4). These are actual
conditional birth densities, including mixtures. No energy postselection
has been applied. The coefficients equal the zero-field pure-input values
throughout this fixed finite-support class.

## 4. One witness works for every mixture in K0

Let V_B=U6 B_i,infinity/sqrt(b_i) and
V_R=U6 R_i,infinity/sqrt(r_i), restricted to K0. They are exact isometries
into the exact Hermitian low and first-high clusters for sufficiently large S.
Their ranges are orthogonal. The bounded observable

    A=i(V_R V_B*-V_B V_R*)

has norm one and A^2=V_B V_B*+V_R V_R*. It is the same observable for all
rho_epsilon supported in K0. With omega_i from (5), the exact-band expansion
and Tr rho_epsilon=1 give

    d=|Tr(omega_i i[H6,A])|
        =2 alpha^2 delta sqrt(b_i r_i)epsilon^-1[1+O(epsilon^2)],
    q=Tr(omega_i A^2)=alpha^2 b_i epsilon^2[1+O(epsilon^2)]. (7)

For the first line, the scalar high-band center produces the displayed term.
The remaining high and low operators have norm O(epsilon^-2); because A is
off-diagonal between the exact bands, only the O(epsilon^3) low/high cross
block enters their expectation, producing an O(epsilon) correction. Terms
outside these two bands give zero. The low/high cross operator has leading
form alpha^2 epsilon^3 R_i rho_epsilon B_i*, which cannot be canceled by
mixing rho_epsilon: the two scalar isometries retain its trace norm and the
witness pairs their input labels. This is not an appeal to convexity in
the direction of a lower bound on Fisher information.

Now use the finite resource premises of the reviewed apparatus note: a finite
initially product apparatus including all phase references, exact additive
energy conservation and covariant zero-energy mark readout. Suppose its
selected subnormalized output sigma_i approximates omega_i with trace error
eta_epsilon. The finite SLD witness bound yields

    F_HR(sigma_R) >= [d-2h_epsilon eta_epsilon]_+^2/(q+eta_epsilon)
                               -F_H4(rho_in),          (8)

where h_epsilon=||H_system-cI||=O(epsilon^-4). Therefore, uniformly over the
input class when eta_epsilon=o(epsilon^3),

    liminf epsilon^4 F_HR(sigma_R)>=4 alpha^2 delta^2 r_i. (9)

The initial input Fisher is O(1), including for mixed input. The proof does
not use purity of the input or output, nor replace an average variance by
the generally smaller mixed-state Fisher information. A variance alone
would not establish (9); the explicit phase witness is essential.

## 5. Frequency, precision and a limited positive comparison

The canonical input is supported in the N=4 exact low band, of width
O(epsilon^-2). Its Bohr frequencies are bounded by that width even when
mixed. The N=6 low/first-high gap is delta epsilon^-4+O(epsilon^-2).
Finite covariance therefore forces the output cross block to vanish if
the apparatus coherence bandwidth B_R plus the input width is smaller than
that gap. Test with V_R V_B*+V_B V_R*. Its target expectation is

    2 alpha^2 sqrt(b_i r_i)epsilon^3[1+O(epsilon^2)].

Thus the same o(epsilon^3) accuracy gives

    liminf epsilon^4 B_R>=delta,
    liminf epsilon^4 diam(spec H_R)>=delta.            (10)

Pinching the selected target into its exact energy clusters removes a
leading trace norm 2alpha^2 sqrt(b_i r_i)epsilon^3+O(epsilon^4). The scalar
isometry identities make the leading coefficient independent of mixing.
The probability-weighted Fisher of the pinched comparison is O(1): the low
energy action is bounded, and within each high band a scalar center can be
subtracted before bounding Fisher by four times the second moment. This
states a precision limitation, not an apparatus implementing the pinched
operation on every input.

For each fixed choice of rho_epsilon and mark, the previous preloaded-state
swap can be used on a replica of the invariant sum of the N=4 low, N=6 low
and N=6 first-high bands, with a zero-energy mark flag. Truncate the target
to the two N=6 bands and retain its exact selected probability p_i. The
gentle-projection estimate gives selected error O(epsilon^4), since the
discarded target mass is O(epsilon^6) and p_i=O(epsilon^2). A stationary
ground state in the other flag completes the probability. The global swap
on the invariant subspace, with identity on its complement, conserves the
additive energy exactly.

For the preloaded resource, the phase-witness lower bound on its selected
block and F<=4p_i Var of the normalized selected state sandwich its leading
Fisher coefficient at 4alpha^2 delta^2 r_i epsilon^-4. Its energy diameter
is delta epsilon^-4+O(epsilon^-2), and its ground-relative mean is
alpha^2 delta r_i+O(epsilon^2), since the low spectral minimum is O(1).
This attains the two leading lower coefficients for the one-input relaxation
with this O(epsilon^4) error sequence. It does not meet every tighter given
tolerance or give one input-independent device for the whole input class.
The apparatus preloads the chosen rho_epsilon's answer and generally fails
the original marked map on other inputs.

## 6. Scope and independent-check obligations

The new contribution is preparation robustness within a stated class,
especially the mixed-input witness. It does not remove canonical low-band
preparation, the finite-support restriction, supplied compensation or the
implementation premises. Moving spin-boundary/high-flux families are outside
the claim, and (3) explicitly preserves their possible changes of weights.
The result does not select a unique preparation, apparatus or physical law.

Before publication independently reconstruct the physical-star operator
identities and finite-spin weights; verify the canonical second coefficient
on arbitrary input words; stress the mixed-state witness against rank-deficient
and maximally mixed inputs; check the weighted low-moment assumptions; and
distinguish one-input state preparation from a universal original instrument.
No new later-time variance result is asserted here. The original resolved or
coherent matter/field outputs remain intact throughout.
