# Development-data checkpoint

The raw-track selection was registered in RAW_DATA_PROTOCOL_v1.json before accessing measurement values. Only C32EASC2002_169_0000XMMMV0.ODF has been opened. Its label declares 36-byte records and 92064 file records. The personally written development parser decoded 91863 orbit data records: 61459 two-way Doppler, 29556 three-way Doppler, 649 one-way Doppler, 199 range. All decoded tracks have increasing time order and the spacecraft ID 82. This is a format inventory, not an empirical gravity test.

The current exploratory parser is orbit_light_time/pds_odf_inventory_v1.py in the local campaign pack, with stdout/stderr and pds_inventory_v1.json. It is preserved unfinished and has not received the canonical theorem runner's independent code review. Source files are local runtime sources/pds_metadata and sources/pds_development, with URL/SHA receipts. Retrieve only the registered development file using verified HTTPS; the later tracks remain unopened.

Exact archive URLs:

- https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/sce1_169/odf/c32easc2002_169_0000xmmmv0.lbl
- https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/sce1_169/odf/c32easc2002_169_0000xmmmv0.odf

Label SHA256: 37beef944cfbab3711ba49b415535e2ca29113c3cd892ffe3f25160b1badf04e. ODF SHA256: 39a658fd74044783b598c947f54dc97dee755c8499a58d7f371831e3f2792e5f. The parser command takes `--label`, `--odf`, `--output`; no fit is performed. Keep its nominal UTC conversion separate from a validated station/time-scale model.

Next work: verify format decoding independently, derive the reference/ramp/bias conversion and check actual multi-frequency availability. ODF one-second compression is explicit; the coherent phase theorem now supplies an exact finite-count operator within its stated vacuum/worldline premises. Joint trajectory, clock, station delay, plasma and covariance modeling remains open. Do not fit a naive Shapiro curve to uncorrected ODF frequencies.
