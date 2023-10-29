

import itertools
import zipfile 
import os


# ans=list('000000')
# l=list('0123456789abcdefghijklmnopqrstuvwxyz')
#l.sort(reverse=True)

# for a in range(len(ans)):
#     for aa in range(len(l)):
#         ans[a]=l[aa]
#         print(ans)
#         if ans=='xxxxxx':
#             break
#     for b in range(1,len(ans)):
#         for bb in range(len(l)):
#             ans[b]=l[bb]
#             print(ans)
#         if ans=='xxxxxx':
#             break
#         for c in range(2,len(ans)):
#             for cc in range(len(l)):
#                 ans[c]=l[cc]
#                 print(ans)
#                 if ans=='xxxxxx':
#                     break
#             for d in range(3,len(ans)):
#                 for dd in range(len(l)):
#                     ans[d]=l[dd]
#                     print(ans)
#                     if ans=='xxxxxx':
#                         break
#                 for e in range(4,len(ans)):
#                     for ee in range(len(l)):
#                         ans[e]=l[ee]
#                         print(ans)
#                         if ans=='xxxxxx':
#                             break
#                     for f in range(5,len(ans)):
#                         for ff in range(len(l)):
#                             ans[f]=l[ff]
#                             print(ans)
#                             if ans=='xxxxxx':
#                                 break


# for a in range(len(ans)):
#     for aa in range(len(l)):
#         ans[a]=l[aa]
#         print(ans)
#         if ans=='xxxxxx':
#             break
#     for bb in range(len(l)):
#         ans[a+1]=l[bb]
#         print(ans)
#         if ans=='xxxxxx':
#             break
#     for cc in range(len(l)):
#         ans[a+2]=l[cc]
#         print(ans)
#         if ans=='xxxxxx':
#                 break
#     for dd in range(len(l)):
#         ans[a+3]=l[dd]
#         print(ans)
#         if ans=='xxxxxx':
#             break
#     for ee in range(len(l)):
#         ans[a+4]=l[ee]
#         print(ans)
#         if ans=='xxxxxx':
#             break
#     for ff in range(len(l)):
#         ans[a+5]=l[ff]
#         print(ans)
#         if ans=='xxxxxx':
#             break


passwd_string = "0123456789abcdefghijklmnopqrstuvwxyz"




for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:
            pwd="xxxxxx"
            if pwd==passwd:
                print (f"password: {passwd}")
                break
        except:
            pass


