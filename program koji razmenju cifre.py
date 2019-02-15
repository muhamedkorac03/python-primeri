broj = int(input('Unesite broj : '))
stotine = (broj // 100) % 10
hiljade = (broj // 1000) % 10
razmenjivanje_cifara= broj - stotine * 100 + hiljade * 100 - hiljade * 1000 + stotine * 1000
print('Razmenjenivanje cifara :', razmenjivanje_cifara)











