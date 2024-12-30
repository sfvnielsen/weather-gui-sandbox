# weather-gui-sandbox
A sandbox Python project to learn about webframeworks and data visualization.

## Idea for version 0.1
* A webservice (spawned locally), where the user can choose a city in Denmark and get historical temperature data visualized.
* Application should feature
  * A configuration step for setting up API key to the [DMI weather data service](https://www.dmi.dk/friedata/klimadata)
  * A plot window where data can be shown
* Frameworks to be used could be: dash, matplotlib, pandas

### Possible extensions
* Supporting other sources of weather data
* Comparing temperature data between cities
* Prediction tab where the user can try to predict future weather trends using various (simple) machine learning models
* GUI Design (make it easily configurable for a new theme/design style)
* For inspiration on how to make widget/windows/figures interactive using plotly/dash: https://plotly.com/blog/dash-matplotlib/

## Setup

Steps for running the main:
* (optional, but encouraged) Start a terminal and activate your local Python environment (either via conda or venv). For more on this see the [virtual environment documentation page from Python](https://docs.python.org/3/library/venv.html)
* In the command line run the package installation tool `pip install -r requirements.txt`
* Try running `python main.py`, which should start (without errors) a webservice with a small dummy plot. The link to the service will be printed in the terminal.

## TODO
* Breaking down the application into tasks (cf. Github projects)
* Setting up a minimal starting point (MVP)
* Setting up unit testing (pytest)
