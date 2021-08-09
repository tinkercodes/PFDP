from django.shortcuts import render
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
from scipy.io import wavfile as wav
import numpy as np
import urllib, io, base64
from pydub import AudioSegment

def demo(request):
    plt.close("all")
    if(request.method=='POST'):
        file=request.FILES['data']
        # plt=util.soundAnalyser(file)

        # src = file
        # # dst = "test.wav"

        # # convert wav to mp3                                                            
        # sound = AudioSegment.from_mp3(src)
        # sound.export(dst, format="wav")

        rate, data = wav.read(file)
        fft_out = fft(data)
        # %matplotlib inline
        plt.plot(data, np.abs(fft_out))

        # plt.plot(range(10))#this is a plot that i used for testing 
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string =base64.b64encode(buf.read())
        uri=urllib.parse.quote(string)
        print(uri)
        return render(request,'home/demo.html',{'data':uri})
        
    else:
        return render(request,'home/demo.html',{'data':None})

def about(request):
    return render(request,'home/about.html',{'data':None})

def home(request):
    return render(request,'home/form.html',{'data':None})