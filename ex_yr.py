from apyori import apriori

transactions=[
    ['beer','nuts'],
    ['beer','cheese'],
    ['beer','cheese','mlik'],
    ['milk','cheese'],
    ['milk','cheese','nuts']
]

results=list(apriori(transactions, min_support=0.3, min_confidence=0.5))
for res in results:
    print(res)