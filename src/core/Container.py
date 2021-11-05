import os
from src.core.Tokens import Tokens

# Initialize token class.
tokens = Tokens()

# Needed computer paths.
pc_roaming = os.getenv('APPDATA')
pc_local = os.getenv('LOCALAPPDATA')
