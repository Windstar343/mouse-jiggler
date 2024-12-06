# 🖱️ Mouse Jiggler with Keyboard Control 🖥️

A simple Python script to keep your computer active by wiggling the mouse. Activate and deactivate the jiggler with the `F5` key. Perfect for avoiding idle status during online meetings or long breaks!

## 🚀 Features
- **Random Mouse Movements**: Simulates natural mouse behavior by moving to random positions.
- **Toggle Control**: Start or stop the jiggler anytime using the `F5` key.
- **Lightweight & Easy to Use**: Requires minimal setup and runs in the background.

## 🛠️ Requirements
- Python 3.6 or later
- Install the required Python packages using:
```bash
pip install pyautogui pynput
```

## 📋 Usage
1. Clone this repository or copy the script.
2. Install the dependencies listed above.
3. Run the script:
```bash
python mouse_jiggler.py
```
4. Press F5 to start or stop the mouse jiggler.

## 📄 Code Overview
### Main Components:
- Mouse Wiggling: The wiggle_mouse function moves the mouse to random nearby positions every 5 seconds.
- Keyboard Listener: The script listens for F5 key presses to toggle the jiggler on and off.

### Key Functions:
```python
def wiggle_mouse():
    # Moves the mouse randomly every 5 seconds when active.
    
def on_press(key):
    # Toggles the jiggler with the F5 key.
```

## 🖼️ Preview
When activated, the script:

- Randomly moves the mouse by ±50 pixels.
- Displays a message in the terminal:
```arduino
Mouse jiggler started. Press F5 to stop.
```

## 🔒 Notes
- System Impact: Minimal CPU usage.
- Responsibility: Use this tool ethically and consider workplace or system policies.

## 💡 Ideas for Improvement
- Add a GUI to control settings (e.g., jiggle interval, distance).
- Add support for customizable toggle keys.

Enjoy your uninterrupted sessions! 😄