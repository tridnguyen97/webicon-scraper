from csv import DictReader
from pathlib import Path


def get_domain_path() -> str:
    domain_file_name = "domains.csv"
    return Path.cwd() / "assets" / domain_file_name


def get_icon_url(domain_path: str, size: int = 64) -> list:
    """Transfer domain url and size parameters into icon URL from hidden Google URL.

    Parameters
    ----------
    domain_path: str, required
        path of file containing list of required domain,
        domain format example: reddit.com, google.com
    size: int, optional
        size of icon

    Returns
    -------
    List of icon URL

    """
    domain_list = []
    with open(domain_path, "r") as domain_list_f:
        reader = DictReader(domain_list_f)
        for row in reader:
            icon_url = f"https://www.google.com/s2/favicons?sz={size}&domain_url={row['domain']}"
            domain_list.append(icon_url)
    return domain_list
