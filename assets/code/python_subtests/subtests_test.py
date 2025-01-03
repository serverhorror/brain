from typing import Optional
import unittest
from dataclasses import dataclass

import pytest
import pytest_subtests as subtests


def divisableByTwo(v: int) -> Optional[Exception]:
    if v % 2 != 0:
        raise Exception("not divisable by two")
    return None


@dataclass
class Case:
    v: int
    wantErr: bool
    raises: Exception


class TestExampleSubtest(unittest.TestCase):
    def test_TICKET123(self):
        tc = [
            Case(v=1, wantErr=True, raises=Exception),
            Case(v=2, wantErr=False, raises=None),
        ]
        for tt in tc:
            with self.subTest("TICKET-123", i=tt.v):
                if tt.wantErr:
                    self.assertRaises(tt.raises, divisableByTwo, tt.v)
                elif not tt.wantErr:
                    self.assertEqual(divisableByTwo(tt.v), None)


def test_TICKET123(subtests):
    tc = [
        Case(v=1, wantErr=True, raises=Exception),
        Case(v=2, wantErr=False, raises=None),
    ]
    for i, tt in enumerate(tc):
        with subtests.test("TICKET123", i=i):
            if tt.wantErr:
                with pytest.raises(tt.raises):
                    divisableByTwo(tt.v)
            elif not tt.wantErr:
                assert divisableByTwo(tt.v) == None
