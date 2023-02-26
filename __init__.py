"""The fuelwatchwa sensor integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .const import DOMAIN

DOMAIN = DOMAIN
PLATFORMS = [Platform.SENSOR]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up FuelWatch WA from a config entry"""
    suburb: str = entry.data["suburb"]
    product: int = entry.data["product"]
    day: str = entry.data["day"]

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True