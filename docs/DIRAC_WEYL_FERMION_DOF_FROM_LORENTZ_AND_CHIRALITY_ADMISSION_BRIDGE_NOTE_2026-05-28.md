# Supplied Dirac/Weyl matrix fixtures and count comparison

**Date:** 2026-05-28 (scope corrected 2026-10-23)
**Type:** open_gate
**Status authority:** source proposal only; independent audit controls effective status.
**Primary runner:** [finite matrix checks](../scripts/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.py)
**Cached output:** [runner output](../logs/runner-cache/audit_companion_dirac_weyl_fermion_dof_from_lorentz_and_chirality_2026_05_28.txt)

This note records supplied complex matrices, finite fixtures, and exact
cardinality arithmetic. It supplies no current ledger authority. The older
Q1/R2 retained-status contract is withdrawn from this source's premises.
No real Clifford-algebra classification, derivation of a physical Dirac
equation, CPT theorem, physical particle inventory, or general mass-shell
exhaustion is claimed. The physical identification remains open.

## Explicit matrices and scope of the algebra

Let I be the 2 by 2 identity and sigma_1, sigma_2, sigma_3 the matrices

```text
sigma_1 = [[0,1],[1,0]],
sigma_2 = [[0,-i],[i,0]],
sigma_3 = [[1,0],[0,-1]].
gamma^0 = [[0,I],[I,0]],
gamma^k = [[0,sigma_k],[-sigma_k,0]] for k=1,2,3.
```

These are specified matrices on C^4. Direct multiplication gives
{gamma^mu,gamma^nu}=2 eta^(mu nu) I_4 with eta=diag(1,-1,-1,-1).
The separate presentation Gamma_k=i gamma^k, Gamma_4=i gamma^0 obeys
signature (+,+,+,-). Several Gamma entries are imaginary. This is
**not a real-matrix classification** or a proof that a real algebra is M_4(R).
No conversion of complex dimension four to an irreducible real spinor
classification is inferred.

For the Gamma presentation, set omega=Gamma_1 Gamma_2 Gamma_3 Gamma_4.
Anticommuting the four generators gives omega²=(-1)^6(1)(1)(1)(-1)I=-I.
Thus gamma_5=i omega squares to I and anticommutes with each Gamma.
Consequently P_L=(I-gamma_5)/2 and P_R=(I+gamma_5)/2 are complementary
orthogonal idempotents (their product is zero). The explicit matrix ranks
are two each over C. The runner checks these products and ranks exactly.
It does not identify these complex projectors with a split of R^4.

## Finite mass-shell fixtures

Use the standard gamma presentation and define
D(p,m)=p_0 gamma^0-p_x gamma^1-p_y gamma^2-p_z gamma^3-m I_4.
The supplied fixtures are:

| Fixture | Supplied p and m | Exact matrix observation |
|---|---|---|
| Rest | p=(3,0,0,0), m=3 | rank 2; complex nullity 2 |
| Moving | p=(5,0,0,4), m=3 | p_0²-p_z²=m²; det D=0; rank 2; nullity 2 |
| Negative energy | p=(-5,0,0,4), m=3 | det D=0; rank 2; nullity 2 |
| Off shell contrast | p=(5,0,0,0), m=3 | nonzero determinant; rank 4 |
| Massless positive | p=(1,0,0,1), m=0 | nullity 2; rank of each chiral projection of the kernel is 1 |
| Massless negative | p=(-1,0,0,1), m=0 | nullity 2; rank of each chiral projection of the kernel is 1 |

The moving fixture also checks D(p,m)(slash(p)+mI)=0. For the massless
fixtures the runner separately constructs gamma_5=i gamma^0 gamma^1
gamma^2 gamma^3 and the corresponding projectors, then projects an exact
nullspace basis. All arithmetic uses symbolic matrices and rational numbers.
These are finite calculations. They do not establish a complete physical
spectrum, a general enumeration of on-shell states, or an identification
of negative-energy solutions with physical antiparticles.

## Supplied count and CAR comparisons

Across the two displayed massive energy-sign fixtures the complex kernel
counts add to 2+2=4. For either fixed chirality across the two displayed
massless fixtures they add to 1+1=2. One complex kernel of dimension two
has real dimension four, while C^4 has real dimension eight. The runner's
older 4*2/2=4 expression is retained as supplied dimension arithmetic;
it is not evidence for a real Clifford representation or a physical
thermal multiplicity. Real component counts and thermal state counts
are not interchangeable without an additional physical interpretation.

The supplied matrices c=[[0,1],[0,0]] and c†=[[0,0],[1,0]] satisfy
{c,c†}=I, c²=(c†)²=0, and n=c†c has n²=n and spectrum {0,1}.
Their matrix size is two. Additional binary-label and two-mode dimensions
2, 2²=4, and 2*2=4 are conditional counting identities. They do not prove
CPT or physical spin statistics.

The [g_star supplied inventory note](G_STAR_SM_CONTENT_AT_LEPTOGENESIS_FROM_SUPPLIED_THERMAL_INVENTORY_BOUNDED_THEOREM_NOTE_2026-05-28.md)
uses P4 Dirac and Weyl conventions, including the particle-antiparticle
labels. This runner reads that paragraph only to locate the stated counting
convention. The equality of its integers with these finite fixture counts
does not derive the physical convention or promote the g_star support
packet. The g_star arithmetic remains conditional on its own inventory.

## Historical authority contract and recovery

The complete previous note, runner, and cache remain at Git revision
`fbd1e8030c02ec6fdbb95bdf819be020aa7f043a`, at these same repository paths.
They include the original stronger claims and exact ledger status tests.
The old runner required `docs/audit/data/audit_ledger.json`, absent from
that source snapshot; no fresh successful execution or current status
verification is inferred from its old cache. The old source remains
available for historical reproduction if its actual inputs are recovered.
No ledger was invented, repinned, or restamped.

The current source withdraws that authority contract rather than treating
a missing ledger as a passing test. All finite matrix, rank, CAR, and
arithmetic predicates are retained. Obsolete documentary checks of the
withdrawn authority packet are replaced by explicit scope checks, which
are not mathematical proofs. An actual current capture and independent
source review are still required for this revised runner.
