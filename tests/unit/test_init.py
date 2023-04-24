'''Pytests for the package / init'''
import sys
import pytest
import inspect
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

# Append parent directory to Python path
sys.path.append("..")
from fuelwatchwa import async_setup_entry
from fuelwatchwa.const import DOMAIN

# tests/unit/test_init.py

def test_init():
    assert DOMAIN == 'fuelwatchwa'

def test_async_setup_entry():
    import fuelwatchwa.__init__
    assert hasattr(fuelwatchwa.__init__, 'async_setup_entry')
    assert inspect.iscoroutinefunction(async_setup_entry)

    assert inspect.signature(async_setup_entry) == inspect.Signature(
        parameters=[
            inspect.Parameter("hass", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=HomeAssistant),
            inspect.Parameter("entry", inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=ConfigEntry),
        ],
        return_annotation=bool
    )

    entry = ConfigEntry(
        version=1,
        domain="fuelwatchwa",
        title="Test",
        data={"suburb": "Test Suburb", "product": 123, "day": "Test Day"},
        source="test",
    )
    suburb = entry.data["suburb"]
    product = entry.data["product"]
    day = entry.data["day"]
    assert isinstance(suburb, str)
    assert isinstance(product, int)
    assert isinstance(day, str)
