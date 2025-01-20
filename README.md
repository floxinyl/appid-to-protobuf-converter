# AppID to Protobuf Converter

A simple tool to convert Steam AppIDs into protobuf-encoded values. 

Includes a Guide on how to private any game/program on Steam - whether the store page still exists or not. Also, you don't even need to own the games!

## 🚀 Features

- **Easy Conversion**: Input a Steam AppID, and get the protobuf-encoded value instantly.
- **Game Info**: Automatically fetches and displays the game name.
- **Clipboard Integration**: The protobuf value is automatically copied for your convenience.
- **Prebuilt Executable**: Download the tool and use it instantly without any setup.

## 👅 Download

Get the latest version here:

👉 [Download the .exe](https://github.com/floxinyl/appid-to-protobuf-converter/releases/latest/download/appid_to_protobuf_gui.exe)

_No installation required. Just download and run!_

---

## 🛠️ Usage

1. **Run the Tool**:
   - Double-click the downloaded `.exe` to open the application.

2. **Convert an AppID**:
   - Enter a valid Steam AppID into the input box.
   - Click **Convert**.
   - View the game name and protobuf value.
   - The protobuf value is automatically copied to your clipboard.

---

## 📖 How to Use Postman to Private Steam Games

You can manually send an API request to Steam using Postman to hide your games. Here's how:

1. **Download and Open Postman**:
   - [Download Postman](https://www.postman.com/downloads/) and install it.

2. **Create a POST Request**:
   - URL:  
     ```
     https://api.steampowered.com/IAccountPrivateAppsService/ToggleAppPrivacy/v1?access_token=YOUR_ACCESS_TOKEN
     ```
   - Replace `YOUR_ACCESS_TOKEN` with your Steam Access Token. Don't know how? -> [Get Your Access Token](https://github.com/floxinyl/appid-to-protobuf-converter?tab=readme-ov-file#-how-to-get-your-access-token)

3. **Set the Body**:
   - Go to the **Body** tab and select **form-data**.
   - Add the following fields:
     | Key                   | Value                          |
     |-----------------------|--------------------------------|
     | `access_token`        | YOUR_ACCESS_TOKEN             |
     | `input_protobuf_encoded` | YOUR_PROTOBUF_ENCODED_VALUE |

   - Replace `YOUR_ACCESS_TOKEN` and `YOUR_PROTOBUF_ENCODED_VALUE` with the appropriate values.

4. **Send the Request**:
   - Click **Send** and verify a `200 OK` response.

---

## 🔍 How to Get Your Access Token

To hide games using Postman or similar tools, you need your Steam access token. Here's how to find it:

1. **Open the Steam Website**:
   - Visit [https://steamcommunity.com/my](https://steamcommunity.com/my) and log in to your account.

2. **Access Developer Tools**:
   - Press `F12` or right-click anywhere on the page and select **Inspect**.
   - Navigate to the **Network** tab in the developer tools.

3. **Reload the Page**:
   - Press `CTRL+R` to reload the page while keeping the developer tools open.

4. **Find the Access Token**:
   - Look for a network request with `v1?access_token=` in its URL.
   - Click on the request to view its details.

5. **Copy the Token**:
   - Go to the **Payload** tab of the request details.
   - Find the `access_token` field and copy the long string following it.

   > **⚠️ Important**: Keep your access token private. Sharing it can compromise your Steam account security.

Once you have the token, you can use it with Postman or other tools to send requests to Steam's API.

---

## 💻 Building From Source (Optional)

If you want to build the executable yourself:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/floxinyl/appid-to-protobuf-converter.git
   cd appid-to-protobuf-converter
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

3. **Run the Application**:
   ```bash
   python appid_to_protobuf_gui.py
   ```

4. **Build the Executable** (Optional):
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --noconsole appid_to_protobuf_gui.py
   ```

---

## 📨 Contact

For issues or suggestions, visit the [GitHub Issues](https://github.com/floxinyl/appid-to-protobuf-converter/issues) page or write me on [X](https://x.com/floxinyl)

