import importlib
from pathlib import Path

class PluginSystem:
    """A class for managing and executing plugins in the calculator.""" 
    def __init__(self):
        """Initializes the PluginSystem and loads available plugins."""
        self.plugins = {}
        self.load_plugins()

    def load_plugins(self):
        """Loads plugins from the 'plugins' directory and registers them."""
        plugin_folder = Path("plugins")
        if plugin_folder.exists():
            for plugin_file in plugin_folder.glob("*.py"):
                plugin_name = plugin_file.stem
                self.register_plugin(plugin_name)

    def register_plugin(self, plugin_name):
        """Registers a plugin module by importing it and storing it."""
        try:
            plugin_module = importlib.import_module(f"plugins.{plugin_name}")
            self.plugins[plugin_name] = plugin_module
        except ImportError as e:
            print(f"Error loading plugin '{plugin_name}': {e}")

    def execute_plugin(self, plugin_command):
        """Executes a plugin based on the given command."""
        plugin = self.plugins.get(plugin_command)
        if plugin:
            if hasattr(plugin, 'execute'):
                plugin.execute()
            else:
                print(f"Plugin '{plugin_command}' does not have an 'execute' method.")
        else:
            print(f"Plugin '{plugin_command}' not found.")
