"""California adapters.

Statewide Cal eProcure components (`caleprocure`, `scprs`, `supplier_search`, `lpa`,
`vendor_ads`), state open data (`openfiscal`), the contractor register (`cslb`), the
surfaces that publish a full bidder field (`caltrans`, `sfpublicworks`, `planetbids`), and
two opportunity-only feeds (`csu`, `sacramento`). A second state gets a sibling package;
only `cli.py` imports these by name -- the assembler, exporter and report reach them
through `BIDDER_SOURCES` and the source registry.
"""
