from random import choice, choices
from string import ascii_lowercase as lw
from typing import List, Union
import meet_generator


def generate_meet(*, k: int = 1) -> Union[str, List[str]]:
    """Generates google meet realistic links

    Args:
        times (int, Optional): 
            The amount of links to generate, 1 by default.

    Returns:
        typing.Union[str, List[str]): 
            A single link or a list
    """
    links = []

    for _ in range(k):
        code = [
            ''.join(choices(lw, k=(4 if i == 1 else 3)))
            for i in range(3)
        ]
        links.append(
            meet_generator.base_url +
            '-'.join(code)
        )

    if len(links) == 1:
        return links[0]

    return links
