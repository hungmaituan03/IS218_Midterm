"""
Plugin System Module

This module implements a system for dynamically loading and executing plugins
for the Advanced Python Calculator.
"""

import importlib
from pathlib import Path

class PluginSystem:
    """A class for managing and executing plugins in the calculator."""
    def __init__(self):
        """Initializes the PluginSystem and loads available plugins."""
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Loads plugins from the 'plugins' directory and registers them.

        This method iterates through all Python files in the 'plugins' folder,
        imports them as modules, and stores them in the `plugins` dictionary.
        """
        plugin_folder = Path("plugins")
        if plugin_folder.exists():
            for plugin_file in plugin_folder.glob("*.py"):
                plugin_name = plugin_file.stem
                plugin_module = importlib.import_module(f"plugins.{plugin_name}")
                self.plugins[plugin_name] = plugin_module

    def execute_plugin(self, plugin_command):
        """Executes a plugin based on the given command.

        Args:
            plugin_command (str): The name of the plugin to execute.

        Raises:
            KeyError: If the specified plugin is not found in the `plugins` dictionary.
        """
        if plugin_command in self.plugins:
            self.plugins[plugin_command].execute()
        else:
            print(f"Plugin '{plugin_command}' not found.")
