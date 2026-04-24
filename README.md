# Modrinth-Shader-Downloader
It is an efficient asynchronous Python application designed for automatic search, selection, and download of Minecraft shader packages from Modrinth API based on filtering the required game version and selecting the most appropriate one (either latest or featured). 

The project structure consists of separate modules that deal with interacting with the API, version selection, filename generation, and package download respectively.

---

## ▶️ How to run

### 1. Install requirements

Make sure you have Python 3.9+ installed, then install dependencies:

```bash
pip install aiohttp
```

---

### 2. Configure settings (optional)

Edit `config.py` if you want to change:

```python
GAME_VERSION = "1.8.9"   # target Minecraft version
LIMIT = 100              # results per request
CONCURRENCY = 10         # async workers
OUTPUT_DIR = "shaders"   # download folder
```

---

### 3. Run the downloader

From the root folder:

```bash
python main.py
```

---

### 4. Output

Downloaded shaders will appear in:

```
shaders/
  ComplementaryShaders-Reimagined.zip
  VHSSHader.zip
  ...
```

---

## ⚠️ Notes
* Existing files are automatically skipped
* Only one version per shader is downloaded (latest or featured)
* Network speed and API limits may affect performance
