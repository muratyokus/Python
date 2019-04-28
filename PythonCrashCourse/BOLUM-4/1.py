pizza = ['sucuklu','kasarli','acili','peynirli']
friend_pizza = pizza
pizza.append('soslu')
friend_pizza.append('karisik')

print('Pizza listesi hazir!')

print('Benim favori pizzalarim: ')
for pizzam in pizza:
    print(pizzam.title())

print('\nMy friends favorites pizza: ')
for friends_pizza in friend_pizza:
    print(friends_pizza.title())

