import re
from typing import List
from pathlib import Path

import requests

HEADERS = {
    'authority': 'adventofcode.com',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://adventofcode.com/2020',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pl;q=0.7',
    'cookie': 'session=53616c7465645f5f464b9d9d3eb56d929178adc64b6e322d8292992ea3a376fd78d0a8e362dd92fe3fa745ca9734615b',
}


def read_files(folder: str, fname: str = 'input.txt'):
    """Read file in repo, assumes in main ~/aoc folder"""
    with open(Path(folder) / fname) as f:
        raw = f.readlines()
    return [line.strip() for line in raw]


def download_file(folder: str) -> List[str]:
    """Download the input file from AoC to the specific subfolder"""
    day_num = re.search(r'\d+', folder).group()
    url = f"https://adventofcode.com/2020/day/{day_num}/input"
    resp = requests.get(url, headers=HEADERS)
    with open(f'{folder}/input.txt', 'w') as f:
        f.write(resp.text)
    return resp.text.split('\n')
