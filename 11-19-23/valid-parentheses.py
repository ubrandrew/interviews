class Solution:
    def isValid(self, s: str) -> bool:
        # {}
        # {{}}
        # {(})
        # {(}
        # {())

        # if length of s is uneven, we know to return false
        # if s is empty, then return true

        # {{}}
        # after iterating through the entire string, if the queue/stack is empty, valid.
        # if we ever encounter parentheses that dont match, we can return false

        # need to maintain a pairing between open and closed parentheses
        closeToOpenParen = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        # lets use a queue, most recent is going to be at the end of the queue and we can 
        # just pop it from the end of the queue once weve processed it
        parenTracker = deque()
        for paren in s:
            if paren not in closeToOpenParen:
                parenTracker.append(paren)
            elif len(parenTracker) == 0 or closeToOpenParen[paren] != parenTracker.pop():
                    return False
        if len(parenTracker) > 0:
            return False
        return True