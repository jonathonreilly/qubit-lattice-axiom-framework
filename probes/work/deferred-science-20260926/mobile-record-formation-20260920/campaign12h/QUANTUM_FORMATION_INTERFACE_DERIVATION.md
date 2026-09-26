# Primary derivation: a single-qubit interface for the formation kernel

2026-09-21. This is a new conditional interface test, personally derived
before a separate check. It is not a consequence of the four minimal axioms.
It asks whether the classical record law studied in this campaign can also
be implemented under a specific ordinary quantum-operation interpretation.
The primary symbolic and unrestricted convex-program checks below are now
complete. A separate pre-source derivation sealed at 02:02:21 UTC confirms
the results; its report and checker have been read completely.

## Explicit interface assumptions

The parent is one physical qubit in an unknown one of the six states
rho_a=(I+v_a dot sigma)/2, v_a in {+/-e_x,+/-e_y,+/-e_z}. The device has no
additional register or preparation information specifying a. Its ancillas
start in fixed states independent of a. A formation event returns a classical
six-valued label b whose conditional distribution is the specified kernel.
It may also return the parent qubit in a changed state. Arbitrary instruments,
ancillas and outcome-dependent recovery are permitted under these conditions.

With exactly one occupied neighbor, normalized raw pair weights (p,q,r)>0
give an input-independent total classical birth rate and conditional kernel

```
D=p+q+4r,
P(b|a)=[p if b=a, q if b=-a, r otherwise]/D.
```

The classical outcome requirement matters. Six Bloch rays are not six mutually
orthogonal qubit labels. If b denotes an unobserved ensemble decomposition
and only a newborn qubit density matrix is available, the POVM-kernel claim
below is a different question; see the last section. Equally, an already
available classical register containing a changes the input resource and
evades the single-unknown-qubit assumptions. The minimal-axiom possibility
algebra does not by itself assert this physical channel interpretation.

## Exact Born-kernel criterion

Any instrument producing b has a POVM {E_b}, with
P(b|a)=Tr(rho_a E_b). For each spatial axis i,
(rho_+i+rho_-i)/2=I/2. Consequently the two-input average probability of b
must be independent of that axis. For b=+x the desired averages are
(p+q)/(2D) from +/-x and r/D from +/-y or +/-z. Thus necessarily

```
p+q=2r.
```

Conversely, on this surface set j=(p-q)/(2r), so |j|<1 and D=6r. The unique
effects, since the six input states span all Hermitian qubit matrices, are

```
E_b=(I+j v_b dot sigma)/6.
```

They are positive, sum to I, and reproduce every entry of P. In normalized
weights this is exactly W_ab=1+j v_a dot v_b. Thus an ordinary single-qubit
measurement of the stipulated six classical outcomes implements precisely
the j-family, among these positive p,q,r kernels. The condition removes the
independent axis-population mode; it does not select j or any physical rate.

## Exact best approximation when the criterion fails

Measure the discrepancy by the largest total-variation distance among the
six input rows. Optimize over ALL qubit POVMs with these six output labels,
including non-covariant ones. Averaging an arbitrary POVM over the 24 proper
cubic rotations cannot increase this convex, permutation-invariant worst-row
loss. The averaged effects commute with the stabilizer of their own output
axis. Hence they have the form

```
E_b(s)=(I+s v_b dot sigma)/6,  -1<=s<=1.
```

For one input row, put d=p+q-2r, A=d/(3D),
B=(p-q)/(2D)-s/6. The exact total variation is

```
TV(s)=|d|/(3D)+max{|d|/(3D), |(p-q)/(2D)-s/6|}.
```

Indeed the equal/opposite discrepancies are A+B,A-B, while each of the four
orthogonal discrepancies is -d/(6D). Their absolute sum divided by two gives
the displayed formula. The interval

```
[(3(p-q)-2|d|)/D, (3(p-q)+2|d|)/D]
```

always intersects [-1,1] for positive p,q,r. For example if p>=q and d>=0,
the lower endpoint is (p-5q+4r)/D<=1; if d<0 it is
(5p-q-4r)/D<1 because p+q<2r. The opposite endpoint condition follows by
exchanging p and q. Any s in that intersection attains

```
min_POVM max_a TV(P(.|a), Tr[rho_a E_.])
       = 2|p+q-2r|/[3(p+q+4r)].
```

For raw (3,1,2) the distance is zero. For (6,1,2) it is 2/15. For (12,1,2)
it is 2/7. The stronger stochastic-correlation menu in this campaign is
therefore not a small perturbation of this particular single-qubit interface.
That does not invalidate the classical simulations or an implementation with
additional classical/spatial resources.

## Minimal disturbance on the exactly realizable family

Suppose now P is exactly the j-family. Write an arbitrary instrument on the
retained parent as Kraus operators K_(b,mu), with
sum_mu K_(b,mu)^dagger K_(b,mu)=E_b. This description includes discarding
other outputs and any recovery based on b. Let Lambda be the parent channel.
Its average preservation fidelity on the six equally weighted input states is

```
F6=(1/6) sum_a Tr[rho_a Lambda(rho_a)]
  =[2+sum_(b,mu) |Tr K_(b,mu)|^2]/6.
```

To see the second equality directly, the six-state average satisfies
(1/6)sum_a rho_a tensor rho_a=(I+SWAP)/6. Insert each Kraus operator and
use trace preservation. No continuum input prior or experimental fidelity
data are needed.

For each fixed b, write K_mu=A_mu sqrt(E_b), where sum_mu A_mu^dagger A_mu=I
on its support. In an eigenbasis of E_b with eigenvalues lambda_1,lambda_2,
the triangle inequality in the vector of Kraus indices and completeness give

```
sqrt(sum_mu |Tr K_mu|^2)
 <= sqrt(lambda_1)*sqrt(sum_mu |(A_mu)_11|^2)
   +sqrt(lambda_2)*sqrt(sum_mu |(A_mu)_22|^2)
 <= sqrt(lambda_1)+sqrt(lambda_2).
```

The sum of squared traces is therefore at most (Tr sqrt(E_b))^2. A single
K_b=sqrt(E_b) attains the bound for every b simultaneously. With the two
eigenvalues (1+j)/6 and (1-j)/6, this proves the sharp optimum

```
F6_max=(2+sqrt(1-j^2))/3,
minimum average infidelity=(1-sqrt(1-j^2))/3.
```

The square-root (Lueders) instrument is a constructive optimal witness. Its
parent channel is depolarizing with Bloch shrink factor

```
eta=(1+2 sqrt(1-j^2))/3.
```

To check this algebraically, write sqrt(E_b)=a I+b v_b dot sigma, with
a^2=(1+sqrt(1-j^2))/12 and b^2=(1-sqrt(1-j^2))/12 (choose b with the sign
of j). Sum over the six axes. The linear terms cancel, and
sum_i sigma_i rho sigma_i=2 Tr(rho) I-rho supplies the stated eta.

At j=1/2, the minimum average infidelity is (2-sqrt(3))/6, about 0.04466
per formation operation. At small j it is j^2/6+O(j^4). This is fidelity
loss on a physical unknown qubit under the specified interface, not an
empirical rate at which the abstract record changes. Exact immutable physical
parent states would have F6=1, so only j=0 permits this entire six-state
classical-outcome interface without disturbance.

## Why mobility, ancillas, and weaker interfaces need separate treatment

Moving the parent by a content-preserving SWAP before or after the operation
does not evade the conclusion if the retained output qubit is followed with
the record. Input-independent ancillas and outcome-dependent recovery were
already included. Repeatedly moving to fresh sites does not supply a second
copy of the unknown state. A known orthogonal pointer basis or a classical
label register is a genuine different resource; standard controlled copying
then has a positive construction, as the repository's pointer-broadcast note
already illustrates. A spatial code may encode more orthogonal labels while
keeping one qubit per fundamental site, with an explicit carrier/cost bridge.

The no-disturbance implication also has a simple basis-independent proof.
In a Stinespring dilation, a pure retained input that remains exactly pure
forces V|psi_a>=|psi_a> tensor |e_a>. Inner products imply |e_a>=|e_c> up
to phase for any nonorthogonal input pair. The six-state overlap graph is
connected, so the complementary output cannot depend on a. This is the
standard no-information-without-disturbance mechanism, not a new principle.

If only the newborn physical qubit is retained, with the classical b label
discarded or never supplied, its stipulated marginal is merely

```
sum_b P(b|a) rho_b = [I+lambda v_a dot sigma]/2,
lambda=(p-q)/(p+q+4r).
```

The axis-population parameter has disappeared from this marginal. Thus the
POVM criterion and its minimax number must NOT be used as a no-go for that
weaker interface. There is a distinct exact channel criterion, added following
the independent calculation: the six promised inputs span the qubit operators,
so the only possible channel for these marginals is the depolarizing map
rho -> lambda rho+(1-lambda)I Tr(rho)/2. Its normalized Choi matrix is diagonal
in the Bell basis with eigenvalues (1+3lambda)/4 and (1-lambda)/4, the latter
threefold. It is completely positive exactly when -1/3<=lambda<=1. In that
interval the Pauli channel with these four nonnegative probabilities attains
the required marginals. Thus not every positive classical (p,q,r) menu even
admits the weaker quantum-only output. Exact preservation of the unknown parent still prohibits
a nonconstant complementary output, so lambda!=0 remains incompatible with
an exactly unchanged parent under ordinary quantum dynamics. An optimal
approximate quantum-only parent/offspring tradeoff would be a different
problem, related to asymmetric cloning, and has not been derived here.
If hidden b labels affect later formation, their operational role over full
future histories also needs a separate sufficiency test.

## Context and next checks

The repository already distinguishes copying orthogonal pointer facts from
cloning arbitrary qubit states in
`docs/RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md` (read fully).
The direct nonorthogonal controller argument in section 7 of the historical
`docs/work_history/repo/review_feedback/RECORD_STATE_ONE_M2_NN_FORTRESS_CYCLE26_NOTE_2026-07-14.md`
was read; its broader historical ontology and fortress claims are not adopted.
The separate pointer non-demolition note dated 2026-06-05 was read completely
and explicitly supplies its physical pointer/dynamics bridge.

Primary literature context: Banaszek, [Fidelity balance in quantum operations](https://arxiv.org/abs/quant-ph/0003123),
derives information/disturbance bounds through operation fidelity; its Kraus
fidelity formula was inspected. Barnum et al., [Noncommuting mixed states
cannot be broadcast](https://arxiv.org/abs/quant-ph/9511010), is a related
general quantum constraint. The calculations above apply elementary channel
and covariance machinery to this specific formation kernel; they do not claim
novelty for the underlying quantum-information principles.

`quantum_formation_interface_check.py` implements the primary checks without
imposing covariance on the numerical feasible sets. The exact symbolic checks
cover the six-state second moment, 36 POVM probabilities, and three Pauli
channel identities. Sixty-five unrestricted six-effect qubit POVM programs
agree with the minimax formula to maximum absolute discrepancy 2.55e-11.
Nine unrestricted instrument Choi programs agree with the fidelity formula
to maximum absolute discrepancy 3.25e-10. Direct square-root channels also
reproduce the probabilities, fidelities and depolarizing action. Full results,
source hash and package versions are in `QUANTUM_FORMATION_INTERFACE_RESULTS.json`.
These floating-point optima support the analytic proof; they are not exact
optimization certificates or independent scrutiny.

Two initial endpoint runs at j=-1 returned `optimal_inaccurate`, first with
CLARABEL and then SCS. Both failure logs are retained as
`QUANTUM_FORMATION_INTERFACE_FIRST_ATTEMPT.log` and
`QUANTUM_FORMATION_INTERFACE_SECOND_ATTEMPT.log`. Their historical intermediate
source hashes were not captured, so the logs alone do not identify those
intermediate programs byte-for-byte. The final source handles |j|=1 by exact
facial reduction: a positive Choi matrix whose input partial trace has rank
one must have the form E_b^T tensor tau_b, with arbitrary output density
matrix tau_b. This retains the full feasible set and restores a strictly
feasible reduced problem; it does not force the square-root answer. The
positive-weight model itself uses |j|<1, where this reduction is unnecessary.

Independent evidence: `independent_quantum_interface/REPORT.md`, SHA-256
`38be6c4c55724ae3329659cc61f605d95e507f7c3a004c5f04929e8595c75f52`.
All five artifacts listed in its pre-source seal were verified. The separate
derivation includes exact effect/rank checks, a linear-program lower-bound
check, and explicit instrument dual certificates. The quantum-only Choi
classification above is credited to that calculation and reconstructed here.
No retained-status or independently audited claim follows from this check.
The later repeated-history and waiting-law notes test further obligations;
preserve the classical/quantum-only distinction in any publication.
