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
claim_type_reason: "Self-contained operator-algebraic and representation-theoretic theorems establishing exact noncommuting Fröhlich-Morchio-Strocchi projector defect decompositions for SU(2), U(5), and Spin(10)/so(10), the exact joint stabilizer K_{U(5)} = S(U(3)xU(2)){+-I_5}, and the nonvanishing fermion-even two-site determinant-square carrier on the five-mode rishon link register Lambda^5(C^10), without claiming dynamical vacuum selection or an infrared mass gap."
target_claim_id: null
target_blocker_text: "Establish exact noncommuting Fröhlich-Morchio-Strocchi projector defect identities across SU(2), U(5), and Spin(10)/so(10), prove the rank-three certification requirement separating noncommuting idempotence from multiplicity selection, and construct an explicit fermion-even native carrier on the five-mode rishon link register realizing the full three-plus-two stabilizer S(U(3)xU(2)){+-I_5}."
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: "Couple the native three-plus-two projector strings and two-site determinant-square carrier to a stationary state construction to bound the orbit defect, commutator defect, and two-sided transport defect in a single state."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## 0. Scope, Premise Provenance, and Obligation Graph

This note is self-contained on `main` and relies on no unlanded branch or external file. It proves five algebraic and operator-theoretic results for gauge-invariant Fröhlich-Morchio-Strocchi (FMS) channel resolution and stabilizer realization in the $SU(2)$, $U(5)$, and $\mathrm{Spin}(10)/\mathfrak{so}(10)$ three-plus-two settings:

1. **Theorem 1 (Noncommuting $SU(2)$ Adjoint Projector Defect Identity and State-$L^2$ Equality):** For any unital $*$-algebra $\mathcal{A}$, any self-adjoint triple $\Phi = (\Phi^1, \Phi^2, \Phi^3) \in (\mathcal{A}_{\mathrm{sa}})^3$, and any scale $r > 0$, the local projectors $P_\pm = \frac{1}{2}(I_{\mathcal{A}} \otimes I_2 \pm r^{-1}\sum_{a=1}^3 \Phi^a \otimes \sigma_a)$ satisfy an exact internal Hilbert-Schmidt equality separating the radial orbit defect from the noncommuting commutator defect with zero cross term. Local gauge covariance implies that the four projected two-end strings $\mathcal{S}_{s,s'}(X,Y) = \Psi_X^* P_s(\Phi_X)\mathcal{U}_{XY}P_{s'}(\Phi_Y)\Psi_Y$ are strictly gauge-invariant for any bi-covariant transporter $\mathcal{U}_{XY}$ (without assuming $\mathcal{U}_{XY}$ is unitary) and sum to $\Psi_X^* \mathcal{U}_{XY} \Psi_Y$.
2. **Theorem 2 ($U(5)$ Three-Plus-Two Adjoint Projector Calculus, Fermionic Bilinear Identity, and Rank-Separation Certification):** For $A = A^* \in \mathcal{A} \otimes M_5(\mathbb{C})$ and distinct real target eigenvalues $a \neq b$, the linear Lagrange projectors $P_3(A) = (A - b I_5)/(a - b)$ and $P_2(A) = (a I_5 - A)/(a - b)$ satisfy $P_3(A)^2 - P_3(A) = (A - a I_5)(A - b I_5)/(a - b)^2$ and $\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}} = (\operatorname{Tr}_{M_5}(A) - (3a + 2b)I_{\mathcal{A}})/(a - b)$. On the five-flavor canonical anticommutation relation (CAR) algebra $\Lambda(\mathbb{C}^5)$, the fundamental bilinear matrix $C_{ik} = c_i^\dagger c_k$ satisfies the exact noncommuting quadratic identity $C^2 = (6 - n)C$ on each $n$-fermion sector $\Lambda^n \mathbb{C}^5$, so $P_{\mathrm{CAR}} = (6 - n)^{-1}C$ ($1 \le n \le 5$) is an exact idempotent ($P_{\mathrm{CAR}}^2 = P_{\mathrm{CAR}}$) whose internal trace is $\frac{n}{6-n} I_{\Lambda^n\mathbb{C}^5}$ (non-integer at $n = 2$). Moreover, an explicit state witness on $A_{(4)} \oplus A_{(2)}$ shows that vanishing quadratic defect $P_3(A)^2 - P_3(A) = 0$ and vanishing mean trace defect $\omega(\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}}) = 0$ still allow zero weight on the rank-three stratum unless the trace-variance defect $\omega((\operatorname{Tr}_{M_5}(P_3(A)) - 3 I_{\mathcal{A}})^2)$ is also controlled.
3. **Theorem 3 (Orthogonal Real Six-Plus-Four Projectors and Complex-Structure Defect Factorization):** For any skew-adjoint operator $A = -A^* \in \mathcal{A} \otimes M_{10}(\mathbb{R})$ and real parameters $a, b \neq 0$ with $a^2 \neq b^2$, the real block projectors $Q_6(A) = (-A^2 - b^2 I_{10})/(a^2 - b^2)$ and $Q_4(A) = I_{10} - Q_6(A)$ commute identically with $A$, and the candidate complex structure $J_A = A(a^{-1}Q_6(A) + b^{-1}Q_4(A))$ satisfies the exact polynomial factorizations
   $$J_A^2 + I_{10} = \frac{(a - b)^2 A^2 + (a^2 - b^2)^2 I_{10}}{a^2 b^2}\,(Q_6(A)^2 - Q_6(A)), \qquad A - (a Q_6(A) + b Q_4(A))J_A = \frac{(a - b)^2}{ab}\,A\,(Q_6(A)^2 - Q_6(A)).$$
   In $\mathfrak{so}(10)$ ($\dim = 45$), the real projector $Q_6(A_0)$ alone has centralizer $\mathfrak{so}(6) \oplus \mathfrak{so}(4)$ of dimension $21$, whereas adjoining $J_{A_0}$ reduces the centralizer to $\mathfrak{u}(3) \oplus \mathfrak{u}(2)$ of dimension $13$.
4. **Theorem 4 (Joint Stabilizer of Adjoint and Determinant-Square Data in $U(5)$):** For $A_0 = a I_3 \oplus b I_2$ ($a \neq b$) and $0 \neq \zeta \in (\det \mathbb{C}^5)^{\otimes 2}$ carrying $g \cdot \zeta = (\det g)^2 \zeta$, the joint stabilizer in $U(5)$ is $K_{U(5)} = \{A \oplus B \in U(3)\times U(2) : (\det A \det B)^2 = 1\} = H\{\pm I_5\}$, where $H = S(U(3)\times U(2)) \cong (SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6$ has Lie algebra of dimension $12$. Because $-I_5$ acts trivially on every fermion-even operator, $K_{U(5)} = H\{\pm I_5\}$ is the minimal subgroup of $U(5)$ containing $H$ that can arise as the stabilizer of fermion-even composites.
5. **Theorem 5 (Native Fermion-Even Five-Mode Determinant-Square Carrier on $\Lambda^5 \mathbb{C}^{10}$):** On a single link $\ell = (x,y)$ with five matter CAR modes per site and the half-filled ten-mode rishon link register $\mathcal{H}_\ell = \Lambda^5 \mathbb{C}^{10}$ ($\dim \mathcal{H}_\ell = \binom{10}{5} = 252$) with link matrix entries $U_\ell^{ij} = r_{y,i} r_{x,j}^\dagger$, the five-rishon transfer operator $D_{xy} = (r_{y,1}\cdots r_{y,5})(r_{x,5}^\dagger\cdots r_{x,1}^\dagger)$ satisfies the exact determinant identity $U_\ell^{i_1,1}\cdots U_\ell^{i_5,5} = \operatorname{sgn}(i_1,\dots,i_5)D_{xy}$ and $\operatorname{Tr}_{\Lambda^5\mathbb{C}^{10}}(D_{xy}^\dagger D_{xy}) = 1$. Dressed with the five-fermion site creations $B_x = c_{x,1}^\dagger\cdots c_{x,5}^\dagger$ and $B_y = c_{y,1}^\dagger\cdots c_{y,5}^\dagger$, the composite $\mathcal{O}_{xy}^{(10)} = B_x D_{xy} B_y$ is nonzero ($\|\mathcal{O}_{xy}^{(10)}\|_{\mathrm{op}} = 1$), fermion-even ($20$ fermion letters), commutes with all $25$ local $\mathfrak{gl}(5)_y$ Gauss generators $[G_y^{ij}, \mathcal{O}_{xy}^{(10)}] = 0$, and satisfies $[G_x^{ij}, \mathcal{O}_{xy}^{(10)}] = 2\delta_{ij}\mathcal{O}_{xy}^{(10)}$ for all $1 \le i,j \le 5$, thereby realizing the exact representation $(\det g_x)^2 \otimes 1_y$ of $U(5)_x \times U(5)_y$.

| Obligation item | Status in this note | Exact scope |
|---|---|---|
| Noncommuting $SU(2)$ adjoint projector defect and state-$L^2$ equality | Proved here (Theorem 1) | Any unital $*$-algebra $\mathcal{A}$, self-adjoint triple $\Phi^a$, scale $r > 0$, and state $\omega$ |
| $U(5)$ $3+2$ linear projector defect, CAR bilinear identity $C^2 = (6-n)C$, and rank-three certification | Proved here (Theorem 2) | Self-adjoint $A \in \mathcal{A} \otimes M_5(\mathbb{C})$, $a \neq b$, and five-mode CAR sectors $\Lambda^n \mathbb{C}^5$ |
| Orthogonal real $6+4$ projector and complex-structure polynomial factorization | Proved here (Theorem 3) | Skew-adjoint $A \in \mathcal{A} \otimes M_{10}(\mathbb{R})$, $a,b \neq 0$, $a^2 \neq b^2$ |
| Joint stabilizer $K_{U(5)} = H\{\pm I_5\}$ and $H \cong (SU(3)\times SU(2)\times U(1))/\mathbb{Z}_6$ | Proved here (Theorem 4) | $A_0 = a I_3 \oplus b I_2$ ($a \neq b$) and $0 \neq \zeta \in (\det \mathbb{C}^5)^{\otimes 2}$ |
| Native fermion-even determinant-square carrier $\mathcal{O}_{xy}^{(10)} = B_x D_{xy} B_y$ on $\Lambda^5 \mathbb{C}^{10}$ | Proved here (Theorem 5) | Two five-mode matter sites $x,y$ and one half-filled link register $\Lambda^5 \mathbb{C}^{10}$ |
| Dynamical selection of a stationary state concentrating on the $3+2$ orbit with small transport defects | Open downstream obligation | Requires a coupled tick state construction and collective multi-strand transport bounds |

**Prior repo context and literature credit:** The representation-theoretic slot matching of one Standard Model generation into $SU(5)$ is treated in `docs/SU5_EMBEDDING_FROM_GRAPH_FIRST_SURFACE_THEOREM_NOTE_2026-05-07.md` and `docs/SU5_DECOMPOSITION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md`. The classical orbit-projector idea for gauge-invariant composites originates in J. Fröhlich, G. Morchio, and F. Strocchi, *Nuclear Physics B* **190** (1981) 553–582. None of those works proves the noncommuting operator defect identities, the five-mode CAR bilinear identity $C^2 = (6-n)C$, the orthogonal complex-structure polynomial factorization, or the $\Lambda^5\mathbb{C}^{10}$ determinant-square carrier established below.

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

## 6. Paired Runner Verification Summary

The primary runner [`scripts/frontier_u5_three_plus_two_fms_projector_carrier.py`](../scripts/frontier_u5_three_plus_two_fms_projector_carrier.py) verifies every identity in Theorems 1–5 with exact rational (`fractions.Fraction`) and integer Fock-space arithmetic:

1. **Theorem 1 controls:** Exact operator verification of $P_\pm^2 - P_\pm = \frac{1}{4r^2}(A^2 - r^2 I_{\mathcal{A}} \otimes I_2)$, the internal Hilbert-Schmidt decomposition $|A^2 - r^2 I|_{\mathrm{HS}}^2 = 2 R_r^2 + \sum_{a,b} |[\Phi^a, \Phi^b]|^2$, the state-$L^2$ equality across mixed states $\omega$, and exact $SU(2)_X \times SU(2)_Y$ invariance and four-channel completeness of $\mathcal{S}_{s,s'}(X,Y)$ with non-unitary quantum-link transporters $\mathcal{U}_{XY}$.
2. **Theorem 2 controls:** Exact operator verification of $P_3(A)^2 - P_3(A) = (A - a I_5)(A - b I_5)/(a - b)^2$ and internal trace formulas; exact $32$-dimensional Fock-space construction of the five-mode CAR algebra $\Lambda(\mathbb{C}^5)$ verifying $C^2 = (6 I - N)C$ on all $32$ Fock states and the exact idempotence $(P_{\mathrm{CAR}}^{(n)})^2 = P_{\mathrm{CAR}}^{(n)}$ and internal trace $\operatorname{Tr}_{M_5}(P_{\mathrm{CAR}}^{(n)}) = \frac{n}{6-n} I$ across all sectors $n \in \{1,2,3,4,5\}$; and exact verification of the rank-separation witness $A_{\mathrm{mix}} = (A_{(4)}, A_{(2)})$ and joint certification functional $\mathcal{D}_{3+2}(A_{(k)}) = (k - 3)^2$.
3. **Theorem 3 controls:** Exact rational $10 \times 10$ and operator-valued verification of $Q_6(A)^2 - Q_6(A)$, $[A, Q_6(A)] = 0$, the polynomial factorizations of $J_A^2 + I_{10}$ and $A - (a Q_6(A) + b Q_4(A)) J_A$, and exact rank/nullity computation over the $45$-dimensional basis of $\mathfrak{so}(10)$ confirming $\dim \mathfrak{c}_{\mathrm{real}} = 21$ and $\dim \mathfrak{c}_{\mathrm{unitary}} = 13$.
4. **Theorem 4 controls:** Exact arithmetic verification of the homomorphism $\pi: SU(3) \times SU(2) \times U(1) \to S(U(3) \times U(2))$, its order-$6$ cyclic kernel $\ker \pi = \{\gamma_6^k : k = 0,\dots,5\}$, the $13 \to 12$ Lie-algebra dimension reduction, and the two-component stabilizer $K_{U(5)} = H\{\pm I_5\}$.
5. **Theorem 5 controls:** Exact $252 \times 252$ Fock-space construction on $\Lambda^5 \mathbb{C}^{10}$ of all $25$ link operators $U_\ell^{ij} = r_{y,i} r_{x,j}^\dagger$ and $D_{xy}$, verifying $U_\ell^{i_1,j_1}\cdots U_\ell^{i_5,j_5} = \varepsilon_{i_1\dots i_5}\varepsilon_{j_1\dots j_5} D_{xy}$ across all $120$ permutations and repeated-index tuples, $D_{xy} = -|5_x, 0_y\rangle\langle 0_x, 5_y|$, $\operatorname{Tr}_{\Lambda^5\mathbb{C}^{10}}(D_{xy}^\dagger D_{xy}) = 1$, and exact two-site-plus-link verification of $[G_x^{ij}, \mathcal{O}_{xy}^{(10)}] = 2\delta_{ij}\mathcal{O}_{xy}^{(10)}$ and $[G_y^{ij}, \mathcal{O}_{xy}^{(10)}] = 0$ for all $25$ generators at each endpoint.
