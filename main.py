import sys
import pdfx

if len(sys.argv)-1 < 1:
    print('Necesito el fichero pdf como parámetro')
    exit(1)

for pdffile in sys.argv[1:]:
    print('Procesamos', pdffile)

pdf = pdfx.PDFx(pdffile)
metadata = pdf.get_metadata()
references_list = pdf.get_references()
references_dict = pdf.get_references_as_dict()

#print(pdf.summary)

print ('Listamos referencias')
for reference in references_list:
    print(reference)

print ('Listamos referencias dict')
for reference in references_dict:
    print ('Referencia: ' , reference)
    counter = 1
    for listurls in references_dict[reference]:
        print(counter, '>' , listurls)
        counter += 1