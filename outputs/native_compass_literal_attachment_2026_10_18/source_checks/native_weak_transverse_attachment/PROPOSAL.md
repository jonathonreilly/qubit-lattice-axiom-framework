# Weak transverse compass attachment to the given literal old pair

**Status: proposed conditional finite-device theorem; distinct check required.** An open cube in the existing anisotropic compass family, with the given literal old K installed explicitly once, approximates the specified W with complete elapsed old aging and a common evolving six-qubit environment. No additional direct target-generator interaction is inserted: the cube's existing x-bond supplies it. The claim is conditional on a small existing transverse-to-x coupling ratio, a finite open boundary, and a delivered product collar. It neither derives K or the compass dynamics from axioms nor preserves the original source-contact apparatus.

## Exact sources and scope

The immutable sources read completely in the immediately preceding probe are:

* PR9752 head `33f0af206df4897744a9d5e248c2889fdd6ed1e7`, docs/NATIVE_CONSERVED_SCALAR_NOTE_2026-10-18.md, raw-body SHA256 `1b579ec1901f2389b4fb058649b8ea78f0d0d0c4737e36c54af1c400bf4f795e`,6226 bytes. It specifies H_c=−Σ_(r,a)J_a σ_r^aσ_(r+e_a)^a. Its isotropic scalar statements and supplied infinite-temperature ensemble are NOT used here.
* PR9747 head `e161fcef330a7cad87a19e3ffcb2fc3b03691083`, docs/NATIVE_LOCAL_NORMALFORM_NOTE_2026-10-18.md, SHA256 `debd8448a97a982d23074582e983438cebc880a86cb03f44bfe9be57921d4d3d`,9105 bytes. It explicitly permits finite open or periodic boundaries in its local interaction construction. Its z-dominant perturbative estimates are NOT imported into the present x-dominant regime.

These exact source identities and unchanged model scope are reused, not a new reread or audit. Positive J_x,J_y,J_z are supplied model parameters. Restricting their ratio below is a declared parameter subfamily, not evidence that the actual physical coefficients have that ratio. Open-cube restriction is a supplied finite boundary; it is not a method for isolating a cube inside an interacting infinite lattice. The source's periodic-length-at-least-five condition concerns its spectral/ensemble calculation, which is not invoked.

Literal target identities reuse the frozen direct benchmark `c0cc65e615bb6bdb7466c01c68ce53d6647c75e73a322bd88fff97580428f7d6` and its scoped review `e58d3fd82b27d94ae862a528707e3eb279ad5964dd5ca4641fb0e7e4fbfe3e38`. The present attachment is new; that review does not validate it. The earlier all-Z collar probe `a9efcd04212f4291c60b2eb659b7fb3ed7c04e4daefbd260c34ca6464aa6a5c0` remains frozen and is not contradicted: its old pair had external x-bonds absent in this cube.

## Actual geometry and positive inventory

Use all eight sites of Ω={0,1}³. The old sites are1=(0,0,0),2=(1,0,0). Their six-site complement is E. Install all twelve nearest-neighbor compass edges in Ω, each with its existing directional coefficient:

    Q_a(v,w)=J_a(I−σ_v^aσ_w^a),  a=x,y,z.

Also retain the GIVEN old K=2I+Z1Z2 on the literal pair, counted once. This thirteenth block is an explicit attachment premise, not a term derived from the compass source. No source A/B terms, source contacts, head, clock or record R are installed. In particular retaining old K does not mean retaining the original four-qubit internal B; that changed inventory is essential.

Each Q_a is positive with spectrum0,0,2J_a,2J_a and full-support norm2J_a. All are real matrices, including YY. K is positive with norm3. Every cube site has one bond of each direction. The incident loads are therefore

    old sites: 3+2(J_x+J_y+J_z),
    other sites: 2(J_x+J_y+J_z).                       (1)

Thus Λ>3 and 2(J_x+J_y+J_z)≤Λ−3 suffice. The construction has eight qubits and thirteen positive blocks on ordinary cubic nearest-neighbor supports. It uses no selectively deleted edge inside Ω. Missing edges outside Ω belong to the explicitly supplied open-boundary contract.

There are four x-bonds: one is the old edge and three are within E. There are four y-bonds and four z-bonds: each direction has two old-to-E bonds and two E-to-E bonds. Let H_E be the sum of these seven positive E-to-E blocks. Set s=J_y+J_z. The exact full decomposition is

    H = H_0+V,
    H_0=[K+J_x(I−X1X2)]⊗I_E + I_old⊗H_E +2s I,
    V=−J_y(Y1Y_(0,1,0)+Y2Y_(1,1,0))
      −J_z(Z1Z_(0,0,1)+Z2Z_(1,0,1)).               (2)

Equation(2) includes the identity part of all four crossing bonds as2s I. No unwanted Z field has been canceled. The full-support triangle inequality gives ||V||≤2s, without restricting to a head-number or ready sector. Individual y/z crossing operators sharing an old site need not commute; the norm bound does not assume they do.

## Complete target, phase and finite window

Supply the basis-product collar χ=|0>_E^⊗6, independent of the arbitrary old input. It may be regarded simply as a mathematical input condition; no native preparation or relaxation claim is made. Let χ(t)=exp(−itH_E)χ. This normalized common environment need not stay blank or product. All six environment outputs are retained; discarding them or replacing them with blanks would change the theorem.

Write X=X1X2 and choose θ∈(π/4,π/2), cosθ=3/5, sinθ=4/5. The literal W is

    W=[(9+12i)I+(-16+12i)X]/25=exp(iθ)exp(iθX).

Since [K,X]=0, the reference evolution is exactly

    exp(−itH_0)(ξ⊗χ)
     =exp[−i(J_x+2s)t] exp(−itK)exp(iJ_xtX)ξ ⊗χ(t).   (3)

Set τ=θ/J_x and define the whole-output isometry

    T_t ξ = exp[−i((J_x+2s)t+θ)] exp(−itK)Wξ⊗χ(t).     (4)

At t=τ, equation(3) agrees exactly with(4); its scalar is exp[−i(2θ+2sτ)]. The scalar of the seven positive environment blocks remains inside χ(t), so it is not omitted or counted again. The scalar2I in old K likewise remains inside exp(−itK). This is full elapsed old aging, with no subtraction of travel or preparation time.

For t≥0, exact finite-dimensional Duhamel on the full space gives

    ||exp(−itH)−exp(−itH_0)||≤t||V||≤2st.

The old rotational error is exactly2|sin[J_x(t−τ)/2]|. Combining these yields the complete induced norm bound

    ||exp(−itH)(·⊗χ)−T_t||
      ≤2st+2|sin[J_x(t−τ)/2]|
      ≤2st+J_x|t−τ|.                               (5)

This includes arbitrary coherent old inputs and arbitrary passive extensions because it is a full-space operator estimate composed with an isometry. It controls leakage and entanglement with E without postselection. For mixed old/passive inputs, the unhalved complete channel distance is at most twice the right side of(5), by purification. This does not need the actual environment to remain uncorrelated; any difference from the common target is paid in(5).

An explicit simultaneous sufficient policy, for0<ε≤1, is

    r=(J_y+J_z)/J_x ≤ ε/[32(θ+1)],
    w=ε/(16J_x),   t∈[τ−w,τ+w],
    2J_x(1+r)≤Λ−3.                                 (6)

The lower endpoint is positive since θ>π/4>1/16. On this interval,

    J_x|t−τ|≤ε/16,
    2st≤2r(θ+ε/16)
         ≤(ε/16)(θ+1/16)/(θ+1)<ε/16.

Thus complete vector error is less than ε/8 and unhalved complete channel error is less than ε/4. The relative half-width is ε/(16θ). The count is fixed; τ=θ/J_x and w=ε/(16J_x). For a family with J_x fixed and existing transverse ratio restricted as ε decreases, center time is fixed and the certified window shrinks linearly. For a single fixed nonzero ratio r, (6) does NOT certify arbitrarily small ε. Nor is(5) a necessary error or physical precision lower bound.

For example one may state a nonempty sufficient parameter domain J_x≤(Λ−3)/4 together with(6)'s ratio, since r<1; this is a conditional subfamily, not a prescription to retune an unspecified real material. No fitted new microscopic coefficient or cancellation term was introduced.

## Scope and remaining suppliers

This is an honest conditional bridge from the *specified compass family plus given K* to the literal old operation. It replaces the independent direct XX actuator premise by the actual x-bond of that family, at the price of finite boundary supply, weak transverse coupling and a moving environment output. It does not derive K, choose the compass Hamiltonian, explain the anisotropy, or prepare χ. The exact original source A/B dynamics is removed; this is not a theorem for the unchanged original two-port apparatus. The original endpoint theorem remains separate and valid under its own stated premises.

It is not a theorem that an arbitrary infinite native substrate can be carved into this cube without outside interactions. An actual embedded cube requires bounds on those missing exterior contacts. Nor does the z-dominant normal-form result automatically apply here: our proof uses only the exact compass definition and elementary full-space Duhamel, and openly chooses a different coefficient regime.

There is no spatial head output, record flag, capture, reset or permanent halt. At the observation window the whole target is the aged old operation and its common evolving six-qubit environment. Nothing switches off the old x-bond or the crossings. No energy-reference supplier or old-aging substitution is used. The static observation time still depends on the known J_x; this is not an autonomous release mechanism. Claims about physical readout, time units, native basis-state preparation and manufacturing tolerances remain outside this calculation.

ROOT proposed the cube boundary and weak-transverse route; I independently reconstructed its exact edge inventory, scalar split, full-support norm budget, phase and finite window. Shared design/model/source exposure is explicit. No scientific execution or new agents were used. Only this proposal was written; no frozen source, Git, canonical document, checkpoint, axiom, editable prompt or model/effort was changed. A distinct mathematical check is required before composing on this new interface.
