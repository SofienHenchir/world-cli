# World CLI

World CLI is a simple Python command-line app that lets you search for a country and fetch country data from an external API.

## Features

- Greets the user
- Asks for your name
- Asks for a country name
- Sends a request using:
  - `BASE_URL` from environment variables
  - `API_Key` as the `X-Api-Key` request header
- Prints the API JSON response in the terminal

## Project Structure

- `world/cli.py` - main CLI entry point
- `world/__init__.py` - package marker
- `pyproject.toml` - project metadata and CLI script registration
- `requirements.txt` - pinned dependencies

## Requirements

- Python 3.10 or newer
- Internet connection
- API key from API Ninjas: https://api-ninjas.com/api/country#country-endpoint

## Environment Variables

Create a `.env` file in the project root with:

```env
API_Key=your_api_key
BASE_URL=https://api.api-ninjas.com/v1/country?name=
```

## Installation

1. Clone or download this project.
2. Open a terminal in the project root.
3. Create and activate a virtual environment.
4. Install dependencies.
5. Install the project in editable mode so the `world` command is available.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Run the App

```bash
world
```

Then follow the prompts:
- Enter your name
- Enter a country name

## Example

```text
Welcome to World CLI!
Enter your name: Sofien
Enter a country name: Tunisia
Sofien is looking for informations aboutt Tunisia.. Fetching data ..
{ ...API response JSON... }
```

## Notes

- `pip install -r requirements.txt` installs all third-party dependencies.
- `pip install -e .` registers the `world` command from `pyproject.toml`.
- If `world` is not recognized, activate your virtual environment and run `pip install -e .` again.