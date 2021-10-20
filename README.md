# Ruangguru_SEIT-TechnicalAssessment
This Automation testing is to fulfill the requirements of recruitment process on Runagguru SEIT. This automation is to test the Web and API of Search feature Skillacademy web.
The automation features parameterized data-driven testing on functional or UI, pytest unit testing framework, and assertions throughout the processes to validate the designated results.

## Tools
* Pytest
* Selenium Webdriver
* requests

more detailed versions of each tools are on the `requirements.txt`

## Requirements
In order to utilise this project you need to have the following installed locally:

* Chrome and Chromedriver (UI tests uses Chrome by default, can be changed in config)
* Python ~=3.8
* optional: Firefox and GeckoDriver

to install dependencies that are listed on the `requirements.txt`

`pip install -r requirements.txt`

For the UI testing, the website url that is used is `https://skillacademy.com/`
while the API endpoint takes place on `https://skillacademy.com/skillacademy/discovery/search`

## Usage

The project is broken into separate modules for UI and API testing. Each of these modules can be utilised independently of the others using following codes on cmd.

To run all modules, navigate to to the `root` directory and run:

`pytest -v -s`

To run UI tests only on the skillacademy website, run:

`pytest TestCases\test_search.py -v -s`

To run API tests only, run:

`pytest TestCases\test_api.py -v -s`

If the virtual environment will be used, first activate the `venv`:

`venv\Scripts\activate`

and install the requirements by the `venv` 
