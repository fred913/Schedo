<p align="center">
  <img width="18%" align="center" src="img/Logo.png" alt="logo">
</p>
  <h1 align="center">
  Class Widgets
</h1>
<p align="center">
  A desktop class schedule app
</p>

![Interface](img/preview.png)


## Installation & Usage
Download the latest compressed file from the Release section, extract it to a suitable location, and then open `ClassWidgets.exe`.
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
   ```
   pyinstaller main.py -w -i ./img/favicon.ico -n Class-Widgets
   ```
7. Copy the dependencies and resources to the build output by executing the following command in the terminal:
   ```
   xcopy /E /I config .\dist\Class-Widgets\config
   xcopy /E /I ui .\dist\Class-Widgets\ui
   xcopy /E /I img .\dist\Class-Widgets\img
   xcopy /E /I audio .\dist\Class-Widgets\audio
   ```
8. Class Widgets is now ready to be used. You can find the build output in the `dist` folder.

## License
This project (Class Widgets) is released under the GPL-3.0 license. Please refer to the [LICENSE](./LICENSE) file for details.

## Acknowledgments
This program uses [zhiyiYo](https://github.com/zhiyiYo/)'s [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets) for the UI interface of the settings. This is an awesome project that provides a clean and modern UI for PyQt applications, and this project won't be that clean and user-friendly without it.

## Contributors

[![][contrib-image]][contrib-link]

[contrib-image]: https://contrib.rocks/image?repo=fred913/Class-Widgets

[contrib-link]: https://github.com/fred913/Class-Widgets/graphs/contributors

<!-- One more thing: credit whitechi73 for providing the contributors section template :D -->
