'''Unit tests for the config_flow file'''
import sys
import pytest

# Append parent directory to Python path
sys.path.append("..")
from fuelwatchwa.const import DOMAIN
from fuelwatchwa.config_flow import ConfigFlow

def test_ConfigFlow():
  assert isinstance(ConfigFlow, type)
  assert hasattr(ConfigFlow, '__init__')
  assert hasattr(ConfigFlow, 'async_step_user')
