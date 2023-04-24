# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unversioned
### Added
    * Unit testing for sensor.py
    * Unit testing for __init__.py
    * Unit testing for config_flow.py
    * Pytest runs inside the pylint.yaml github action.
    * Python cache and virtual environment directory exclusions added to `.gitignore`.

### Changed
    * Python version updated to 3.10.11
    * Pylint command improved to capture only this module's content.
    * README.md updated to include information about using Python virtual environments.
    * Required python packages have now been pinned to a particular version in `requirements.txt`.

## v0.1.0 - 2023/03/16
### Added
    * 4 sensors for the cheapest fuel price of either today or tomorrow.
        * `fuel_station_name`: The brand of the petrol station.
        * `fuel_station_address`: The address of the petrol station.
        * `fuel_station_suburb`: The location of the petrol station.
        * `fuel_cheapest_price`: The price of the fuel at the petrol station.
