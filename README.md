**House Code Raspberry Pi Software**


<sub>
This is a software package for the House Code project that runs on a Raspberry Pi. It provides a user interface accessible through a local host and enables control of smart home devices.
</sub>

**Requirements**


* <sub>Raspberry Pi with Raspbian installed</sub>
* <sub>Python 3.6 or later</sub>
* <sub>Flask module</sub>
* <sub>PySerial module</sub>
* <sub>Arduino Uno or compatible microcontroller</sub>
* <sub>Smart home devices compatible with the microcontroller</sub>


**Installation**

1.  <sub>Connect the Arduino Uno or compatible microcontroller to the Raspberry Pi.</sub>
2.  <sub>Install Python 3.6 or later if it is not already installed on the Raspberry Pi.</sub>
3.  <sub>Install the Flask and PySerial modules by running the following command in the terminal:</sub>
    ```
    pip install flask pyserial
    ```
4. <sub>Clone or download the repository to the Raspberry Pi.</sub>
5. <sub>Open the terminal and navigate to the HouseCode_raspi directory.</sub>
6. <sub>Run the main.py file using the following command:
    ```
    python main.py
    ```
    This will start the Flask server and the user interface will be accessible through a web browser at http://localhost:5000/.</sub>

7. <sub>Connect the smart home devices to the microcontroller according to the project specifications.</sub>


**Usage**

<sub>
The user interface provides the following features:
</sub>

* <sub> Display of real-time data from the smart home devices</sub>
* <sub> Control of the smart home devices using the on-screen buttons</sub>
* <sub> Monitoring and logging of the device status and usage history</sub>
* <sub> Configuration of the device settings and preferences</sub>


**Troubleshooting**

* <sub> If the Flask server fails to start or the web page does not load, check that the required modules are installed correctly and that the microcontroller is connected properly.</sub>
* <sub> If the smart home devices are not responding or behaving unexpectedly, check that they are properly connected to the microcontroller and that the device configurations are correct.</sub>

**Disclaimer**


<sub>This software package is provided as-is and is intended for educational and experimental purposes only. Use at your own risk. The creators and contributors of this software are not responsible for any damages or consequences arising from its use. </sub>



