'''Pytests for sensor'''
from unittest.mock import MagicMock, Mock
import pytest
import asyncio
from fuelwatchwa import async_setup_entry

@pytest.mark.asyncio
async def test_async_setup_entry():
    '''pytests for test_async_function_entry'''
    # create a mock HomeAssistant instance and ConfigEntry object
    hass = Mock()
    config = Mock()

    # create a mock AddEntitiesCallback
    async_add_entities = Mock()

    # call async_setup_entry with mocked objects
    await async_setup_entry(hass, config, async_add_entities)

    # check that async_add_entities was called with the expected arguments
    async_add_entities.assert_called_once_with([
        FuelPrice(hass, config),
        FuelStationName(hass, config),
        FuelStationLocation(hass, config),
        FuelStationAddress(hass, config)
    ])

@pytest.mark.asyncio
async def test_fuelwatch_sensor_update():
    '''pytests for test_fuelwatch_sensor_update'''
    # create a mock HomeAssistant instance and ConfigEntry object
    hass = Mock()
    config = Mock()
    config.data = {'product': 'U91', 'suburb': 'Test Suburb', 'day': 'Today'}

    # create a mock FuelWatch instance and set its query result
    fuelwatch = MagicMock()
    fuelwatch.get_xml = [{'Key': 'Value'}]

    # create a FuelWatchSensor instance with mocked objects
    sensor = FuelWatchSensor(hass, config, 'Test Attribute', 'Key')
    sensor.api = fuelwatch

    # call the update method
    sensor.update()

    # check that the sensor properties are set as expected
    assert sensor.fuel_type == 'U91'
    assert sensor.suburb == 'Test Suburb'
    assert sensor.day == 'Today'
    assert sensor.xml_query == [{'Key': 'Value'}]
    assert sensor._attr_native_value == 'Value'
