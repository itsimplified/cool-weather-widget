# cool-weather-widget
This is a simple Python weather widget that uses the OpenWeatherMap API and Tkinter.  

### Widget Notes:
This weather widget only provides weather information for US cities by zip.  It uses weather data provided by https://openweathermap.org.  An API Key is required in order for this widget to interact with OpenWeatherMap's API.  To obtain an API key, you must first register via the link provided above.  Then modify the openweather.py file by pasting your API key into the app_address variable definition.

### Creating a Stand-Alone Application:
To create a stand-alone application, use pyinstaller with the included spec and icon files.  Be sure to change the pathex filepath to the directory path that the widget files were downloaded to.  Important! Windows users remove the app = BUNDLE block.

### Downloading the Stand-Alone Application:
For your convenience, you can download the stand-alone applications from our website https://goo.gl/hyrFWg.  
