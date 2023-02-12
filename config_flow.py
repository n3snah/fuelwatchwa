from __future__ import annotations

from typing import Any

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN
import voluptuous as vol


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """FuelWatch WA config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1

    def __init__(self):
        """Initialize the Config flow for FuelWatch WA"""

    async def async_step_user(self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        errors = {}

        STEP_USER_DATA_SCHEMA= {
            vol.Required("suburb", default="Kelmscott"): str
        }

        if user_input is not None:
            # Validate User input.
            # todo: add in validations
            valid = True
            if valid:
                return self.async_create_entry(
                    title="FuelWatchWA",
                    data=user_input
                )

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema(STEP_USER_DATA_SCHEMA), errors=errors
        )