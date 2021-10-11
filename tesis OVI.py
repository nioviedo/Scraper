from bs4 import BeautifulSoup
import xlsxwriter
import urllib.request as ur

#       browser = Browser('chrome')
#       browser.visit('http://www.espaciovino.com.ar/vinos-ficha/Escorihuela-Gascon-Sangiovese')

def vinos(worksheet):


        
         #vino de Winery.
        page = ur.urlopen('http://www.winery.com.ar/escorihuela-gascon-sangiovese.html')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.div.findAll("span",{"class":'price'})

        #Precio cosa 0 .string
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(1,0,"Winery")
                worksheet.write(1,1,cosa[0].string)
               


        #Vino de TONELPRIVADO
        page = ur.urlopen('http://www.tonelprivado.com/vinos-tintos-escorihuela-gascon-sangiovese-750-ml-111227/p')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("strong", {"class":"skuBestPrice"})
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(2,0,"Tonel Privado")
                worksheet.write(2,1,cosa[0].string)
                

        #Vino de espacioVino
        page = ur.urlopen("http://www.espaciovino.com.ar/vinos-ficha/Escorihuela-Gascon-Sangiovese")
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("span", {"class":"product-price"})
        if cosa != []:
                cosa = cosa[0].stripped_strings
                worksheet.write(3,0,"Tonel Privado")
                
                for i in cosa:
                        print(i)
                        worksheet.write(3,1,i)

def cervezas(worksheet):           


        #Bodegacervezas
        page = ur.urlopen('http://www.bodegadecervezas.com/las-rubias/cerveza-artesanal-antares-kolsch/')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("span", {"class":"price"})
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(5, 0, "Bodega Cervezas")
                worksheet.write(5,1,cosa[0].string)

        #Bevybar
        page = ur.urlopen('https://www.bevybar.com.ar/products/antares-kolsch')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("div", {"class":"variant-price"})
        if cosa != []:
                
                
                worksheet.write(6, 0, "BevyBar")
                worksheet.write(6,1,cosa[0].string)

                print(cosa[0].string)

        #Lamembresia
        page = ur.urlopen('http://www.lamembresia.com.ar/producto/antareskolsch/')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("span", {"class":"amount"})
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(7, 0, "Lamembresia")
                worksheet.write(7,1,cosa[0].string)




def tv(worksheet):


        #Garbarino
        page = ur.urlopen('https://www.garbarino.com/producto/smart-tv-samsung-50-full-hd-un50j5300agcdf/5f89ee3623')
 
                
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("div", {"class":"gb-main-detail-prices-current", "id":"final-price"})

        if cosa != []:
                cosa = cosa[0].stripped_strings
                worksheet.write(9, 0, "Garbarino")
                for i in cosa:
                        print(i)
                        worksheet.write(9, 1, i)

               

        
        #Avenida
        page = ur.urlopen('https://producto.avenida.com.ar/smart-tv-50-samsung-full-hd-hdmi-x2-50j5300ag')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("span", {"class":"publication-price"})
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(10, 0, "Avenida")
                worksheet.write(10,1,cosa[0].string)


        #Fravega
        page = ur.urlopen('http://www.fravega.com/smart-tv-samsung-50-un50j5300-501285/p')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("strong", {"class":"skuBestPrice"})
        if cosa != []:
                print(cosa[0].string)
                worksheet.write(11, 0, "Fravega")
                worksheet.write(11,1,cosa[0].string)


'''
def libros():

        page = ur.urlopen('https://www.walmart.com/ip/Harry-Potter-and-the-Cursed-Child-Parts-One-and-Two-The-Official-Script-Book-of-the-Original-West-End-Production-Special-Rehearsal-Edition/49838462')
        page = page.read()
        soup = BeautifulSoup(page, "html.parser")
        soup.prettify()
        cosa = soup.body.findAll("div", {"itemprop":"price"})

        print(a.string)
'''

def main():
        var = input("Escribi el nombre que queres para el excel")
        var = var + ".xlsx"
        workbook = xlsxwriter.Workbook(var)
        worksheet = workbook.add_worksheet()

        worksheet.write(0, 0, "Vinos")
        vinos(worksheet)
        worksheet.write(4, 0, "Cervezas")
        cervezas(worksheet)
        worksheet.write(8, 0, "TV")
        tv(worksheet)
        
        
        workbook.close()
        
main()


        
