times = ['são paulo', 'palmeiras', 'santos', 'corinthians', 'portuguesa']

outros_times = times[:]

for time in times:
    print(f"O {time.title()} é um dos meus times favoritos!")

outros_times.append('ponte-preta')
outros_times.append('guarani')

for time in outros_times:
    print(f"Já este time {time.title()}, é um dos meus favoritos")