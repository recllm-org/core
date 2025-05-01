from dotenv import dotenv_values
import os



class EnvVars:
  """
  Environment variables
    - `envars` is a dictionary of environment variables
    - `get` is a method to get an environment variable
  
  `get`
    - If `include_os` is `True`, the environment variable is searched in both `os.environ` and `envars`
    - If `include_os` is `False`, the environment variable is only searched in `envars`
  """

  envars = dotenv_values('.env')
  
  @staticmethod
  def get(key, include_os=True): # include_os is useful if there are namespace conflicts, ie same key in .env and os.environ
    if include_os:
      return EnvVars.envars.get(key) or os.environ.get(key)
    else:
      return EnvVars.envars.get(key)