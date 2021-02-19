piles = [9,8,7,6,5,4,3,2,1]
num_triple_groups = int(len(piles) / 3)
piles.sort(reverse=True)

coin_count = 0

for x in range(num_triple_groups):
    print(x, 2*x + 1)
    coin_count += piles[2*x + 1]

print(coin_count)





# coin_list = []

# def coin_sort(input_pile):
#     output = []
#     output.append(input_pile[0])
#     output.append(input_pile[1])
#     output.append(input_pile[-1])
#     return output
# def coin_remove(input_pile):
#     output = input_pile
#     output.remove(input_pile[0])
#     output.remove(input_pile[1])
#     output.remove(input_pile[-1])
#     return output

# while len(piles) > 3:
#     print('Starting Piles', piles)
#     current_pile = coin_sort(piles)
#     coin_list.append(current_pile[1])
#     piles = coin_remove(piles)
#     print('Remaining Piles', piles)
#     print('Current Pile', current_pile)

# last_pile = coin_sort(piles)
# coin_list.append(last_pile[1])

# print('Final Coins', coin_list)
# print('Sum of Coins', sum(coin_list))






# for pile in range(num_triple_groups):
#     coin_list.append(piles[pile*3+1])

# print(coin_list)
# print(sum(coin_list))
