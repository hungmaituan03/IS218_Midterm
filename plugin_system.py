# plugin_system.py
import importlib
from pathlib import Path

class PluginSystem:
    def __init__(self):
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        plugin_folder = Path("plugins")
        if plugin_folder.exists():
            for plugin_file in plugin_folder.glob("*.py"):
                plugin_name = plugin_file.stem
                plugin_module = importlib.import_module(f"plugins.{plugin_name}")
                self.plugins[plugin_name] = plugin_module

    def execute_plugin(self, plugin_command):
        if plugin_command in self.plugins:
            self.plugins[plugin_command].execute()
        else:
            print(f"Plugin '{plugin_command}' not found.")
