## 10. Independent edge coefficients and a nominal observation time

Exact lattice homogeneity is unnecessary for a corresponding local estimate. Assign every installed directional edge its own positive coefficient j_e, keeping its exact Pauli matrix form. Let J_0 be the old x-bond coefficient and J_L,J_R the two adjacent exterior x coefficients. Put g=J_L+J_R. Let b be the sum of coefficients of the eight old/E transverse edges and c the sum of the eight E/E transverse edges incident on L,R. All other coefficients may vary independently, subject to their physical incident caps.

With the actual E-only Hamiltonian H_E, the full-space estimate is

\[
\begin{aligned}
T_j(t)&=e^{-i[(J_L+J_0+J_R+b)t+\theta]}
 [e^{-itK}W]\otimes e^{-itH_E},\\
\|e^{-itH}-T_j(t)\|&\le g+\tfrac12g^2t+|J_0t-\theta|+(b+2c)t.
\end{aligned}                                                    \tag{22}
\]

To verify it, replace (7) by

\[
H_4=K+(J_L+J_0+J_R)I-J_LX_LX_1-J_0X_1X_2-J_RX_2X_R.
\]

In endpoint signs a,d and old XX sign p, the detuning in (9) becomes q=J_La+J_Rdp, hence |q|≤g. Equation (10) bounds its cost by g+g²t/2. Delete the same eight E/E transverse edges only in H_E,ref. Its retained endpoint contacts still commute with X_L,X_R, regardless of their coefficients. The exact physical decomposition has scalar b+c and signed perturbation norm at most b+c; restoring the actual environment transfers scalar c and costs at most ct. This proves (22), including its phase. Remote environment terms remain unchanged in both evolutions and incur no extensive error penalty.

For an explicit sufficient policy with 0<ε≤1, choose a nominal J>0 and

\[
\begin{gathered}
J_0\in[J(1-\eta),J(1+\eta)],\quad 0<J_L,J_R\le2J,\\
J\le\frac{\epsilon}{512(\theta+1)},\quad
0\le\eta\le\frac{\epsilon}{64(\theta+1)},\quad
b+2c\le\frac{\epsilon J}{64(\theta+1)},\\
|t-\theta/J|\le\frac{\epsilon}{64J}.
\end{gathered}                                                    \tag{23}
\]

Since Jt<θ+1, the four terms in (22) are respectively <ε/128, <ε/64, <ε/32, and <ε/64. For the third term use
|J_0t−θ|≤J|t−θ/J|+ηJt. Thus the vector bound is <9ε/128<ε/8, and the unhalved complete channel bound is <9ε/64<ε/4. The interval center uses the nominal J, rather than fitting the actual J_0.

The old incident cap is at most 3+2[J_0+max(J_L,J_R)+b]<3+8J. Impose also J≤(Λ−3)/8 for Λ>3. All non-old incident caps must be enforced separately. A simultaneous nonempty coefficient box is obtained by choosing every remaining x coefficient in (0,J] and every transverse coefficient in (0,εJ/[1536(θ+1)]]. Then b+2c has 24 weighted coefficient slots, so its bound in (23) holds; the non-old loads are <8J. Larger remote coefficients are permitted by (22) when their local hardware caps hold. No uniform smallness of all remote transverse coefficients is required by that theorem.

The common phase in (22) uses the actual coefficients. It is not a guarantee relative to an unknown nominal apparatus phase. The inventory, all-output comparison and finite-volume qualifications of §§2,5,6 remain unchanged. This result covers independent positive edge weights within the exact directional Pauli family, not arbitrary matrix errors, errors in K, graph changes, or a native mechanism supplying calibrated coefficients. It still gives an observation window, not a release or halt.

The [inhomogeneous source](../outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_inhomogeneous_attachment/PROPOSAL.md) and its [distinct check](../outputs/native_compass_literal_attachment_2026_10_18/source_checks/native_inhomogeneous_attachment_check/REVIEW.md) are frozen in the publication manifest. ROOT authored this extension; the checker reconstructed it with source exposure and shared campaign ancestry. Editorial integration is not an additional independent check.
