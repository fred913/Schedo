# Schedo

Class schedule, made simple.


## Installation & Usage
Download the latest compressed file from the Release section, extract it to a suitable location, and then open `Schedo.exe`.
You can access settings or exit the program via the tray menu.

### Building from source
1. Clone the repository to your local machine.
2. Create a virtual environment by executing the following command in the terminal. We did test the application with Python 3.8.10, but other versions may work as well.
   ```
   python -m venv venv
   ```
3. Activate the virtual environment by executing the following command in the terminal:
   ```
   .\venv\Scripts\activate
   ```
4. Install the required packages by executing the following command in the terminal:
   ```
   pip install -r requirements.txt
   ```
5. Install PyInstaller by executing the following command in the terminal:
   ```
   pip install pyinstaller
   ```
6. Package the application with PyInstaller by executing the following command in the terminal:
   ``` also pack assets/ dir with the executable
   pyinstaller main.py -w --add-data "assets/*;assets/" -i ./assets/img/favicon.ico -n Schedo
   ```
7. Copy the dependencies and resources to the build output by executing the following command in the terminal:
   ```
   xcopy /E /I config .\dist\Schedo\config
   xcopy /E /I audio .\dist\Schedo\audio
   ```
8. Schedo is now ready to be used. You can find the build output in the `dist` folder.

## License
This project (Schedo) is released under the GPL-3.0 license. Please refer to the [LICENSE](./LICENSE) file for details.

### Source
Originally this project is created by [RinLit-233-shiroko](https://github.com/RinLit-233-shiroko) called Class-Widgets. This is forked and completely (almost) rewritten by [fred913](https://github.com/fred913) to make it more efficient, user-friendly, cusomizable and lightweight.

## Acknowledgments
This program uses [zhiyiYo](https://github.com/zhiyiYo/)'s [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets) for the UI interface of the settings. This is an awesome project that provides a clean and modern UI for PyQt applications, and this project won't be that clean and user-friendly without it.

## Contributors

[![][contrib-image]][contrib-link]

[contrib-image]: https://contrib.rocks/image?repo=fred913/Schedo

[contrib-link]: https://github.com/fred913/Schedo/graphs/contributors

<!-- One more thing: credit whitechi73 for providing the contributors section template :D -->
