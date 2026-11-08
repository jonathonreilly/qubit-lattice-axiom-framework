## Repo search

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, and `pr/10141` in the full repository.
Terms: `RED`, `independent.current R9`, `reduced R9`, `[RED]`, `nl-r9`, `red.md`, and off-shell/R9 variants.
The focused search found two relevant outside-lane hits, both under `pr/10141:research/ym4d/library/`:

- `assembly-status.md:229`: “[RED] identifies (5) with that nonlinear map; it does not identify the two current continuations in (7).” This is the exact distinction below, already owned by DR.
- `open-registry.md:443`: “an unconditional [NL] for a uniquely pre-existing R9 map has not been established here.” This repeats the pre-adoption obligation. It supplies no different formula.

No relevant hit appeared on the other four refs in that focused search. Broader independent-current hits concern other objects.
Reused `prior/repo-search-2026-11-08.md` §13. `prior/leaf-red.md` is absent.

Research text at `aa33ce362`; no audit or status grant. Credit `red.md`, `nl-r9.md`, and `drlocp.md` for the existing arguments. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex, for the account at `31a47c543775`; Balaban for its method.

## Specification and stopping point

**The adopted field formula matches. The pair-current mismatch is already documented and belongs to DR. Stop there.**
`hstep-tree.md` §7 forbids a new RED proof. Its specification is `nl-r9.md` (4.1)–(4.4):

\[
W_s^{\rm red}(a)=-d_{3,s}'{}^{\mathsf T}p_s-K^{\mathsf T}M_sd_s
-d_s'{}^{\mathsf T}M_sKa+d_s'{}^{\mathsf T}M_sd_s+Z^{\mathsf T}N_0(z),
\]

where \(d_s=\mathcal C(a-Hd_s)\), \(z=a-Hd_s\), \(Z=I-Hd_s'\), \(d_{3,s}=d_s-\mathcal C_2\), and \(p_s=H^{\mathsf T}\mathbf J\).
Keep the raw pairings, separate walk assignments, repeated switch powers, and unparameterized diagonal in \(M_s=M_s^{\rm walk}-a_0I\).

| Caller read | Literal formula or requirement | Match |
|---|---|---|
| `red.md:10,21–39`; `dr.md` (4); `drlocp.md` (5)–(6) | \(a=H_1B'-\mathfrak G W_s^{\rm red}(a)\), \(h=a-H\mathcal C(h)\) | Yes. These adopt the displayed expression. |
| `loc-3.md:119,194`; `loc-4.md:23,242–260`; `r2-heal.md` (F), via its check §9 | (D1), then \(\mathfrak F_\tau(\mathscr T_Y;p,\xi_Y)\) | Indirect use. Adoption settles the field specification; every-move existence and domains remain inputs. |
| `shift-map.md` (23); `ti-cov.md:87` | \(a+G_pW_p(a)=H_{1,p}b_p\); \(d=\mathcal C(a-Hd)\) | Yes, by their explicit references to (4.4). |
| Outline 10360–10372, 10562–10576 | \(\mathbf A+\mathfrak G(s)\mathsf W_s(A_\bullet)=0\) | Prescribes reduction before switching. It does not display a competing five-term formula. This is the adoption already covered by `red.md`. |
| `red.md:59–69`; `loc-4.md:207`, through `d3-local.md` (3) | Force-anchored multiplier and current below | Different current continuation from `dr.md` (5). Already recorded in `drlocp.md` (7)–(8). |

Put \(A_h=(I+H^{\mathsf T}\mathcal C'_h{}^{\mathsf T})^{-1}\). The two literal calls are
\[
\begin{array}{ll}
\lambda_F=A_hH^{\mathsf T}F'_U(h),&\lambda_{F,0}=H^{\mathsf T}F'_U(0),\\
\lambda_J=A_hH^{\mathsf T}[F'_U(h)-F'_U(0)+\mathbf J],&\lambda_{J,0}=H^{\mathsf T}\mathbf J,\\
j_F=R_hK_h^{\mathsf T}\lambda_F-K_0^{\mathsf T}\lambda_{F,0},&
j_J=R_hK_h^{\mathsf T}\lambda_J-K_0^{\mathsf T}\lambda_{J,0}.
\end{array}
\]
Their difference is exactly `drlocp.md` (8):
\[
j_F-j_J=[R_hK_h^{\mathsf T}A_h-K_0^{\mathsf T}]H^{\mathsf T}(F'_U(0)-\mathbf J).
\]
On-shell agreement does not remove this off-shell difference. This is a known pair-current mismatch, **not** a new counterexample to the adopted \(W_s^{\rm red}\).

The account has no literal RED call. Its three `R9` hits, CA-I 9217, 9278 and 9339, concern a lower bound on \(M\).
Its separately specified response chart, CA-I 14376–14420, uses
\(\mathcal A\mapsto\tilde{\mathfrak G}_0[\Theta_J(\mathcal A+H_0B)-\mathbb V'^J(\mathcal A+H_0B)]\).
That is not a literal adoption of (4.4). No equivalence or inequivalence is inferred here; `port-map.md` row 4 already assigns this formulation match to DR.

**Kill-test result:** no different field nonlinearity was found in the calls compared above. The known current mismatch stops a blanket pair-response match. This is the requested stopping alternative, not an exhaustive certification of all callers. No proof, computation, ownership change, or new obligation is added.
