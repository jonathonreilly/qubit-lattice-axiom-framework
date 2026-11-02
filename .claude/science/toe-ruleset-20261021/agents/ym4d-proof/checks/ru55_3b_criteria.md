# ru55_3b — criteria (written BEFORE checks/ru55_3b_lncheck.py exists; `date -u` appended)

Why a second id. ru55_3 ran once (ru55_3_out.txt kept unaltered). All its gates PASSed and controls K1-K3 fired, but control
K4 reported False. Diagnosis (before writing this file): K4 as pre-registered was DEFECTIVE — it asked the ln 10 enclosure
(width ~4·10⁻⁴⁵) to contain 2.302585092994045684, which is an 18-digit TRUNCATION of ln 10 = 2.302585092994045684017991454684…,
lying ~1.8·10⁻²⁰ below ln 10; a correct enclosure of width 10⁻⁴⁵ cannot contain it. The 20-digit display line of ru55_3
("2.30258509299404590109") is a float-conversion artifact (the nearest double), not the enclosure. Per the rules, ru55_3's
criteria and script are not edited; the log-enclosure sanity check is redone here under a new id with a correct criterion.

Gates (pre-registered; the script imports ru55_3_u1.py's functions read-only and changes nothing in them):
- L1: the enclosure ln_enc(10) lies inside [2.302585092994045684017, 2.302585092994045684018] and has width < 10⁻³⁰.
- L2 (independent route): 3·ln_enc(2) + ln_enc(5/4) (interval sum) overlaps ln_enc(10), and the overlap has width < 10⁻³⁰.
- L3: ln_enc(2) lies inside [0.693147180559945309417, 0.693147180559945309418] (ln 2 = 0.6931471805599453094172321…).
- L4 (designed FAIL): the shifted interval ln_enc(10) + 10⁻²⁰ must NOT lie inside L1's window.
Verdict: if L1-L3 PASS and L4 fails as designed, ru55_3's log enclosures are certified and ru55_3's verdicts stand with K4
replaced by L1-L4.
Written at (date -u, appended): 2026-10-29T00:39:38Z
