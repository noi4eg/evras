# ; Напишите программу, принимающую у пользователя ввод построчно количества слов n и далее всех слов построчно, 
# ; и, выводящую построчно количество уникальных слов, а далее количество повторений каждого слова в порядке их поступления от пользователя.

n = int(input().strip())
wordlist = []
for i in range(0,n):
    word = input().strip()
    wordlist.append(word)


wordset = set(wordlist)
wordsetlist = list(wordset)

print (wordlist)
print (len(wordset))
print (wordsetlist)
for elem in wordsetlist:
    print (elem, "встречается раз",wordlist.count(wordsetlist[elem]))