def get_value(rank) -> int:
    if rank in 'ДВК':
        return 10
    
    elif rank == 'Т':
        return (1, 11)
    
    else:
        return ['2', '3', '4', '5', '6', '7', '8', '9', '10'].index(rank) + 2
        




cards = ['Т', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Д', 'В', 'К']
value = [get_value(rank) for rank in cards]
print(value)

value = {'Т': (1, 11), '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Д': 10, 'В': 10, 'К':10}
