'''Unit tests for the config_flow file'''
import sys
import inspect
from homeassistant import config_entries

# Append parent directory to Python path
sys.path.append("..")
from fuelwatchwa.config_flow import ConfigFlow

def test_ConfigFlow():
    """Unit tests for ConfigFlow class"""
    assert issubclass(config_entries.ConfigFlow, config_entries.ConfigFlow)

    assert hasattr(config_entries.ConfigFlow, 'async_step_user')
    assert inspect.iscoroutinefunction(config_entries.ConfigFlow.async_step_user)
    assert ConfigFlow.VERSION == 1
