from kokoro import KPipeline
import soundfile as sf
import numpy as np

lang_code = 'p'

pipeline = KPipeline(lang_code=lang_code)

text = '''
Olá! Este é um exemplo de uso básico do paipelaine Kokoro para síntese de voz.
Com o Kokoro, você pode gerar áudio de alta qualidade a partir de texto em português.
A biblioteca Kokoro é projetada para ser fácil de usar e eficiente, permitindo que você crie suas próprias aplicações de síntese de voz.
'''

#voice = 'pf_dora'
#voice = 'pm_alex'
voice = 'pm_santa'

generator = pipeline(text=text, voice=voice, speed=1)

audio_chunks = []
for i, (gs, ps, audio) in enumerate(generator):
    print(f'Processing chunk {i + 1}... {gs} {ps}')
    audio_chunks.append(audio)
    
if audio_chunks:
    full_audio = np.concatenate(audio_chunks).astype('float32')
    output_file = f'voice_{voice}.wav'
    sf.write(output_file, full_audio, 24000)
    print(f'Audio saved to {output_file}')