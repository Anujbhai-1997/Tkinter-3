from tkinter import *
from tkinter import ttk

class mainApp(Tk):   #Hereda de Tk
    size = "1024x768"
    
    def __init__(self):   #Esto es una etiqueta que dice que es un método que se va a ejecutar cuando se inicialice la clase
        Tk.__init__(self)        
                
        #self.root = Tk()  #Cn TK init esto no lo necesito
    '''
        self.root.geometry(self.size)  #También se puede cambiar self.size directamente por "640x480"
        self.root.title("Mi ventana")
        self.root.configure(bg = "blue")
    '''  
    #Ahora yo soy la ventana y me hablo a mi mismo, por lo que elimino la referencia externa root
        self.geometry(self.size)  #También se puede cambiar self.size directamente por "640x480"
        self.title("Mi ventana")
        self.configure(bg = "blue")
        
        
    def start(self):
        self.root.mainloop()  #Loop de interfaz gráfica
    
if __name__ == '__main__':
    app = mainApp()
    
    app.start()
    
    
ttk.Button
ttk.Radiobutton
ttk.Entry
   
    
    
    
    