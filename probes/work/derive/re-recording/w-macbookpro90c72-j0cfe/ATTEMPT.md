# re-recording, attempt 4 (worker w-macbookpro90c72-j0cfe, model grok-4.6)

Axiom-adjacent: consequences of a hypothetical re-recording dynamics with the covariant rule. Nothing here assumes re-recording is admissible. Independent of other attempts (none were on the branch at claim time). Definitions: the covariant rule and the static law of block 01 (product class (P); Boltzmann special case \(K(s\mid S)\propto e^{\beta s\cdot S}\)); block 19's transverse kernel \(1/(\beta E(k))\), \(E(k)=\sum_{j=1}^3 2(1-\cos k_j)\).

## (1) The statement attempted

Let \(G=(V,E)\) be a finite undirected graph of maximum degree 6 (the torus \((\mathbb{Z}/L\mathbb{Z})^3\), or a window). Records take values in a menu \(M\) (six-axis \(\{\pm e_i\}\), or \(S^2\)). The covariant Boltzmann rule is
\[
K(s\mid S)=\frac{e^{\beta s\cdot S}}{Z(\beta|S|)},\qquad S=\sum_{y\sim x}s_y,
\]
with \(Z(\kappa)=\sum_{s\in M}e^{\kappa\,\hat S\cdot s}\) (six-axis) or \(Z(\kappa)=4\pi\sinh\kappa/\kappa\) (sphere, \(\kappa>0\); \(Z(0)=4\pi\)). The product rule of block 01, \(r(s\mid\eta)\propto\prod_{y\sim x}\phi(s,\eta_y)\) with \(\phi\) symmetric, is included: Boltzmann is the case \(\phi(a,b)=e^{\beta a\cdot b}\).

**(a)** Asynchronous re-recording (site \(x\) redrawn from \(K(\,\cdot\mid S_x)\) at any positive clock rates \(\lambda_x\)). The unique stationary law on a finite window with positive \(\phi\) is the static law
\[
\mu(s)\propto\prod_{\{x,y\}\in E}\phi(s_x,s_y)^{\mathrm{mult}(xy)}\qquad\bigl(\text{Boltzmann: }\mu\propto\exp\bigl(\beta\sum_{\mathrm{bonds}}s\cdot s'\bigr)\bigr).
\]
It is the Gibbs sampler of that law; block 19's kernel is its equal-time transverse covariance whenever that law is the static sphere law of blocks 01–24.

**(b)** Synchronous re-recording (every site redrawn at once from the current neighbours). The chain is reversible with respect to
\[
\pi(s)\propto\prod_{x\in V}Z(S_x(s)),
\]
a Gibbs law with a star-shaped many-body interaction. The key identity is \(\sum_x s'_x\cdot S_x(s)=\sum_x s_x\cdot S_x(s')\). On every tested window \(\pi\neq\mu\) (total variation strictly positive). At large \(\beta\) on the sphere, \(\log Z(\beta|S|)=\beta|S|-\log(\beta|S|)+\log(2\pi)+O(e^{-2\beta|S|})\), and the transverse quadratic form of \(\sum_x|S_x|\) is \((-E+E^2/12)|\theta_k|^2\); the IR kernel is \(1/E\) with stiffness \(2\beta\) against the static law's \(\beta/2\). The chain orders in the same sense as the static law at large \(\beta\) (aligned configurations dominate; Goldstone mode at \(k=0\)).

**(c)** Transfer. Uniqueness regions, the ordered side, and block 19's kernel transfer to **(a)** because the measure is the static law. They do not transfer as theorems to **(b)**: the specification is different (\(\mathrm{TV}(\pi,\mu)>0\)); the IR kernel is still \(1/E\) but the stiffness and the threshold are not those of the static law. The identities of (a)(b) are menu-agnostic for any symmetric \(\phi\) (resp. any bilinear \(s\cdot S\)).

## (2) Steps

**Step 1 — pairing identity (PROVED; CHECKED as E1).** For any configurations \(s,s'\) of vectors in \(\mathbb{R}^3\),
\[
\sum_x s'_x\cdot S_x(s)=\sum_x\sum_{y\sim x}s'_x\cdot s_y=\sum_y s_y\cdot S_y(s')=\sum_x s_x\cdot S_x(s'),
\]
the middle equality by reindexing the undirected (multi)graph. Holds with multiplicities (the \(L=2\) torus has \(\mathrm{mult}=2\) on each axis). `check.py` enumerates all pairs on the 2-site edge and rotation/one-site slices on C4, \(T^2_2\), \(T^3_2\).

**Step 2 — asynchronous detailed balance (PROVED; CHECKED as E2, E3, E9).** The static weight \(\mu(s)\propto\prod_{\{xy\}}\phi(s_x,s_y)^{m_{xy}}\) has one-site conditional at \(x\) equal to \(K(\,\cdot\mid S_x)\), because \(S_x\) and the complementary bonds do not depend on \(s_x\), so
\[
\frac{\mu(s_{x\leftarrow a})}{\mu(s_{x\leftarrow b})}=\frac{K(a\mid S_x)}{K(b\mid S_x)}.
\]
Hence each site's update is a Gibbs kernel for \(\mu\). For any rates \(\lambda_x>0\) the generator \(Q(s,s_{x\leftarrow a})=\lambda_x K(a\mid S_x)\) (\(a\neq s_x\)) satisfies \(\mu(s)Q(s,s')=\mu(s')Q(s',s)\). On a finite window with \(\phi>0\) the chain is irreducible and aperiodic on \(M^V\), so \(\mu\) is the unique stationary law. CHECKED: every (config, site, value) on the edge, C4 and \(T^2_2\) for Boltzmann \(e^\beta=3\) and product \((p,q,r)=(3,1,2)\); unequal rates \(\lambda=(2,5)\) on the edge; \(Z(S_x)\) independent of \(s_x\); static weight ratios equal kernel ratios.

**Step 3 — synchronous reversibility (PROVED; CHECKED as E4, E6).**
\[
P(s\to s')=\prod_x\frac{K_{\mathrm{unnorm}}(s'_x\mid S_x(s))}{Z(S_x(s))}.
\]
With \(\pi(s)\propto\prod_x Z(S_x(s))\),
\[
\pi(s)P(s\to s')\propto\prod_x K_{\mathrm{unnorm}}(s'_x\mid S_x(s))=\exp\bigl(\beta\sum_x s'_x\cdot S_x(s)\bigr)
\]
in the Boltzmann case (or \(\prod_x\prod_{y\sim x}\phi(s'_x,s_y)\) in the product case). Step 1 and symmetry of \(\phi\) give equality with \(\pi(s')P(s'\to s)\). On a bipartite graph this factors as \(P_A(s'_A\mid s_B)\,P_B(s'_B\mid s_A)\) (CHECKED on C4). The interaction is many-body: \(Z(S_x)\) depends on the whole star of \(x\).

**Step 4 — the two laws are distinct (PROVED; CHECKED as E5).** On C4 with Boltzmann \(e^\beta=3\),
\[
\mathrm{TV}(\pi,\mu)=\frac{39161524}{79474827}>0
\]
(14 distinct values of \(\pi(s)/\mu(s)\)). On \(T^2_2\), \(\mathrm{TV}=122900831405716/159789899835723>0\), again 14 ratios. So \(\pi\) is not a multiple of \(\mu\).

**Step 5 — sphere large-\(\beta\) kernel of \(\pi\) (PROVED as a jet; CHECKED as E8).** \(Z(\kappa)=4\pi\sinh\kappa/\kappa=2\pi e^\kappa(1-e^{-2\kappa})/\kappa\), so
\[
\log Z(\beta|S|)=\beta|S|-\log(\beta|S|)+\log(2\pi)+\log(1-e^{-2\beta|S|}).
\]
The last term is \(O(e^{-2\beta|S|})\); \(-\log(\beta|S|)\) is \(O(\log\beta)\). Leading order is \(\beta\sum_x|S_x|\). Write \(s_y=(\theta_y,1-|\theta_y|^2/2)+O(\theta^4)\) about \(e_z\), \(L=\sum_{y\sim x}|\theta_y|^2\), \(Q=|\sum_{y\sim x}\theta_y|^2\). Then \(|S|=6-L/2+Q/12+O(\theta^4)\). Summing stars: \(\sum_x L=6\sum|\theta|^2\), \(\sum_x Q=\sum_k(6-E(k))^2|\theta_k|^2\), hence
\[
\sum_x(|S_x|-6)=\sum_k\bigl(-E+E^2/12\bigr)|\theta_k|^2.
\]
At \(E=0\) the quadratic vanishes (Goldstone). The IR is \(-E\), so \(\pi\propto\exp(-\beta\sum_k E(k)|\theta_k|^2+\cdots)\). The static law has \(\sum_{\mathrm{bonds}}s\cdot s'=\mathrm{const}-\frac12\sum_k E(k)|\theta_k|^2\), hence \(\mu\propto\exp(-(\beta/2)\sum E|\theta|^2)\). Same \(1/E\) kernel; IR stiffness \(2\beta\) against \(\beta/2\). The \(E^2/12\) term is \(O(k^4)\). (Local spin-wave identification ASSUMED at the usual \(O(\theta^4)\) remainder; the jets themselves are CHECKED as formal series.)

**Step 6 — ordering diagnostic (CHECKED as E7; Peierls ASSUMED).** On C4, the ratio of the all-\(+z\) weight to a one-site opposite flip is \(p^4\) (static) and grows in \(p=e^\beta\) for \(\pi\) as well (\(121/64\), \(3481/729\), \(14641/625\), \(187489/2401\) at \(p=2,3,5,7\)). Aligned beats a single orthogonal flip under both laws at \(p=5\). A Peierls argument for \(\pi\) on \(\mathbb{Z}^3\) is not supplied.

**Step 7 — transfer (PROVED from 2–5; CHECKED as E9).**

| result | async (a) | sync (b) |
|---|---|---|
| uniqueness regions of the static specification | yes (identical kernels) | no (different specification; TV\(>0\)) |
| ordered side of the static law | yes (same measure) | IR Goldstone yes; threshold not the static one |
| block 19 kernel \(1/(\beta E)\) | yes, as equal-time covariance of \(\mu\) | \(1/E\) with stiffness \(2\beta\) at leading spin-wave, not the same prefactor |
| menus | identities use only symmetry of \(\phi\) / bilinear \(s\cdot S\) | same |

## (3) First failing step, if any

The route does not fail for (a) or for the reversibility and distinctness of (b) on finite windows. Not proved: uniqueness of the infinite-volume DLR measure for \(\pi\) (the many-body spec); a Peierls bound for \(\pi\) on \(\mathbb{Z}^3\); the \(O(\theta^4)\) remainder in Step 5; any statement that re-recording is admissible.

## (4) What would finish it

A DLR/uniqueness theorem for the star potential \(\sum_x\log Z(\beta|S_x|)\) on \(\mathbb{Z}^3\); a Peierls or infrared bound giving an ordered phase for \(\pi\) with an explicit \(\beta_c\); the exact spin-wave stiffness including the \(O(1)\) from \(-\log|S|\) (relative \(O(1/\beta)\)). The gravity node's construction run on the equal-time covariance of \(\pi\) rather than of \(\mu\).
