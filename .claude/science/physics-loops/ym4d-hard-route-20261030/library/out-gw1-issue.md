**Title:** The (J7) port on the PI class: corrected inverse and lift walks

Ethan and Levent,

Following issues #13 and #14, [this note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/7198d9fa2/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-gw1.md) writes out your (J7) reduction for \(G_1^J\), \((QG_1^JQ^*)^{-1}\), and \(H_1^J\). Your (J7), CA-I 13944–13955, says the arguments of (J1)–(J4) apply verbatim; (J8), 13957–13977, expands them into concatenated walks, and takes the walks of \(q_0\) from a remark printed without proof. All account labels and lines refer to `31a47c543775`.

**What it supplies.** Termwise first-order and differentiated-source bounds with a fixed Hölder gap; coarse density and physical transpose bounds; analytic words, common-footprint restrictions, and zero-switch component separation for these operators. The proof follows your reduction and Balaban's CMP 99b (3.130)–(3.138).

**Scope and inputs.** Use the PI class and the common constant order of GW. The inputs are [Theorem PI, issue #13](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/94df5579a/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-pi.md), [GW, issue #14](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/9a3ad2072/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-gw.md), and GW's stated flat and supplied-frame averaging estimates. The flat estimates rebuild Balaban's CMP 95–96 propagator method. The averaging estimates are the analytic form of his CMP 98 Proposition 5, (156)–(157), which he states without proof (your CA-I 13175–13196). The note links a written proof of each. The note lists and links these inputs before its proof.

The identity in \(\Pi\) uses \(I_f=\sum_\tau h_{\tau,f}^2I_f\), with PI's full cutoff footprints. This extends GW's convention for \(R\); your account does not fix it. It agrees with your operator at one. Following Balaban, CMP 116 (1.6)–(1.11), primitive union tags give \(Ce^{16\kappa_1}\). Your composite lift retains both tags and has bound \(Ce^{32\kappa_1}\). This fits your \(Ce^{c_{\mathbb K}\kappa_1}\) when your parameter-free integer \(c_{\mathbb K}\) (CA-I 14512) is at least 32. The current ceiling precedes \(\kappa_1\); the stated cube floor applies.

**Not covered.** No Laplacian bound for \(G_1^J\) or \(G_\pi^J\), and no graph norm for the general layer. We found no use in your proof of Theorem 0 that needs the first, but the uses were not checked one by one. No general layer-map or switched-current assignment, no admission of arbitrary account domains, and no check of the individual uses in your proof of Theorem 0. The identification with Balaban's true-current operators is a cited remark only. No switched inverse identity is used.

Codex (gpt-6-astra) wrote the proof and this note. Claude (Opus 5.5) checked the proof and this note line by line, and its repairs are applied.

This is a proposed proof for your review. It is research text, not an audit, and grants no status.
