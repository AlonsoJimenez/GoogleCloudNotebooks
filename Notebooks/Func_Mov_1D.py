from IPython.display import HTML
from IPython.display import display

# Tomado de https://stackoverflow.com/questions/31517194/how-to-hide-one-specific-cell-input-or-output-in-ipython-notebook
tag = HTML('''<script>
code_show=false; 
function code_toggle() {
    if (code_show){
        $('div.cell.code_cell.rendered.selected div.input').hide();
    } else {
        $('div.cell.code_cell.rendered.selected div.input').show();
    }
    code_show = !code_show
} 

$( document ).ready(code_toggle);
</script>

Para mostrar/ocultar código presione <a href="javascript:code_toggle()">aquí</a>.''')


###########################################################################################################################


from ipywidgets import interactive
import ipywidgets as widgets
from IPython.display import display 
import numpy as np
import matplotlib.pyplot as plt


def CalculoVelocidad (arregloTiempo, velInicial, aceleración):
    velocidad = velInicial + aceleración * arregloTiempo
    return velocidad

def CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración):
    posición = posInicial + velInicial * arregloTiempo + 1/2 * aceleración * arregloTiempo ** 2
    return posición


def Rapidez():
#     print('Instrucciones')
    display(tag)    
   

    def GraficoInteractivoVelocidad (velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 100)

      velocidadActual = CalculoVelocidad (arregloTiempo, velInicial, aceleración)

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Rapidez $(m/s)$')
      plt.xlim (0, 40)
      plt.ylim (-50, 50)
      ax.plot(arregloTiempo, velocidadActual, lw=3)
      ax.set_title('Rapidez de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return

#     instruccionesEtiqueta = widgets.Label(value="Instrucciones: \nAjuste los valores de rapidez inicial y aceleración.\nPresione \"PLAY\" para generar la gráfica de rapidez")
#     cajaInstrucciones = widgets.HBox([instruccionesEtiqueta])
        
    velEtiqueta = widgets.Label (value="Rapidez Inicial $(m/s)$:")
    velSlider = widgets.IntSlider(min=-50.0, max=50.0, step=1.0, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-5, max=5, step=0.5, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=40, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=40,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoVelocidad, {'velInicial':velSlider, 
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)
    


###########################################################################################################################


def Posición():
    
    display(tag)

    def GraficoInteractivoPosición(posInicial, velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 100)

      posiciónActual = CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración)

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Posición $(m)$')
      plt.xlim (0, 40)
      plt.ylim (-30, 70)
      ax.plot(arregloTiempo, posiciónActual, lw=4)
      ax.set_title('Posición de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-30.0, max=70.0, step=1.0, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Rapidez Inicial $(m/s)$:")
    velSlider = widgets.FloatSlider(min=-10, max=10, step=0.5, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-0.5, max=0.5, step=0.01, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=40, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=40,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoPosición, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)


###########################################################################################################################


def Aceleración ():
    
    display(tag)
    
    def GraficoInteractivoPosición(posInicial, velInicial, aceleración,tiempo):
      arregloTiempo = np.linspace(0, tiempo, 100)
      aceleraciónActual = np.ones(100) * aceleración    

      fig, ax = plt.subplots (dpi=120)

      ax.set_xlabel('Tiempo $(s)$')
      ax.set_ylabel('Aceleración $(m/s^2)$')
      plt.xlim (0, 40)
      plt.ylim (-10, 10)
      ax.plot(arregloTiempo, aceleraciónActual, lw=3)
      ax.set_title('Aceleración de una partícula en una dimensión')

      plt.grid ()

      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-10.0, max=10.0, step=1, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Rapidez Inicial $(m/s)$:")
    velSlider = widgets.IntSlider(min=-10, max=10, step=1, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.IntSlider(min=-10.0, max=10.0, step=1, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=40, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=40,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoPosición, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)
    
    
###########################################################################################################################


def GraficasVarias ():
    
    display (tag)
    
    def GraficoInteractivoGeneral(posInicial, velInicial, aceleración,tiempo):

      arregloTiempo = np.linspace (0, tiempo, 100)

      posiciónActual = CalculoPosición (posInicial, arregloTiempo, velInicial, aceleración)
      velocidadActual = CalculoVelocidad (arregloTiempo, velInicial, aceleración)
      aceleraciónActual = np.ones (100) * aceleración

      fig, (ax1, ax2, ax3) = plt.subplots (1, 3, figsize = (20,7), dpi= 120, sharex = True)

      ax1.set_xlabel('Tiempo $(s)$')
      ax1.set_ylabel('Posición $(m)$')
      ax1.plot (arregloTiempo, posiciónActual, lw=3)
      ax1.set_xlim([0,40]) 
      ax1.set_ylim([-25,25])      
      ax1.grid ()
        
      ax2.set_xlabel('Tiempo $(s)$')
      ax2.set_ylabel('Rapidez $(m/s)$')
      ax2.plot (arregloTiempo, velocidadActual, lw=3) 
      ax2.set_xlim([0,40])
      ax2.set_ylim([-2.5,2.5]) 
      ax2.grid ()
    
      ax3.set_xlabel('Tiempo $(s)$')
      ax3.set_ylabel('Aceleración $(m/s^2)$')
      ax1.set_xlim([0,40])
      ax3.set_ylim([-0.35, 0.35]) 
      ax3.plot (arregloTiempo, aceleraciónActual, lw=3)        
      ax3.grid ()
    
      plt.show()

      return


    posEtiqueta = widgets.Label (value="Posición Inicial $(m)$:")
    posSlider = widgets.IntSlider(min=-20.0, max=20.0, step=1.0, value=0.0)
    cajaPosición = widgets.HBox([posEtiqueta, posSlider])

    velEtiqueta = widgets.Label (value="Rapidez Inicial $(m/s)$:")
    velSlider = widgets.FloatSlider(min=-2, max=2, step=0.05, value=0.0)
    cajaVelocidad = widgets.HBox([velEtiqueta, velSlider])

    aceEtiqueta = widgets.Label (value="Aceleración $(m/s^2)$:")
    aceSlider = widgets.FloatSlider(min=-0.3, max=0.3, step=0.01, value=0)
    cajaAceleracion = widgets.HBox([aceEtiqueta, aceSlider])

    play = widgets.Play(value=0, min=0, max=40, step=2, disabled=False)
    tieEtiqueta = widgets.Label (value="Tiempo $(s)$:")
    tieSlider = widgets.IntSlider(min=0, max=40,)
    widgets.jslink((play, 'value'), (tieSlider, 'value'))
    cajaTiempo = widgets.HBox([tieEtiqueta, tieSlider])

    salida = widgets.interactive_output(GraficoInteractivoGeneral, {'posInicial':posSlider,
                                                                  'velInicial':velSlider,
                                                                  'aceleración':aceSlider,
                                                                  'tiempo':tieSlider})

    display(cajaPosición, cajaVelocidad, cajaAceleracion, cajaTiempo, play, salida)