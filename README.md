# Offline Smart Home

An offline voice-controlled smart home assistant that supports Tamil–English mixed commands without using the internet. The system focuses on privacy, low latency, and local speech processing by combining deep learning and lightweight offline speech recognition.

## Features
- Fully offline voice recognition
- Tamil + English code-mixed command support
- Hybrid CRNN and PocketSphinx architecture
- Low-latency command execution
- No cloud services or internet dependency
- Privacy-preserving local processing

## System Architecture
Microphone Input  
→ Speech Recognition (CRNN + PocketSphinx)  
→ Intent Matching (Command Corpus)  
→ Action Execution (Home Automation Simulation)

## Technologies Used
- Python 3.10
- TensorFlow
- PocketSphinx
- SpeechRecognition
- pyttsx3

## Speech Recognition Method
### CRNN
- Uses MFCC features from speech audio
- CNN layers extract spatial features
- LSTM layers capture temporal patterns
- Trained on a Tamil–English speech subset

### PocketSphinx
- Lightweight offline speech recognition engine
- Custom grammar (.gram) and dictionary (.dict)
- Fast recognition for predefined commands

## Example Commands
- vilakku on pannu
- fan off
- light off pannu
- switch on motor

## Performance
PocketSphinx provides fast responses (~0.5s) for common commands.  
CRNN provides higher accuracy (~1.8s) for complex or unclear inputs.

## Privacy
- No internet connection required
- No cloud storage
- All audio processing is local

## Future Scope
- Real IoT device integration
- Additional language support
- Expanded command corpus
- Improved noise handling


