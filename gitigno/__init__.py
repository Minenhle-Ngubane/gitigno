from gitigno.core import cli

from gitigno.constants import (
    START_MESSAGE,
    ERROR_TEXT,
    ECHO_LABEL,
)

from gitigno.utils import (
    request_gitignore,
    display_text_block,
    display_ascii_art,
    display_available_templates_table,
)


# yyyymmdd
__releasedate__ = "20230628"


# x.y.z or x.y.z.dev0 -- semver
__version__ = "0.0.2"