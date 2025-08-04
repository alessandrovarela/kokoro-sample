from kokoro import KPipeline
import simpleaudio as sa
import numpy as np

lang_code = 'p'

pipeline = KPipeline(lang_code=lang_code)

text = '''
Olá! Este é um exemplo de uso básico do paipelaine Kokoro para síntese de voz.
Com o Kokoro, você pode gerar áudio de alta qualidade a partir de texto em português.
A biblioteca Kokoro é projetada para ser fácil de usar e eficiente, permitindo que você crie suas próprias aplicações de síntese de voz.
'''

voice = 'pf_dora'
#voice = 'pm_alex'
#voice = 'pm_santa'

def stream_kokoro():
    print("Iniciando streaming do Kokoro...")
    
    generator = pipeline(text=text, voice=voice, speed=1)
    
    for i, (gs, ps, audio) in enumerate(generator):
        print(f'Playing chunk {i + 1}... {gs} {ps}')
        # Convert tensor to numpy array first, then to 16-bit PCM
        audio_numpy = audio.numpy() if hasattr(audio, 'numpy') else audio.cpu().numpy()
        audio_int16 = (audio_numpy * 32767).astype(np.int16)
        play_obj = sa.play_buffer(audio_int16, 1, 2, 24000)
        play_obj.wait_done()
    
    print("Streaming concluído!")

if __name__ == "__main__":
    stream_kokoro()