import sys
from io import StringIO


def prepare_sample(sample: str):
    sys.stdin = StringIO(sample.strip() + '\n')
