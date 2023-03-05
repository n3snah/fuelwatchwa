# FuelWatch WA

The FuelWatch WA custom component provides fuel prices for petrol stations in Western Australia as sensors for Home Assistant.

The component uses the FuelWatch API to fetch petrol prices from petrol stations in Western Australia.

## Installation

To install the FuelWatch WA custom component, you can install it manually by copying this code into a `fuelwatchwa` directory into the `custom_components` directory of your Home Assistant installation.

After installing the component, you will need to configure it by going to the `Devices & Services` page and adding the integration via the `Add Integration` button.

## Sensors

The component creates sensors for the cheapest petrol station for your configured suburb.

    `fuel_brand`: The brand of the petrol station.
    `fuel_address`: The address of the petrol station.
    `fuel_location`: The location of the petrol station.
    `fuel_price`: The price of the fuel at the petrol station.


## Credits

[FuelWatch](https://www.fuelwatch.wa.gov.au/) API provided by Government of Western Australia.
[FuelWatcher library](https://github.com/danielmichaels/fuelwatcher) by Daniel Michaels