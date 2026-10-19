> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Weak bounded background for the exact gap-mediated interaction

**Status: proposed conditional interface, pending distinct check.** This addendum preserves PROPOSAL.md SHA256 `d683b07790c9da2d9bf5a27d8045fa19309b918877e31e15431daa74f43d7258` unchanged. It proves a full-output background estimate using that source's exact real rotation. It does not compose several gadgets or implement an arbitrary clock matrix.

## Exact rotation and its distance

Reuse0<λ<1, Z=Z1Z2, Q=X1X2Y_aY_b, R=ZQ, P_±=(I±R)/2, V=λ(Y1Y_a+Y2Y_b), c=2λ+λ², and

    H_eff=K−λ²Q, K=2I+Z,
    H=K+λ²(I−Z)+λ(I+Y1Y_a)+λ(I+Y2Y_b).

The frozen proof gives [R,Z]=[R,V]=0, {Z,V}=0, V²=2λ²(I−R). Thus V vanishes on P_+, and X'=V/(2λ) is a real symmetric involution on P_- that anticommutes with Z. With α=arctanλ, define on the full four-qubit space

    D=P_+ + cosα P_- −sinα ZV/(2λ).                  (A1)

Since ZV/(2λ) is real antisymmetric, vanishes on P_+, and squares to−P_-, D is real orthogonal. Equivalently its P_- restriction is exp(−α ZX'). The rotation identity is

    D Z D† = cos(2α)Z+sin(2α)X'  on P_-.

Because cos(2α)=(1−λ²)/(1+λ²) and sin(2α)=2λ/(1+λ²), the exact full identity is

    H=cI+D H_eff D†.                                (A2)

The nontrivial rotation eigenvalues are exp(±iα), so

    d:=||D−I||=2sin(α/2)≤α≤λ.                       (A3)

The exact norm is not the more generous two-endpoint propagation estimate. P_- is nonempty, so it is attained. All identities extend by tensoring D,H,H_eff with identity on any further finite spectator system; B below may couple that system to the gadget.

## Arbitrary bounded selfadjoint background

Let B be any bounded selfadjoint operator on the full joint Hilbert space. It need not commute with Z,Q,R,V or D and need not preserve a head number or a selected ancillary state. Write B'=D†BD. Equation(A2) gives

    H+B=cI+D(H_eff+B')D†.

The elementary subtraction

    B'−B=D†B(D−I)+(D†−I)B

implies ||B'−B||≤2d||B||. Duhamel for selfadjoint generators then gives, for every real t,

    ||exp[−it(H_eff+B')]−exp[−it(H_eff+B)]||
       ≤2d |t| ||B||.

The two outside D factors cost at most2d by another two-term subtraction. Hence

    ||exp[−it(H+B)]
       −exp(−ict)exp[−it(H_eff+B)]||
       ≤2d(1+|t| ||B||)
       ≤2λ(1+|t| ||B||).                            (A4)

One may cap the right side at2. The common scalar c is retained once. The actual B, including any scalar or old-energy component it contains, remains in the comparator; nothing is silently removed. This is a complete operator estimate, valid for all initial joint states and after arbitrary passive extension. For mixed-state outputs the unhalved complete channel distance is at most twice the capped operator estimate, again capped at2. No ancillary projection or postselection is used.

In particular, if B=λ²B0 for a bounded selfadjoint B0 and |t|≤a/λ² with fixed a≥0, then

    complete vector/operator error≤2λ(1+a||B0||).     (A5)

Thus weak backgrounds with uniformly bounded ||B0|| preserve an O(λ) full-output simulation over the mediated timescale. For desired vector tolerance ε, the sufficient condition λ≤ε/[2(1+a||B0||)] can be combined with λ<1 and the actual incident cap. B0 may depend on λ only if a uniform stated bound is available. An extensive sum cannot be called uniformly bounded merely because its local terms are bounded.

## Physical supplier and assembly boundaries

The actual four positive blocks and base incident loads remain those of the source: old sites3+2λ+2λ², ancillary sites2λ. Equation(A4) is mathematical for any bounded selfadjoint B, but positivity of H+B is not automatic for such a B. To retain an ordinary positive two-body physical inventory, B must separately be presented as supplied positive local blocks on allowed supports, with their full-support norms charged to every incident site. If B=λ²Σ_l b_l with positive listed blocks b_l, then the extra incident load at v is λ²Σ_(l incident v)||b_l||, and a sufficient global bound is ||B0||≤Σ_l||b_l||. These costs are not waived by the small parameter.

The exact rotation may have support beyond a two-site term, but it is only a proof transformation and is never installed as a physical gate. Conjugating B does not create an uncharged physical implementation: the actual device is H+B and the comparison uses H_eff+B. Any new hardware needed for B remains explicit.

For a background of fixed nonzero norm at times O(λ^−2), this bound is generally O(λ^−1), so it does not certify small error. That is a limitation of this estimate, not a lower bound on actual dynamics. Several gadgets sharing the old pair cannot each count K or its counterterm independently; their combined exact rotation and cross terms require another proof. The addendum does not prepare the ancillary Y-pair eigenstate, produce common clock outputs at two samples, establish dwell, or derive native dynamics, capture, reset or permanent halt.

## Exposure and work record

ROOT proposed the weak-background conjugation route. I derived(A1)–(A5) from the frozen exact sector identity, retaining all operator domains, endpoint terms and phases. This is same-model, shared-design author work, not an independent check or retained result. No scientific executable, external search, Git/source/canonical/checkpoint/axiom/editable-prompt/model change, publication or delegation occurred. Only this addendum was written; the frozen proposal remains unchanged. A distinct check is required before downstream use.
