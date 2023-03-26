# FuelWatch WA

The FuelWatch WA custom component provides fuel prices for petrol stations in Western Australia as sensors for Home Assistant.

The component uses the FuelWatch API to fetch petrol prices from petrol stations in Western Australia.

## Installation

To install the FuelWatch WA custom component, you can install it manually by copying this code into a `fuelwatchwa` directory into the `custom_components` directory of your Home Assistant installation.

After installing the component, you will need to configure it by going to the `Devices & Services` page and adding the integration via the `Add Integration` button.

## Sensors

The component creates sensors for the cheapest petrol station for your configured suburb.

    `fuel_station_name`: The brand of the petrol station.
    `fuel_station_address`: The address of the petrol station.
    `fuel_station_suburb`: The location of the petrol station.
    `fuel_cheapest_price`: The price of the fuel at the petrol station.

## Virtual Environment
This project uses a virtual environment to manage dependencies and ensure consistent behavior across different environments. A virtual environment allows you to isolate the Python environment used by your project from the global environment on your system, making it easier to manage dependencies and avoid conflicts.

In this section, we'll provide instructions on how to create and activate the virtual environment, as well as how to install the necessary dependencies.

### Creating a Virtual environment
To create a virtual environment on your local machine, run the following command:
`python3 -m venv env`

### Activating the virtual environment
To activate the virtual environment, run the following command:
`source env/bin/activate`

### Installing dependencies
To ensure that all dependencies have been downloaded, run the following command:
`pip install -r requirements.txt`


## Credits

[FuelWatch](https://www.fuelwatch.wa.gov.au/) API provided by Government of Western Australia.
[FuelWatcher library](https://github.com/danielmichaels/fuelwatcher) by Daniel Michaels