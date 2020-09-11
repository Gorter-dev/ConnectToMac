# ConnectToMac

ConnectToMap is a python script with a tkinter GUI. All it basically is execute a few commands with button presses. 

ONLY ANDROID AND MAC.

## Download

The pre-compiled version can be downloaded at:

[![Download ConnectToMac](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/connect-phone-mac/files/latest/download)

## Installation

To run the script:

```bash
./connectToMac.py
```

To build a .app file for MacOSX

```bash
python3 setup.py py2app --emulate-shell-environment
```

## Usage

Insert IP and press the button to connect to your android device.

### First time using program

You have to plug in your device and allow usb debugging. 

Then restart the service by:

```bash
adb tcpip 5555
```

Now you should be able to connect wirelessly.

NOTE: You can connect to multiple devices at the same time.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Roadmap
This is an ongoing project, the first next thing I want to implement is the logcat. I am also thinking of a new design. 

Feel free to recommend any idea's

## License
[MIT](https://choosealicense.com/licenses/mit/)
