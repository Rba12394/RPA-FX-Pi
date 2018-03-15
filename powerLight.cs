//Code is in C#
//Source: https://docs.microsoft.com/en-us/windows/iot-core/learn-about-hardware/pinmappings/pinmappingsrpi
//Altered last by: Blake Arledge
//Date: 3/15/18

using Windows.Devices.Gpio;

public void GPIO(){
    GpioPin pin1, pin2;
    // Get the default GPIO controller on the system
    GpioController gpio = GpioController.GetDefault();
    if (gpio == null)
        return; // GPIO not available on this system

    // Open GPIO 5
    using (pin1 = gpio.OpenPin(5) && pin2 = gpio.OpenPin(7)){

        // Latch HIGH value first. This ensures a default value when the pin is set as output
        pin1.Write(GpioPinValue.High);
        pin2.Write(GpioPinValue.Low);

        // Set the IO direction as output
        pin1.SetDriveMode(GpioPinDriveMode.Output);
	pin2.SetDriveMode(GpioPinDriveMode.Output);


    } // Close pin - will revert to its power-on state
    
    
}