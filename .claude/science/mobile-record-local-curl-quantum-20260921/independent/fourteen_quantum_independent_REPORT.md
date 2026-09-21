# Final independent fourteen-label quantum-interface and Born-deformation review

Date: 2026-09-21. This is review of two completely read mathematical notes,
followed by independently assembled derivations and checks before access to
the author's associated checkers/results. It is not blind to the notes,
an audit verdict, or a claim that an operational quantum bridge follows
from the framework axioms.

**Final disposition:** no actionable mathematical error or source/code drift found. The
rank/TV obstruction, exact fixed-natural-encoding optimum, positive carrier
constructions and projective covariance argument reconstruct correctly.
The changed kernel has the claimed one-event interface and optimal
single-operation fidelity. Its complete fourteen-field linearization and
ordered late-state argument are consistent. The late-wave norm/scattering
argument concerns the six raw vector components U,V, with beta>0 inherited
from the native process; it must not be exported to the separate decaying
density component or to a native stochastic fluctuation theorem.

The initial reconstruction and sixteen independent control groups were sealed
before the three author checkers/results were opened. All three checkers,
result files and raw logs have since been read completely and authenticated.
Sections 1-10 give the reconstructed arguments; Section 12 gives the
post-seal source comparison. No source correction is requested.

The reviewed note identities are:

- FOURTEEN_LABEL_QUANTUM_INTERFACE_DERIVATION.md:
  9bb453c1041ea2a548989f14e2666df6a27c76adb8e35bf2d833eb2334bd2f5d
  (266 lines).
- BORN_COMPATIBLE_FOURTEEN_LABEL_FORMATION.md:
  42197693e57ead840ef3fc174c62cb56c1ae1ab7b49e3d164a36241698685c8f
  (132 lines).

SOURCE_IDENTITIES.json records these sources and unchanged dependencies.
The earlier local-curl, fifteen-state exchange and native entropy proofs
are reused by their authenticated identities. No new proof claim is inferred
from a PASS total.

## 1. Original rank and total-variation bound

Let F have rows t_a=(e_a,b_a/2). Direct summation over the six axes and
eight cube corners gives F^T F=2 I_6 and F^T 1=0. With T=F F^T,

    P=(11^T+jT)/14, T^2=2T.

The constant subspace has eigenvalue 1, range(F) has eigenvalue j/7
and the remaining seven dimensions have eigenvalue zero. Thus rank(P)=7
for every nonzero j.

For a fixed d-dimensional preparation encoding and fixed apparatus,
Q_ab=Tr(E_a rho_b) factors through the real d^2-dimensional Hermitian
operator space. Arbitrary disturbance, adaptive operations and
input-independent ancillas still reduce to effects E_a on the input.
Therefore rank(Q)<=d^2. A qubit cannot realize this P. Replacing
normalized effects by observed positive rate effects does not help:
P diag(h_b) still has rank seven whenever all prescribed occurrence rates
are positive. Zero-occurrence inputs would change the positive-rate task.

For a qubit Q, ker Q has dimension at least ten and intersects range(P)
in dimension at least three. On that intersection P has smallest singular
value |j|/7. Three orthonormal vectors therefore give

    ||P-Q||_F^2 >= 3 j^2/49.

The difference of each normalized column has zero sum. If its total
variation is delta_b, its positive and negative masses each equal delta_b,
so its squared Euclidean norm is at most 2 delta_b^2. Consequently

    max_b TV(P_.b,Q_.b) >= sqrt(3/7)|j|/14.

This is a universal lower bound under the specified uncorrelated
preparation/apparatus model; it is not a claimed sharp minimax over all
qubit encodings. The independent checker verifies every matrix identity
and the constant. The stochastic rank-four truncation
Q=(11^T+j E E^T)/14, retaining only the A features, attains the Frobenius
lower bound, but its worst-column TV is 3|j|/28. Tightness of the
Frobenius step therefore does not imply TV sharpness.

The shared-resource qualification is essential. A concrete excluded
construction uses a uniform shared seed r in {1,...,6}, prepares a qubit
with Bloch z-coordinate t_br and measures effects
(I+6j t_ar sigma_z)/14 conditional on r. For |j|<=1/6 these are positive
and the averaged probabilities equal P exactly. The joint input/apparatus
state is not rho_b tensor one fixed apparatus state. This confirms, rather
than contradicts, the note's explicit resource restriction.

A quantum-only output marginal is also different. Under the natural
fourteen Bloch-ray encoding s_A=e, s_B=b/sqrt(3),

    sum_a P_ab rho_a=(I+(j/7)s_b.sigma)/2.

This follows because the three columns of S=(s_a) lie in range(F).
The depolarizing channel with parameter j/7 realizes that marginal for
|j|<1; its Pauli-mixture probabilities are (1+3j/7)/4 and three copies
of (1-j/7)/4. It does not supply the inaccessible classical label a
with the stipulated probability kernel.

## 2. Exact optimum for the fixed natural Bloch encoding

The fixed input family is covariant under the 24 proper cubic rotations,
implemented projectively on qubits. Simultaneously averaging an arbitrary
POVM over the input/output group action cannot increase the convex
worst-column TV error. Stabilizers of an axis and a cube corner force the
averaged effects to be

    E_A=alpha I+u e_A.sigma,
    E_B=eta I+w b_B.sigma,
    6alpha+8eta=1, alpha>=|u|, eta>=sqrt(3)|w|.

This is a reduction of the complete POVM optimization, not an unproved
restriction to a convenient ansatz.

For j>=0 set a=alpha-1/14, d=eta-1/14,
z=w/sqrt(3)-j/56. Exact dot-product multiplicities give

    TV_A=max(|a|,|u-j/14|)+2|a|+4max(|d|,|w|),
    TV_B=3max(|a|,|u|/sqrt(3))
             +max(|d|,3|z|)+3max(|d|,|z|).

Projecting u onto [0,j/14] and w onto [0,sqrt(3)j/56] decreases every
slope discrepancy and preserves the original effect positivity. Setting
a=d=0 then decreases both losses further. Positivity remains valid on
this rectangle for 0<=j<=1. The remaining objective is

    max(L_A,L_B),
    L_A=j/14-u+4w,
    L_B=sqrt(3)u+3j/28-2sqrt(3)w.

Let theta=sqrt(3)/(2+sqrt(3)). Its positive weighted average is exactly

    theta L_A+(1-theta)L_B
      =j(3-sqrt(3))/14+theta u.

Since u>=0, this proves the lower bound. At u=0 and
w=j(2-sqrt(3))/56 the two losses coincide, attaining it. Output antipodal
relabeling handles j<0. Thus

    delta_natural=|j|(3-sqrt(3))/14

is an exact optimum for the stated fixed inputs, not the variable-encoding
optimum of Section 1.

The independent checker directly evaluates all fourteen column losses
for positive, negative and boundary j and verifies this dual identity.
Five additional SciPy linear programs retain all fourteen column TV
constraints in the rigorously justified twirled family. Their numerical
optima agree to floating precision. These LPs supplement the proof; they
are not presented as independent unrestricted-encoding optimizations.

## 3. Positive qutrit and four-dimensional constructions

Choose six orthogonal traceless Hermitian Gell-Mann matrices, with
Tr(G_r G_s)=2delta_rs. Then G(t)=sum t_r G_r obeys
||G(t)||op<=sqrt(2)|t|<=sqrt(2). With

    rho_b=I_3/3+G(t_b)/(3sqrt(2)),
    E_a=I_3/14+(3sqrt(2)j/28)G(t_a),

the states are positive and have trace one, the effects sum to I_3, and
their minimum eigenvalue is at least (1-3|j|)/14. Moreover

    Tr(E_a rho_b)=1/14+(j/14)t_a.t_b.

Thus qutrits suffice for |j|<=1/3. Rank excludes dimension one or two
for j!=0, so minimum dimension is exactly three in that range without the
additional covariance/permanence constraints. The bound on the range is
sufficient; no optimization for larger |j| has been supplied.

The four-dimensional construction is a direct sum of two qubit blocks.
Its states occupy the appropriate A/B orbit block. In their own block,
A effects have Bloch radius |j| and B effects radius 3|j|/4, with scalar
I/14 in the other block. Effects sum to identity and all 196 probabilities
are the required P. Hence this construction works for |j|<=1.

The checker independently constructs a concrete six-matrix qutrit basis
and all fourteen states/effects, checks all 196 probabilities in each
construction, and verifies the stated norm certificates. Numerical
endpoint eigenvalues are only supplemental checks of positivity already
proved by the displayed inequalities. Neither construction supplies a
microscopic spatial carrier or record-capacity model. Their instruments
generally disturb the parent.

## 4. Why proper-cubic covariance forces dimension four

The symmetry assumption is a single projective unitary representation
U_g of the proper cubic group G, with equivariant preparations and effects.
For proper rotations G is isomorphic to S_4. Both e and b transform in
the same three-dimensional real rotation representation R.

The preparation map Gamma:c->sum_b c_b rho_b intertwines the label
permutation representation and Ad(U). On the six-dimensional feature
subspace R+R, P acts by the nonzero scalar j/7. Since P is the measurement
map composed with Gamma, Gamma is injective there. Its image contains
two copies of R in Hermitian operator space. That image is traceless and
does not contain the invariant identity.

If d=3, Ad(U) has dimension nine. Complete reducibility therefore writes

    chi_Ad=1+2 chi_R+chi_W, dim W=2.

Even when U is projective, Ad(U) is an ordinary representation because
its multiplier cancels in conjugation. Its character is
|Tr U_g|^2, the same trace whether computed on complex operators or on
the complexification of Hermitian operators.

The independent checker constructs all 24 proper signed cubic matrices,
their action on the four unoriented body diagonals, and the permutation
action on the three pairings. It obtains the five character rows in the
note. Their character inner products are orthonormal and the squared
dimensions sum to 24, so they form the full ordinary S_4 table.

A two-dimensional W is either the irreducible E or a sum of two
one-dimensional characters. At a transposition chi_R=-1; nonnegativity
of |Tr U_g|^2 requires chi_W>=1. Only W=1+1 satisfies that requirement.
Thus Ad(U) would have exactly three invariant components, equivalently
a complex commutant of dimension three.

The last step is important and valid for projective representations.
Decompose the finite-dimensional unitary projective representation with
one fixed multiplier into inequivalent irreducible invariant blocks.
Orthogonal complements remain invariant; Schur's lemma gives commutant
dimension sum_alpha m_alpha^2. A sum of positive integer squares equal
to three forces three inequivalent multiplicity-one blocks. Because the
whole Hilbert space has dimension three, all blocks must be one-dimensional.

All three one-dimensional projective characters must have the same
multiplier. The ratio of two then obeys the ordinary character
multiplication law. Relative to any one block, inequivalent blocks
therefore give distinct ordinary one-dimensional characters of S_4.
There are only two (trivial and sign), so three such blocks are impossible.
This contradiction excludes every projective qutrit representation; it
does not assume a classification of projective S_4 irreducibles.

Dimensions one and two were already excluded by rank. The four-dimensional
orbit-register construction is covariant under I_orbit tensor u_g,
so four is the exact minimum with this additional covariance requirement
for every nonzero j in the stated interval. A direct sum of an ordinary
one-dimensional block and a spinor with a different projective multiplier
would not be a single projective representation and cannot evade the step.

## 5. Pure-parent permanence and what it does not imply

Consider a fixed channel, including any recovery, that returns the original
pure parent |psi_b><psi_b| for every promised input. After purification of
any input-independent apparatus, its Stinespring isometry must factor as

    V|psi_b>=|psi_b> tensor |z_b>.

For <psi_b|psi_c>!=0, preservation of inner products forces
<z_b|z_c>=1, with phases absorbed consistently. Thus all complementary
outcome laws coincide for such a pair.

Every two columns of the original P differ: equality would imply
F(t_b-t_c)=0, and full column rank of F then gives t_b=t_c, contrary to
the fourteen distinct features. Hence the fourteen parent pure states
must be pairwise orthogonal. Dimension fourteen is necessary and a
fourteen-state orthogonal pointer register is sufficient. This dimension
counts the occupied parent carrier, not an independently stipulated
orthogonal vacancy flag or a spatial mobile-record implementation.

The purity premise is material. The independent control measures Z on two
different diagonal mixed qubit states. Their unconditioned parent density
matrices remain exactly unchanged while their classical outcome laws differ.
That is not a realization of the original rank-seven kernel, but it shows
why the pure-state factorization cannot simply be reused for arbitrary
mixed-state permanence. Input-correlated auxiliary labels, quantum-only
outputs and preservation only on a selected branch would also be different
resource/operation tasks. The note does not claim otherwise.

The natural qubit rays have 84 nonorthogonal unordered pairs, so the
specific fixed natural encoding certainly cannot preserve every unknown
pure parent while producing distinct marked laws. Conversely, a dimension
bound for this operational task is not an axiom consequence about the
framework's abstract possibility algebra.

## 6. Changed Born-compatible kernel and one-event interface

Now s_A=e, s_B=b/sqrt(3), so

    sum_a s_a=0, sum_a s_a s_a^T=(14/3)I,
    P'_ab=(1+j s_a.s_b)/14.

This is a different kernel, of rank four for j!=0. The qubit states
rho_b=(I+s_b.sigma)/2 and effects E_a=(I+j s_a.sigma)/14 realize it
exactly. The checker verifies all 196 probabilities.

For k independently prepared unknown occupied parents, the tensor-product
rate effects

    F_a=(beta/N) tensor_r (I+j s_a.sigma_r)

are positive and have the exact stipulated product expectations. Their
sum has norm at most 14(beta/N)(1+|j|)^k, so, for example,
dt<=N/[14beta(1+|j|)^k] makes the effects dt F_a and
I-dt sum_a F_a a POVM. Square roots define a complete one-step instrument.
For k=2, the independently checked total rate operator is

    (beta/N)[14 I+(14j^2/3) sum_i sigma_i tensor sigma_i].

These are ordinary observed event effects; they do not supply an
exponential classical waiting law for all later times or repeated iid
marks from an unchanged unknown parent. Known occupancy/which parent
slots are supplied is also part of this local interface specification;
no qubit-only orthogonal vacancy readout or immutable quantum record
transport is constructed.

## 7. Exact average parent-preservation fidelity

The fourteen equally weighted pure qubit states form a projective
two-design at the required order:

    (1/14)sum_b rho_b tensor rho_b=(I+SWAP)/6.

For Kraus operators K_ar with sum_r K_ar^dagger K_ar=E_a, including any
outcome-dependent recovery in the final Kraus family, the average pure-state
overlap fidelity is

    F=1/3+(1/6)sum_(a,r)|Tr K_ar|^2.

To optimize at a fixed effect, diagonalize E_a with eigenvalues lambda_0,
lambda_1. Cauchy-Schwarz on the vectors of diagonal Kraus entries gives

    sum_r |(K_ar)_00+(K_ar)_11|^2
       <=(sqrt(sum_r |(K_ar)_00|^2)
          +sqrt(sum_r |(K_ar)_11|^2))^2
       <=(sqrt(lambda_0)+sqrt(lambda_1))^2.

Off-diagonal entries can only use up the fixed column norms. The single
positive Kraus operator sqrt(E_a) attains equality. Because the axis
inputs already span the qubit Hermitian space, any effect family realizing
the stipulated kernel on all these inputs must equal the displayed E_a;
there is no additional exact-kernel POVM freedom.

Here lambda_0,lambda_1=(1+/-j)/14 for every outcome. Summing yields

    F_max=(2+sqrt(1-j^2))/3.

The checker verifies the two-design tensor, exact square-root effects at
j=3/5, and fidelity 14/15. The analytical trace inequality supplies the
optimization, including recovery. Fidelity means <psi_b|rho_out,b|psi_b>,
averaged over the input ensemble and all outcomes. It is a single-operation
bound. At j=0 the operation can preserve parents exactly; for j!=0 this
bound is strictly below one for these pure preparations.

## 8. Complete reaction/current matrix of the changed classical process

The unchanged context-exchange current remains

    J_a=gamma p_a[e_a cross Y+X cross b_a-2X cross Y].

The new product reaction is

    B_a=beta p0[1+j s_a.(X+Y/sqrt(3))]^6.

The smooth-profile entropy proof applies with exactly the same conservative
positive floor, finite alphabet and bounded seven-site source. With p fixed
in an interior compact set, averaging the source adjoint under q gives

    beta sum_a [q_a p0/p_a-q0] m_a(q)^6,

which vanishes at q=p and has differential H(p)B(p). The neighbor-factor
derivatives vanish because each central bracket is zero there. The
polynomial Hessian is bounded for q on the closed simplex; the uniform
reference adjoint is at most beta(1+|j|)^6 V. Thus the prior fixed-block
replacement and entropy argument survive without exact product evolution.
This remains conditional on a C^2 uniformly interior solution and an
initial o(V) entropy discrepancy on each fixed time interval.

Use the full basis rho, d=4rhoA-3rhoB, U(3), V(3), A quadrupoles(2),
B pair characters(3) and B triple character(1). At p_a=rho/14,
rho'=14beta(1-rho). Writing h=beta j(1-rho), the complete reaction has

    density eigenvalue -14beta;
    seven zero spectator fields;
    vector block 4h [[3,2sqrt(3)],[2sqrt(3),4]] tensor I_3.

The only linear exchange block is, for C_K v=K cross v,

    A(K)=[[0,-c C_K],[c C_K,0]], c=2gamma rho/7.

These matrices were obtained independently by differentiating all fourteen
species rates/currents and changing to the full invertible moment basis.
No scalar, quadrupole, higher-character or longitudinal mode is discarded.

The constant determinant-one rotation
P=(sqrt(3)U+2V)/sqrt(7), Q=(-2U+sqrt(3)V)/sqrt(7)
diagonalizes the orbit reaction into 28h and zero and preserves the
antisymmetric exchange coupling. The full fourteen-field drift polynomial is

    z^8 (z+14beta)(z-28h)
          [z^2-28hz+c^2|K|^2]^2.

Thus the raw longitudinal drifts are 28h and zero. Each transverse helicity
has roots 14h+/-sqrt((14h)^2-c^2|K|^2). They can be real during formation;
at the equality threshold a repeated root need not be semisimple.
The note does not assert a diagonalization there. If gamma or K vanishes
there is no propagating splitting. These formulas do not describe the
time-ordered propagator when rho evolves.

## 9. Vector norm, time ordering and late free waves

For clarity, F(t) in the note's norm/scattering argument is the six-component
Fourier vector (U_K,V_K). It is not the complete fourteen-field vector.
The density component has its separate decay exp(-14beta t), which would
contradict a lower norm ratio of one if erroneously included.

The exchange matrix L_ex is anti-Hermitian in this U,V norm. The symmetric
reaction has eigenvalues 28h and zero. Therefore, for nonzero F(s) and t>=s,

    0 <= d log||F||/dt <=28h                 if j>0,
    28h <= d log||F||/dt <=0                 if j<0.

Since integral_s^t 28h=2j[rho(t)-rho(s)], this proves the note's two-sided
norm bound. It proves bounded amplification/damping, not exponential growth
or decay indefinitely. In particular every fundamental matrix has a
strictly positive uniform lower singular bound
exp(2 min(j,0)[1-rho(0)]).

For nonzero beta, gamma, j and K, coefficient matrices at different
densities generally do not commute. Their commutator is proportional to
(c(t)h(s)-h(t)c(s)) times the nonzero commutator of the fixed orbit reaction
and exchange matrices. The checker verifies an exact nonzero example.
No frozen-eigenvalue phase formula is used.

Assume beta>0 as in the supplied native model. Put a=14beta, v(t)=v0 e^-at
and L_infinity=L_ex at c_infinity=2gamma/7. Then

    ||L(t)-L_infinity||
       <=A e^-at,
    A=v0[28beta|j|+|c_infinity||K|].

The interaction picture Z=e^(-L_infinity t)F has the same norm because
the transformation is unitary. Its derivative has integrable norm bounded
by A e^-at times the uniform bound on ||F||. The integral equation gives
a Cauchy limit and the explicit tail estimate

    ||Z_infinity-Z(t)||
       <=(A/a)e^-at exp(2 max(j,0)v0)||F(0)||.

Applying this to the fundamental matrix and its uniform lower singular
bound shows directly that its limiting linear map is invertible. Hence

    F(t)=e^(L_infinity t)[Z_infinity+O(e^-14beta t)].

Longitudinal zero-frequency amplitudes are included. Transverse oscillations
have frequency |c_infinity||K| when it is nonzero. This is a statement
about the fixed finite-dimensional deterministic linear ODE only.
Beta=0 with an interior nonsaturated background would not permit this
specific saturation/scattering argument.

Numerical DOP853 controls at fixed rho0=0.37, beta=0.23, gamma=-0.8,
K=(2pi,0,2pi), j=+/-0.61 retain the full time dependence. All sampled
singular values obey the proved two-sided envelopes within solver error.
The interaction-picture change from t=6 to t=8 is below the explicit
tail estimate for both signs. These controls supplement the proof and
do not stand in for a native stochastic limit.

## 10. Parity and ordered late-state selection

Under the earlier polar/axial convention, an improper R sends
e->R e and b->det(R)R b. Cross-orbit e.b/sqrt(3) changes sign.
The checker gives +1/sqrt(3) before a reflection and -1/sqrt(3) after.
The new kernel is covariant under the 24 proper rotations, not that
48-element extension. Its curl identities remain kinematically true;
they do not restore the lost reflection covariance of the dynamics.

The ordered late-state proof for the specified classical process survives
this change of weights. The new W still lies in
[1-|j|,1+|j|], has occupied row sum fourteen, and gives the same equal-label
homogeneous Euler trajectory. At finite N the total birth rate with m
vacancies is at least 14beta(1-|j|)^6 m, so full occupancy is reached
almost surely. For a fixed time T, final species counts differ from their
time-T counts by at most the remaining vacancy count. Fixed-T Euler laws
of large numbers followed by T large force final fractions to 1/14.
The exchange process at full occupancy remains irreducible within each
count sector and has uniform permutations as its invariant law.

Thus, taking long time at each finite N and then N to infinity, the
limiting local law is iid uniform over the fourteen occupied labels.
The exact canonical nonzero-mode covariance identity previously checked,

    Cov(fhat(k),fhat(l)^*)=V/(V-1) C_f(p) 1_(k=l),

passes through the random final counts because conditional nonzero-mode
means vanish exactly. The vector covariance tends to 4 I_6/7 and the
scaled curl covariance to (4/7)(|K|^2 I-KK^T). The checker verifies the
unchanged row sum and full-occupancy feature covariance/rank.

The initial law here must be the stated fixed interior equal-label product,
and the Euler theorem is used only on fixed intervals. No mixing rate,
simultaneous large-time/volume limit, native Gaussian fluctuation theorem
or result about global count fluctuations is being imported. Crucially,
this late-state conclusion belongs to the supplied classical process.
Its one-event quantum realization does not establish a repeated quantum
process with the same history law.

## 11. External attribution, controls and retained failures

The only external source inspected for this review is Gallego, Brunner,
Hadley and Acin, [Device-independent tests of classical and quantum
dimensions](https://arxiv.org/pdf/1010.5064v1). The prepare-and-measure
definition and the distinction between correlated and uncorrelated devices
on PDF pages 1-3 agree with the note's attribution. No paper-specific
dimension witness or optimum was imported. These are established methods;
the finite matrix application is not evidence of methodological novelty.
The archived v1 PDF and EXTERNAL_SOURCE.json identify the version, read
boundary, URL and SHA-256 c919dec4d75cafd53138a9ec64d09d344ce520caadb5a85a77f7561faa70106d.

The independently written checker completed sixteen groups, including
exact matrix/character/Kraus controls, five numerical symmetry-reduced LP
cases and two time-ordered ODE cases. It does not import author code.

An environment probe found cvxpy unavailable in the default Python runtime.
No package was installed. The probe source and traceback are preserved;
the exact minimax proof and available SciPy LP were used instead. The
first mathematical checker execution stopped after eight completed groups
because Python sum cannot add SymPy BooleanAtom values while counting
nonorthogonal pairs. The original script and complete failed log were
preserved before replacing that count by explicit bool/int conversion.
No formula, target, model or parameter changed. The second execution
completed all groups. ATTEMPTS.json binds both executions and the reason.

The initial document remains unchanged as INITIAL_RECONSTRUCTION.md,
SHA-256 f867b2fdf8bcfefb4c7e0db1305610d10c15a27d20b6fe65da44108896ccafce.
PRE_COMPARISON_SEAL.json, SHA-256
b8d703de6cf7c9618c51d1294a35f0d867b63ba85a61085f793e4f423aeb4ef5,
binds its derivation, all exact/numerical outputs and failures, ten
source identities and three instruction identities before any associated
author checker/result access. Every initial sealed artifact and dependency
was reauthenticated after the comparison. No production source, publication,
prompt, Git/PR/audit state or unrelated file was modified, and no agent
was spawned.


## 12. Complete source/evidence comparison after the initial seal

The following three checkers, their result JSON files and their raw logs
were read completely. All nine identities are in SOURCE_COMPARISON.json.

| Checker | SHA-256 | Recorded groups |
|---|---|---:|
| fourteen_label_quantum_check.py | 7cac1e6ac6129faa930f3cc322686420c790070f962f09f67ee9a851df7d5561 | 13 |
| fourteen_label_cubic_carrier_check.py | 398741417193fe997c9d11c717ecfff717378332a916edba71765287dea58ef5 | 5 |
| born_compatible_fourteen_formation_check.py | cd899415da554be8d4e691417248c709820d17c220c9cebce86c6640dc4816d4 | 13 |

Each result binds the actual source hash. Its named group inventory matches
the source's complete check-call inventory and every raw log line. These
counts inventory selective evidence; they do not certify the mathematical
proofs. No author checker was executed merely to reproduce a count.

The first checker really does optimize arbitrary fourteen-effect qubit
POVMs for fixed natural preparations: its variables are all fourteen scalar
parts and all fourteen independent three-vectors, with the full positivity,
completeness and worst-column TV constraints. It does not impose the cubic
ansatz and does not optimize the input encoding. Its nine recorded conic
optima at j=-0.99,-0.75,-0.5,-0.1,0,0.1,0.5,0.75,0.99 agree with the exact
formula; the largest recorded objective difference is about 3.65e-12.
Recorded references, discrepancy arithmetic and declared feasibility/TV
thresholds were authenticated. The primal effect arrays are not included
in the results, so their residuals were not independently recomputed.
The unavailable local cvxpy program was not rerun or installed. The exact
independent primal/dual argument supplies the scientific optimality result.

That checker uses six off-diagonal Gell-Mann matrices, whereas the
independent checker uses a different orthogonal set containing one diagonal
matrix. Both satisfy the proof's stated normalization and reproduce all
196 qutrit probabilities. This difference is permitted by the argument.
The endpoint positivity samples are floating-point controls, including a
roughly -3e-18 roundoff eigenvalue; positivity over the whole asserted range
comes from the norm bound and exact qubit-block spectra, not sampling.

The cubic-carrier checker derives the ordinary S_4 character table from
actual permutations and checks the four-dimensional construction under all
24 proper rotations using numerical spinors. It correctly labels the
projective-commutant exclusion as a proof obligation beyond those finite
checks. Section 4 above reconstructs that step, including the common
multiplier and complex-commutant dimension. No classification of every
projective irreducible representation was silently imported.

The Born checker retains the full fourteen-species reaction/current matrix,
its driven/undriven rotation, parity witness and 2,744 exact two-parent
marked probabilities. Its fidelity-related check verifies the two-design
identity; the sharp optimization additionally needs the Kraus trace
inequality in Section 7, which was independently reconstructed and tested
at an exact fidelity witness. The source does not mislabel its fixed-time
one-event instrument as a repeated quantum realization.

Its numerical propagation uses the complete six-by-six time-dependent
vector matrix. The recorded bounds are consistent with its stated solver
and comparison tolerances. At j=0 the numerical interaction-picture
change exceeds the analytic tail bound by about 2e-11, within the explicitly
allowed 2e-10 numerical error. That is not a violation of the exact tail
inequality. The independent check uses different parameters, a different
wave direction and both nonzero signs, and reconstructs the bound without
frozen-time propagation. The j=0 exact integrated-phase control in the
author script is valid because that special case's exchange matrices commute.

Two scope details remain essential rather than unresolved defects. First,
the norm ratio and invertible late-wave amplitude apply to F=(U_K,V_K), as
specified by the U,V norm and matrix block in the note. The full density
mode decays separately; neither it nor all fourteen components obey that
lower norm ratio. Second, the rate effects beta/N use the microscopic
clock, while the reaction beta in the Euler equation uses the accelerated
macroscopic clock. There is no omitted factor of N between these statements.

The two late-time conclusions concern different objects: the scattering
argument is for the deterministic finite-mode linearized Euler ODE, whereas
the selected canonical covariance is obtained by taking late time first
at each finite microscopic volume. They are not combined into a native
stochastic late-time wave or fluctuation theorem, nor do they assert that
those two orders of limits commute.

The independent post-comparison script also checks exactly the
quantum-only marginal identity S^T P=(j/7)S^T already derived and sealed
in Section 1. This is a positive witness for the excluded quantum-only
interface, not a realization of the original marked probability law.
No new mathematical discrepancy was found during this phase.

## 13. Reproduction, boundaries and final seal

From this directory the independent evidence is reproduced with

    OPENBLAS_NUM_THREADS=1 python3 independent_check.py
    python3 compare_sources.py

The first program has its initial helper failure preserved alongside the
successful second run. The second authenticates the source/results/logs and
performs the supplementary exact marginal check without importing or
executing author code. The independent LP and ODE outputs are explicitly
numerical; the carrier probability, character, moment and Kraus controls
are exact except their labeled endpoint-eigenvalue samples.

The mathematics remains conditional on the specified preparation encoding,
carrier dimension, resource independence, instrument model, projective
unitary covariance and pure-parent condition where each is invoked. Those
are separate interface hypotheses, not consequences of the minimal
framework axioms. Likewise, the changed birth kernel, context exchange,
clock and field readout are supplied constructions. A physical spatial
carrier, exact permanent unknown-parent histories, a native stochastic
fluctuation theorem, uniform late-time/volume mixing, and the desired
non-product spectral state remain outside the proved claims.

FINAL_SEAL.json binds this report, all initial and final review artifacts,
all source identities and the unchanged procedural dependencies. The result
is complete bounded source scrutiny with no actionable mathematical finding;
it is not a formal retained-status or audit decision. Earlier sealed
evidence remains byte unchanged.
