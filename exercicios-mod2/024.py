cidade = str(input('Em qual cidade vc nasceu?\n')).strip()

if cidade[:5].lower() == 'santo':
    print(True)
else: print(False)