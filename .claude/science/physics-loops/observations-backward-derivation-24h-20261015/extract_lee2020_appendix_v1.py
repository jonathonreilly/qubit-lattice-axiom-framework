"""Reproduce the exposed Appendix A.1 CSV from the pinned public thesis.

Two different PDF engines and row-segmentation rules must agree on all 95
printed rows. This validates transcription, not the experiment or any theory.
The source PDF remains in runtime storage; fetch its public URL from the data
identity receipt and verify the digest before using this script.
"""

import argparse
import csv
import hashlib
import io
import json
import re
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import fitz
import pypdf

PDF_SHA = "00d13a466e4f8c14c3f6067d49d90fd0c49a89e72a8cf93f3a79c18d6aef924a"
CSV_SHA = "de832b111212a39a6a7a610a1013fbf6fa7201b1e9f304da13801e92961ba381"
FIELDS = ["run", "separation_um", "separation_sigma_um", "N120_fNm",
          "N120_sigma_fNm", "N18_fNm", "N18_sigma_fNm", "N54_fNm",
          "N54_sigma_fNm", "source_pdf_page", "source_printed_page"]
RUN = re.compile(r"(?:run|kun)\d+[a-z]?")
NUMBER = r"-?\d+(?:\.\d+)?"
PAIR = re.compile(rf"({NUMBER})\s*±\s*({NUMBER})")


def pypdf_rows(pdf):
    rows = []
    reader = pypdf.PdfReader(pdf)
    for page in range(158, 163):
        # Pypdf places a complete printed table row on one line.
        text = re.split(r"(?m)^A\.2\b", reader.pages[page - 1].extract_text())[0]
        for line in text.splitlines():
            tokens = line.replace("±", " ").split()
            if len(tokens) == 9 and RUN.fullmatch(tokens[0]):
                rows.append((tokens[0], tuple(map(Decimal, tokens[1:])), page))
    return rows


def pymupdf_rows(pdf):
    rows = []
    with fitz.open(pdf) as document:
        for page in range(158, 163):
            # MuPDF gives a standalone run ID followed by four cell lines.
            # Stop before A.2: its centering data have a different table schema.
            lines = document[page - 1].get_text().splitlines()
            if "A.2" in lines:
                lines = lines[:lines.index("A.2")]
            for index, line in enumerate(lines):
                if not RUN.fullmatch(line.strip()):
                    continue
                cells = lines[index + 1:index + 5]
                matches = [PAIR.fullmatch(cell.strip()) for cell in cells]
                if len(matches) != 4 or not all(matches):
                    raise ValueError((page, line, cells))
                values = tuple(Decimal(value) for match in matches
                               for value in match.groups())
                rows.append((line.strip(), values, page))
    return rows


def csv_bytes(rows):
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(FIELDS)
    for run, values, page in rows:
        writer.writerow([run, *map(float, values), page, page - 12])
    return output.getvalue().encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--verify-csv", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    assert hashlib.sha256(args.pdf.read_bytes()).hexdigest() == PDF_SHA
    first, second = pypdf_rows(args.pdf), pymupdf_rows(args.pdf)
    assert first == second, "Independent PDF engines/row parsers disagree"
    assert len(first) == len({row[0] for row in first}) == 95
    assert all(values[i] > 0 for _, values, _ in first for i in (1, 3, 5, 7))
    expected = csv_bytes(first)
    assert hashlib.sha256(expected).hexdigest() == CSV_SHA
    assert args.verify_csv.read_bytes() == expected
    receipt = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "source_pdf_sha256": PDF_SHA, "csv_sha256": CSV_SHA,
        "extractor_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "pypdf_version": pypdf.__version__, "pymupdf_version": fitz.VersionBind,
        "rows": len(first), "numeric_table_cells_compared": len(first) * 8,
        "run_and_page_identifiers_compared": True,
        "cross_engine_exact_decimal_agreement": True,
        "original_csv_byte_identical": True,
        "separation_range_um": [float(min(r[1][0] for r in first)),
                                 float(max(r[1][0] for r in first))],
        "all_printed_rows_kept": True,
        "new_selection_or_model_fitting": False,
        "data_role": "Exposed processed development data; not an empirical holdout",
        "empirical_validation": False,
    }
    args.receipt.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt))


if __name__ == "__main__":
    main()
