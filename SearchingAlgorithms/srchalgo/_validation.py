# _*_ coding:utf-8 --*-
"""입력 시퀀스의 유효성 검사를 위한 모듈입니다."""


def chkif_searchable(seq):
    """검색 기능의 적용이 가능한 개체인지 검사합니다."""
    if not hasattr(seq, "__getitem__"):
        raise TypeError(f"{type(seq).__name__} is not subscriptable.")


def chkif_sorted(seq):
    """정렬이 되어 있는 시퀀스인지 검사합니다."""
    if list(seq) != sorted(seq):
        raise ValueError(f"{type(seq).__name__} is not sorted.")


def chkif_uniquified(seq):
    """시퀀스 내 중복된 요소가 없는지 검사합니다."""
    if len(seq) > len(set(seq)):
        raise ValueError(f"{type(seq).__name__} has duplicated elements.")
