class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        local = []
        for i in range(len(emails)):
            start, end = emails[i].split('@')
            start = start.replace('.', '')
            if '+' in start:
                start = start.split('+')[0]
            local.append(start+'@'+end)
        valid = set(local)
        return len(valid)
        
