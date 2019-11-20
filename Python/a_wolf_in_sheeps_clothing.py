def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if queue.index('wolf') == len(queue) - 1 else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(len(queue) - queue.index('wolf') - 1)
print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))