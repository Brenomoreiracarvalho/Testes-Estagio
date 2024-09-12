sp = 67836.43
rj = 36678.66
mg = 27165.48
outros = 19849.53

total = sp + rj + mg + outros

percSp = (sp/total)*100
percRj = (rj/total)*100
percMg = (mg/total)*100
percOutros = (outros/total)*100

print('O percentual de cada Estado segue abaixo')
print(f'• SP - {percSp:.2f}%')
print(f'• RJ - {percRj:.2f}%')
print(f'• MG - {percMg:.2f}%')
print(f'• Outros - {percOutros:.2f}%')