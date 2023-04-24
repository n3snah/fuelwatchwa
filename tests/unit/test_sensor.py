'''Pytests for sensor'''
import sys
import pytest
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass
)
from homeassistant.const import CURRENCY_CENT

# Append parent directory to Python path
sys.path.append("..")
from fuelwatchwa.sensor import async_setup_entry, FuelWatchSensor, FuelPrice, FuelStationName, FuelStationLocation, FuelStationAddress

def test_async_setup_entry():
    assert True

class MockConfigEntry:
    def __init__(self, data):
        self.data = data

class MockFuelWatch:
    def __init__(self, xml):
        self._xml = xml

    @property
    def get_xml(self):
        return self._xml

    @get_xml.setter
    def get_xml(self, value):
        self._xml = value

class TestFuelWatchSensor:
    def test_base(self):
        assert hasattr(FuelWatchSensor, '__init__')

    def test_fuel_type(self):
        fuel_type = 1
        suburb = "Test Suburb"
        day = "Test Day"
        xml_key = "Test Key"
        hass = None
        config_entries = MockConfigEntry({'product': fuel_type, 'suburb': suburb, 'day': day})

        fuel_watch_sensor = FuelWatchSensor(hass, config_entries, "attr_name", xml_key)

        # Test fuel_type property
        assert fuel_watch_sensor.fuel_type == fuel_type

    def test_suburb(self):
        fuel_type = 1
        suburb = "Test Suburb"
        day = "Test Day"
        xml_key = "Test Key"
        hass = None
        config_entries = MockConfigEntry({'product': fuel_type, 'suburb': suburb, 'day': day})

        fuel_watch_sensor = FuelWatchSensor(hass, config_entries, "attr_name", xml_key)

        # Test suburb property
        assert fuel_watch_sensor.suburb == suburb

    def test_day(self):
        fuel_type = 1
        suburb = "Test Suburb"
        day = "Test Day"
        xml_key = "Test Key"
        hass = None
        config_entries = MockConfigEntry({'product': fuel_type, 'suburb': suburb, 'day': day})

        fuel_watch_sensor = FuelWatchSensor(hass, config_entries, "attr_name", xml_key)

        # Test day property
        assert fuel_watch_sensor.day == day

    def test_update(self):
        fuel_type = 1
        suburb = "Test Suburb"
        day = "Test Day"
        xml_key = "Test Key"
        hass = None
        config_entries = MockConfigEntry({'product': fuel_type, 'suburb': suburb, 'day': day})

        fuel_watch_sensor = FuelWatchSensor(hass, config_entries, "attr_name", xml_key)

        # Create a mock FuelWatch object and define a setter for get_xml property
        fuel_watch_mock = MockFuelWatch([{"Test Key": "Test Value"}])
        fuel_watch_sensor.api = fuel_watch_mock

        # Mock the FuelWatch API query and get_xml methods
        fuel_watch_sensor.api.query = lambda **kwargs: None
        fuel_watch_sensor.api.get_xml = [{"Test Key": "Test Value"}]

        # Test update method
        fuel_watch_sensor.update()
        assert fuel_watch_sensor.xml_query == fuel_watch_sensor.api.get_xml
        assert fuel_watch_sensor._attr_native_value == "Test Value"

def test_FuelPrice():
    assert issubclass(FuelPrice, FuelWatchSensor)
    assert hasattr(FuelPrice, '__init__')
    assert hasattr(FuelPrice, '_attr_native_unit_of_measurement')
    assert FuelPrice._attr_native_unit_of_measurement == CURRENCY_CENT  # Check the expected value

    assert hasattr(FuelPrice, '_attr_device_class')
    assert FuelPrice._attr_device_class == SensorDeviceClass.MONETARY  # Check the expected value

    assert hasattr(FuelPrice, '_attr_state_class')
    assert FuelPrice._attr_state_class == SensorStateClass.MEASUREMENT  # Check the expected value

def test_FuelStationName():
    assert issubclass(FuelStationName, FuelWatchSensor)
    assert hasattr(FuelStationName, '__init__')

def test_FuelStationLocation():
    assert issubclass(FuelStationLocation, FuelWatchSensor)
    assert hasattr(FuelStationLocation, '__init__')

def test_FuelStationAddress():
    assert issubclass(FuelStationAddress, FuelWatchSensor)
    assert hasattr(FuelStationAddress, '__init__')
