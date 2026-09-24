# Blind PRE: exact initial field response with live births

Independent derivation and bounded primitive control, 2026-09-24. This report was completed before release of the root candidate. It studies the supplied **full compensated common rotor generator**, with the original resolved or coherent formation instruments. It does not study an autonomous apparatus, replace the common slow Hamiltonian by a fast energy operator, or apply an audit verdict.

The supported conclusion is an exact initial response, including a matter-dependent second Wilson derivative. On a regular graph of degree `z`, the first-birth contribution to that derivative is `-4 kappa z(z-1) w'(0)`. This is a derivative at the specified initial sector, not an evolution equation valid after the sector changes. In particular it does not, by itself, establish finite-duration photon propagation or an exponential damping law.

## 1. Frozen sources, conventions, and domain

Both primary arguments were read completely at main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` in `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/campaign-working`:

| Source under `docs/` | SHA256 |
|---|---|
| `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b` |
| `LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a` |

The primitive convention in section 2 of `EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `54559e6c6a6871aad27ac5cf899f7f30277ea4777f62b0235134ac05cb90af6a`, was read only as the necessary transport/formation definition. No energy theorem from that note is imported. A preliminary definition search inspected the first 130 lines of `GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md`, SHA256 `9e13c659e9a418e9e77e619a3cbd82d371f8219003a92e49fb2cc9ac5f87d6c7`; no result from that search is used. Both are pinned at the same main revision so this incidental access is explicit.

`SOURCE_PINS.json` binds exact git bytes and local snapshots, including the repository AGENTS pointer and current `SCIENCE_WORKFLOW.md`. The unchanged standing execution instructions are separately bound by `INSTRUCTION_PIN.json`, at revision `eb1f1ca8338848cf2046582e13aef372d8540937`, SHA256 `b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7`. Already-read instructions were reused after identity verification. No root candidate, checkpoint, or other active independent packet was read. No author builder was imported, and no parent numerical runner was rerun.

Let `G=(A union B, E)` be a fixed finite simple bipartite graph. Every edge is oriented **A to B**. Write `partial` for the incidence matrix, with `+1` at A and `-1` at B. Physical words obey

    partial E = q - 1_A,       q_x in {0,+1,-1}.

Work in P, where every A site is occupied. The initial matter word is `q0=1_A`, with every B empty. The initial field density `rho` is arbitrary on the divergence-free integer-field subspace, subject to the observable-domain qualification below. A field word `|E>` can have any finite integer magnitude; there is no small-field restriction.

Use `T_s|E>=|E+s>`. For an integer circulation `ell` with `partial ell=0`, define the Wilson operator `W_ell=T_ell`. In the Fourier convention `psi(theta)=sum_E psi_E exp(i E.theta)`, `T_s` multiplies by `exp(i s.theta)`, and `E_e=-i partial_theta_e`. Norms and dot products on edge vectors use the ordinary Euclidean metric.

The supplied common generator and full electric operator are

    L rho = -i[h,rho] + kappa sum_j (B_j rho B_j* - {B_j* B_j,rho}/2),
    h = K D + delta H4^C,
    D(q,E) = sum_(a in A, b~a, q_b=0) E_ab (E_ab - q_a),
    H4^C = -2 sum_(unordered a<c, dist(a,c)=2) S_ac* S_ac,
    S_ac = F_c F_a P.

Here `K,delta,kappa>0` are fixed supplied couplings. `F_a` moves the charge at a to an empty B neighbor and shifts that edge by `-q_a`. The primitive `j_(a,b),sigma` requires a and b empty, creates `(q_a,q_b)=(sigma,-sigma)`, and shifts the edge by `+sigma`. Thus

    B_(a,b),sigma = P j_(a,b),sigma F_a P,
    B_(a,b),coherent = B_(a,b),+ + B_(a,b),-.

There is no extra factor `1/sqrt(2)` in the coherent mark. All rotor path weights in these primitive steps equal one. The full magnetic operator, jumps, and their adjoints are finite sums of field translations with matter-dependent coefficients. Therefore every physical Wilson translation commutes with **all** of them on the full P space, including after births:

    [W_ell,H4^C]=[W_ell,B_j]=[W_ell,B_j*]=0.             (1)

This structural identity, rather than a field-only approximation to the postbirth Hamiltonian, is essential below.

On the initial matter sector, Gauss gives

    D0 = sum_e E_e^2,
    h0 = K sum_e E_e^2 - 2 delta sum_p(W_p+W_p*) + delta c_G,
    c_G = -2 sum_(a<c,r_ac>0) (z_a z_c-r_ac),
    r_ac = |N(a) intersection N(c)|.                    (2)

Here p runs once over each simple unoriented four-cycle with either orientation chosen. The source pair-count proof applies to all such cycles, not just geometrically selected faces. The scalar `delta c_G` cancels from every response below.

**Domain qualification.** All derivative formulas are exact on finite-support physical density matrices, hence on every fixed divergence-free electric word and every finite coherent superposition. Let `Q=1+sum_e E_e^2`. The Wilson derivatives through order two and electric moment identities below extend to states with `Tr(Q rho)<infinity` as quadratic-form expectation identities. One justification is as follows. Every bounded interaction/jump is a finite sum of finite translations and hence is bounded on the Hilbert space with norm `||Q^(1/2) psi||`. The diagonal `D` commutes with Q. Its free unitary acts isometrically on the associated weighted trace space; adding the bounded magnetic and jump terms gives a strongly continuous semigroup there by its convergent bounded-perturbation expansion. The first and second dual Wilson expressions have degree at most one and two in E, respectively, and are Q-bounded forms. Finite-support cutoff states converge in that weighted trace norm. The integrated first- and second-derivative identities therefore pass to the limit, with continuous integrands. This also justifies the moment identities. A trace-norm density derivative additionally requires the generator domain; finite support, or the sufficient condition `Tr(Q^2 rho)<infinity`, supplies it here.

For an arbitrary normalizable state with no finite electric moment, the bounded jump map and exact no-first-birth law below still hold, but an electric mean, covariance, or Wilson time derivative need not exist. Nothing here provides a Taylor remainder uniform over states whose field moments diverge, growing graphs, or a simultaneous microscopic-spin/time limit. We work in the already supplied common rotor theory.

## 2. Initial source and exact no-first-birth law

Fix a birth edge `(a,b)`. The old A-plus record must first hop to a distinct neighbor `d != b`. The resulting field kick is

    s_(a;b,d),sigma = sigma e_ab - e_ad.                (3)

For `sigma=+`, A remains all plus, B site b has charge -1, and d has +1. For `sigma=-`, A site a has -1, b and d both have +1, and other A sites remain plus. These are the actual new matter words, not projected records.

For a fixed original edge/mark, different old destinations d have orthogonal matter words. The two signs within a coherent edge mark also have orthogonal matter words. After tracing matter, therefore, the initial source has the same field map for resolved and coherent instruments:

    J_F(rho) = sum_a sum_(b,d in N(a), b!=d) sum_(sigma=+/-1)
                       T_(sigma e_ab-e_ad) rho T_(sigma e_ab-e_ad)*. (4)

This equality concerns the **reduced field source at the initial sector**. The coherent joint source contains cross terms between different signs. It is not the resolved mixture, and those coherences are retained by the full later generator.

At the initial sector,

    Gamma0 = sum_j B_j* B_j = R_G I,
    R_G = 2 sum_(a in A) z_a(z_a-1),
    lambda0 = kappa R_G.                               (5)

One way to see the absence of interference in this Gram operator is to use the orthogonal matter destinations above. Equivalently, at the initial record number and total charge there is only one P matter word, and the reverse legal path is unique within each marked output. The resolved edge/sign hazard is `kappa(z_a-1)`; a coherent edge hazard is `2 kappa(z_a-1)`.

Thus, wherever a density derivative is defined, the exact initial reduced-field derivative is

    rho_F'(0) = -i[h0,rho]
                + kappa sum_(a;b!=d;sigma)
                    (T_s rho T_s* - rho).              (6)

The loss and no-first-birth statement is stronger than an initial expansion. Since h preserves record number and total charge, the no-first evolution stays in the same unique initial matter sector. Since `Gamma0` is scalar, for every `t>=0` the exact unnormalized no-first component is

    rho_nf(t) = exp(-lambda0 t) |q0><q0|
                  tensor exp(-i h0 t) rho exp(+i h0 t),
    P(no first birth before t) = exp(-lambda0 t).        (7)

This does not say that the subsequent birth process is a homogeneous Poisson process. Later hazards depend on the changed matter and field state. If `sigma0(t)` denotes the normalized density in (7), positivity of the trajectory decomposition does give the finite-graph estimate

    ||rho_full(t)-sigma0(t)||_1 <= 2(1-exp(-lambda0 t)). (8)

The same holds after any partial trace. It controls a global short no-birth window, not an extensive-time or volume-uniform response. In particular `lambda0` grows with the number of A sites at fixed degree.

## 3. Angular response, electric moments, and transverse projection

For `u=theta-theta'`, the jump part in (6) multiplies the field density kernel by

    chi(u) = kappa sum_a sum_(b!=d in N(a))
                   [exp(i(u_ab-u_ad)) + exp(-i(u_ab+u_ad)) - 2]
           = kappa sum_a sum_(b!=d) [2 cos(u_ab) exp(-i u_ad)-2]. (9)

Each summand arises from an actual path in (3). Consequently `chi(0)=0` and `Re chi(u)<=0`. The initial jump source leaves the angular diagonal probability unchanged and changes its off-diagonal kernel. More generally, (1) shows that the full jump dissipator annihilates every bounded gauge-invariant angular multiplication observable in the dual picture, at every full state. This is not a claim that the complete angular probability is stationary: the electric Hamiltonian still acts.

The small-u coefficients of this *initial* jump kernel are

    chi(u) = i v.u - (1/2) u^T Q_jump u + O(|u|^3),
    v_e = -2 kappa(z_a-1),                 e=(a,b),
    (Q_jump)_ef = 4 kappa(z_a-1) delta_ef.               (10)

The cross terms from the two signs cancel. For each edge, it appears `z_a-1` times as the newly created edge and `z_a-1` times as the old hop edge, with two signs. These counts explain the covariance coefficient. Equation (10) is not a Gaussian-noise limit or a time-homogeneous random-walk model after births.

Let `m_e=<E_e>_rho` and let `C_ef` be the initial centered electric covariance. Write

    F_e = i[h0,E_e]
        = 2 i delta sum_p p_e(W_p-W_p*)
        = -4 delta sum_p p_e sin(p.theta).              (11)

Then

    m_e'(0) = <F_e> + v_e,                              (12)

    C_ef'(0) = (1/2)<{E_e-m_e,F_f}>
               + (1/2)<{E_f-m_f,F_e}>
               + (Q_jump)_ef.                          (13)

The anticommutators make the reality and symmetry explicit; the identity follows from the Hamiltonian derivation rule and the first two kick moments. For a deterministic electric word the magnetic expectations and covariance cross terms vanish at zero, so `m'=v`, `C'=Q_jump`. These are unconditional first derivatives, not a statement about a particular conditioned jump.

The drift v is longitudinal even for irregular graphs: choose the vertex scalar `phi_a=-2 kappa(z_a-1)` on A and `phi_b=0` on B, and then `v=partial^T phi`. If `P_T` is the orthogonal projection onto `ker partial`,

    P_T v=0,             Q_T = P_T Q_jump P_T.          (14)

The magnetic force in (11) is itself transverse since every p is a circulation. On a regular graph of degree z,

    Q_T = 4 kappa(z-1) P_T.                             (15)

Thus a unit transverse direction receives initial jump variance rate `4 kappa(z-1)` although its jump mean drift is zero. For a circulation ell, the jump contribution to `Var(ell.E)'` is `4 kappa(z-1)||ell||^2`. A four-edge plaquette has norm squared four.

The longitudinal mean is consistent with the new matter, rather than a violation of Gauss. At A site a its divergence is `-2 kappa z_a(z_a-1)`, the mean change caused by the minus births flipping that A charge. At B site b it is `+2 kappa sum_(a~b)(z_a-1)`, the old-record inflow. Total charge is conserved.

## 4. First two exact Wilson derivatives under the full generator

Let `w_ell(t)=Tr(rho_full(t) W_ell)`. Define the **full** multiplication operator

    d_ell(q,E) = D(q,E+ell)-D(q,E)
      = sum_(a,b~a,q_b=0) [2 ell_ab E_ab + ell_ab^2 - q_a ell_ab]. (16)

Equation (1) and `[D,W_ell]=W_ell d_ell` give the full operator identity

    L* W_ell = i K W_ell d_ell.                         (17)

On the initial sector, `sum_e ell_e=sum_a (partial ell)_a=0`, so

    A_ell(E) := d_ell(q0,E) = 2 ell.E + ||ell||^2,
    w_ell'(0) = i K <W_ell A_ell>_rho.                 (18)

There is no direct dissipative term at first order. Applying the **same full generator** once more yields

    (L*)^2 W_ell = -K^2 W_ell d_ell^2
                   -K W_ell[delta H4^C,d_ell]
                   +i kappa K W_ell D_B* d_ell,
    D_B* X = sum_j(B_j* X B_j - {B_j*B_j,X}/2).         (19)

Both d factors in this formula are the matter-dependent ones in (16). The initial Hamiltonian contribution is

    -K^2 <W_ell A_ell^2>
    -4 K delta sum_p (ell.p)<W_ell(W_p-W_p*)>.           (20)

To derive it, H4 preserves record number and charge, so on an initial word it remains in the unique initial matter sector and the exact restriction (2) applies. Then `[W_p,A_ell]=-2(ell.p)W_p`. The full postbirth magnetic dynamics has not been discarded; its commutation with W in (1) is why it does not supply an extra second-order term here.

### The postbirth electric calculation

For the birth `(a;b,d),sigma`, let `R(b,d)` be all edges incident to either B vertex b or d. The field kicks in (3) lie entirely on these deleted edges. On an initial divergence-free field E, the resulting electric energies are

    D(q_+,E+s_+) = sum_(e not in R(b,d)) E_e^2,
    D(q_-,E+s_-) = sum_(e not in R(b,d)) E_e^2
                      +2 sum_(c~a,c not in {b,d}) E_ac. (21)

For the first formula, the linear sum on the remaining edges vanishes: the complete A sum vanishes, and each removed B star separately has zero initial divergence. For the second, the charge at a is now -1 rather than +1, which reverses that remaining star's linear term. Both facts use the actual matter and the initial Gauss constraint.

Taking the increment along ell in (21), and using the zero divergence of ell, gives

    d_ell(q_+,E+s_+) = A_ell(E)
                   - sum_(e in R(b,d)) (2 ell_e E_e+ell_e^2),
    d_ell(q_-,E+s_-) = A_ell(E)
                   - sum_(e in R(b,d)) (2 ell_e E_e+ell_e^2)
                   - 2(ell_ab+ell_ad).                 (22)

The last term is an explicit contribution of the changed A matter. It must be retained branch by branch. In the sum over the complete original marks and ordered destinations, it cancels, because

    sum_a sum_(b!=d in N(a)) (ell_ab+ell_ad)
      = 2 sum_a(z_a-1) sum_(b~a) ell_ab = 0.            (23)

For fixed B vertex b, the number of ordered pairs in which b occurs as either the new or old destination is

    2 nu_b,       nu_b = sum_(a~b)(z_a-1).

The two signs in (22) supply the other factor of two. The exact initial restriction is consequently

    (D_B* d_ell)|initial
       = -4 sum_(e=(c,b)) nu_b (2 ell_e E_e+ell_e^2).   (24)

The loss term is already included: it subtracts `R_G A_ell`. The coherent mark gives the same (24), since d is matter-diagonal and its within-edge distinct matter outputs have no cross matrix elements. That observation does not replace the coherent state by a resolved state at later times.

Combining (18), (20), and (24) gives the initial derivative on any finite simple bipartite graph:

    w_ell''(0) = -K^2 <W_ell A_ell^2>
      -4 K delta sum_p (ell.p)<W_ell(W_p-W_p*)>
      -4 i kappa K <W_ell sum_(e=(c,b))
                                  nu_b(2 ell_e E_e+ell_e^2)>. (25)

On a graph regular of degree z, `nu_b=z(z-1)` and the last line becomes `-gamma w_ell'(0)`, where

    gamma = 4 kappa z(z-1),
    w_ell''(0) = -K^2 <W_ell A_ell^2>
      -4 K delta sum_p (ell.p)<W_ell(W_p-W_p*)>
      -gamma w_ell'(0).                                (26)

There is no `kappa^2` term at this order: `D_B* W_ell=0` exactly, so the second application contains the one dissipator acting on the electric commutator. Equation (26) holds for the complete original resolved or coherent instruments, not for an arbitrary reweighted instrument.

Two mistakes would be consequential. Freezing the postbirth electric operator to `sum_e E_e^2` gives only a kick drift proportional to `ell.v`, which is zero, and misses the entire last term of (25). Freezing only the A charge at +1 while correctly deleting occupied B stars also gives incorrect branch values in (22); its error happens to cancel in the complete initial Wilson sum (23). An aggregate second-derivative test alone would therefore fail to detect that second mistake. The independent control tests the individual branches as well.

## 5. Cube, a simple degree-six torus, and a nonzero test state

The cubic graph with vertices `{0,1}^3` has degree three, A and B of size four, and twelve edges. The separate degree-six example used here is the nearest-neighbor periodic `6 x 6 x 6` lattice, with checkerboard A/B. It is simple and bipartite and has 216 vertices and 648 edges. Its simple four-cycles are precisely the 648 elementary plaquettes. Choosing an even torus of side four instead would introduce additional straight winding four-cycles; silently keeping only elementary plaquettes would change (2). Side six avoids that ambiguity.

| Exact initial quantity | Cube | Periodic `6^3` torus |
|---|---:|---:|
| Degree z | 3 | 6 |
| Number of A sites | 4 | 108 |
| Simple unoriented four-cycles | 6 | 648 |
| `c_G` | -84 | -66744 |
| `lambda0/kappa` | 48 | 6480 |
| `v_e/kappa`, A-to-B orientation | -4 | -10 |
| `(Q_jump)_ee/kappa` | 8 | 20 |
| Unit transverse jump variance rate divided by kappa | 8 | 20 |
| Plaquette `Var(ell.E)'` jump part divided by kappa | 32 | 80 |
| `gamma/kappa` in (26) | 24 | 120 |

The large torus scalar is merely a path count: there are 324 A pairs with one common B neighbor and 648 pairs with two, so `c_G=-2[324(36-1)+648(36-2)]`. It has no effect on the observables above.

For a plaquette ell, take the legitimate initial field state

    psi = (|0> + i|ell>)/sqrt(2).

Then the exact derivatives from the full generator are

    w(0) = -i/2,
    w'(0) = 2 K,
    w''(0) = 16 K delta - 2 K gamma + 8 i K^2.         (27)

At `K=delta=kappa=1`, (27) is `-32+8i` on the cube and `-224+8i` on the degree-six torus; the Hamiltonian-only second derivative is `16+8i` in both. This tests a nonzero birth correction. In contrast, for a deterministic electric word, a nontrivial Wilson loop has `w'(0)=0`. For a plaquette, its Hamiltonian second derivative is `16 K delta`, so that particular initial expectation would not reveal the matter-induced term at second order. The full word-level dual expression still contains it.

## 6. What these facts do and do not establish about propagation

There are two rigorous finite-duration statements here: the exact no-first component (7), and its finite-graph trace-distance estimate (8). These may support a separate response calculation in a time interval for which the no-birth probability is controlled. Neither has a uniform thermodynamic window at the supplied fixed birth intensity; no infinite-volume conclusion is inferred from that observation.

One can also identify the *formal quadratic comparison* associated with the no-birth Hamiltonian. Expanding its plaquette cosines around a weak-angle reference gives

    h_quad = K ||E||^2 + 2 delta ||C theta||^2 + scalar,
    theta_dot = 2 K E,
    E_dot = -4 delta C^T C theta,
    theta_double_dot = -8 K delta C^T C theta.          (28)

Here C is the plaquette incidence matrix. On an ordinary periodic cubic lattice, after the harmless edge-orientation sign change to coordinate orientation, its transverse Fourier eigenvalue is `4 sum_mu sin^2(k_mu/2)`. Thus this supplied quadratic comparison has

    omega(k)^2 = 32 K delta sum_mu sin^2(k_mu/2),

and a formal small-k speed `sqrt(8 K delta)` in lattice units. This is the algebra of a linearized reference Hamiltonian, conditional on a controlled weak-angle/semiclassical or appropriate quantum linear-response regime. A finite side-six torus itself does not provide a small-k continuum limit. No such reference-state or approximation theorem is established here.

The exact initial identities add three specific facts to that comparison: live births do not directly change Wilson angles at first order; they inject transverse electric variance immediately; and their change to the electric commutator produces the last term of (25). They do not close the hierarchy after births. In particular h is then still `K D(q,E)+delta H4^C`, its electric response depends on matter, the Hamiltonian-only term in (26) contains further field correlations, and later resolved/coherent distinctions may matter. Replacing (26) by `w''+gamma w'+omega^2 w=0` for finite times is unsupported. Neither a photon lifetime nor the absence of propagation follows from these derivatives.

A finite-duration photon statement would need, among other things, a specified stationary or controlled evolving reference state; an operationally defined transverse response or two-point function; estimates on the matter/field correlation hierarchy and the error of any linearization for the requested time; and, if intended, a compatible volume/long-wavelength limit. The initial all-A-plus, B-empty preparation is not asserted to be a stationary vacuum of the full live-birth generator. No native-law selection, empirical identification, or reservoir/apparatus conclusion is made.

## 7. Independent primitive control and evidence limits

`primitive_initial_response.py` is a new standard-library sparse-word implementation. It does not import a parent or root builder. It constructs the cube and the simple periodic side-six graph directly from vertices and nearest neighbors; implements legal F, F*, j, j*, B, B* by charge and integer-field changes; evaluates D from actual charges and occupied B sites; and accumulates amplitudes as exact integers. Real and imaginary derivative coefficients are stored separately; the final state expectations use exact rational arithmetic.

The primitive `-2 sum S_ac* S_ac` action reconstructs the full initial magnetic translation kernel. A separately enumerated four-cycle expression agrees coefficient by coefficient, including the scalar. The control then checks every initial birth path, Gauss, the initial loss, the reduced-field kick counts, electric drift/covariance, an exact angular-kernel value at `u=(pi/2)ell`, nonzero postbirth jump commutations with W, and full first/second dual Wilson actions on three finite field words. The second derivative is computed using B, the changed matter in D, and B*, rather than inserting gamma. It agrees for resolved and coherent marks. The expectation (27) is evaluated from those word actions.

At a fixed initial birth edge, the squared Hilbert-Schmidt difference between coherent and resolved **joint** sources is 8 on the cube and 50 on the torus; the reduced-field source difference is zero. This is a direct check that initial field equality has not been misreported as joint instrument equality. Mutation controls find the false field-only D has zero Wilson birth correction, and an individual minus-birth charge-freezing error changes a checked `d_ell` from 0 to 2 on both graphs. There are eight such detected branch discrepancies for the chosen cube loop and 32 for the chosen torus loop.

The first exact run passed. A subsequent coverage review found that its auxiliary commutation check applied the just-used edge after it had become occupied, so that one check was vacuous. The final version instead chooses a different channel with a nonzero second-birth source and asserts nonzero equality; it checks four such born states on the cube and ten on the torus. The initial successful code/results/logs and this coverage finding are preserved under `first_control_attempt/`. The full initial derivative calculation was already nonvacuous, and its scientific values did not change. No failed execution or counterexample has been discarded.

The final genuine run completed successfully in 4.499080624897033 seconds, with empty stderr. `PRIMITIVE_EXECUTION.json` binds the command, code hash and complete logs; `PRIMITIVE_STDOUT.log` is byte-identical to `PRIMITIVE_RESULTS.json`. The final code SHA256 is `c82c5ad022127307a0d818f6f7f5db3eca1ac9beb3ee2e36f701b31d1086408c`; the result/stdout SHA256 is `ef9ec7753fb02cbf65dc3a8660a34138cc31f859fa820166990fd620ebb50af0`. The complete output was inspected; it was not inferred from a PASS label.

These finite-word computations corroborate the independent analytic identities and catch specified incorrect substitutions. They do not numerically construct the full infinite rotor semigroup, certify a uniform time remainder, establish arbitrary-graph identities without the proof, or simulate propagating photons. The exact source-byte and evidence correspondence check is recorded separately. The immutable PRE seal binds this report and all its source, code, data, execution, and preserved-attempt evidence. Work stops at that seal pending an explicit source release.
