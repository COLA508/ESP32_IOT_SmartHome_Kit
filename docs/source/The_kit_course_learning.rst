The  Kit Course Learning
========================

 - This kit not only provides you with a complete course curriculum but also guides you through a step-by-step in-depth study of the fundamentals and applications of the Internet of Things. 
 - In this section, we'll individually introduce each component and functional module included in the kit, from basic sensors and actuators to communication modules, to help you systematically understand their functions and usage. 
 - By studying the working principles of these components, you'll not only master how to connect and control modules in real-world projects, but also gain a deeper understanding of how IoT systems achieve environmental perception, intelligent linkage, and remote operation. 
 - This will lay a solid foundation for your subsequent experiments, course design, and IoT project development, allowing you to better grasp the core knowledge of smart hardware and the Internet of Things.

----

Course 1：LED Module
-------------------

**Working principle:** 
LED (Light Emitting Diode) is a semiconductor device that can emit light. When a forward voltage is applied, the LED conducts in a single direction and emits light. By controlling the high and low levels of the circuit it is connected to, it can be turned on or off.

**wiring:** LED Module → ESP32 GPIO26

**Sample Code:**

.. code-block:: cpp

   #include <Arduino.h>
   const int ledPin = 26;   // LED PIN
   const uint32_t freq = 5000;
   const uint8_t resolution = 8;  // 0-255
   void setup() {
     Serial.begin(115200);
     Serial.println("breathing light");

     ledcAttach(ledPin, freq, resolution);
   }

   void loop() {
     // Bright
     for (int duty = 0; duty <= 255; duty++) {
       ledcWrite(ledPin, duty);
       delay(2);
     }

     // dark
     for (int duty = 255; duty >= 0; duty--) {
       ledcWrite(ledPin, duty);
       delay(2);
     }
   }


**Code Explanation:**
delay(10): Wait 10ms each time the brightness is changed. You can change the breathing speed by changing the value.
 - Smaller value → faster breathing light
 - Larger value → slower breathing light

----

Course 2：Light Sensor
----------------------
