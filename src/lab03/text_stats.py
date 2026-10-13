from text import normalize, tokenize, count_freq, top_n

text=input()
FLAg = True 

norm = normalize(text)
token = tokenize(norm)
cnt_freq=count_freq(token)
top = top_n(cnt_freq)

print(f'Всего слов: {len(token)}')
print(f'Уникальных слов: {len(cnt_freq)}')

if FLAg:
    max_len = max([len(i[0]) for i in top] + [len('слово')])
    len_words = f"{'слово':<{max_len}} | частота"
    print(len_words)
    print('-' * len(len_words)) 
    for i in top:
        print(f"{i[0]:<{max_len}} | {i[1]}")
else:
    print('Топ-5:')
    for i in top:
        print(f'{i[0]}: {i[1]}')