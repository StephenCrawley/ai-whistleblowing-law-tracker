# Source texts

Source texts for the law entries in data/laws/. Retrieved 2026-09-28 unless a file says otherwise.

**These are working copies, not authoritative.** Always check the live source before marking an entry `verified`.
**Official sources only.** Every file is a verbatim extract (converted from HTML or PDF to plain text) of a text published by a legislature, government or official journal. Facts in the file headers, such as signing dates and bill status, also come from official pages, which are listed in the manifest. Third-party summaries, trackers and law-firm articles may be used to find sources but are never kept or cited here.

## Scope

Illustrative, not comprehensive. The sources support six entries, chosen so that each shows a different pattern:

| Entry | Pattern | Files |
|---|---|---|
| California SB 53 | AI-specific protections for frontier-lab staff | `us-ca-sb53-2025.txt` |
| Connecticut PA 26-15 § 2 | A later, weaker variant of SB 53 | `us-ct-pa-26-15-sb5-excerpt.txt`, `us-ct-cgs-31-51m.txt` |
| EU AI Act Art 87 | General whistleblower law applied to AI, plus an AI-specific channel | `eu-*.txt` |
| UK Employment Rights Act 1996 Part IVA | General law only; no AI body among the prescribed regulators | `uk-*.txt` |
| US S.1792 | Proposed federal protection | `us-federal-s1792-*.txt` |
| New York Labor Law § 740 | General law only; the state's frontier-AI law (RAISE Act) dropped its employee protections before passage | `us-ny-*.txt` |

Not covered, among others: Illinois SB 315 (2026), which closely follows SB 53.

## Files

[`manifest.yaml`](manifest.yaml) is the canonical record of every file here: its source URLs (including the official status pages behind header facts), retrieval date and method, and licence. Each file also starts with a header block that describes it, so it can be read on its own.

`raw_sha256` in the manifest is the hash of each download as fetched (HTML, PDF or XML), before conversion to text. It is recorded for provenance only: the raw downloads are not committed, and a fresh download will not reproduce the hash if the live page has changed since.

## Retrieval notes

- EUR-Lex's website blocks scripted downloads, so EU texts came from the EU Publications Office's Cellar endpoint, which serves the same Official Journal text.
- cga.ct.gov does not send its intermediate TLS certificate. The download was verified by adding GoDaddy's published G2 intermediate certificate, not by disabling verification.
- nysenate.gov refuses scripted downloads, so the three New York pages were saved by hand in a browser. Each saved page records the URL it came from, which is the URL given in the manifest. `raw_sha256` is the hash of the saved HTML file.

## Licensing

The repository's licence does not cover the texts in this directory. Each keeps its own terms, listed per file in `manifest.yaml`:

- **EU legislation and European Commission web pages:** reuse is authorised provided the source is acknowledged (Commission Decision 2011/833/EU). Source: EUR-Lex / Publications Office of the European Union; European Commission.
- **UK legislation and GOV.UK guidance:** Contains public sector information licensed under the Open Government Licence v3.0.
- **US federal texts** (S.1792 and govinfo bill status data): public domain as works of the US government (17 U.S.C. 105).
- **US state legislative texts and statutes** (California, Connecticut, New York): not subject to copyright under the government edicts doctrine (*Georgia v. Public.Resource.Org*, 2020).
