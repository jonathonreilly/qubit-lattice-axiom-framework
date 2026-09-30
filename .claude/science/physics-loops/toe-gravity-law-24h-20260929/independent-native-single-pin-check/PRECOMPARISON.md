# Independent precomparison: one spectator pin

September 30, 2026. Before reading SINGLE_PIN_EXTENSION.md or the parent's
new proof/code, I reconstructed the following from the actual landed law,
the earlier threshold definition and my previous checks. The dispatch
already exposed the proposed coefficient 2a/g, the nine forward bonds, and
the far amplitude sqrt(2) U A U^T. This is independent derivation, not blind
target discovery. The old lower REPORT remains frozen.

The landed full-carrier estimate is H0 >= a Egrad, with
a=min(tau,mu/12), where Egrad is the sum of gradients of all fifteen bare
pair annihilation words, including all output occupation amplitudes.
Resolving those outputs introduces no normalization factor: an input word
is repeated once for each occupied removed bond. That repetition is already
present in the literal squared annihilation norms; it must not be divided
by a matching count or by two.

Use nine forward anchored edges:

    B_i(x)=b_x b_(x+2e_i),
    B_(ij,r)(x)=b_x b_(x+e_i+r e_j), r=+1,-1.

The three axial fields are translations of the centered d_i. For each plane,
the four signed centered v fields are translations, with signs, of two
forward fields, each appearing twice. Summing over all centers makes
Egrad exactly the sum of axial gradient norms plus twice the six forward
plane gradient norms. It therefore dominates the unweighted nine-field sum.
All nine forward fields share the exact pin x=y for every fixed output
occupation eta containing the spectator site y. Changing axial cells only
multiplies their nonzero-momentum Fourier rows by phases; their zero-momentum
coefficient matrix U is unchanged.

Write the incoming fifteen-component vector as an arbitrary complex
symmetric 5 by 5 matrix A with Hilbert-Schmidt norm. The physical incoming
profile is (1/sqrt(2)) sum_ab A_ab C_a^dagger C_b^dagger Omega, where
the five uniform one-pair modes have U^dagger U=I. Their nine real rows are
the two traceless axial columns and the three plane pairs (-1,+1)/sqrt(2).
For a fixed graph-edge residual d and a removed edge of type beta far from
it, only that separated matching contributes. The two creator orders give
the exact amplitude sqrt(2) (U A u_d^T)_beta. This is also correct for an
off-diagonal symmetric basis matrix whose two entries are 1/sqrt(2).
Additional contact matchings and any compact relative correction change
this constant profile only on finitely many forward anchors.

For a scalar field f=c+h on Z^3 with compact h and f(y)=0, Parseval and
Cauchy-Schwarz give

    |c|^2=|h(y)|^2 <= g sum_(x,j)|h(x+e_j)-h(x)|^2,
    g=int_BZ [4 sum_j sin^2(k_j/2)]^-1 dk/(2pi)^3.

There is no zero Fourier eigenvector on infinite l2 to project out here.
The integral is finite in dimension three; ell>=4|k|^2/pi^2 and enclosing
the cube in the radius sqrt(3)pi ball give g<=sqrt(3)pi/8. The same point
evaluation extends continuously to the homogeneous energy completion,
although compact corrections already suffice for the threshold infimum.

Apply this inequality separately to all nine outputs for each graph-edge
residual, keeping one actual spectator pin rather than summing both pins.
Per unit translated volume there are nine such residual types. Their far
amplitudes have total squared norm

    2 sum_d ||U A u_d^T||^2 = 2 tr(A^dagger A),

using the real U and U^T U=I on both sides. Thus the prospective inequality
is E(Phi_A+chi) >= (2a/g)||A||_HS^2 for every compact relative chi, then
T0 >= (2a/g) I_15. It concerns all complex symmetric A, not only A=z z^T.

The all-volume passage must be checked precisely. For fixed compact chi,
the energy/SOS gradients of the incoming-plus-correction profile are local
in relative position: separated zero-mode pairs contribute no gradient.
One may sum each fixed residual's finite gradient support on Z^3 and count
one representative per translation orbit. Alternatively first embed every
relevant connected support in a sufficiently large torus and divide the
actual local energy by V. A global isometry for all N=4 torus words would
be wrong because distant words can have nontrivial translation stabilizers.
The fixed compact support/local cancellation argument is essential. One
must then take the infimum over compact chi, known to equal the l2 affine
threshold infimum by bounded H4 and compact source. No l2 minimizing response
or bounded zero-energy inverse is assumed.

Points still to compare against the released proof: the exact forward-cell
enumeration/signs; unweighted nine-field rather than an incorrectly divided
gradient sum; local energy/V normalization; control of compact correction
embedding; and use of the full Hilbert-Schmidt identity. Nothing here proves
a many-particle lower EOS, phase, or positive-energy on-shell scattering.
