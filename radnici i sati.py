ceo_broj = int(input('Unesite broj : '))
stotine = ceo_broj // 100
desetice = (ceo_broj //10) % 10
jedinice = ceo_broj % 10
print(stotine,desetice,jedinice)


