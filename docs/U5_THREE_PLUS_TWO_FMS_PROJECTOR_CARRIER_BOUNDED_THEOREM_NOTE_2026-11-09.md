# U(5) Three-Plus-Two FMS Projector Calculus and Native Stabilizer Carrier Bounded Theorem Note

**Date:** 2026-11-09
**Type:** bounded_theorem
**Primary runner:** [`scripts/frontier_u5_three_plus_two_fms_projector_carrier.py`](../scripts/frontier_u5_three_plus_two_fms_projector_carrier.py)
**Runner cache:** `logs/runner-cache/frontier_u5_three_plus_two_fms_projector_carrier.txt`
**Loop pack:** `.claude/science/physics-loops/u5-three-plus-two-fms-projector-carrier-20261109/HANDOFF.md`

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Self-contained operator-algebraic, variational, and representation-theoretic theorems establishing exact noncommuting Fröhlich-Morchio-Strocchi projector defect decompositions for SU(2), U(5), and Spin(10)/so(10), the exact joint stabilizer K_{U(5)} = S(U(3)xU(2)){+-I_5}, the nonvanishing fermion-even two-site determinant-square carrier on Lambda^5(C^10), the global su(5) quartic potential minimum on the 3+2 orbit, the 25x25 Higgs Gram matrix spectrum and unbroken-subalgebra projector, and the single-link vs. multi-copy FMS defect scaling, without claiming dynamical Floquet vacuum selection or a continuum infrared mass gap."
target_claim_id: null
target_blocker_text: "Establish exact noncommuting Fröhlich-Morchio-Strocchi projector defect identities across SU(2), U(5), and Spin(10)/so(10), prove the rank-three certification requirement, construct the fermion-even native carrier on Lambda^5(C^10) realizing S(U(3)xU(2)){+-I_5}, prove global 3+2 orbit selection for the quartic su(5) potential, diagonalize the joint Higgs Gram matrix on u(5), and establish single-link transport defect bounds alongside multi-copy coherent FMS defect scaling."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Derive the effective quartic coupling sign lambda_2 > 0 and multi-copy coherent state preparation directly from the coupled five-mode Floquet tick."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 0. Scope, Premise Provenance, and Obligation Graph

This note is self-contained on `main` and relies on no unlanded branch or external file. It proves eight algebraic, variational, and operator-theoretic results for gauge-invariant Fröhlich-Morchio-Strocchi (FMS) channel resolution, stabilizer realization, orbit selection, Gram-matrix spectral splitting, and multi-copy defect scaling in the $SU(2)$, $U(5)$, and $\mathrm{Spin}(10)/\mathfrak{so}(10)$ three-plus-two settings:

1. **Theorem 1 (Noncommuting $SU(2)$ Adjoint Projector Defect Identity and State-$L^2$ Equality):** For any unital $*$-algebra $\mathcal{A}$, any self-adjoint triple $\Phi = (\Phi^1, \Phi^2, \Phi^3) \in (\mathcal{A}_{\mathrm{sa}})^3$, and any scale $r > 0$, the local projectors $P_\pm = \frac{1}{2}(I_{\mathcal{A}} \otimes I_2 \pm r^{-1}\sum_{a=1}^3 \Phi^a \otimes \sigma_a)$ satisfy an exact internal Hilbert-Schmidt equality separating the radial orbit defect from the noncommuting commutator defect with zero cross term. Local gauge covariance implies that the four projected two-end strings $\mathcal{S}_{s,s'}(X,Y) = \Psi_X^* P_s(\Phi_X)\mathcal{U}_{XY}P_{s'}(\Phi_Y)\Psi_Y$ are strictly gauge-invariant for any bi-covariant transporter $\mathcal{U}_{XY}$ (without assuming $\mathcal{U}_{XY}$ is unitary) and sum to $\Psi_X^* \mathcal{U}_{XY} \Psi_Y$.
2. **Theorem 2 ($U(5)$ Three-Plus-Two Adjoint Projector Calculus, Fermionic Bilinear Identity, and Rank-Separation Certification):** For $A = A^* \in \mathcal{A} \otimes M_5(\mathbb{C})$ and distinct real target eigenvalues $a \neq b$, the linear Lagrange projectors $P_3(A) = (A - b I_5)/(a - b)$ and $P_2(A) = (a I_5 - A)/(a - b)$ satisfy $P_3(A)^2 - P_3(A) = (A - a I_5)(A - b I_5)/(a - b)^2$ and $\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}} = (\operatorname{Tr}_{M_5}(A) - (3a + 2b)I_{\mathcal{A}})/(a - b)$. On the five-flavor canonical anticommutation relation (CAR) algebra $\Lambda(\mathbb{C}^5)$, the fundamental bilinear matrix $C_{ik} = c_i^\dagger c_k$ satisfies the exact noncommuting quadratic identity $C^2 = (6 - n)C$ on each $n$-fermion sector $\Lambda^n \mathbb{C}^5$, so $P_{\mathrm{CAR}} = (6 - n)^{-1}C$ ($1 \le n \le 5$) is an exact idempotent ($P_{\mathrm{CAR}}^2 = P_{\mathrm{CAR}}$) whose internal trace is $\frac{n}{6-n} I_{\Lambda^n\mathbb{C}^5}$ (non-integer at $n = 2$). Moreover, an explicit state witness on $A_{(4)} \oplus A_{(2)}$ shows that vanishing quadratic defect $P_3(A)^2 - P_3(A) = 0$ and vanishing mean trace defect $\omega(\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}}) = 0$ still allow zero weight on the rank-three stratum unless the trace-variance defect $\omega((\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}})^2)$ is also controlled.
3. **Theorem 3 (Orthogonal Real Six-Plus-Four Projectors and Complex-Structure Defect Factorization):** For any skew-adjoint operator $A = -A^* \in \mathcal{A} \otimes M_{10}(\mathbb{R})$ and real parameters $a, b \neq 0$ with $a^2 \neq b^2$, the real block projectors $Q_6(A) = (-A^2 - b^2 I_{10})/(a^2 - b^2)$ and $Q_4(A) = I_{10} - Q_6(A)$ commute identically with $A$, and the candidate complex structure $J_A = A(a^{-1}Q_6(A) + b^{-1}Q_4(A))$ satisfies the exact polynomial factorizations
   $$J_A^2 + I_{10} = \frac{(a - b)^2 A^2 + (a^2 - b^2)^2 I_{10}}{a^2 b^2}\,(Q_6(A)^2 - Q_6(A)), \qquad A - (a Q_6(A) + b Q_4(A))J_A = \frac{(a - b)^2}{ab}\,A\,(Q_6(A)^2 - Q_6(A)).$$
   In $\mathfrak{so}(10)$ ($\dim = 45$), the real projector $Q_6(A_0)$ alone has centralizer $\mathfrak{so}(6) \oplus \mathfrak{so}(4)$ of dimension $21$, whereas adjoining $J_{A_0}$ reduces the centralizer to $\mathfrak{u}(3) \oplus \mathfrak{u}(2)$ of dimension $13$.
4. **Theorem 4 (Joint Stabilizer of Adjoint and Determinant-Square Data in $U(5)$):** For $A_0 = a I_3 \oplus b I_2$ ($a \neq b$) and $0 \neq \zeta \in (\det \mathbb{C}^5)^{\otimes 2}$ carrying $g \cdot \zeta = (\det g)^2 \zeta$, the joint stabilizer in $U(5)$ is $K_{U(5)} = \{A \oplus B \in U(3)\times U(2) : (\det A \det B)^2 = 1\} = H\{\pm I_5\}$, where $H = S(U(3)\times U(2)) \cong (SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6$ has Lie algebra of dimension $12$. Because $-I_5$ acts trivially on every fermion-even operator, $K_{U(5)} = H\{\pm I_5\}$ is the minimal subgroup of $U(5)$ containing $H$ that can arise as the stabilizer of fermion-even composites.
5. **Theorem 5 (Native Fermion-Even Five-Mode Determinant-Square Carrier on $\Lambda^5 \mathbb{C}^{10}$):** On a single link $\ell = (x,y)$ with five matter CAR modes per site and the half-filled ten-mode rishon link register $\mathcal{H}_\ell = \Lambda^5 \mathbb{C}^{10}$ ($\dim \mathcal{H}_\ell = \binom{10}{5} = 252$) with link matrix entries $U_\ell^{ij} = r_{y,i} r_{x,j}^\dagger$, the five-rishon transfer operator $D_{xy} = (r_{y,1}\cdots r_{y,5})(r_{x,5}^\dagger\cdots r_{x,1}^\dagger)$ satisfies the exact determinant identity $U_\ell^{i_1,1}\cdots U_\ell^{i_5,5} = \operatorname{sgn}(i_1,\dots,i_5)D_{xy}$ and $\operatorname{Tr}_{\Lambda^5\mathbb{C}^{10}}(D_{xy}^\dagger D_{xy}) = 1$. Dressed with the five-fermion site creations $B_x = c_{x,1}^\dagger\cdots c_{x,5}^\dagger$ and $B_y = c_{y,1}^\dagger\cdots c_{y,5}^\dagger$, the composite $\mathcal{O}_{xy}^{(10)} = B_x D_{xy} B_y$ is nonzero ($\|\mathcal{O}_{xy}^{(10)}\|_{\mathrm{op}} = 1$), fermion-even ($20$ fermion letters), commutes with all $25$ local $\mathfrak{gl}(5)_y$ Gauss generators $[G_y^{ij}, \mathcal{O}_{xy}^{(10)}] = 0$, and satisfies $[G_x^{ij}, \mathcal{O}_{xy}^{(10)}] = 2\delta_{ij}\mathcal{O}_{xy}^{(10)}$ for all $1 \le i,j \le 5$, thereby realizing the exact representation $(\det g_x)^2 \otimes 1_y$ of $U(5)_x \times U(5)_y$.
6. **Theorem 6 (Global Quartic $\mathfrak{su}(5)$ Three-Plus-Two Orbit Selection via Cubic Discriminant):** Using an elementary derivative-free three-variable cubic discriminant identity $\Delta(u,v,w) = \frac{1}{2}r^6 - 27(uvw)^2 = (u-v)^2(v-w)^2(w-u)^2 \ge 0$, every traceless self-adjoint matrix $A \in \mathfrak{su}(5)_{\mathrm{sa}}$ with $\operatorname{Tr}(A^2) = s > 0$ satisfies the sharp fourth-moment bounds $\frac{7}{30}s^2 \le \operatorname{Tr}(A^4) \le \frac{13}{20}s^2$, with equality on the lower bound $\frac{7}{30}s^2$ if and only if $A$ lies in the three-plus-two unitary orbit of $\pm\sqrt{s/30}\operatorname{diag}(-2,-2,-2,3,3)$ and equality on the upper bound $\frac{13}{20}s^2$ if and only if $A$ lies in the four-plus-one unitary orbit of $\pm\sqrt{s/20}\operatorname{diag}(1,1,1,1,-4)$. Consequently, for all $\mu^2 > 0$, $\lambda_2 > 0$, and $30\lambda_1 + 7\lambda_2 > 0$, the quartic potential $V_{\mu,\lambda_1,\lambda_2}(A) = -\frac{\mu^2}{2}\operatorname{Tr}(A^2) + \frac{\lambda_1}{4}(\operatorname{Tr}(A^2))^2 + \frac{\lambda_2}{4}\operatorname{Tr}(A^4)$ attains its strict global minimum over $\mathfrak{su}(5)_{\mathrm{sa}}$ exclusively on the three-plus-two orbit.
7. **Theorem 7 (Joint Higgs Gram Matrix Spectrum, Unbroken-Subalgebra Projector, and Noncommuting Pinch Identity):** For the joint datum $(A_0, \zeta)$ with $A_0 = a I_3 \oplus b I_2$ ($a \neq b$) and $|\zeta| = \kappa > 0$, the $25 \times 25$ infinitesimal gauge Gram operator $\mathcal{M}^2$ on $\mathfrak{u}(5)_{\mathrm{sa}}$ decomposes into three orthogonal eigenspaces: $\ker \mathcal{M}^2 = \operatorname{Lie}(H) = \mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)_Y$ (eigenvalue $0$, multiplicity $12$), the off-diagonal coset space $\mathfrak{m}_{3\times 2}$ (eigenvalue $(a - b)^2 > 0$, multiplicity $12$), and the central generator $T_0 = \frac{1}{\sqrt{5}}I_5$ (eigenvalue $20\kappa^2 > 0$, multiplicity $1$). The orthogonal projector onto $\operatorname{Lie}(H)$ has the exact polynomial form $\Pi_{\operatorname{Lie}(H)}(X) = X - (a-b)^{-2}[A_0,[A_0,X]] - \frac{1}{5}\operatorname{Tr}(X)I_5 = P_3(A_0)X P_3(A_0) + P_2(A_0)X P_2(A_0) - \frac{1}{5}\operatorname{Tr}(X)I_5$, and for any noncommuting $A \in \mathcal{A} \otimes M_5(\mathbb{C})$ the pinch-commutator difference equals $(P_3(A)X P_3(A) + P_2(A)X P_2(A)) - (X - (a-b)^{-2}[A,[A,X]]) = D_A X + X D_A$ where $D_A = P_3(A)^2 - P_3(A)$.
8. **Theorem 8 (Single-Link Two-Sided Transport Floor and Multi-Copy Coherent FMS Defect Scaling):** On a single link register $\Lambda^5 \mathbb{C}^{10}$, every scalar multiple $T(\gamma) = \gamma D_{xy}$ ($\gamma \in \mathbb{C}$) satisfies the exact state identity $D_+(\omega; \gamma) + D_-(\omega; \gamma) = 2 - (1 - (|\gamma|^2 - 1)^2)(p_0 + p_5) \ge 1$ in every state $\omega$. In contrast, on the $K$-copy symmetric coherent representation $(\mathbb{C}^2)^{\otimes K}$ with $\Phi_K^a = \frac{1}{K}\sum_{\nu=1}^K \sigma_a^{(\nu)}$ and state $|\psi_K\rangle = |+\rangle^{\otimes K}$, $|\psi_K\rangle$ is an exact eigenvector of $\sum_{a=1}^3 (\Phi_K^a)^2$ with eigenvalue $1 + \frac{2}{K}$, yielding closed-form rational idempotence defects $\omega_K(|P_\pm(1)^2 - P_\pm(1)|_{\mathrm{HS}}^2) = \frac{K+1}{K^3}$ at classical radius $r = 1$ and $\omega_K(|P_\pm(r_K)^2 - P_\pm(r_K)|_{\mathrm{HS}}^2) = \frac{1}{2K(K+2)}$ at Casimir-matched radius $r_K = \sqrt{1 + 2/K}$, while on $(\Lambda^5\mathbb{C}^{10})^{\otimes K}$ the $K$-copy coherent determinant average $\widehat{D}_K = \frac{2}{K}\sum_{\nu=1}^K D_{xy}^{(\nu)}$ has exact rational transport defect $\varpi_K((\widehat{D}_K^\dagger \widehat{D}_K - I)^2) = \varpi_K((\widehat{D}_K \widehat{D}_K^\dagger - I)^2) = \frac{3K+2}{K^3}$.

| Obligation item | Status in this note | Exact scope |
|---|---|---|
| Noncommuting $SU(2)$ adjoint projector defect and state-$L^2$ equality | Proved here (Theorem 1) | Any unital $*$-algebra $\mathcal{A}$, self-adjoint triple $\Phi^a$, scale $r > 0$, and state $\omega$ |
| $U(5)$ $3+2$ linear projector defect, CAR bilinear identity $C^2 = (6-n)C$, and rank-three certification | Proved here (Theorem 2) | Self-adjoint $A \in \mathcal{A} \otimes M_5(\mathbb{C})$, $a \neq b$, and five-mode CAR sectors $\Lambda^n \mathbb{C}^5$ |
| Orthogonal real $6+4$ projector and complex-structure polynomial factorization | Proved here (Theorem 3) | Skew-adjoint $A \in \mathcal{A} \otimes M_{10}(\mathbb{R})$, $a,b \neq 0$, $a^2 \neq b^2$ |
| Joint stabilizer $K_{U(5)} = H\{\pm I_5\}$ and $H \cong (SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6$ | Proved here (Theorem 4) | $A_0 = a I_3 \oplus b I_2$ ($a \neq b$) and $0 \neq \zeta \in (\det \mathbb{C}^5)^{\otimes 2}$ |
| Native fermion-even determinant-square carrier $\mathcal{O}_{xy}^{(10)} = B_x D_{xy} B_y$ on $\Lambda^5 \mathbb{C}^{10}$ | Proved here (Theorem 5) | Two five-mode matter sites $x,y$ and one half-filled link register $\Lambda^5 \mathbb{C}^{10}$ |
| Global quartic $\mathfrak{su}(5)$ potential $3+2$ orbit selection and sharp fourth-moment bounds | Proved here (Theorem 6) | All $A \in \mathfrak{su}(5)_{\mathrm{sa}}$ and parameters $\mu^2 > 0$, $\lambda_2 > 0$, $30\lambda_1 + 7\lambda_2 > 0$ |
| Joint $25 \times 25$ Higgs Gram matrix spectrum, $\Pi_{\operatorname{Lie}(H)}$ projector, and pinch identity | Proved here (Theorem 7) | Full Lie algebra $\mathfrak{u}(5)_{\mathrm{sa}}$ and noncommuting $A, X \in \mathcal{A} \otimes M_5(\mathbb{C})$ |
| Single-link two-sided transport bound $\ge 1$ and $K$-copy coherent FMS defect scaling | Proved here (Theorem 8) | All states on $\Lambda^5 \mathbb{C}^{10}$ and $K$-copy coherent registers $(\mathbb{C}^2)^{\otimes K}$ ($K \ge 1$) |
| Microscopic derivation of effective quartic coupling $\lambda_2 > 0$ from the Floquet tick | Open downstream obligation | Requires deriving the effective potential from the coupled unitary tick |

**Prior repo context and literature credit:** The representation-theoretic slot matching of one Standard Model generation into $SU(5)$ is treated in `docs/SU5_EMBEDDING_FROM_GRAPH_FIRST_SURFACE_THEOREM_NOTE_2026-05-07.md` and `docs/SU5_DECOMPOSITION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`. The classical orbit-projector idea for gauge-invariant composites originates in J. Fröhlich, G. Morchio, and F. Strocchi, *Nuclear Physics B* **190** (1981) 553–582, and the classical $\mathfrak{su}(N)$ quartic potential minimization is studied in L.-F. Li, *Physical Review D* **9** (1974) 1723–1739. None of those works proves the noncommuting operator defect identities, the five-mode CAR bilinear identity $C^2 = (6-n)C$, the orthogonal complex-structure polynomial factorization, the $\Lambda^5\mathbb{C}^{10}$ determinant-square carrier, the derivative-free cubic-discriminant proof of $\mathfrak{su}(5)$ orbit selection, the noncommuting pinch-commutator identity, or the exact $K$-copy rational FMS defect formulas established below.

---

## 1. Noncommuting $SU(2)$ Adjoint Projector Defect Identity and Invariant Strings

Let $\mathcal{A}$ be a unital $*$-algebra over $\mathbb{C}$ with unit $I_{\mathcal{A}}$. In $M_2(\mathbb{C})$, let $I_2$ be the $2\times 2$ identity matrix and let
$$
\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\sigma_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \qquad
\sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$
be the standard Pauli matrices, which satisfy $\sigma_a^* = \sigma_a$, $\operatorname{Tr}_{M_2}(\sigma_a) = 0$, and
$$
\sigma_a \sigma_b = \delta_{ab} I_2 + i \sum_{c=1}^3 \varepsilon_{abc} \sigma_c \qquad (a,b \in \{1,2,3\}),
$$
where $\varepsilon_{abc}$ is the totally antisymmetric Levi-Civita symbol with $\varepsilon_{123} = +1$.

For any $M = \sum_{\alpha,\beta=1}^2 M_{\alpha\beta} \otimes E_{\alpha\beta} \in \mathcal{A} \otimes M_2(\mathbb{C})$, define the internal trace $\operatorname{Tr}_{M_2}(M) = M_{11} + M_{22} \in \mathcal{A}$ and the internal Hilbert-Schmidt square
$$
|M|_{\mathrm{HS}}^2 := \operatorname{Tr}_{M_2}(M^* M) = \sum_{\alpha,\beta=1}^2 M_{\alpha\beta}^* M_{\alpha\beta} \in \mathcal{A}.
$$

### Theorem 1 (Noncommuting $SU(2)$ Adjoint Projector Defect Identity and State-$L^2$ Equality)

Let $\Phi = (\Phi^1, \Phi^2, \Phi^3) \in (\mathcal{A}_{\mathrm{sa}})^3$ be three self-adjoint elements of $\mathcal{A}$ ($(\Phi^a)^* = \Phi^a$), let $r > 0$ be a real scale parameter, and define in $\mathcal{A} \otimes M_2(\mathbb{C})$:
$$
A := \sum_{a=1}^3 \Phi^a \otimes \sigma_a, \qquad
P_\pm := \frac{1}{2}\left(I_{\mathcal{A}} \otimes I_2 \pm \frac{1}{r} A\right).
$$

1. **Exact algebraic resolution and quadratic defect:** $A^* = A$, $P_\pm^* = P_\pm$, $P_+ + P_- = I_{\mathcal{A}} \otimes I_2$, $\operatorname{Tr}_{M_2}(P_\pm) = I_{\mathcal{A}}$, and
   $$
   P_+^2 - P_+ = P_-^2 - P_- = -P_+ P_- = -P_- P_+ = \frac{1}{4 r^2}\left(A^2 - r^2 I_{\mathcal{A}} \otimes I_2\right),
   $$
   where
   $$
   A^2 - r^2 I_{\mathcal{A}} \otimes I_2 = R_r \otimes I_2 + \sum_{c=1}^3 C_c \otimes \sigma_c,
   $$
   with self-adjoint radial and commutator defect operators in $\mathcal{A}$ given by
   $$
   R_r := \sum_{a=1}^3 (\Phi^a)^2 - r^2 I_{\mathcal{A}}, \qquad
   C_c := \frac{i}{2}\sum_{a,b=1}^3 \varepsilon_{abc}[\Phi^a, \Phi^b].
   $$
2. **Exact internal Hilbert-Schmidt orthogonality and state-$L^2$ identity:** In $\mathcal{A}$, the internal Hilbert-Schmidt square of $A^2 - r^2 I_{\mathcal{A}} \otimes I_2$ satisfies the exact operator identity
   $$
   \left|A^2 - r^2 I_{\mathcal{A}} \otimes I_2\right|_{\mathrm{HS}}^2
   = 2 R_r^2 + 2 \sum_{c=1}^3 C_c^2
   = 2\left(\sum_{a=1}^3 (\Phi^a)^2 - r^2 I_{\mathcal{A}}\right)^2 + \sum_{a,b=1}^3 |[\Phi^a, \Phi^b]|^2,
   $$
   where $|[\Phi^a, \Phi^b]|^2 := [\Phi^a, \Phi^b]^* [\Phi^a, \Phi^b] = -[\Phi^a, \Phi^b]^2$. Consequently, for every linear functional $\omega$ on $\mathcal{A}$,
   $$
   \omega\!\left(|P_\pm^2 - P_\pm|_{\mathrm{HS}}^2\right)
   = \omega\!\left(|P_+ P_-|_{\mathrm{HS}}^2\right)
   = \frac{1}{8 r^4}\omega\!\left(\left(\sum_{a=1}^3 (\Phi^a)^2 - r^2 I_{\mathcal{A}}\right)^2\right)
   + \frac{1}{16 r^4}\sum_{a,b=1}^3 \omega\!\left(|[\Phi^a, \Phi^b]|^2\right).
   $$
3. **Local gauge covariance and four-channel invariant strings:** Let $SU(2)_X \times SU(2)_Y$ act on $\mathcal{A}$ by $*$-automorphisms $\alpha_{g_X, g_Y}$ such that at endpoints $Z \in \{X, Y\}$, $\alpha_{g_X, g_Y}(\Phi_Z^a) = \sum_{b=1}^3 \mathrm{Ad}_{g_Z}^{ab}\Phi_Z^b$, where $g \sigma_b g^* = \sum_{a=1}^3 \mathrm{Ad}_g^{ab}\sigma_a$. Then
   $$
   (\alpha_{g_X, g_Y} \otimes \mathrm{id})(P_s(\Phi_Z)) = (I_{\mathcal{A}} \otimes g_Z)\, P_s(\Phi_Z)\, (I_{\mathcal{A}} \otimes g_Z^*) \qquad (s \in \{+,-\}).
   $$
   For any endpoint doublets $\Psi_Z \in \mathcal{A} \otimes \mathbb{C}^2$ transforming as $(\alpha_{g_X, g_Y} \otimes \mathrm{id})(\Psi_Z) = (I_{\mathcal{A}} \otimes g_Z)\Psi_Z$ and any transporter $\mathcal{U}_{XY} \in \mathcal{A} \otimes M_2(\mathbb{C})$ transforming bi-covariantly as $(\alpha_{g_X, g_Y} \otimes \mathrm{id})(\mathcal{U}_{XY}) = (I_{\mathcal{A}} \otimes g_X)\mathcal{U}_{XY}(I_{\mathcal{A}} \otimes g_Y^*)$, the four projected strings
   $$
   \mathcal{S}_{s,s'}(X,Y) := \Psi_X^* P_s(\Phi_X)\, \mathcal{U}_{XY}\, P_{s'}(\Phi_Y) \Psi_Y \in \mathcal{A} \qquad (s,s' \in \{+,-\})
   $$
   satisfy $\alpha_{g_X, g_Y}(\mathcal{S}_{s,s'}(X,Y)) = \mathcal{S}_{s,s'}(X,Y)$ for all $(g_X, g_Y) \in SU(2)_X \times SU(2)_Y$ and resolve the full unprojected string:
   $$
   \sum_{s,s' \in \{+,-\}} \mathcal{S}_{s,s'}(X,Y) = \Psi_X^* \mathcal{U}_{XY} \Psi_Y.
   $$

#### Proof of Theorem 1

**(1)** Since $(\Phi^a)^* = \Phi^a$ and $\sigma_a^* = \sigma_a$, we have $A^* = A$ and $P_\pm^* = P_\pm$. Adding $P_+$ and $P_-$ gives $P_+ + P_- = I_{\mathcal{A}} \otimes I_2$, and $\operatorname{Tr}_{M_2}(P_\pm) = \frac{1}{2}\operatorname{Tr}_{M_2}(I_2)I_{\mathcal{A}} \pm \frac{1}{2r}\sum_{a=1}^3 \Phi^a \operatorname{Tr}_{M_2}(\sigma_a) = I_{\mathcal{A}}$. Direct expansion gives
$$
P_\pm^2 - P_\pm = \frac{1}{4}\left(I_{\mathcal{A}} \otimes I_2 \pm \frac{2}{r}A + \frac{1}{r^2}A^2\right) - \frac{1}{2}\left(I_{\mathcal{A}} \otimes I_2 \pm \frac{1}{r}A\right) = \frac{1}{4 r^2}\left(A^2 - r^2 I_{\mathcal{A}} \otimes I_2\right),
$$
and $P_+ P_- = (I_{\mathcal{A}} \otimes I_2 - P_-)P_- = -(P_-^2 - P_-) = P_- P_+$. Expanding $A^2$ via the Pauli product law yields
$$
\begin{aligned}
A^2 &= \sum_{a,b=1}^3 \Phi^a \Phi^b \otimes \sigma_a \sigma_b
= \sum_{a,b=1}^3 \Phi^a \Phi^b \otimes \left(\delta_{ab} I_2 + i \sum_{c=1}^3 \varepsilon_{abc}\sigma_c\right) \\
&= \left(\sum_{a=1}^3 (\Phi^a)^2\right) \otimes I_2 + \frac{i}{2}\sum_{a,b,c=1}^3 \varepsilon_{abc}(\Phi^a \Phi^b - \Phi^b \Phi^a) \otimes \sigma_c,
\end{aligned}
$$
where the second term used the antisymmetry $\varepsilon_{abc} = -\varepsilon_{bac}$. Subtracting $r^2 I_{\mathcal{A}} \otimes I_2$ gives $A^2 - r^2 I_{\mathcal{A}} \otimes I_2 = R_r \otimes I_2 + \sum_{c=1}^3 C_c \otimes \sigma_c$. Because $(\Phi^a)^* = \Phi^a$, $([\Phi^a, \Phi^b])^* = -[\Phi^a, \Phi^b]$, so $C_c^* = C_c$ and $R_r^* = R_r$.

**(2)** Since $A^2 - r^2 I_{\mathcal{A}} \otimes I_2$ is self-adjoint, its square in $\mathcal{A} \otimes M_2(\mathbb{C})$ is
$$
\begin{aligned}
(A^2 - r^2 I_{\mathcal{A}} \otimes I_2)^2
&= R_r^2 \otimes I_2 + \sum_{c=1}^3 (R_r C_c + C_c R_r) \otimes \sigma_c + \sum_{c,d=1}^3 C_c C_d \otimes \sigma_c \sigma_d.
\end{aligned}
$$
Applying $\operatorname{Tr}_{M_2}$ and using $\operatorname{Tr}_{M_2}(I_2) = 2$, $\operatorname{Tr}_{M_2}(\sigma_c) = 0$, and $\operatorname{Tr}_{M_2}(\sigma_c \sigma_d) = 2\delta_{cd}$ eliminates all cross terms $(R_r C_c + C_c R_r)$ and all off-diagonal terms $c \neq d$:
$$
|A^2 - r^2 I_{\mathcal{A}} \otimes I_2|_{\mathrm{HS}}^2
= \operatorname{Tr}_{M_2}\!\left((A^2 - r^2 I_{\mathcal{A}} \otimes I_2)^2\right)
= 2 R_r^2 + 2\sum_{c=1}^3 C_c^2.
$$
For each $c \in \{1,2,3\}$, let $(a,b,c)$ be an even permutation of $(1,2,3)$. Then $C_c = i[\Phi^a, \Phi^b]$, so $C_c^2 = C_c^* C_c = |[\Phi^a, \Phi^b]|^2 = |[\Phi^b, \Phi^a]|^2$. Summing over $c \in \{1,2,3\}$ gives $2\sum_{c=1}^3 C_c^2 = \sum_{a \neq b} |[\Phi^a, \Phi^b]|^2 = \sum_{a,b=1}^3 |[\Phi^a, \Phi^b]|^2$. Dividing by $(4r^2)^2 = 16r^4$ and applying $\omega$ yields the state-$L^2$ equality.

**(3)** At endpoint $Z \in \{X,Y\}$,
$$
(\alpha_{g_X, g_Y} \otimes \mathrm{id})(A_Z)
= \sum_{a,b=1}^3 \mathrm{Ad}_{g_Z}^{ab} \Phi_Z^b \otimes \sigma_a
= \sum_{b=1}^3 \Phi_Z^b \otimes (g_Z \sigma_b g_Z^*)
= (I_{\mathcal{A}} \otimes g_Z) A_Z (I_{\mathcal{A}} \otimes g_Z^*),
$$
which gives $(\alpha_{g_X, g_Y} \otimes \mathrm{id})(P_s(\Phi_Z)) = (I_{\mathcal{A}} \otimes g_Z) P_s(\Phi_Z) (I_{\mathcal{A}} \otimes g_Z^*)$. Since $\Psi_X^*$ transforms from the right by $I_{\mathcal{A}} \otimes g_X^*$ and $g_Z^* g_Z = I_2$ for $g_Z \in SU(2)$, all internal gauge factors cancel in $\mathcal{S}_{s,s'}(X,Y)$:
$$
\begin{aligned}
\alpha_{g_X, g_Y}(\mathcal{S}_{s,s'}(X,Y))
&= \Psi_X^*(I_{\mathcal{A}} \otimes g_X^*)(I_{\mathcal{A}} \otimes g_X)P_s(\Phi_X)(I_{\mathcal{A}} \otimes g_X^*)(I_{\mathcal{A}} \otimes g_X)\mathcal{U}_{XY}(I_{\mathcal{A}} \otimes g_Y^*)(I_{\mathcal{A}} \otimes g_Y)P_{s'}(\Phi_Y)(I_{\mathcal{A}} \otimes g_Y^*)(I_{\mathcal{A}} \otimes g_Y)\Psi_Y \\
&= \mathcal{S}_{s,s'}(X,Y).
\end{aligned}
$$
Summing over $s, s' \in \{+,-\}$ and using $P_+(\Phi_X) + P_-(\Phi_X) = I_{\mathcal{A}} \otimes I_2$ and $P_+(\Phi_Y) + P_-(\Phi_Y) = I_{\mathcal{A}} \otimes I_2$ gives $\sum_{s,s'} \mathcal{S}_{s,s'}(X,Y) = \Psi_X^* \mathcal{U}_{XY} \Psi_Y$. $\blacksquare$

---

## 2. $U(5)$ Three-Plus-Two Adjoint Projector Calculus and Rank-Separation Certification

Let $\mathcal{A}$ be a unital $*$-algebra and write $I_5$ for $I_{\mathcal{A}} \otimes I_5 \in \mathcal{A} \otimes M_5(\mathbb{C})$. For $M = \sum_{i,j=1}^5 M_{ij} \otimes E_{ij} \in \mathcal{A} \otimes M_5(\mathbb{C})$, write $\operatorname{Tr}_{M_5}(M) = \sum_{i=1}^5 M_{ii} \in \mathcal{A}$ and $|M|_{\mathrm{HS}}^2 = \operatorname{Tr}_{M_5}(M^* M) = \sum_{i,j=1}^5 M_{ij}^* M_{ij} \in \mathcal{A}$.

### Theorem 2 ($U(5)$ Three-Plus-Two Adjoint Projector Calculus, Fermionic Bilinear Identity, and Rank-Separation Certification)

Let $A = A^* \in \mathcal{A} \otimes M_5(\mathbb{C})$ be self-adjoint and let $a, b \in \mathbb{R}$ with $a \neq b$. Define the linear Lagrange interpolants
$$
P_3(A) := \frac{A - b I_5}{a - b}, \qquad
P_2(A) := \frac{a I_5 - A}{a - b} = I_5 - P_3(A).
$$

1. **Exact resolution, quadratic defect, and internal trace identities:** $P_3(A)^* = P_3(A)$, $P_2(A)^* = P_2(A)$, $P_3(A) + P_2(A) = I_5$, $a P_3(A) + b P_2(A) = A$, and
   $$
   P_3(A)^2 - P_3(A) = P_2(A)^2 - P_2(A) = -P_3(A) P_2(A) = -P_2(A) P_3(A) = \frac{(A - a I_5)(A - b I_5)}{(a - b)^2},
   $$
   with internal trace residuals
   $$
   \operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}} = \frac{\operatorname{Tr}_{M_5}(A) - (3a + 2b)I_{\mathcal{A}}}{a - b}, \qquad
   \operatorname{Tr}_{M_5}(P_2(A)) - 2 I_{\mathcal{A}} = -\frac{\operatorname{Tr}_{M_5}(A) - (3a + 2b)I_{\mathcal{A}}}{a - b}.
   $$
   In particular, when $3a + 2b = 0$ and $\operatorname{Tr}_{M_5}(A) = 0$, $\operatorname{Tr}_{M_5}(P_3(A)) = 3 I_{\mathcal{A}}$ and $\operatorname{Tr}_{M_5}(P_2(A)) = 2 I_{\mathcal{A}}$ hold identically in $\mathcal{A}$.
2. **Exact noncommuting quadratic identity for the five-flavor CAR bilinear:** Let $\mathcal{A} = \operatorname{End}(\Lambda(\mathbb{C}^5))$ be the operator algebra of five canonical fermion modes $c_1,\dots,c_5$ satisfying $\{c_i, c_j\} = 0$ and $\{c_i, c_j^\dagger\} = \delta_{ij} I$. Let $N = \sum_{j=1}^5 c_j^\dagger c_j$ be the total fermion number operator and define $C := \sum_{i,k=1}^5 c_i^\dagger c_k \otimes E_{ik} \in \mathcal{A} \otimes M_5(\mathbb{C})$. Then $C^* = C$, $\operatorname{Tr}_{M_5}(C) = N$, and in $\mathcal{A} \otimes M_5(\mathbb{C})$:
   $$
   C^2 = (6 I - N) C.
   $$
   Consequently, on each $n$-fermion sector $\Lambda^n \mathbb{C}^5$ ($n \in \{1,2,3,4,5\}$), the rescaled operator $P_{\mathrm{CAR}}^{(n)} := \frac{1}{6 - n} C|_{\Lambda^n \mathbb{C}^5}$ is an exact self-adjoint idempotent in $\operatorname{End}(\Lambda^n \mathbb{C}^5) \otimes M_5(\mathbb{C})$,
   $$
   \left(P_{\mathrm{CAR}}^{(n)}\right)^2 - P_{\mathrm{CAR}}^{(n)} = 0,
   $$
   whose internal trace is
   $$
   \operatorname{Tr}_{M_5}\!\left(P_{\mathrm{CAR}}^{(n)}\right) = \frac{n}{6 - n} I_{\Lambda^n \mathbb{C}^5} =
   \begin{cases}
   \frac{1}{5} I & (n = 1), \\
   \frac{1}{2} I & (n = 2), \\
   1\, I & (n = 3), \\
   2\, I & (n = 4), \\
   5\, I & (n = 5).
   \end{cases}
   $$
   At $n = 4$, the complementary idempotent $I_5 - P_{\mathrm{CAR}}^{(4)} = I_5 - \frac{1}{2}C|_{\Lambda^4 \mathbb{C}^5}$ satisfies $(I_5 - P_{\mathrm{CAR}}^{(4)})^2 = I_5 - P_{\mathrm{CAR}}^{(4)}$ and $\operatorname{Tr}_{M_5}(I_5 - P_{\mathrm{CAR}}^{(4)}) = 3 I_{\Lambda^4 \mathbb{C}^5}$.
3. **Rank-separation witness and joint certification functional:** For $k \in \{0,1,2,3,4,5\}$, let $A_{(k)} = \operatorname{diag}(\underbrace{a,\dots,a}_{k},\underbrace{b,\dots,b}_{5-k}) \in M_5(\mathbb{C})$. Every $A_{(k)}$ satisfies $(A_{(k)} - a I_5)(A_{(k)} - b I_5) = 0$ and $\operatorname{Tr}_{M_5}(P_3(A_{(k)})) = k$. On the two-dimensional commutative algebra $\mathcal{A}_2 = \mathbb{C} \oplus \mathbb{C}$ with state $\omega_{\mathrm{mix}}(x_1, x_2) = \frac{1}{2}(x_1 + x_2)$, the operator $A_{\mathrm{mix}} = (A_{(4)}, A_{(2)}) \in \mathcal{A}_2 \otimes M_5(\mathbb{C})$ satisfies
   $$
   P_3(A_{\mathrm{mix}})^2 - P_3(A_{\mathrm{mix}}) = 0, \qquad
   \omega_{\mathrm{mix}}\!\left(\operatorname{Tr}_{M_5}(P_3(A_{\mathrm{mix}})) - 3 I_{\mathcal{A}_2}\right) = 0,
   $$
   while having zero support on the $k = 3$ stratum. In contrast, the positive joint defect element
   $$
   \mathcal{D}_{3+2}(A) := \left|P_3(A)^2 - P_3(A)\right|_{\mathrm{HS}}^2 + \left(\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}}\right)^2 \in \mathcal{A}_+
   $$
   satisfies $\omega_{\mathrm{mix}}(\mathcal{D}_{3+2}(A_{\mathrm{mix}})) = 1$, and for any self-adjoint matrix $A = A^* \in M_5(\mathbb{C})$ with eigenvalues $\lambda_1,\dots,\lambda_5 \in \mathbb{R}$,
   $$
   \mathcal{D}_{3+2}(A) = \sum_{m=1}^5 \frac{(\lambda_m - a)^2(\lambda_m - b)^2}{(a - b)^4} + \left(\sum_{m=1}^5 \frac{\lambda_m - b}{a - b} - 3\right)^2 \ge \min_{k \in \{0,\dots,5\}} \mathcal{D}_{3+2}(A_{(k)}) = 0,
   $$
   with $\mathcal{D}_{3+2}(A) = 0$ in $M_5(\mathbb{C})$ if and only if $A$ is unitarily conjugate to $A_{(3)} = a I_3 \oplus b I_2$, and $\mathcal{D}_{3+2}(A_{(k)}) = (k - 3)^2 \ge 1$ for every $k \in \{0,1,2,4,5\}$.

#### Proof of Theorem 2

**(1)** By definition, $P_3(A) + P_2(A) = \frac{A - b I_5 + a I_5 - A}{a - b} = I_5$ and $a P_3(A) + b P_2(A) = \frac{a(A - b I_5) + b(a I_5 - A)}{a - b} = A$. Next,
$$
P_3(A)^2 - P_3(A) = P_3(A)(P_3(A) - I_5) = -P_3(A) P_2(A) = \frac{(A - b I_5)(A - a I_5)}{(a - b)^2} = \frac{(A - a I_5)(A - b I_5)}{(a - b)^2},
$$
because $A - a I_5$ and $A - b I_5$ are polynomials in the single operator $A$ and therefore commute. Taking $\operatorname{Tr}_{M_5}$ of $P_3(A) = (A - b I_5)/(a - b)$ gives $\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}} = \frac{\operatorname{Tr}_{M_5}(A) - 5 b I_{\mathcal{A}} - 3(a - b)I_{\mathcal{A}}}{a - b} = \frac{\operatorname{Tr}_{M_5}(A) - (3a + 2b)I_{\mathcal{A}}}{a - b}$.

**(2)** For $C = \sum_{i,k=1}^5 c_i^\dagger c_k \otimes E_{ik}$, its $(i,k)$ entry in $M_5(\mathbb{C})$ is $C_{ik} = c_i^\dagger c_k$, so $(C^*)_{ik} = C_{ki}^* = (c_k^\dagger c_i)^* = c_i^\dagger c_k = C_{ik}$ and $\operatorname{Tr}_{M_5}(C) = \sum_{i=1}^5 c_i^\dagger c_i = N$. The $(i,k)$ matrix entry of $C^2$ is
$$
(C^2)_{ik} = \sum_{j=1}^5 c_i^\dagger c_j c_j^\dagger c_k.
$$
Using the CAR identity $c_j c_j^\dagger = I - c_j^\dagger c_j$, we have $\sum_{j=1}^5 c_j c_j^\dagger = 5 I - N$. Furthermore, for every $j \in \{1,\dots,5\}$, $\{c_j, c_k\} = 0$ and $\{c_j^\dagger, c_k\} = \delta_{jk} I$ give
$$
c_j^\dagger c_j c_k = -c_j^\dagger c_k c_j = -(\delta_{jk} I - c_k c_j^\dagger) c_j = -\delta_{jk} c_j + c_k c_j^\dagger c_j,
$$
and summing over $j = 1,\dots,5$ gives $N c_k = -c_k + c_k N = c_k(N - I)$. Consequently, $(5 I - N) c_k = 5 c_k - c_k(N - I) = c_k (6 I - N)$, and since $N$ commutes with the number-conserving bilinear $c_i^\dagger c_k$, we obtain $c_i^\dagger (5 I - N) c_k = c_i^\dagger c_k (6 I - N) = (6 I - N) c_i^\dagger c_k$. Therefore,
$$
(C^2)_{ik} = c_i^\dagger (5 I - N) c_k = (6 I - N) c_i^\dagger c_k = ((6 I - N)C)_{ik}
$$
for all $1 \le i,k \le 5$. Restricting to $\Lambda^n \mathbb{C}^5$ where $N = n I_{\Lambda^n \mathbb{C}^5}$ gives $C^2 = (6 - n)C$. For $1 \le n \le 5$, $6 - n \ge 1$, so $P_{\mathrm{CAR}}^{(n)} = (6 - n)^{-1}C|_{\Lambda^n \mathbb{C}^5}$ satisfies $(P_{\mathrm{CAR}}^{(n)})^2 = (6 - n)^{-2}(6 - n)C|_{\Lambda^n \mathbb{C}^5} = P_{\mathrm{CAR}}^{(n)}$ and $\operatorname{Tr}_{M_5}(P_{\mathrm{CAR}}^{(n)}) = (6 - n)^{-1} n I_{\Lambda^n \mathbb{C}^5}$.

**(3)** For $A_{(k)}$, its diagonal entries lie in $\{a,b\}$ with $a$ appearing $k$ times and $b$ appearing $5 - k$ times, so $(A_{(k)} - a I_5)(A_{(k)} - b I_5) = 0$ and $P_3(A_{(k)}) = \operatorname{diag}(\underbrace{1,\dots,1}_{k},\underbrace{0,\dots,0}_{5-k})$ has trace $k$. For $A_{\mathrm{mix}} = (A_{(4)}, A_{(2)})$, $\operatorname{Tr}_{M_5}(P_3(A_{\mathrm{mix}})) - 3 I_{\mathcal{A}_2} = (4 - 3, 2 - 3) = (1, -1)$, whose $\omega_{\mathrm{mix}}$-expectation is $\frac{1}{2}(1 - 1) = 0$, whereas $(\operatorname{Tr}_{M_5}(P_3(A_{\mathrm{mix}})) - 3 I_{\mathcal{A}_2})^2 = (1, 1)$ has expectation $1$. Finally, for any $A = A^* \in M_5(\mathbb{C})$ with eigenvalues $\lambda_1,\dots,\lambda_5$, unitary invariance of $\operatorname{Tr}_{M_5}$ gives the displayed spectral sum. Since both terms are nonnegative, $\mathcal{D}_{3+2}(A) = 0$ forces $\lambda_m \in \{a,b\}$ for every $m$ from the first term and $|\{m : \lambda_m = a\}| = 3$ from the second term, which means $A$ is unitarily conjugate to $A_{(3)}$. $\blacksquare$

---

## 3. Orthogonal Real Six-Plus-Four Projectors and Complex-Structure Factorization

Let $\iota: M_5(\mathbb{C}) \to M_{10}(\mathbb{R})$ be the standard real block embedding sending each entry $x + i y \mapsto x I_2 + y J_2$, where
$$
I_2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
J_2 = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
J_2^2 = -I_2, \qquad J_2^T = -J_2.
$$
Under $\iota$, the skew-Hermitian generator $i H_0$ with $H_0 = a I_3 \oplus b I_2$ maps to the real skew-symmetric matrix
$$
A_0^{\mathrm{orth}} := \iota(i H_0) = a J_6 \oplus b J_4 \in \mathfrak{so}(10), \qquad
J_6 = I_3 \otimes J_2, \qquad J_4 = I_2 \otimes J_2.
$$

### Theorem 3 (Orthogonal Real Six-Plus-Four Projectors and Complex-Structure Defect Factorization)

Let $\mathcal{A}$ be a unital $*$-algebra, let $A \in \mathcal{A} \otimes M_{10}(\mathbb{R})$ be skew-adjoint ($A^* = -A$), and let $a, b \in \mathbb{R} \setminus \{0\}$ satisfy $a^2 \neq b^2$. Write $I_{10}$ for $I_{\mathcal{A}} \otimes I_{10}$ and define in $\mathcal{A} \otimes M_{10}(\mathbb{R})$:
$$
Q_6(A) := \frac{-A^2 - b^2 I_{10}}{a^2 - b^2}, \qquad
Q_4(A) := I_{10} - Q_6(A) = \frac{A^2 + a^2 I_{10}}{a^2 - b^2}, \qquad
J_A := A\left(a^{-1} Q_6(A) + b^{-1} Q_4(A)\right).
$$

1. **Commutation, adjointness, and real $6+4$ quartic defect:** $Q_6(A)^* = Q_6(A)$, $Q_4(A)^* = Q_4(A)$, $J_A^* = -J_A$, $[A, Q_6(A)] = [A, Q_4(A)] = [A, J_A] = 0$, $-a^2 Q_6(A) - b^2 Q_4(A) = A^2$, and
   $$
   Q_6(A)^2 - Q_6(A) = Q_4(A)^2 - Q_4(A) = -Q_6(A) Q_4(A) = \frac{(A^2 + a^2 I_{10})(A^2 + b^2 I_{10})}{(a^2 - b^2)^2}.
   $$
2. **Exact polynomial factorization of the complex-structure and reconstruction defects:** In $\mathcal{A} \otimes M_{10}(\mathbb{R})$, both the complex-structure defect $J_A^2 + I_{10}$ and the linear reconstruction residual $A - (a Q_6(A) + b Q_4(A)) J_A$ factor identically through $Q_6(A)^2 - Q_6(A)$:
   $$
   J_A^2 + I_{10} = \frac{(a - b)^2 A^2 + (a^2 - b^2)^2 I_{10}}{a^2 b^2}\,\left(Q_6(A)^2 - Q_6(A)\right),
   $$
   $$
   A - \left(a Q_6(A) + b Q_4(A)\right) J_A = \frac{(a - b)^2}{ab}\,A\,\left(Q_6(A)^2 - Q_6(A)\right).
   $$
3. **Centralizer dimension reduction in $\mathfrak{so}(10)$:** For $A_0^{\mathrm{orth}} = a J_6 \oplus b J_4 \in \mathfrak{so}(10)$ with $a, b \neq 0$ and $a^2 \neq b^2$, we have $Q_6(A_0^{\mathrm{orth}}) = I_6 \oplus 0_4$, $Q_4(A_0^{\mathrm{orth}}) = 0_6 \oplus I_4$, and $J_{A_0^{\mathrm{orth}}} = J_6 \oplus J_4$. In $\mathfrak{so}(10)$ ($\dim \mathfrak{so}(10) = 45$):
   $$
   \mathfrak{c}_{\mathrm{real}} := \{X \in \mathfrak{so}(10) : [X, Q_6(A_0^{\mathrm{orth}})] = 0\} = \mathfrak{so}(6) \oplus \mathfrak{so}(4), \qquad \dim_{\mathbb{R}} \mathfrak{c}_{\mathrm{real}} = 15 + 6 = 21,
   $$
   whereas the joint centralizer of $(Q_6(A_0^{\mathrm{orth}}), J_{A_0^{\mathrm{orth}}})$ equals the centralizer of $A_0^{\mathrm{orth}}$:
   $$
   \mathfrak{c}_{\mathrm{unitary}} := \{X \in \mathfrak{so}(10) : [X, Q_6(A_0^{\mathrm{orth}})] = 0 \text{ and } [X, J_{A_0^{\mathrm{orth}}}] = 0\} = \{X \in \mathfrak{so}(10) : [X, A_0^{\mathrm{orth}}] = 0\} = \iota(i\,\mathfrak{u}(3)_{\mathrm{sa}} \oplus i\,\mathfrak{u}(2)_{\mathrm{sa}}),
   $$
   which has real dimension $\dim_{\mathbb{R}} \mathfrak{c}_{\mathrm{unitary}} = 9 + 4 = 13$.

#### Proof of Theorem 3

**(1)** Since $A^* = -A$, $(A^2)^* = (A^*)^2 = A^2$, so $Q_6(A)$ and $Q_4(A)$ are self-adjoint polynomials in $A^2$. Every polynomial in $A$ commutes with $A$, so $[A, Q_6(A)] = [A, Q_4(A)] = 0$ and $J_A^* = (a^{-1}Q_6(A) + b^{-1}Q_4(A)) A^* = -J_A$. Direct algebra gives $-a^2 Q_6(A) - b^2 Q_4(A) = \frac{a^2(A^2 + b^2 I_{10}) - b^2(A^2 + a^2 I_{10})}{a^2 - b^2} = A^2$, and
$$
Q_6(A)^2 - Q_6(A) = -Q_6(A) Q_4(A) = \frac{(A^2 + b^2 I_{10})(A^2 + a^2 I_{10})}{(a^2 - b^2)^2}.
$$

**(2)** Put $D := Q_6(A)^2 - Q_6(A) = Q_4(A)^2 - Q_4(A) = -Q_6(A) Q_4(A)$. Using $Q_6(A)^2 = Q_6(A) + D$, $Q_4(A)^2 = Q_4(A) + D$, and $Q_6(A) Q_4(A) = -D$, we compute:
$$
\begin{aligned}
\left(a^{-1}Q_6(A) + b^{-1}Q_4(A)\right)^2
&= a^{-2}(Q_6(A) + D) - 2(ab)^{-1}D + b^{-2}(Q_4(A) + D) \\
&= a^{-2}Q_6(A) + b^{-2}Q_4(A) + \frac{(a - b)^2}{a^2 b^2} D.
\end{aligned}
$$
Similarly, multiplying $A^2 = -a^2 Q_6(A) - b^2 Q_4(A)$ by $a^{-2}Q_6(A) + b^{-2}Q_4(A)$ gives
$$
\begin{aligned}
A^2\left(a^{-2}Q_6(A) + b^{-2}Q_4(A)\right)
&= -Q_6(A)^2 - Q_4(A)^2 - \left(\frac{a^2}{b^2} + \frac{b^2}{a^2}\right)Q_6(A) Q_4(A) \\
&= -(Q_6(A) + Q_4(A)) - 2 D + \frac{a^4 + b^4}{a^2 b^2} D
= -I_{10} + \frac{(a^2 - b^2)^2}{a^2 b^2} D.
\end{aligned}
$$
Since $J_A^2 = A^2(a^{-1}Q_6(A) + b^{-1}Q_4(A))^2$, combining the two identities yields
$$
J_A^2 + I_{10} = \frac{(a - b)^2 A^2 + (a^2 - b^2)^2 I_{10}}{a^2 b^2} D.
$$
Likewise,
$$
(a Q_6(A) + b Q_4(A))(a^{-1} Q_6(A) + b^{-1} Q_4(A))
= Q_6(A)^2 + Q_4(A)^2 + \left(\frac{a}{b} + \frac{b}{a}\right) Q_6(A) Q_4(A)
= I_{10} + 2 D - \frac{a^2 + b^2}{ab} D
= I_{10} - \frac{(a - b)^2}{ab} D,
$$
and multiplying $I_{10} - (a Q_6(A) + b Q_4(A))(a^{-1}Q_6(A) + b^{-1}Q_4(A))$ by $A$ gives $A - (a Q_6(A) + b Q_4(A)) J_A = \frac{(a - b)^2}{ab} A D$.

**(3)** For $A_0^{\mathrm{orth}} = a J_6 \oplus b J_4$, $(A_0^{\mathrm{orth}})^2 = -a^2 I_6 \oplus (-b^2 I_4)$, so $Q_6(A_0^{\mathrm{orth}}) = I_6 \oplus 0_4$ and $J_{A_0^{\mathrm{orth}}} = J_6 \oplus J_4$. A skew-symmetric matrix $X = \begin{pmatrix} X_{66} & X_{64} \\ -X_{64}^T & X_{44} \end{pmatrix} \in \mathfrak{so}(10)$ commutes with $I_6 \oplus 0_4$ if and only if $X_{64} = 0$, leaving $X_{66} \in \mathfrak{so}(6)$ ($\dim = \binom{6}{2} = 15$) and $X_{44} \in \mathfrak{so}(4)$ ($\dim = \binom{4}{2} = 6$), total dimension $21$. Commuting in addition with $J_6 \oplus J_4$ requires $[X_{66}, J_6] = 0$ and $[X_{44}, J_4] = 0$, which identifies $X_{66} \in \mathfrak{so}(6) \cap \operatorname{End}_{\mathbb{C}}(\mathbb{C}^3) \cong \mathfrak{u}(3)$ ($\dim = 9$) and $X_{44} \in \mathfrak{so}(4) \cap \operatorname{End}_{\mathbb{C}}(\mathbb{C}^2) \cong \mathfrak{u}(2)$ ($\dim = 4$), total dimension $13$. Since $A_0^{\mathrm{orth}} = a Q_6(A_0^{\mathrm{orth}}) J_{A_0^{\mathrm{orth}}} + b Q_4(A_0^{\mathrm{orth}}) J_{A_0^{\mathrm{orth}}}$ and conversely $Q_6(A_0^{\mathrm{orth}}), J_{A_0^{\mathrm{orth}}}$ are polynomials in $A_0^{\mathrm{orth}}$, the joint centralizer of $(Q_6(A_0^{\mathrm{orth}}), J_{A_0^{\mathrm{orth}}})$ coincides with the centralizer of $A_0^{\mathrm{orth}}$. $\blacksquare$

---

## 4. Exact Joint Stabilizer $K_{U(5)} = H\{\pm I_5\}$ in $U(5)$

Let $G = U(5)$ act on the Hermitian adjoint $\mathfrak{u}(5)_{\mathrm{sa}} = \{X \in M_5(\mathbb{C}) : X^* = X\}$ by conjugation $g \cdot X = g X g^{-1}$ and on the one-dimensional determinant-square space $L_{\det^2} := (\Lambda^5 \mathbb{C}^5)^{\otimes 2}$ by $g \cdot \zeta = (\det g)^2 \zeta$. Put
$$
H := S(U(3) \times U(2)) = \left\{ \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} : A \in U(3),\; B \in U(2),\; \det A \det B = 1 \right\} \subset U(5).
$$

### Theorem 4 (Joint Stabilizer of Adjoint and Determinant-Square Data in $U(5)$)

Let $A_0 = a I_3 \oplus b I_2 \in \mathfrak{u}(5)_{\mathrm{sa}}$ with $a \neq b$, and let $0 \neq \zeta \in L_{\det^2}$.

1. **Exact quotient structure of $H$:** The homomorphism $\pi: SU(3) \times SU(2) \times U(1) \to H$ defined by
   $$
   \pi(U_3, U_2, z) := \begin{pmatrix} z^{-2} U_3 & 0 \\ 0 & z^3 U_2 \end{pmatrix}
   $$
   is surjective with cyclic kernel of order $6$ generated by $\gamma_6 := (e^{2\pi i/3} I_3,\, -I_2,\, e^{i\pi/3})$:
   $$
   \ker \pi = \{\gamma_6^k : k = 0,1,2,3,4,5\} \cong \mathbb{Z}_6, \qquad
   H \cong \frac{SU(3) \times SU(2) \times U(1)}{\mathbb{Z}_6}, \qquad
   \dim_{\mathbb{R}} \operatorname{Lie}(H) = 8 + 3 + 1 = 12.
   $$
2. **Exact joint stabilizer $K_{U(5)} = H\{\pm I_5\}$:** The stabilizer of $A_0$ in $U(5)$ is $\operatorname{Stab}_{U(5)}(A_0) = U(3) \times U(2)$ ($\dim_{\mathbb{R}} = 13$), and the joint stabilizer of $(A_0, \zeta)$ in $U(5)$ is
   $$
   K_{U(5)} := \operatorname{Stab}_{U(5)}(A_0, \zeta)
   = \left\{ \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \in U(3) \times U(2) : (\det A \det B)^2 = 1 \right\}
   = H\{\pm I_5\},
   $$
   which is the disjoint union of two connected components $H$ ($\det g = +1$) and $(-I_5)H$ ($\det g = -1$), with $H \cap \{\pm I_5\} = \{I_5\}$ and $K_{U(5)} \cong H \times \mathbb{Z}_2$.
3. **Fermion-even parity constraint:** Let $\mathfrak{A}$ be any CAR/link algebra on which the central element $-I_5 \in Z(U(5))$ acts by $(-1)^F$, where $F$ is the total fermion-letter parity. On the fermion-even subalgebra $\mathfrak{A}_{\mathrm{even}} = \{X \in \mathfrak{A} : (-1)^F X (-1)^F = X\}$, $-I_5$ acts as the identity. Consequently, for every tuple of fermion-even covariant elements $v$, $-I_5 \in \operatorname{Stab}_{U(5)}(v)$, so any fermion-even stabilizer containing $H$ necessarily contains $H\{\pm I_5\} = K_{U(5)}$.

#### Proof of Theorem 4

**(1)** For $(U_3, U_2, z) \in SU(3) \times SU(2) \times U(1)$, $\det(z^{-2} U_3)\det(z^3 U_2) = z^{-6}(1)\cdot z^6(1) = 1$, so $\pi$ maps into $H$. Given $A \oplus B \in H$, let $w = \det B = (\det A)^{-1} \in U(1)$ and choose $z \in U(1)$ with $z^6 = w$. Setting $U_3 = z^2 A$ and $U_2 = z^{-3} B$ gives $\det U_3 = z^6 \det A = w w^{-1} = 1$ and $\det U_2 = z^{-6}\det B = w^{-1} w = 1$, so $\pi(U_3, U_2, z) = A \oplus B$ and $\pi$ is surjective. Next, $(U_3, U_2, z) \in \ker \pi$ if and only if $U_3 = z^2 I_3$ and $U_2 = z^{-3} I_2$; unitarity of $\det U_3 = 1$ and $\det U_2 = 1$ forces $z^6 = 1$, so $z = e^{i\pi k/3}$ ($k \in \{0,\dots,5\}$), which gives $(U_3, U_2, z) = (e^{2\pi i k/3} I_3, (-1)^k I_2, e^{i\pi k/3}) = \gamma_6^k$.

**(2)** Since $a \neq b$, $g A_0 = A_0 g$ for $g = \begin{pmatrix} A & C \\ D & B \end{pmatrix} \in U(5)$ reads $a C = C b$ and $b D = D a$, forcing $C = 0$ and $D = 0$, so $\operatorname{Stab}_{U(5)}(A_0) = U(3) \times U(2)$. An element $g = A \oplus B \in U(3) \times U(2)$ fixes $\zeta \neq 0$ if and only if $(\det g)^2 = (\det A \det B)^2 = 1$, i.e., $\det g \in \{+1, -1\}$. If $\det g = +1$, then $g \in H$. If $\det g = -1$, then since $\det(-I_5) = (-1)^5 = -1$ and $-I_5 = (-I_3) \oplus (-I_2) \in Z(U(3) \times U(2))$, the product $(-I_5)g$ lies in $U(3) \times U(2)$ with $\det((-I_5)g) = (-1)(-1) = +1$, so $(-I_5)g \in H$ and $g \in (-I_5)H$. Because $\det(-I_5) = -1 \neq +1$, $-I_5 \notin H$, so $H \cap \{\pm I_5\} = \{I_5\}$ and $K_{U(5)} = H\{\pm I_5\} \cong H \times \mathbb{Z}_2$.

**(3)** The central element $-I_5 = e^{i\pi} I_5 \in U(5)$ acts on each fundamental creation/annihilation mode with phase $-1$, and therefore acts by conjugation on any monomial of $2m$ fermion letters by $(-1)^{2m} = +1$. Hence $-I_5$ fixes every element of $\mathfrak{A}_{\mathrm{even}}$ and every vector in any representation carried by $\mathfrak{A}_{\mathrm{even}}$. $\blacksquare$

---

## 5. Native Fermion-Even Five-Mode Determinant-Square Carrier on $\Lambda^5 \mathbb{C}^{10}$

Consider two adjacent lattice sites $x, y$ joined by a directed link $\ell = (x,y)$ in the five-mode unitary rishon model:
- Site $x$ carries five matter CAR modes $c_{x,1},\dots,c_{x,5}$, and site $y$ carries five matter CAR modes $c_{y,1},\dots,c_{y,5}$.
- Link $\ell = (x,y)$ carries five left-end rishon CAR modes $r_{x,1},\dots,r_{x,5}$ and five right-end rishon CAR modes $r_{y,1},\dots,r_{y,5}$ generating the ten-mode rishon Fock space $\Lambda(\mathbb{C}^{10})$. All twenty fermion modes $\{c_{x,i}, c_{y,i}, r_{x,i}, r_{y,i}\}_{i=1}^5$ mutually anticommute: $\{f_\alpha, f_\beta\} = 0$ and $\{f_\alpha, f_\beta^\dagger\} = \delta_{\alpha\beta} I$.
- The link Hilbert space is the half-filled five-rishon subspace
  $$
  \mathcal{H}_\ell := \Lambda^5 \mathbb{C}^{10} = \left\{\psi \in \Lambda(\mathbb{C}^{10}) : (N_{\ell,x} + N_{\ell,y})\psi = 5\psi\right\}, \qquad
  \dim \mathcal{H}_\ell = \binom{10}{5} = 252,
  $$
  where $N_{\ell,z} = \sum_{i=1}^5 r_{z,i}^\dagger r_{z,i}$ ($z \in \{x,y\}$).
- The $5 \times 5$ quantum-link operator matrix $U_\ell = (U_\ell^{ij})_{i,j=1}^5$ has entries
  $$
  U_\ell^{ij} := r_{y,i} r_{x,j}^\dagger \in \operatorname{End}(\Lambda^5 \mathbb{C}^{10}),
  $$
  which preserve $N_{\ell,x} + N_{\ell,y}$ because they annihilate one right-end rishon at $y$ and create one left-end rishon at $x$.
- For $z \in \{x,y\}$ and $1 \le i,j \le 5$, the local $\mathfrak{gl}(5)_z$ Gauss generators are
  $$
  G_z^{ij} := c_{z,i}^\dagger c_{z,j} + r_{z,i}^\dagger r_{z,j}, \qquad
  Q_z := \sum_{i=1}^5 G_z^{ii} = N_{z,\mathrm{matter}} + N_{\ell,z}.
  $$

### Theorem 5 (Native Fermion-Even Five-Mode Determinant-Square Carrier on $\Lambda^5 \mathbb{C}^{10}$)

Define the site five-fermion creation operators and the link five-rishon determinant operator
$$
B_x := c_{x,1}^\dagger c_{x,2}^\dagger c_{x,3}^\dagger c_{x,4}^\dagger c_{x,5}^\dagger, \qquad
B_y := c_{y,1}^\dagger c_{y,2}^\dagger c_{y,3}^\dagger c_{y,4}^\dagger c_{y,5}^\dagger,
$$
$$
D_{xy} := \left(r_{y,1} r_{y,2} r_{y,3} r_{y,4} r_{y,5}\right)\left(r_{x,5}^\dagger r_{x,4}^\dagger r_{x,3}^\dagger r_{x,2}^\dagger r_{x,1}^\dagger\right) \in \operatorname{End}(\Lambda^5 \mathbb{C}^{10}),
$$
and the two-site link-dressed composite
$$
\mathcal{O}_{xy}^{(10)} := B_x D_{xy} B_y.
$$

1. **Exact determinant-word factorization of $D_{xy}$ from the link matrix $U_\ell$:** For every five-tuple $(i_1, i_2, i_3, i_4, i_5) \in \{1,\dots,5\}^5$ and every five-tuple $(j_1, j_2, j_3, j_4, j_5) \in \{1,\dots,5\}^5$,
   $$
   U_\ell^{i_1, j_1} U_\ell^{i_2, j_2} U_\ell^{i_3, j_3} U_\ell^{i_4, j_4} U_\ell^{i_5, j_5}
   = \varepsilon_{i_1 i_2 i_3 i_4 i_5}\, \varepsilon_{j_1 j_2 j_3 j_4 j_5}\, D_{xy} \quad \text{in } \operatorname{End}(\Lambda^5 \mathbb{C}^{10}),
   $$
   where $\varepsilon_{i_1 i_2 i_3 i_4 i_5}$ is the five-index Levi-Civita symbol ($\varepsilon_{12345} = +1$, and $0$ if any two indices coincide). In particular,
   $$
   U_\ell^{1,1} U_\ell^{2,2} U_\ell^{3,3} U_\ell^{4,4} U_\ell^{5,5} = D_{xy}, \qquad
   \frac{1}{(5!)^2}\sum_{\pi, \sigma \in S_5} \operatorname{sgn}(\pi)\operatorname{sgn}(\sigma)\, U_\ell^{\pi(1),\sigma(1)}\cdots U_\ell^{\pi(5),\sigma(5)} = D_{xy}.
   $$
2. **Exact rank-one spectral action and norm on $\Lambda^5 \mathbb{C}^{10}$:** Let $|0_x, 5_y\rangle := r_{y,1}^\dagger\cdots r_{y,5}^\dagger |0\rangle_{\mathrm{link}} \in \Lambda^5 \mathbb{C}^{10}$ and $|5_x, 0_y\rangle := r_{x,1}^\dagger\cdots r_{x,5}^\dagger |0\rangle_{\mathrm{link}} \in \Lambda^5 \mathbb{C}^{10}$. Then on $\Lambda^5 \mathbb{C}^{10}$,
   $$
   D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y|, \qquad
   D_{xy}^\dagger D_{xy} = |0_x, 5_y\rangle\langle 0_x, 5_y|, \qquad
   D_{xy} D_{xy}^\dagger = |5_x, 0_y\rangle\langle 5_x, 0_y|,
   $$
   $$
   \operatorname{Tr}_{\Lambda^5 \mathbb{C}^{10}}\!\left(D_{xy}^\dagger D_{xy}\right) = 1, \qquad
   \|\mathcal{O}_{xy}^{(10)}\|_{\mathrm{op}} = 1.
   $$
3. **Fermion parity and exact $\mathfrak{gl}(5)_x \oplus \mathfrak{gl}(5)_y$ Gauss commutators:** $\mathcal{O}_{xy}^{(10)}$ has $5 + 10 + 5 = 20$ fermion letters (strictly fermion-even), preserves the link register $\Lambda^5 \mathbb{C}^{10}$, and satisfies for all $1 \le i,j \le 5$:
   $$
   \left[G_x^{ij},\, \mathcal{O}_{xy}^{(10)}\right] = 2\delta_{ij}\,\mathcal{O}_{xy}^{(10)}, \qquad
   \left[G_y^{ij},\, \mathcal{O}_{xy}^{(10)}\right] = 0.
   $$
   In particular, $[Q_x, \mathcal{O}_{xy}^{(10)}] = 10\,\mathcal{O}_{xy}^{(10)}$ and $[Q_y, \mathcal{O}_{xy}^{(10)}] = 0$, and under the local unitary gauge action $\alpha_{g_x, g_y} = \operatorname{Ad}(\Gamma(g_x) \otimes \Gamma(g_y))$ of $U(5)_x \times U(5)_y$,
   $$
   \alpha_{g_x, g_y}\!\left(\mathcal{O}_{xy}^{(10)}\right) = (\det g_x)^2\,\mathcal{O}_{xy}^{(10)}.
   $$
   Together with a local adjoint composite $A_x = \sum_{i,j=1}^5 (A_0)_{ij} c_{x,i}^\dagger c_{x,j}$ at site $x$ ($A_0 = a I_3 \oplus b I_2$, $a \neq b$), the pair $(A_x, \mathcal{O}_{xy}^{(10)})$ has local $U(5)_x \times U(5)_y$ stabilizer $K_{U(5),x} \times U(5)_y = (H\{\pm I_5\})_x \times U(5)_y$.

#### Proof of Theorem 5

**(1)** Because every left-end creator $r_{x,j}^\dagger$ anticommutes with every right-end annihilator $r_{y,i}$, moving the five $r_{y,i_k}$ factors to the left of the five $r_{x,j_k}^\dagger$ factors in
$$
U_\ell^{i_1,j_1} U_\ell^{i_2,j_2} U_\ell^{i_3,j_3} U_\ell^{i_4,j_4} U_\ell^{i_5,j_5}
= (r_{y,i_1} r_{x,j_1}^\dagger)(r_{y,i_2} r_{x,j_2}^\dagger)(r_{y,i_3} r_{x,j_3}^\dagger)(r_{y,i_4} r_{x,j_4}^\dagger)(r_{y,i_5} r_{x,j_5}^\dagger)
$$
requires $1 + 2 + 3 + 4 = 10$ pairwise anticommutations between $r_{x,\bullet}^\dagger$ and $r_{y,\bullet}$, producing the sign $(-1)^{10} = +1$:
$$
U_\ell^{i_1,j_1}\cdots U_\ell^{i_5,j_5}
= (r_{y,i_1} r_{y,i_2} r_{y,i_3} r_{y,i_4} r_{y,i_5})(r_{x,j_1}^\dagger r_{x,j_2}^\dagger r_{x,j_3}^\dagger r_{x,j_4}^\dagger r_{x,j_5}^\dagger).
$$
Now reversing the order of the five creators $r_{x,j_1}^\dagger \cdots r_{x,j_5}^\dagger$ to $r_{x,j_5}^\dagger \cdots r_{x,j_1}^\dagger$ requires $\binom{5}{2} = 10$ anticommutations, again giving $(-1)^{10} = +1$. By exterior-algebra antisymmetry $r_{y,i_1}\cdots r_{y,i_5} = \varepsilon_{i_1 i_2 i_3 i_4 i_5} r_{y,1}\cdots r_{y,5}$ and $r_{x,j_5}^\dagger\cdots r_{x,j_1}^\dagger = \varepsilon_{j_1 j_2 j_3 j_4 j_5} r_{x,5}^\dagger\cdots r_{x,1}^\dagger$, which establishes $U_\ell^{i_1,j_1}\cdots U_\ell^{i_5,j_5} = \varepsilon_{i_1\dots i_5}\varepsilon_{j_1\dots j_5} D_{xy}$.

**(2)** On the Fock basis of $\Lambda^5 \mathbb{C}^{10}$, the factor $r_{x,5}^\dagger\cdots r_{x,1}^\dagger$ annihilates any basis state containing at least one $x$-rishon, and on the unique five-rishon state $|0_x, 5_y\rangle = r_{y,1}^\dagger\cdots r_{y,5}^\dagger |0\rangle_{\mathrm{link}}$ with zero $x$-rishons, commuting the five $r_y$ annihilators past the five $r_x^\dagger$ creators uses $5 \times 5 = 25$ anticommutations (producing the sign $(-1)^{25} = -1$):
$$
D_{xy}|0_x, 5_y\rangle
= (-1)^{25} \left(r_{x,5}^\dagger\cdots r_{x,1}^\dagger\right)\left(r_{y,1}\cdots r_{y,5}\right) r_{y,1}^\dagger\cdots r_{y,5}^\dagger |0\rangle_{\mathrm{link}}.
$$
Reversing $r_{y,1}\cdots r_{y,5}$ to $r_{y,5}\cdots r_{y,1}$ uses $\binom{5}{2} = 10$ anticommutations (sign $(-1)^{10} = +1$), so $(r_{y,1}\cdots r_{y,5})(r_{y,1}^\dagger\cdots r_{y,5}^\dagger)|0\rangle_{\mathrm{link}} = (r_{y,5}\cdots r_{y,1})(r_{y,1}^\dagger\cdots r_{y,5}^\dagger)|0\rangle_{\mathrm{link}} = |0\rangle_{\mathrm{link}}$. Similarly, reversing $r_{x,5}^\dagger\cdots r_{x,1}^\dagger$ to $r_{x,1}^\dagger\cdots r_{x,5}^\dagger$ uses $\binom{5}{2} = 10$ anticommutations (sign $(-1)^{10} = +1$), giving $r_{x,5}^\dagger\cdots r_{x,1}^\dagger |0\rangle_{\mathrm{link}} = |5_x, 0_y\rangle$ and therefore
$$
D_{xy}|0_x, 5_y\rangle = -|5_x, 0_y\rangle.
$$
Thus $D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y|$, which is a rank-one partial isometry with $D_{xy}^\dagger D_{xy} = |0_x, 5_y\rangle\langle 0_x, 5_y|$, $D_{xy} D_{xy}^\dagger = |5_x, 0_y\rangle\langle 5_x, 0_y|$, and $\operatorname{Tr}_{\Lambda^5\mathbb{C}^{10}}(D_{xy}^\dagger D_{xy}) = 1$. Since $B_x$ and $B_y$ are partial isometries of norm $1$ on independent site Fock spaces, $\|\mathcal{O}_{xy}^{(10)}\|_{\mathrm{op}} = \|B_x\|_{\mathrm{op}}\|D_{xy}\|_{\mathrm{op}}\|B_y\|_{\mathrm{op}} = 1$.

**(3)** For any five-mode creation top form $B = f_1^\dagger f_2^\dagger f_3^\dagger f_4^\dagger f_5^\dagger$ and bilinear $E^{ij} = f_i^\dagger f_j$:
- If $i \neq j$, $f_j B = \pm \prod_{k \neq j} f_k^\dagger$ already contains $f_i^\dagger$, so $f_i^\dagger f_j B = 0$; likewise $B f_i^\dagger = 0$, so $[E^{ij}, B] = 0$.
- If $i = j$, $f_i^\dagger f_i B = B$ and $B f_i^\dagger f_i = 0$ (since $B f_i^\dagger = 0$), so $[E^{ii}, B] = B$.
Thus $[f_i^\dagger f_j, B] = \delta_{ij} B$, and taking the adjoint gives $[f_j^\dagger f_i, B^\dagger] = -\delta_{ij} B^\dagger$, i.e., $[f_i^\dagger f_j, f_1\cdots f_5] = -\delta_{ij}(f_1\cdots f_5)$. Applying this identity to $B_x = c_{x,1}^\dagger\cdots c_{x,5}^\dagger$, $B_y = c_{y,1}^\dagger\cdots c_{y,5}^\dagger$, $r_{x,5}^\dagger\cdots r_{x,1}^\dagger = r_{x,1}^\dagger\cdots r_{x,5}^\dagger$, and $r_{y,1}\cdots r_{y,5}$ yields:
$$
[c_{x,i}^\dagger c_{x,j}, B_x] = \delta_{ij} B_x, \qquad
[r_{x,i}^\dagger r_{x,j}, D_{xy}] = \delta_{ij} D_{xy},
$$
$$
[c_{y,i}^\dagger c_{y,j}, B_y] = \delta_{ij} B_y, \qquad
[r_{y,i}^\dagger r_{y,j}, D_{xy}] = -\delta_{ij} D_{xy}.
$$
Since $B_x, D_{xy}, B_y$ have even pairwise products ($B_x$ and $B_y$ have $5$ fermion letters each while $D_{xy}$ has $10$, and $G_z^{ij}$ has $2$ fermion letters and therefore commutes with fermion-odd operators on disjoint mode sets), the Leibniz rule for commutators gives
$$
\left[G_x^{ij},\, B_x D_{xy} B_y\right] = [c_{x,i}^\dagger c_{x,j}, B_x] D_{xy} B_y + B_x [r_{x,i}^\dagger r_{x,j}, D_{xy}] B_y = (\delta_{ij} + \delta_{ij}) B_x D_{xy} B_y = 2\delta_{ij}\,\mathcal{O}_{xy}^{(10)},
$$
$$
\left[G_y^{ij},\, B_x D_{xy} B_y\right] = B_x [r_{y,i}^\dagger r_{y,j}, D_{xy}] B_y + B_x D_{xy} [c_{y,i}^\dagger c_{y,j}, B_y] = (-\delta_{ij} + \delta_{ij}) B_x D_{xy} B_y = 0.
$$
Exponentiating $i\sum_{i,j} \Theta_{x,ij} G_x^{ij}$ and $i\sum_{i,j} \Theta_{y,ij} G_y^{ij}$ gives $\alpha_{g_x, g_y}(\mathcal{O}_{xy}^{(10)}) = e^{2 i \operatorname{Tr}(\Theta_x)} \mathcal{O}_{xy}^{(10)} = (\det g_x)^2 \mathcal{O}_{xy}^{(10)}$. By Theorem 4, combining $(A_x, \mathcal{O}_{xy}^{(10)})$ at site $x$ reduces $U(5)_x$ to $K_{U(5),x} = H\{\pm I_5\}$. $\blacksquare$

---

## 6. Global Quartic $\mathfrak{su}(5)$ Three-Plus-Two Orbit Selection via Cubic Discriminant

Let $\mathfrak{su}(5)_{\mathrm{sa}} := \{A \in M_5(\mathbb{C}) : A^* = A,\; \operatorname{Tr}(A) = 0\}$ be the $24$-dimensional space of traceless self-adjoint $5 \times 5$ matrices. For real parameters $\mu^2 > 0$, $\lambda_1 \in \mathbb{R}$, and $\lambda_2 > 0$, consider the general $U(5)$-invariant reflection-symmetric quartic potential
$$
V_{\mu, \lambda_1, \lambda_2}(A) := -\frac{\mu^2}{2}\operatorname{Tr}(A^2) + \frac{\lambda_1}{4}\left(\operatorname{Tr}(A^2)\right)^2 + \frac{\lambda_2}{4}\operatorname{Tr}(A^4).
$$

### Theorem 6 (Global Quartic $\mathfrak{su}(5)$ Three-Plus-Two Orbit Selection via Cubic Discriminant)

1. **Three-variable cubic discriminant identity:** For any $(x, y, z) \in \mathbb{R}^3$, let $\bar{x} := \frac{1}{3}(x + y + z)$ and set $u := x - \bar{x}$, $v := y - \bar{x}$, $w := z - \bar{x}$, so $u + v + w = 0$ and $r^2 := u^2 + v^2 + w^2 = (x^2 + y^2 + z^2) - 3\bar{x}^2 \ge 0$. Then
   $$
   u^4 + v^4 + w^4 = \frac{1}{2} r^4, \qquad
   x^4 + y^4 + z^4 = 3\bar{x}^4 + 6\bar{x}^2 r^2 + \frac{1}{2} r^4 + 12\bar{x}\, uvw,
   $$
   and the cubic discriminant satisfies the exact polynomial identity
   $$
   \Delta(u,v,w) := (u - v)^2(v - w)^2(w - u)^2 = \frac{1}{2} r^6 - 27(uvw)^2 \ge 0.
   $$
   Consequently, $|uvw| \le \frac{r^3}{3\sqrt{6}}$, with equality if and only if $(x - y)(y - z)(z - x) = 0$.
2. **Sharp fourth-moment bounds on $\mathfrak{su}(5)_{\mathrm{sa}}$:** For every $A \in \mathfrak{su}(5)_{\mathrm{sa}}$ with $s := \operatorname{Tr}(A^2) > 0$,
   $$
   \frac{7}{30} s^2 \le \operatorname{Tr}(A^4) \le \frac{13}{20} s^2.
   $$
   Equality on the lower bound $\operatorname{Tr}(A^4) = \frac{7}{30} s^2$ holds if and only if $A$ is unitarily conjugate to $\pm\sqrt{\frac{s}{30}}\operatorname{diag}(-2,-2,-2,3,3)$ (the three-plus-two orbit with stabilizer $S(U(3)\times U(2))$ in $SU(5)$). Equality on the upper bound $\operatorname{Tr}(A^4) = \frac{13}{20} s^2$ holds if and only if $A$ is unitarily conjugate to $\pm\sqrt{\frac{s}{20}}\operatorname{diag}(1,1,1,1,-4)$ (the four-plus-one orbit with stabilizer $S(U(4)\times U(1))$ in $SU(5)$).
3. **Exact global potential minimization:** Suppose $\mu^2 > 0$, $\lambda_2 > 0$, and $\kappa_{3+2} := \lambda_1 + \frac{7}{30}\lambda_2 > 0$. Put $s_* := \frac{\mu^2}{\kappa_{3+2}} = \frac{30\mu^2}{30\lambda_1 + 7\lambda_2}$ and $V_{\min}(3+2) := -\frac{\mu^4}{4\kappa_{3+2}} = -\frac{15\mu^4}{2(30\lambda_1 + 7\lambda_2)}$. Then for every $A \in \mathfrak{su}(5)_{\mathrm{sa}}$,
   $$
   V_{\mu, \lambda_1, \lambda_2}(A) - V_{\min}(3+2)
   = \frac{\kappa_{3+2}}{4}\left(\operatorname{Tr}(A^2) - s_*\right)^2
   + \frac{\lambda_2}{4}\left(\operatorname{Tr}(A^4) - \frac{7}{30}\left(\operatorname{Tr}(A^2)\right)^2\right) \ge 0,
   $$
   with $V_{\mu, \lambda_1, \lambda_2}(A) = V_{\min}(3+2)$ if and only if $A$ is unitarily conjugate to $\pm\sqrt{\frac{s_*}{30}}\operatorname{diag}(-2,-2,-2,3,3)$. On the four-plus-one and $(2,1,2)$ strata at optimal norm, the energy gaps above $V_{\min}(3+2)$ are strictly positive:
   $$
   \operatorname{Tr}(A_{4+1}^4) - \frac{7}{30} s^2 = \frac{5}{12} s^2 > 0, \qquad
   \operatorname{Tr}(A_{(2,1,2)}^4) - \frac{7}{30} s^2 = \frac{1}{60} s^2 > 0.
   $$

#### Proof of Theorem 6

**(1)** Since $u + v + w = 0$, $0 = (u + v + w)^2 = r^2 + 2(uv + vw + wu)$, so $e_2 := uv + vw + wu = -\frac{1}{2}r^2$. The monic polynomial with roots $u,v,w$ is $P(t) = (t - u)(t - v)(t - w) = t^3 + e_2 t - e_3 = t^3 - \frac{1}{2}r^2 t - uvw$. Summing $u^3 + v^3 + w^3 = \frac{1}{2}r^2(u + v + w) + 3 uvw = 3 uvw$ and $u^4 + v^4 + w^4 = \frac{1}{2}r^2(u^2 + v^2 + w^2) + uvw(u + v + w) = \frac{1}{2}r^4$ gives
$$
x^4 + y^4 + z^4 = 3\bar{x}^4 + 4\bar{x}^3(u+v+w) + 6\bar{x}^2(u^2+v^2+w^2) + 4\bar{x}(u^3+v^3+w^3) + (u^4+v^4+w^4) = 3\bar{x}^4 + 6\bar{x}^2 r^2 + \frac{1}{2}r^4 + 12\bar{x}\,uvw.
$$
By the discriminant formula for the depressed cubic $t^3 + p t + q$ ($\Delta = -4p^3 - 27q^2$) with $p = -\frac{1}{2}r^2$ and $q = -uvw$, we have $(u-v)^2(v-w)^2(w-u)^2 = \frac{1}{2}r^6 - 27(uvw)^2 \ge 0$, which proves $|uvw| \le \frac{r^3}{3\sqrt{6}}$ with equality if and only if two of $u,v,w$ (hence two of $x,y,z$) are equal.

**(2)** Since $A = A^*$, its eigenvalues $\lambda = (\lambda_1,\dots,\lambda_5) \in \mathbb{R}^5$ lie on the compact sphere $\mathcal{S}_s = \{\lambda \in \mathbb{R}^5 : \sum_{i=1}^5 \lambda_i = 0,\; \sum_{i=1}^5 \lambda_i^2 = s\}$, where the continuous function $f(\lambda) := \sum_{i=1}^5 \lambda_i^4$ attains its global minimum and maximum. Let $\lambda \in \mathcal{S}_s$ be a global extremizer of $f$ on $\mathcal{S}_s$. By part (1), for any three coordinates $(\lambda_i, \lambda_j, \lambda_k)$ with $\bar{x} = \frac{1}{3}(\lambda_i + \lambda_j + \lambda_k) \neq 0$, keeping the remaining two coordinates and $(\bar{x}, r^2)$ fixed varies $\lambda_i^4 + \lambda_j^4 + \lambda_k^4$ strictly monotonically with $uvw \in [-\frac{r^3}{3\sqrt{6}}, \frac{r^3}{3\sqrt{6}}]$, whose extreme values occur only when at least two of $(\lambda_i, \lambda_j, \lambda_k)$ are equal. Thus no three distinct values among $(\lambda_1,\dots,\lambda_5)$ can have a nonzero sum.
- If $\lambda$ had four or more distinct values $x_1 < x_2 < x_3 < x_4$, then $x_1 + x_2 + x_3 < x_1 + x_2 + x_4$ cannot both be zero, a contradiction.
- If $\lambda$ has three distinct values $x_1 < x_2 < x_3$, then $x_1 + x_2 + x_3 = 0$ is forced, so the remaining two coordinates $\lambda_4, \lambda_5 \in \{x_1, x_2, x_3\}$ satisfy $\lambda_4 + \lambda_5 = 0$, which forces $x_2 = 0$, $x_3 = -x_1 = c > 0$, and multiplicity pattern either $(2,1,2)$: $(-c,-c,0,c,c)$ with $s = 4c^2$ and $f = 4c^4 = \frac{1}{4}s^2 = \frac{15}{60}s^2$, or $(1,3,1)$: $(-c,0,0,0,c)$ with $s = 2c^2$ and $f = 2c^4 = \frac{1}{2}s^2 = \frac{30}{60}s^2$.
- If $\lambda$ has two distinct values $a \neq b$ ($s > 0$ excludes $a = b = 0$), the multiplicity pattern up to permutation and sign is either $(3,2)$: $(a,a,a,b,b)$ with $3a + 2b = 0$ and $3a^2 + 2b^2 = s$, giving $a = \mp 2\sqrt{s/30}$, $b = \pm 3\sqrt{s/30}$, and
  $$
  f_{3+2}(s) = 3a^4 + 2b^4 = (48 + 162)\frac{s^2}{900} = \frac{7}{30}s^2 = \frac{14}{60}s^2,
  $$
  or $(4,1)$: $(a,a,a,a,b)$ with $4a + b = 0$ and $4a^2 + b^2 = s$, giving $a = \pm\sqrt{s/20}$, $b = \mp 4\sqrt{s/20}$, and
  $$
  f_{4+1}(s) = 4a^4 + b^4 = (4 + 256)\frac{s^2}{400} = \frac{13}{20}s^2 = \frac{39}{60}s^2.
  $$
Since $\frac{14}{60}s^2 < \frac{15}{60}s^2 < \frac{30}{60}s^2 < \frac{39}{60}s^2$, the global minimum on $\mathcal{S}_s$ is uniquely $\frac{7}{30}s^2$ (attained exclusively on the $3+2$ orbit) and the global maximum is uniquely $\frac{13}{20}s^2$ (attained exclusively on the $4+1$ orbit).

**(3)** Writing $\operatorname{Tr}(A^4) = \frac{7}{30}s^2 + (\operatorname{Tr}(A^4) - \frac{7}{30}s^2)$ and completing the square in $s = \operatorname{Tr}(A^2)$ gives
$$
V_{\mu, \lambda_1, \lambda_2}(A)
= -\frac{\mu^2}{2} s + \frac{\kappa_{3+2}}{4} s^2 + \frac{\lambda_2}{4}\left(\operatorname{Tr}(A^4) - \frac{7}{30}s^2\right)
= V_{\min}(3+2) + \frac{\kappa_{3+2}}{4}(s - s_*)^2 + \frac{\lambda_2}{4}\left(\operatorname{Tr}(A^4) - \frac{7}{30}s^2\right).
$$
Since $\kappa_{3+2} > 0$ and $\lambda_2 > 0$, part (2) implies both terms are nonnegative and vanish simultaneously if and only if $s = s_*$ and $A$ lies in the $3+2$ orbit. $\blacksquare$

---

## 7. Joint Higgs Gram Matrix, Unbroken-Subalgebra Projector, and Noncommuting Pinch Identity

Equip $\mathfrak{u}(5)_{\mathrm{sa}} := \{X \in M_5(\mathbb{C}) : X^* = X\}$ ($\dim_{\mathbb{R}} = 25$) with the inner product $\langle X, Y \rangle := \operatorname{Tr}(X Y)$. For $A_0 = a I_3 \oplus b I_2 \in \mathfrak{u}(5)_{\mathrm{sa}}$ ($a \neq b$) and $0 \neq \zeta \in L_{\det^2}$ with $|\zeta| = \kappa > 0$, the infinitesimal gauge action of $X \in \mathfrak{u}(5)_{\mathrm{sa}}$ on $(A_0, \zeta)$ is
$$
\delta_X(A_0, \zeta) := \left(i[X, A_0],\; 2 i \operatorname{Tr}(X)\,\zeta\right).
$$
Define the Hermitian Higgs Gram (mass-squared) operator $\mathcal{M}^2: \mathfrak{u}(5)_{\mathrm{sa}} \to \mathfrak{u}(5)_{\mathrm{sa}}$ by
$$
\langle X,\, \mathcal{M}^2(Y)\rangle := \operatorname{Tr}\!\left((i[X, A_0])^*(i[Y, A_0])\right) + (2 i \operatorname{Tr}(X)\zeta)^*(2 i \operatorname{Tr}(Y)\zeta),
$$
so that for every $Y \in \mathfrak{u}(5)_{\mathrm{sa}}$,
$$
\mathcal{M}^2(Y) = [A_0, [A_0, Y]] + 4\kappa^2 \operatorname{Tr}(Y)\, I_5.
$$

### Theorem 7 (Joint Higgs Gram Matrix Spectrum, Unbroken-Subalgebra Projector, and Noncommuting Pinch Identity)

1. **Exact orthogonal spectral decomposition of $\mathcal{M}^2$ on $\mathfrak{u}(5)_{\mathrm{sa}}$:** The $25$-dimensional space $\mathfrak{u}(5)_{\mathrm{sa}}$ decomposes into three mutually orthogonal $\mathcal{M}^2$-eigenspaces:
   $$
   \mathfrak{u}(5)_{\mathrm{sa}} = \operatorname{Lie}(H) \oplus \mathfrak{m}_{3\times 2} \oplus \mathbb{R} T_0,
   $$
   where:
   - $\operatorname{Lie}(H) = \{X \in \mathfrak{u}(3)_{\mathrm{sa}} \oplus \mathfrak{u}(2)_{\mathrm{sa}} : \operatorname{Tr}(X) = 0\} \cong \mathfrak{su}(3) \oplus \mathfrak{su}(2) \oplus \mathfrak{u}(1)_Y$ has dimension $8 + 3 + 1 = 12$ and eigenvalue $0$ ($\ker \mathcal{M}^2 = \operatorname{Lie}(H) = \operatorname{Lie}(K_{U(5)})$);
   - $\mathfrak{m}_{3\times 2} = \left\{\begin{pmatrix} 0 & C \\ C^* & 0 \end{pmatrix} : C \in M_{3\times 2}(\mathbb{C})\right\}$ has real dimension $12$ and uniform positive eigenvalue $(a - b)^2 > 0$;
   - $\mathbb{R} T_0$ spanned by $T_0 := \frac{1}{\sqrt{5}}I_5$ has dimension $1$ and positive eigenvalue $20\kappa^2 > 0$.
   Consequently, $\operatorname{rank}(\mathcal{M}^2) = 13$, $\operatorname{Tr}_{\mathfrak{u}(5)_{\mathrm{sa}}}(\mathcal{M}^2) = 12(a - b)^2 + 20\kappa^2$, and $\det\nolimits_{\operatorname{Lie}(H)^\perp}(\mathcal{M}^2) = 20\kappa^2 (a - b)^{24} > 0$.
2. **Exact polynomial formula for the unbroken-subalgebra projector $\Pi_{\operatorname{Lie}(H)}$:** The orthogonal projection $\Pi_{\operatorname{Lie}(H)}: \mathfrak{u}(5)_{\mathrm{sa}} \to \operatorname{Lie}(H)$ is given identically by
   $$
   \Pi_{\operatorname{Lie}(H)}(X)
   = X - \frac{1}{(a - b)^2}[A_0, [A_0, X]] - \frac{1}{5}\operatorname{Tr}(X)\,I_5
   = P_3(A_0) X P_3(A_0) + P_2(A_0) X P_2(A_0) - \frac{1}{5}\operatorname{Tr}(X)\,I_5.
   $$
3. **Universal noncommuting pinch-commutator identity:** For any unital $*$-algebra $\mathcal{A}$, any elements $A, X \in \mathcal{A} \otimes M_5(\mathbb{C})$, and any $a \neq b$, let $P_3(A) = (A - b I_5)/(a - b)$, $P_2(A) = I_5 - P_3(A)$, and $D_A := P_3(A)^2 - P_3(A) = (A - a I_5)(A - b I_5)/(a - b)^2$. Then in $\mathcal{A} \otimes M_5(\mathbb{C})$:
   $$
   \left(P_3(A) X P_3(A) + P_2(A) X P_2(A)\right) - \left(X - \frac{1}{(a - b)^2}[A, [A, X]]\right) = D_A X + X D_A.
   $$

#### Proof of Theorem 7

**(1)** Write $Y = \begin{pmatrix} Y_{33} & C \\ C^* & Y_{22} \end{pmatrix} \in \mathfrak{u}(5)_{\mathrm{sa}}$. Then $[A_0, Y] = \begin{pmatrix} 0 & (a - b)C \\ (b - a)C^* & 0 \end{pmatrix}$ and $[A_0, [A_0, Y]] = (a - b)^2 \begin{pmatrix} 0 & C \\ C^* & 0 \end{pmatrix}$.
- If $Y \in \operatorname{Lie}(H)$, then $C = 0$ and $\operatorname{Tr}(Y) = 0$, so $\mathcal{M}^2(Y) = 0$.
- If $Y \in \mathfrak{m}_{3\times 2}$, then $Y_{33} = 0$, $Y_{22} = 0$, and $\operatorname{Tr}(Y) = 0$, so $\mathcal{M}^2(Y) = (a - b)^2 Y$.
- For $T_0 = \frac{1}{\sqrt{5}}I_5$, $[A_0, T_0] = 0$ and $\operatorname{Tr}(T_0) = \sqrt{5}$, so $\mathcal{M}^2(T_0) = 4\kappa^2(\sqrt{5})(\sqrt{5} T_0) = 20\kappa^2 T_0$.
Since $12 + 12 + 1 = 25$ and the three subspaces are mutually orthogonal under $\operatorname{Tr}(X Y)$, this exhausts $\mathfrak{u}(5)_{\mathrm{sa}}$ and proves $\ker \mathcal{M}^2 = \operatorname{Lie}(H)$.

**(2)** By the calculation in part (1), $X - (a - b)^{-2}[A_0, [A_0, X]] = \begin{pmatrix} X_{33} & 0 \\ 0 & X_{22} \end{pmatrix} = P_3(A_0) X P_3(A_0) + P_2(A_0) X P_2(A_0)$ removes the $\mathfrak{m}_{3\times 2}$ component, and subtracting $\frac{1}{5}\operatorname{Tr}(X)I_5 = \langle T_0, X\rangle T_0$ removes the $\mathbb{R} T_0$ component, leaving the orthogonal projection onto $\operatorname{Lie}(H)$.

**(3)** Since $A = (a - b)P_3(A) + b I_5$, we have $[A, X] = (a - b)[P_3(A), X]$ and
$$
\frac{1}{(a - b)^2}[A, [A, X]] = [P_3(A), [P_3(A), X]] = P_3(A)^2 X - 2 P_3(A) X P_3(A) + X P_3(A)^2.
$$
On the other hand, expanding $P_2(A) = I_5 - P_3(A)$ gives
$$
P_3(A) X P_3(A) + P_2(A) X P_2(A) = X - P_3(A) X - X P_3(A) + 2 P_3(A) X P_3(A).
$$
Subtracting $X - (a - b)^{-2}[A, [A, X]]$ cancels $X$ and $2 P_3(A) X P_3(A)$, yielding $(P_3(A)^2 - P_3(A))X + X(P_3(A)^2 - P_3(A)) = D_A X + X D_A$. $\blacksquare$

---

## 8. Single-Link Two-Sided Transport Floor and Multi-Copy Coherent FMS Defect Scaling

### Theorem 8 (Single-Link Two-Sided Transport Floor and Multi-Copy Coherent FMS Defect Scaling)

1. **Exact single-link two-sided transport defect identity on $\Lambda^5 \mathbb{C}^{10}$:** Let $D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y| \in \operatorname{End}(\Lambda^5 \mathbb{C}^{10})$ be the five-rishon determinant operator of Theorem 5, and for any scalar $\gamma \in \mathbb{C}$ put $T(\gamma) := \gamma D_{xy}$. Let $P_0 := |0_x, 5_y\rangle\langle 0_x, 5_y|$ and $P_5 := |5_x, 0_y\rangle\langle 5_x, 0_y|$. For every state $\omega$ on $\operatorname{End}(\Lambda^5 \mathbb{C}^{10})$, let $p_0 := \omega(P_0) \ge 0$ and $p_5 := \omega(P_5) \ge 0$ (so $p_0 + p_5 \le 1$). Then the two-sided transport defects $D_+(\omega; \gamma) := \omega((T(\gamma)^\dagger T(\gamma) - I)^2)$ and $D_-(\omega; \gamma) := \omega((T(\gamma) T(\gamma)^\dagger - I)^2)$ satisfy the exact identity
   $$
   D_+(\omega; \gamma) + D_-(\omega; \gamma)
   = 2 - (p_0 + p_5) + \left(|\gamma|^2 - 1\right)^2 (p_0 + p_5) \ge 2 - (p_0 + p_5) \ge 1,
   $$
   with $D_+(\omega; \gamma) + D_-(\omega; \gamma) = 1$ if and only if $p_0 + p_5 = 1$ and $|\gamma| = 1$.
2. **Exact multi-copy coherent FMS defect scaling:** For each integer $K \ge 1$, let $\mathcal{H}_K := (\mathbb{C}^2)^{\otimes K}$ carry the $K$-copy symmetric Pauli composites $\Phi_K^a := \frac{1}{K}\sum_{\nu=1}^K \sigma_a^{(\nu)}$ ($a \in \{1,2,3\}$) and the product coherent state $|\psi_K\rangle := |+\rangle^{\otimes K}$ ($\sigma_3|+\rangle = |+\rangle$), with state $\omega_K(X) := \langle \psi_K, X \psi_K\rangle$. Then:
   - $|\psi_K\rangle$ is an exact eigenvector of the Casimir operator $\sum_{a=1}^3 (\Phi_K^a)^2$:
     $$
     \left(\sum_{a=1}^3 (\Phi_K^a)^2\right)|\psi_K\rangle = \left(1 + \frac{2}{K}\right)|\psi_K\rangle,
     $$
     and the commutator square sum satisfies
     $$
     \sum_{a,b=1}^3 \omega_K\!\left(|[\Phi_K^a, \Phi_K^b]|^2\right) = \frac{8(K + 2)}{K^3}.
     $$
   - Consequently, by Theorem 1(2), the $SU(2)$ adjoint projector $P_\pm(r) = \frac{1}{2}(I \pm r^{-1}\sum_{a=1}^3 \Phi_K^a \otimes \sigma_a)$ has exact rational state-$L^2$ idempotence defect
     $$
     \omega_K\!\left(|P_\pm(1)^2 - P_\pm(1)|_{\mathrm{HS}}^2\right) = \frac{K + 1}{K^3} \quad (r = 1), \qquad
     \omega_K\!\left(|P_\pm(r_K)^2 - P_\pm(r_K)|_{\mathrm{HS}}^2\right) = \frac{1}{2 K(K + 2)} \quad \left(r_K = \sqrt{1 + \frac{2}{K}}\right).
     $$
   - For the $K$-copy link space $(\Lambda^5 \mathbb{C}^{10})^{\otimes K}$ carrying the symmetric determinant average $\widehat{D}_K := \frac{2}{K}\sum_{\nu=1}^K D_{xy}^{(\nu)}$ and the coherent product state $|\Theta_K\rangle := |\theta\rangle^{\otimes K}$ with $|\theta\rangle := \frac{1}{\sqrt{2}}(|0_x, 5_y\rangle - |5_x, 0_y\rangle)$ and $\varpi_K(X) := \langle \Theta_K, X \Theta_K\rangle$, we have
     $$
     \varpi_K\!\left((\widehat{D}_K - I)^\dagger(\widehat{D}_K - I)\right)
     = \varpi_K\!\left((\widehat{D}_K^\dagger - I)^\dagger(\widehat{D}_K^\dagger - I)\right)
     = \frac{1}{K},
     $$
     $$
     \varpi_K\!\left(\left(\widehat{D}_K^\dagger \widehat{D}_K - I\right)^2\right)
     = \varpi_K\!\left(\left(\widehat{D}_K \widehat{D}_K^\dagger - I\right)^2\right)
     = \frac{3K + 2}{K^3}.
     $$
     In particular, the two-sided transport defect sum $\frac{2(3K+2)}{K^3}$ equals $10 \ge 1$ at $K = 1$ (consistent with part (1) at $\gamma = 2$, $p_0 = p_5 = \frac{1}{2}$), drops strictly below the single-link floor $1$ at $K = 3$ ($\frac{22}{27} < 1$), and vanishes at rate $O(1/K^2)$ as $K \to \infty$.

#### Proof of Theorem 8

**(1)** By Theorem 5(2), $D_{xy}^\dagger D_{xy} = P_0$ and $D_{xy} D_{xy}^\dagger = P_5$ are orthogonal rank-one projections ($P_0^2 = P_0$, $P_5^2 = P_5$, $P_0 P_5 = 0$). For $T(\gamma) = \gamma D_{xy}$, $T(\gamma)^\dagger T(\gamma) - I = (|\gamma|^2 - 1)P_0 - (I - P_0)$. Since $P_0(I - P_0) = 0$, squaring gives
$$
(T(\gamma)^\dagger T(\gamma) - I)^2 = (|\gamma|^2 - 1)^2 P_0 + (I - P_0), \qquad
(T(\gamma) T(\gamma)^\dagger - I)^2 = (|\gamma|^2 - 1)^2 P_5 + (I - P_5).
$$
Taking $\omega$ and summing yields $D_+(\omega; \gamma) + D_-(\omega; \gamma) = (1 - p_0) + (1 - p_5) + (|\gamma|^2 - 1)^2(p_0 + p_5) = 2 - (p_0 + p_5) + (|\gamma|^2 - 1)^2(p_0 + p_5)$. Since $P_0 + P_5 \le I$, $p_0 + p_5 = \omega(P_0 + P_5) \le 1$, so $2 - (p_0 + p_5) \ge 1$.

**(2)** Since $\sigma_3|+\rangle = |+\rangle$, $\Phi_K^3|\psi_K\rangle = |\psi_K\rangle$ and $(\Phi_K^3)^2|\psi_K\rangle = |\psi_K\rangle$. Because $(\sigma_1 + i\sigma_2)|+\rangle = 0$, we have $\sigma_2|+\rangle = i\sigma_1|+\rangle$. Hence for every pair $\nu \neq \mu$,
$$
\left(\sigma_1^{(\nu)}\sigma_1^{(\mu)} + \sigma_2^{(\nu)}\sigma_2^{(\mu)}\right)|\psi_K\rangle
= (1 + i^2)\sigma_1^{(\nu)}\sigma_1^{(\mu)}|\psi_K\rangle = 0.
$$
Using $(\sigma_a^{(\nu)})^2 = I$, we obtain
$$
\left((\Phi_K^1)^2 + (\Phi_K^2)^2\right)|\psi_K\rangle
= \frac{1}{K^2}\sum_{\nu=1}^K \left((\sigma_1^{(\nu)})^2 + (\sigma_2^{(\nu)})^2\right)|\psi_K\rangle
= \frac{2}{K}|\psi_K\rangle,
$$
so $\left(\sum_{a=1}^3 (\Phi_K^a)^2\right)|\psi_K\rangle = (1 + \frac{2}{K})|\psi_K\rangle$. Next, $[\Phi_K^a, \Phi_K^b] = \frac{1}{K^2}\sum_{\nu=1}^K [\sigma_a^{(\nu)}, \sigma_b^{(\nu)}] = \frac{2i}{K}\sum_{c=1}^3 \varepsilon_{abc}\Phi_K^c$. Therefore,
$$
\sum_{a,b=1}^3 |[\Phi_K^a, \Phi_K^b]|^2
= \frac{4}{K^2}\sum_{a,b,c=1}^3 \varepsilon_{abc}^2 (\Phi_K^c)^2
= \frac{8}{K^2}\sum_{c=1}^3 (\Phi_K^c)^2,
$$
whose $\omega_K$-expectation is $\frac{8}{K^2}(1 + \frac{2}{K}) = \frac{8(K + 2)}{K^3}$. Substituting $\omega_K(R_1^2) = (\frac{2}{K})^2 = \frac{4}{K^2}$ at $r = 1$ and $\omega_K(R_{r_K}^2) = 0$ at $r_K^2 = 1 + \frac{2}{K}$ into Theorem 1(2) gives
$$
\omega_K\!\left(|P_\pm(1)^2 - P_\pm(1)|_{\mathrm{HS}}^2\right)
= \frac{1}{8}\cdot\frac{4}{K^2} + \frac{1}{16}\cdot\frac{8(K+2)}{K^3}
= \frac{K + 1}{K^3},
$$
$$
\omega_K\!\left(|P_\pm(r_K)^2 - P_\pm(r_K)|_{\mathrm{HS}}^2\right)
= 0 + \frac{1}{16(1 + 2/K)^2}\cdot\frac{8(K+2)}{K^3}
= \frac{1}{2 K(K + 2)}.
$$
Finally, on each copy of $\Lambda^5 \mathbb{C}^{10}$, let $|\theta_\perp\rangle := \frac{1}{\sqrt{2}}(|0_x, 5_y\rangle + |5_x, 0_y\rangle)$, which is orthogonal to $|\theta\rangle$. Direct action of $D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y|$ and $D_{xy}^\dagger = -|0_x, 5_y\rangle\langle 5_x, 0_y|$ gives $2 D_{xy}|\theta\rangle = |\theta\rangle - |\theta_\perp\rangle$, $2 D_{xy}^\dagger|\theta\rangle = |\theta\rangle + |\theta_\perp\rangle$, and $2 D_{xy}^\dagger|\theta_\perp\rangle = -(|\theta\rangle + |\theta_\perp\rangle)$. Writing $|\theta_\perp^{(\nu)}\rangle$ and $|\theta_\perp^{(\mu,\nu)}\rangle$ ($\mu < \nu$) for the mutually orthonormal $K$-copy product states with $|\theta_\perp\rangle$ in slot $\nu$ (respectively slots $\mu,\nu$) and $|\theta\rangle$ elsewhere, we obtain
$$
(\widehat{D}_K - I)|\Theta_K\rangle = -\frac{1}{K}\sum_{\nu=1}^K |\theta_\perp^{(\nu)}\rangle, \qquad
(\widehat{D}_K^\dagger - I)|\Theta_K\rangle = \frac{1}{K}\sum_{\nu=1}^K |\theta_\perp^{(\nu)}\rangle,
$$
both of norm squared $K(1/K^2) = 1/K$, and
$$
\left(\widehat{D}_K^\dagger \widehat{D}_K - I\right)|\Theta_K\rangle
= \frac{1}{K}|\Theta_K\rangle + \frac{2}{K^2}\sum_{\nu=1}^K |\theta_\perp^{(\nu)}\rangle - \frac{2}{K^2}\sum_{1 \le \mu < \nu \le K} |\theta_\perp^{(\mu,\nu)}\rangle.
$$
By mutual orthonormality of $|\Theta_K\rangle$, $\{|\theta_\perp^{(\nu)}\rangle\}$, and $\{|\theta_\perp^{(\mu,\nu)}\rangle\}$, the squared norm is $(1/K)^2 + K(2/K^2)^2 + \binom{K}{2}(-2/K^2)^2 = \frac{3K + 2}{K^3}$, and the same holds for $(\widehat{D}_K \widehat{D}_K^\dagger - I)|\Theta_K\rangle$ by exchanging $|\theta_\perp\rangle \mapsto -|\theta_\perp\rangle$. $\blacksquare$

---

## 9. Paired Runner Verification Summary

The primary runner [`scripts/frontier_u5_three_plus_two_fms_projector_carrier.py`](../scripts/frontier_u5_three_plus_two_fms_projector_carrier.py) verifies every identity in Theorems 1–8 with exact rational (`fractions.Fraction`) and integer Fock-space arithmetic:

1. **Theorem 1 controls:** Exact operator verification of $P_\pm^2 - P_\pm = \frac{1}{4r^2}(A^2 - r^2 I_{\mathcal{A}} \otimes I_2)$, the internal Hilbert-Schmidt decomposition $|A^2 - r^2 I|_{\mathrm{HS}}^2 = 2 R_r^2 + \sum_{a,b} |[\Phi^a, \Phi^b]|^2$, the state-$L^2$ equality across mixed states $\omega$, and exact $SU(2)_X \times SU(2)_Y$ invariance and four-channel completeness of $\mathcal{S}_{s,s'}(X,Y)$ with non-unitary quantum-link transporters $\mathcal{U}_{XY}$.
2. **Theorem 2 controls:** Exact operator verification of $P_3(A)^2 - P_3(A) = (A - a I_5)(A - b I_5)/(a - b)^2$ and internal trace formulas; exact $32$-dimensional Fock-space construction of the five-mode CAR algebra $\Lambda(\mathbb{C}^5)$ verifying $C^2 = (6 I - N)C$ on all $32$ Fock states and the exact idempotence $(P_{\mathrm{CAR}}^{(n)})^2 = P_{\mathrm{CAR}}^{(n)}$ and internal trace $\operatorname{Tr}_{M_5}(P_{\mathrm{CAR}}^{(n)}) = \frac{n}{6-n} I$ across all sectors $n \in \{1,2,3,4,5\}$; and exact verification of the rank-separation witness $A_{\mathrm{mix}} = (A_{(4)}, A_{(2)})$ and joint certification functional $\mathcal{D}_{3+2}(A_{(k)}) = (k - 3)^2$.
3. **Theorem 3 controls:** Exact rational $10 \times 10$ and operator-valued verification of $Q_6(A)^2 - Q_6(A)$, $[A, Q_6(A)] = 0$, the polynomial factorizations of $J_A^2 + I_{10}$ and $A - (a Q_6(A) + b Q_4(A)) J_A$, and exact rank/nullity computation over the $45$-dimensional basis of $\mathfrak{so}(10)$ confirming $\dim \mathfrak{c}_{\mathrm{real}} = 21$ and $\dim \mathfrak{c}_{\mathrm{unitary}} = 13$.
4. **Theorem 4 controls:** Exact arithmetic verification of the homomorphism $\pi: SU(3) \times SU(2) \times U(1) \to S(U(3) \times U(2))$, its order-$6$ cyclic kernel $\ker \pi = \{\gamma_6^k : k = 0,\dots,5\}$, the $13 \to 12$ Lie-algebra dimension reduction, and the two-component stabilizer $K_{U(5)} = H\{\pm I_5\}$.
5. **Theorem 5 controls:** Exact $252 \times 252$ Fock-space construction on $\Lambda^5 \mathbb{C}^{10}$ of all $25$ link operators $U_\ell^{ij} = r_{y,i} r_{x,j}^\dagger$ and $D_{xy}$, verifying $U_\ell^{i_1,j_1}\cdots U_\ell^{i_5,j_5} = \varepsilon_{i_1\dots i_5}\varepsilon_{j_1\dots j_5} D_{xy}$ across all $120$ permutations and repeated-index tuples, $D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y|$, $\operatorname{Tr}_{\Lambda^5\mathbb{C}^{10}}(D_{xy}^\dagger D_{xy}) = 1$, and exact two-site-plus-link verification of $[G_x^{ij}, \mathcal{O}_{xy}^{(10)}] = 2\delta_{ij}\mathcal{O}_{xy}^{(10)}$ and $[G_y^{ij}, \mathcal{O}_{xy}^{(10)}] = 0$ for all $25$ generators at each endpoint.
6. **Theorem 6 controls:** Exact rational verification of the three-variable cubic discriminant identity $\Delta(u,v,w) = \frac{1}{2}r^6 - 27(uvw)^2 = (u-v)^2(v-w)^2(w-u)^2$, the sharp fourth-moment ratios $\frac{7}{30}s^2 < \frac{1}{4}s^2 < \frac{1}{2}s^2 < \frac{13}{20}s^2$ across all symmetry strata and off-stratum perturbations in $\mathfrak{su}(5)_{\mathrm{sa}}$, and the exact square-completed potential decomposition $V_{\mu,\lambda_1,\lambda_2}(A) - V_{\min}(3+2)$.
7. **Theorem 7 controls:** Exact construction of the $25 \times 25$ Gram matrix $\mathcal{M}^2$ on a complete basis of $\mathfrak{u}(5)_{\mathrm{sa}}$, verifying $\dim \ker \mathcal{M}^2 = 12$ ($\operatorname{Lie}(H)$), eigenvalue $(a-b)^2$ with multiplicity $12$ on $\mathfrak{m}_{3\times 2}$, eigenvalue $20\kappa^2$ with multiplicity $1$ on $T_0$, the exact polynomial projector $\Pi_{\operatorname{Lie}(H)}$, and the noncommuting pinch-commutator identity $(P_3(A)X P_3(A) + P_2(A)X P_2(A)) - (X - (a-b)^{-2}[A,[A,X]]) = D_A X + X D_A$ on noncommuting operator matrices.
8. **Theorem 8 controls:** Exact verification on $\Lambda^5 \mathbb{C}^{10}$ of $D_+(\omega;\gamma) + D_-(\omega;\gamma) = 2 - (p_0 + p_5) + (|\gamma|^2 - 1)^2(p_0 + p_5) \ge 1$, and exact Fock/tensor construction on $\mathcal{H}_K = (\mathbb{C}^2)^{\otimes K}$ ($K = 1, 2, 3, 4$) verifying $(\sum_a (\Phi_K^a)^2)|\psi_K\rangle = (1 + 2/K)|\psi_K\rangle$, $\omega_K(|P_\pm(1)^2 - P_\pm(1)|_{\mathrm{HS}}^2) = \frac{K+1}{K^3}$, $\omega_K(|P_\pm(r_K)^2 - P_\pm(r_K)|_{\mathrm{HS}}^2) = \frac{1}{2K(K+2)}$, and $\varpi_K((\widehat{D}_K^\dagger \widehat{D}_K - I)^2) = \varpi_K((\widehat{D}_K \widehat{D}_K^\dagger - I)^2) = \frac{3K+2}{K^3}$.
