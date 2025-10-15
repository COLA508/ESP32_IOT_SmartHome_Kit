Frequently Asked Questions
=========================

*1.The development board is not recognized or the program cannot be burned.*
 - Please make sure the CH340 driver is correctly installed on your computer.
 - Use a Type-C data cable (make sure it supports data transmission, not just charging).
 - Open the Device Manager and check if the "USB-SERIAL CH340" device appears.
 - If the port number is occupied, reconnect the USB or restart the computer.

----

*2.The serial monitor output is garbled.*
 - Please set the serial port baud rate to 115200 baud in the Arduino IDE.
 - If garbled characters persist, please confirm that the line "Serial.begin(115200);" in the example code is consistent.
 