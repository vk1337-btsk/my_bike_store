import os
from configparser import ConfigParser, NoSectionError


def get_data_from_config(name_section: str, base_dir: str) -> dict[str, str]:
    """This method gets a dictionary with data from the config.ini file."""
    filename = os.path.join(base_dir, "config.ini")
    parser = ConfigParser()
    try:
        parser.read(filename)
        return dict(parser.items(name_section))
    except NoSectionError as err_:
        raise Exception(f"Section '{name_section}' not found in '{filename}'") from err_
