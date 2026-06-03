import os

# Automatically create a 'bite' symlink pointing to 'src' in the project root.
# This allows users to `import bite` instead of `import src` after `pip install -e .`
project_root = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(project_root, 'src')
bite_link = os.path.join(project_root, 'bite')

if not os.path.exists(bite_link):
    os.symlink('src', bite_link, target_is_directory=True)
    print(f"[BITE] Created symlink: bite -> src")

from setuptools import setup

setup()
