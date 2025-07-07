import requests
import webbrowser
from PyQt6.QtWidgets import QMessageBox
from .version import __version__

GITHUB_REPO = "slysmoke/ntt-demo"

def get_latest_release():
    """Fetches the latest release information from GitHub."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching latest release: {e}")
        return None

def check_for_updates(parent):
    """Checks for updates and prompts the user if a new version is available."""
    latest_release = get_latest_release()
    if not latest_release:
        QMessageBox.information(parent, "Update Check", "Could not fetch release information.")
        return

    latest_version = latest_release["tag_name"].lstrip('v')
    if latest_version > __version__:
        reply = QMessageBox.question(parent, "Update Available", 
                                     f"A new version ({latest_version}) is available. Open download page?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            webbrowser.open(latest_release["html_url"])
    else:
        QMessageBox.information(parent, "Update Check", "You are using the latest version.")
