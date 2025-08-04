from kokoro import KPipeline
import numpy as np
import pygame
import io
import scipy.io.wavfile as wavfile
import queue
import threading

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
    """Streaming real usando pygame com fila - evita sobreposição"""
    pygame.mixer.pre_init(frequency=24000, size=-16, channels=1, buffer=512)
    pygame.mixer.init()
    
    print("Iniciando streaming REAL do Kokoro com fila...")
    
    # Fila para armazenar chunks de áudio
    audio_queue = queue.Queue()
    
    def producer():
        """Produz chunks de áudio e coloca na fila"""
        generator = pipeline(text=text, voice=voice, speed=1)
        
        for i, (gs, ps, audio) in enumerate(generator):
            print(f'Produzindo chunk {i + 1}... {gs} {ps}')
            
            # Convert tensor to numpy array
            audio_numpy = audio.numpy() if hasattr(audio, 'numpy') else audio.cpu().numpy()
            
            # Convert to 16-bit PCM
            audio_int16 = (audio_numpy * 32767).astype(np.int16)
            
            # Create a WAV buffer in memory
            buffer = io.BytesIO()
            wavfile.write(buffer, 24000, audio_int16)
            buffer.seek(0)
            
            # Adiciona o buffer na fila
            audio_queue.put(buffer)
        
        # Sinaliza fim da produção
        audio_queue.put(None)
    
    def consumer():
        """Consome chunks da fila e reproduz sequencialmente"""
        chunk_num = 0
        while True:
            try:
                # Pega próximo chunk da fila
                buffer = audio_queue.get(timeout=10)
                
                if buffer is None:  # Fim da produção
                    break
                
                chunk_num += 1
                print(f'Reproduzindo chunk {chunk_num}...')
                
                # Load and play
                sound = pygame.mixer.Sound(buffer)
                sound.play()
                
                # Espera este chunk terminar antes do próximo
                while pygame.mixer.get_busy():
                    pygame.time.wait(10)
                
                audio_queue.task_done()
                
            except queue.Empty:
                print("Timeout na fila - finalizando...")
                break
    
    # Inicia produtor em thread separada
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()
    
    # Consumidor roda na thread principal
    consumer()
    
    # Espera produtor terminar
    producer_thread.join()
    
    pygame.mixer.quit()
    print("Streaming real concluído!")

if __name__ == "__main__":
    stream_kokoro()