# Emitted sparse-compiler word: one complete numerical fixture

**New author-produced evidence; sparse-compiler acceptance remains pending.** The requested q=1,L=1 word was generated down to forward A gates and onsite Z rotations, then routed by actual adjacent full SWAPs. Its complete 32-by-16 input isometry agrees with the specified buffered-prefix target to observed operator residual **2.951e-13**. The routed count is **24,720**, below Gbar=44,688. Omitting determinant compensation produces observed error **1.8461538461538018**, agreeing with the exact fixture prediction 24/13. These are complex128 residuals, not interval certificates or a general compiler certification.

The frozen candidate `6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b` and its freeze `1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9` were rehashed and remain unchanged. No earlier checker was imported or rerun.

## 1. Complete target and exact order/phase prediction

Use q=1,L=1,M=3,n=4,m=5. Physical sites are numbered 0 through 4, with site 0 the most significant bit and site 4 the synthesis ancilla. Let

    z=(5+12i)/13,
    V=z [[3/5,4i/5],[4i/5,3/5]],
    det V=z^2=(-119+120i)/169.

The selected four-qubit ordered basis pairs are

| Total number a | First state | Second state | Decimal indices |
|---|---|---|---|
| 1 | 0100 | 1000 | (4,8) |
| 2 | 0110 | 1100 | (6,12) |
| 3 | 0111 | 1110 | (7,14) |

Define U_1(V) by V on each pair and identity on the other ten basis states. All six selected columns actually change for this V. The upper a=3 block is retained. Let J append ancilla zero: J[2j,j]=1. The complete comparator is **C J=J U_1(V)**, with no phase minimization and no discarded output row. Its operator-norm form includes arbitrary data/reference inputs; the executable checks the entire 32-by-16 matrix representing this map.

For the first column (a,b)^T of V the Givens matrix is

    G=[[conj(a),conj(b)],[-b,a]],   G V=diag(1,det V),
    V=G^* diag(1,det V).

Here the normalization radius is exactly one. Each sector therefore applies its determinant phase **first** in time and then G*. In the five-qubit space the determinant phase is a determinant-one diagonal two-level gate on the respective pairs

    (10000,00001), (11000,01001), (11100,01101),
    or decimal (16,1), (24,9), (28,13).

It applies det V to the first state and its inverse to the second. Every first state has ancilla zero and every partner has ancilla one. This is the source's single-clean-ancilla construction; it does not impose identity on the whole ancilla-one subspace. The complete output retains that ancilla, including numerical leakage.

## 2. What was actually emitted

`emitted_word_fixture.py` implements the candidate formulas directly. Its gate lists are chronological; a dedicated `product` helper reverses the list of matrix factors, avoiding an implicit convention change.

* One controlled SU(2) leaf uses X-Y-X Euler rotations. The internally reconstructed Euler matrices are checked before emission. The ordered target basis is always |01>,|10> on the two named target sites.
* Each controlled X rotation expands the source's F/S conjugation into two variable-XY words, forward A powers for every iSWAP and inverse, and onsite Z letters. A*=A^7 and iSWAP*=A^6 are counted literally. Each controlled X word has 50 letters.
* The controlled Y rotation is S X S* conjugation; the paired S factors are emitted as opposite Z angles. The total controlled SU(2) leaf has 152 letters: 120 A and 32 Z.
* For k>1 the actual source commutator split is emitted recursively. The numerical factors A0,B0 are checked against A0 B0 A0* B0*=U before their descendants are emitted. Both zero and one control values are used by this fixture. T(2)=4 and T(3)=10 are evaluated by the integer recurrence.
* Each data Givens pair has two controls and costs 608 letters. Each determinant phase has three controls and costs 1,520. All factors, including zero-angle rotations, are retained, so there is no unreported optimizer or cancellation.
* Every arbitrary-pair A is surrounded by an actual full-SWAP route and its reverse on the five-site path. Each generated physical edge is asserted adjacent. Each route record carries its originating logical-gate index and whether it moves out, applies A, or returns. All wire assignments are restored after each elementary gate.

The count read from the emitted lists is

| Word | Forward A | Onsite Z | Full SWAP | Total |
|---|---:|---:|---:|---:|
| Logical | 5,040 | 1,344 | 0 | 6,384 |
| Routed | 5,040 | 1,344 | 18,336 | 24,720 |
| Mutant logical | 1,440 | 384 | 0 | 1,824 |
| Mutant routed | 1,440 | 384 | 2,496 | 4,320 |

There are 42 single-control SU(2) leaves: three sectors times [T(2)+T(3)]. Thus

    G0=3*152*(4+10)=6,384,
    Gbar=(2n-1)G0=7*6,384=44,688,
    tighter uniform routing bound=1,344+7*5,040=36,624.

The actual 24,720 lies below both routed bounds. These counts concern the circuit. The physical endpoint illustration below adds five simultaneous onsite number-phase generators in one further time slot; those five generators are explicitly priced and are not hidden in the circuit count.

## 3. Complete residuals and the load-bearing mutant

The source propagates the full 32-by-32 logical and routed matrices. It also constructs the 32-by-16 comparator independently from the six explicit selected indices and V. All matrix outputs are saved in `complete_matrices.npz`; all logical and routed nominal/mutant words are complete JSON lists.

| Quantity | Observed value |
|---|---:|
| ||C_routed J-J U_1(V)||_op | 2.9508448902312835e-13 |
| Full isometry Frobenius residual | 8.930355179806793e-13 |
| Maximum column Euclidean error | 2.9506123471984577e-13 |
| Identity on all ten unselected inputs, operator residual | 2.950835855960473e-13 |
| Ancilla-one output, operator norm | 1.203455149051588e-14 |
| Isometry defect ||(CJ)*CJ-I||_op | 5.90018483444466e-13 |
| Full 32-input routed/logical operator residual | 0.0 |
| Full 32-input total-number commutator | 0.0 |
| Largest internal Euler reconstruction residual, 42 checks | 2.556934838376727e-16 |
| Largest internal SU(2) commutator residual, 12 checks | 2.1912899996703748e-16 |

Zero in this table reports the returned floating-point value; it is not a certified exact-arithmetic result. The mathematical number-conservation and wire-permutation claims have separate source arguments. The internal residuals are diagnostics of this emission, not replacements for the complete comparison.

The sole load-bearing mutant deletes every sector determinant-compensation word while keeping the same Givens factors and routing algorithm. Its isometry error is **1.8461538461538018**, while the unselected-input error remains 8.209e-14 and the ancilla-one leakage is zero. Hence those latter two checks alone would miss this phase failure.

There is an exact analytic prediction for this particular mutation. On each selected block the mutant is G*, whereas the target is G*D with D=diag(1,det V). Unitary invariance gives

    ||G*-G*D||=|1-det V|=|288-120i|/169=24/13.

The observed value differs by 4.441e-14. This tests a relative phase against the off-sector identity; no freely chosen global scalar was used to improve either comparison.

## 4. Positive-pulse scalar and one declared laboratory endpoint

The scalar check evaluates the positive generators by local Hermitian eigendecomposition, independently of the logical gate-matrix routine:

    Q_A=(pi/4)(I-R),
    Q_Z(phi)=|phi|I-phi Z,
    Q_SWAP=(pi/2)(I-SWAP).

Every eigenvalue is checked against the declared floating tolerance for positivity. These are exactly the parent's supplied generators; full SWAP remains an extra physical permission. The positive-word comparator is

    C_positive=exp(-i Phi) C_routed,
    Phi=(pi/4)*5,040 + sum over the 1,344 emitted |phi|.

For the actual emitted angles Phi=4732.64387840259; the observed complete-isometry residual is 3.6647411565014315e-12. A full SWAP has endpoint scalar one in this convention. Its positive generator and reserve remain physically counted.

For an illustrative endpoint choose units with hbar=1, E0=1/5, Delta=7/10, h=1. Set Q*=6pi, g=24pi and sigma=24pi^2, so both fixed-slot inequalities in the parent hold with equality. The literal free Hamiltonian is F=E0 I+Delta N_tot on all five qubits. With the actual circuit count,

    tau=(24,720+1)h=24,721,
    r=2754.125, k=floor(r)+2=2756,
    lambda=2pi k-Delta tau=11.758706586941116.

The program verifies numerically that |r-Delta tau/(2pi)|<=1/4 and 3pi/2<lambda<=9pi/2. Five positive onsite generators lambda n act simultaneously in the last slot. All controls commute with F; free evolution is retained during every circuit and phase slot. The source's exact symbolic endpoint identity is

    U_lab(tau)=exp[-i(E0 tau+Phi)] C_routed.

The separately evaluated full comparator residual is 5.44294855010996e-12, with gamma approximately 0.7394755605940313-0.6731834038983308i. The final lambda n layer is evaluated as exp(-i lambda N_tot); its identity reserve is not discarded or counted again in Phi.

This illustration declares 24,725 control generators in 24,721 slots, ideal common added incident cap Delta+g/2=38.39911184307752, and ideal slew at most sigma/2. Its maximum free energy is 3.7. The parent's loose bound on absolute prescribed-drive work is g(G+m)=1,864,221.0806401833 in these units; ideal net work is zero for the supplied commuting drive. These are consequences of the stated pulse model, not measured hardware quantities. No actual waveform, calibration, microscopic driver, interval arithmetic or energy measurement is simulated here. Physical perturbations and initial/final energy errors still need the parent's separate budgets with the same physical F; none are set to zero by this fixture.

## 5. Execution provenance and limits

There was one scientific launch and it completed successfully. No failed attempt was deleted; none occurred in this packet. The separately generated mutant failed the desired comparator as intended and is retained with its full word and output.

* Source at launch: `runs/attempt_01/source_at_launch.py`, SHA256 `e7dc44e6493fb9d847390161e109d3fe58d5124fb1ce8e308eeec4dfd93bb7c8`.
* Launcher at launch: `runs/attempt_01/launcher_at_launch.py`, SHA256 `fd9229b989b33e4a3959dc42fcbadcc016b82dc0ef56cccd6436b672cf03deb5`.
* Started 2026-10-16T15:14:50.930833Z; completed 15:14:51.934683Z; elapsed 1.003451709 seconds; exit 0.
* CPU limit 90 seconds; subprocess wall timeout 120 seconds; no address-space limit imposed. BLAS/OpenMP thread overrides were one. Exact argv/cwd and limits are in `EXECUTION.json`.
* Python 3.13.5, NumPy 2.4.4, complex128, machine epsilon 2.220446049250313e-16. The discriminator threshold 1e-9 was in the source before execution. NumPy eigendecomposition/SVD and trigonometric evaluation have no certified outward rounding here.
* Full stdout SHA256 `4e279574f87ea9dfabf4f98de5db201801892f93f6f1258fcbc098f7277a9ba9`; stderr is empty, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

This is an exposed continuation by the compiler's author using the same inherited model and reasoning. Root's independent acceptance of the sparse candidate is still pending. The root proposal and review directories were not read. The control-parent acceptance/status was reported by root; this numerical packet relies on the pinned mathematical source and imports no new review conclusion.

The fixture exercises Givens order, two- and three-control splitting, complex determinant compensation, clean ancilla return, all unselected inputs, spatial routing and paid scalar conventions. It does not exercise distance-greater-than-two logical basis-state routing, q>1 block elimination, arbitrary zero-pivot selection or certified finite-error word search. At L=1 it is a compiler test for U_1(V); it gives no useful small-error unchanged-reservoir guarantee for implementing V. A general claim needs the source proof and independent review; a certified instance needs interval/rational bounds on its full residual. No broad failure or impossibility result is inferred.

Only this new packet directory was written. The earlier source/freeze, canonical sources, Git, PRs, audit/cache/lock state, prompts and axioms remain unchanged. Root controls acceptance and publication. No editable prompt file changed.
