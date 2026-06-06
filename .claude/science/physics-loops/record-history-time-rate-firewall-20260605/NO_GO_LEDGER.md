# No-Go Ledger

- History length is not a physical time coordinate.
- Counts per record step are not rates per physical time without a clock.
- A transition matrix per step does not determine the continuous-time
  generator until `dt` is supplied.
- Unbounded finite retention does not imply unlimited metric duration.
- Record order can orient a history without fixing interval lengths.
