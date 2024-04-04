models = ['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500']
available = [1, 1, 1, 1, 0, 1, 1, 0]
manufacturers = ['Intel', 'Samsung', 'WD']
repair_count = 0 # количество дисков, которые купит сисадмин
ssds = [] # модели дисков из списка models, которые купит сисадмин
    # код вашего решения ниже:

for manufacturer in manufacturers:
    for model_, avai_ in zip(models, available):
        if avai_ == 1 and manufacturer in model_:
            repair_count += 1
            ssds.append(model_)
print(repair_count)            
print(ssds)