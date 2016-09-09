from schematics.models import Model
from schematics.types.base import StringType


class Internal:
    """Model that is going to be used to test import with strings."""
    class Schema(Model):
        abc = StringType()
