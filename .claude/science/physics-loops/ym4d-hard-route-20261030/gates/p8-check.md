lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T16:56Z

# P8 positivity and limits ports: one line-by-line check (row 342)

Status: in progress (started 2026-11-06T04:56Z). Sections are written as they are checked.

Pinned at commit a81e94ca8. Scope: `library/port/p8-positivity.md` (B5, B7, B8) and `library/port/p8b-limits.md` (B10-B13). Codex wrote both ports. Source: the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) at 31a47c543775, CA-I and CA-II, fetched by URL into a scratch folder. Kind of result: a check of a port of their proofs.

## Working notes, section by section

### B5 (p8-positivity.md lines 26-144; source II:60440-60690)

- Statement block (lines 30-45) matches II:60440-60465, including the inversion rule for bonds parallel to e_mu.
- Lines 47-104. The port replaces the source's irreducible expansion, with its asserted Fourier decay, by the explicit series (P8.3) in R^{tensor q}, R = V + Vbar. Redone: Re tr W = chi_R(W)/(2d) with tr 1 = 1; a_q = x_0^q/(q!(2d)^q); sum_q a_q d_q^k = exp(x_0 (2d)^{k-1}). Irreducibility is never used, only unitarity and Haar invariance. The factorisation (P8.5) and (P8.6) was redone index by index and holds. Absolute convergence: |u| <= 1, so sum_alpha c_alpha |G_alpha|^2 <= prod_{x,nu} sum_q a_q d_q^6 < infinity.
- Line 106 (correction at the endpoint N/2 = eps). Redone for N = 2, eps = 1: the two crossing families are distinct edges, and each crossing plaquette uses two mu-links of one family. The same tangential bond can be b^+ for both planes, which is harmless because a product of two functions of U_+ is a function of U_+. Correct and harmless; the source's K' range is not needed.
- Lines 108-114 (positivity) and 133-144 (reflection form, Cauchy-Schwarz by G - tF). Redone; both hold.
- B5 verdict: first failing step none.
