from enum import Enum


class TaxonomicStatus(Enum):
    """
    The taxonomic status of a taxon.
    For synonyms more detailed status values are provided which
    "subclass" synonym.

    see http://rs.gbif.org/vocabulary/gbif/taxonomic_status.xml
    """
    ACCEPTED = 'Accepted'

    # Treated as accepted, but doubtful whether this is correct.
    DOUBTFUL = 'Doubtful'

    # A general synonym, the exact type is unknown.
    SYNONYM = 'Synonym'

    # More specific subclass of SYNONYM.
    HETEROTYPIC_SYNONYM = 'Heterotypic Synonym'
    HOMOTYPIC_SYNONYM = 'Homotypic Synonym'
    PROPARTE_SYNONYM = 'Proparte Synonym'
    MISAPPLIED = 'Misapplied'
