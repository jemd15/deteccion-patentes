import SimpleCV
display = SimpleCV.Display() #crear la ventana para mostrar la imagen
cam = SimpleCV.Camera(1) # inicializar la camara
normaldisplay = True # opción de mostrar solo un segmento de pantalla si es false 
while display.isNotDone(): # ciclo hasta que detengamos el programa 
    if display.mouseRight: # si el hacemos click derecho cambiar de modo
        normaldisplay = not(normaldisplay)
        print "Modo de Ventana:", "Normal" if normaldisplay else "Segmentado"
    img = cam.getImage().flipHorizontal() # obtenemos una imagen de la camara
    if normaldisplay: # si esta en modo normal
        img.show() #mostrar la imagen
    else: # modo segmentado
        segmented.show() #mostrar la imagen
