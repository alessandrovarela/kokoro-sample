# Kokoro TTS Sample - Streaming Real

Este repositório demonstra como implementar **streaming real** e **processamento em lote** usando o **Kokoro TTS**, um modelo de síntese de fala leve e eficiente com 82 milhões de parâmetros.

## 🚀 Instalação

### 1. Clonar o repositório
```bash
git clone https://github.com/alessandrovarela/kokoro-sample
cd kokoro-sample
```

### 2. Pré-requisitos

1. **Instalar uv** (gerenciador de pacotes Python):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Instalar espeak-ng** (necessário para síntese de fala):

**macOS:**
```bash
brew install espeak-ng
```

**Linux:**
```bash
apt-get -qq -y install espeak-ng
```

**Windows:**
- Vá para [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases)
- Clique em "Latest release"
- Baixe o arquivo *.msi apropriado
- Execute o instalador baixado

### 3. Instalar dependências do projeto
```bash
uv sync
```

## 📁 Scripts Disponíveis

### 1. kokoro_batch.py

Script para **processamento em lote** - gera arquivo de áudio completo.

**Funcionalidades:**
- Processa todo o texto de uma vez
- Concatena todos os chunks de áudio
- Salva arquivo .wav único
- Melhor para textos longos e arquivos finais

**Como usar:**
```bash
python kokoro_batch.py
```

**Saída:**
- `output.wav` - Arquivo de áudio com todo o texto processado

### 2. kokoro_stream.py

Script de **streaming real** usando pygame com sistema de filas.

**Funcionalidades:**
- ✅ **Streaming real** - geração e reprodução em paralelo
- ✅ **Sem sobreposição** - chunks tocam sequencialmente 
- ✅ **Sem pausas** - transições suaves entre chunks
- ✅ **Arquitetura producer-consumer** com threading
- ✅ **Fila thread-safe** para coordenação

**Como usar:**
```bash
python kokoro_stream.py
```

**Tecnologia:**
- **Pygame** para reprodução de áudio
- **Threading** para processamento paralelo
- **Queue** para sincronização entre threads
- **Buffer WAV** em memória para eficiência

## 🌍 Idiomas Suportados (lang_code)

```python
# 🇺🇸 'a' => American English
# 🇬🇧 'b' => British English  
# 🇪🇸 'e' => Spanish es
# 🇫🇷 'f' => French fr-fr
# 🇮🇳 'h' => Hindi hi
# 🇮🇹 'i' => Italian it
# 🇯🇵 'j' => Japanese (pip install misaki[ja])
# 🇧🇷 'p' => Brazilian Portuguese pt-br
# 🇨🇳 'z' => Mandarin Chinese (pip install misaki[zh])
```

## 🎤 Vozes Disponíveis

### Vozes Brasileiras (pt-br):
- `pf_dora` - Voz feminina brasileira (padrão neste projeto)
- `pm_alex` - Voz masculina brasileira 
- `pm_santa` - Voz masculina brasileira alternativa

### Outras vozes:
Você pode conferir todas as vozes disponíveis aqui:
**https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md**

## 🛠️ Dependências Principais

- `kokoro>=0.9.4` - Modelo TTS
- `pygame>=2.0.0` - Reprodução de áudio (streaming)
- `scipy>=1.9.0` - Processamento de arquivos WAV
- `numpy>=1.24.0` - Processamento de arrays
- `torch` - Framework de deep learning

## ⚡ Diferenças entre Batch vs Stream

| Característica | kokoro_batch.py | kokoro_stream.py |
|----------------|-----------------|------------------|
| **Processamento** | Lote completo | Chunk por chunk |
| **Latência** | Alta (espera tudo) | Baixa (inicia imediatamente) |
| **Memória** | Mais uso | Uso otimizado |
| **Uso ideal** | Arquivos finais | Aplicações real-time |
| **Interatividade** | Baixa | Alta |

## 🎯 Casos de Uso

### kokoro_batch.py
- **Geração de audiobooks**
- **Narração de documentos**
- **Processamento offline**
- **Arquivos de áudio finais**

### kokoro_stream.py
- **Assistentes virtuais em tempo real**
- **Chatbots com voz**
- **Aplicações interativas**
- **Streaming de conteúdo dinâmico**
- **Sistemas de resposta rápida**

## 🔧 Configurações

No código, você pode ajustar:

```python
# Trocar idioma
lang_code = 'p'  # português brasileiro

# Trocar voz
voice = 'pf_dora'  # voz feminina
# voice = 'pm_alex'  # voz masculina

# Velocidade da fala
speed = 1  # velocidade normal (0.5 = mais lento, 2 = mais rápido)
```

## 🔗 Links Úteis

- [Kokoro TTS no Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)
- [Lista completa de vozes](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md)
- [Documentação do Kokoro - Github](https://github.com/hexgrad/Kokoro)
- [Pygame Documentation](https://www.pygame.org/docs/)

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, especialmente:
- Otimizações de performance no streaming
- Suporte a mais formatos de áudio
- Interface gráfica para o streaming
- Exemplos com outras vozes e idiomas

## 📝 Licença

Este projeto é open source e está disponível sob a [MIT License](LICENSE).