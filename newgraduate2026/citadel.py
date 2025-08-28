
def getMaxEarnings(schedule: str, k: int, fixedPay: int, bonus: int) -> int:
   
    n = len(schedule)
    if n == 0 or k <= 0:
        # quick compute without flips
        ones = schedule.count('1')
        if ones == 0:
            return 0
        # count runs
        runs = 0
        i = 0
        while i < n:
            if schedule[i] == '1':
                runs += 1
                while i < n and schedule[i] == '1':
                    i += 1
            else:
                i += 1
        return ones * (fixedPay + bonus) - bonus * runs

    s = schedule
    ones = s.count('1')

    # Case: no initial 1s -> best is one block of length L=min(k,n)
    if ones == 0:
        L = min(k, n)
        return 0 if L == 0 else L * (fixedPay + bonus) - bonus

    # Count runs and collect gaps
    runs = 0
    i = 0
    gaps = []
    left_zeros = 0
    right_zeros = 0

    # leading zeros
    while i < n and s[i] == '0':
        left_zeros += 1
        i += 1

    while i < n:
        runs += 1  # at start of a 1-run
        while i < n and s[i] == '1':
            i += 1
        j = i
        while j < n and s[j] == '0':
            j += 1
        zero_len = j - i
        if zero_len > 0:
            if j < n and s[j] == '1':
                gaps.append(zero_len)  # internal gap
            else:
                right_zeros = zero_len  # trailing zeros
        i = j

    # Base earnings
    base = ones * (fixedPay + bonus) - bonus * runs

    # Fill internal gaps (smallest first)
    gaps.sort()
    used = 0          # total zeros flipped so far
    run_delta = 0     # change to number of runs (negative means runs decreased)
    for g in gaps:
        if k >= g:
            k -= g
            used += g
            run_delta -= 1   # two runs merged
        else:
            used += k        # partial fill (no run change)
            k = 0
            break

    # Any remaining flips can be placed adjacent to existing 1s (edges or partially filled gaps)
    if k > 0:
        remaining_zeros = left_zeros + right_zeros + sum(gaps) - used
        extra = min(k, remaining_zeros)
        used += extra
        k -= extra

    # Final earnings
    return base + used * (fixedPay + bonus) - bonus * run_delta

# ---- Sample tests from the prompt ----
print("Sample 0")
print(getMaxEarnings("100101", 2, 4, 3))  # expected 29

print("Sample 1")
print(getMaxEarnings("1111001", 1, 3, 3))  # expected 30
print(getMaxEarnings("0000", 2, 5, 2))  # expected 18