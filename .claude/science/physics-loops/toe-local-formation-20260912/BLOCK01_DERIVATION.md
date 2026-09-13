# Native leaf formation: exact probability family and local information

Author derivation, 2026-09-12. Provisional, with small exact author counterchecks.
This is a conditional mathematical interface, not physical formation selection.
No axiom change or universal no-go is claimed.

## 1. Fixed target and source distinction

Use the specified native product-ready path filter of PR8036, head
6067254e3bca867aa6e737f7aa2bb6078e5d622d. Its carrier, CAR representation,
initial leaf occupations, hopping/phase controls and Born/Lüders event rule
are supplied. The charged-history dictionary of PR8065, head
b20fb72faf9fb793487a664fb927296c65f7d493, explains preservation of recorded
signs and original particle observables.

The new target is the event law at actual physical midpoint sites. A general
CP instrument or factorized success amplitude does not by itself answer that
question. The preparation domain, formation order and local Record condition
are held explicit throughout.

Let there be m matter modes, one distinct sacrificial leaf per mode, and a
parity reservoir. In the modal frame, leaf j initially has occupation l_j in
{0,1}. The represented even matter functional of the ready density is the
normalized full m-mode Fock trace. More generally let p(n) be the diagonal
occupation distribution of the modal matter density; coherences are allowed.

A leaf pulse has attenuation 0 <= r_j <= 1, s_j=sqrt(1-r_j²), and

    U_j = I + (r_j-1) T_j² - i s_j T_j,
    T_j = c_j† a_j + a_j† c_j.

The fixed native phases may change the represented amplitude convention,
but not the following occupation effects. Every outcome is retained.

## 2. One-pair lemma

T is zero in the empty/doubly occupied sectors and exchanges the two singly
occupied states. Therefore the unchanged-leaf event has matter effect

    E_same = I - (1-r²) n             if l=0,
    E_same = r² I + (1-r²) n          if l=1,

and E_flip=I-E_same. This follows by squaring the two-state rotation's
amplitudes; no assumed probability factorization is used.

For a matter occupation probability pi, write w=pi if l=0 and w=1-pi if l=1.
Then

    p_same = 1-(1-r²) w,   p_flip=(1-r²) w.              (1)

At uniform occupation, w=1/2:

    p_same=(1+r²)/2,  p_flip=(1-r²)/2.                  (2)

In actual leaf-bit labels a:

    p(a=1)=[1+(2l-1)r²]/2.                            (3)

For 0<r<1, an empty leaf's same outcome changes its matter occupation mean
from 1/2 to r²/(1+r²); its flip outcome leaves matter occupation exactly zero.
This post-event update, not a Bayesian update of the old input variable, is
essential for the hopping test below.

## 3. All finite histories, not just success

Distinct matter/leaf pairs have commuting even operations. A history over a
subset J consequently has effect product_j E_j^(a_j). The Fock trace of
that diagonal product factorizes, giving

    p(a_J)= product_j in J p_j(a_j).                   (4)

The parity reservoir causes no correction: the ready-state construction
already gives the complete normalized Fock functional on this even algebra.
Equation (4) includes every failure branch, every subset/order, r=1
zero-probability flips, degeneracy and zero modes. Conditional probabilities
are used only at prefixes with positive mass.

On a general diagonal p(n), the complete outcome law is

    q(a)= sum_n p(n) product_j M_j[a_j,n_j],           (5)

where, with rows a=0,1 and columns n=0,1,

    M(l=0) = [[1,r²],[0,1-r²]],
    M(l=1) = [[1-r²,0],[r²,1]].

Both determinants are 1-r². Let J be the informative modes r_j<1. Outcomes
on other modes are fixed at l_j. The product channel on J is invertible.
Hence its outcome law equals a specified product of the one-mode output
laws iff the input occupation marginal p_J equals the corresponding product
of one-mode occupation laws. In particular (2) across all histories is
equivalent to uniform p_J, not to a fully mixed quantum density operator.
Off-diagonal coherence is invisible to these particular effects.

Proof of the converse: apply the tensor product of the inverse M_j to the
specified product q_J; tensor products preserve products, and injectivity
leaves exactly the specified p_J. No positivity claim for arbitrary inverse
images is needed because the input p is already a probability distribution.

This is a precise state-family restriction. It is not an assertion that
generic native matter automatically has independent modal occupations.

## 4. A nontrivial invariant probability family

Between distinct leaf events, allow any supplied diagonal matter unitary
exp[-i f(n_1,...,n_m)], including a time-dependent choice and diagonal
multi-mode interactions. Such a unitary leaves the entire occupation diagonal
unchanged. A selective leaf operation reweights and possibly flips only its
own mode in that diagonal. Starting with a product diagonal, all untouched
mode diagonals remain their original product after every supported prefix.
Induction proves (4) even with these intervening diagonal operations.

This statement concerns event probabilities. For coherent input, the full
conditional quantum state can acquire phases and entanglement. The allowed
diagonal unitary need not be physically local in the original carrier; its
physical realization is a separate supplied-control condition. Arbitrary
noncommuting hopping is not covered.

## 5. The literal bare apparatus has a local-condition alias

For the source dimer, virtual edges are (0,1),(0,2),(1,3),(0,4), with virtual
vertices (0,0,0),(1,0,0),(0,1,0),(1,1,0),(0,0,1). Physical edge sites are
the doubled-coordinate midpoints:

    (1,0,0), (0,1,0), (2,1,0), (0,0,1).

The two forming leaf targets x_0=(0,1,0), x_1=(2,1,0) are distance two.
All their six physical nearest neighbors are blank, both before the first
event and before the second in the source schedule. The first leaf Record
is not a nearest neighbor of the second.

With l_0=0,l_1=1 and common r>0, equation (3) requires two different
probabilities for the same output projector P_1 under that identical blank
condition: (1-r²)/2 and (1+r²)/2. Their gap is r². At r=3/5 these are
8/25 and 17/25. The preparation bit and programmed pulse are unrecorded
apparatus data in this bare construction.

This refutes identifying that bare apparatus, with only its stated Records
as local conditions, with one fixed local content kernel. It does not refute
the native instrument theorem, the existence of other condition domains,
or the axioms. At r=0 this particular alias vanishes.

## 6. Local program Record interface

Supply one program Record next to each target, at (2j,2,0), containing

    C_j = P_(l_j) + w_j I + i(1+r_j) I.               (6)

Its Hermitian part has eigenvalues w_j and w_j+1, so w_j and P_(l_j)
are recovered from content. Its anti-Hermitian part recovers r_j. Define
F on a shell with exactly one such recognized program by (1), supported
on P_(l_j) and I-P_(l_j). This is one rule for all j and all supplied
parameters; it never reads an unrecorded mode or remote outcome.

The code fits one existing M2(C) site. Extraction and the measure commute
with unitary conjugation of contents. Shell recognition uses the unordered
neighbor contents, so translations and proper cubic rotations preserve F.
Result projectors are not program codes because their imaginary parts vanish.
The rule can be extended outside the apparatus domain, for example by a
fixed conjugation-invariant default distribution when no unique program is
present. Such an extension is a chosen downstream law, not a derived one.

Equation (4) proves exact matching on the declared ready family and schedule.
This resolves the finite content-law alias conditional on supplied program
Records. It does not supply their genesis, native readiness, physical pulses,
which target forms, time, or indefinite renewal. Those remaining conditions
prevent calling this a full model of the four axioms.

## 7. Noncommuting dwell gives a same-preparation history test

Keep the same two-mode mixed ready density, same program Records and source
leaf pulses. After the first leaf event but before the second, add a supplied
surviving matter hopping unitary exp(-i theta T_01). T_01 preserves the first
leaf Record; its old recorded sign is retained in the native word.

The first two outcomes have positive probabilities (1+r_0²)/2 and
(1-r_0²)/2 when 0<r_0<1. The untouched mode is initially uniform. After
the hopping step its occupation expectation is

    pi_1|a_0 = cos²(theta)/2 + sin²(theta) pi_0|a_0,
    pi_0|0 = r_0²/(1+r_0²),  pi_0|1 = 0.

The cross coherence is initially zero in both branches. For the second,
filled leaf, its same-outcome probability is r_1²+(1-r_1²)pi_1.
Thus the exact difference between the two histories is

    Delta = (1-r_1²) sin²(theta) r_0²/(1+r_0²).        (7)

The second target's complete nearest-neighbor Record shell is identical
in those histories. Its own program is unchanged; the first outcome lies
two physical edges away. For 0<r_0<1, r_1<1 and sin(theta) != 0 this
defeats the unrevised local program rule on the enlarged dwell domain.

This is a fixed-preparation, reachable-history collision, not arbitrary
remote-state steering. It is also a test of an additional interleaved dwell,
not a defect in PR8036's original control sequence.

## 8. One intervening Record can repair this finite collision

Supply a blank bridge at b=(1,1,0), adjacent to both leaf targets. After the
first event, form a bridge Record copying its content P_(a_0); old Records
remain fixed. Let the second target's supplied program encode

    C = A + i(2I+P_1),
    A = alpha_0 P_0 + alpha_1 P_1,
    alpha_b = r_1²+(1-r_1²)[cos²(theta)/2+sin²(theta)pi_0|b].

A is an effect. The program is distinguishable from (6). Its imaginary
part recovers P_1, and its Hermitian part recovers A. With adjacent bridge
content R, one local formula gives p(P_1)=Tr(A R). This exactly matches
the two conditional probabilities. Copying an already readable Record
is a classical content operation; it is not coherent cloning of an unknown
quantum state.

One piecewise F can include (6), this effect-table code and deterministic
copy on the specified one-projector/no-program shell. Its classes are
content-defined and conjugation covariant. Formation readiness still orders
first leaf, bridge, second leaf; the axiom does not itself supply that order.

This is a conditional finite causal-information repair, costing one fresh
bridge Record and a precomputed local program. It is not a proof that one
extra site is globally minimal, that all native histories admit bounded
memory, or that the physical control/formation mechanism is derived.

## Checks and continuation

The source dimer was reconstructed directly on four physical edge qubits
and compared with a separate occupation calculation. The exact checks of
(2), (4), (7), transported number, permanence, geometry and program decoding
include r=0, r=1 and theta=0; see BLOCK01_CHECKS.json and CHECK_NOTES.md.
BLOCK02_DERIVATION.md extends the finite-path response analytically and
derives the complete Gaussian history calculus. What local memory and causal
traffic are required when a chain contains repeated noncommuting dwell and
many fresh leaf events? A merely exponential precomputed history table is not
an efficient physical construction.
