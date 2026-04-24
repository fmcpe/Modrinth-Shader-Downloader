# Modrinth-Shader-Downloader

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Async](https://img.shields.io/badge/async-aiohttp-green.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

An efficient asynchronous Python application designed to automatically search, select, and download Minecraft shader packs from the Modrinth API.

It filters shaders by a target game version and intelligently selects the most appropriate version (featured or latest), saving them with clean, consistent filenames.

## 📸 Example

### Terminal Output

```
Downloading: ComplementaryShaders-Reimagined.zip
Downloading: VHSSHader.zip
Skipping: BSL-Shaders.zip
```

### Output Folder

```
shaders/
  ComplementaryShaders-Reimagined.zip
  VHSSHader.zip
  BSL-Shaders.zip
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/fmcpe/modrinth-shader-downloader.git
cd modrinth-shader-downloader
```

---

### 2. Install requirements

```bash
pip install aiohttp
```

---

### 3. Configure settings (optional)

Edit `config.py`:

```python
GAME_VERSION = "1.8.9"   # Target Minecraft version

SHADER_LIMIT = -1        # -1 = unlimited downloads
LIMIT = 100              # API results per request
CONCURRENCY = 10         # Async workers
OUTPUT_DIR = "shaders"   # Download directory
```

---

### 4. Run the downloader

```bash
python main.py
```

---

## 📦 Output

All downloaded shaders will be saved in:

```
shaders/
  ShaderName.zip
```

---

## ⚙️ Configuration

| Option       | Description                        | Default |
| ------------ | ---------------------------------- | ------- |
| GAME_VERSION | Minecraft version filter           | 1.8.9   |
| SHADER_LIMIT | Max shaders to download (-1 = all) | -1      |
| LIMIT        | API results per request            | 100     |
| CONCURRENCY  | Number of async requests           | 10      |
| OUTPUT_DIR   | Download directory                 | shaders |

---

## 🧠 How It Works

1. Fetch shader projects from Modrinth API
2. Retrieve all versions for each project
3. Filter versions by the target Minecraft version
4. Select the best version:

   * Prefer **featured**
   * Fallback to **latest**
5. Download the file with a clean filename

---

## ⚠️ Notes

* Existing files are automatically skipped
* Only one version per shader is downloaded
* With high concurrency, downloads are significantly faster
* API rate limits may apply depending on usage

---

## 🤝 Contributing

Contributions are welcome.

If you want to improve this project:

* Open an issue
* Submit a pull request

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**.

---

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.
