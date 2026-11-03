lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T12:00Z

# a3-close: the four named premises left on real-critical nonlinear A3 (row 103)

Pinned at commit 795392014 (branch claude/ym4d-hard-route). Research-stage working state; no status. Written section by section.

Moves: the four named premises left on real-critical nonlinear A3 (`FINISH.md` "Where it stands", second bullet; row 103): (1) U_0 in Reg, (2) A1's pointed-core admission (10.2), (3) (G1) for the outline's actual joined sequence and the 2.8 mismatch set, (4) M1 weight matching.

Status: in progress.

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort max, Mac mini worker, fresh session. One same-provider session; not gated, not an audit. Sources read: the Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775` (fetched into a scratch folder, SHA-256 `d7f77d4d...b4d6f`, matching the hash in `gates/a3-derivative-gate.md`); Balaban CMP 99 (75-102) pp. 77, 98-100 and CMP 102 p. 279, read from the scans in `~/ym4d-papers/` (nothing copied here beyond short statements). Credit: T. Balaban for the regular class, the local-gauge proposition and the variational theorem; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's definitions, Theorems 1-6 of (1b), the BGR conventions and the joined-sequence construction; Codex for `a1-balaban.md` and `flat-port.md`. No numeric job was run; every step is written by hand.

## 1. Premise (1): the critical reference U_0 lies in Reg

**Statement.** Let \(\mathbf B\) be a separated sequence (SA 9593) with gap \(\rho\ge\rho_0'\), \(\mathbf V_0\) a real \(\varepsilon_1\)-regular datum, and \(U_0=U^\circ(\mathbf V_0)\) the axial representative of A1 (`a1-balaban.md` (8.2)). Let \(M,c_{\rm reg}\) be the constants of `p82-curved.md` Theorem P and \(W:=R_1M_1\) the walk length of Balaban's propagator theorems used in the gauge theorem of `a1-balaban.md` §3.8. Put \(M'=c_{\rm reg}M+2W\). There are \(C_L\) and \(a_L>0\), depending on \(L\) only, such that if \(\rho_0'\ge 4LW+2L\) and \(C_LM'\varepsilon_1\le a_L\), then \(U_0\) satisfies (Reg\(_\alpha\)) of `p82-curved.md` §1 with
\[
\alpha=C_LM'\varepsilon_1 .
\]
So [Reg at \(U_0\)] holds with \(\alpha\le\alpha_*\) as soon as \(\varepsilon_1\le\alpha_*/(C_LM')\), which is the consumer's ceiling of `p82-curved.md` (a radius chosen after the lengths).

**Counterexample attempt.** Reg asks for a derivative bound on a gauge potential, and curvature alone does not give one: on a cube of side \(m\xi\) at mesh \(\eta\), a field with \(|\partial U-1|\le\varepsilon\eta^2\xi^{-2}\) can have, in every gauge, transverse differences of size \(\varepsilon\xi^{-2}\log(\xi/\eta)\) (the \(L^\infty\) failure of the Calderon-Zygmund bound; this is `p82-curved.md` test 2.4). So a counterexample at \(U_0\) would have to violate the current bound at some bond. The only places where criticality does not control the current directly are the layer-0 bonds (fixed by the datum), the free inward bonds and the bonds next to \(\partial\Omega_0\). At layer 0 the scale is \(\eta\), and the current is at most \(2(d-1)\) plaquette differences over \(\eta^3\), so it is controlled by curvature (`a1-balaban.md` §8, base case). At the others, (8.2) bounds \(J(U_0)(b)\) at every bond, since the reset (6.6) bounds \(r(U)\), a supremum over all bonds. No counterexample.

**Proof.** Four steps.

*(i) Balaban's class.* `a1-balaban.md` (8.2) (gated ADVANCE conditional on F0, `gates/a1-balaban-gate.md` §§4, 8; F0 is `flat-port.md`, gated in row 99) gives at every plaquette and bond of \(\Omega_0\)
\[
|\partial U_0(p)-1|\le B\varepsilon_1\eta^2\mathsf L(p)^{-2},\qquad |J(U_0)(b)|\le B\varepsilon_1\mathsf L(b)^{-3}.
\]
Balaban's class \(\mathcal U_k(\{\Omega_j\},\alpha_0)\) (CMP 99a (1.7)-(1.9), read on the scan of p. 77) is: \(|U(\partial p)-1|<\alpha_0L^{-2j}\) for \(p\in\Omega_j\), and \(|(D^{\eta*}_U\partial U)(b)|<\alpha_0L^{-2j}(L^j\eta)^{-1}\) for \(b\in\Omega_j\), where \(p\in\Omega_j\) means that some corner lies in \(\Omega_j\). In level-\(k\) units \(L^j\eta=\xi_j\) and \(L^{-2j}=\eta^2\xi_j^{-2}\). A corner in \(\Omega_j\) has scale at least \(\xi_j\), so \(\mathsf L(p)\ge\xi_j\) and \(\mathsf L(b)\ge\xi_j\). Hence the curvature half of (8.2) gives (1.7) with \(\alpha_0=B\varepsilon_1\). For (1.9): Balaban's \(\eta^{-2}D^*_U\partial U\) is a matrix whose anti-Hermitian part is \(J(U)\) at every bond whose six plaquettes lie in \(\Omega_0\); its Hermitian part is bounded by \(C\varepsilon^2\mathsf L^{-3}\) through \(\mathrm{Re}\,W-1=-\frac12(W-1)^*(W-1)\) for unitary \(W\) (`a1-balaban.md` §2, checked in its gate). So (1.9) holds at those bonds with \(\alpha_0=C(B\varepsilon_1+B^2\varepsilon_1^2)\le 2CB\varepsilon_1\). Below, only bonds with all six plaquettes in \(\Omega_0\) are read.

*(ii) Geometry for \(j\ge1\).* Let \(Z\subset\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\) be a cube of side \(c_{\rm reg}M\xi_j\), \(j\ge1\). Let \(\square\) be the union of the cubes of side \(W\xi_j\), aligned with the level-\(j\) blocks, that meet \(Z\). It is a cube of side \(M''\xi_j\le M'\xi_j\), \(M''\) a multiple of \(W\). Balaban's enlargement \(\tilde\square\) (CMP 99a p. 98: the cover of the outermost nested cube, whose boundary lies at distance \(2W\xi_j\) from \(\square\)) satisfies \(\tilde\square\subset Z+4W\xi_j\) (\(\ell^\infty\) neighbourhood). Since \(Z\subset\Omega_j\) and \(\operatorname{dist}_\infty(\Omega_{j-1}^c,\Omega_j)>\rho\xi_{j-1}=\rho\xi_j/L\), the condition \(\rho>4LW+2L\) gives \(\tilde\square\subset\Omega_{j-1}\), at distance at least \(2\xi_j/L\ge 2\eta\) from \(\Omega_{j-1}^c\). Thus every plaquette and every bond, with its six plaquettes, meeting \(\tilde\square\) lies in \(\Omega_0\).

*(iii) Proposition 6 at level \(j\).* Balaban's proof of CMP 99a Proposition 6 (pp. 98-99) first drops the members \(\Omega_{j'}\), \(j'>j\): the class conditions at a coarser scale are stronger, so \(U_0\) lies in the class of the truncated sequence \(\Omega_0\supset\dots\supset\Omega_j\) with the same \(\alpha_0\). After rescaling \(\xi_j=1\), the only use of the hypotheses is (1.7)-(1.9) on \(\tilde\square\subset\Omega_{j-1}\), at scale \(\xi_{j-1}\), which costs \(L^2\) (curvature) and \(L^3\) (current); this is his (1.128) and (1.132). The membership \(\square\subset\Omega_j\), \(\square\not\subset\Omega_{j+1}\) is used only to place \(\tilde\square\) in \(\Omega_{j-1}\), which (ii) supplies directly. Its port is `a1-balaban.md` §3.8, last paragraph ("Proposition 6's local gauge needs no critical background"; reference 1, flat inverses only), gated ADVANCE conditional on F0. Under \(7dL^2M''\alpha_0\le c_1\) it gives a gauge \(u\) on \(\tilde\square\) with \(U_0^{u^{-1}}=e^{i\eta A}\) and, on \(\square\supset Z\), in level-\(j\) units (his (1.134), (1.136)),
\[
\xi_j|A|,\ \xi_j^2|\nabla A|<7dL^2B_1M''\alpha_0\le 14\,C\,dL^2B_1BM'\varepsilon_1,
\]
with \(\nabla\) the ordinary difference. This is (Reg\(_\alpha\)) on \(Z\).

*(iv) \(j=0\), no current needed.* Let \(Z\subset\Omega_0\cap(\mathcal L_0\cup\mathcal L_1)\) have side \(n\eta\), \(n=c_{\rm reg}M\). In complete axial gauge from a corner of \(Z\) (\(U_1\equiv1\); \(U_2=1\) on \(x_1=0\); \(U_3=1\) on \(x_1=x_2=0\); \(U_4=1\) on \(x_1=x_2=x_3=0\)), the link \(U_\mu(x)\) is the holonomy of a loop bounding a staircase of at most \(3n\) plaquettes of \(Z\). By unitarity the holonomy is within the sum of their deviations of \(1\): \(|U(b)-1|\le 3nB\varepsilon_1\), since \(\mathsf L(p)\ge\eta\). For \(U=e^{i\eta A}\) with eigenvalue angles \(\pm\theta\), \(|\theta|\le\pi\), one has \(|U-1|=2|\sin(\theta/2)|\ge(2/\pi)|\theta|\), so \(\eta|A|\le\frac{3\pi}{2}nB\varepsilon_1\) and \(\eta^2|\nabla A|\le2\sup\eta|A|\le3\pi nB\varepsilon_1\). This is (Reg\(_\alpha\)) at \(j=0\) with \(\alpha=5\pi c_{\rm reg}MB\varepsilon_1\).

Taking \(C_L\) the larger of the two constants proves the statement. \(\square\)

**Order of constants.** \(L\); flat constants (F0); \(W\); \(M,c_{\rm reg},\alpha_*\) (`p82-curved.md`); \(\rho_0'=\max\{\rho_0,4LW+2L\}\), so the gap is fixed after \(M\) and \(W\), as in the outline's order (SA 9916) and `gates/a1-balaban-gate.md` D2; then \(B\) (A1); then \(\varepsilon_1\le\min\{\alpha_*,a_L\}/(C_LM')\). Depth, mesh, volume and region shape enter nowhere. Torus floors: \(\tilde\square\) has side \(O(M'+W)\xi_j\), within the outline's second floor (SA (1b)(ii)).

**Label.** Premise (1) is **discharged as an implication**: [Reg at \(U_0\)] follows from A1 (8.2) and the Proposition 6 port, both gated conditional on F0, and F0 (`flat-port.md`, gated row 99). The two-layer condition \(Z\subset\mathcal L_j\cup\mathcal L_{j+1}\) is not needed for existence; it only fixes the unit \(\xi_j\). What this does not cover: complex references, the independent-current clause of SA 10133-10137, and Balaban's Laplacian and Hölder members; P82° at real critical references reads none of them.
