To uninstall Python 3.10.12 and install the latest version on Ubuntu, follow these steps:

### 1. Uninstall Python 3.10.12

First, check if Python 3.10 is installed through `apt`:

```bash
sudo apt list --installed | grep python3.10
```

If it’s installed via `apt`, you can remove it using:

```bash
sudo apt remove python3.10
sudo apt autoremove
```

If you installed Python 3.10 from a source, you may need to delete it from its installation directory (usually `/usr/local` or `/usr`). Ensure to check the installation path used during the original setup.

### 2. Install the Latest Python Version

#### Option 1: Install Python via `apt` (if Ubuntu provides the latest version)

1. **Update your system:**

   ```bash
   sudo apt update
   ```

2. **Install Python (latest available via `apt`):**

   ```bash
   sudo apt install python3
   ```

3. **Verify the version:**

   ```bash
   python3 --version
   ```

#### Option 2: Install Python from the Source (for the absolute latest release)

1. **Install prerequisites:**

   ```bash
   sudo apt update
   sudo apt install -y wget build-essential libssl-dev libffi-dev zlib1g-dev
   ```

2. **Download the latest Python source code from the official site:**

   ```bash
   wget https://www.python.org/ftp/python/<latest_version>/Python-<latest_version>.tgz
   ```

   Replace `<latest_version>` with the latest Python version (e.g., `3.12.0`).

3. **Extract and install:**

   ```bash
   tar -xvf Python-<latest_version>.tgz
   cd Python-<latest_version>
   ./configure --enable-optimizations
   make -j $(nproc)
   sudo make altinstall
   ```

4. **Verify the new Python installation:**

   ```bash
   python3.<latest_minor_version> --version
   ```

You’ll now have the latest Python installed on your system.
