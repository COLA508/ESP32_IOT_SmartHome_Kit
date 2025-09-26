Arduino IDE Getting Started Tutorial
====================================

Introduction
------------

*The Arduino IDE is an open-source programming tool officially provided by Arduino, supporting C/C++ development. It provides users with simple and intuitive code writing, compiling, and uploading functions, making it easy to burn programs to development boards such as Arduino and ESP32. The IDE includes extensive built-in example code and supports library file extensions, allowing developers to quickly access drivers for various sensors and modules, enabling a rich set of hardware interaction features. With its cross-platform support (Windows, macOS, and Linux), the Arduino IDE is widely used in education, makerspaces, and IoT development, making it an essential tool for both beginners and advanced embedded development learners.*

----

Install the Arduino IDE
-----------------------

This section will guide you through installing the **Arduino IDE** on Windows, macOS, and Linux systems.  


Install Arduino IDE on Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Visit the official Arduino website and go to the software download page:  
   `Arduino IDE Download <https://www.arduino.cc/en/software/>`_

   .. image:: _static/2.arduino_install.png
      :alt: Arduino IDE official website
      :align: center

2. Select the version that matches your computer configuration, then click the **Download** button to begin.  

.. note::

   - The Arduino IDE is updated frequently. To ensure compatibility, it is recommended to download the **latest official version**.

3. Run the installer by double-clicking the downloaded ``arduino-ide_xxxx.exe`` file.  

4. Read and accept the **License Agreement**.  

   .. image:: _static/3.Install_Arduino_IDE.png
      :alt: License Agreement window
      :align: center

5. Select the desired installation options.  

   .. image:: _static/4.Install_Arduino_IDE.png
      :alt: Installation options
      :align: center

6. Choose the installation path. It is recommended to install the software on a **non-system drive**.  

   .. image:: _static/5.Install_Arduino_IDE.png
      :alt: Installation path
      :align: center

7. Click **Install** and wait for the process to complete. Finally, click **Finish**.  

   .. image:: _static/6.Install_Arduino_IDE.png
      :alt: Installation finished
      :align: center


Install Arduino IDE on MacOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Double-click the downloaded ``arduino-ide_xxxx.dmg`` file.  

2. Drag and drop **Arduino IDE.app** into the **Applications** folder.  

3. After a few seconds, you will see Arduino IDE installed successfully.  

   .. image:: _static/7.Install_Arduino_IDE.png
      :width: 800
      :alt: Arduino IDE installation on macOS
      :align: center


Install Arduino IDE on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Linux users, please follow the official tutorial for Arduino IDE 2.0 installation:  

`Linux Installation Guide <https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux>`_


Open the Arduino IDE
~~~~~~~~~~~~~~~~~~~~

When you open Arduino IDE for the first time:  

- The software will automatically install the **Arduino AVR Boards**, built-in libraries, and other required files.  

   .. image:: _static/8.Install_Arduino_IDE.png
      :alt: First startup window
      :align: center

- During installation, your **firewall** or **security center** may ask for permission to install drivers. Please allow all requests.  

   .. image:: _static/9.Install_Arduino_IDE.png
      :alt: Driver installation prompt
      :align: center

Now your Arduino IDE is ready to use! 🎉  

.. note::

   - If some installations fail due to network issues, simply **reopen the Arduino IDE** and it will continue the remaining installation steps.  
   - The **Output Window** will not appear automatically after setup. It will only open when you click **Verify** or **Upload**.  

   