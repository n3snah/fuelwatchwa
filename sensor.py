"""Platform for sensor integration."""
from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
    PLATFORM_SCHEMA
)
from homeassistant.const import CURRENCY_CENT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry

from fuelwatcher import FuelWatch, PRODUCT, REGION, BRAND, SUBURB
from .const import DOMAIN

_LOGGER = logging.getLogger(DOMAIN)

async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    async_add_entities([FuelPriceToday(hass, config)])


class FuelPriceToday(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Cheapest Fuel Price today"
    _attr_native_unit_of_measurement = CURRENCY_CENT
    _attr_device_class = SensorDeviceClass.MONETARY
    _attr_state_class = SensorStateClass.MEASUREMENT
    api = FuelWatch()

    def __init__(self, hass: HomeAssistant, config_entries: ConfigEntry) -> None:
        self._hass = hass
        self._attr_unique_id = 'sensor.fuelwatchwa_pricetoday'
        self.xml_query = None
        self._attr_native_value = None

        self._fuel_type = config_entries.data['product']
        self._suburb = config_entries.data['suburb']
        self._day = config_entries.data['day']

    @property
    def fuel_type(self) -> int:
        """Return the Fuel Type specified"""
        return self._fuel_type
    
    @property
    def suburb(self) -> str:
        """Return the Suburb for the fuel search"""
        return self._suburb

    @property
    def day(self) -> str:
        """Return the day of the fuel price"""
        return self._day

    def update(self) -> None:
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        #self._attr_native_value = 161.9
        self.api.query(product=self._fuel_type, suburb=self._suburb, day=self._day)
        self.xml_query = self.api.get_xml
        self._attr_native_value = self.xml_query[0]['price']
