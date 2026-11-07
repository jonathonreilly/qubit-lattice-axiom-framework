lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-08T08:52Z

# Check of library/b98p5.md sections 2.1-2.5 (queue row 446, b98p5-port-check)

Provenance: Claude Opus 5.5, max effort, commit 9fcc75acc, branch claude/ym4d-hard-route. One line-by-line reading by one model of another model's text (Codex gpt-6-astra). Not an audit. No numerics were run.

Sources read. CMP 98 printed pages 22-24, 27-28, 30-42 as page images (`~/ym4d-papers/png/cmp98_p0NN.png`), and the OCR only to locate them. The account at `31a47c543775`, fetched by URL into a scratch folder; SHA-256 of SA, CA-I and CA-III agree with the note's table. Line numbers below are those files. Credit: Tadeusz Bałaban for the construction and the proof method; Ethan Sussman and Levent Alpoge, with Claude and Codex as text authors, for the account.

(In progress. Sections are written as the check proceeds.)

## 2.1 The map, its subtraction, and its complete read: ADVANCE

Checked against the printed formulas, not the OCR.

- The comb map M in (5) is CMP 98 (42), p. 23, and its iterate is (43), p. 24: `Ū_c = exp[i Σ_{x∈B(c_-)} L^{-d} (1/i) log U(Γ_{c,x})U(c)^{-1}] U(c)`.
- The site factor m_W(a;y) is Bałaban's `\overline{R_{0,y}V_1}` of (110), p. 34, with (62), p. 28. The identity `P_{e^{ia}W}(γ) P_W(γ)^{-1} = Π_{b⊂γ} R(W(γ_{y,b_-})) e^{ia(b)}` (ordered) is CMP 98 (58), and the note's reverse-edge rule agrees with it.
- F_W(a) is (1/i) log of CMP 98 (89), p. 31 (= (63), p. 28), with V_0 = W, V_1 = e^{ia}. Indeed `R̄_{0,c} = R((V̄_0)_c)` (CMP 98 (59); CA-I 24268) turns `g(c_-)^{-1} \overline{V_1V_0}_c (V̄_0)_c^{-1} R̄_{0,c} g(c_+)` into `g(c_-)^{-1} \overline{V_1V_0}_c g(c_+) (V̄_0)_c^{-1}`, which is the bracket in (5).
- Recursion (6) is CMP 98 (91) and CA-I 24320-24326; the quotation is at CA-I 24324-24326 (the note cites 24323-24332, which contains it). q_c = a_j(c) is Bałaban's Q_j(U_0, ηA, c) = (1/i) log(Ū_1^j)_c of Proposition 4, p. 38. R_c in (1) is Bałaban's C_j(U_0, L^jηA, c) of (150).
- I rederived the factorisation `M(e^{ia}W) = (e^{iF_W(a)} M(W))^{m_W(a)}` with `V^u(c) = u(c_-)V(c)u(c_+)^{-1}`, and the covariance `F_{W^u}(a^u) = Ad(u(c_-)) F_W(a)` with `a^u(b) = Ad(u(b_-)) a(b)`. Both hold wherever the principal logarithms are defined.
- Read set: CMP 98 p. 24 and p. 31, and CA-I 24332-24336, state that the value on c reads only bonds in B^k(c_-) ∪ B^k(c_+). The note's backward induction proves it: for odd L with centred blocks, B^{m+1}(y) is the union of the B^m(z), z ∈ B(y), and each straight segment [x, x'] lies in B(c_-) ∪ B(c_+).

No defect. The note's claim that its extension of the potential off E_c needs no cutoff derivative is correct, because the map never reads outside E_c.
