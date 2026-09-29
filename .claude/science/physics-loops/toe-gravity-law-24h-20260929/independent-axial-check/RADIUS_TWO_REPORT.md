# Independent radius-two expanded axial check

Checked 2026-09-29 against science revision `7146fe17a76de41badcaca3c3c7cac6d11eb2a00` and the exact runner inputs below. This is focused mathematical verification, not formal review PASS, audit, primitive adoption, or a physical gravity result.

**Result:** the radius-two system with cubic momentum in G3 and the specified full constraint mixing is inconsistent. An independent explicit finite-torus derivative implementation reproduces every coefficient and right-hand side of its 2,920-column, 3,767-row system. The 752-row dual certificate then cancels every unknown coefficient and yields `0=-1`.

The certificate uses no continuum-zero condition on G3(P³), Z1 or W1. Dropping every such condition leaves it valid. Its only normalization rows are the transverse B,P_B moments: h derivative coefficient +1 and momentum derivative coefficient 0. The same bounded obstruction extends algebraically to every nonzero real alpha and K by the invertible coefficient rescaling proved below. Neither result extends the tested support radius or changes the fixed starting Hamiltonian.

## Exact inputs and prior coverage

`REPORT.md` supplies the independently checked signs, kinetic normalization, continuum moments, and necessity of the axial projection. `EXTENSION_REPORT.md` checks the radius-one enlarged generator and kernel families. The present check changes their radius to two and verifies the complete resulting matrix independently; it does not infer radius-two correctness from those earlier calculations.

All source scripts were read in the earlier checks, and their hashes remain unchanged. Exact radius-two snapshots have `_radius2_start` suffixes here. `RADIUS_TWO_INPUTS.json` records:

| Input from `nonlinear-evidence/` | SHA256 |
| --- | --- |
| `axial_cc.py` | `427e83efa1d55c836465c61c672e0cf4c0814420a59fc64430e2b80e6aae9528` |
| `axial_mixed_kinetic.py` | `8d7d288bc5aa66a381c6d9aecd734f2612ca4be4723cf27e1749bac98a24692f` |
| `axial_cubic_momentum.py` | `6087d885109dc37e0f0ddd5f3b760fc209b86407228a2bdf927e301a2a5c9f21` |
| `axial_constraint_mixing.py` | `af7cb28e5d175138d2176e8214f70066c3ae4cf6e0cad1158f1c123e677cf647` |
| `axial_r2_constraint_mixing_system.json` | `013ff43a3b96f9c8dd669d713936b751cbef43168699948bba7c55cb2413acd1` |
| `axial_r2_constraint_mixing_rational.json` | `dfb2ee4a99dac69fed6133004f6512bbb82e9c276bf985acc476448ead7c19f6` |

The strict original radius-two system was checked. The parent's separately generated relaxed-system files were not run or relied upon. Relaxation follows directly from the independently verified witness's support. The parent's result was disclosed before dispatch, so this is mathematical and implementation independence, not blind review.

## Domain and complete enumerated basis

Work on the axial diagonal restriction with A,B,C and momenta P_A,P_B,P_C; canonical pairing, fixed C1,T2,G1, and field-degree definitions are those in `REPORT.md`. Support is physical lattice radius two. Vertex-anchored diagonal slots have offsets {-2,-1,0,1,2}; edge-anchored diagonal slots have offsets {-1,0,1,2} from the edge's left endpoint. All coefficients are real and freely independent, without cubic, axial-reflection, or transverse-exchange reduction.

| Unknown family | Explicit basis | Columns |
| --- | --- | ---: |
| V2 | Every unordered pair of the 15 vertex h slots | 120 |
| T3 | Each of those h slots times every unordered pair of 15 vertex P slots | 1,800 |
| G2 | Every hP pair from the 12 edge-near h and 12 edge-near P slots | 144 |
| F1 | Each edge-near h slot times every antisymmetric pair of its four lapse sites | 72 |
| U0 | Four nearby shift edges times five vertex-near lapse sites | 20 |
| V0 | Every antisymmetric pair among five nearby shift edges | 10 |
| G3(P³) | Every unordered triple of the 12 edge-near momentum slots | 364 |
| Z1 | Each of 15 vertex-near momentum slots times every antisymmetric pair of five lapse sites | 150 |
| W1 | Each of 12 edge-near momentum slots, five shift edges, and four lapse sites | 240 |

The independently assembled bracket equations are

`CC2: {C1,T3}+{T3,C1}+{V2,T2}+{T2,V2}=G2[F0]+G1[F1]+C1[Z1]`,

`GC1: {G1,V2}+{G2,C1}=C1[U0]`,

`GG1: {G1[X],G2[Y]}+{G2[X],G1[Y]}=G1[V0]`,

`GC2_P2: {G1,T3}+{G2,T2}+{G3(P³),C1}=T2[U0]+G1[W1]`.

Every prescribed uniform-potential and continuum-moment equation in the strict payload was also independently reconstructed. The cubic kinetic polynomial was again obtained by differentiating the determinant-normalized smooth Hamiltonian, not by calling the author's normalization function. Repeated momentum factors in G3 are differentiated individually, giving their exact multiplicities.

These are necessary equations, not the full degree-two closure problem. No higher-order unknown omitted from these equations can contribute to these field degrees within the stated polynomial expansion. Configuration-space hhP terms in G3 contribute h² in GC and do not replace the P³ terms explicitly included here. The omitted-coordinate argument still holds because each bracket has C1,T2,or G1 as a fixed factor with vanishing omitted-coordinate derivatives on axial data. It does not license dropping nonlinear-versus-nonlinear brackets at later orders.

## Materially independent implementation and anti-alias proof

`check_radius_two.py` builds full globally summed polynomials on a 13-site periodic chain. The reusable independent polynomial helpers explicitly differentiate each finite functional at each canonical site and sum the products of those gradients. They do not use the author's relative-slot alignment or infinite-lattice bracket assembly. No parent assembly function is imported or executed.

Only after independently constructing every column does the script read the frozen matrix. Each residual monomial has a unique labelled N or X anchor; after forming the bracket, the monomial is translated to put that anchor at zero. The script compares every exact coefficient and right-hand side, including zeros and all moment constraints. No fields or smearings are sampled, and no numerical tolerance is used.

For radius two, the maximum integer slot-position diameter of any complete residual monomial is at most five:

- In `{C1,T3}`, the C1 lapse is within one site of the differentiated T3 momentum, itself within two sites of the T3 anchor; the surviving T3 slots are within two sites of that anchor. The farthest possible separation is five.
- In `{G1,V2}` or `{G1,T3}`, X lies at the differentiated h slot or one site to its left; other slots are at most two sites from the density anchor. The same bound is five.
- The other bracket terms and substitutions have diameter at most four. In particular, G3 momentum slots lie in [-1,2], and the C1 lapse produced by differentiation lies in [-2,3], with surviving momentum slots still in [-1,2], giving diameter at most four.

Thus every relative separation from the unique anchor lies in [-5,5]. Since 13>2*5, reduction modulo 13 is injective on these separations. A monomial's full translation orbit has exactly 13 elements because its distinguished smearing occurs once. Dividing the accumulated orbit coefficient by 13 therefore reproduces the infinite-lattice coefficient, including wrapped stencils. Uniform-potential translation quotients and smooth moments are computed directly, without this division.

This proves the finite-torus coefficient comparison lifts locally. The maximum diameter actually present in the fully matching serialized residual table was five, consistent with the a priori bound.

## Exact contradiction and its normalization content

The independently rebuilt table matches all 2,920 columns and 3,767 serialized rows. Recombining the supplied witness against this independent table gives:

| Witness family | Rows used |
| --- | ---: |
| CC2 | 488 |
| GC1 | 24 |
| GC2_P2 | 238 |
| continuum_G2_dh(1,1) | 1 |
| continuum_G2_dp(1,1) | 1 |
| Total | 752 |

Every combined unknown coefficient is exactly zero. The dh normalization has witness weight -1 and right-hand side +1. The dp normalization has weight +1 and right-hand side 0. Their total right-hand side is -1.

In particular, the witness uses no GG1, uniform V2, continuum T3, F1 moment, U0 moment, G2 zeroth moment, G3(P³) continuum moment, Z1 moment, or W1 moment equation. Removing any or all of those rows leaves the same exact witness valid. No inference from an author-only relaxed solve is required.

Let c_BB(a,b) multiply `X_x B_(x+a) P_B(x+b)` in G2, with a,b in {-1,0,1,2}. Its continuum moments are

`m_h = sum_(a,b)(a-1/2)c_BB(a,b)=1`,

`m_P = sum_(a,b)(b-1/2)c_BB(a,b)=0`.

The ordinary bracket rows in the verified witness combine to the negative of

`m_P-m_h = sum_(a,b)(b-a)c_BB(a,b)`

and have zero right-hand side. Therefore those rows force `m_P-m_h=0`, whereas the two continuum equations demand `m_P-m_h=-1`.

`check_radius_two_projection.py` separately reconstructs this projection from the preserved independent witness arrays: precisely the 12 off-diagonal (a!=b) c_BB coefficients survive, with weights b-a in {-3,-2,-1,1,2,3}; every other coefficient cancels. This identifies a useful Laurent-polynomial target for further work, but does not prove that relation at arbitrary support.

For provenance precision, the radius-one full-mixing certificate also uses these transverse (1,1) moments. The radius-one momentum-linear and P³-only certificates use the longitudinal (0,0) pair. An earlier sentence in `EXTENSION_REPORT.md` conflated those pairs; it has been corrected by inspecting the independently preserved witness rows. The verified numerical contradictions were unchanged.

## Extension to nonzero alpha and K

This parameter extension is established for the same necessary equations and support, rather than left as a conjecture. Let barred generators and coefficients denote the alpha=1,K=4 normalization. For arbitrary nonzero real alpha,K, the fixed pieces are

`C1=(K/4) C1bar`, `T2=(1/alpha) T2bar`, `F0=(K/(4alpha)) F0bar`,

and G1 is unchanged. Define the barred unknown coefficients by

| Family | Barred coefficient in terms of the original coefficient |
| --- | --- |
| V2 | `(4/K)V2` |
| T3 | `alpha T3` |
| G2 | `G2` |
| F1 | `(4alpha/K)F1` |
| U0,V0 | unchanged |
| G3(P³) | `(alpha K/4)G3(P³)` |
| Z1,W1 | `alpha Z1`, `alpha W1` |

Substitution and bilinearity of the fixed canonical bracket give the residual identities

`CC2_original = (K/(4alpha)) CC2_barred`,

`GC1_original = (K/4) GC1_barred`,

`GC2_P2_original = (1/alpha) GC2_P2_barred`,

`GG1_original = GG1_barred`.

Every map factor is real and nonzero for nonzero alpha,K; no square root or positivity assumption is needed. This is a coefficient reparametrization of the tested necessary system, not a claim to have found a canonical transformation of an entire nonlinear theory.

The G2 moment equations are unchanged. The supplied uniform V2 target scales as K, the cubic kinetic target as 1/alpha, and the F1 target as K/(4alpha), so their normalizations also transform correctly. Homogeneous zero-moment equations remain homogeneous under nonzero column rescaling. The certificate already avoids those other normalization rows.

Equivalently, `A_original=R A_barred D` and `b_original=R b_barred` for invertible diagonal row and column scales. Multiplying the normalized witness weights by R^-1 gives a general-parameter witness with the same right-hand side -1. The projection script verifies symbolically all 15 potentially nonzero bracket-family/column-family scaling factors; the two G2 normalization rows have unit scales.

Therefore this bounded inconsistency holds for every nonzero real alpha,K with the corresponding supplied DeWitt kinetic form, fixed linear curvature term, and positive-Lie-action G2 moments. Positive alpha,K are the original physical-parameter domain; allowing other signs here is only an algebraic extension. K=0 is not covered by the invertible map; alpha=0 does not define the supplied inverse kinetic form. Neither special case is excluded by this result.

## Commands, resources, and limits

Before work, the original runtime file and stop sentinel were checked. The deadline remained `2026-09-30T22:41:00.557005Z`, and no stop sentinel was present. The main script repeats deadline/stop checks during assembly. Pricing before execution was one sparse single-thread process, an estimate below 512 MB and below two minutes; peak memory was not measured.

Executed from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_radius_two.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/radius_two_results.txt 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/check_radius_two_projection.py > .claude/science/physics-loops/toe-gravity-law-24h-20260929/independent-axial-check/radius_two_projection_results.txt 2>&1
```

Both exited 0. Full assembly/comparison/certificate recombination took 15.35 seconds; the separate projection and symbolic scaling check took less than one second. No rank claim was inferred from the author's elimination, and no new Gaussian elimination was needed for the contradiction. Exact independent witness rows are preserved in `radius_two_independent_certificate.json`; hashes are in `MANIFEST.json`.

No all-radius, universal-locality, 3D-sufficiency, nonlinear-Jacobi, matter-coupling, alternative-kinetic-stencil, altered-phase-space, singular-trace-branch, or record-formation result is supplied. Finite-radius evidence motivates the displayed Laurent target but does not prove it. No parent script, science source, root state, Git index, commit, push, or external service was mutated. Writes stayed in the assigned independent-check directory.
