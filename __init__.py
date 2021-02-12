"""
setup_db
==========================================

Package belonging to Karttur´s GeoImagine Framework.

Author
------
Thomas Gumbricht (thomas.gumbricht@karttur.com)

Last update: 11 Feb 2021

"""

from .version import __version__, VERSION, metadataD

from .setup_db_class import PGsession

from .paramjson_mini import Params

__all__ = ['PGsession', 'Params']