def is_valid(s: str) -> bool:
    stack: list[str] = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in pairs and (not stack or stack.pop() != pairs[ch]):
            return False
        elif ch not in pairs:
            stack.append(ch)
    return not stack
