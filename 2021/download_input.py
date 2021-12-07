from os import makedirs, getenv
from pathlib import Path

import fire
import requests

AOC_COOKIE = "53616c7465645f5f334ba9bc2108908bd4e1c500747719452d47b9121405a4b41a78805009a95fcd6429672a62a6e87f"

def download_input(task):
    task = str(task)
    p = Path(f"t{task}") / 'input.txt'

    if not p.parent.exists():
        makedirs(p.parent.as_posix(), exist_ok=True)

    with p.open('w') as fh:
        resp = requests.get(
            f'https://adventofcode.com/2021/day/{task.lstrip("0")}/input',
            cookies={'session': getenv('AOC_COOKIE')}
        )
        fh.write(resp.text)


if __name__ == '__main__':
    fire.Fire(download_input)