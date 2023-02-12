from homeassistant import config_entries
from .const import DOMAIN


class FuelwatchwaConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """FuelWatch WA config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1