# ; Напишите программу, принимающую у пользователя ввод построчно количества слов n и далее всех слов построчно, 
# ; и, выводящую построчно количество уникальных слов, а далее количество повторений каждого слова в порядке их поступления от пользователя.

n = int(input("N=").strip())
wordlist = []
wordcount = []

for i in range(0,n):
    word = input().strip()
    wordlist.append(word)

print ("Количество уникальных слов = "+str(len(set(wordlist))))

wordlistcopy = []

for word in wordlist:
    if word in wordlistcopy:
        next
    else:
        wordlistcopy.append(word)
        wordcount.append(wordlist.count(word))


print ("Кол-во повторений слов",wordcount)
