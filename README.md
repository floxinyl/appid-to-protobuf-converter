# AppID to Protobuf Converter

This is a simple tool that converts Steam AppIDs into protobuf-encoded values. You need those to manually mark any game as private using API. You will be able to hide **ANY GAME AND PROGRAM** on your *Recent Activity* feed on your Steam Profile, even if the Store Page doesn't exist anymore. In that case hover over the game icon in your **Browser** and write down the APPID from the Link in the *bottom left*.

## Features

- **Convert Steam AppIDs**: Quickly generate protobuf-encoded values for any valid STEAM AppID.
- **Game/Program Name Fetch**: Automatically fetches and displays the game/program name for the provided AppID.
- **Clipboard Copy**: Copies the generated protobuf value to the clipboard and provides a notification.

## Download

You can download the latest version of the AppID to Protobuf Converter here.
This will not require you to download any of the Requirements to clone and use this repository.
*Recommended for any user on a Windows PC.*

[Click to Download the ready-to-use .exe](https://github.com/floxinyl/appid-to-protobuf-converter/releases/latest/download/appid_to_protobuf_gui.exe)

*alternatively click on releases on the right.* --->

## Requirements

- Python 3.x
- `requests` library
- `tkinter` (comes pre-installed with Python on most platforms)
- POSTMAN or similar API tools to send requests (scroll down for a simple guide)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/floxinyl/appid-to-protobuf-converter.git
   cd appid-to-protobuf-converter
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Run the application:
   ```bash
   python appid_to_protobuf_gui.py
   ```

## Usage

1. Enter the Steam AppID in the input box.
2. Click the **Convert** button.
3. The game name and the protobuf-encoded value will be displayed.
4. The protobuf value is automatically copied to your clipboard.

## Convert to Executable (Optional)

To make the program executable for easier sharing:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile --noconsole appid_to_protobuf_gui.py
   ```
3. The executable will be available in the `dist` folder.

## Using Postman to Hide Steam Games

Follow these steps to use Postman and send an API request to private your Steam games:

1. **Open Postman**:
   - Download and install Postman from [https://www.postman.com/downloads/](https://www.postman.com/downloads/).

2. **Create a New Request**:
   - Click **+ New Tab** to create a new request.
   - Set the method to **POST**.
   - Enter the following URL:
     ```
     https://api.steampowered.com/IAccountPrivateAppsService/ToggleAppPrivacy/v1?access_token=YOUR_ACCESS_TOKEN
     ```
     Replace `YOUR_ACCESS_TOKEN` with the valid Steam access token obtained via the network activity in your browser.
     There is many ways to get your *ACCESS_TOKEN*. If you don't know how:
     - 1. Open the Steam website in your browser and log into your account.
       2. Go to your profile: [https://steamcommunity.com/my](https://steamcommunity.com/my)
       3. Open the browser's developer tools (usually by pressing F12 or right-clicking and selecting Inspect).
       4. Go to the Network tab and hit **CTRL+R** to reload.
       5. There will be many entries. Look for **v1?access_token=*YOUR_ACCESS_TOKEN***
       6. Click on that entry. On the right side you will see *access_token:* followed by your Access Token in the PAYLOAD tab. Copy that long string.
          **>DO NOT SHARE THE ACCESS TOKEN, NOT EVEN WITH YOUR MOM! YOU WILL GET HACKED<**

3. **Set the Body**:
   - Go to the **Body** tab.
   - Select **form-data**.
   - Add the following fields:
     | Key                    | Value                                      |
     |------------------------|--------------------------------------------|
     | `access_token`         | YOUR_ACCESS_TOKEN                         |
     | `input_protobuf_encoded` | YOUR_PROTOBUF_ENCODED_VALUE               |
   - Replace `YOUR_ACCESS_TOKEN` with the actual access token.
   - Replace `YOUR_PROTOBUF_ENCODED_VALUE` with the protobuf value generated using this tool.

4. **Send the Request**:
   - Click the **Send** button in Postman.

5. **Verify the Response**:
   - **Status Code**: Look for `200 OK` indicating a successful request.
   - **Response Body**: If successful, the game's privacy status should change. If not, review the error message and adjust accordingly.

### Example
If the access token is `eyAidHlwIjogIkpXVC...` and the protobuf value is `CJqiFxAB`:
- **Access Token**: `eyAidHlwIjogIkpXVC...`  
- **Input Protobuf Encoded**: `CJqiFxAB`  

Make sure these values match your intended AppID and token.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For issues or suggestions, visit the [GitHub Issues](https://github.com/floxinyl/appid-to-protobuf-converter/issues) page.

