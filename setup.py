from setuptools import setup, find_packages
from pathlib import Path


this_dir = Path('.').resolve()


def _load_reqs(path: Path):
    reqs = []
    with open(path) as in_fp:
        for line in in_fp.readlines():
            line = line.rstrip('\n\r')
            reqs.append(line)
    return reqs


setup(
    name="vanguard",
    packages=find_packages(),
    install_requires=_load_reqs(this_dir / 'requirements' / 'install.pip.in'),
    tests_require=_load_reqs(this_dir / 'requirements' / 'devtools.pip.in'),
    entry_points={
        'console_scripts': [
            'vanguard-api=vanguard_api.__main__:main',
        ],
    },
)
