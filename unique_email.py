class Solution(object):
    def numUniqueEmails(self, emails):
        final_list = []
        for email in emails:
            seperate = email.split('@')

            if seperate[0].count('.') != 0:
                seperate[0].replace('.','')

            if seperate[0].count('+') != 0:
                temp = seperate[0].split('+')
                temp += seperate[1]
                final_list.append(temp)
            else:
                temp = seperate[0] + seperate[1]
                final_list.append(temp)
        set_final = set(final_list)
        return  len(set_final)

test = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(test.numUniqueEmails(emails))