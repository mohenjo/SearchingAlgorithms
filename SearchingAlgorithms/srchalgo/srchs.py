# -*- coding: utf-8 -*-
import srchalgo._validation as valchk


# region Linear Search


def linear_search(seq, srchval):
    """Linear Search

    Args:
        seq: 검색 대상
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)

    for idx in range(len(seq)):
        if seq[idx] == srchval:
            return idx

    return -1


# endregion

# region Binary Search


def iterative_binary_search(seq, srchval):
    """Iterative Binary Search

    Args:
        seq: 검색 대상. 중복값이 없는 오름차순 정렬 시퀀스입니다.
        srchval: 검색 값

    Returns:
        int:검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)
    valchk.chkif_uniquified(seq)

    startidx = 0
    endidx = len(seq) - 1

    while startidx <= endidx:
        mididx = startidx + (endidx - startidx) // 2
        if seq[mididx] == srchval:
            return mididx
        elif seq[mididx] < srchval:
            startidx = mididx + 1
        else:
            endidx = mididx - 1

    return -1


def recursive_binary_search(seq, srchval):
    """Recursive Binary Search

    Args:
        seq: 검색 대상. 중복값이 없는 오름차순 정렬 시퀀스입니다.
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)
    valchk.chkif_uniquified(seq)

    return _recursive_binary_search(seq, 0, len(seq) - 1, srchval)


def _recursive_binary_search(seq, startidx, endidx, srchval):
    if startidx <= endidx:
        mididx = startidx + (endidx - startidx) // 2
        if seq[mididx] == srchval:
            return mididx
        elif seq[mididx] < srchval:
            return _recursive_binary_search(seq, mididx + 1, endidx, srchval)
        else:
            return _recursive_binary_search(seq, startidx, mididx - 1, srchval)
    else:
        return -1


# endregion

# region Jump Search


def jump_search(seq, srchval):
    """Jump Search

    Args:
        seq: 검색 대상. 오름차순으로 정렬되어 있어야 합니다.
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)

    length = len(seq)
    step = int(length ** 0.5)

    curidx = 0
    nxtidx = min(curidx + step - 1, length - 1)
    while seq[nxtidx] < srchval:
        curidx += step - 1
        nxtidx = min(curidx + step - 1, length - 1)
        if curidx > length - 1:
            return -1
    for idx in range(curidx, nxtidx + 1):
        if seq[idx] == srchval:
            return idx
    return -1


# endregion

# region Interpolation Search


def interpolation_search(seq, srchval):
    """Interpolation Search

    Args:
        seq: 검색 대상. 중복값이 없는 오름차순 정렬 시퀀스입니다.
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)
    valchk.chkif_uniquified(seq)

    startidx = 0
    endidx = len(seq) - 1

    while startidx <= endidx and seq[startidx] <= srchval <= seq[endidx]:
        if startidx == endidx:
            return startidx if seq[startidx] == srchval else -1
        pos = startidx + int(
            (srchval - seq[startidx])
            * (endidx - startidx)
            / (seq[endidx] - seq[startidx])
        )

        if srchval == seq[pos]:
            return pos
        elif srchval > seq[pos]:
            startidx = pos + 1
        else:
            endidx = pos - 1

    return -1


# endregion

# region Exponential Search


def exponential_search(seq, srchval):
    """Exponential Search

    Args:
        seq: 검색 대상. 중복값이 없는 오름차순 정렬 시퀀스입니다..
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)
    valchk.chkif_uniquified(seq)

    length = len(seq)

    if seq[0] == srchval:
        return 0

    idx = 1
    while idx < length and seq[idx] < srchval:
        idx *= 2

    return _recursive_binary_search(seq, idx // 2, min(idx, length - 1), srchval)


# endregion

# region Fibonaccvi Search


def fibonacci_search(seq, srchval):
    """Fibonacci Search

    Args:
        seq: 검색 대상. 중복값이 없는 오름차순 정렬 시퀀스입니다..
        srchval: 검색 값

    Returns:
        int: 검색 값의 최초 인덱스. 존재하지 않을 경우 -1을 반환합니다.
    """

    # 개체 유효성 검사
    valchk.chkif_searchable(seq)
    valchk.chkif_sorted(seq)
    valchk.chkif_uniquified(seq)

    length = len(seq)

    fib_2 = 0
    fib_1 = 1
    fib_0 = fib_2 + fib_1

    while fib_0 < length:
        fib_2 = fib_1
        fib_1 = fib_0
        fib_0 = fib_2 + fib_1

    offset = -1
    while fib_0 > 1:
        idx = min(offset + fib_2, length - 1)
        if seq[idx] == srchval:
            return idx
        elif seq[idx] > srchval:
            fib_0 = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_0 - fib_1
        elif seq[idx] < srchval:
            fib_0 = fib_1
            fib_1 = fib_2
            fib_2 = fib_0 - fib_1
            offset = idx

    if fib_1 == 1 and seq[offset] == srchval:
        return offset
    return -1


# endregion


if __name__ == "__main__":
    pass

