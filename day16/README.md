## Day 16

### Content of Day 16

![Content of Day 16](assets/IMG_20171216_082003.jpg)

Amount | Name | Note
--- | --- | ---
1 | RGB LED | w/ built-in resistor

### Task
The actual task was to build a simple *Scratch* program with sliders to manipulate the RGB LEDs.
Instead of *Scratch* I used the web framework *Flask* and simple *jQuery* sliders to change the values which are sent to the web server by *POST* requests.
To continuously adjust the duty cycle, the *PWM* driver must be run in a separate thread.

![Circuit of Day 16](assets/IMG_20171216_085133.jpg)
Circuit of day 16

### Result

![Result of Day 16](assets/day16_rgbSlider.gif)

Python script: [rgbLeds.py](rgbLeds.py)
Flask templates:
- [index.html](templates/index.html)
- [layout.html](templates/layout.html)
